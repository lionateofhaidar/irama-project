# 15 — Spesifikasi Modul Vision Tracker dan Optimasi Waktu Simpang

Status: 2026-09-14, berdasarkan keputusan user T-34 s.d. T-42 (`docs/LOG_SESI.md`). Dokumen ini menjadi acuan utama keluaran T2. Angka kinerja komputasi dan waktu kerja adalah perkiraan yang diuji ulang di T1.

Ringkasan. T2 menghasilkan dua modul yang berjalan baik untuk satu simpang lengkap. Vision Tracker mengubah rekaman atau stream CCTV menjadi tabel hitungan kendaraan per kelas, per arah, dan per 15 menit, ditambah hitungan hambatan samping dan pembacaan nyala lampu. Modul Optimasi Waktu Simpang mengubah tabel itu menjadi arus dalam satuan mobil penumpang, menghitung kinerja simpang dengan PKJI 2023, lalu merekomendasikan waktu siklus dan waktu hijau terbaik per periode dengan beberapa mode yang bisa dipilih. Keduanya dilengkapi konfigurasi simpang yang mudah, tiga halaman dashboard, laporan kajian otomatis, perkiraan manfaat rupiah, dan validasi di simulator SUMO. Pada T2 produk berperan sebagai sistem pendukung keputusan; rekomendasi diterapkan petugas secara manual.

## 1. Posisi kedua modul dalam produk

| Aspek | Keputusan T2 |
|---|---|
| Lingkup bukti | Satu simpang lengkap, semua lengan. Analisis tingkat koridor di T5; koordinasi dasar (offset) di T4 |
| Peran produk | Sistem pendukung keputusan untuk engineer Dishub. Tidak mengendalikan lampu |
| Cara penyerahan awal | Jasa kajian: Dishub memberi rekaman, tim menjalankan IRAMA di laptop dan menyerahkan dashboard serta laporan. Perangkat lunak yang sama nanti dipasang di server pemda |
| Standar hitung | PKJI 2023 utama; mode MKJI 1997 untuk pembanding studi lama dan uji regresi |
| Kelas LOS resmi | Tundaan rata-rata simpang (PM 96/2015). Derajat kejenuhan (DJ) ditampilkan sebagai pendukung, batas desain 0,85 |
| Sumber video | Rekaman (termasuk video publik) sampai ada MoU. Mode stream diuji dengan rekaman yang diputar ulang sebagai stream lokal |
| Komputasi | Laptop tim (CPU AMD Ryzen 7 7730U, RAM 32 GB, tanpa GPU NVIDIA) sampai T3 selesai. Pelatihan model memakai layanan GPU gratis |
| Pengadaan | Nol biaya produk sampai T3 selesai. Biaya administrasi bisnis (merek, badan usaha, domain) diperbolehkan |
| Lisensi komponen AI | Hanya berlisensi permisif (Apache-2.0, MIT, BSD). Ultralytics YOLO (AGPL) tidak dipakai |
| Acuan metode | Rantai perhitungan kinerja simpang bersinyal pada naskah tugas akhir user (dokumen lokal, tidak dipush), diperbarui ke PKJI 2023 dan PM 96/2015 |

## 2. Alur kerja pengguna di T2

1. Engineer membuat simpang baru lewat wizard konfigurasi (lokasi, lengan, lebar, fase, waktu lampu eksisting, parameter kebijakan).
2. Engineer mengunggah rekaman per pendekat atau menautkan stream, lalu menandai garis hitung, arah keluar, zona hambatan samping, dan area kepala lampu di cuplikan kamera.
3. Vision Tracker memproses video dan mengisi tabel hitungan per 15 menit, tabel hambatan samping, tabel status lampu, dan perkiraan antrian.
4. Halaman kualitas data menunjukkan jam yang hilang, kondisi malam atau hujan, dan hasil uji akurasi; engineer dapat mengoreksi atau mengisi proporsi belok manual.
5. Periode rekomendasi ditentukan otomatis (paling banyak delapan jadwal per jenis hari) atau diatur manual.
6. Modul Optimasi menghitung semua mode sekaligus; engineer memilih mode yang ditampilkan dan yang dijadikan rekomendasi.
7. Rekomendasi diuji di simulator SUMO dan dibandingkan dengan kondisi eksisting.
8. Engineer mengunduh laporan kajian (Word atau PDF) dan menyampaikannya ke Kepala Dinas.
9. Setelah disetujui, petugas menerapkan waktu baru di controller secara manual (T2). Mulai T3 sistem menyediakan lembar jadwal siap pakai dan uji lapangan sebelum-sesudah; mulai T4 jadwal dikirim langsung ke controller.

## 3. Modul Vision Tracker

### 3.1 Masukan

| Masukan | Format | Tahap |
|---|---|---|
| Rekaman per kamera | MP4, MKV, AVI, atau ekspor NVR; resolusi minimal 720p disarankan | T1 |
| Metadata rekaman | simpang, kamera, pendekat yang terlihat, tanggal, jam mulai, kondisi (siang, malam, hujan), sumber dan izin | T1 |
| Stream langsung | RTSP atau HLS. Di T2 diuji dengan rekaman yang diputar ulang lewat server stream lokal (MediaMTX); stream Dishub setelah MoU | T2 |
| Garis dan zona | garis masuk per pendekat, zona keluar per arah, zona hambatan samping dengan panjang segmen, area kepala lampu, zona antrian per lajur | T1 dasar, T2 lengkap |

Rekaman untuk satu simpang boleh berupa kumpulan klip terbatas (puncak, non-puncak, pagi, malam, hujan). Klip kondisi boleh berasal dari simpang berbeda bila hanya dipakai untuk uji akurasi. Rekomendasi waktu sinyal untuk satu simpang tetap membutuhkan hitungan semua lengan pada periode yang sama.

### 3.2 Kelas objek dan pemetaannya

| Kelas rinci | Tahap | Kelas PKJI 2023 | Kelas MKJI 1997 (mode pembanding) |
|---|---|---|---|
| Sepeda motor | T1 | SM | MC |
| Mobil (termasuk angkot dan pikap sampai T2) | T1 | MP | LV |
| Angkot | T3 (dipisah dari mobil) | MP | LV |
| Pikap | T3 (dipisah dari mobil) | MP | LV |
| Bus | T1 | KS | HV |
| Truk | T1 | KS | HV |
| Kendaraan tak bermotor (sepeda, becak, gerobak) | T1 | KTB, tidak dikonversi ke SMP; masuk rasio KTB dan hambatan samping | UM |
| Pejalan kaki | T1 | kejadian hambatan samping | kejadian hambatan samping |
| Ambulans, damkar, mobil polisi dengan lampu menyala, iring-iringan | T3 | MP atau KS menurut bentuk; ditandai sebagai kendaraan prioritas | LV atau HV |

Kelas rinci selalu disimpan. Pemetaan ke PKJI dilakukan otomatis dan dapat ditinjau. Pemisahan bus dan truk sejak T1 dipakai untuk perhitungan manfaat rupiah.

### 3.3 Proses

| Tahap proses | Cara kerja | Komponen (lisensi) |
|---|---|---|
| Ambil gambar | video dibaca per bingkai pada laju tetap (mis. 10 bingkai per detik) | FFmpeg (LGPL, dipanggil sebagai program terpisah), OpenCV (Apache-2.0) |
| Deteksi | model pendeteksi objek mengenali kendaraan dan pejalan kaki beserta kelasnya | RF-DETR atau YOLOX (Apache-2.0), dijalankan dengan ONNX Runtime (MIT) di CPU atau iGPU |
| Pelacakan | objek yang sama diikuti antar bingkai dan diberi nomor unik | ByteTrack (MIT) |
| Hitung gerakan | lintasan yang memotong garis masuk lalu masuk zona keluar tertentu dicatat sebagai lurus, belok kiri, belok kiri langsung, atau belok kanan | supervision (MIT) dan logika IRAMA |
| Cadangan arah | bila arah keluar tidak terlihat kamera, hitungan pendekat dibagi menurut proporsi belok hasil survei singkat atau kamera lain; sumbernya ditandai | logika IRAMA |
| Hambatan samping | empat jenis kejadian dihitung di zona sisi jalan: pejalan kaki di badan jalan atau menyeberang, kendaraan berhenti atau parkir (diam lebih dari batas waktu, mis. 10 detik), kendaraan keluar-masuk sisi jalan, dan kendaraan lambat (KTB) | logika IRAMA |
| Nyala lampu | warna di area kepala lampu dibaca per bingkai dan dihaluskan terhadap waktu, menghasilkan awal hijau, kuning, dan merah, sehingga siklus dan waktu hijau eksisting terukur otomatis | OpenCV |
| Antrian dasar | jumlah kendaraan diam di zona lajur saat akhir merah dan okupansi garis henti | logika IRAMA |
| Penyamaran | wajah dan pelat pada cuplikan yang disimpan diburamkan; video mentah tidak disimpan setelah diolah, kecuali sampel validasi | OpenCV |

### 3.4 Keluaran tabel terstruktur

| Tabel | Kolom utama | Dipakai oleh |
|---|---|---|
| hitung_15m | simpang, kamera, pendekat, gerakan (lurus, belok kiri, belok kiri langsung, belok kanan), kelas rinci, kelas PKJI, waktu mulai, jumlah, sumber (vision, manual, proporsi), skor mutu, kondisi | konversi arus, dashboard, laporan |
| hambatan_samping_15m | simpang, pendekat, jenis kejadian, jumlah, panjang segmen terlihat (m), frekuensi berbobot per 200 m per jam, kelas KHS | faktor hambatan samping, dashboard |
| status_lampu | simpang, kepala lampu atau fase, waktu, warna, sumber (kamera, manual, controller mulai T3) | waktu eksisting, evaluasi |
| antrian_1m | simpang, pendekat, lajur, waktu, jumlah kendaraan diam, perkiraan panjang antrian (m), okupansi garis henti | pembanding hitungan PKJI |
| peristiwa (T3) | jenis kejadian, waktu, lokasi, klip bukti tersamarkan, tingkat keyakinan, status tindak lanjut | pemantauan operasional |
| mutu_rekaman | rekaman, jam valid, persentase bingkai terbaca, kondisi, catatan (kamera bergeser, tertutup) | halaman kualitas data |

Hambatan samping dihitung sesuai PKJI 2023. Frekuensi berbobot = pejalan kaki × 0,5 + kendaraan berhenti × 1,0 + keluar-masuk × 0,7 + kendaraan lambat × 0,4, dinormalkan ke per 200 m per jam dan kedua sisi jalan. Kelasnya: sangat rendah <100, rendah 100–299, sedang 300–499, tinggi 500–899, sangat tinggi ≥900. Untuk faktor hambatan samping simpang, kelas dipetakan menjadi rendah (sangat rendah dan rendah), sedang, dan tinggi (tinggi dan sangat tinggi). Pemetaan ini adalah asumsi terdokumentasi yang dapat dikoreksi engineer.

### 3.5 Target akurasi hitungan

| Tahap | Siang cerah | Malam atau hujan | Cara uji |
|---|---|---|---|
| T1 | sekitar 90% per kelas utama | sekitar 85% | klip uji yang tidak dipakai melatih, dibanding hitungan manual per 15 menit |
| T2 | 90% per kelas per 15 menit | 85% | sama, untuk semua lengan simpang pilot |
| T3 dan seterusnya | 95% | 90% | sama, ditambah uji di beberapa simpang dan kondisi |

Akurasi per kelas = 1 − |hitungan vision − hitungan manual| / hitungan manual, dihitung per 15 menit lalu dirata-ratakan. Target T1–T2 sengaja lebih rendah 5% (keputusan user) agar data latih bisa disiapkan dengan cepat; penalaan mencapai 95%/90% dilakukan mulai T3. Hasil akurasi selalu ditampilkan di dashboard dan laporan.

### 3.6 Perkiraan kinerja di laptop

| Pekerjaan | Perkiraan | Keterangan |
|---|---|---|
| Mengolah rekaman | 2 sampai 5 kali lebih cepat dari waktu nyata per kamera dengan model ringan pada 10 bingkai per detik | diukur ulang di T1; menentukan pilihan model |
| Stream langsung | 2 sampai 4 stream bersamaan | cukup untuk satu simpang |
| Rekaman satu simpang, 4 kamera, 17 jam, 2 hari | sekitar 1 sampai 2 hari komputasi, bisa berjalan semalaman | bila rekaman seharian tersedia |

### 3.7 Privasi dan sumber data

- Hanya angka dan peristiwa yang disimpan; video mentah dihapus setelah diolah, kecuali sampel validasi yang wajah dan pelatnya disamarkan.
- Setiap rekaman dicatat di register sumber (asal, tautan, izin atau lisensi, tanggal, kegunaan). Video publik termasuk YouTube dipakai untuk uji dan latih sesuai keputusan user; risikonya dicatat di dokumen asumsi dan risiko.
- Rekaman Dishub hanya diolah di laptop tim dan tidak diunggah ke layanan cloud.

### 3.8 Peta jalan Vision Tracker

| Tahap | Kemampuan |
|---|---|
| T1 | rekaman satu simpang; enam kelas; garis hitung per pendekat; tabel hitungan 15 menit |
| T2 | arah gerakan dari lintasan dengan cadangan proporsi manual; hambatan samping empat jenis berbobot; pembacaan nyala lampu; antrian dasar; mode stream (diuji dengan rekaman yang diputar ulang); uji akurasi; penyamaran |
| T3 | kelas angkot dan pikap; kendaraan prioritas dan iring-iringan; kejadian lalu lintas (berhenti, dugaan kecelakaan, lawan arah, antrian menutup simpang); pelanggaran sebagai bukti (parkir di zona larangan, terobos merah, penyeberang di luar zebra); kesehatan kamera dasar (tertutup, gelap, buram, bergeser); waktu tunggu dan volume penyeberang; kecepatan dan waktu tempuh antar kamera tanpa pelat; antrian dan okupansi lengkap; penalaan akurasi ke 95%/90% |
| T4 | berjalan di perangkat edge untuk banyak kamera 24 jam; pembacaan pelat (ANPR) dengan kamera khusus; kesehatan kamera lanjutan (hujan lebat, genangan, silau); detektor virtual untuk kendali adaptif |
| T5 | fusi kamera dan radar untuk keselamatan pejalan kaki; analitik multi-kota |

## 4. Modul Optimasi Waktu Simpang

### 4.1 Masukan

- Tabel hitungan dan hambatan samping dari Vision Tracker, atau unggahan CSV hasil survei manual, atau input langsung di layar.
- Konfigurasi simpang (geometri tiap pendekat, gerakan yang diizinkan, fase dan waktu lampu eksisting).
- Parameter kebijakan dan ekonomi (lihat bagian 5).

### 4.2 Penentuan periode

| Cara | Kapan dipakai | Keterangan |
|---|---|---|
| Otomatis | rekaman panjang (misalnya seharian) tersedia | profil 15 menit dikelompokkan menjadi paling banyak delapan jadwal per jenis hari (hari kerja, akhir pekan), sesuai PM 49/2014; setiap jadwal berdurasi minimal 30 menit dan berurutan dalam waktu |
| Manual | sampel terbatas atau kebutuhan khusus | engineer menentukan jam mulai dan selesai setiap periode di konfigurasi simpang |
| Pilihan cepat | kajian cepat | periode baku puncak pagi, siang, sore, dan non-puncak |

Arus desain setiap periode default = arus satu jam tertinggi di dalam periode itu (empat interval 15 menit berurutan), dengan faktor jam puncak ditampilkan. Pilihan lain: rata-rata periode. Faktor K dari LHRT hanya dipakai bila yang tersedia hanya data harian.

### 4.3 Konversi arus

Arus SMP per jam = jumlah kendaraan per kelas × EMP. EMP PKJI 2023 untuk simpang APILL: MP 1,00; KS 1,30; SM 0,15 pada pendekat terlindung dan 0,40 pada pendekat terlawan. KTB tidak dikonversi dan dihitung sebagai rasio KTB untuk faktor hambatan samping. Rasio belok kiri, belok kanan, dan belok kiri langsung dihitung per pendekat.

### 4.4 Rantai perhitungan PKJI 2023

1. Lebar efektif (LE) dari lebar pendekat, lebar masuk, lebar keluar, dan lajur belok kiri langsung.
2. Arus jenuh dasar: tipe P = 600 × LE; tipe O dari tabel hasil digitalisasi grafik PKJI.
3. Faktor koreksi: ukuran kota (dari jumlah penduduk), hambatan samping (tipe lingkungan, kelas hambatan samping, tipe fase, rasio KTB), kelandaian, parkir, belok kanan, belok kiri.
4. Arus jenuh terkoreksi, rasio arus per pendekat, rasio arus kritis per fase, rasio arus simpang.
5. Waktu kuning 3 detik, merah semua dari jarak konflik dan kecepatan (PKJI 5-9), waktu hijau hilang total.
6. Waktu siklus dan waktu hijau menurut mode optimasi yang dipilih (bagian 4.5).
7. Kapasitas per pendekat = arus jenuh × hijau / siklus; derajat kejenuhan = arus / kapasitas.
8. Antrian (Nq1 dengan kapasitas C sesuai keputusan Q-11, Nq2, Nq, Nqmax), panjang antrian, rasio dan jumlah kendaraan terhenti.
9. Tundaan lalu lintas, tundaan geometrik, tundaan per pendekat, tundaan rata-rata simpang tertimbang arus.
10. Kelas LOS PM 96/2015: A <5, B 5–15, C 15–25, D 25–40, E 40–60, F >60 detik per kendaraan.

Mode MKJI 1997 menjalankan rantai yang sama dengan faktor dan EMP MKJI untuk dibandingkan dengan studi lama. Uji regresi memakai angka studi lama sebagai pembanding per baris formulir.

Uji regresi kalkulator memakai dua contoh resmi dengan cara berikut.

- **Contoh PKJI 2023 Lampiran 12.5** (contoh 1 Jl. Iskandarsyah dan Jl. Wijaya, Jakarta, dengan pengaturan empat fase dan tiga fase; contoh 2 perencanaan simpang APILL baru). Contoh ini memakai EMP dan faktor PKJI 2023, sehingga dijalankan dari data Formulir SA-I sampai SA-III lalu dibandingkan dengan Formulir SA-IV, SA-V, dan Tabel 12-9. Untuk contoh 1 empat fase, nilai acuannya RAS 0,777, siklus 117 detik, DJ 0,88, dan tundaan rata-rata 51,2 detik/SMP. Nilai Formulir SA-IV dan SA-V dibaca dari berkas PDF karena teks ekstraksinya bertumpuk. Contoh ini juga dipakai untuk memeriksa Q-11 (Nq1 dengan kapasitas C) dan hasil digitalisasi grafik (F-T1-17).
- **Contoh Kep. Dirjen 273/1996 Bab X** (Yogyakarta, dua fase, semua pendekat terlawan). Contoh ini memakai EMP tahun 1996, yaitu kendaraan tak bermotor dikonversi 0,5 atau 1,0 dan ikut dihitung dalam arus, serta arus jenuh dasar tipe O dari grafik. PKJI 2023 tidak mengonversi KTB ke SMP. Karena itu uji T1 memasukkan arus (SKR/jam) dan arus jenuh terkoreksi per pendekat dari Formulir APILL-IV contoh itu, lalu memeriksa bagian rumus yang sama di kedua pedoman: rasio arus simpang sekitar 0,67, siklus 70 detik, hijau 28 dan 30 detik, kapasitas pendekat utara 824 SKR/jam, dan DJ 0,44. Uji dari LHR sampai kinerja memerlukan set parameter Dirjen 273/MKJI dan grafik tipe O, sehingga dijalankan bersama mode MKJI di T2 (F-T2-162).

Kapasitas per arah ditampilkan sebagai berikut. Bila gerakan memiliki lajur khusus, kapasitas dihitung untuk lajur itu. Bila lajur dipakai bersama, kapasitas pendekat dibagi menurut porsi arus gerakan dan ditandai sebagai kapasitas bersama.

### 4.5 Mode optimasi yang dapat dipilih

Semua mode dihitung bersamaan untuk setiap periode. Pengguna memilih mode yang ditampilkan dan mode yang dijadikan rekomendasi resmi.

| Mode | Cara kerja | Cocok untuk | Tahap |
|---|---|---|---|
| Tundaan terendah dengan batasan | mulai dari siklus Webster, lalu mencoba siklus 40–130 detik per 1 detik dan pembagian hijau yang memberi tundaan rata-rata simpang terendah, dengan batas DJ ≤0,85 bila memungkinkan dan hijau minimum | rekomendasi default | T2 |
| Webster / PKJI baku | siklus Webster; hijau sebanding rasio arus kritis, persis prosedur buku | pembanding resmi dan kajian yang harus mengikuti prosedur baku | T1 |
| Minimalkan DJ tertinggi | hijau dibagi agar DJ pendekat kritis setara; siklus dipilih yang memberi DJ tertinggi paling rendah dalam batas siklus maksimum yang ditetapkan pengguna | simpang jenuh, mengejar kapasitas | T2 |
| Siklus praktis minimum | siklus terpendek yang membuat semua pendekat kritis berada di bawah DJ target (default 0,85); bila tidak mungkin, beralih ke mode DJ tertinggi | mengurangi waktu tunggu dan membantu pejalan kaki | T2 (usulan tambahan) |
| Pertahankan siklus eksisting | siklus tetap seperti eksisting; hanya pembagian hijau yang diatur ulang untuk tundaan terendah | perubahan paling kecil bagi petugas; memudahkan koordinasi di T4 | T2 (usulan tambahan) |
| Multi-kriteria berbobot | gabungan tundaan, panjang antrian terhadap ruang tersedia, kendaraan terhenti, waktu tunggu pejalan kaki, dan prioritas angkutan umum dengan bobot yang diatur pengguna | kebijakan khusus | T3 |

Dua mode tambahan dipilih karena effort-nya lebih kecil dari mode pencarian: keduanya memakai rumus tertutup dan satu kali pembagian hijau.

### 4.6 Batasan keselamatan dan kebijakan

| Batasan | Nilai default | Dapat diubah |
|---|---|---|
| Waktu kuning | 3 detik | tidak di T2 |
| Merah semua | dihitung dari jarak konflik dan kecepatan (PKJI), dibulatkan ke atas per detik | nilai minimum dapat dinaikkan |
| Hijau minimum | 10 detik; lebih panjang bila ada penyeberangan pejalan kaki dalam fase itu | ya, tidak boleh di bawah waktu penyeberangan |
| Rentang siklus | 40–130 detik (PKJI; di atas 130 detik dihindari) | ya, dalam batas aman |
| DJ target | 0,85 | ya |
| Skema fase | sama dengan eksisting di T2; skema fase alternatif dievaluasi di T3 | tidak di T2 |
| Pembulatan | semua waktu dalam detik bulat | tidak |

Validator menolak rekomendasi yang melanggar batas keselamatan dan menjelaskan alasannya dalam bahasa sederhana.

### 4.7 Keluaran per periode

- Siklus, hijau per fase, kuning, merah semua, waktu hijau hilang.
- Kapasitas, DJ, antrian, panjang antrian, kendaraan terhenti, dan tundaan per pendekat dan per arah; tundaan dan LOS simpang.
- Perbandingan eksisting dengan rekomendasi untuk setiap mode.
- Nilai antara yang menjelaskan keputusan (rasio arus kritis, faktor koreksi yang dipakai, sumber setiap angka).
- Peringatan: DJ di atas target yang tidak dapat diturunkan dengan pengaturan waktu saja, antrian melebihi ruang tersedia, hijau pejalan kaki kurang, data berkualitas rendah.

### 4.8 Validasi di simulator SUMO

Jaringan simulasi dibangun otomatis dari konfigurasi simpang (atau peta OpenStreetMap), rute dibentuk dari hitungan per arah, lalu jadwal eksisting dan rekomendasi dijalankan dengan beberapa bilangan acak. Hasilnya berupa tundaan rata-rata, panjang antrian, dan kendaraan yang lolos, ditampilkan berdampingan dengan hasil PKJI. Perbedaan antara PKJI dan simulasi dijelaskan di laporan; keputusan resmi tetap memakai PKJI. Uji lapangan sebelum-sesudah dilakukan di T3.

### 4.9 Perkiraan manfaat rupiah (versi sederhana T2)

| Komponen | Cara hitung sederhana | Parameter default (dapat diubah) |
|---|---|---|
| Nilai waktu | selisih tundaan per kendaraan × jumlah kendaraan per kelas × nilai waktu per kelas; nilai waktu orang = UMK / jam kerja per bulan, dikali rata-rata okupansi kendaraan | UMK kota terbaru, 166,67 jam kerja per bulan, okupansi motor dan mobil hasil survei atau nilai acuan |
| Bahan bakar | selisih waktu diam × konsumsi BBM saat diam per kelas × harga BBM | konsumsi saat diam per kelas dari literatur, harga BBM terbaru |
| Emisi | BBM yang dihemat × faktor emisi CO2 per liter, ditambah nilai kerugian polutan memakai faktor emisi per jenis kendaraan dan nilai unit pencemaran | faktor emisi dan nilai unit pencemaran menurut peraturan lingkungan hidup yang berlaku |
| Tahunan | nilai harian per periode × jumlah hari kerja dan akhir pekan per tahun | 250 hari kerja, sisanya akhir pekan dan libur |

Hasil ditampilkan sebagai perkiraan dengan rentang dan asumsi yang terlihat. Versi lengkap dengan biaya operasional kendaraan berbasis kecepatan dan analisis sensitivitas dikembangkan di T3.

### 4.10 Laporan kajian otomatis

Satu klik menghasilkan dokumen Word dan PDF dalam bahasa Indonesia berisi: ringkasan untuk pimpinan; lokasi dan diagram simpang; data rekaman dan kualitasnya; hitungan per kelas, per arah, dan per periode; hambatan samping; formulir PKJI SA-I sampai SA-V; rekomendasi per periode untuk mode yang dipilih; perbandingan eksisting dan rekomendasi; hasil validasi SUMO; perkiraan manfaat rupiah; asumsi dan batasan; lampiran tabel. Templat laporan dapat disesuaikan dengan kop dan format pemda.

### 4.11 Peta jalan modul optimasi

| Tahap | Kemampuan |
|---|---|
| T1 | konversi arus; kalkulator PKJI 2023; mode Webster/PKJI baku; validator keselamatan; satu simpang, periode manual |
| T2 | semua mode kecuali multi-kriteria; mode MKJI pembanding; periode otomatis dan manual; manfaat rupiah sederhana; laporan otomatis; validasi SUMO |
| T3 | mode multi-kriteria berbobot; skema fase alternatif; uji lapangan sebelum-sesudah; ekspor lembar jadwal untuk controller; manfaat lengkap dengan biaya operasional kendaraan; banyak simpang yang dihitung mandiri |
| T4 | penerapan jadwal ke controller; penyesuaian adaptif per simpang dari detektor virtual; offset dasar antar simpang berdekatan |
| T5 | optimasi koridor dan jaringan (bandwidth, penalaan offset, max-pressure jaringan, pengendalian perimeter) |

## 5. Konfigurasi simpang dan data statis

Konfigurasi dilakukan lewat wizard berurutan. Setiap langkah memberi nilai default PKJI yang ditandai, penjelasan singkat, dan pesan validasi yang mudah dipahami.

| Langkah wizard | Isi | Kemudahan |
|---|---|---|
| Identitas dan lokasi | nama simpang, koordinat di peta, kota (ukuran kota terisi otomatis dari data penduduk), status jalan (nasional, provinsi, kota) | pencarian di peta; status jalan jalan nasional memunculkan catatan persetujuan Dirjen/BPTJ |
| Lengan dan pendekat | jumlah lengan, kode pendekat, nama jalan, lebar pendekat, lebar masuk, lebar keluar, lajur belok kiri langsung, jumlah dan lebar lajur, panjang lajur khusus belok, median dan jenisnya, kelandaian, tipe lingkungan, kelas hambatan samping pengamatan (T1), jarak parkir, jarak garis henti ke titik konflik | lebar dan jarak titik konflik diukur dengan menggambar di citra satelit; templat simpang tiga lengan dan empat lengan |
| Gerakan dan lajur | gerakan yang diizinkan, lajur khusus, belok kiri langsung | diagram gerakan interaktif |
| Fase dan waktu eksisting | urutan fase, gerakan per fase, hijau, kuning, merah semua | nilai terisi otomatis dari pembacaan nyala lampu bila tersedia |
| Kamera dan rekaman | tautan rekaman atau stream ke pendekat; garis hitung, zona keluar per arah, zona hambatan samping dan panjangnya, area kepala lampu | menggambar langsung di cuplikan kamera; pratinjau hitungan beberapa detik |
| Periode dan jadwal | otomatis atau manual; hari kerja, akhir pekan, libur | pilihan cepat periode baku |
| Parameter kebijakan dan ekonomi | hijau minimum, siklus maksimum, DJ target, UMK, harga BBM, okupansi kendaraan | nilai acuan terisi dan dapat diubah |
| Tinjau dan simpan | ringkasan, pemeriksaan konsistensi, versi konfigurasi | ekspor dan impor berkas konfigurasi |

## 6. Dashboard T2 (tiga halaman)

Setiap halaman memiliki filter yang sama: simpang, tanggal atau set rekaman, jenis hari, periode, dan mode optimasi.

| Halaman | Isi | Pembaca utama |
|---|---|---|
| Ringkasan Simpang dan Rekomendasi | peta dan diagram simpang; LOS dan tundaan simpang keseluruhan; LOS per pendekat; siklus dan hijau rekomendasi per periode dalam bentuk lembar jadwal; perbandingan eksisting dan rekomendasi (tundaan, antrian, DJ, LOS); perkiraan manfaat rupiah per hari dan per tahun; tombol unduh laporan | Kepala Dinas, pimpinan |
| Arus Lalu Lintas dan Kapasitas | profil hitungan 15 menit sepanjang rekaman; komposisi kelas kendaraan; volume per pendekat dan per arah dalam diagram gerakan; kapasitas per pendekat dan per arah; jam puncak dan faktor jam puncak; kelas hambatan samping per pendekat; jadwal hasil pengelompokan periode | engineer |
| Kinerja Pendekat dan Kualitas Data | DJ, antrian, panjang antrian, kendaraan terhenti, dan tundaan per pendekat; peringatan pendekat jenuh atau antrian melebihi ruang; antrian terukur kamera dibanding hitungan PKJI; akurasi hitungan terhadap sampel manual; cakupan rekaman, jam hilang, kondisi malam dan hujan | engineer, tim IRAMA |

## 7. Kriteria kelulusan

| Tahap | Kriteria |
|---|---|
| T1 | satu simpang dari rekaman: tabel hitungan enam kelas per pendekat per 15 menit; akurasi sekitar 90% siang pada klip uji; kalkulator PKJI lolos uji terhadap contoh resmi PKJI 2023 (Lampiran 12.5) dan Dirjen 273/1996 dengan cara di bagian 4.4; rekomendasi mode Webster/PKJI dengan validator; dashboard dasar; demo ujung ke ujung berjalan di laptop |
| T2 | satu simpang lengkap semua lengan; akurasi 90% siang dan 85% malam/hujan; arah gerakan, hambatan samping empat jenis, pembacaan nyala lampu, antrian dasar; mode stream teruji dengan rekaman yang diputar ulang; lima mode optimasi; periode otomatis dan manual; wizard konfigurasi; tiga halaman dashboard; laporan Word/PDF; validasi SUMO; manfaat rupiah; seluruhnya berjalan di laptop tanpa pengadaan |

## 8. Keterkaitan dengan dokumen lain

- Tahapan dan batas lingkup: `04_Konsep_Tahapan_1-5.md`.
- Nomor fitur E20 sampai E23: `05_Inventaris_Fitur_per_Tahap.md`.
- Pilihan teknologi dan lisensi: `06_Arsitektur_Konseptual_dan_Opsi_Teknologi.md`.
- Data yang perlu disiapkan: `13_Kebutuhan_Data_per_Tahap.md`.
- Diagram arsitektur alur data (A01): `14_Arsitektur_per_Tahap.md` bagian 1.
- Langkah menyiapkan data latih: `16_Panduan_Data_Latih_Vision_Tracker.md`.
