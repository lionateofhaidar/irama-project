# 14 — Arsitektur Sistem per Tahap (T1 sampai T5)

Status: 2026-09-13. Dokumen ini menjelaskan susunan sistem IRAMA pada tiap tahap dalam bahasa yang ditujukan untuk pembaca berlatar strategi IT. Rincian teknis (nama teknologi, ukuran server, daftar ADR) ada di `06_Arsitektur_Konseptual_dan_Opsi_Teknologi.md`; daftar fitur per tahap ada di `05`; alasan pembagian tahap ada di `04`.

## 1. Cara membaca arsitektur ini

Sistem selalu terdiri dari lima lapisan yang sama, dari jalan sampai layar pengguna.

| Lapisan | Isi | Analogi |
|---|---|---|
| Lapangan | lampu lalu lintas, alat pengatur di kabinet (controller), detektor, kamera, dan mulai T2 sebuah komputer kecil di kabinet (edge) | cabang/gerai |
| Komunikasi | kabel fiber atau modem seluler dari kabinet ke kantor | jaringan antar cabang |
| Pusat | server aplikasi dan basis data di kantor Dishub (atau cloud pemda) | kantor pusat dan gudang data |
| Integrasi | sambungan ke sistem instansi lain (Polri, operator bus, pemadam, pajak, portal kota) | kemitraan |
| Penyajian | layar operator ruang kendali, aplikasi teknisi, dashboard pimpinan dan publik | etalase dan laporan manajemen |

Tiap tahap menambah kemampuan pada lapisan tertentu tanpa membongkar tahap sebelumnya. Empat aturan berlaku sejak T1 dan tidak pernah berubah.

1. Lampu tetap bekerja sendiri bila pusat mati. Controller di kabinet menyimpan minimal delapan jadwal lokal (kewajiban PM 49/2014). Pusat hanya mengirim instruksi terbatas dan "detak jantung" berkala; bila detak berhenti, controller kembali ke jadwal lokal.
2. Pusat mengubah jadwal hanya lewat transaksi yang diperiksa dulu keabsahannya sebelum dikirim ke alat.
3. Setiap keputusan sistem dan setiap perintah operator disimpan bersama alasannya, sehingga bisa diaudit dan dijelaskan ke Polri, DPRD, atau warga.
4. Data disimpan hemat. Perhitungan dilakukan sedekat mungkin dengan sumbernya, data rinci disimpan singkat, data ringkasan disimpan lama, video tidak disimpan di pusat sampai T3.

## 2. Tahap 1, MVP "Lihat & Kelola"

Gambaran singkat: meja kerja perencana lalu lintas yang dilengkapi simulator. Belum ada sambungan ke lampu sungguhan.

Susunan sistem

| Lapisan | Yang ada di T1 |
|---|---|
| Lapangan | tidak ada perangkat; lampu digantikan simulator SUMO yang berperilaku seperti controller sungguhan. Bila Dishub mengizinkan, satu controller ber-IP boleh dibaca statusnya (hanya baca) |
| Komunikasi | tidak ada |
| Pusat | satu laptop atau satu VM kecil menjalankan aplikasi web, basis data (PostgreSQL dengan ekstensi peta dan deret waktu), dan simulator |
| Integrasi | sengaja tidak ada |
| Penyajian | aplikasi web untuk perencana: peta simpang, tampilan fase, editor jadwal, kalkulator, dashboard LOS, laporan sebelum-sesudah |

Alur data: data survei dan rekaman (lihat `13`) dimasukkan ke registri simpang. Kalkulator PKJI menghitung kapasitas, antrian, tundaan, dan kelas LOS. Perencana menyusun jadwal lampu, sistem memvalidasi keselamatannya (kuning, merah semua, hijau minimum), lalu jadwal dijalankan di simulator. Simulator menghasilkan catatan kejadian sepersepuluh detik dengan format yang sama seperti controller sungguhan. Dari catatan itu dihitung ukuran kinerja sinyal (ATSPM), dan hasilnya tampil di dashboard.

Mengapa disusun begini: dua orang dapat membangun dan mendemokan seluruh alur tanpa izin lapangan, tanpa biaya perangkat, dan tanpa risiko mengganggu lalu lintas. Format catatan kejadian yang sama dengan lapangan membuat semua yang dibangun di T1 langsung terpakai saat perangkat sungguhan tersambung di T2.

Ukuran: 3 sampai 5 simpang koridor pilot. Laptop 16 GB cukup.

## 3. Tahap 2, Siap Jual "Kendali Terkoordinasi"

Gambaran singkat: ruang kendali kecil yang dapat dijual ke Dishub yang sudah punya lampu, CCTV, dan jaringan, tanpa mengganti alat mereka.

Susunan sistem

| Lapisan | Tambahan di T2 |
|---|---|
| Lapangan | komputer kecil (edge) dipasang di kabinet yang controllernya hanya punya port serial. Tugasnya menerjemahkan protokol vendor, menyimpan data sementara bila jaringan putus, dan mengirim detak jantung. Controller yang sudah ber-IP dihubungi langsung dari pusat tanpa edge |
| Komunikasi | jaringan yang sudah dimiliki Dishub (fiber atau 4G). Semua lalu lintas data dienkripsi dan lewat VPN |
| Pusat | satu server 8 inti/32 GB di kantor Dishub untuk sampai 40 simpang dan 60 tampilan kamera. Ditambah modul kesehatan perangkat dan alarm, tiket keluhan, pembuat laporan wajib, gerbang video (menyalurkan CCTV ke layar tanpa merekam), dan pengelolaan pengguna dan peran |
| Integrasi | email dan WhatsApp untuk alarm; sambungan opsional ke aplikasi pengaduan kota |
| Penyajian | konsol operator (pilih program, mode manual untuk petugas, sinkron jam), dashboard kesehatan perangkat, dashboard publik sederhana, aplikasi ponsel teknisi (tiket, checklist pemeliharaan, foto, bisa offline) |

Alur perintah: operator memilih program atau mode dari konsol. Pusat mengirim instruksi terbatas (pilih program, sinkron jam, tahan atau lepas fase) beserta detak jantung. Perubahan jadwal dikirim sebagai paket transaksi yang diperiksa dulu, lalu diunduh ke controller. Bila jaringan putus, controller berjalan dengan jadwal lokal dan edge menyimpan catatan kejadian sampai jaringan pulih.

Alur data: controller atau edge mengirim catatan kejadian secara berkala dalam paket, sehingga bandwidth hemat. Pusat menyimpan data rinci 90 hari dan ringkasan 15 menit selama 5 tahun. Watchdog harian memeriksa gejala detektor rusak atau lampu bermasalah dan membuat tiket otomatis.

Mengapa disusun begini: nilai jual T2 adalah keandalan, akuntabilitas, dan laporan, dengan biaya server yang terjangkau pemda kecil. Edge hanya dipasang di kabinet yang benar-benar memerlukannya agar biaya dan pekerjaan lapangan minimal (keputusan "edge-light"). Pemasangan edge dirancang agar bisa dilakukan teknisi Dishub atau vendor dengan checklist, karena tim inti tidak memiliki teknisi lapangan.

Ukuran: sampai 40 simpang per server. Stabil 30 hari tanpa campur tangan menjadi syarat kelulusan.

## 4. Tahap 3, Transisi "Responsif"

Gambaran singkat: koridor yang mulai menyesuaikan diri dengan kondisi lalu lintas, dengan manfaat yang diukur sebelum melangkah ke adaptif penuh.

Susunan sistem

| Lapisan | Tambahan di T3 |
|---|---|
| Lapangan | kotak edge AI (komputer kecil ber-GPU) di simpang terpilih. Kamera yang ada diolah menjadi "detektor virtual": jumlah kendaraan, okupansi, panjang antrian per lajur, dan pembacaan pelat untuk bukti dan prioritas. Pengolahan pelat tunduk pada penilaian dampak perlindungan data dan retensi singkat |
| Komunikasi | sama dengan T2; edge AI hanya mengirim angka ringkasan, tanpa video |
| Pusat | dua server (aplikasi dan data) ditambah satu pekerja simulasi. Modul baru: pemilihan program otomatis menurut lalu lintas terukur, penalaan offset koridor dari data GPS dan kedatangan kendaraan, layanan permintaan prioritas bus (green extension dan early green), digital twin per koridor, mode bayangan (algoritma baru diuji dengan data hidup tanpa mengendalikan lampu), paket bukti pelanggaran untuk Polri |
| Integrasi | AVL operator bus (posisi dan keterlambatan bus), sumber data GPS, pengiriman bukti ke Polri |
| Penyajian | tampilan koridor (diagram waktu-ruang, arrivals on green), konsol prioritas, tampilan hasil simulasi sebelum jadwal ditetapkan (kewajiban PM 96/2015) |

Alur adaptif tahap ini: detektor virtual mengirim angka ke pusat setiap beberapa detik. Pusat memilih program yang paling cocok dari pustaka jadwal dan menyesuaikan offset antar simpang. Perubahan hanya dilakukan bila kondisi bertahan cukup lama, sehingga lampu tidak "gelisah". Bus yang terlambat mendapat tambahan hijau maksimal sepuluh detik, satu kali per siklus, tanpa memotong waktu penyeberangan pejalan kaki.

Mengapa disusun begini: pemda perlu bukti manfaat terukur (waktu tempuh, arrivals on green, split failure) sebelum membiayai adaptif penuh. Semua algoritma baru lewat urutan uji simulator, mode bayangan, lalu jalan sepi, lalu jam sibuk.

Ukuran: sampai 100 simpang, 5 sampai 10 koridor adaptif, edge AI di 10 sampai 30 simpang.

## 5. Tahap 4, Setara ITCS "Adaptif Terpadu"

Gambaran singkat: kemampuan setara ITCS DKI dengan standar terbuka: adaptif real-time terkoordinasi, prioritas bersyarat dan darurat, integrasi lintas instansi, ruang kendali skala kota.

Susunan sistem

| Lapisan | Tambahan di T4 |
|---|---|
| Lapangan | edge AI di semua simpang kritis; dukungan controller berstandar NTCIP versi terbaru termasuk objek prioritas; keamanan kabinet mengikuti NEMA TS 8 |
| Komunikasi | sertifikat dua arah (mTLS) untuk setiap edge; segmentasi jaringan |
| Pusat | cluster kecil tiga node atau cloud pemda. Mesin adaptif: alokasi hijau per siklus berdasarkan tekanan antrian (cyclic max-pressure) di simpang kritis, dengan siklus dan offset tetap agar green wave terjaga; pengendalian perimeter untuk kawasan pusat kota saat jenuh; prioritas bus bersyarat berdasarkan muatan dan keterlambatan; prioritas kendaraan darurat bertingkat yang hanya aktif bila target waktu tanggap terancam; layanan prediksi volume 15 sampai 60 menit; semua nilai antara model AI disimpan agar dapat dijelaskan |
| Integrasi | pusat kendali Polri, Back Office ETLE (bukti diverifikasi Polri, aplikasi tidak menerbitkan tilang), CAD pemadam dan ambulans, Bapenda dan DLH melalui perjanjian, pengelola tol, cuaca dan kualitas udara, portal kota |
| Penyajian | ruang kendali skala kota dengan video wall, banyak operator per shift, SLA keluhan, laporan efektivitas ke Dirjen/BPTJ/Gubernur, dashboard publik dengan metode yang dipublikasikan |

Alur adaptif tahap ini: setiap siklus, pusat menghitung tekanan antrian di semua kaki simpang kritis dan membagi ulang waktu hijau, dengan batas perubahan lima detik per siklus dan hijau minimum yang menghormati pejalan kaki. Bila kawasan pusat kota mendekati jenuh, gerbang masuk kawasan ditahan sedikit agar bagian dalam tidak macet total. Prioritas bus dan darurat diselesaikan oleh satu layanan yang mengatur urutan dan konflik.

Mengapa disusun begini: inti adaptif memakai metode yang terbukti stabil dan dapat dijelaskan; pembelajaran mesin hanya berperan sebagai penasihat. Ukuran kinerja sinyal berjalan sebagai pengamat independen untuk setiap algoritma, termasuk milik vendor lain.

Ukuran: 100 sampai 350 simpang satu kota; penyimpanan sekitar 10 TB.

## 6. Tahap 5, End-state "Platform Mobilitas Kota"

Gambaran singkat: satu platform melayani banyak kota, terbuka untuk algoritma pihak ketiga yang tervalidasi, dan menjadi dasar kebijakan pengelolaan permintaan perjalanan.

Susunan sistem

| Lapisan | Tambahan di T5 |
|---|---|
| Lapangan | fusi kamera dan radar untuk keselamatan pejalan kaki; siaran status lampu ke aplikasi navigasi (GLOSA) |
| Komunikasi | sama; tambahan kanal ke penyedia navigasi |
| Pusat | multi-tenant per kota dengan isolasi data; digital twin skala kota untuk uji kebijakan (ganjil-genap, penutupan jalan, acara); marketplace algoritma yang wajib lewat simulator dan mode bayangan dengan lapisan veto statistik; kalkulator ambang legal pembatasan kendaraan (V/C dan kecepatan) dan evaluasi tahunan otomatis; penasihat berbasis pembelajaran mesin yang hanya mengusulkan parameter kepada operator; gudang data dan mesin analitik besar |
| Integrasi | API publik dan data terbuka (kewajiban UU 22/2009 Pasal 250), sistem ERP/ganjil-genap pemprov, sistem informasi provinsi |
| Penyajian | benchmark antar kota untuk Kemenhub/BPTJ, portal data terbuka, e-learning operator bersertifikat |

Mengapa disusun begini: pemda kecil dapat berbagi ruang kendali, kementerian dapat mengawasi efektivitas banyak kota, dan riset kampus lokal dapat masuk ke lapangan dengan aman.

Infrastruktur: cloud multi-wilayah atau pusat data pemerintah, dengan skala otomatis.

## 7. Ringkasan lapisan per tahap

| Lapisan | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| Lapangan | simulator; 1 controller baca-saja (opsional) | edge ringan di kabinet serial; controller IP langsung | edge AI di simpang terpilih; detektor virtual; pelat | edge AI di semua simpang kritis; NTCIP terbaru | fusi radar; GLOSA |
| Komunikasi | tidak ada | jaringan Dishub + VPN | sama | mTLS, segmentasi | sama + kanal navigasi |
| Pusat | 1 laptop/VM | 1 server (≤40 simpang) | 2 server + pekerja simulasi (≤100 simpang) | cluster 3 node (100 sampai 350 simpang) | cloud/DC pemerintah, multi-kota |
| Integrasi | tidak ada | alarm email/WA; aduan kota | AVL bus, GPS, bukti ke Polri | Polri, ETLE, CAD, Bapenda, DLH, tol, cuaca | API publik, ERP, provinsi |
| Penyajian | web perencana | konsol operator, dashboard, aplikasi teknisi, publik | tampilan koridor, konsol prioritas, hasil simulasi | ruang kendali kota, video wall, laporan efektivitas | benchmark antar kota, portal data |
| Cara kendali | simulasi | pilih program terpusat, mode manual | responsif (pilih program otomatis, offset, prioritas dasar) | adaptif per siklus + perimeter + prioritas bersyarat/darurat | + algoritma pihak ketiga, penasihat ML |

## 8. Bagian yang tidak berubah sepanjang tahap

- Satu model data untuk semua jenis controller (standar NTCIP maupun vendor lokal), sehingga adaptor baru tidak mengubah aplikasi.
- Satu format catatan kejadian untuk lapangan dan simulator, sehingga ukuran kinerja dapat dibandingkan langsung.
- Urutan validasi untuk setiap perubahan cara kendali: simulator, uji dengan perangkat di meja, mode bayangan, jam sepi, jam sibuk, lalu perbandingan hidup-mati.
- Hierarki cadangan: adaptif turun ke jadwal terpusat, lalu jadwal lokal di controller, lalu mode aktuasi bebas, lalu kedip, dan terakhir pengaturan manual petugas. Setiap penurunan tercatat dan menjadi alarm.
- Kepemilikan data di tangan pemda; akses pihak lain lewat perjanjian; data pribadi (pelat, wajah) diproses hanya dengan dasar hukum dan retensi singkat.

## 9. Risiko arsitektur dan cara menguranginya

| Risiko | Dampak | Pengurangan |
|---|---|---|
| Protokol controller vendor tertutup | adaptor T2 tidak bisa dibangun | kuesioner `12`; perjanjian kerahasiaan dengan vendor; cadangan berupa pencatat masukan/keluaran kabinet |
| Jaringan Dishub sering putus | data hilang, kendali terputus | penyimpanan sementara di edge 24 sampai 72 jam; ringkasan per menit bila jaringan lemah; controller selalu punya jadwal lokal |
| Kamera buruk saat hujan atau malam | detektor virtual tidak akurat | pemeriksaan kesehatan detektor sebelum mode adaptif; turun otomatis ke jadwal bila kualitas rendah |
| Server pemda terbatas | sistem lambat | agregasi di edge, retensi bertingkat, video tidak disimpan di pusat sampai T3 |
| Ketergantungan pada satu vendor perangkat | harga dan dukungan dikunci | adaptor untuk lebih dari satu vendor sejak T2; NTCIP untuk pengadaan baru |
| Kewenangan Polri dan Dirjen | perubahan jadwal tertahan | alur persetujuan dalam aplikasi; catatan koordinasi; integrasi pusat kendali Polri di T4 |
| Tim kecil tanpa teknisi lapangan | pemasangan edge tertunda | edge dirancang untuk dipasang teknisi Dishub atau vendor dengan checklist dan dukungan jarak jauh |
