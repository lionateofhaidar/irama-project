# 08 — Asumsi, Risiko Pra-Proyek, dan Pertanyaan Terbuka

Status: draf pra-perencanaan (2026-09-12), direvisi 2026-09-14 (tahapan baru; asumsi dan risiko Vision Tracker, data, laptop, dan lisensi). Setiap asumsi punya cara validasi; setiap pertanyaan punya rekomendasi default agar planning rinci bisa berjalan tanpa menunggu.

## 1. Asumsi (A-xx)

### Teknis
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-01 | Controller APILL di kota target (mayoritas produk lokal) dapat diakses lewat protokol vendor RS-232/TCP atau NTCIP; sebagian hanya "pilih plan" | SK.7234/2013 mewajibkan interface komunikasi ATCS pada controller [R00 H]; NTCIP hanya pada controller modern | Survei 3 kota: inventaris merek controller, protokol, dokumentasi; uji bench 2 merek |
| A-02 | Kamera CCTV eksisting dan rekamannya cukup untuk menghitung arus per kelas dan per arah dengan akurasi sekitar 90% siang dan 85% malam atau hujan (T2), lalu 95% dan 90% (T3); diolah di laptop sampai T3 dan di edge mulai T4 (direvisi 2026-09-14) | Praktik DKI (kamera + edge AI) [majalah]; degradasi malam/hujan [R04 A.2]; keputusan user T-34, T-39 | Uji akurasi per kondisi terhadap hitungan manual (`16` langkah H) |
| A-03 | Data probe (GPS bus, Google/TomTom, ojol) dapat diperoleh untuk evaluasi koridor dengan penetrasi ≥3% | Mahmud & Day 2023 [R04 A.19] | Uji dengan GPS bus BRT kota pilot; cek lisensi data komersial |
| A-04 | Laptop tim (Ryzen 7 7730U, 32 GB, tanpa GPU NVIDIA) cukup untuk T1 sampai T3: mengolah rekaman 2 sampai 5 kali lebih cepat dari waktu nyata per kamera dengan model ringan dan menjalankan 2 sampai 4 stream uji; server baru di T4 (direvisi 2026-09-14) [A] | Spesifikasi laptop (log T-33); `15` bagian kinerja | Uji kecepatan model di T1 (`16` langkah G) |
| A-05 | Kendali adaptif per simpang (actuated, pembagian hijau dengan batas perubahan per siklus) dengan cadangan TOD dapat berjalan dengan data antrian 10 s dari detektor virtual dan latensi komunikasi ≤2 s (T4); max-pressure jaringan di T5 (direvisi 2026-09-14) | Tsitsokas 2022 [R04 A.5] | SUMO (SIL) lalu mode bayangan |
| A-06 | Jaringan komunikasi simpang–pusat tersedia (fiber/seluler 4G) dan diizinkan Diskominfo | Tipikal ATCS Indonesia memakai fiber/wireless [R02 F.4] | Cek per simpang saat survei |
| A-07 | Log hi-res 0,1 s tidak tersedia dari controller lama; perlu logger eksternal atau derivasi dari status poll 1 s | NCDOT: logger eksternal tak merekam termination type [R03 C.1] | Uji pada controller pilot |

### Pasar & bisnis
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-08 | Dishub kota target punya pos anggaran "pengembangan/pemeliharaan ATCS" tahunan yang bisa dipakai e-purchasing | Yogya, Kudus, Bekasi, Depok belanja ATCS 2023–2025 [Pra-Perencanaan 03] | Wawancara Kabid Lalin 3 kota; cek DPA/LPSE |
| A-09 | Harga software Rp25–60 jt/simpang diterima bila di bawah 20% biaya paket turnkey | Paket Rp350 jt–1,8 M/simpang [03] | Uji harga di 2 kota; bandingkan e-katalog |
| A-10 | Pilot berbiaya rendah (satu simpang untuk uji lapangan T3, lalu beberapa simpang) dapat dilegalkan lewat PKS/swakelola tanpa tender (direvisi 2026-09-14) | Perda 5/2014 Ps.239; Pergub 68 Ps.7 [R05] | Konsultasi bagian hukum pemda pilot |
| A-11 | Vendor controller lokal bersedia bermitra (bukan menghalangi) karena membuka pasar software | Javis sudah menjual ATMS sendiri → bisa bersaing [03] | Pendekatan 2 vendor |
| A-12 | Sertifikat TKDN untuk software dapat diperoleh <6 bulan | Perpres 46/2025 preferensi PDN [03] | Konsultasi Kemenperin/LKPP |

### Hukum & tata kelola
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-13 | Aplikasi cukup sebagai "penyedia bukti/data" untuk ETLE; penindakan tetap Polri | UU Ps.272, 260; PP 32 Ps.46 [R05] | Konfirmasi Ditlantas; jangan bangun fitur denda |
| A-14 | Pemda adalah pengendali data (UU PDP); vendor = prosesor; ANPR/plat = data pribadi | UU 27/2022 [Bahan Acuan] | Kajian PDP + PKS pengolahan data sebelum T3 |
| A-15 | Simpang jalan nasional di kota target bisa dioperasikan Dishub kota setelah persetujuan/koordinasi Dirjen/BPTJ | PM 96 Ps.5; PM 49 Ps.28 [R05] | Inventaris status jalan per simpang pilot |
| A-16 | Kewajiban ≥8 rencana siklus, LOS PM 96, pemeliharaan 6 bulan, umur teknis 5 tahun berlaku sebagai syarat produk | PM 49, PM 96 [R00] | Cek dengan konsultan/BPTJ |

### Sumber daya
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-17 | Tim inti T1 dan T2: dua orang, dibantu pendamping traffic engineer lewat kolaborasi; bertambah 1 sampai 2 orang di T3 (direvisi 2026-09-14) | Keputusan user U-06; T1 satu simpang | Diputuskan user |
| A-18 | Rekaman sendiri dan video publik cukup untuk T1 dan T2; akses rekaman dan stream Dishub lewat MoU menjelang T3 (direvisi 2026-09-14) | Keputusan user T-39, T-41 | `13` |
| A-19 | Dishub pilot menyediakan minimal 1 operator + 1 teknisi sebagai counterpart | Kebutuhan pelatihan & kalibrasi [R02] | Dalam PKS |

### Tambahan 2026-09-14 (Vision Tracker, data, dan komputasi)
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-20 | Video publik (misalnya YouTube) dapat dipakai untuk uji dan pelatihan selama pengembangan | Keputusan user T-42 | Register sumber; tinjauan hukum dan pelatihan ulang dengan data berizin sebelum penjualan komersial skala besar |
| A-21 | Layanan GPU gratis (Kaggle, Colab) cukup untuk pra-label dan pelatihan model T1 sampai T3 | Kuota Kaggle sekitar 30 jam GPU per minggu (dapat berubah) | Uji pelatihan di T1 (`16` langkah F) |
| A-22 | Sampel rekaman terbatas, termasuk dari simpang berbeda, cukup untuk membuktikan akurasi di T1 dan T2 | Keputusan user T-41 | Uji pada klip dari simpang yang tidak dipakai melatih |
| A-23 | Engineer Dishub bersedia memakai rekomendasi berbasis PKJI 2023 yang divalidasi SUMO sebagai dasar penetapan jadwal | Kewajiban simulasi sebelum penetapan (PM 96/2015) | Wawancara dan jasa kajian pertama |

## 2. Register risiko pra-proyek (keputusan produk, pasar, tim, dana, mitra, hukum)

| ID | Risiko | Kemungkinan | Dampak | Mitigasi | Pemilik |
|---|---|---|---|---|---|
| R-01 | Salah asumsi "controller bisa dikendalikan": banyak APILL lama hanya bisa ganti plan lokal → adaptif detik-ke-detik mustahil | Tinggi | Tinggi | Kendali baru di T4; T3 membaca controller untuk memetakan kemampuan; "plan-level control" (pilih/ubah TOD & split via download) sebagai jalur utama T4; second-by-second hanya bila NTCIP/vendor mendukung | Produk |
| R-02 | Vendor petahana memblokir akses protokol/menuntut lisensi | Sedang | Tinggi | Kemitraan B2B2G; adaptor via logger/relay; targetkan kota tanpa vendor dominan dulu | Bisnis |
| R-03 | Membangun terlalu banyak fitur ITCS (ANPR, ETLE, digital twin) sebelum ada pembeli | Tinggi | Tinggi | Disiplin tahap T1–T2 (lihat 04/05); tiap fitur harus punya persona & pembeli | Produk |
| R-04 | Klaim manfaat tidak bisa dibuktikan → kredibilitas hilang | Sedang | Tinggi | Perbandingan eksisting dan rekomendasi sejak T1; validasi SUMO sejak T2; uji lapangan sebelum-sesudah di T3; MOE PM 96/PKJI; publikasi metode | Produk |
| R-05 | Siklus anggaran APBD melewatkan tahun → 12–18 bulan tanpa pendapatan | Tinggi | Sedang | Pilot swakelola; e-katalog; APBD-P; bidik 3 kota paralel | Bisnis |
| R-06 | Ketergantungan data mitra (AVL bus, Polri, probe komersial) tidak terwujud | Sedang | Sedang | Fitur inti tidak bergantung data mitra; TSP/EVP di T4 dengan MoU tertulis (detik prioritas) [R06] | Bisnis |
| R-07 | UU PDP: ANPR/plat tanpa dasar → sanksi/penolakan Diskominfo | Sedang | Tinggi | T1 dan T2 memproses video yang memuat wajah dan pelat, sehingga penyamaran, akses terbatas, dan penghapusan video mentah berlaku sejak T2; DPIA sebelum memproses data Dishub (T3); ANPR baru di T4 dengan minimisasi, hashing pelat, dan retensi singkat | Hukum |
| R-08 | Tim kecil tanpa traffic engineer bersertifikat → salah hitung PKJI/keselamatan (yellow/all-red) | Sedang | Tinggi | Rekrut/konsultan MRLL; validator rumus di aplikasi; uji SUMO | Tim |
| R-09 | Pemda menganggap "adaptif = set and forget" lalu sistem dikembalikan ke fixed-time (umur ASCT 6–7 tahun) | Tinggi | Tinggi | Paket wajib: pelatihan, AMS, KPI kesehatan, retiming ≤3 tahun [R02] | Bisnis/Produk |
| R-10 | Keamanan: kabinet/jaringan pemda lemah; insiden siber merusak reputasi | Sedang | Tinggi | NEMA TS 8, RBAC, audit log, heartbeat/backup timer NTCIP (controller kembali ke TOD) [R03] | Teknis |
| R-11 | Kompetisi harga dari paket turnkey vendor (software "gratis" ikut hardware) | Tinggi | Sedang | Diferensiasi: KPI resmi, transparansi, multi-vendor, analitik; jual ke kota yang sudah punya hardware | Bisnis |
| R-12 | Ketidakjelasan kewenangan (Dishub vs Polri vs BPTJ) menghambat go-live | Sedang | Sedang | Peta yurisdiksi per simpang; workflow persetujuan; libatkan Polantas sejak pilot | Produk/Bisnis |
| R-13 | Nama/merek bentrok dengan produk existing (mis. "SITS", "ATCS Kota X", "Lancar") | Sedang | Rendah | Cek merek DJKI & domain sebelum branding (lihat 02) | Bisnis |
| R-14 | Pendanaan pengembangan T1–T2 tidak cukup hingga pendapatan pertama (12–18 bulan) | Sedang | Tinggi | Nol pengadaan sampai T3; jasa kajian T2 sebagai pendapatan awal; hibah riset (Kedaireka/LPDP) [A] | Pemilik |
| R-15 | Akurasi Vision Tracker di bawah target pada malam, hujan, atau motor yang berhimpitan | Tinggi | Tinggi | Target bertahap (sekitar 90% dan 85% di T1–T2, 95% dan 90% mulai T3); halaman kualitas data; koreksi engineer; active learning; hitungan manual untuk sampel uji | Produk |
| R-16 | Hak cipta dan ketentuan layanan video publik (YouTube) | Sedang | Sedang | Register sumber; hanya untuk uji dan pelatihan; video tidak didistribusikan ulang; pelatihan ulang dengan data berizin sebelum penjualan skala besar | Hukum |
| R-17 | Keterbatasan laptop (kinerja, ruang disk, titik tunggal kegagalan) | Sedang | Sedang | Model ringan, olah per batch, resolusi 720p, video mentah dihapus setelah diolah, cadangan ke GitHub | Teknis |
| R-18 | Lisensi pustaka berubah atau komponen berlisensi tidak cocok ikut masuk | Sedang | Tinggi | Pemeriksaan lisensi otomatis di CI, daftar larangan (Ultralytics, Redis versi baru, EMQX), ADR-25 | Teknis |
| R-19 | Sampel rekaman dari simpang berbeda tidak mewakili simpang target | Sedang | Sedang | Rekaman gabungan hanya untuk uji akurasi; optimasi memakai rekaman semua lengan pada periode yang sama; sumber ditandai di laporan | Produk |
| R-20 | Kuota GPU gratis berubah atau dihentikan | Sedang | Rendah | Dua layanan bergantian; model kecil; pelatihan di CPU laptop sebagai jalan terakhir | Teknis |
| R-21 | Perbedaan hasil PKJI dan simulasi SUMO membingungkan pengguna | Sedang | Sedang | Keduanya ditampilkan dengan penjelasan; PKJI sebagai acuan resmi dan SUMO sebagai validasi | Produk |
| R-22 | MoU dengan Dishub tertunda sehingga T3 tertahan | Sedang | Sedang | Deteksi kejadian tetap dikembangkan dengan rekaman; jasa kajian T2 sebagai pintu masuk MoU; kuesioner `12` | Bisnis |
| R-23 | Tim tanpa teknisi lapangan tidak dapat memasang perangkat di kabinet (T4) | Tinggi | Sedang | Perangkat di kabinet dirancang untuk dipasang teknisi Dishub atau vendor dengan checklist dan dukungan jarak jauh | Teknis |

## 3. Pertanyaan terbuka untuk user (Q-xx) + rekomendasi default

Status 2026-09-14: Q-01 sampai Q-13 sudah dijawab user pada 2026-09-13, dan sebagian direvisi pada 2026-09-14. Jawaban kanonis ada di `docs/kb/10` bagian B dan B2; tabel di bawah dipertahankan sebagai riwayat. Contoh revisi: kendali dan override petugas dari konsol pindah ke T4, dan hosting sampai T3 memakai laptop tim.

| ID | Pertanyaan | Mengapa penting | Default bila tidak dijawab |
|---|---|---|---|
| Q-01 | Entitas & pendanaan: dikembangkan oleh perusahaan (Hydem Custodia & Co?) dengan modal sendiri, mitra, atau hibah? Berapa runway? | Menentukan skala T1 dan model bisnis | Bootstrapped 12 bulan; T1 dalam 3–4 bulan; T2 dalam 9 bulan |
| Q-02 | Tim: siapa yang tersedia (jumlah, keahlian backend/edge/ML/traffic engineering)? Ada traffic engineer/konsultan MRLL? | Kelayakan T1 & keselamatan | Tim 3–5 orang + 1 konsultan MRLL paruh waktu |
| Q-03 | Bangun/pasarkan hardware (controller/detektor) sendiri atau **software-only** di atas controller vendor? | Menentukan produk, TKDN, modal | **Software-only** + adaptor; hardware via mitra |
| Q-04 | Kota pilot pertama? Ada relasi di Dishub tertentu? | Menentukan survei, protokol controller, bahasa daerah data | 1 kota Bodetabek (akses & jarak) + 1 dari Bandung/Medan |
| Q-05 | Akses data uji: bisakah memperoleh log APILL/CCTV/count dari satu Dishub? Jika tidak, mulai dengan SUMO sintetis? | Kualitas MVP | Mulai SUMO (NEMA, koridor sintetis mirip kota pilot) + data publik CCTV |
| Q-06 | Preferensi stack (bahasa, DB, cloud/on-prem) & lisensi kode (open-source inti + modul komersial, atau proprietary)? | Arsitektur & GTM (SPBE/Diskominfo suka on-prem) | Python (algoritma/edge) + TypeScript (web) + PostgreSQL/TimescaleDB + MQTT; on-prem-first, container; inti proprietary dengan SDK/ICD terbuka [A] |
| Q-07 | Hosting: server pemda (Diskominfo), cloud lokal (mis. BSSN-compliant), atau hybrid? | Keamanan & biaya | On-prem pemda/hybrid; cloud hanya untuk analitik agregat |
| Q-08 | Apakah ETLE/pajak/uji emisi masuk roadmap, atau hanya "penyedia bukti"? | PDP & kewenangan | Hanya penyedia bukti/agregat (T4), tidak ada modul penindakan |
| Q-09 | Bahasa produk: Indonesia saja atau dwibahasa (untuk vendor/standar)? | UI & dokumentasi | UI Indonesia, istilah teknis EN, dokumen API EN |
| Q-10 | Nama & merek: apakah ada preferensi/konotasi yang dihindari; perlu cek DJKI? | Branding | Lihat 02 Kandidat Nama; cek DJKI & domain sebelum T2 |
| Q-11 | Batas keterlibatan Polri: cukup akses baca + log, atau override langsung dari TMC Polda? | Desain RBAC & yurisdiksi | Akses baca + tombol plan darurat dengan approval Dishub (T2); override langsung T3 dengan PKS |
| Q-12 | Apakah ingin menerbitkan bagian inti sebagai open source untuk kepercayaan pemda/akademisi? | Adopsi & TKDN | Buka SDK/adaptor & ICD; inti tetap tertutup sampai T3 |
| Q-13 | Target waktu tayang e-katalog & sertifikasi TKDN? | GTM | Mulai proses saat T1 selesai |

## 4. Keputusan yang sudah tersirat dari bahan acuan (dianggap tetap kecuali user membatalkan)

| ID | Keputusan | Sumber |
|---|---|---|
| D-01 | Standar antarmuka controller: NTCIP 1202 (+1211 untuk prioritas) sebagai bahasa internal; adaptor untuk vendor lama | R02 G.7, R03 |
| D-02 | LOS simpang memakai ambang PM 96/2015; kinerja dihitung PKJI 2023 (MKJI sebagai pembanding) | R00 E, R05 D |
| D-03 | Fallback wajib: ≥8 rencana TOD; degradasi adaptif → actuated → TOD lokal → flash; heartbeat < backup timer | PM 49 Ps.14; HOP-11-027; NTCIP `unitBackupTime` |
| D-04 | Inti adaptif realistis bertahap: T4 actuated, pembagian hijau dengan batas perubahan, pemilihan program (TRPS), dan offset dasar; T5 cyclic max-pressure terkoordinasi dan perimeter control di simpang kritis; RL hanya advisor via shadow mode (direvisi 2026-09-14) | R04 F; keputusan user T-35 |
| D-05 | Prioritas bus berbasis aturan di T4 (green extension/early green ≤10 s, 1 aktivasi/siklus, lockout) dan bersyarat berbasis occupancy/headway di T5; EVP bertingkat di T4 (direvisi 2026-09-14) | R04, R06 |
| D-06 | ATSPM sebagai observer independen; log hi-res 0,1 s sebagai sumber kebenaran KPI; pipeline sama untuk lapangan & SUMO | R03 D |
| D-07 | Evaluasi manfaat wajib desain on/off + before–after, terpisah dari manfaat retiming | R02 E |
| D-08 | Aplikasi = penyedia bukti/data untuk ETLE; bukan penindak; data pribadi diminimalkan (UU PDP) | R05 G |
| D-09 | Keamanan: NEMA TS 8, RBAC per yurisdiksi, audit log semua perintah, LLM di luar control loop | R02 G.7, R04 A.17 |
| D-10 | Deployment bertahap: satu simpang (T1 dan T2), beberapa simpang yang dihitung mandiri (T3), koordinasi dasar untuk grup ≥3 simpang ≤1 km (T4), koridor dan jaringan penuh (T5), dengan pilot & experimental plan (direvisi 2026-09-14) | PM 96; R02 H.3; keputusan user T-34, T-35 |
| D-11 | Transparansi algoritma: nilai perhitungan antara & alasan keputusan tersimpan dan dapat dilaporkan ke publik/pejabat | HOP-11-027 Req 18.0-1/2, 6.0-11 |
| D-12 | Dukung stage-based (Indonesia) dan ring-barrier (NTCIP) dalam model data | R00 I |
