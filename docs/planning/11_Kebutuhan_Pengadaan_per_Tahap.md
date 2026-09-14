# 11 — Kebutuhan Pengadaan per Tahap (versi non-teknis)

Status: revisi 2026-09-14, menggantikan versi 2026-09-13. Dasar revisi adalah keputusan user T-39: **produk nol biaya sampai T3 selesai**, dan biaya administrasi bisnis diperbolehkan. Konteks lain: tim dua orang, pilot Bandung, T1 sampai T3 berjalan di laptop tim, dan pengadaan dimulai di T4 (`04` §8). Semua harga adalah **perkiraan 2026** untuk gambaran besaran, bukan penawaran, dan perlu diverifikasi sebelum membayar.

**Cara membaca.** Tiap baris adalah satu hal yang harus diadakan, baik dibeli, disewa, dipinjam, maupun diurus. Kolom tahap menunjukkan kapan paling tepat diadakan. Kolom konsekuensi menjelaskan apa yang terjadi bila hal itu tidak diadakan, terlambat, atau terlalu awal.

**Arti "nol pengadaan" sampai T3.** Tidak ada pembelian perangkat keras, lisensi perangkat lunak, data atau standar berbayar, maupun sewa server atau cloud. Yang boleh dibayar hanya biaya administrasi bisnis, yaitu cek dan pendaftaran merek, badan usaha, serta domain dan email. Prinsip lama tetap berlaku: jangan membeli sebelum ada pertanyaan yang hanya bisa dijawab dengan barang itu.

## 1. Ringkasan per tahap

| Tahap | Pengadaan produk | Biaya administrasi yang boleh | Pengganti tanpa biaya yang dipakai |
|---|---|---|---|
| T1 | tidak ada | cek merek dan domain (gratis) | laptop tim, perangkat lunak berlisensi bebas, GPU gratis Kaggle atau Colab, rekaman sendiri dan video publik |
| T2 | tidak ada | pendaftaran merek, domain dan email bisnis, PT Perorangan | stream uji dari rekaman lewat server stream lokal, demo langsung dari laptop |
| T3 | tidak ada | tidak ada tambahan wajib; konsultasi hukum untuk MoU dan DPIA bersifat opsional | stream Dishub dan izin baca controller lewat MoU, tetap di laptop tim |
| T4 | dimulai: server atau cluster, edge, kamera ANPR, adaptor dan controller uji, standar berbayar | sesuai kebutuhan kontrak | dibiayai kontrak pemda |
| T5 | sesuai kontrak | sesuai kontrak | dibiayai kontrak |

Perkiraan kas yang keluar sampai T3 hanya biaya administrasi, sekitar Rp 1 sampai 6 juta pada tahun pertama. Porsi terbesar adalah pendaftaran merek dua kelas, lalu email bisnis bila memilih layanan berbayar. Rinciannya ada di bagian 3.

## 2. Yang dipakai tanpa biaya sampai T3

| # | Item | Untuk apa | Mulai | Batasan dan catatan |
|---|---|---|---|---|
| A1 | Laptop tim (Ryzen 7 7730U, RAM 32 GB, GPU terintegrasi, ruang kosong sekitar 249 GB) | seluruh pekerjaan T1 sampai T3 | T1 (sudah ada) | tanpa GPU NVIDIA, sehingga model ringan dipilih untuk operasi; laptop menjadi titik tunggal kegagalan, jadi kode dan dokumen dicadangkan ke GitHub |
| A2 | Perangkat lunak berlisensi bebas: Python, PostgreSQL dan PostGIS, FFmpeg, OpenCV, ONNX Runtime, RF-DETR atau YOLOX, supervision, MediaMTX, SUMO, Label Studio, React, MapLibre | seluruh sistem | T1 | daftar lengkap dan lisensinya di `06` bagian 3 dan 4; Ultralytics YOLO (AGPL), Redis versi baru, dan EMQX tidak dipakai |
| A3 | GPU gratis Kaggle (utama) dan Google Colab (cadangan) | pra-label dan pelatihan model | T1 | kuota Kaggle sekitar 30 jam GPU per minggu dan dapat berubah; hanya data publik atau rekaman sendiri yang diunggah; data Dishub tetap diolah di laptop |
| A4 | GitHub privat dengan Git LFS 1 GB | kode dan dokumen | sudah ada | LFS terpakai sekitar 421 MB; video tidak disimpan di repositori |
| A5 | Standar dan regulasi yang gratis: PKJI 2023, MKJI 1997, Kep. Dirjen 273/1996, PM 49/2014, PM 96/2015, PM 76/2021, UU 22/2009, UU 27/2022, regulasi Jawa Barat dan Kota Bandung | rumus kalkulator, validator, kepatuhan | sudah ada | tersimpan di `docs/sources/` |
| A6 | NTCIP 1202 v03 dan NTCIP 1211 | model data controller dan objek prioritas | sebelum baca status controller di T3 | gratis setelah registrasi di ntcip.org; bila ternyata berbayar, pembeliannya ditunda ke T4 dan T3 memakai v02 yang sudah ada |
| A7 | Peta OpenStreetMap dan citra satelit dari layanan tanpa biaya | peta dan wizard konfigurasi | T2 | sumber citra dipilih lewat ADR-17 dengan syarat tanpa biaya dan atribusi dipenuhi; cadangannya berupa unggahan citra yang diskalakan manual |
| A8 | Ponsel tim | merekam simpang sendiri, uji stream dengan aplikasi kamera IP gratis, GPS logger | T1 | rekaman di ruang publik mengikuti aturan penyamaran wajah dan pelat |
| A9 | Sertifikat TLS (Let's Encrypt) dan VPN WireGuard | keamanan saat menerima stream Dishub | T3 | gratis |
| A10 | Webinar dan dokumentasi terbuka (FHWA, ITE, ATSPM UDOT, dokumentasi Roboflow dan SUMO) | pembelajaran tim | T1 | gratis |

## 3. Biaya administrasi yang diperbolehkan

| # | Item | Untuk apa | Tahap | Perkiraan biaya | Bila tidak atau terlambat | Bila terlalu awal |
|---|---|---|---|---|---|---|
| B1 | Cek merek "IRAMA" di PDKI dan ketersediaan domain | memastikan nama aman dipakai | sekarang (T1) | Rp 0 | ganti nama setelah materi dan repositori dibuat merugikan waktu dan kredibilitas | tidak ada |
| B2 | Pendaftaran merek kelas 9 (perangkat lunak) dan kelas 42 (jasa) | melindungi nama saat mulai dipresentasikan | akhir T1 atau awal T2 | Rp 500 ribu (tarif UMK) sampai Rp 1,8 juta per kelas | nama bisa didahului pihak lain setelah demo | tidak ada, selama nama sudah dicek |
| B3 | Badan usaha (PT Perorangan) dengan NPWP dan rekening | syarat MoU dengan Dishub, kerja sama vendor, hibah | sebelum MoU (akhir T2) | Rp 50 sampai 300 ribu lewat OSS | tidak bisa menandatangani MoU yang dibutuhkan T3 | kewajiban laporan pajak tahunan berjalan sebelum ada pendapatan, tetapi bebannya kecil untuk PT Perorangan |
| B4 | Domain (.id atau .co.id) dan email bisnis | kredibilitas saat menghubungi Dishub dan vendor | awal T2, sebelum kuesioner `12` dikirim | Rp 150 sampai 400 ribu per tahun, ditambah email Rp 0 sampai 70 ribu per pengguna per bulan | surat dari email gratisan kurang meyakinkan pejabat | biaya tahunan berjalan tanpa manfaat |
| B5 | Templat NDA dan perjanjian data | menerima dokumen protokol vendor dan rekaman Dishub | akhir T2 | Rp 0 bila disusun sendiri; konsultasi hukum opsional | vendor enggan berbagi dokumentasi; risiko perlindungan data saat menerima rekaman | tidak ada |
| B6 | Kebijakan privasi dan DPIA (penilaian dampak perlindungan data) | wajib sebelum memproses data kamera Dishub | awal T3 | Rp 0 bila disusun sendiri; konsultan opsional | Dishub tidak dapat menyerahkan stream; risiko sanksi UU 27/2022 | tidak ada |
| B7 | Teks lisensi open-core (Apache-2.0 untuk inti dan lisensi komersial untuk modul) | kejelasan hak saat kode dibagikan ke kampus atau vendor | T2 | Rp 0 | ambiguitas hak saat kolaborasi | tidak ada |
| B8 | TKDN perangkat lunak | syarat e-katalog dan tender pemda | T3, setelah badan usaha ada | Rp 0 (Kemenperin) | penjualan harus lewat mitra yang sudah terdaftar | tidak ada |
| B9 | Klausul batas tanggung jawab dalam MoU | melindungi tim saat Dishub menerapkan jadwal rekomendasi pada uji lapangan | T3 | Rp 0 | tuntutan bila terjadi kejadian saat uji lapangan | tidak ada |

## 4. Rencana lama yang ditunda ke T4 dan cara menutup celahnya

| # | Item | Rencana lama | Sekarang | Akibat penundaan | Cara menutup celah sampai T3 |
|---|---|---|---|---|---|
| C1 | Mini-PC atau Raspberry Pi di kabinet (edge ringan) | pertengahan T2 | T4 | ketahanan saat jaringan putus belum bisa didemokan | T1 sampai T3 tidak mengendalikan lampu, jadi kebutuhan ini baru muncul di T4 |
| C2 | Controller untuk uji di meja | akhir T2 | T4, diutamakan pinjam atau sewa dari vendor | adaptor kendali belum teruji pada alat sungguhan | T3 membaca status controller tanpa mengubah (dengan izin Dishub) untuk memahami protokol |
| C3 | Kamera IP uji | T2 | tidak dibeli | stream hanya diuji dari rekaman | MediaMTX memutar rekaman sebagai stream RTSP atau HLS; ponsel dapat berfungsi sebagai kamera IP; stream Dishub setelah MoU |
| C4 | Edge AI (Jetson) | awal T3 | T4 | Vision Tracker belum teruji 24 jam di kabinet | T3 berjalan di laptop dengan pilot terbatas; model ONNX yang sama tinggal dipindahkan |
| C5 | UPS dan switch PoE untuk rak uji | T3 | T4 | tidak ada | tidak diperlukan sebelum ada perangkat lapangan |
| C6 | Server pilot di kantor Dishub | T2 (dibiayai pembeli) | T4 | kapasitas T2 dan T3 terbatas pada satu laptop | jasa kajian dijalankan tim di laptop; batas kapasitas dicatat dan disampaikan ke pembeli |
| C7 | VM demo daring | akhir T1 | T4 atau dibiayai pembeli | tidak ada demo daring 24 jam | demo langsung dari laptop dan video demo |
| C8 | GPU cloud berbayar | T3 | tidak diperlukan | kuota GPU gratis dapat berubah atau habis | Kaggle dan Colab bergantian; bila kuota habis, latih model lebih kecil atau jalankan di CPU laptop semalaman |
| C9 | NEMA TS 2 dan TS 8 | T2 dan T4 | T4 | checklist keamanan kabinet disusun dari sumber sekunder | T1 sampai T3 tidak menyentuh kabinet |
| C10 | HCM edisi 7 | opsional T3 ke atas | hanya bila pembeli memintanya | tidak ada | PKJI 2023 dan PM 96/2015 cukup untuk Indonesia |
| C11 | Data probe komersial (TomTom, HERE) | opsional T3 ke atas | opsional T5 | tidak ada | Vision Tracker dan GPS logger ponsel |

## 5. Pengadaan mulai T4

| # | Item | Untuk apa | Perkiraan biaya | Catatan |
|---|---|---|---|---|
| D1 | Server pemda atau cluster tiga node (16 inti dan 64 GB per node) | pusat sistem skala kota | dibiayai kontrak; sewa VM sebagai alternatif | kapasitas penyimpanan ditetapkan lewat ADR-04 |
| D2 | Edge di simpang kritis (Jetson Orin Nano/NX atau PC industri bersertifikat) | Vision Tracker 24 jam sebagai detektor virtual | Rp 6 sampai 12 juta per unit untuk Jetson; PC industri bersertifikat lebih mahal | sertifikasi perangkat mengikuti PM 49/2014 Pasal 25; bila edge buatan sendiri belum bersertifikat, pakai perangkat vendor bersertifikat |
| D3 | Kamera ANPR khusus | pembacaan pelat untuk ETLE, Bapenda, DLH | sesuai spesifikasi Polri dan penawaran vendor | DPIA wajib diperbarui sebelum aktif |
| D4 | Controller uji dan adaptor | uji kendali di meja sebelum dipasang di lapangan | pinjam atau sewa Rp 0 sampai 5 juta; controller lokal baru Rp 30 sampai 80 juta; controller NTCIP impor lebih dari Rp 100 juta | diutamakan pinjam dari vendor merek kota pilot |
| D5 | Standar berbayar (NEMA TS 2 dan TS 8, NTCIP bila berbayar) | spesifikasi pengadaan dan keamanan kabinet | sekitar USD 300 sampai 600 per dokumen | dibeli bila kontrak mensyaratkan |
| D6 | UPS, switch PoE, rak uji | replika kabinet | Rp 2 sampai 4 juta | |
| D7 | Integrasi instansi (Polri, CAD, AVL, Bapenda, DLH, tol) | kemampuan T4 | umumnya lewat perjanjian tanpa biaya lisensi; biaya kerja integrasi masuk kontrak | tiap integrasi punya dokumen antarmuka |
| D8 | Teknisi lapangan mitra | pemasangan edge dan kamera | masuk kontrak atau MoU dengan Dishub atau vendor | tim inti tidak memiliki teknisi lapangan |

T5 dibiayai kontrak: cloud atau pusat data pemerintah, data OD atau probe untuk twin kota, dan kebutuhan multi-kota.

## 6. SDM dan pengetahuan

| # | Item | Tahap | Bentuk tanpa biaya sampai T3 | Bila tidak ada |
|---|---|---|---|---|
| E1 | Pendamping traffic engineer (dosen atau mahasiswa S2 dari ITB, Unpar, atau Itenas) | T1 sampai T3 | kolaborasi riset, magang, atau karya ilmiah bersama; honor baru bila ada pendanaan | kalkulator dan rekomendasi kurang divalidasi praktisi lain |
| E2 | Anotator data latih | T1 dan T2 | tim sendiri, sekitar 55 sampai 75 jam-orang sesuai `16`; magang bila ada | jadwal data latih mundur |
| E3 | Kontak Dishub dan vendor | T2 dan T3 | kuesioner `12`, pertemuan, MoU | MoU dan akses stream tertunda |
| E4 | Teknisi lapangan mitra | T4 | lewat kontrak | pemasangan edge tertunda |

## 7. Urutan yang disarankan (berbasis capaian, tanpa tanggal)

1. Sekarang: cek merek dan domain (B1); registrasi NTCIP bila gratis (A6). Biaya Rp 0.
2. T1: tidak membeli apa pun. Rekaman dan hitungan manual dikerjakan tim, model dilatih di GPU gratis.
3. Akhir T1 atau awal T2: daftarkan merek (B2), domain dan email (B4). Biaya sekitar Rp 1 sampai 6 juta, bergantung pada tarif merek dan pilihan email.
4. T2: tetap tanpa pembelian. Jasa kajian dijalankan di laptop, dan kuesioner `12` dikirim ke Dishub dan vendor.
5. Akhir T2: PT Perorangan (B3) dan templat NDA serta perjanjian data (B5), sebagai persiapan MoU.
6. T3: MoU dengan Dishub untuk akses stream, izin baca controller, dan uji lapangan; DPIA (B6); TKDN (B8).
7. T4: pengadaan dimulai sesuai kontrak dengan urutan server, adaptor dan controller uji, edge di simpang kritis, lalu kamera ANPR.

## 8. Risiko dari keputusan nol pengadaan dan cara menguranginya

| Risiko | Dampak | Pengurangan |
|---|---|---|
| Laptop rusak atau hilang | pekerjaan terhenti | kode dan dokumen dicadangkan ke GitHub; dataset berlabel disalin ke penyimpanan kedua yang sudah dimiliki; data Dishub dienkripsi |
| Kuota GPU gratis berubah atau dibatasi | pelatihan tertunda | dua layanan dipakai bergantian; model kecil; pelatihan di CPU laptop sebagai jalan terakhir |
| Kinerja laptop tidak cukup untuk rekaman panjang atau banyak stream | proses lambat, pilot T3 terbatas | model ringan, olah per batch, resolusi 720p; batas kapasitas disampaikan terbuka ke pembeli |
| Ruang disk habis karena video | rekaman tidak bisa diolah | video mentah dihapus setelah diolah kecuali sampel validasi; rekam atau unduh dalam 720p |
| Pembeli meminta demo daring atau kinerja skala kota sebelum T4 | penjualan tertunda | demo langsung dan video demo; skala kota diposisikan sebagai lingkup T4 yang dibiayai kontrak |

Rujukan: `04` (tahapan), `06` (arsitektur, teknologi, lisensi), `14` (arsitektur per tahap), `13` (data), `03` (pengadaan pemda dan TKDN), `docs/kb/03` (kepatuhan C-xx), `docs/kb/10` (keputusan dan pertanyaan terbuka).
