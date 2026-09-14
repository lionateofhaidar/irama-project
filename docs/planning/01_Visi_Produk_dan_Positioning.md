# 01 — Visi Produk & Positioning
Status: draf pra-perencanaan (2026-09-12), direvisi 2026-09-14 untuk tahapan baru (`04`) dan ditambah bagian 8 Definisi Istilah. Dasar: seluruh bahan di `docs/sources/` (ringkasan di `docs/kb/` dan `docs/sources/_ringkasan/R00` bagian K). Angka bertanda [asumsi] belum diverifikasi.

## 1. Masalah yang nyata di lapangan (bukan yang dibayangkan)
| Masalah | Bukti | Sumber |
|---|---|---|
| Pengaturan simpang statis: kaki simpang padat dapat hijau pendek, kaki sepi dapat hijau panjang | Pernyataan Kadishub DKI; 256 dari 321 simpang Jakarta masih ATCS statis | [R06 D.2], majalah h.4 |
| Kota-kota besar lebih macet dari Jakarta tetapi ATCS-nya masih tahap CCTV + koordinasi dasar | TomTom 2024: Bandung #12 dunia, Medan #15, Surabaya, Palembang di atas Jakarta (#90); Palembang 15 simpang terkoneksi; Bekasi ruang ATCS baru 2023 | riset [T-09], [KB-09] |
| Sistem adaptif sering "mati" karena detektor rusak, komunikasi putus, SDM & pemeliharaan, bukan karena algoritma | Umur ASCT rata-rata 6–7 tahun; alasan decommissioning = deteksi, komunikasi, maintenance; ATCS Makassar/Garut/multi-kota: peralatan rusak, dana, SDM | [R02 F.5], [R06 E.4] |
| Klaim manfaat tanpa ukuran kinerja yang terdefinisi → sulit dipertanggungjawabkan ke DPRD/publik | Klaim "+20–30%" tanpa MOE; DPRD DKI menanyakan dampak Rp7,15 T | [R06 D.1, D.6] |
| Waktu sinyal jarang ditinjau ulang padahal aturan mewajibkan (≥ tiap 3 bulan) dan retiming saja bernilai B/C 40:1; kajian ulang umumnya memerlukan survei hitung manual per kelas kendaraan [asumsi] | Kep. Dirjen 273/1996; NCDOT; 69% deployment ASCT AS tidak di-retime tahunan | [R00 G], [R01 H.2], [R02 F.2] |
| Prioritas bus/darurat belum sistematis; detik prioritas "menyusut" tanpa perjanjian & log | TSP Handbook; PM 76/2021 Ps.7 & 11 mewajibkan prioritas bus/darurat | [R06 A.4, A.7], [R00 C] |
| Controller lapangan beragam & proprietary (RS-232), vendor lock-in | Diagram majalah (RS232 ke controller); TSPH: proprietary mengunci vendor; e-katalog LKPP penuh controller merek lokal | [R00 A], [R02 G.7], [T-09] |
| Data terpencar; single data transportasi belum ada; kewajiban data terbuka (UU 22/2009 Ps.250) belum terpenuhi | MTI Jakarta; Perda/Pergub soal integrasi data | [R06 D.6], [R05 A.6–A.7] |

## 2. Pernyataan visi
**Platform pengendalian lalu lintas kota yang terbuka, bertahap, dan dapat dipertanggungjawabkan: mulai dari mengubah CCTV yang sudah ada menjadi hitungan lalu lintas dan rekomendasi waktu sinyal yang sah menurut PKJI 2023, lalu bertahap menjadi kendali adaptif terkoordinasi setara ITCS, tanpa mengganti seluruh perangkat lapangan dan tanpa bergantung pada satu vendor.**

Nilai inti (urut prioritas):
1. **Berjalan di atas yang sudah ada.** CCTV eksisting menjadi sumber data lewat Vision Tracker sejak T1. Controller eksisting dibaca mulai T3 dan dikendalikan lewat adaptor mulai T4 (NTCIP untuk yang standar, RS-232 vendor untuk yang lama), sehingga pemda tidak harus membeli ulang.
2. **Fail-safe dan sesuai aturan.** Cadangan ke rencana waktu lokal (≥8 plan, PM 49/2014), perintah petugas didahulukan (UU 22/2009 Ps.104), preemption hak utama, kewenangan Polri dihormati, LOS PM 96/2015, dan PDP.
3. **Terukur, bukan diklaim.** KPI PKJI 2023 dan akurasi Vision Tracker tampil di dashboard; perbandingan eksisting dan rekomendasi, uji lapangan sebelum-sesudah (T3), ATSPM, dan laporan wajib (Forum LLAJ, Dirjen, Gubernur) dibuat otomatis.
4. **Hemat sumber daya.** T1 sampai T3 berjalan di laptop tim tanpa pengadaan; video mentah dihapus setelah diolah dan yang disimpan hanya angka dan peristiwa; edge dan server baru diadakan di T4 (`11`).
5. **Bertahap dan bisa dibeli per tahap.** Tiap tahap punya nilai sendiri dan definisi selesai yang terukur; T2 dijual lebih dulu sebagai jasa kajian.
6. **Anti black-box.** Setiap keputusan sistem menampilkan nilai antara dan alasannya (Req 18.0-2 HOP-11-027); AI/RL hanya sebagai penasihat lewat shadow mode sampai terbukti.
7. **Manusia di dalam loop.** Operator, engineer, teknisi, dan petugas lapangan adalah pengguna utama, bukan objek otomatisasi; sampai T3 rekomendasi diterapkan oleh petugas.
8. **Lisensi bebas dan lock-in minimal.** Komponen berlisensi permisif, model deteksi dalam format ONNX yang dilatih dengan dataset milik tim dan pemda, kamera lewat RTSP/ONVIF, controller lewat NTCIP, dan data dapat diekspor penuh (`06` bagian 4).

## 3. Positioning
- **Untuk** Dinas Perhubungan kota/kabupaten/provinsi (dan UPT pengendali lalu lintas) yang sudah punya APILL/ATCS dasar dan CCTV tetapi belum punya kendali adaptif terukur,
- **produk ini adalah** sistem manajemen & kendali lalu lintas kota (ATMS/ITCS) berbasis standar terbuka,
- **yang** menghasilkan kajian waktu sinyal dari rekaman CCTV yang sudah ada (T1 dan T2), menambah deteksi kejadian dan pemantauan tanpa pengadaan (T3), lalu bertumbuh menjadi kendali adaptif terkoordinasi dengan prioritas bus dan darurat (T4) serta platform banyak kota (T5),
- **berbeda dari** ATCS vendor perangkat (terkunci pada controller mereka, KPI minim) dan dari sistem "AI" turnkey (mahal, black-box, bergantung deteksi kamera sempurna),
- **karena** dibangun di atas PKJI 2023, PM 96/2015, dan NTCIP, dengan Vision Tracker berlisensi bebas, mesin KPI, dan fallback sebagai fitur utama, serta dijual bertahap mulai dari jasa kajian.

## 4. Apa yang sengaja berbeda dari ITCS DKI (bukan tiruan)
| ITCS DKI (end-state) | Produk ini |
|---|---|
| Kamera AI vendor per kaki simpang sebagai satu-satunya deteksi | Deteksi berlapis: hitung dari CCTV eksisting, radar/loop bila ada, probe GPS, laporan manual; degradasi anggun bila satu sumber hilang |
| Nilai jual = "AI, digital twin 3D" | Nilai jual = sinyal yang benar, terukur, dan patuh aturan; AI menyusul sebagai penasihat |
| Satu vendor menyediakan lapangan + pusat | Pusat terbuka; lapangan dari vendor mana pun yang memenuhi spesifikasi (NTCIP wajib di pengadaan baru) |
| Fokus Jakarta (321 simpang, Rp120 M) | Multi-kota; mulai dari satu simpang, lalu banyak simpang yang dihitung mandiri, koordinasi dasar di T4, dan optimasi koridor di T5; skala ke ratusan simpang |
| Perangkat, analitik, dan lisensi dari vendor | Nol pengadaan sampai T3; komponen berlisensi permisif; model deteksi milik tim dan pemda dalam format ONNX |
| Klaim kinerja tanpa MOE publik | Dashboard publik dengan metode yang dipublikasikan (UU Ps.250) |

## 5. Ringkasan tahapan (revisi 2026-09-14; rincian dan kriteria kelulusan di `04_Konsep_Tahapan_1-5.md`)
| Tahap | Nama kerja | Inti nilai |
|---|---|---|
| T1 | Purwarupa Hitung dan Rekomendasi | Alur ujung ke ujung untuk satu simpang dari rekaman: Vision Tracker enam kelas, kalkulator PKJI 2023, rekomendasi Webster/PKJI dengan validator keselamatan, dashboard dasar; nol pengadaan |
| T2 | Vision Tracker dan Optimasi Simpang | Satu simpang lengkap: hitungan per kelas dan per arah, hambatan samping, nyala lampu, antrian; lima mode optimasi dan pembanding MKJI 1997; wizard konfigurasi, tiga halaman dashboard, laporan Word/PDF, validasi SUMO, manfaat rupiah; dijual sebagai jasa kajian dan perangkat lunak pendukung keputusan; nol pengadaan |
| T3 | Deteksi Kejadian dan Pemantauan Operasional | Kendaraan prioritas, kejadian, pelanggaran sebagai bukti, kesehatan kamera dasar; pemantauan, tiket, laporan wajib; controller baca-saja dan ekspor jadwal; uji lapangan sebelum-sesudah; mode multi-kriteria; akurasi 95% siang dan 90% malam atau hujan; nol pengadaan |
| T4 | Kendali Adaptif Terpadu | Pengadaan dimulai; kendali terpusat dan adaptif per simpang, offset dasar dan green wave sederhana, prioritas bus dan darurat, ANPR dan integrasi ETLE/Bapenda/DLH, ruang kendali skala kota; setara fungsi ITCS DKI |
| T5 | Platform Mobilitas Kota | Optimasi koridor dan jaringan penuh, banyak kota, digital twin kota, pasar algoritma lewat mode bayangan, TDM berbasis data, data terbuka |

## 6. Prinsip "kreatif tapi berpijak"
Setiap ide baru harus lolos tiga uji: (1) ada bukti kebutuhan lapangan (keluhan, kendala terdokumentasi, kewajiban regulasi); (2) bisa diukur dampaknya dengan KPI yang sudah didefinisikan; (3) punya fallback bila gagal. Ide yang lolos masuk backlog `05_Inventaris_Fitur_per_Tahap.md`; yang belum lolos dicatat di `docs/kb/10_Keputusan_dan_Pertanyaan_Terbuka.md`.

## 7. Ukuran sukses produk (level program)
- Pemda pilot menaikkan LOS atau menurunkan tundaan secara terukur (PM 96) dengan desain on/off. Target awal: tundaan turun ≥10% pada simpang pilot saat uji lapangan T3 [asumsi dari EDC-1 "≥10%"].
- Akurasi hitungan Vision Tracker sekitar 90% siang dan 85% malam atau hujan di T2, naik menjadi 95% dan 90% mulai T3 (dibanding hitungan manual per kelas per 15 menit).
- Kajian satu simpang (hitungan, rekomendasi, laporan) dapat diselesaikan dari rekaman tanpa survei hitung manual penuh; hitungan manual hanya untuk sampel uji akurasi [asumsi].
- ≥95% ketersediaan komunikasi & ≥90% detektor sehat di simpang yang dikelola, berlaku mulai T4 [asumsi; KPI kesehatan TSPH].
- Setiap perubahan waktu sinyal ter-log, ter-review ≤3 bulan (Kep. Dirjen 273/1996).
- Laporan wajib (Forum LLAJ/Dirjen/Gubernur) dihasilkan otomatis.
- Jasa kajian T2 dipakai minimal satu Dishub dan dapat dijual ke minimal satu kota di luar pilot [asumsi].

## 8. Definisi Istilah

Daftar ini menjelaskan istilah yang sering muncul di dokumen perencanaan IRAMA dengan bahasa sehari-hari. Istilah dikelompokkan menurut bidangnya dan diurutkan menurut abjad di dalam setiap kelompok. Bila sebuah penjelasan memakai istilah lain yang juga teknis, istilah tersebut dapat dicari di kelompok lain pada daftar yang sama.

### Istilah lalu lintas dan simpang

| Istilah | Penjelasan |
|---|---|
| APILL | Singkatan dari Alat Pemberi Isyarat Lalu Lintas, istilah resmi untuk lampu lalu lintas (merah, kuning, hijau). Di IRAMA dipakai sebagai nama resmi aset yang dikelola dan diatur waktunya. |
| Arus lalu lintas | Banyaknya kendaraan yang melewati satu titik dalam satu satuan waktu, biasanya per jam. Di IRAMA dihitung oleh Vision Tracker dari rekaman kamera. |
| ATCS | Singkatan dari Area Traffic Control System, sistem yang menghubungkan beberapa lampu lalu lintas ke satu ruang kendali agar bisa dipantau dan diatur dari pusat. Hampir semua kota besar di Indonesia sudah memiliki ATCS, walaupun sebagian besar baru dipakai untuk memantau kamera. |
| ATMS | Singkatan dari Advanced Traffic Management System, istilah umum untuk sistem pengelolaan lalu lintas terpadu yang mencakup lampu, kamera, papan informasi, dan penanganan kejadian. Menurut PM 76/2021, ATCS adalah salah satu bagian dari ATMS. |
| Belok kiri langsung (LTOR) | Gerakan belok kiri yang boleh jalan terus walaupun lampu sedang merah. LTOR adalah singkatan dari Left Turn On Red. Di IRAMA kendaraan LTOR dihitung terpisah karena tidak ikut antre di lampu merah. |
| BRT | Singkatan dari Bus Rapid Transit, layanan bus cepat dengan jalur khusus dan halte tertutup, misalnya TransJakarta atau Trans Metro Bandung. Bus seperti ini menjadi sasaran utama prioritas bus di T4. |
| Controller | Kotak elektronik di pinggir simpang yang menyalakan dan mematikan lampu sesuai jadwal. Ibarat "otak lokal" lampu lalu lintas yang tetap bekerja walaupun hubungan ke ruang kendali terputus. |
| Detektor | Alat pendeteksi kendaraan, misalnya kabel di bawah aspal, radar, atau kamera. Di IRAMA fungsi detektor dijalankan oleh kamera yang diolah Vision Tracker sehingga tidak perlu memasang alat baru. |
| Fase | Satu bagian dari putaran lampu ketika sekelompok arah diberi hijau bersamaan. Simpang empat lengan umumnya memiliki dua sampai empat fase. |
| Gerakan lurus, belok kiri, belok kanan | Tiga arah pergerakan kendaraan di simpang. Rincian volume per gerakan dibutuhkan untuk menghitung kinerja simpang menurut PKJI 2023 dan ditampilkan di dashboard IRAMA. |
| Green wave | Pengaturan beberapa lampu berurutan di satu jalan agar kendaraan yang melaju dengan kecepatan wajar terus mendapat hijau. Di IRAMA green wave sederhana direncanakan pada T4 dan optimasi koridor penuh pada T5. |
| Green wave VIP | Green wave terjadwal untuk rute rombongan pejabat atau tamu negara, disiapkan sebelum rombongan lewat lalu dikembalikan ke jadwal normal. Kemampuan ini diklaim ITCS DKI dan direncanakan di IRAMA pada T4. |
| ITCS | Singkatan dari Integrated/Intelligent Traffic Control System, nama sistem kendali lalu lintas terpadu milik Pemprov DKI Jakarta. Dalam dokumen IRAMA, ITCS DKI menjadi acuan kemampuan untuk T4. |
| Jam puncak | Jam dengan arus lalu lintas tertinggi dalam sehari, umumnya pagi dan sore hari kerja. Perhitungan waktu lampu biasanya dibuat terpisah untuk jam puncak dan di luar jam puncak. |
| Kabinet | Lemari logam di pinggir simpang tempat controller dan perangkat pendukungnya disimpan. |
| Kendaraan tak bermotor (KTB) | Kendaraan tanpa mesin seperti sepeda, becak, dan gerobak. Dalam PKJI 2023 KTB tidak dihitung sebagai arus kendaraan, tetapi dianggap sebagai hambatan samping. |
| Koordinasi simpang | Pengaturan waktu beberapa simpang yang berdekatan secara bersama agar saling mendukung. Green wave adalah salah satu bentuk koordinasi. |
| Koridor | Satu ruas jalan panjang yang memuat beberapa simpang berlampu berurutan. PM 96/2015 menyebut koridor ATCS berisi minimal tiga simpang yang jaraknya tidak lebih dari satu kilometer. |
| LHR | Singkatan dari lalu lintas harian rata-rata, yaitu jumlah kendaraan yang lewat dalam sehari dirata-ratakan selama periode tertentu. Data ini biasanya dimiliki Dishub dari survei berkala. |
| LV, HV, MC | Kelas kendaraan menurut MKJI 1997. LV (light vehicle) adalah kendaraan ringan seperti mobil, HV (heavy vehicle) adalah kendaraan berat seperti bus dan truk, MC (motorcycle) adalah sepeda motor. Di IRAMA kelas ini dipakai untuk mode pembanding MKJI 1997. |
| Merah semua | Jeda singkat ketika semua arah mendapat lampu merah bersamaan. Gunanya memberi waktu kendaraan terakhir keluar dari simpang sebelum arah berikutnya mulai jalan. |
| OD (asal-tujuan) | Data tentang dari mana dan ke mana orang atau kendaraan bepergian. Data OD dibutuhkan untuk simulasi skala kota dan kebijakan pengelolaan permintaan perjalanan di T5. |
| Offset | Selisih waktu mulai hijau antara satu simpang dan simpang berikutnya. Offset yang tepat membuat green wave terbentuk. |
| Pendekat atau lengan simpang | Setiap jalan yang masuk ke simpang. Simpang empat memiliki empat pendekat, masing-masing dengan lebar, antrian, dan lampunya sendiri. |
| Simpang bersinyal | Persimpangan jalan yang diatur dengan lampu lalu lintas. Simpang bersinyal adalah objek utama yang dihitung dan dioptimasi oleh IRAMA. |
| SM, MP, KS | Kelas kendaraan menurut PKJI 2023. SM adalah sepeda motor, MP adalah mobil penumpang (termasuk angkot dan pikap), KS adalah kendaraan sedang dan besar seperti bus dan truk. Di IRAMA kelas rinci hasil Vision Tracker dipetakan otomatis ke kelas ini. |
| TMC atau ruang kendali | Ruangan tempat petugas memantau dan mengatur lalu lintas kota lewat layar, kamera, dan sistem kendali. TMC adalah singkatan dari Traffic Management Centre. |
| V/C | Perbandingan volume lalu lintas dengan kapasitas jalan, sama maknanya dengan derajat kejenuhan. PP 32/2011 memakai ambang V/C dan kecepatan sebagai syarat kebijakan pembatasan kendaraan seperti ganjil-genap. |
| Volume | Jumlah kendaraan yang lewat dalam periode tertentu, misalnya per 15 menit atau per jam. Istilah ini sering dipakai bergantian dengan arus lalu lintas. |
| Waktu antar hijau | Jumlah waktu kuning ditambah merah semua di antara berakhirnya hijau satu arah dan dimulainya hijau arah berikutnya. Waktu ini dianggap waktu hilang karena tidak ada arah yang bergerak penuh. |
| Waktu hijau | Lama lampu hijau menyala untuk satu fase. Pembagian waktu hijau antar fase adalah salah satu keluaran utama modul optimasi IRAMA. |
| Waktu kuning | Lama lampu kuning menyala setelah hijau, di Indonesia umumnya tiga detik. Gunanya memberi peringatan agar pengemudi bersiap berhenti. |
| Waktu siklus | Waktu satu putaran penuh lampu sampai kembali ke fase awal, misalnya 90 detik. Siklus yang terlalu pendek membuat antrian tidak habis, sedangkan siklus yang terlalu panjang membuat orang menunggu lama. |

### Istilah kinerja dan perhitungan

| Istilah | Penjelasan |
|---|---|
| Antrian | Barisan kendaraan yang menunggu di lampu merah, dihitung dalam jumlah kendaraan atau panjang meter. Di IRAMA antrian dihitung dengan rumus PKJI dan, mulai T2, juga diukur dari kamera. |
| Arrivals on green (AoG) | Persentase kendaraan yang tiba di simpang ketika lampu sedang hijau. Semakin tinggi angkanya, semakin baik koordinasi antar simpang. |
| Arus jenuh | Jumlah kendaraan maksimal yang bisa lewat per jam hijau bila antrian terus tersedia. Nilainya bergantung pada lebar jalan, ukuran kota, hambatan samping, dan kondisi lain. |
| ATSPM | Singkatan dari Automated Traffic Signal Performance Measures, kumpulan ukuran kinerja lampu lalu lintas yang dihitung otomatis dari catatan kejadian lampu dan detektor. Di IRAMA dipakai sebagai alat ukur independen untuk menilai apakah pengaturan lampu berjalan baik. |
| Before-after (uji sebelum-sesudah) | Cara menilai dampak dengan membandingkan kondisi sebelum dan sesudah perubahan, misalnya sebelum dan sesudah waktu lampu diubah. PM 96/2015 mewajibkan evaluasi semacam ini, dan di IRAMA uji lapangan sebelum-sesudah dilakukan mulai T3. |
| BOK (biaya operasional kendaraan) | Biaya yang dikeluarkan untuk menjalankan kendaraan, seperti bahan bakar, oli, ban, dan penyusutan. Di T2 IRAMA menghitung bagian yang paling terpengaruh pengaturan lampu, yaitu bahan bakar yang terbuang saat kendaraan diam atau berhenti. |
| Derajat kejenuhan (DS/DJ) | Perbandingan antara arus kendaraan dan kapasitas, misalnya 0,85 berarti jalan terisi 85% dari kemampuannya. PKJI 2023 menyarankan nilai desain tidak melebihi 0,85; di IRAMA DS ditampilkan sebagai indikator pendukung LOS. |
| EMP | Singkatan dari ekuivalensi mobil penumpang, angka pengali untuk menyetarakan setiap jenis kendaraan dengan satu mobil. Menurut PKJI 2023 untuk simpang bersinyal, MP bernilai 1,00, KS bernilai 1,30, dan SM bernilai 0,15 bila arahnya terlindung atau 0,40 bila berhadapan dengan arus lawan. |
| Faktor emisi | Perkiraan banyaknya gas buang per kilometer untuk tiap jenis kendaraan. Di IRAMA dipakai untuk memperkirakan pengurangan emisi dan nilai rupiahnya bila kendaraan lebih lancar. |
| Faktor jam puncak (PHF) | Angka yang menunjukkan seberapa merata arus dalam satu jam puncak, dihitung dari perbandingan arus satu jam dengan empat kali arus 15 menit tertinggi. Nilai yang rendah berarti ada lonjakan singkat yang perlu diperhitungkan. |
| FHS | Singkatan dari faktor koreksi hambatan samping, angka pengurang arus jenuh akibat aktivitas di sisi jalan. Nilainya diambil dari tabel PKJI 2023 berdasarkan tipe lingkungan, kelas hambatan samping, dan proporsi kendaraan tak bermotor. |
| Hambatan samping | Kegiatan di sisi jalan yang memperlambat kendaraan, misalnya pejalan kaki, angkot berhenti, kendaraan keluar masuk toko, dan sepeda. PKJI 2023 memberi bobot pejalan kaki 0,5, kendaraan berhenti 1,0, kendaraan keluar-masuk 0,7, dan kendaraan lambat 0,4. |
| HCM | Singkatan dari Highway Capacity Manual, pedoman kapasitas jalan dari Amerika Serikat. IRAMA memakai PKJI 2023 untuk Indonesia, sehingga HCM hanya menjadi rujukan pembanding bila pembeli memintanya. |
| Kapasitas | Jumlah kendaraan maksimal yang dapat dilayani satu pendekat atau simpang per jam dengan pengaturan lampu tertentu. Kapasitas simpang bersinyal dihitung dari arus jenuh dikalikan porsi waktu hijau. |
| Kendaraan terhenti | Perkiraan banyaknya kendaraan yang harus berhenti setidaknya sekali saat melewati simpang. Angka ini ikut dipakai untuk memperkirakan boros bahan bakar. |
| KHS | Singkatan dari kelas hambatan samping, yaitu tingkat hambatan samping dari sangat rendah sampai sangat tinggi. Kelas ditentukan dari jumlah kejadian berbobot per 200 meter per jam; di IRAMA jumlah itu dihitung oleh Vision Tracker. |
| LOS | Singkatan dari Level of Service atau tingkat pelayanan, nilai huruf A sampai F untuk menggambarkan kelancaran. Untuk simpang, PM 96/2015 memakai tundaan rata-rata per kendaraan, yaitu A di bawah 5 detik, B 5–15, C 15–25, D 25–40, E 40–60, dan F di atas 60 detik. |
| Manfaat rupiah | Perkiraan nilai uang dari perbaikan kinerja simpang, dihitung dari waktu yang dihemat, bahan bakar yang tidak terbuang saat kendaraan diam, dan emisi yang berkurang. Ditampilkan di dashboard dan laporan T2 agar keputusan mudah dipertanggungjawabkan. |
| MOE | Singkatan dari Measure of Effectiveness, ukuran efektivitas yang dipakai untuk menilai hasil sebuah pengaturan, misalnya tundaan, antrian, atau waktu tempuh. Klaim manfaat tanpa MOE yang jelas sulit dipertanggungjawabkan. |
| Nilai waktu | Nilai rupiah dari satu jam waktu yang hilang di perjalanan, misalnya dihitung dari upah minimum. Di IRAMA dipakai untuk mengubah pengurangan tundaan menjadi manfaat rupiah. |
| RKTB | Singkatan dari rasio kendaraan tak bermotor, yaitu perbandingan jumlah kendaraan tak bermotor dengan kendaraan bermotor di satu pendekat. Angka ini memengaruhi faktor hambatan samping dalam PKJI 2023. |
| Siklus praktis | Waktu siklus terpendek yang masih membuat derajat kejenuhan berada di bawah batas yang ditetapkan. Pendekatan ini membuat pengendara dan pejalan kaki tidak menunggu terlalu lama dan menjadi salah satu pilihan mode optimasi IRAMA. |
| SMP (satuan mobil penumpang) | Satuan hitung arus setelah semua jenis kendaraan disetarakan dengan mobil memakai EMP. Contohnya, satu motor di arah terlindung dihitung 0,15 SMP. |
| Split failure | Kejadian ketika waktu hijau habis sebelum antrian terlayani, sehingga sebagian kendaraan harus menunggu satu siklus lagi. Makin sering terjadi, makin besar tanda waktu hijau perlu ditambah. |
| Tundaan | Tambahan waktu perjalanan yang dialami kendaraan karena melewati simpang, dihitung dalam detik per kendaraan. Tundaan rata-rata simpang menjadi dasar kelas LOS resmi dan tujuan utama optimasi IRAMA. |
| Uji regresi | Pengujian ulang secara otomatis bahwa hasil hitungan tetap sama dengan contoh yang sudah diketahui jawabannya, setiap kali program diubah. Di IRAMA kalkulator PKJI diuji terhadap contoh resmi Kep. Dirjen 273/1996, dan mode MKJI diuji terhadap studi lama. |
| UMK | Upah minimum kabupaten atau kota yang ditetapkan gubernur setiap tahun. IRAMA memakai UMK sebagai dasar sederhana untuk menghitung nilai waktu perjalanan dalam rupiah. |
| Webster | Rumus klasik untuk menghitung waktu siklus yang menghasilkan tundaan kecil, kemudian dibagi menjadi waktu hijau sesuai beban setiap fase. Rumus ini dipakai di PKJI 2023 dan menjadi salah satu mode optimasi di IRAMA. |

### Istilah regulasi dan kelembagaan

| Istilah | Penjelasan |
|---|---|
| Bapenda | Badan Pendapatan Daerah, instansi pemda yang mengelola pajak daerah termasuk pajak kendaraan bermotor. Integrasi dengan Bapenda direncanakan di T4 dengan perjanjian dan perlindungan data. |
| BPTJ | Singkatan dari Badan Pengelola Transportasi Jabodetabek di bawah Kementerian Perhubungan. BPTJ berwenang atas jalan nasional di wilayah Jakarta dan sekitarnya. |
| Dirjen Hubdat | Direktorat Jenderal Perhubungan Darat di Kementerian Perhubungan. Persetujuan Dirjen Hubdat diperlukan untuk perubahan pengaturan lalu lintas di jalan nasional. |
| Dishub | Dinas Perhubungan, instansi pemerintah daerah yang mengelola lampu lalu lintas, ATCS, dan manajemen lalu lintas kota. Dishub adalah calon pengguna utama IRAMA. |
| Diskominfo | Dinas Komunikasi dan Informatika di pemerintah daerah, pengelola server, jaringan, dan kebijakan data kota. Menurut Perda Kota Bandung 12/2024, sistem informasi transportasi dikelola Dishub bersama Diskominfo. |
| DLH | Dinas Lingkungan Hidup, instansi pemda yang antara lain mengelola uji emisi kendaraan dan pemantauan kualitas udara. Integrasi dengan DLH direncanakan di T4. |
| DPIA | Singkatan dari Data Protection Impact Assessment, yaitu penilaian risiko sebelum mengolah data pribadi dalam jumlah besar, misalnya pelat nomor. Menurut UU PDP, penilaian ini wajib dilakukan sebelum fitur semacam ANPR dijalankan. |
| DPRD | Dewan Perwakilan Rakyat Daerah, lembaga yang menyetujui anggaran pemda dan mengawasi pelaksanaannya. Bukti manfaat yang terukur dibutuhkan agar anggaran lalu lintas dapat dipertanggungjawabkan kepada DPRD. |
| ETLE | Singkatan dari Electronic Traffic Law Enforcement, sistem tilang elektronik milik Polri. IRAMA hanya boleh mengirim bukti pelanggaran; penerbitan tilang tetap kewenangan Polri. |
| FHWA | Singkatan dari Federal Highway Administration, badan jalan raya federal Amerika Serikat yang menerbitkan banyak pedoman dan penelitian pengaturan lampu lalu lintas. Beberapa pedomannya menjadi rujukan IRAMA. |
| Forum LLAJ | Forum koordinasi lalu lintas dan angkutan jalan di daerah yang beranggotakan Dishub, Polri, dinas pekerjaan umum, dan instansi lain. Laporan pelaksanaan manajemen lalu lintas wajib disampaikan ke forum ini. |
| MKJI 1997 | Manual Kapasitas Jalan Indonesia terbitan 1997, pedoman lama untuk menghitung kapasitas dan kinerja jalan serta simpang. Sudah digantikan PKJI 2023, tetapi masih banyak dipakai di studi lama sehingga IRAMA menyediakan mode pembandingnya. |
| MRLL | Singkatan dari manajemen dan rekayasa lalu lintas, kegiatan perencanaan, pengaturan, dan evaluasi lalu lintas yang diatur UU 22/2009 dan PM 96/2015. Laporan MRLL disampaikan ke Forum LLAJ. |
| PDKI dan DJKI | DJKI adalah Direktorat Jenderal Kekayaan Intelektual, dan PDKI adalah pangkalan data kekayaan intelektualnya. Di PDKI nama IRAMA dicek sebelum didaftarkan sebagai merek. |
| Perpol ETLE | Peraturan Kepolisian Nomor 8 Tahun 2023 dan Nomor 2 Tahun 2025 yang mengatur sistem elektronik lalu lintas dan penindakan berbasis rekaman elektronik. Isinya menegaskan bahwa bukti dari kamera di luar sistem ETLE wajib diverifikasi petugas Polri. |
| PKJI 2023 | Pedoman Kapasitas Jalan Indonesia terbitan Kementerian PUPR tahun 2023, standar resmi terbaru untuk menghitung kapasitas, derajat kejenuhan, antrian, dan tundaan. Seluruh rekomendasi resmi IRAMA memakai pedoman ini. |
| PM 49/2014 | Peraturan Menteri Perhubungan tentang APILL. Isinya antara lain mewajibkan setiap lampu memiliki paling sedikit delapan rencana waktu, pemeliharaan berkala, dan batas umur teknis perangkat. |
| PM 76/2021 | Peraturan Menteri Perhubungan tentang sistem manajemen transportasi cerdas. Isinya menjadi dasar hukum ATMS dan mensyaratkan sistem yang terbuka dan sesuai standar. |
| PM 96/2015 | Peraturan Menteri Perhubungan tentang pedoman manajemen dan rekayasa lalu lintas. Isinya memuat klasifikasi LOS simpang berdasarkan tundaan dan kewajiban mensimulasikan kebijakan sebelum ditetapkan. |
| RITJ | Singkatan dari Rencana Induk Transportasi Jabodetabek, rencana induk yang dikoordinasikan BPTJ. Salah satu pilarnya adalah pembangunan dan pengembangan ATCS. |
| RPJMD dan RKPD | RPJMD adalah rencana pembangunan jangka menengah daerah untuk lima tahun, dan RKPD adalah rencana kerja tahunan pemda. Program lalu lintas perlu tercantum di kedua dokumen ini agar bisa dianggarkan. |
| SPBE | Singkatan dari Sistem Pemerintahan Berbasis Elektronik, kebijakan nasional yang mengatur aplikasi, data, dan infrastruktur digital pemerintah. Aplikasi yang dipakai pemda diharapkan selaras dengan SPBE, misalnya dalam hal interoperabilitas dan tempat penyimpanan data. |
| UU 22/2009 | Undang-Undang Lalu Lintas dan Angkutan Jalan, dasar hukum semua pengaturan lalu lintas. Undang-undang ini mengatur pembagian kewenangan antara pemerintah daerah dan Polri. |
| UU PDP | Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi. Isinya relevan karena rekaman kamera dan pelat nomor dapat mengenali orang. |

### Istilah kendali dan prioritas

| Istilah | Penjelasan |
|---|---|
| Actuated | Cara kerja lampu yang memperpanjang atau memperpendek hijau berdasarkan ada tidaknya kendaraan yang terdeteksi. Cara ini lebih responsif daripada jadwal tetap. |
| Adaptif | Cara kerja lampu yang menyesuaikan waktu hijau dan siklus secara otomatis mengikuti kondisi lalu lintas saat itu. Di IRAMA kendali adaptif direncanakan mulai T4. |
| Adaptor controller | Program penerjemah antara sistem pusat dan controller merek tertentu. Dengan adaptor, controller merek berbeda dapat dibaca atau dikendalikan tanpa mengubah aplikasi utama; di IRAMA adaptor baca-saja dimulai di T3 dan adaptor kendali di T4. |
| ANPR | Singkatan dari Automatic Number Plate Recognition, pembacaan pelat nomor kendaraan secara otomatis dari kamera. Di IRAMA fitur ini ditunda ke T4 karena membutuhkan kamera khusus dan pengelolaan data pribadi. |
| ASCT | Singkatan dari Adaptive Signal Control Technology, istilah umum di Amerika Serikat untuk teknologi lampu lalu lintas adaptif. Pengalaman di sana menunjukkan sistem adaptif sering berhenti dipakai karena masalah detektor, komunikasi, dan pemeliharaan, sehingga IRAMA menaruh perhatian besar pada kesehatan perangkat. |
| AVL | Singkatan dari Automatic Vehicle Location, pelacakan posisi kendaraan (misalnya bus) dengan GPS secara terus-menerus. Di IRAMA data AVL dibutuhkan untuk prioritas bus. |
| CAD | Singkatan dari Computer Aided Dispatch, sistem pusat panggilan darurat (misalnya pemadam kebakaran dan ambulans) untuk mengirim dan melacak unit. Di IRAMA data CAD dipakai untuk prioritas kendaraan darurat pada T4. |
| Detak jantung (heartbeat) | Sinyal berkala dari pusat ke controller yang menandakan hubungan masih sehat. Bila detak berhenti, controller otomatis kembali ke jadwal lokalnya sehingga lampu tetap aman. |
| Detektor virtual | Garis atau zona yang digambar pada tampilan kamera dan berfungsi seperti detektor fisik, misalnya menghitung kendaraan yang lewat atau mendeteksi antrian. Di IRAMA detektor virtual dijalankan Vision Tracker dan dipakai untuk kendali adaptif mulai T4. |
| EVP (prioritas kendaraan darurat) | Pengaturan lampu agar ambulans atau pemadam kebakaran mendapat hijau saat mendekat. EVP adalah singkatan dari Emergency Vehicle Preemption. |
| GLOSA | Singkatan dari Green Light Optimal Speed Advisory, saran kecepatan di aplikasi navigasi agar pengemudi tiba saat lampu hijau. Direncanakan di T5. |
| Link Pivot | Metode dari Purdue University untuk mencari offset terbaik antar simpang berurutan agar lebih banyak kendaraan tiba saat hijau. Di IRAMA dipakai sebagai salah satu cara optimasi koridor. |
| Log kejadian resolusi tinggi | Catatan setiap perubahan lampu dan setiap deteksi kendaraan dengan ketelitian sepersepuluh detik, dikenal juga sebagai hi-res log. Log ini menjadi bahan ukuran kinerja sinyal (ATSPM) dari controller mulai T4. |
| Max-pressure | Metode kendali adaptif yang memberi hijau lebih banyak kepada arah dengan antrian paling menekan dibanding ruang kosong di hilirnya. Metode ini memiliki dasar stabilitas secara teori dan telah banyak diuji pada simulasi; di IRAMA direncanakan untuk jaringan di T5. |
| Perimeter control | Pengaturan lampu di pintu masuk sebuah kawasan agar kendaraan yang masuk tidak melebihi daya tampung, sehingga bagian dalam kawasan tidak macet total. Direncanakan pada T5 bersama optimasi jaringan. |
| Preemption | Pengambilalihan urutan lampu secara paksa untuk memberi jalan kepada kendaraan darurat atau kereta api. Setelah kendaraan lewat, lampu kembali ke pengaturan semula. |
| Rencana waktu atau jadwal (TOD) | Kumpulan pengaturan lampu (siklus dan hijau) yang dipakai pada jam tertentu, misalnya jadwal pagi, siang, dan malam. TOD adalah singkatan dari Time of Day; IRAMA dapat mengelompokkan hitungan 15 menit menjadi paling banyak delapan jadwal. |
| SCATS dan SCOOT | Dua sistem lampu adaptif komersial yang terkenal, masing-masing berasal dari Australia dan Inggris. Beberapa kota Indonesia pernah memakai sistem semacam ini dan mengalami ketergantungan pada vendor. |
| SPaT dan MAP | SPaT (Signal Phase and Timing) adalah informasi fase lampu yang sedang menyala beserta sisa waktunya, dan MAP adalah peta geometri simpang dalam format standar. Keduanya disiarkan agar aplikasi navigasi dan kendaraan terhubung dapat membacanya. |
| Transaksi perubahan jadwal | Cara mengirim perubahan jadwal ke controller sebagai satu paket yang diperiksa keabsahannya lebih dulu, lalu diterapkan sekaligus. Bila ada bagian yang salah, seluruh paket ditolak sehingga controller tidak pernah menjalankan jadwal setengah jadi. |
| TRPS | Singkatan dari Traffic Responsive Plan Selection, pemilihan jadwal lampu secara otomatis dari pustaka jadwal berdasarkan hitungan kendaraan saat itu. Cara ini berada di antara jadwal tetap dan kendali adaptif penuh. |
| TSP (prioritas bus) | Pengaturan lampu yang memperpanjang hijau atau mempercepat hijau bagi bus yang terlambat. TSP adalah singkatan dari Transit Signal Priority. |
| Uji di meja (bench test) | Pengujian perangkat lunak dengan controller sungguhan yang diletakkan di meja kerja sebelum alat dipasang di jalan. Di IRAMA uji ini dilakukan di T4 sebelum adaptor kendali dipasang di lapangan. |

### Istilah vision dan kecerdasan buatan

| Istilah | Penjelasan |
|---|---|
| Active learning (belajar aktif) | Cara menyiapkan data latih dengan memprioritaskan gambar yang paling membingungkan model untuk dikoreksi manusia. Dengan cara ini akurasi naik lebih cepat dengan jumlah koreksi yang lebih sedikit. |
| Akurasi hitungan | Seberapa dekat jumlah kendaraan hasil Vision Tracker dengan hitungan manusia pada video yang sama. Target IRAMA sekitar 90% pada siang hari dan 85% pada malam atau hujan di T1 dan T2, lalu dinaikkan bertahap menjadi 95% dan 90% mulai T3. |
| Anotasi atau label | Kegiatan menandai objek pada gambar, misalnya menggambar kotak di sekeliling setiap motor lalu memberi nama kelasnya. Hasil anotasi menjadi bahan belajar bagi model. |
| Bingkai (frame) | Satu gambar diam dari rangkaian video. Video umumnya berisi 25 sampai 30 bingkai per detik, dan Vision Tracker cukup mengambil sekitar 10 bingkai per detik agar ringan. |
| ByteTrack | Metode pelacakan objek yang populer, berlisensi MIT, dan cepat. Di IRAMA dipakai untuk mengikuti setiap kendaraan dari satu gambar ke gambar berikutnya. |
| CUDA, TensorRT, dan OpenVINO | Perangkat lunak percepatan kecerdasan buatan dari NVIDIA (CUDA, TensorRT) dan Intel (OpenVINO). IRAMA dapat memakainya lewat ONNX Runtime ketika perangkat edge atau server berkartu grafis tersedia di T4. |
| CVAT | Aplikasi gratis untuk membuat anotasi gambar dan video, bisa dipasang sendiri di komputer. Salah satu pilihan alat anotasi data latih IRAMA. |
| Dataset | Kumpulan gambar beserta labelnya yang dipakai untuk melatih dan menguji model. |
| Deteksi objek | Kemampuan komputer menemukan benda pada gambar dan menentukan jenisnya, misalnya "ini motor" atau "ini bus". Deteksi objek adalah langkah pertama Vision Tracker. |
| DirectML dan iGPU | iGPU adalah grafis terintegrasi yang menyatu dengan prosesor laptop, dan DirectML adalah cara Windows memakai iGPU untuk mempercepat kecerdasan buatan. ONNX Runtime dapat memakai DirectML sehingga laptop tim bisa lebih cepat tanpa kartu grafis khusus. |
| FFmpeg dan OpenCV | FFmpeg adalah alat gratis untuk membaca, memotong, dan mengubah format video, sedangkan OpenCV adalah pustaka gratis untuk mengolah gambar. Keduanya dipakai Vision Tracker untuk mengambil bingkai dari rekaman atau stream. |
| Fine-tuning | Melatih ulang model yang sudah pintar secara umum dengan contoh lokal agar lebih tepat, misalnya mengenali angkot dan motor berhimpitan di Bandung. Cara ini jauh lebih cepat daripada melatih dari nol. |
| Garis hitung dan zona | Garis atau area yang digambar engineer di atas tampilan kamera. Kendaraan dihitung ketika melewati garis hitung, arahnya ditentukan dari zona keluar, dan hambatan samping dihitung di zona pinggir jalan. |
| Inferensi | Tahap ketika model yang sudah dilatih dipakai untuk mengenali objek pada video baru. Inferensi IRAMA berjalan di laptop tim sampai T3. |
| Kaggle dan Google Colab | Layanan daring yang meminjamkan komputer berkartu grafis secara gratis dengan kuota tertentu. IRAMA memakainya untuk melatih model tanpa membeli perangkat; rekaman milik Dishub tidak diunggah ke layanan ini. |
| Kelas objek | Kategori yang dikenali model, misalnya motor, mobil, bus, truk, kendaraan tak bermotor, dan pejalan kaki. |
| Label Studio | Aplikasi gratis berlisensi Apache-2.0 untuk membuat anotasi berbagai jenis data termasuk gambar. Alternatif selain CVAT. |
| Model | Program hasil pelatihan yang telah "belajar" mengenali pola dari banyak contoh. |
| ONNX dan ONNX Runtime | ONNX adalah format standar penyimpanan model kecerdasan buatan, dan ONNX Runtime adalah mesin gratis untuk menjalankannya di berbagai jenis komputer. Keduanya membuat IRAMA tidak terikat pada satu merek prosesor atau kartu grafis. |
| OWLv2 dan Grounding DINO | Model yang dapat mencari objek berdasarkan kata yang diketik, misalnya becak atau gerobak, tanpa dilatih khusus. Di IRAMA keduanya dipakai untuk membuat pra-label kelas yang jarang ada di dataset umum. |
| Pelacakan (tracking) | Mengikuti objek yang sama dari satu gambar ke gambar berikutnya dan memberinya nomor tetap. Dengan pelacakan, satu kendaraan hanya dihitung sekali saat melewati garis hitung. |
| Pelatihan model (training) | Proses komputer mempelajari contoh berlabel sampai mampu mengenali objek sendiri. Proses ini paling cepat bila memakai kartu grafis. |
| Penyamaran wajah dan pelat | Pengaburan otomatis wajah orang dan pelat nomor pada cuplikan video yang disimpan. Langkah ini diwajibkan mulai T2 untuk melindungi data pribadi. |
| Pra-label | Label awal yang dibuat otomatis oleh model, lalu dikoreksi manusia. Cara ini menghemat waktu anotasi secara besar. |
| Register sumber rekaman | Daftar yang mencatat asal setiap video, tautannya, izin atau lisensinya, dan kegunaannya. Register ini membuktikan asal-usul data latih dan memudahkan penggantian data bila suatu saat diperlukan. |
| RF-DETR | Model deteksi objek dari Roboflow yang akurat; varian yang direncanakan berlisensi Apache-2.0, dan lisensi bobot tiap varian tetap diperiksa sebelum dipakai. Salah satu kandidat model deteksi IRAMA dan dipakai untuk pra-label. |
| Supervision | Pustaka perangkat lunak gratis berlisensi MIT yang menyediakan alat hitung kendaraan melewati garis atau zona pada video. |
| Vision Tracker | Modul IRAMA yang menonton video kamera, mengenali dan mengikuti kendaraan, lalu menghasilkan tabel hitungan per kelas, per arah, dan per 15 menit, termasuk kejadian hambatan samping. Tabel ini menjadi masukan modul optimasi waktu simpang. |
| YOLO dan Ultralytics | YOLO adalah keluarga model deteksi objek yang sangat populer, dan Ultralytics adalah perusahaan pengembang versi terbarunya. Versi Ultralytics berlisensi AGPL sehingga tidak dipakai di IRAMA. |
| YOLOX | Varian YOLO berlisensi Apache-2.0 yang ringan dan bisa berjalan cepat di prosesor biasa. Versi terkecilnya, YOLOX-tiny, menjadi kandidat model operasi di laptop tanpa kartu grafis khusus. |

### Istilah perangkat lunak dan infrastruktur

| Istilah | Penjelasan |
|---|---|
| ADR | Singkatan dari Architecture Decision Record, catatan singkat tentang satu keputusan teknis beserta alasan dan konsekuensinya. Gunanya agar tim di kemudian hari tahu mengapa sebuah pilihan dibuat. |
| API | Pintu komunikasi antar aplikasi, ibarat loket layanan dengan aturan permintaan dan jawaban yang jelas. Di IRAMA API dipakai agar dashboard, sistem Polri, dan sistem pemda bisa bertukar data. |
| Audit log | Catatan permanen tentang siapa melakukan apa dan kapan di dalam sistem. Dibutuhkan agar setiap perubahan waktu lampu bisa dipertanggungjawabkan. |
| CI (continuous integration) | Pemeriksaan otomatis yang berjalan setiap kali kode diubah, misalnya menjalankan uji dan memeriksa lisensi pustaka. Dengan CI, kesalahan dan komponen berlisensi terlarang ketahuan sebelum masuk produk. |
| Cloud | Layanan server milik penyedia besar yang disewa lewat internet. IRAMA tidak menyewa cloud sampai T3 selesai. |
| CPU dan GPU | CPU adalah prosesor utama komputer yang serba bisa, sedangkan GPU adalah kartu grafis yang sangat cepat untuk perhitungan kecerdasan buatan. Laptop tim hanya memiliki CPU dan grafis terintegrasi, sehingga model dipilih yang ringan. |
| CRM | Singkatan dari Customer Relationship Management; dalam dokumen IRAMA artinya aplikasi pengaduan warga milik pemda. Integrasi dua arah dengan CRM kota direncanakan di T3 agar keluhan tentang lampu langsung menjadi tiket. |
| Dashboard | Halaman tampilan yang merangkum angka dan grafik penting agar mudah dibaca sekilas. IRAMA T2 memiliki beberapa halaman dashboard yang dipisah menurut jenis informasinya. |
| Digital twin | Tiruan digital sebuah simpang atau koridor di komputer yang berperilaku mirip dengan kondisi nyata. Gunanya menguji pengaturan lampu baru tanpa risiko di jalan. |
| Docker | Alat untuk membungkus aplikasi beserta semua kebutuhannya dalam satu paket agar bisa dijalankan sama persis di komputer mana pun. Memudahkan pemasangan IRAMA di laptop maupun server pemda. |
| Edge atau edge device | Komputer kecil yang dipasang dekat sumber data, misalnya di kabinet simpang, agar pengolahan dilakukan di tempat. Di IRAMA edge baru dipakai pada T4 bersamaan dengan pengadaan. |
| FastAPI | Kerangka kerja gratis berbahasa Python untuk membuat API. Dipakai sebagai dasar layanan pusat IRAMA. |
| Git, GitHub, dan Git LFS | Git adalah alat pencatat riwayat perubahan berkas, GitHub adalah layanan penyimpanan repositori Git secara daring, dan Git LFS adalah tambahan untuk menyimpan berkas besar seperti PDF dan gambar. |
| HLS | Format siaran video lewat internet yang memecah video menjadi potongan-potongan kecil, umum dipakai di portal CCTV publik. |
| ICD (dokumen antarmuka) | Singkatan dari Interface Control Document, dokumen yang menetapkan format, frekuensi, dan tanggung jawab pertukaran data antara dua sistem. Setiap integrasi dengan instansi lain di IRAMA memiliki ICD sendiri. |
| Jetson | Komputer kecil buatan NVIDIA dengan kartu grafis untuk menjalankan kecerdasan buatan di lapangan. Kandidat perangkat edge untuk T4 ke atas. |
| k3s dan Kubernetes | Kubernetes adalah sistem untuk menjalankan dan mengatur banyak paket aplikasi di beberapa server sekaligus, dan k3s adalah versi ringannya. Di IRAMA dipakai mulai T4 saat skala sudah besar. |
| Keycloak, IdP, dan OIDC | IdP (identity provider) adalah layanan pusat untuk login dan hak akses, OIDC adalah standar terbuka yang dipakainya, dan Keycloak adalah IdP gratis yang direncanakan dipakai IRAMA mulai T3. |
| LibreOffice dan python-docx | python-docx adalah pustaka gratis untuk membuat berkas Word dari program, dan LibreOffice adalah paket perkantoran gratis yang dapat mengubah Word menjadi PDF. Keduanya dipakai untuk laporan kajian otomatis tanpa lisensi Microsoft Office. |
| Lisensi perangkat lunak terbuka | Izin pemakaian perangkat lunak yang kodenya terbuka. Lisensi permisif (Apache, MIT, BSD) membolehkan pemakaian di produk komersial tanpa membuka kode sendiri; lisensi seperti LGPL, MPL, dan EPL hanya mewajibkan perubahan pada komponen itu sendiri dibuka; GPL dan AGPL mewajibkan kode produk yang memakainya ikut dibuka, dan AGPL berlaku juga bila produk hanya diakses lewat jaringan. Lisensi SSPL, BSL, dan RSAL membatasi pemakaian komersial. IRAMA memilih komponen berlisensi permisif, memakai komponen LGPL, MPL, dan EPL sebatas aturannya, dan menghindari komponen AGPL, SSPL, BSL, dan RSAL. |
| MapLibre dan OpenStreetMap (OSM) | OpenStreetMap adalah peta dunia gratis yang disusun sukarelawan, dan MapLibre adalah pustaka gratis untuk menampilkan peta di aplikasi web. Keduanya dipakai untuk peta simpang dan wizard konfigurasi tanpa biaya lisensi peta. |
| MediaMTX | Aplikasi gratis untuk menyiarkan ulang video, termasuk memutar file rekaman seolah-olah siaran langsung dari kamera. Di IRAMA dipakai untuk menguji mode siaran langsung dengan rekaman sebelum ada akses resmi ke kamera Dishub. |
| Mode bayangan (shadow mode) | Cara menguji algoritma baru dengan data nyata tanpa benar-benar mengubah lampu; keputusannya hanya dicatat dan dibandingkan. Setelah terbukti aman barulah algoritma diizinkan mengendalikan lampu. |
| MQTT | Protokol pengiriman pesan ringan yang hemat kuota, cocok untuk perangkat di lapangan yang koneksinya tidak stabil. |
| mTLS | Cara pengamanan hubungan antar komputer ketika kedua pihak saling menunjukkan sertifikat digital sebelum bertukar data. |
| Multi-tenant | Satu sistem yang melayani banyak kota sekaligus, dengan data setiap kota terpisah dan tidak bisa saling melihat. Direncanakan untuk T5. |
| NEMA TS 2 dan TS 8 | Standar Amerika Serikat untuk kabinet dan controller lampu lalu lintas (TS 2) serta keamanan siber kabinet (TS 8). Dokumennya berbayar, sehingga baru dibeli di T4 bila dibutuhkan kontrak. |
| NTCIP | Kumpulan standar komunikasi terbuka dari Amerika Serikat untuk perangkat lalu lintas, termasuk controller. Dengan NTCIP, perangkat dari berbagai merek dapat diatur oleh satu sistem pusat. |
| NumPy dan SciPy | Pustaka gratis berbahasa Python untuk perhitungan angka dan optimasi. Modul optimasi IRAMA memakainya untuk mencari siklus dan pembagian hijau terbaik. |
| NVR | Singkatan dari Network Video Recorder, alat perekam video dari kamera jaringan yang biasanya ada di ruang kendali. Rekaman dari NVR dapat menjadi masukan Vision Tracker. |
| OER | Singkatan dari Octet Encoding Rules, cara pengodean ringkas dalam standar NTCIP untuk menyalin banyak pengaturan controller sekaligus. Dipakai untuk mencadangkan dan memulihkan konfigurasi controller di T4. |
| On-prem | Aplikasi dipasang di server milik pengguna sendiri, misalnya di kantor Dishub, sehingga data tidak keluar dari lingkungan pemda. |
| ONVIF | Standar terbuka agar kamera jaringan dari berbagai merek dapat dikenali dan dikendalikan dengan cara yang sama. Dengan ONVIF dan RTSP, IRAMA tidak terikat pada merek kamera tertentu. |
| PC industri (IPC) | Komputer kecil yang dirancang tahan panas, debu, dan getaran untuk dipasang di lapangan. Salah satu pilihan perangkat edge di T4 selain Jetson. |
| PoE dan UPS | PoE (Power over Ethernet) mengalirkan listrik dan data lewat satu kabel jaringan ke kamera atau perangkat kecil, sedangkan UPS adalah baterai cadangan agar perangkat tetap menyala sesaat ketika listrik padam. |
| PostgreSQL, PostGIS, dan TimescaleDB | PostgreSQL adalah basis data terbuka yang andal, PostGIS menambahkan kemampuan menyimpan data peta, dan TimescaleDB menambahkan kemampuan menyimpan data deret waktu seperti hitungan per 15 menit. Ketiganya gratis dan menjadi fondasi penyimpanan IRAMA. |
| Prometheus dan Grafana | Prometheus adalah alat gratis untuk mencatat kesehatan server dan aplikasi, dan Grafana adalah alat untuk menampilkan grafiknya. Grafana berlisensi AGPL, sehingga di IRAMA hanya boleh dipakai sebagai alat terpisah tanpa diubah. |
| PWA | Singkatan dari Progressive Web App, aplikasi web yang dapat dipasang di ponsel dan tetap bekerja saat sinyal lemah. Direncanakan untuk aplikasi teknisi di T4. |
| RBAC | Singkatan dari Role Based Access Control, pengaturan hak akses berdasarkan peran, misalnya operator hanya boleh melihat, sedangkan engineer boleh mengubah konfigurasi. |
| React dan ECharts | React adalah pustaka gratis untuk membangun tampilan aplikasi web, dan ECharts adalah pustaka gratis untuk grafik interaktif. Keduanya dipakai untuk wizard dan dashboard IRAMA. |
| Redis, Valkey, EMQX, Mosquitto, dan NATS | Perangkat lunak untuk menyimpan data sementara (Redis, Valkey) dan mengantar pesan antarperangkat (EMQX, Mosquitto, NATS). Redis versi baru dan EMQX tidak lagi berlisensi bebas, sehingga IRAMA memakai Valkey, Mosquitto, atau NATS bila perlu. |
| Repositori | Tempat penyimpanan kode dan dokumen proyek beserta riwayat perubahannya. Repositori IRAMA berada di GitHub secara privat. |
| RS-232 | Jenis sambungan kabel data lama yang masih banyak dipakai controller buatan lokal. |
| RTSP | Protokol siaran video langsung dari kamera jaringan, umum dipakai kamera CCTV. |
| Simulasi | Percobaan di komputer yang meniru kejadian nyata. PM 96/2015 mewajibkan perubahan pengaturan lalu lintas disimulasikan dahulu sebelum ditetapkan. |
| SLO | Singkatan dari Service Level Objective, target teknis internal, misalnya status simpang tampil paling lambat lima detik. SLO dipakai untuk memastikan janji layanan (SLA) dapat dipenuhi. |
| SNMP | Protokol standar untuk membaca dan mengubah pengaturan perangkat jaringan, dipakai oleh standar NTCIP untuk berkomunikasi dengan controller. |
| Stream | Aliran video yang dikirim terus-menerus secara langsung dari kamera. |
| SUMO | Singkatan dari Simulation of Urban MObility, perangkat lunak simulasi lalu lintas gratis dari lembaga riset Jerman. SUMO menghidupkan kendaraan virtual di jalan virtual sehingga pengaturan lampu dapat diuji dahulu di komputer; di IRAMA dipakai sejak T2 untuk membuktikan rekomendasi. |
| TLS, Let's Encrypt, dan WireGuard | TLS adalah pengamanan standar hubungan internet yang ditandai gembok di peramban, Let's Encrypt adalah penyedia sertifikat TLS gratis, dan WireGuard adalah perangkat lunak VPN gratis. Ketiganya dipakai untuk mengamankan stream Dishub mulai T3. |
| TraCI | Antarmuka program untuk mengendalikan simulasi SUMO dari luar, misalnya mengubah waktu lampu saat simulasi berjalan. Dipakai untuk menguji rekomendasi IRAMA di SUMO. |
| VM | Singkatan dari virtual machine, komputer tiruan yang berjalan di dalam server fisik. Satu server fisik dapat dibagi menjadi beberapa VM. |
| VPN | Jalur khusus terenkripsi di atas internet agar data antar lokasi tidak bisa disadap. |
| WebRTC | Teknologi untuk menampilkan video langsung di peramban dengan jeda sangat kecil. Direncanakan untuk tampilan CCTV langsung di konsol pemantauan T3. |

### Istilah bisnis dan pengadaan

| Istilah | Penjelasan |
|---|---|
| AMS | Singkatan dari Annual Maintenance Service, biaya layanan pemeliharaan tahunan setelah perangkat lunak dibeli, biasanya dihitung sebagai persentase harga lisensi. |
| APBD | Anggaran Pendapatan dan Belanja Daerah, anggaran tahunan pemerintah daerah. Pembelian sistem oleh pemda umumnya harus direncanakan satu tahun sebelumnya dalam APBD. |
| B2B2G | Model penjualan melalui mitra: IRAMA menjual ke vendor atau integrator, lalu vendor menjual paket lengkapnya ke pemerintah. |
| BUMD | Badan Usaha Milik Daerah, perusahaan milik pemda, misalnya operator bus kota. BUMD dapat menjadi mitra atau pembeli, terutama untuk prioritas bus. |
| CC-Room | Command Center Room, sebutan umum ruang kendali atau pusat komando di pemda. Banyak kota sudah memiliki CC-Room yang menampilkan CCTV. |
| E-katalog | Katalog belanja elektronik pemerintah yang dikelola LKPP, tempat instansi membeli barang dan jasa secara langsung. Masuk e-katalog memudahkan pemda membeli IRAMA. |
| GTM | Singkatan dari go-to-market, strategi membawa produk ke pasar: siapa pembelinya, lewat jalur apa, dan dengan harga berapa. |
| Jasa kajian | Model penjualan awal IRAMA di T2. Tim menjalankan perangkat lunak di laptop sendiri dengan rekaman dari Dishub, lalu menyerahkan dashboard dan laporan kajian, sehingga Dishub tidak perlu memasang apa pun. |
| KPI | Singkatan dari Key Performance Indicator, ukuran utama keberhasilan, misalnya tundaan rata-rata atau akurasi hitungan. |
| MoSCoW | Cara memberi prioritas fitur: Must (wajib), Should (sebaiknya ada), Could (boleh ada), dan Won't (tidak dikerjakan saat ini). Dipakai di inventaris fitur IRAMA. |
| MoU | Singkatan dari Memorandum of Understanding, nota kesepahaman kerja sama antar pihak. Di IRAMA MoU dengan Dishub diperlukan sebelum memakai rekaman atau siaran kamera resmi. |
| MVP | Singkatan dari Minimum Viable Product, versi paling awal produk yang sudah bisa menunjukkan nilai utamanya. Di IRAMA, Tahap 1 (purwarupa) berperan sebagai MVP untuk pembuktian, dan Tahap 2 menjadi versi pertama yang dijual. |
| NDA | Singkatan dari Non-Disclosure Agreement, perjanjian kerahasiaan. NDA biasanya diminta vendor sebelum membagikan dokumentasi protokol controller. |
| Open-core | Model bisnis ketika bagian inti perangkat lunak dibuka gratis, sedangkan modul lanjutan dijual. IRAMA memakai model ini agar pemda percaya pada keterbukaan sistem sekaligus tetap ada pendapatan. |
| PDN dan BMP | PDN berarti produk dalam negeri, dan BMP adalah bobot manfaat perusahaan. Keduanya bersama TKDN menentukan preferensi produk dalam pengadaan pemerintah. |
| PKS | Singkatan dari perjanjian kerja sama, dokumen resmi kerja sama antara pemda dan pihak lain, misalnya kampus atau badan usaha, yang dapat menjadi dasar pilot tanpa tender. |
| PoC | Singkatan dari Proof of Concept, uji coba kecil untuk membuktikan sebuah gagasan dapat bekerja sebelum diputuskan untuk dibeli atau dikembangkan. |
| PT Perorangan dan OSS | PT Perorangan adalah badan usaha berbadan hukum yang dapat didirikan satu orang untuk usaha mikro dan kecil, dan OSS adalah sistem perizinan berusaha daring tempat PT Perorangan didaftarkan. Badan usaha dibutuhkan sebelum menandatangani MoU dengan Dishub. |
| SaaS | Singkatan dari Software as a Service, perangkat lunak yang dipakai lewat internet dengan berlangganan tanpa dipasang sendiri. |
| SLA | Singkatan dari Service Level Agreement, janji tingkat layanan, misalnya keluhan ditangani paling lama tiga jam. |
| Source code escrow | Penitipan salinan kode sumber kepada pihak ketiga yang netral. Bila penyedia berhenti beroperasi, pembeli tetap bisa mendapatkan kode tersebut sehingga sistemnya tidak terbengkalai. |
| TKDN | Tingkat Komponen Dalam Negeri, persentase kandungan lokal sebuah produk. Nilai TKDN memengaruhi peluang produk dibeli pemerintah. |
| Vendor lock-in | Kondisi ketika pembeli sulit berpindah ke penyedia lain karena sistemnya hanya bisa bekerja dengan produk atau layanan satu vendor. IRAMA dirancang agar risiko ini sekecil mungkin melalui standar terbuka, lisensi bebas, dan data yang bisa diekspor. |
