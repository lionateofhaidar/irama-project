# 12 — Kuesioner Survei Perangkat APILL/ATCS (untuk Dishub & vendor)

Status: siap pakai, 2026-09-13; direvisi 2026-09-14 untuk tahapan baru. Menjawab Q-01 (protokol & spesifikasi controller di kota pilot). Tujuan internal: (1) memastikan rekaman CCTV bisa diperoleh dan disalin untuk Vision Tracker (T2), serta stream bisa diakses setelah MoU (T3); (2) menentukan adaptor baca-saja (T3) dan kendali (T4), termasuk kebutuhan edge di T4; (3) mengetahui log atau riwayat yang bisa dipakai untuk ATSPM.

**Cara pakai (internal, jangan disertakan saat dibagikan):**
- Bagian A–G untuk **Dishub** (kepala UPT/ruang kendali/teknisi). Bagian H untuk **vendor/integrator**. Tiap wawancara 30–45 menit; lebih baik diisi sambil berkunjung ke ruang kendali dan satu kabinet simpang, sambil memotret panel controller & label perangkat (dengan izin).
- Bahasa sengaja sehari-hari; istilah teknis hanya bila lazim dipakai petugas (controller, kabinet, CCTV, fiber, modem).
- Hal yang **tidak ditanyakan karena sudah kita asumsikan** (Bagian I) — hanya dikonfirmasi bila jawaban lain mengindikasikan sebaliknya. Pertanyaan D21–D24 dan H8 (rekaman kamera) ditambahkan 2026-09-14 karena rekaman adalah masukan utama T2.
- Jawaban dicatat ke `docs/kb/10_Keputusan_dan_Pertanyaan_Terbuka.md` (Q-01) dan `docs/planning/03` (profil kota).

---

## Pengantar singkat (dibacakan/ditulis di atas formulir)

Kami sedang menyiapkan perangkat lunak pemantauan dan pengaturan lampu lalu lintas yang bisa dipakai bersama perangkat yang sudah terpasang, tanpa harus mengganti alat di lapangan. Supaya cocok dengan kondisi di sini, kami perlu memahami perangkat dan cara kerja yang sekarang berjalan. Tidak ada jawaban benar atau salah; kalau ada yang tidak diketahui, cukup tulis "tidak tahu" atau sebutkan siapa yang biasanya paham. Jawaban hanya dipakai untuk keperluan penyesuaian teknis.

Nama/jabatan responden: ______  Instansi/unit: ______  Tanggal: ______

## A. Gambaran umum simpang bersinyal

1. Kira-kira berapa jumlah simpang berlampu lalu lintas di kota ini? Berapa di antaranya yang sudah terhubung ke ruang kendali (ATCS)?
2. Simpang yang terhubung itu dipasang bertahap tahun berapa saja? Apakah perangkatnya berasal dari satu pengadaan/satu merek, atau campuran?
3. Adakah simpang yang dulu terhubung tetapi sekarang tidak lagi (putus jaringan, alat rusak, kontrak habis)? Kira-kira berapa dan kenapa?
4. Kalau boleh tahu, koridor atau simpang mana yang paling sering dikeluhkan warga atau pimpinan?

## B. Perangkat di kabinet simpang

5. Merek/tipe alat pengatur (controller) yang dipakai apa saja? (boleh lebih dari satu; bila ada, foto label di dalam kabinet sangat membantu)
   ☐ Javis  ☐ Qumicon  ☐ TKDN  ☐ Marktel  ☐ Siemens/Yunex  ☐ SWARCO  ☐ lainnya: ______  ☐ tidak tahu
6. Untuk mengubah waktu hijau/merah di satu simpang, biasanya petugas melakukannya dengan cara apa?
   ☐ langsung di kabinet (tombol/laptop)  ☐ dari ruang kendali  ☐ minta ke vendor  ☐ lainnya: ______
7. Apakah ada simpang yang bisa "menyesuaikan sendiri" lamanya hijau menurut kepadatan (pakai sensor/kamera penghitung)? Kalau ada, berapa simpang, dan sensornya jenis apa (kamera, loop di aspal, radar)?
8. Apakah controller-nya menyimpan jadwal sendiri (pagi/siang/sore/malam) sehingga tetap jalan normal bila hubungan ke ruang kendali putus? Pernah kejadian putus, lalu apa yang terjadi di lampu?
9. Di kabinet, kabel dari controller ke jaringan biasanya lewat apa?
   ☐ kabel fiber/LAN  ☐ modem seluler (4G)  ☐ radio/wireless  ☐ tidak ada jaringan  ☐ tidak tahu
10. Adakah alat tambahan di kabinet yang menjadi "perantara" antara controller dan jaringan (misalnya kotak kecil/komputer mini dari vendor)? Kalau ada, siapa yang memasang dan apa fungsinya?
11. Kamera di simpang: mereknya apa, dan apakah kameranya hanya untuk memantau (CCTV biasa) atau juga bisa menghitung kendaraan/membaca pelat? Rekaman kamera disimpan di mana dan berapa lama?

## C. Ruang kendali (ATCS)

12. Perangkat lunak yang dipakai di ruang kendali namanya apa, buatan siapa, dan tahun berapa dipasang? Apakah masih ada kontrak perawatan/dukungan dari vendornya?
13. Dari ruang kendali, apa saja yang bisa dilakukan sekarang?
   ☐ melihat status lampu  ☐ melihat CCTV  ☐ mengubah waktu hijau  ☐ mengganti jadwal/program  ☐ mengatur manual saat ada pejabat/darurat  ☐ menerima alarm bila alat rusak  ☐ lainnya: ______
14. Berapa petugas yang bertugas per shift, dan apa kegiatan rutin mereka sehari-hari (misalnya memantau CCTV, mengatur manual di jam sibuk)?
15. Kalau lampu di satu simpang padam/kedip, bagaimana ruang kendali tahu, dan apa langkah yang biasa dilakukan? Rata-rata berapa lama sampai teknisi tiba?
16. Apakah petugas kepolisian pernah/biasa meminta pengaturan manual? Bagaimana caranya (telepon, radio, datang ke ruang kendali)?

## D. Data dan catatan yang sudah ada

17. Apakah sistem sekarang menyimpan catatan/riwayat (misalnya berapa lama hijau tiap siklus, jumlah kendaraan, kapan alat rusak)? Kalau ada, bisa dilihat/diunduh dalam bentuk apa (Excel, laporan PDF, hanya di layar)?
18. Apakah ada data hasil survei lalu lintas (hitungan kendaraan, kecepatan, waktu tempuh) dalam 1–2 tahun terakhir? Disimpan siapa?
19. Untuk pelaporan ke pimpinan/DPRD/kementerian, laporan apa yang rutin dibuat dan seberapa sering? Bagian mana yang paling merepotkan dibuat?
20. Adakah daftar/inventaris perangkat (lokasi, merek, tahun pasang, kondisi)? Dalam bentuk apa?
21. Rekaman kamera di simpang disimpan di mana (alat perekam di ruang kendali, server vendor, atau di kameranya sendiri), dan biasanya tersimpan berapa hari sebelum tertimpa?
22. Kalau kami memerlukan rekaman satu simpang selama beberapa jam atau satu hari penuh, apakah rekamannya bisa disalin? Biasanya dalam bentuk apa (file video, flashdisk/hard disk, tautan unduhan), dan siapa yang bisa melakukannya?
23. Di simpang yang kameranya lebih dari satu, apakah setiap jalan masuk terlihat jelas sampai garis berhenti, dan apakah lampunya ikut terlihat? Kira-kira setinggi apa kamera dipasang?
24. Apakah tampilan kamera bisa dibuka dari luar ruang kendali (misalnya lewat VPN)? Apa syaratnya bila ada pihak lain yang ingin mengakses untuk uji coba?

## E. Masalah yang sering muncul

25. Tiga masalah teknis yang paling sering terjadi apa? (misalnya: jaringan putus, kamera rusak, controller hang, listrik padam, kabel dicuri/dirusak)
26. Ketika perangkat rusak, siapa yang memperbaiki (teknisi sendiri atau vendor)? Suku cadangnya mudah didapat?
27. Apa yang selama ini diinginkan dari sistem tetapi belum bisa dilakukan?

## F. Dokumen dan kontak

28. Apakah ada buku manual/dokumen teknis controller dan sistem ruang kendali yang bisa kami pelajari (bisa dipinjam/difoto)?
29. Boleh kami diperkenalkan ke kontak teknis vendor perangkat yang sekarang dipakai?

## G. Kerja sama uji coba (opsional, bila suasana mendukung)

30. Kalau ada perangkat lunak pemantauan tambahan yang tidak mengganggu sistem yang ada (hanya membaca), apakah dimungkinkan diuji di satu atau beberapa simpang? Apa syarat administrasinya (surat, nota kesepahaman, izin akses)?
31. Bila hasil kajian kami menyarankan pengaturan waktu lampu yang baru untuk satu simpang, apakah Dishub bersedia mencobanya lalu mengukur hasilnya bersama kami?
32. Dengan siapa hal ini sebaiknya dibicarakan lebih lanjut?

---

## H. Pertanyaan untuk vendor/integrator perangkat (30 menit)

1. Tipe controller yang paling banyak terpasang di kota-kota Jawa Barat/Jawa Timur apa, dan tahun produksinya?
2. Apakah sistem pusat pihak lain bisa membaca status dan mengubah program di controller tersebut? Lewat jalur apa (port serial di kabinet, jaringan, atau harus lewat server vendor)? Apakah dokumentasi antarmukanya bisa dibagikan dengan perjanjian kerahasiaan?
3. Apakah controller tipe terbaru sudah mendukung standar NTCIP? Bila belum, apakah ada rencana atau alat konversi?
4. Apakah controller menyimpan catatan kejadian (perubahan lampu, deteksi kendaraan) yang bisa diambil? Dalam bentuk apa dan seberapa rinci?
5. Untuk kamera analitik/penghitung: keluaran datanya bisa dikirim ke sistem lain? Dalam format apa?
6. Bagaimana skema kerja sama yang biasa dilakukan bila ada pihak yang menyediakan perangkat lunak pusat sementara perangkat lapangan dari Bapak/Ibu (mis. bundling di e-katalog, bagi peran perawatan)?
7. Apakah memungkinkan meminjam/menyewa satu unit controller untuk pengujian di meja kerja selama beberapa bulan?
8. Apakah alat perekam atau perangkat lunak kamera yang Bapak/Ibu pasang bisa menyalin rekaman ke file video biasa (misalnya MP4) dan menyediakan siaran langsung dengan format umum (misalnya RTSP)?

---

## I. Asumsi internal (tidak ditanyakan; diverifikasi lewat jawaban B5–B10, H2–H4)

| Asumsi | Dasar | Dampak bila ternyata salah |
|---|---|---|
| Controller lokal (Javis/Qumicon/TKDN/Marktel) memakai protokol vendor lewat port serial RS-232/RS-485 di kabinet, bukan NTCIP | SK 7234/2013; profil vendor e-katalog; majalah ITCS DKI (RS-232 ke controller) | Bila NTCIP tersedia → adaptor SNMP langsung, edge tidak wajib |
| Komunikasi ke ruang kendali via fiber/Metro-E untuk pusat kota dan modem 4G untuk pinggiran | Pola ATCS kota-kota Indonesia (KB-09) | Bila hanya 4G → buffer edge & agregasi wajib sejak T4 |
| CCTV IP standar (RTSP/ONVIF), disimpan di NVR vendor, tanpa analitik hitung kendaraan pada sebagian besar simpang | Surabaya 580 kamera/8 sensor adaptif; Bandung CCTV publik | Bila kamera analitik ada → keluarannya dipakai sebagai pembanding; hitungan utama tetap dari Vision Tracker (U-08 direvisi) |
| Controller menyimpan ≥8 program TOD lokal dan tetap berjalan saat putus jaringan | PM 49/2014 Ps.14; SK 7234 (≥4–16 program) | Bila tidak → fallback pusat lebih rumit; prioritas rendah untuk simpang tersebut |
| Tidak ada log hi-res 0,1 s dari controller; riwayat hanya di server vendor (bila ada) | Umum di ATCS Indonesia | Bila ada → ATSPM langsung dari log; tanpa itu → metrik dari status lampu kamera (T3) lalu edge logger (F-T2-31, T4) |
| Perangkat lunak ruang kendali adalah produk vendor tertutup tanpa API | Pola vendor lokal | Bila ada API → integrasi paralel, tanpa mengganti |
| Petugas mengatur manual jam sibuk lewat perangkat lunak vendor atau telepon ke teknisi | Alur kerja TMC (KB-09) | Menentukan desain mode manual F-T2-38 |
| Rekaman NVR tersimpan sekitar 7 sampai 30 hari dan dapat disalin ke berkas video oleh petugas atau vendor | Praktik umum NVR [A] | Bila tidak bisa → rekam sendiri atau tunggu stream setelah MoU (`13`) |

Sumber rujukan internal: `docs/kb/09_Konteks_Jakarta_dan_Kota_Target.md`, `docs/planning/03`, `docs/sources/_ringkasan/R00 §H` (SK 7234), `R03 §D.2` (adaptor).
