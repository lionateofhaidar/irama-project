# 04 — Konsep Tahapan Pengembangan (Tahap 1–5)

Status: revisi besar 2026-09-14 (menggantikan versi 2026-09-12 dan catatan revisi 2026-09-13). Dasar revisi: keputusan user T-34 s.d. T-42 di `docs/LOG_SESI.md`. Tahap diselesaikan berbasis capaian (tanpa tanggal target); perkiraan effort hanya untuk perencanaan sprint. Tag sumber: [R00]…[R07] catatan studi di `docs/sources/_ringkasan/`; [KB] basis pengetahuan `docs/kb/`; C-xx kebutuhan kepatuhan (KB-03 §B).

## 0. Prinsip lintas tahap

| # | Prinsip | Alasan dan sumber |
|---|---|---|
| P1 | **Nol pengadaan produk sampai T3 selesai.** Semua pekerjaan T1–T3 berjalan di laptop tim dengan perangkat lunak berlisensi bebas; pelatihan model memakai layanan GPU gratis; biaya administrasi bisnis (merek, badan usaha, domain) diperbolehkan | keputusan user T-39; dana terbatas, model "kembangkan dulu, jual kemudian" |
| P2 | **Risiko vendor lock-in minimal.** Kamera lewat standar RTSP/ONVIF, controller lewat NTCIP dan adaptor terpisah, data dalam format terbuka yang dapat diekspor, komponen berlisensi permisif, perangkat keras dan cloud bebas dipilih | PM 76/2021 Ps.4 "sistem terbuka, sesuai standar"; Perda Kota Bandung 12/2024 Ps.103 [R07]; keputusan user 2026-09-14 |
| P3 | **Transparan dan terukur.** Semua nilai antara perhitungan dan akurasi Vision Tracker ditampilkan; manfaat diukur dengan perbandingan eksisting dan rekomendasi, lalu uji lapangan sebelum-sesudah | HOP-11-027 Req 18.0 [R02]; klaim ITCS DKI tanpa metode [R06] |
| P4 | **Patuh standar Indonesia.** PKJI 2023 untuk kapasitas dan tundaan, LOS simpang PM 96/2015, minimal delapan jadwal PM 49/2014, UU PDP untuk data kamera | [R05], [KB-03] |
| P5 | **Keputusan tetap di tangan manusia.** T1–T3 menghasilkan rekomendasi dan bukti; kendali lampu baru dimulai di T4 dengan cadangan jadwal lokal di controller dan prioritas perintah petugas | UU 22/2009 Ps.104, 247 [R05]; D-01, D-05 [KB-10] |
| P6 | **Bertahap: satu simpang, banyak simpang mandiri, lalu koridor.** Koordinasi dasar di T4, optimasi koridor dan jaringan penuh di T5 | keputusan user T-34, T-35 |
| P7 | **Hemat data dan privasi.** Hanya angka dan peristiwa yang disimpan; video mentah dihapus setelah diolah kecuali sampel validasi yang disamarkan | UU PDP; hemat penyimpanan |
| P8 | **Kreatif tetapi berpijak.** Fitur baru harus menjawab kebutuhan lapangan yang terdokumentasi, dapat diukur, dan punya jalan kembali bila gagal | `01` §6 |

## 1. Ringkasan lima tahap

| Tahap | Nama kerja | Inti | Unit bukti | Komputasi dan pengadaan |
|---|---|---|---|---|
| **T1** | Purwarupa Hitung dan Rekomendasi | alur ujung ke ujung dari rekaman sampai rekomendasi waktu sinyal untuk satu simpang | 1 simpang, rekaman terbatas | laptop tim; nol pengadaan |
| **T2** | Vision Tracker dan Optimasi Simpang | kedua modul berjalan baik: hitungan per kelas, per arah, hambatan samping, nyala lampu; optimasi PKJI dengan beberapa mode; konfigurasi, tiga halaman dashboard, laporan, validasi SUMO, manfaat rupiah | 1 simpang lengkap semua lengan | laptop tim; GPU gratis untuk pelatihan; nol pengadaan |
| **T3** | Deteksi Kejadian dan Pemantauan Operasional | anomali (kendaraan prioritas, kejadian, pelanggaran sebagai bukti, kesehatan kamera dasar), pemantauan dan laporan wajib, controller baca-saja, ekspor jadwal, uji lapangan, optimasi multi-kriteria, akurasi 95% | beberapa simpang yang dihitung mandiri; pilot live setelah MoU | laptop tim; nol pengadaan |
| **T4** | Kendali Adaptif Terpadu | pengadaan dimulai: edge, ANPR, adaptor controller; kendali terpusat dan adaptif per simpang; offset dasar dan green wave sederhana; prioritas bus dan darurat; integrasi instansi; ruang kendali skala kota | kota, 50 sampai 300 simpang | server pemda atau cluster kecil; perangkat edge dan kamera khusus |
| **T5** | Platform Mobilitas Kota | optimasi koridor dan jaringan penuh, banyak kota, digital twin kota, pasar algoritma, TDM, data terbuka | regional atau nasional | cloud atau pusat data pemerintah |

T4 disebut setara ITCS DKI (tidak identik) karena seluruh kemampuan yang diklaim ITCS DKI sudah ada: actuated, adaptif mandiri, green wave terkoordinasi dasar, green wave VIP, prioritas bus, pengenalan kendaraan, prediksi, dan digital twin [Majalah §4; R06 D.2]. T5 melampaui ITCS DKI melalui optimasi jaringan, banyak kota, keterbukaan data, dan pasar algoritma yang teruji.

## 2. Tahap 1 — Purwarupa Hitung dan Rekomendasi

**Tujuan.** Membuktikan seluruh alur bekerja untuk satu simpang, dari rekaman CCTV sampai rekomendasi waktu siklus dan hijau yang sah menurut PKJI 2023.

**Definisi selesai.**
1. Vision Tracker mengolah rekaman semua pendekat satu simpang dan menghasilkan tabel hitungan enam kelas per pendekat per 15 menit.
2. Akurasi hitungan sekitar 90% pada siang hari untuk kelas utama, diuji pada klip yang tidak dipakai melatih.
3. Konfigurasi simpang sederhana (formulir) untuk geometri, fase, dan waktu lampu eksisting.
4. Kalkulator PKJI 2023 lolos uji terhadap contoh resmi PKJI 2023 Lampiran 12.5 dan Kep. Dirjen 273/1996 (c = 70 s, g = 28/30 s, C = 824, DS = 0,44), dengan cara uji di `15` bagian 4.4 [R00 G].
5. Rekomendasi mode Webster/PKJI baku dengan validator keselamatan waktu.
6. Dashboard dasar (volume, kapasitas, DJ, tundaan, LOS, rekomendasi) dan demo ujung ke ujung tanpa campur tangan engineer.

**Nilai bagi calon pembeli.** Bukti awal bahwa hitungan manual oleh surveyor dan perhitungan kinerja simpang dapat diotomasi dari CCTV yang sudah dimiliki pemda.

**Lingkup inti.** Epik E20 (sebagian), E21 (sebagian), E22 (formulir), E23 (dashboard dasar); kalkulator E03; registri simpang. Rincian di `05` dan `15`.

**Infrastruktur.** Laptop tim; Python, PostgreSQL; model deteksi berlisensi Apache-2.0 dijalankan dengan ONNX Runtime; pelatihan awal di GPU gratis.

**Sumber data.** Rekaman terbatas dari user (puncak dan non-puncak; pagi, malam, hujan; boleh dari simpang berbeda untuk uji akurasi), termasuk video publik; geometri dari citra satelit dan kunjungan singkat. Rincian di `13`.

**Integrasi.** Tidak ada.

**Kepatuhan.** C-30 (LOS PM 96), dasar C-09 (jadwal), keselamatan waktu (kuning, merah semua, hijau minimum).

**Validasi.** Uji regresi kalkulator terhadap contoh resmi; uji akurasi hitungan terhadap hitungan manual.

**Effort (perkiraan).** Sekitar 10 sampai 14 minggu kerja untuk tim dua orang, termasuk penyiapan data latih sesuai `16`.

**Risiko.** Motor yang berhimpitan menurunkan akurasi; sudut kamera rekaman publik tidak ideal; grafik PKJI tipe O dan faktor kelandaian perlu didigitalisasi [R00 G].

**Sengaja tidak dilakukan.** Stream langsung, pembacaan nyala lampu, hambatan samping otomatis, mode optimasi selain Webster, integrasi apa pun.

## 3. Tahap 2 — Vision Tracker dan Optimasi Simpang

**Tujuan.** Kedua modul berjalan baik untuk satu simpang lengkap sehingga produk dapat dijual sebagai jasa kajian dan perangkat lunak pendukung keputusan bagi Dishub.

**Definisi selesai.**
1. Satu simpang lengkap, semua lengan, dengan akurasi hitungan 90% siang dan 85% malam atau hujan per kelas per 15 menit.
2. Arah gerakan dari lintasan (dengan cadangan proporsi manual), hambatan samping empat jenis berbobot PKJI, pembacaan nyala lampu dari kamera, antrian dasar.
3. Mode stream langsung berfungsi dan diuji dengan rekaman yang diputar ulang sebagai stream lokal.
4. Lima mode optimasi (tundaan terendah, Webster/PKJI baku, DJ tertinggi minimal, siklus praktis minimum, pertahankan siklus eksisting) dan mode pembanding MKJI 1997.
5. Periode otomatis (maksimal delapan jadwal per jenis hari) dan periode yang ditentukan pengguna.
6. Wizard konfigurasi simpang dan data statis yang intuitif; tiga halaman dashboard; laporan kajian Word/PDF; validasi SUMO eksisting dan rekomendasi; perkiraan manfaat rupiah.
7. Seluruhnya berjalan di laptop tim tanpa pengadaan, dengan panduan pemakaian untuk engineer Dishub.

**Nilai bagi pembeli.** Kajian waktu sinyal yang biasanya membutuhkan survei manual dan konsultan berminggu-minggu dapat dihasilkan dari rekaman CCTV, lengkap dengan bukti simulasi dan nilai manfaat dalam rupiah, tanpa mengganti alat di lapangan.

**Lingkup inti.** Epik E20–E23 lengkap sesuai `15`; fitur pendukung E03 (editor jadwal, versi rekomendasi), E08 (agregasi dan retensi), E09 (evaluasi eksisting vs rekomendasi, manfaat), E14 (jaringan SUMO dari konfigurasi), E15 (RBAC dan audit dasar).

**Infrastruktur.** Laptop tim (CPU dan iGPU); layanan GPU gratis untuk pelatihan; server stream lokal (MediaMTX) untuk uji mode live.

**Sumber data.** Rekaman user dan video publik; rekaman seharian bila tersedia untuk pengelompokan jadwal otomatis; hitungan manual referensi untuk uji akurasi. Rekaman Dishub hanya setelah MoU.

**Integrasi.** Tidak ada integrasi sistem; pertukaran dengan Dishub lewat berkas rekaman dan laporan.

**Kepatuhan.** C-30 (LOS PM 96), C-09 (jadwal), C-19 sebagian (simulasi sebelum penetapan), C-40 dasar (keamanan data di laptop), prinsip PDP (penyamaran, retensi singkat).

**Validasi.** Uji akurasi hitungan per kondisi; perbandingan PKJI dan SUMO; uji regresi mode MKJI terhadap studi lama.

**Effort (perkiraan).** Sekitar 5 sampai 8 bulan kerja setelah T1 untuk tim dua orang.

**Risiko.** Sampel rekaman terbatas dan tersebar di simpang berbeda; performa laptop untuk rekaman panjang; hak cipta video publik; perbedaan hasil PKJI dan simulasi yang harus dijelaskan.

**Sengaja tidak dilakukan.** Kendali controller, deteksi anomali, pembacaan pelat, kesehatan kamera otomatis, koordinasi antar simpang, stream Dishub sebelum MoU, pengadaan apa pun.

## 4. Tahap 3 — Deteksi Kejadian dan Pemantauan Operasional

**Tujuan.** Menambah kemampuan operasional yang bernilai bagi ruang kendali tanpa pengadaan: mendeteksi kejadian penting, memantau kamera dan simpang, menyusun laporan wajib, dan membuktikan manfaat rekomendasi di lapangan.

**Definisi selesai.**
1. Deteksi kendaraan prioritas dan iring-iringan, kejadian lalu lintas (kendaraan berhenti atau mogok, dugaan kecelakaan, lawan arah, antrian menutup simpang), dan pelanggaran sebagai bukti (parkir di zona larangan, terobos merah, penyeberang di luar zebra); penindakan tetap oleh Polri.
2. Kesehatan kamera dasar: kamera tertutup, gelap, buram, atau bergeser memicu peringatan.
3. Kelas angkot dan pikap; akurasi 95% siang dan 90% malam atau hujan.
4. Waktu tunggu dan volume penyeberang; kecepatan dan waktu tempuh antar kamera tanpa pelat; antrian dan okupansi lengkap.
5. Mode optimasi multi-kriteria berbobot dan evaluasi skema fase alternatif.
6. Controller dibaca tanpa diubah (bila Dishub mengizinkan) dan lembar jadwal siap pakai diekspor untuk petugas.
7. Uji lapangan sebelum-sesudah pada minimal satu simpang: Dishub menerapkan jadwal rekomendasi, Vision Tracker mengukur perubahan tundaan dan antrian.
8. Pemantauan operasional: CCTV live view (setelah MoU), tiket keluhan, laporan wajib berbasis data vision (Forum LLAJ, kajian kecepatan dan V/C, laporan triwulan), dashboard publik sederhana.

**Nilai bagi pembeli.** Bukti manfaat nyata di lapangan, peringatan kejadian yang selama ini hanya dipantau mata operator, dan laporan wajib yang tersusun otomatis.

**Lingkup inti.** E20 (lanjutan T3), E21 (multi-kriteria, uji lapangan, ekspor jadwal), E06–E07 (kesehatan kamera, tiket), E09 (laporan wajib), E13 (CCTV live view), E16 (kejadian dan pelanggaran), E04 (NTCIP baca-saja). Rincian di `05`.

**Infrastruktur.** Laptop tim (keputusan user T-39); pilot live terbatas pada sedikit kamera dan tidak berjalan 24 jam.

**Sumber data.** Rekaman dan stream resmi Dishub setelah MoU; data AVL bus bila tersedia; hitungan manual untuk uji lapangan.

**Integrasi.** Baca status controller (NTCIP atau data vendor) bila diizinkan; ekspor jadwal dalam format yang dapat dibaca petugas atau vendor.

**Kepatuhan.** C-18 (notifikasi APILL tidak berfungsi), C-19 penuh (simulasi sebelum penetapan), C-20 dan C-21 (laporan), C-23 (portal publik), C-24 (bukti saja), C-26 dan C-37 (tata kelola data dan DPIA bila memproses data Dishub).

**Validasi.** Uji lapangan sebelum-sesudah; uji deteksi kejadian terhadap rekaman berlabel; mode bayangan untuk logika peringatan.

**Effort (perkiraan).** Sekitar 6 sampai 9 bulan kerja; tim bertambah 1 sampai 2 orang.

**Risiko.** MoU dan akses stream; keterbatasan laptop untuk pilot live; akurasi kejadian langka (kecelakaan) karena data latih sedikit.

**Sengaja tidak dilakukan.** Kendali lampu, pembacaan pelat, perangkat edge, integrasi ETLE/Bapenda/DLH, koordinasi antar simpang, pengadaan apa pun.

## 5. Tahap 4 — Kendali Adaptif Terpadu

**Tujuan.** Setara fungsi ITCS DKI dengan standar terbuka: kendali terpusat dan adaptif, koordinasi dasar, prioritas bus dan darurat, integrasi lintas instansi, dan ruang kendali skala kota. Pengadaan dimulai di tahap ini.

**Definisi selesai.**
1. Adaptor controller NTCIP 1202/1211 dan minimal satu protokol vendor lokal lewat perangkat edge di kabinet; detak jantung dan cadangan jadwal lokal teruji dengan memutus jaringan.
2. Kendali terpusat (pilih program, mode manual petugas, sinkron jam) dengan jejak audit; alarm controller dan detektor.
3. Adaptif per simpang dari detektor virtual kamera: actuated dan penyesuaian pembagian hijau dengan batas perubahan per siklus; pemilihan program menurut kondisi (TRPS); prediksi volume 15 sampai 60 menit.
4. Offset dasar dan green wave sederhana untuk simpang berdekatan, termasuk green wave terjadwal untuk rute VIP.
5. Prioritas bus berbasis aturan (perpanjangan hijau dan hijau lebih awal) dan prioritas kendaraan darurat bertingkat.
6. Pembacaan pelat (ANPR) dengan kamera khusus; bukti ke Back Office ETLE Polri; integrasi Bapenda, DLH, CAD pemadam dan ambulans, AVL bus, pengelola tol, cuaca.
7. Kesehatan kamera lanjutan (hujan lebat, genangan, silau); ruang kendali skala kota dengan video wall; keamanan NEMA TS 8 dan mTLS; RBAC per yurisdiksi.

**Nilai bagi pembeli.** Kemampuan setara ITCS dengan biaya dan ketergantungan vendor yang terkendali, disertai bukti manfaat yang dapat dipertanggungjawabkan ke DPRD.

**Infrastruktur.** Server pemda atau cluster kecil tiga node; perangkat edge di simpang kritis; kamera ANPR khusus. Daftar di `11`.

**Kepatuhan.** Seluruh C-01…C-43, PM 76/2021 Ps.7 lengkap, Perpol 8/2023 dan 2/2025 untuk ETLE, UU PDP untuk ANPR.

**Validasi.** Simulasi di twin, uji di meja dengan controller, mode bayangan, penerapan di jam sepi lalu jam sibuk, perbandingan hidup-mati.

**Effort (perkiraan).** Sekitar 9 sampai 15 bulan; tim membesar sesuai kontrak.

**Risiko.** Protokol vendor tertutup; kewenangan Polri dan Dirjen/BPTJ; kebutuhan dana pengadaan; SDM operator.

**Sengaja tidak dilakukan.** Optimasi koridor dan jaringan penuh, pengendalian perimeter, pembelajaran mesin sebagai pengendali langsung, banyak kota.

## 6. Tahap 5 — Platform Mobilitas Kota (rekomendasi end-state)

**Tujuan.** Satu platform untuk banyak kota yang terbuka, dapat diaudit, dan berkembang lewat algoritma teruji.

**Komponen.**
1. Optimasi koridor dan jaringan: bandwidth green wave, penalaan offset dari data kedatangan dan GPS (Link Pivot, diagram waktu-ruang siklik), max-pressure jaringan dengan pemilihan simpang kritis, pengendalian perimeter kawasan jenuh, prioritas bus bersyarat berbasis muatan dan keterlambatan, toolkit kondisi jenuh.
2. Banyak kota (multi-tenant) dengan perbandingan kinerja antar kota untuk Kemenhub/BPTJ.
3. Digital twin kota untuk uji kebijakan (ganjil-genap, penutupan jalan, acara).
4. Pasar algoritma yang wajib lolos simulasi dan mode bayangan dengan veto statistik.
5. TDM berbasis data (ambang V/C dan kecepatan PP 32/2011), data terbuka dan API publik, analitik tanpa detektor dari data GPS, penasihat berbasis pembelajaran mesin, siaran status lampu ke aplikasi navigasi, keselamatan pejalan kaki dengan fusi kamera dan radar.

**Definisi selesai (indikatif).** Minimal tiga kota tenant; minimal satu koridor dengan optimasi jaringan aktif; minimal satu algoritma pihak ketiga lolos jalur uji; API publik dengan SLA.

## 7. Perbandingan ITCS DKI, T4, dan T5

| Aspek | ITCS DKI (klaim) | IRAMA T4 | IRAMA T5 |
|---|---|---|---|
| Deteksi | kamera analitik, fisheye, ANPR per simpang, edge AI | Vision Tracker di edge, ANPR khusus, detektor virtual | ditambah fusi radar dan analitik GPS |
| Kendali | actuated, adaptif, green wave terkoordinasi, green wave VIP, prioritas bus | adaptif per simpang, TRPS, offset dasar dan green wave sederhana, VIP, prioritas bus dan darurat | optimasi koridor dan jaringan, perimeter, pasar algoritma |
| Evaluasi | klaim 20–30% tanpa metode terbuka | eksisting vs rekomendasi, uji lapangan, LOS PM 96, akurasi terbuka | ditambah perbandingan antar kota dan audit publik |
| Standar | tidak dipublikasikan | RTSP/ONVIF, NTCIP 1202/1211, PKJI 2023, PM 96 | ditambah data terbuka |
| Skala | 321 simpang satu kota | 50–300 simpang satu kota | regional dan nasional |

## 8. Pengadaan dan komputasi per tahap

| Tahap | Komputasi | Pengadaan |
|---|---|---|
| T1–T3 | laptop tim; GPU gratis untuk pelatihan | tidak ada (biaya administrasi bisnis diperbolehkan) |
| T4 | server pemda atau cluster kecil; edge di simpang | edge, kamera ANPR, adaptor controller, standar NTCIP versi terbaru bila berbayar |
| T5 | cloud atau pusat data pemerintah | dibiayai kontrak |

Rincian dan konsekuensi di `11_Kebutuhan_Pengadaan_per_Tahap.md`.

## 9. Prasyarat lintas tahap

- T1: rekaman sesuai `13`, panduan data latih `16`, keputusan model deteksi (ADR).
- T2: rekaman satu simpang lengkap; hitungan manual referensi; parameter ekonomi terbaru.
- T3: MoU dengan Dishub (akses stream, izin baca controller, uji lapangan).
- T4: kontrak dengan pemda dan anggaran pengadaan.

## 10. Catatan perubahan

- 2026-09-14: T2 difokuskan pada Vision Tracker dan Optimasi Simpang; T1 menjadi purwarupa ujung ke ujung; nol pengadaan sampai T3; kendali controller pindah ke T4; ANPR ke T4; optimasi koridor ke T5 dengan offset dasar di T4; fitur pemantauan dan laporan ke T3.
- 2026-09-13 (tidak berlaku lagi): edge-light di T2, pelat di T3.
