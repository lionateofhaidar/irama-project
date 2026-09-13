##  Diagram alur fitur utama dan pemetaannya ke arsitektur dan tahap

Diagram berikut menggambarkan cara IRAMA bekerja pada kondisi end-state, satu diagram per fitur utama. Cara membacanya sama untuk semua diagram.

- Baris (lajur mendatar) adalah lapisan arsitektur: pengguna dan mitra eksternal, penyajian, pusat, komunikasi dan integrasi, lapangan. Posisi kotak menunjukkan komponen mana yang menjalankan langkah itu.
- Kotak adalah langkah, diberi huruf urut dan warna bingkai. Label kecil di pojok kanan atas (T1 sampai T5) menandai tahap saat langkah itu pertama tersedia. Warna: T1 hijau, T2 biru, T3 jingga, T4 ungu, T5 merah.
- Panah adalah aliran data atau perintah. Label pada panah menjelaskan kondisi, misalnya "bila putus".
- Untuk membaca diagram pada tahap tertentu, abaikan kotak yang labelnya lebih tinggi dari tahap itu. Contoh: pada T2, kotak berlabel T3 sampai T5 belum ada, dan alur berhenti pada kotak terakhir yang tersedia.

Tabel di bawah tiap diagram memetakan langkah ke komponen dalam struktur repositori (apps, services, edge, sim, infra) dan tahapnya.

### F00 Gambaran keseluruhan komponen per lapisan dan tahap

![F00](diagram/F00_Gambaran_Keseluruhan.png)

Diagram ini memperlihatkan semua komponen yang ada pada end-state, dikelompokkan per lapisan, dengan label tahap pemunculannya. Diagram F01 sampai F12 memperlihatkan bagaimana komponen tersebut bekerja sama untuk tiap fitur.

### F01 Pemantauan status simpang secara langsung

Operator ruang kendali melihat kondisi setiap simpang (mode kendali, lampu yang menyala, detektor, alarm) dengan jeda paling lama lima detik. Pada T1 lampu sungguhan digantikan simulator; mulai T2 data datang dari controller di kabinet.

![F01](diagram/F01_Pemantauan_status_simpang_secara_langsun.png)

Tahap yang terlibat: T1, T2. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Simulator SUMO berperan sebagai controller | Lapangan | sim/, services/cai (adaptor TraCI) | T1 |
| b. Controller melaporkan status lampu dan detektor tiap detik | Lapangan | controller vendor/NTCIP | T2 |
| c. Agen edge menerjemahkan protokol vendor, menyimpan data bila jaringan putus | Lapangan | edge/ (edge-light) | T2 |
| d. Jaringan Dishub (fiber/4G) lewat VPN, pesan MQTT | Komunikasi | infra/ (MQTT, WireGuard) | T2 |
| e. Layanan status menerima dan menyimpan potret status | Pusat | apps/api, TimescaleDB | T1 |
| f. Mesin aturan menandai anomali (offline, kedip, konflik, jam melenceng) | Pusat | services/health | T2 |
| g. Peta simpang dan tampilan fase langsung di konsol | Penyajian | apps/tmc-web (MapLibre) | T1 |
| h. Operator memantau; pimpinan dan publik melihat ringkasan | Pengguna | dashboard publik | T2 |

### F02 Perencanaan dan penetapan jadwal lampu

Perencana menyusun jadwal lampu (fase, lama hijau, offset) berdasarkan data survei, memeriksanya dengan kalkulator dan validator, mengujinya di simulator, lalu mengirimkannya ke controller setelah disetujui pejabat yang berwenang.

![F02](diagram/F02_Perencanaan_dan_penetapan_jadwal_lampu.png)

Tahap yang terlibat: T1, T2. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Perencana memasukkan data survei, geometri, dan arus | Pengguna | apps/tmc-web | T1 |
| b. Kalkulator PKJI 2023: kapasitas, antrian, tundaan, kelas LOS | Pusat | services/kpi-pkji | T1 |
| c. Editor jadwal (fase, hijau, offset); minimal delapan jadwal per simpang | Penyajian | apps/tmc-web | T1 |
| d. Validator keselamatan (kuning, merah semua, hijau minimum) dan konsistensi urutan fase | Pusat | services/kpi-pkji | T1 |
| e. Uji di digital twin SUMO; laporan hasil (wajib sebelum penetapan mulai T3) | Pusat | sim/, services/twin | T1 |
| f. Persetujuan Kepala Dinas; Dirjen/BPTJ bila simpang di jalan nasional | Pengguna | alur persetujuan | T2 |
| g. Transaksi unduh jadwal tervalidasi; versi dan jejak audit | Pusat | services/cai | T2 |
| h. Controller menerima jadwal baru; jadwal lokal ikut diperbarui | Lapangan | controller, edge/ | T2 |

### F03 Kendali terpusat, mode manual petugas, dan cadangan saat putus

Operator atau petugas Polri memilih program atau mode manual dari ruang kendali. Pusat mengirim perintah terbatas beserta detak jantung. Bila jaringan putus, controller kembali ke jadwal lokal dan semua kejadian tetap tercatat.

![F03](diagram/F03_Kendali_terpusat.png)

Tahap yang terlibat: T2. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Operator atau petugas Polri memilih program, kedip, atau mode manual | Pengguna | konsol operator | T2 |
| b. Konsol kendali meminta konfirmasi dan alasan | Penyajian | apps/tmc-web | T2 |
| c. Layanan perintah memeriksa hak akses, mengirim perintah tipe C dan detak jantung | Pusat | services/cai | T2 |
| d. SNMP/MQTT lewat VPN | Komunikasi | infra/ | T2 |
| e. Controller menjalankan program; edge meneruskan detak jantung | Lapangan | controller, edge/ | T2 |
| f. Jaringan putus: controller kembali ke jadwal lokal; edge menyimpan catatan | Lapangan | controller (backup timer), edge/ | T2 |
| g. Jejak audit perintah dan KPI transisi; alarm bila cadangan aktif | Pusat | audit log, services/health | T2 |

### F04 Kesehatan perangkat, alarm, tiket kerja, dan pemeliharaan

Kerusakan detektor, kamera, controller, atau jaringan terdeteksi otomatis, diprioritaskan, lalu menjadi tiket kerja untuk teknisi. Jadwal pemeliharaan berkala dan umur teknis aset dijaga sesuai PM 49/2014.

![F04](diagram/F04_Kesehatan_perangkat.png)

Tahap yang terlibat: T1, T2. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Alarm controller dan detektor; pintu kabinet; catu daya | Lapangan | controller, edge/ | T2 |
| b. Watchdog harian dari catatan kejadian (detektor diam, max-out dini hari) | Pusat | services/atspm | T2 |
| c. Mesin alarm: prioritas, eskalasi, notifikasi ke Polri bila APILL mati | Pusat | services/health | T2 |
| d. Email/WhatsApp; API CRM kota | Komunikasi | infra/, integrasi CRM | T2 |
| e. Tiket kerja otomatis dengan SLA dan pencatatan waktu perbaikan | Pusat | services/ticket | T2 |
| f. Aplikasi ponsel teknisi: tiket, checklist, foto, bisa offline | Penyajian | apps/tmc-web (PWA) | T2 |
| g. Jadwal pemeliharaan enam bulanan, umur teknis lima tahun, penilaian aset | Pusat | apps/api (inventory) | T1 |
| h. Kepala Dinas melihat KPI kesehatan perangkat dan biaya | Pengguna | dashboard pimpinan | T2 |

### F05 Pengukuran kinerja dan laporan wajib

Catatan kejadian resolusi tinggi dari controller, edge, atau simulator diolah menjadi ukuran kinerja sinyal, KPI resmi (PKJI, LOS PM 96/2015), dan laporan yang wajib disampaikan ke Forum LLAJ, Dirjen/BPTJ, dan Gubernur.

![F05](diagram/F05_Pengukuran_kinerja_dan_laporan_wajib.png)

Tahap yang terlibat: T1, T2. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Catatan kejadian 0,1 detik dari controller, edge, atau simulator | Lapangan | controller/edge/sim | T1 |
| b. Dikirim berkala dalam paket lewat MQTT | Komunikasi | infra/ | T2 |
| c. Ingest dan simpan: rinci 90 hari, ringkasan 15 menit selama 5 tahun | Pusat | services/atspm, TimescaleDB | T1 |
| d. Mesin ATSPM: terminasi fase, split failure, arrivals on green, diagram koordinasi | Pusat | services/atspm | T1 |
| e. KPI PKJI dan LOS PM 96; perbandingan sebelum-sesudah dan hidup-mati | Pusat | services/kpi-pkji | T1 |
| f. Generator laporan: Forum LLAJ, Dirjen/BPTJ, Gubernur triwulanan | Pusat | services/reports | T2 |
| g. Dashboard pimpinan dan engineer; dashboard publik dengan metode terbuka | Penyajian | apps/tmc-web | T2 |
| h. Pejabat, DPRD, Forum LLAJ, warga | Pengguna | (pihak luar) | T2 |

### F06 Deteksi berbasis kamera dan detektor virtual

Kamera yang sudah ada diolah di kotak edge AI menjadi angka jumlah kendaraan, okupansi, dan panjang antrian, serta pembacaan pelat untuk bukti dan prioritas. Hanya angka ringkasan yang dikirim ke pusat; data pelat tunduk pada tata kelola perlindungan data pribadi.

![F06](diagram/F06_Deteksi_berbasis_kamera_dan_detektor_vir.png)

Tahap yang terlibat: T2, T3. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Kamera CCTV (RTSP) atau kamera analitik vendor | Lapangan | kamera eksisting | T2 |
| b. Edge AI: hitung kendaraan, okupansi, antrian; baca pelat (disamarkan) | Lapangan | edge/ (Jetson, YOLO, OCR) | T3 |
| c. Pemeriksaan kualitas deteksi (malam, hujan); turun otomatis bila buruk | Lapangan | edge/ health | T3 |
| d. Kirim angka ringkasan lewat MQTT, tanpa video | Komunikasi | infra/ | T3 |
| e. Detektor virtual menjadi catatan kejadian dan masukan kendali | Pusat | services/cai, services/atspm | T3 |
| f. Tata kelola PDP: dasar hukum, retensi pelat singkat, akses terbatas, DPIA | Pusat | keamanan & kepatuhan | T3 |
| g. Tampilan kamera langsung (WebRTC) dengan lapisan hitungan | Penyajian | apps/tmc-web, gerbang video | T2 |
| h. Operator ruang kendali; pejabat perlindungan data | Pengguna | (pihak luar) | T3 |

### F07 Kendali responsif dan adaptif

Data detektor dipakai untuk memilih program dan menala offset secara otomatis (T3), lalu membagi ulang waktu hijau setiap siklus dan mengendalikan perimeter kawasan jenuh (T4). Mode bayangan dan ukuran kinerja independen memastikan setiap algoritma terbukti sebelum mengendalikan lampu.

![F07](diagram/F07_Kendali_responsif_dan_adaptif.png)

Tahap yang terlibat: T3, T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Detektor (virtual, loop, radar) melaporkan okupansi dan antrian | Lapangan | edge/, controller | T3 |
| b. Gerbang kesehatan: adaptif hanya bila detektor sehat | Pusat | services/adaptive | T3 |
| c. Pemilihan program otomatis dan penalaan offset koridor (Link Pivot, data GPS) | Pusat | services/adaptive (TRPS), services/atspm | T3 |
| d. Cyclic max-pressure membagi hijau tiap siklus, perubahan maksimal lima detik | Pusat | services/adaptive | T4 |
| e. Pengendalian perimeter kawasan pusat kota saat jenuh | Pusat | services/adaptive | T4 |
| f. Mode bayangan dan ATSPM sebagai pengamat independen | Pusat | shadow harness, services/atspm | T3 |
| g. Perintah split/program lewat antarmuka controller | Komunikasi | services/cai, MQTT | T3 |
| h. Controller menjalankan; jadwal lokal tetap sebagai cadangan | Lapangan | controller | T3 |
| i. Konsol adaptif: parameter, keputusan, dan nilai antara yang bisa dijelaskan | Penyajian | apps/tmc-web | T4 |

### F08 Prioritas bus dan kendaraan darurat

Permintaan prioritas datang dari sistem pelacakan bus dan pusat komando pemadam atau ambulans. Layanan prioritas menilai kelayakan, menjaga batas keselamatan, lalu memberi hijau tambahan atau preemption melalui controller, dan mencatat dampaknya.

![F08](diagram/F08_Prioritas_bus_dan_kendaraan_darurat.png)

Tahap yang terlibat: T3, T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. AVL/APC operator bus; CAD pemadam dan ambulans | Pengguna | operator bus, 112/119 | T3 |
| b. API mitra sesuai dokumen antarmuka; MoU digital detik prioritas | Komunikasi | integrasi (ICD) | T3 |
| c. Layanan permintaan prioritas: kelayakan (terlambat, muatan), antrian permintaan | Pusat | services/priority | T3 |
| d. Prioritas bersyarat (OCC/Transit-MP) dan darurat bertingkat dengan penyelesaian konflik | Pusat | services/priority | T4 |
| e. Batas: pejalan kaki tidak dipotong, satu aktivasi per siklus, jeda, pemulihan koordinasi | Pusat | services/priority | T3 |
| f. Perintah tahan, perpanjang, atau preempt ke controller | Komunikasi | services/cai | T3 |
| g. Controller memberi hijau tambahan atau preempt; check-out geofence mengakhiri | Lapangan | controller, edge/ | T3 |
| h. Konsol prioritas: permintaan, dilayani/ditolak, dampak jalan samping | Penyajian | apps/tmc-web | T3 |
| i. Log dan KPI: waktu tempuh bus, waktu tanggap darurat | Pusat | services/atspm | T3 |

### F09 Bukti pelanggaran untuk ETLE Polri

Sistem hanya menyediakan bukti. Edge AI mendeteksi pelanggaran seperti menerobos merah, pusat menyusun paket bukti dengan kontrol perlindungan data, lalu mengirimkannya ke Back Office ETLE Polri untuk diverifikasi dan ditindak oleh petugas.

![F09](diagram/F09_Bukti_pelanggaran_untuk_ETLE_Polri.png)

Tahap yang terlibat: T3, T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Edge AI mendeteksi terobos merah (aktuasi saat kuning/merah) dan pelat | Lapangan | edge/, services/atspm (YRA) | T3 |
| b. Paket bukti: foto/klip 30 detik, pelat terenkripsi, waktu, lokasi | Pusat | services/evidence, object store | T3 |
| c. Kontrol PDP dan DPIA; retensi bukti sesuai alur Perpol 2/2025 | Pusat | keamanan & kepatuhan | T3 |
| d. API ke Back Office ETLE Polda sesuai Perpol 8/2023 | Komunikasi | integrasi (ICD Polri) | T4 |
| e. Petugas Polri memverifikasi dan menindak; aplikasi tidak menerbitkan tilang | Pengguna | Polri | T4 |
| f. Status tindak lanjut hanya-baca; laporan integrasi tahunan | Pusat | services/evidence | T4 |
| g. Dashboard keselamatan: pelanggaran per simpang, tren | Penyajian | apps/tmc-web | T3 |

### F10 Keluhan publik dan jaminan layanan

Laporan warga masuk lewat aplikasi kota atau CRM, menjadi tiket dengan target waktu penyelesaian, dan didiagnosis dengan data kinerja sinyal termasuk pemutaran ulang kejadian. Jawaban dan status dikembalikan ke pelapor.

![F10](diagram/F10_Keluhan_publik_dan_jaminan_layanan.png)

Tahap yang terlibat: T2, T3. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Warga melapor lewat aplikasi kota, CRM, atau telepon | Pengguna | CRM kota | T2 |
| b. API CRM dua arah | Komunikasi | integrasi CRM | T2 |
| c. Tiket tujuh langkah, klasifikasi, target penyelesaian tiga jam | Pusat | services/ticket | T2 |
| d. Matriks diagnosis: jenis keluhan dipetakan ke data ATSPM terkait | Pusat | services/atspm | T2 |
| e. Pemutaran ulang kejadian historis (status lampu dan detektor saat keluhan) | Pusat | services/atspm, TimescaleDB | T3 |
| f. Operator menindaklanjuti; tiket kerja ke teknisi bila perlu | Penyajian | apps/tmc-web | T2 |
| g. Jawaban ke pelapor; status dapat dilihat publik | Pengguna | CRM kota, dashboard publik | T2 |

### F11 Digital twin, mode bayangan, dan marketplace algoritma

Setiap jadwal atau algoritma baru diuji dulu di simulator yang dikalibrasi dengan data kota, lalu dijalankan dalam mode bayangan dengan data hidup tanpa mengendalikan lampu, dan baru dipromosikan bertahap ke jam sepi dan jam sibuk. Pada T5 pihak ketiga dapat mengajukan algoritma lewat jalur yang sama.

![F11](diagram/F11_Digital_twin.png)

Tahap yang terlibat: T1, T3, T4, T5. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Generator jaringan simulasi dari registri simpang dan peta OSM | Pusat | sim/ | T1 |
| b. Kalibrasi twin per koridor dengan data hitungan dan GPS | Pusat | sim/, services/twin | T3 |
| c. Skenario: jadwal baru, insiden, acara; kebijakan TDM skala kota (T5) | Pusat | services/twin | T3 |
| d. Pekerja simulasi menjalankan; hasil MoE dan catatan kejadian | Pusat | sim/ worker | T3 |
| e. Mode bayangan: algoritma menerima data hidup, keputusan dicatat, tidak dikirim | Pusat | shadow harness | T3 |
| f. Veto statistik dan uji konflik prioritas | Pusat | services/adaptive | T4 |
| g. Universitas atau vendor mengajukan algoritma (marketplace) | Pengguna | portal mitra | T5 |
| h. Promosi bertahap: jam sepi, jam sibuk, perbandingan hidup-mati | Pusat | services/adaptive | T3 |
| i. Laporan divergensi dan keputusan lanjut atau berhenti | Penyajian | apps/tmc-web | T3 |

### F12 Platform banyak kota, data terbuka, dan pengelolaan permintaan perjalanan

Satu platform melayani banyak kota dengan data terpisah per yurisdiksi, membandingkan kinerja antar kota, menghitung ambang legal kebijakan pembatasan kendaraan, dan membuka data lewat API publik untuk aplikasi navigasi, peneliti, dan warga.

![F12](diagram/F12_Platform_banyak_kota.png)

Tahap yang terlibat: T4, T5. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Kota A, Kota B, dan seterusnya sebagai tenant; Kemenhub/BPTJ; provinsi | Pengguna | tenant | T5 |
| b. Isolasi data per tenant dan yurisdiksi; peran akses | Pusat | apps/api (multi-tenant) | T4 |
| c. Benchmark antar kota: arrivals on green, LOS, ketersediaan perangkat | Pusat | services/kpi-pkji | T5 |
| d. Kalkulator ambang kebijakan pembatasan (V/C dan kecepatan) dan evaluasi tahunan | Pusat | services/tdm | T5 |
| e. Penasihat pembelajaran mesin yang hanya mengusulkan parameter | Pusat | services/advisor | T5 |
| f. API publik dan data terbuka; integrasi ERP dan ganjil-genap pemprov | Komunikasi | API gateway | T5 |
| g. Portal data terbuka; dashboard benchmark | Penyajian | apps/tmc-web | T5 |
| h. Aplikasi navigasi (GLOSA/SPaT), peneliti, warga | Pengguna | (pihak luar) | T5 |
