## 9. Diagram alur fitur utama dan pemetaannya ke arsitektur dan tahap

Diagram berikut menggambarkan cara IRAMA bekerja pada kondisi end-state, satu diagram per fitur utama. Cara membacanya sama untuk semua diagram.

- Baris (lajur mendatar) adalah lapisan arsitektur: pengguna dan mitra eksternal, penyajian, pusat, komunikasi dan integrasi, lapangan. Posisi kotak menunjukkan komponen mana yang menjalankan langkah itu.
- Kotak adalah langkah, diberi huruf urut dan warna bingkai. Label kecil di pojok kanan atas (T1 sampai T5) menandai tahap saat langkah itu pertama tersedia. Warna: T1 hijau, T2 biru, T3 jingga, T4 ungu, T5 merah.
- Panah adalah aliran data atau perintah. Label abu-abu pada panah menjelaskan kondisi, misalnya "bila putus". Label berwarna, misalnya T3, berarti hubungan itu baru ada mulai tahap tersebut.
- Untuk membaca diagram pada tahap tertentu, abaikan kotak yang labelnya lebih tinggi dari tahap itu. Contoh: pada T2, kotak berlabel T3 sampai T5 belum ada, dan alur berhenti pada kotak terakhir yang tersedia.

Tabel di bawah tiap diagram memetakan langkah ke komponen dalam struktur repositori (apps, services, edge, sim, infra) dan tahapnya. Diagram direvisi 2026-09-14 mengikuti tahapan baru: T1 purwarupa, T2 Vision Tracker dan optimasi, T3 deteksi kejadian dan pemantauan, T4 kendali adaptif, T5 platform kota. Diagram arsitektur alur data per komponen dan teknologi (A01) ada di dokumen 14.

### F00 Gambaran keseluruhan komponen per lapisan dan tahap

![F00](diagram/F00_Gambaran_Keseluruhan.png)

Diagram ini memperlihatkan semua komponen yang ada pada end-state, dikelompokkan per lapisan, dengan label tahap pemunculannya. Diagram F01 sampai F12 memperlihatkan bagaimana komponen tersebut bekerja sama untuk tiap fitur.

### F01 Pemantauan kondisi simpang

Kondisi setiap simpang (arus, LOS, nyala lampu, peringatan) terlihat di dashboard. T1 dan T2 memakai data dari rekaman melalui Vision Tracker; T3 menambah stream Dishub dan status controller baca-saja; T4 menambah edge dan kendali.

![F01](diagram/F01_Pemantauan_kondisi_simpang.png)

Tahap yang terlibat: T1, T2, T3, T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Rekaman atau stream CCTV simpang | Lapangan | kamera eksisting, berkas rekaman | T1 |
| b. Controller dibaca tanpa diubah, bila Dishub mengizinkan | Lapangan | controller vendor/NTCIP | T3 |
| c. Agen edge di kabinet menerjemahkan protokol vendor | Lapangan | edge/ | T4 |
| d. Stream Dishub lewat VPN setelah MoU; MQTT dan mTLS di T4 | Komunikasi | infra/ (MediaMTX, VPN) | T3 |
| e. Vision Tracker menghitung arus (T1) dan membaca nyala lampu (T2) | Pusat | services/vision | T1 |
| f. Aturan peringatan (lampu mati atau kedip, kamera bermasalah) | Pusat | services/health | T3 |
| g. Peta simpang, LOS, dan kondisi terkini di dashboard | Penyajian | apps/tmc-web (MapLibre) | T2 |
| h. Engineer, operator, dan pimpinan memantau | Pengguna | (pihak luar) | T2 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F01h["h. Engineer, operator, dan pimpinan memantau (T2)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F01g["g. Peta simpang, LOS, dan kondisi terkini di dashboard (T2)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F01e["e. Vision Tracker menghitung arus (T1) dan membaca nyala lampu (T2) (T1)"]
    F01f["f. Aturan peringatan (lampu mati atau kedip, kamera bermasalah) (T3)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F01d["d. Stream Dishub lewat VPN setelah MoU; MQTT dan mTLS di T4 (T3)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F01a["a. Rekaman atau stream CCTV simpang (T1)"]
    F01b["b. Controller dibaca tanpa diubah, bila Dishub mengizinkan (T3)"]
    F01c["c. Agen edge di kabinet menerjemahkan protokol vendor (T4)"]
  end
  F01a --> F01e
  F01b --> F01d
  F01c -->|T4| F01d
  F01d --> F01e
  F01e --> F01f
  F01e --> F01g
  F01f -->|peringatan| F01g
  F01g --> F01h
  classDef t1 stroke:#2E7D32,stroke-width:2px
  class F01a,F01e t1
  classDef t2 stroke:#1565C0,stroke-width:2px
  class F01g,F01h t2
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F01b,F01d,F01f t3
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F01c t4
```

### F02 Rekomendasi dan penetapan waktu sinyal

Engineer mengonfigurasi simpang, sistem mengubah hitungan Vision Tracker menjadi arus SMP, menghitung kinerja dengan PKJI 2023, menjalankan mode optimasi, memvalidasinya di SUMO, lalu menyusun laporan. Rekomendasi diterapkan manual di T2, lewat lembar jadwal di T3, dan dikirim ke controller di T4.

![F02](diagram/F02_Rekomendasi_dan_penetapan_waktu_sinyal.png)

Tahap yang terlibat: T1, T2, T3. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Engineer mengisi konfigurasi simpang (formulir T1, wizard T2) | Pengguna | apps/tmc-web | T1 |
| b. Konversi hitungan ke arus SMP per periode (EMP PKJI 2023) | Pusat | services/optimizer | T1 |
| c. Kalkulator PKJI 2023: kapasitas, DJ, antrian, tundaan, LOS | Pusat | services/optimizer (NumPy) | T1 |
| d. Mode optimasi: Webster (T1); empat mode lain (T2); multi-kriteria (T3) | Pusat | services/optimizer (SciPy) | T1 |
| e. Validator keselamatan dan validasi SUMO eksisting vs rekomendasi | Pusat | sim/ (SUMO) | T2 |
| f. Dashboard rekomendasi, manfaat rupiah, laporan Word/PDF | Penyajian | apps/tmc-web, services/reports | T2 |
| g. Persetujuan Kepala Dinas; Dirjen/BPTJ bila jalan nasional | Pengguna | alur persetujuan | T2 |
| h. Petugas menerapkan waktu baru di controller | Lapangan | manual (T2), lembar jadwal (T3), NTCIP/adaptor (T4) | T2 |
| i. Uji lapangan sebelum-sesudah diukur Vision Tracker | Pusat | services/vision | T3 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F02a["a. Engineer mengisi konfigurasi simpang (formulir T1, wizard T2) (T1)"]
    F02g["g. Persetujuan Kepala Dinas; Dirjen/BPTJ bila jalan nasional (T2)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F02f["f. Dashboard rekomendasi, manfaat rupiah, laporan Word/PDF (T2)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F02b["b. Konversi hitungan ke arus SMP per periode (EMP PKJI 2023) (T1)"]
    F02c["c. Kalkulator PKJI 2023: kapasitas, DJ, antrian, tundaan, LOS (T1)"]
    F02d["d. Mode optimasi: Webster (T1); empat mode lain (T2); multi-kriteria (T3) (T1)"]
    F02e["e. Validator keselamatan dan validasi SUMO eksisting vs rekomendasi (T2)"]
    F02i["i. Uji lapangan sebelum-sesudah diukur Vision Tracker (T3)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F02h["h. Petugas menerapkan waktu baru di controller (T2)"]
  end
  F02a --> F02b
  F02b --> F02c
  F02c --> F02d
  F02d --> F02e
  F02e --> F02f
  F02f --> F02g
  F02g --> F02h
  F02h -->|T3| F02i
  classDef t1 stroke:#2E7D32,stroke-width:2px
  class F02a,F02b,F02c,F02d t1
  classDef t2 stroke:#1565C0,stroke-width:2px
  class F02e,F02f,F02g,F02h t2
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F02i t3
```

### F03 Kendali terpusat, mode manual petugas, dan cadangan saat putus

Mulai T4 operator atau petugas Polri memilih program atau mode manual dari ruang kendali. Pusat mengirim perintah terbatas beserta detak jantung. Bila jaringan putus, controller kembali ke jadwal lokal dan semua kejadian tetap tercatat.

![F03](diagram/F03_Kendali_terpusat.png)

Tahap yang terlibat: T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Operator atau petugas Polri memilih program, kedip, atau mode manual | Pengguna | konsol kendali | T4 |
| b. Konsol kendali meminta konfirmasi dan alasan | Penyajian | apps/tmc-web | T4 |
| c. Layanan perintah memeriksa hak akses, mengirim perintah dan detak jantung | Pusat | services/cai | T4 |
| d. SNMP/MQTT lewat VPN | Komunikasi | infra/ | T4 |
| e. Controller menjalankan program; edge meneruskan detak jantung | Lapangan | controller, edge/ | T4 |
| f. Jaringan putus: controller kembali ke jadwal lokal; edge menyimpan catatan | Lapangan | controller, edge/ | T4 |
| g. Jejak audit perintah; alarm bila cadangan aktif | Pusat | audit log, services/health | T4 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F03a["a. Operator atau petugas Polri memilih program, kedip, atau mode manual (T4)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F03b["b. Konsol kendali meminta konfirmasi dan alasan (T4)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F03c["c. Layanan perintah memeriksa hak akses, mengirim perintah dan detak jantung (T4)"]
    F03g["g. Jejak audit perintah; alarm bila cadangan aktif (T4)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F03d["d. SNMP/MQTT lewat VPN (T4)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F03e["e. Controller menjalankan program; edge meneruskan detak jantung (T4)"]
    F03f["f. Jaringan putus: controller kembali ke jadwal lokal; edge menyimpan catatan (T4)"]
  end
  F03a --> F03b
  F03b --> F03c
  F03c --> F03d
  F03d --> F03e
  F03e -->|bila putus| F03f
  F03e --> F03g
  F03f -->|alarm| F03g
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F03a,F03b,F03c,F03d,F03e,F03f,F03g t4
```

### F04 Kesehatan kamera dan perangkat, alarm, tiket kerja, dan pemeliharaan

Kamera bermasalah terdeteksi dari gambar mulai T3; alarm controller dan detektor mulai T4. Peringatan menjadi tiket kerja untuk teknisi. Jadwal pemeliharaan berkala dan umur teknis aset dijaga sesuai PM 49/2014.

![F04](diagram/F04_Kesehatan_kamera_dan_perangkat.png)

Tahap yang terlibat: T3, T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Kamera tertutup, gelap, buram, atau bergeser | Lapangan | kamera; dideteksi services/vision | T3 |
| b. Alarm controller, detektor, pintu kabinet, catu daya | Lapangan | controller, edge/ | T4 |
| c. Mesin peringatan: prioritas, eskalasi, notifikasi APILL mati | Pusat | services/health | T3 |
| d. Email/WhatsApp; API aduan kota | Komunikasi | integrasi | T3 |
| e. Tiket kerja otomatis dengan target waktu penyelesaian | Pusat | services/ticket | T3 |
| f. Aplikasi ponsel teknisi: tiket, checklist, foto | Penyajian | apps/tmc-web (PWA) | T4 |
| g. Jadwal pemeliharaan enam bulanan dan umur teknis lima tahun | Pusat | apps/api (aset) | T3 |
| h. Kepala Dinas melihat KPI kesehatan kamera dan perangkat | Pengguna | dashboard pimpinan | T3 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F04h["h. Kepala Dinas melihat KPI kesehatan kamera dan perangkat (T3)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F04f["f. Aplikasi ponsel teknisi: tiket, checklist, foto (T4)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F04c["c. Mesin peringatan: prioritas, eskalasi, notifikasi APILL mati (T3)"]
    F04e["e. Tiket kerja otomatis dengan target waktu penyelesaian (T3)"]
    F04g["g. Jadwal pemeliharaan enam bulanan dan umur teknis lima tahun (T3)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F04d["d. Email/WhatsApp; API aduan kota (T3)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F04a["a. Kamera tertutup, gelap, buram, atau bergeser (T3)"]
    F04b["b. Alarm controller, detektor, pintu kabinet, catu daya (T4)"]
  end
  F04a --> F04c
  F04b -->|T4| F04c
  F04c --> F04d
  F04c --> F04e
  F04e --> F04f
  F04f -->|selesai| F04e
  F04g -->|jatuh tempo| F04e
  F04e -->|KPI| F04h
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F04a,F04c,F04d,F04e,F04g,F04h t3
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F04b,F04f t4
```

### F05 Pengukuran kinerja dan laporan

Hitungan dan status lampu dari Vision Tracker (kemudian juga log controller) diolah menjadi KPI resmi PKJI dan LOS PM 96/2015, perbandingan eksisting dan rekomendasi, laporan kajian (T2), dan laporan wajib ke Forum LLAJ, Dirjen/BPTJ, dan Gubernur (T3).

![F05](diagram/F05_Pengukuran_kinerja_dan_laporan.png)

Tahap yang terlibat: T1, T2, T3, T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Hitungan (T1), status lampu dan antrian (T2) dari Vision Tracker | Lapangan | services/vision | T1 |
| b. Log kejadian controller lewat MQTT | Komunikasi | infra/ | T4 |
| c. Simpan tabel 15 menit (T1), status lampu dan antrian (T2); retensi bertingkat | Pusat | PostgreSQL | T1 |
| d. Metrik kinerja sinyal (split failure, arrivals on green) | Pusat | services/metrics | T3 |
| e. KPI PKJI dan LOS PM 96; eksisting vs rekomendasi | Pusat | services/optimizer | T1 |
| f. Laporan kajian simpang (T2); laporan wajib (T3) | Pusat | services/reports | T2 |
| g. Dashboard pimpinan dan engineer; dashboard publik (T3) | Penyajian | apps/tmc-web | T2 |
| h. Pejabat, DPRD, Forum LLAJ, warga | Pengguna | (pihak luar) | T2 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F05h["h. Pejabat, DPRD, Forum LLAJ, warga (T2)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F05g["g. Dashboard pimpinan dan engineer; dashboard publik (T3) (T2)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F05c["c. Simpan tabel 15 menit (T1), status lampu dan antrian (T2); retensi bertingkat (T1)"]
    F05d["d. Metrik kinerja sinyal (split failure, arrivals on green) (T3)"]
    F05e["e. KPI PKJI dan LOS PM 96; eksisting vs rekomendasi (T1)"]
    F05f["f. Laporan kajian simpang (T2); laporan wajib (T3) (T2)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F05b["b. Log kejadian controller lewat MQTT (T4)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F05a["a. Hitungan (T1), status lampu dan antrian (T2) dari Vision Tracker (T1)"]
  end
  F05a --> F05c
  F05b -->|T4| F05c
  F05c --> F05d
  F05c --> F05e
  F05e --> F05f
  F05e --> F05g
  F05f --> F05h
  F05g --> F05h
  classDef t1 stroke:#2E7D32,stroke-width:2px
  class F05a,F05c,F05e t1
  classDef t2 stroke:#1565C0,stroke-width:2px
  class F05f,F05g,F05h t2
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F05d t3
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F05b t4
```

### F06 Pipeline Vision Tracker dan keluaran tabel hitungan

Vision Tracker mengubah rekaman atau stream CCTV menjadi tabel hitungan per kelas, per arah, dan per 15 menit, ditambah hambatan samping, nyala lampu, dan antrian. Penyamaran wajah dan pelat berlaku mulai T2. Mulai T3 ditambah deteksi kejadian dan kesehatan kamera. Di T4 Vision Tracker berjalan di perangkat edge dan pembacaan pelat memakai kamera ANPR khusus.

![F06](diagram/F06_Pipeline_Vision_Tracker_dan_keluaran.png)

Tahap yang terlibat: T1, T2, T3, T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Rekaman CCTV atau video publik (T1); stream RTSP/HLS (uji T2, Dishub T3) | Lapangan | berkas, MediaMTX | T1 |
| b. Ambil bingkai sekitar 10 per detik | Pusat | FFmpeg, OpenCV | T1 |
| c. Deteksi enam kelas dan pelacakan | Pusat | RF-DETR/YOLOX, ONNX Runtime, ByteTrack | T1 |
| d. Hitung per pendekat (T1) dan per arah dari lintasan (T2) | Pusat | supervision, services/vision | T1 |
| e. Hambatan samping berbobot PKJI, nyala lampu, antrian dasar | Pusat | services/vision | T2 |
| f. Tabel hitungan 15 menit dan mutu data; penyamaran video mulai T2 | Pusat | PostgreSQL, services/vision | T1 |
| g. Kendaraan prioritas, kejadian, pelanggaran, kesehatan kamera | Pusat | services/vision | T3 |
| h. Vision Tracker di edge 24 jam; ANPR kamera khusus | Lapangan | edge/ (Jetson/IPC) | T4 |
| i. Tabel dan dashboard dasar (T1); halaman kualitas data (T2) | Penyajian | apps/tmc-web | T1 |
| j. Engineer memeriksa dan mengoreksi | Pengguna | (pihak luar) | T1 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F06j["j. Engineer memeriksa dan mengoreksi (T1)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F06i["i. Tabel dan dashboard dasar (T1); halaman kualitas data (T2) (T1)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F06b["b. Ambil bingkai sekitar 10 per detik (T1)"]
    F06c["c. Deteksi enam kelas dan pelacakan (T1)"]
    F06d["d. Hitung per pendekat (T1) dan per arah dari lintasan (T2) (T1)"]
    F06e["e. Hambatan samping berbobot PKJI, nyala lampu, antrian dasar (T2)"]
    F06f["f. Tabel hitungan 15 menit dan mutu data; penyamaran video mulai T2 (T1)"]
    F06g["g. Kendaraan prioritas, kejadian, pelanggaran, kesehatan kamera (T3)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F06a["a. Rekaman CCTV atau video publik (T1); stream RTSP/HLS (uji T2, Dishub T3) (T1)"]
    F06h["h. Vision Tracker di edge 24 jam; ANPR kamera khusus (T4)"]
  end
  F06a --> F06b
  F06b --> F06c
  F06c --> F06d
  F06d -->|T2| F06e
  F06d --> F06f
  F06e --> F06f
  F06c -->|T3| F06g
  F06h -->|T4| F06f
  F06f --> F06i
  F06i --> F06j
  classDef t1 stroke:#2E7D32,stroke-width:2px
  class F06a,F06b,F06c,F06d,F06f,F06i,F06j t1
  classDef t2 stroke:#1565C0,stroke-width:2px
  class F06e t2
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F06g t3
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F06h t4
```

### F07 Kendali responsif dan adaptif

Mulai T4 detektor virtual dari kamera dipakai untuk actuated, pemilihan program menurut kondisi, dan offset dasar antar simpang berdekatan. Di T5 ditambah max-pressure jaringan dan pengendalian perimeter. Mode bayangan memastikan algoritma terbukti sebelum mengendalikan lampu.

![F07](diagram/F07_Kendali_responsif_dan_adaptif.png)

Tahap yang terlibat: T4, T5. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Detektor virtual kamera, loop, atau radar | Lapangan | edge/, controller | T4 |
| b. Gerbang kesehatan: adaptif hanya bila detektor sehat | Pusat | services/adaptive | T4 |
| c. Actuated dan pemilihan program per simpang (TRPS) | Pusat | services/adaptive | T4 |
| d. Offset dasar dan green wave sederhana simpang berdekatan | Pusat | services/adaptive | T4 |
| e. Max-pressure jaringan dan pengendalian perimeter | Pusat | services/network | T5 |
| f. Mode bayangan dan metrik kinerja sebagai pengamat | Pusat | shadow harness | T4 |
| g. Perintah lewat antarmuka controller | Komunikasi | services/cai | T4 |
| h. Controller menjalankan; jadwal lokal tetap cadangan | Lapangan | controller | T4 |
| i. Konsol adaptif: parameter, keputusan, nilai antara | Penyajian | apps/tmc-web | T4 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph U["Penyajian (layar & aplikasi)"]
    F07i["i. Konsol adaptif: parameter, keputusan, nilai antara (T4)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F07b["b. Gerbang kesehatan: adaptif hanya bila detektor sehat (T4)"]
    F07c["c. Actuated dan pemilihan program per simpang (TRPS) (T4)"]
    F07d["d. Offset dasar dan green wave sederhana simpang berdekatan (T4)"]
    F07e["e. Max-pressure jaringan dan pengendalian perimeter (T5)"]
    F07f["f. Mode bayangan dan metrik kinerja sebagai pengamat (T4)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F07g["g. Perintah lewat antarmuka controller (T4)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F07a["a. Detektor virtual kamera, loop, atau radar (T4)"]
    F07h["h. Controller menjalankan; jadwal lokal tetap cadangan (T4)"]
  end
  F07a --> F07b
  F07b --> F07c
  F07c --> F07d
  F07d -->|T5| F07e
  F07c --> F07g
  F07d --> F07g
  F07e --> F07g
  F07g --> F07h
  F07a --> F07f
  F07f --> F07i
  F07c --> F07i
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F07a,F07b,F07c,F07d,F07f,F07g,F07h,F07i t4
  classDef t5 stroke:#C62828,stroke-width:2px
  class F07e t5
```

### F08 Prioritas bus dan kendaraan darurat

Vision Tracker mengenali kendaraan prioritas sejak T3. Mulai T4 permintaan prioritas dari pelacakan bus dan pusat komando pemadam atau ambulans dinilai, dijaga batas keselamatannya, lalu dilayani lewat controller. Prioritas bus bersyarat berbasis muatan di T5.

![F08](diagram/F08_Prioritas_bus_dan_kendaraan_darurat.png)

Tahap yang terlibat: T3, T4, T5. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. AVL/APC operator bus; CAD pemadam dan ambulans | Pengguna | operator bus, 112/119 | T4 |
| j. Vision Tracker mengenali ambulans, damkar, dan pengawalan dari kamera | Pusat | services/vision | T3 |
| b. API mitra sesuai dokumen antarmuka | Komunikasi | integrasi (ICD) | T4 |
| c. Layanan permintaan prioritas: kelayakan dan antrean | Pusat | services/priority | T4 |
| d. Prioritas bersyarat berbasis muatan dan keterlambatan | Pusat | services/priority | T5 |
| e. Batas: pejalan kaki tidak dipotong, satu aktivasi per siklus, pemulihan | Pusat | services/priority | T4 |
| f. Perintah perpanjangan hijau atau preemption | Komunikasi | services/cai | T4 |
| g. Controller memberi hijau tambahan atau preempt | Lapangan | controller, edge/ | T4 |
| h. Konsol prioritas: permintaan, dilayani, dampak jalan samping | Penyajian | apps/tmc-web | T4 |
| i. Log dan KPI waktu tempuh bus dan waktu tanggap darurat | Pusat | services/metrics | T4 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F08a["a. AVL/APC operator bus; CAD pemadam dan ambulans (T4)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F08h["h. Konsol prioritas: permintaan, dilayani, dampak jalan samping (T4)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F08j["j. Vision Tracker mengenali ambulans, damkar, dan pengawalan dari kamera (T3)"]
    F08c["c. Layanan permintaan prioritas: kelayakan dan antrean (T4)"]
    F08d["d. Prioritas bersyarat berbasis muatan dan keterlambatan (T5)"]
    F08e["e. Batas: pejalan kaki tidak dipotong, satu aktivasi per siklus, pemulihan (T4)"]
    F08i["i. Log dan KPI waktu tempuh bus dan waktu tanggap darurat (T4)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F08b["b. API mitra sesuai dokumen antarmuka (T4)"]
    F08f["f. Perintah perpanjangan hijau atau preemption (T4)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F08g["g. Controller memberi hijau tambahan atau preempt (T4)"]
  end
  F08a --> F08b
  F08j -->|T4| F08c
  F08b --> F08c
  F08c -->|T5| F08d
  F08c --> F08e
  F08d --> F08e
  F08e --> F08f
  F08f --> F08g
  F08g --> F08i
  F08c --> F08h
  F08i --> F08h
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F08j t3
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F08a,F08b,F08c,F08e,F08f,F08g,F08h,F08i t4
  classDef t5 stroke:#C62828,stroke-width:2px
  class F08d t5
```

### F09 Bukti pelanggaran untuk ETLE Polri

Sistem hanya menyediakan bukti. Di T3 Vision Tracker mendeteksi pelanggaran tanpa membaca pelat. Di T4 kamera ANPR khusus dan API ke Back Office ETLE Polri ditambahkan; verifikasi dan penindakan tetap oleh petugas Polri.

![F09](diagram/F09_Bukti_pelanggaran_untuk_ETLE_Polri.png)

Tahap yang terlibat: T3, T4. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Vision Tracker mendeteksi terobos merah dan pelanggaran lain, tanpa pelat | Pusat | services/vision | T3 |
| b. Paket bukti: klip tersamarkan, waktu, lokasi | Pusat | services/evidence | T3 |
| c. Kontrol perlindungan data dan DPIA | Pusat | keamanan & kepatuhan | T3 |
| d. Pembacaan pelat dengan kamera ANPR khusus | Lapangan | kamera ANPR, edge/ | T4 |
| e. API ke Back Office ETLE sesuai Perpol 8/2023 | Komunikasi | integrasi (ICD Polri) | T4 |
| f. Petugas Polri memverifikasi dan menindak | Pengguna | Polri | T4 |
| g. Status tindak lanjut hanya-baca; laporan integrasi tahunan | Pusat | services/evidence | T4 |
| h. Dashboard keselamatan per simpang | Penyajian | apps/tmc-web | T3 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F09f["f. Petugas Polri memverifikasi dan menindak (T4)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F09h["h. Dashboard keselamatan per simpang (T3)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F09a["a. Vision Tracker mendeteksi terobos merah dan pelanggaran lain, tanpa pelat (T3)"]
    F09b["b. Paket bukti: klip tersamarkan, waktu, lokasi (T3)"]
    F09c["c. Kontrol perlindungan data dan DPIA (T3)"]
    F09g["g. Status tindak lanjut hanya-baca; laporan integrasi tahunan (T4)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F09e["e. API ke Back Office ETLE sesuai Perpol 8/2023 (T4)"]
  end
  subgraph L["Lapangan (kamera, kabinet, controller)"]
    F09d["d. Pembacaan pelat dengan kamera ANPR khusus (T4)"]
  end
  F09a --> F09b
  F09b --> F09c
  F09d -->|T4| F09b
  F09c -->|T4| F09e
  F09e --> F09f
  F09f -->|status| F09g
  F09b --> F09h
  F09g --> F09h
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F09a,F09b,F09c,F09h t3
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F09d,F09e,F09f,F09g t4
```

### F10 Keluhan publik dan jaminan layanan

Mulai T3 laporan warga masuk lewat aplikasi kota atau CRM, menjadi tiket dengan target waktu penyelesaian, dan didiagnosis dengan data Vision Tracker termasuk pemutaran ulang kondisi saat keluhan.

![F10](diagram/F10_Keluhan_publik_dan_jaminan_layanan.png)

Tahap yang terlibat: T3. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Warga melapor lewat aplikasi kota, CRM, atau telepon | Pengguna | CRM kota | T3 |
| b. API CRM dua arah | Komunikasi | integrasi CRM | T3 |
| c. Tiket, klasifikasi, target penyelesaian | Pusat | services/ticket | T3 |
| d. Diagnosis: jenis keluhan dipetakan ke data hitungan dan nyala lampu | Pusat | services/metrics | T3 |
| e. Pemutaran ulang kondisi saat keluhan | Pusat | PostgreSQL | T3 |
| f. Operator menindaklanjuti; tiket kerja bila perlu | Penyajian | apps/tmc-web | T3 |
| g. Jawaban ke pelapor; status dapat dilihat publik | Pengguna | CRM kota, dashboard publik | T3 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F10a["a. Warga melapor lewat aplikasi kota, CRM, atau telepon (T3)"]
    F10g["g. Jawaban ke pelapor; status dapat dilihat publik (T3)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F10f["f. Operator menindaklanjuti; tiket kerja bila perlu (T3)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F10c["c. Tiket, klasifikasi, target penyelesaian (T3)"]
    F10d["d. Diagnosis: jenis keluhan dipetakan ke data hitungan dan nyala lampu (T3)"]
    F10e["e. Pemutaran ulang kondisi saat keluhan (T3)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F10b["b. API CRM dua arah (T3)"]
  end
  F10a --> F10b
  F10b --> F10c
  F10c --> F10d
  F10d --> F10e
  F10d --> F10f
  F10e --> F10f
  F10f --> F10g
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F10a,F10b,F10c,F10d,F10e,F10f,F10g t3
```

### F11 Simulasi SUMO, digital twin, dan mode bayangan

Sejak T2 setiap rekomendasi diuji di SUMO dengan jaringan yang dibangun dari konfigurasi simpang. T3 mengkalibrasi twin per simpang dengan hitungan Vision Tracker. T4 menambah mode bayangan untuk algoritma adaptif. T5 membuka pasar algoritma.

![F11](diagram/F11_Simulasi_SUMO.png)

Tahap yang terlibat: T2, T3, T4, T5. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Jaringan simulasi dibangun dari konfigurasi simpang atau OSM | Pusat | sim/ | T2 |
| b. Kalibrasi twin per simpang dengan hitungan Vision Tracker | Pusat | sim/ | T3 |
| c. Skenario: jadwal baru (T2), insiden dan acara (T4), kebijakan TDM (T5) | Pusat | sim/ | T2 |
| d. Pekerja simulasi menjalankan beberapa bilangan acak | Pusat | sim/ worker | T2 |
| e. Mode bayangan: algoritma menerima data hidup tanpa mengendalikan lampu | Pusat | shadow harness | T4 |
| f. Veto statistik dan uji konflik prioritas | Pusat | services/adaptive | T4 |
| g. Universitas atau vendor mengajukan algoritma | Pengguna | portal mitra | T5 |
| h. Promosi bertahap: jam sepi, jam sibuk, hidup-mati | Pusat | services/adaptive | T4 |
| i. Hasil validasi di dashboard dan laporan | Penyajian | apps/tmc-web | T2 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F11g["g. Universitas atau vendor mengajukan algoritma (T5)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F11i["i. Hasil validasi di dashboard dan laporan (T2)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F11a["a. Jaringan simulasi dibangun dari konfigurasi simpang atau OSM (T2)"]
    F11b["b. Kalibrasi twin per simpang dengan hitungan Vision Tracker (T3)"]
    F11c["c. Skenario: jadwal baru (T2), insiden dan acara (T4), kebijakan TDM (T5) (T2)"]
    F11d["d. Pekerja simulasi menjalankan beberapa bilangan acak (T2)"]
    F11e["e. Mode bayangan: algoritma menerima data hidup tanpa mengendalikan lampu (T4)"]
    F11f["f. Veto statistik dan uji konflik prioritas (T4)"]
    F11h["h. Promosi bertahap: jam sepi, jam sibuk, hidup-mati (T4)"]
  end
  F11a -->|T3| F11b
  F11a --> F11c
  F11b --> F11c
  F11c --> F11d
  F11d --> F11i
  F11d -->|T4| F11e
  F11e --> F11f
  F11f --> F11h
  F11g -->|T5| F11d
  F11h --> F11i
  classDef t2 stroke:#1565C0,stroke-width:2px
  class F11a,F11c,F11d,F11i t2
  classDef t3 stroke:#EF6C00,stroke-width:2px
  class F11b t3
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F11e,F11f,F11h t4
  classDef t5 stroke:#C62828,stroke-width:2px
  class F11g t5
```

### F12 Platform banyak kota, data terbuka, dan pengelolaan permintaan perjalanan

Di T5 satu platform melayani banyak kota dengan data terpisah, membandingkan kinerja antar kota, mengoptimasi koridor dan jaringan, menghitung ambang legal kebijakan pembatasan, dan membuka data lewat API publik.

![F12](diagram/F12_Platform_banyak_kota.png)

Tahap yang terlibat: T4, T5. Langkah dan komponennya:

| Langkah | Lapisan | Komponen | Tahap |
|---|---|---|---|
| a. Kota-kota sebagai tenant; Kemenhub/BPTJ; provinsi | Pengguna | tenant | T5 |
| b. Isolasi data per tenant dan yurisdiksi | Pusat | apps/api | T4 |
| c. Optimasi koridor dan jaringan (bandwidth, Link Pivot, perimeter) | Pusat | services/network | T5 |
| d. Benchmark antar kota; kalkulator ambang kebijakan pembatasan | Pusat | services/tdm | T5 |
| e. Penasihat pembelajaran mesin yang hanya mengusulkan parameter | Pusat | services/advisor | T5 |
| f. API publik dan data terbuka; integrasi ERP dan ganjil-genap | Komunikasi | API gateway | T5 |
| g. Portal data terbuka dan dashboard benchmark | Penyajian | apps/tmc-web | T5 |
| h. Aplikasi navigasi, peneliti, warga | Pengguna | (pihak luar) | T5 |

Versi teks (mermaid):

```mermaid
flowchart LR
  subgraph P["Pengguna & mitra eksternal"]
    F12a["a. Kota-kota sebagai tenant; Kemenhub/BPTJ; provinsi (T5)"]
    F12h["h. Aplikasi navigasi, peneliti, warga (T5)"]
  end
  subgraph U["Penyajian (layar & aplikasi)"]
    F12g["g. Portal data terbuka dan dashboard benchmark (T5)"]
  end
  subgraph S["Pusat (laptop T1-T3, server T4+)"]
    F12b["b. Isolasi data per tenant dan yurisdiksi (T4)"]
    F12c["c. Optimasi koridor dan jaringan (bandwidth, Link Pivot, perimeter) (T5)"]
    F12d["d. Benchmark antar kota; kalkulator ambang kebijakan pembatasan (T5)"]
    F12e["e. Penasihat pembelajaran mesin yang hanya mengusulkan parameter (T5)"]
  end
  subgraph K["Komunikasi & integrasi"]
    F12f["f. API publik dan data terbuka; integrasi ERP dan ganjil-genap (T5)"]
  end
  F12a --> F12b
  F12b --> F12c
  F12b --> F12d
  F12b --> F12e
  F12c --> F12f
  F12d --> F12f
  F12d --> F12g
  F12f --> F12h
  F12g --> F12h
  classDef t4 stroke:#6A1B9A,stroke-width:2px
  class F12b t4
  classDef t5 stroke:#C62828,stroke-width:2px
  class F12a,F12c,F12d,F12e,F12f,F12g,F12h t5
```
