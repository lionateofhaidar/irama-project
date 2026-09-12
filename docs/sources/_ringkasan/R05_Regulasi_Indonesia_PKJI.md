# R05 — Catatan Studi Regulasi Indonesia, PKJI 2023, dan Format Proyek Perubahan PKN II
## Untuk perancangan aplikasi Intelligent/Integrated Traffic Control System (ITCS) DKI Jakarta

Sumber: hasil ekstraksi teks (pdftotext) di folder `docs/sources/_teks_ekstraksi/`. Semua rujukan pasal di bawah diambil langsung dari teks ekstraksi; jika sebuah ketentuan **tidak ditemukan** dalam teks, hal itu dinyatakan secara eksplisit. Nomor halaman PKJI mengacu pada penomoran "xx dari 326" yang tercetak di dokumen.

Catatan kualitas sumber:
- `Permenhub_PM_76_2021_...txt` hanya berisi **abstrak** (28 baris, 1.490 byte), bukan batang tubuh. Pasal-pasal PM 76/2021 **tidak dapat dikutip** dari korpus ini.
- `Draf_Raperda_Rencana_Induk_Transportasi_Jakarta.txt` **kosong** (0 baris).
- Pada `Permenhub_PM_49_2014_...txt` label "Pasal N" hilang saat ekstraksi; nomor pasal di bawah **direkonstruksi** dari rujukan silang internal (mis. "sebagaimana dimaksud dalam Pasal 19 huruf a") dan ditandai (*rekonstruksi*).
- `Perpres_55_2018_...txt` hasil OCR buruk pada tabel lampiran; kutipan diambil dari bagian yang terbaca.

---

## A. Kajian per regulasi

### A.1 UU No. 22 Tahun 2009 tentang Lalu Lintas dan Angkutan Jalan (LN 2009/96, TLN 5025)

**Identitas & struktur.** 22 Bab, 326 pasal. Bab yang relevan untuk ITCS: Bab I Ketentuan Umum; Bab V Penyelenggaraan (Pasal 7–13, termasuk Forum LLAJ); Bab VI Jaringan LLAJ (Pasal 25–28 perlengkapan jalan); Bab IX Lalu Lintas (Pasal 93–98 MRLL; Pasal 99–101 Andalalin; Pasal 102–104 pengutamaan APILL/rambu/marka/petugas; Pasal 106 kewajiban pengemudi; Pasal 133 manajemen kebutuhan lalu lintas; Pasal 134–135 hak utama); Bab XIV Keamanan dan Keselamatan (Pasal 200–204); Bab XVI Sistem Informasi dan Komunikasi LLAJ (Pasal 245–252); Bab XIX Penyidikan dan Penindakan (Pasal 260–272); Bab XX Ketentuan Pidana (Pasal 273–317); Bab XXII Penutup (Pasal 321–322).

**Definisi resmi (Pasal 1).**
- Angka 6: *Prasarana LLAJ* adalah Ruang Lalu Lintas, Terminal, dan Perlengkapan Jalan "yang meliputi marka, rambu, Alat Pemberi Isyarat Lalu Lintas, alat pengendali dan pengaman Pengguna Jalan, alat pengawasan dan pengamanan Jalan, serta fasilitas pendukung."
- Angka 19: *Alat Pemberi Isyarat Lalu Lintas* (APILL) adalah "perangkat elektronik yang menggunakan isyarat lampu yang dapat dilengkapi dengan isyarat bunyi untuk mengatur Lalu Lintas orang dan/atau Kendaraan di persimpangan atau pada ruas Jalan."
- Angka 29: *Manajemen dan Rekayasa Lalu Lintas* (MRLL) adalah "serangkaian usaha dan kegiatan yang meliputi perencanaan, pengadaan, pemasangan, pengaturan, dan pemeliharaan fasilitas perlengkapan Jalan dalam rangka mewujudkan, mendukung dan memelihara keamanan, keselamatan, ketertiban, dan kelancaran Lalu Lintas."
- Angka 30–33: definisi Keamanan, Keselamatan, Ketertiban, Kelancaran LLAJ (empat tujuan normatif; "Kelancaran" = "bebas dari hambatan dan kemacetan di Jalan").
- Angka 34: *Sistem Informasi dan Komunikasi LLAJ* adalah "sekumpulan subsistem yang saling berhubungan dengan melalui penggabungan, pemrosesan, penyimpanan, dan pendistribusian data yang terkait dengan penyelenggaraan Lalu Lintas dan Angkutan Jalan."

**Pembagian urusan (Pasal 7–13) — siapa berwenang.**
- Pasal 7 ayat (2): urusan sarana & prasarana LLAJ → kementerian bidang sarana dan prasarana LLAJ (Kemenhub); urusan **"Registrasi dan Identifikasi Kendaraan Bermotor dan Pengemudi, Penegakan Hukum, Operasional Manajemen dan Rekayasa Lalu Lintas, serta pendidikan berlalu lintas"** → Kepolisian (Polri).
- Pasal 9: Kemenhub antara lain menyelenggarakan MRLL (huruf b) dan "pengembangan sistem informasi dan komunikasi di bidang sarana dan Prasarana LLAJ" (huruf e).
- Pasal 12: Polri antara lain melakukan "pengumpulan, pemantauan, pengolahan, dan penyajian data LLAJ" (c), "pengelolaan pusat pengendalian Sistem Informasi dan Komunikasi LLAJ" (d), penegakan hukum (f), "pelaksanaan Manajemen dan Rekayasa Lalu Lintas" (h), dan "pelaksanaan manajemen operasional Lalu Lintas" (i).
- Pasal 13: penyelenggaraan LLAJ "dilakukan secara terkoordinasi" oleh **Forum LLAJ**, yang bertugas koordinasi antarinstansi; keanggotaan: pembina, penyelenggara, akademisi, masyarakat. Pasal 321: Forum harus dibentuk ≤1 tahun sejak UU berlaku.

**Perlengkapan jalan (Pasal 25–28).** Pasal 25 ayat (1): setiap jalan untuk lalu lintas umum wajib dilengkapi perlengkapan jalan termasuk APILL (huruf c) dan "alat pengawasan dan pengamanan Jalan" (huruf f). Pasal 26: penyediaan oleh Pemerintah (jalan nasional), pemerintah provinsi (jalan provinsi), kab/kota, atau BUJT (tol). Pasal 28 ayat (2): setiap orang dilarang mengganggu fungsi perlengkapan jalan; sanksi Pasal 275 (gangguan fungsi APILL: kurungan ≤1 bulan/denda ≤Rp250.000; merusak hingga tidak berfungsi: penjara ≤2 tahun/denda ≤Rp50 juta).

**MRLL (Pasal 93–98).**
- Pasal 93 ayat (1): MRLL "dilaksanakan untuk mengoptimalkan penggunaan jaringan Jalan dan gerakan Lalu Lintas". Ayat (2) delapan cara, termasuk (f) "pengendalian Lalu Lintas pada persimpangan" dan (g) "pengendalian Lalu Lintas pada ruas Jalan". Ayat (3) lima kegiatan: perencanaan, pengaturan, perekayasaan, pemberdayaan, pengawasan.
- Pasal 94 ayat (1): perencanaan mencakup identifikasi masalah, inventarisasi/analisis arus, kebutuhan angkutan, daya tampung jalan, daya tampung kendaraan, "angka pelanggaran dan Kecelakaan", dampak lalu lintas, "penetapan tingkat pelayanan", dan penetapan rencana kebijakan. Ayat (3) perekayasaan mencakup (b) "pengadaan, pemasangan, perbaikan, dan pemeliharaan perlengkapan Jalan" dan (c) "optimalisasi operasional rekayasa Lalu Lintas dalam rangka meningkatkan ketertiban, kelancaran, dan efektivitas penegakan hukum". Ayat (5) pengawasan: penilaian pelaksanaan kebijakan, tindakan korektif, penegakan hukum.
- Pasal 95: kebijakan penggunaan jaringan jalan yang berupa perintah/larangan/peringatan/petunjuk diatur dengan Permen (jalan nasional) atau **Perda provinsi** (jalan provinsi), dan ayat (2) "harus dinyatakan dengan Rambu Lalu Lintas, Marka Jalan, dan/atau Alat Pemberi Isyarat Lalu Lintas."
- Pasal 96 ayat (4): "Gubernur bertanggung jawab atas pelaksanaan MRLL ... untuk jalan provinsi setelah mendapat rekomendasi dari instansi terkait." Ayat (3): Kapolri bertanggung jawab atas Pasal 94 ayat (3) huruf c (optimalisasi operasional) dan ayat (5) (pengawasan).
- Pasal 97: dalam perubahan arus "secara tiba-tiba atau situasional", Polri dapat melaksanakan MRLL kepolisian dengan rambu/APILL/alat pengendali "yang bersifat sementara"; Polri dapat memberi rekomendasi MRLL kepada instansi terkait.
- Pasal 98 ayat (1): "Penanggung jawab pelaksana MRLL wajib berkoordinasi dan membuat analisis, evaluasi, dan laporan pelaksanaan berdasarkan data dan kinerjanya." Ayat (2): laporan disampaikan kepada Forum LLAJ.

**Kekuatan hukum dan hierarki isyarat (Pasal 102–104, 135).**
- Pasal 102: pemasangan APILL/rambu/marka harus selesai ≤60 hari sejak pemberlakuan Permen/Perda; "mempunyai kekuatan hukum yang berlaku mengikat 30 (tiga puluh) hari setelah tanggal pemasangan."
- Pasal 103 ayat (1): APILL yang bersifat perintah/larangan **diutamakan** daripada rambu dan marka; ayat (3): saat kemacetan yang tidak memungkinkan gerak kendaraan, "fungsi marka kotak kuning harus diutamakan daripada APILL".
- Pasal 104: dalam keadaan tertentu petugas Polri dapat memberhentikan, memerintahkan jalan terus, mempercepat, memperlambat, mengalihkan arus; ayat (2) tindakan itu "wajib diutamakan daripada perintah yang diberikan oleh APILL, Rambu, dan/atau Marka". Sanksi tidak patuh: Pasal 282.
- Pasal 134–135: kendaraan hak utama (pemadam, ambulans, dst.); Pasal 135 ayat (3): "APILL dan Rambu Lalu Lintas tidak berlaku bagi Kendaraan yang mendapatkan hak utama."
- Pasal 106 ayat (4) huruf c: pengemudi wajib mematuhi APILL; Pasal 287 ayat (2): pelanggaran APILL dipidana kurungan ≤2 bulan atau denda ≤Rp500.000.

**Manajemen kebutuhan lalu lintas (Pasal 133).** Kriteria: V/C, ketersediaan angkutan umum, kualitas lingkungan. Cara: pembatasan kendaraan perseorangan, barang, sepeda motor, KBU, ruang parkir, kendaraan tidak bermotor umum pada koridor/kawasan/waktu tertentu. Ayat (3): pembatasan perseorangan & barang "dapat dilakukan dengan pengenaan retribusi pengendalian Lalu Lintas" (dasar ERP). Ayat (4): ditetapkan dan "dievaluasi secara berkala" oleh Menteri/pemprov/pemkab-kot.

**Sistem Informasi dan Komunikasi LLAJ (Pasal 245–252) — dasar hukum TMC/pusat kendali.**
- Pasal 245: diselenggarakan "sistem informasi dan komunikasi yang terpadu"; dilaksanakan Pemerintah, **pemerintah provinsi**, kab/kota; digunakan untuk "perencanaan, pengaturan, pengendalian, dan pengawasan serta operasional LLAJ".
- Pasal 246 ayat (2): sistem terpadu "dikendalikan oleh pusat kendali yang mengintegrasikan data, informasi, dan komunikasi dari setiap subsistem"; ayat (3) data "harus dapat diakses oleh setiap pembina LLAJ".
- Pasal 247: setiap pembina "wajib mengelola subsistem informasi dan komunikasi LLAJ sesuai dengan kewenangannya"; subsistem "terintegrasi dalam pusat kendali"; ayat (3) **"Pusat kendali ... dikelola oleh Kepolisian Negara Republik Indonesia."**
- Pasal 248: pengembangan meliputi sistem terstruktur, jaringan informasi/komunikasi, pusat data, untuk: perencanaan, perumusan kebijakan, pemantauan, pengawasan, pengendalian, informasi geografi, pelacakan, informasi pengguna jalan, "pendeteksian arus Lalu Lintas", "pengenalan tanda nomor Kendaraan Bermotor", "pengidentifikasian Kendaraan Bermotor di Ruang Lalu Lintas".
- Pasal 249: fungsi pusat kendali: kendali, koordinasi, komunikasi, data terpadu, pelayanan masyarakat, "rekam jejak elektronis untuk penegakan hukum"; kegiatan minimal termasuk "dukungan penegakan hukum dengan alat elektronik dan secara langsung", "pemberian informasi kualitas baku mutu udara", "dukungan pengendalian pergerakan LLAJ".
- Pasal 250: "Data dan informasi pada pusat kendali ... harus dapat diakses dan digunakan oleh masyarakat."
- Pasal 251: SIK dapat digunakan untuk penegakan hukum (penyelidikan/penyidikan; penanganan kecelakaan, pelanggaran, kemacetan oleh Polri; pengejaran/penindakan).
- Pasal 322: pusat kendali harus dibentuk ≤2 tahun sejak UU berlaku.

**Penegakan hukum elektronik dan penyidik (Pasal 260–262, 272).**
- Pasal 272: "(1) Untuk mendukung kegiatan penindakan pelanggaran di bidang LLAJ, dapat digunakan peralatan elektronik. (2) Hasil penggunaan peralatan elektronik ... dapat digunakan sebagai alat bukti di pengadilan." Ini dasar ETLE.
- Pasal 260: kewenangan penyidik Polri (menghentikan, menyita, menindak, dsb.).
- Pasal 262: PPNS berwenang terbatas pada persyaratan teknis/laik jalan, perizinan angkutan, muatan/dimensi; dilaksanakan di terminal/jembatan timbang; ayat (3) jika di jalan "wajib berkoordinasi dengan dan harus didampingi oleh Petugas Polri."
- Pasal 204 ayat (2): KBU harus dilengkapi alat pemberi informasi kecelakaan "ke Pusat Kendali Sistem Keselamatan LLAJ".

### A.2 PP No. 32 Tahun 2011 tentang Manajemen dan Rekayasa, Analisis Dampak, serta Manajemen Kebutuhan Lalu Lintas (LN 2011/61, TLN 5221)

**Struktur.** 5 Bab, 85 pasal: Bab I Ketentuan Umum (Pasal 1); Bab II MRLL (Pasal 2–46: perencanaan 4–21, pengaturan 22–27, perekayasaan 28–35, pemberdayaan 36–42, pengawasan 43–46); Bab III Andalalin (47–59); Bab IV Manajemen Kebutuhan Lalu Lintas (60–83); Bab V Penutup (84–85). Ditetapkan 21 Juni 2011.

**Definisi tambahan (Pasal 1).** Angka 8: MKLL "kegiatan yang dilaksanakan dengan sasaran meningkatkan efisiensi dan efektivitas penggunaan ruang lalu lintas dan mengendalikan pergerakan lalu lintas." Angka 9: Tingkat pelayanan "ukuran kuantitatif dan kualitatif yang menggambarkan kondisi operasional lalu lintas." Angka 11–14: Volume (kend/jam atau smp/jam), Kapasitas, Kecepatan (km/jam), Tundaan ("waktu tambahan yang diperlukan untuk melewati persimpangan dibandingkan dengan situasi tanpa persimpangan").

**Kewenangan MRLL (Pasal 2–5).** Pasal 2: tanggung jawab Menhub (jalan nasional), Menteri PU (jalan nasional), Kapolri (semua status jalan), gubernur (jalan provinsi), bupati, walikota. Pasal 5 ayat (2)–(3): perencanaan oleh gubernur "dilaksanakan setelah mendapatkan rekomendasi" Kemenhub, Kemen PU, dan Polri ("mengenai operasional MRLL"); ayat (5) berkoordinasi dengan provinsi berbatasan.

**Perencanaan — data yang wajib dikelola (Pasal 6–21).**
- Pasal 7 huruf d: gubernur mengidentifikasi masalah termasuk "kapasitas jalan", "pengaturan lalu lintas", "kinerja lalu lintas", "lokasi potensi kecelakaan dan kemacetan".
- Pasal 9 huruf d: gubernur menginventarisasi "volume lalu lintas; ... komposisi; variasi; distribusi arah; pengaturan arus; kecepatan dan tundaan lalu lintas; kinerja perlengkapan jalan; perkiraan volume lalu lintas yang akan datang."
- Pasal 16 ayat (2): Polri "pengumpulan data, menyusun pangkalan data, serta analisis pelanggaran dan kecelakaan lalu lintas eksisting pada setiap ruas jalan" (pangkalan data pelanggaran ada di Polri).
- Pasal 19: penetapan tingkat pelayanan oleh gubernur (ayat 2 b); indikator ayat (3): V/C, kecepatan, waktu perjalanan, kebebasan bergerak, keamanan, keselamatan, ketertiban, kelancaran, penilaian pengemudi.
- Pasal 21 huruf d: gubernur menetapkan kebijakan lalu lintas "yang berlaku pada setiap ruas jalan dan/atau persimpangan."

**Pengaturan (Pasal 22–27).** Pasal 24: perintah/larangan per ruas jalan provinsi "ditetapkan oleh gubernur"; yang bersifat umum diatur Perda provinsi. Pasal 27: kebijakan "diinformasikan kepada masyarakat."

**Perekayasaan (Pasal 28–35).**
- Pasal 31 ayat (2): perbaikan & pemeliharaan meliputi "memantau keberadaan dan kinerja perlengkapan jalan", menyingkirkan penghalang, mengembalikan posisi, mengganti yang rusak/hilang. Ayat (3): dilakukan gubernur untuk jalan provinsi.
- Pasal 33: daftar perlengkapan jalan yang berkaitan langsung dengan pengguna jalan (APILL, rambu, marka, penerangan, dll.).
- Pasal 34: optimalisasi operasional rekayasa dilakukan dalam situasi: perubahan lalu lintas tiba-tiba/situasional; **"alat pemberi isyarat lalu lintas tidak berfungsi"**; pengguna jalan yang diprioritaskan; pekerjaan jalan; kerusakan infrastruktur; kecelakaan; bencana; konflik sosial; terorisme. Pasal 35 ayat (1): **dilaksanakan oleh Polri**, melalui pengaturan arus di ruas/simpang, penertiban lajur, penertiban hambatan samping, dengan APILL/rambu/alat pengarah "yang bersifat sementara."

**Pengawasan (Pasal 43–46).** Pasal 44 huruf c: gubernur "pemantauan dan analisis terhadap efektivitas pelaksanaan kebijakan untuk jalan provinsi"; Polri menilai tingkat kamseltibcar, tingkat pelanggaran, efektivitas penegakan hukum. Pasal 46: penegakan hukum oleh Polri; ayat (3) **"dapat dilakukan dengan cara langsung atau tidak langsung melalui media elektronik."**

**Manajemen Kebutuhan Lalu Lintas (Pasal 60–83) — dasar pembatasan/ERP/ganjil-genap.**
- Pasal 60–61: kriteria (V/C, angkutan umum, lingkungan); strategi simultan-terintegrasi termasuk "mengendalikan lalu lintas di ruas jalan tertentu dan persimpangan".
- Pasal 62: pembatasan "wajib dinyatakan dengan rambu lalu lintas." Pasal 63: gubernur untuk jalan provinsi setelah masukan bupati/walikota; ayat (2) "dievaluasi setiap tahun."
- Pasal 64–66 (kendaraan perseorangan: MP, bus, mobil barang JBB ≤3.500 kg): kriteria Pasal 65 — V/C ≥0,7 pada salah satu jalur; kecepatan rata-rata jam puncak <30 km/jam; tersedia angkutan umum trayek memenuhi SPM; Pasal 66 cara: berdasarkan "jumlah penumpang; dan/atau tanda nomor kendaraan bermotor" (dasar 3-in-1/ganjil-genap).
- Pasal 67–69 (barang JBB >3.500 kg): V/C ≥0,7; <30 km/jam; tersedia jalan alternatif.
- Pasal 70–71 (sepeda motor): V/C ≥0,5 dan angkutan umum SPM; dilakukan dengan melarang melalui lajur/jalur tertentu.
- Pasal 72–75 (parkir): V/C ≥0,7; <30 km/jam; diatur Perda.
- Pasal 79–83 (retribusi pengendalian lalu lintas = ERP): kriteria ayat (2): V/C ≥0,9; 2 jalur masing-masing 2 lajur; kecepatan rata-rata jam puncak ≤10 km/jam; angkutan umum massal SPM; ayat (3) **"tidak dapat dilakukan pada jalan nasional"**. Pasal 80: retribusi jasa umum, hasil hanya untuk peningkatan kinerja lalu lintas dan pelayanan angkutan umum. Pasal 81: pemda wajib menyediakan "sistem dan peralatan yang diperlukan". Pasal 82 ayat (1) c: peningkatan kinerja lalu lintas termasuk "pemeliharaan dan pengembangan teknologi untuk kepentingan lalu lintas". Pasal 83: diatur Perda (kawasan, besaran, tata cara, pemanfaatan).

### A.3 Permenhub PM 96 Tahun 2015 tentang Pedoman Pelaksanaan Kegiatan MRLL (BN 2015/834)

**Struktur.** 8 pasal batang tubuh + Lampiran I (Pedoman: Bab I–VI), Lampiran II (Tata Cara Pelaksanaan MRLL: A–H), Lampiran III (persetujuan MRLL di jalan nasional). Mencabut KM 14/2006.

**Batang tubuh.** Pasal 1 ayat (3): tanggung jawab MRLL (Menhub, Menteri PU, Kapolri, gubernur, bupati, walikota); ayat (4) dilaksanakan "oleh pejabat dan petugas yang mempunyai kompetensi di bidang MRLL." Pasal 4: delapan cara MRLL (sama dengan UU Pasal 93). **Pasal 5 ayat (2): "Pelaksanaan kegiatan MRLL di jalan nasional yang berada di Provinsi DKI Jakarta dapat dilakukan oleh gubernur setelah mendapat persetujuan Direktur Jenderal Perhubungan Darat"**; ayat (3) hanya untuk kegiatan perencanaan dan perekayasaan. Pasal 6: pembinaan teknis oleh Dirjen Hubdat.

**Lampiran I — Bab II Perencanaan.**
- 8 kegiatan; **5 wajib**: identifikasi masalah; inventarisasi & analisis arus; daya tampung jalan; penetapan tingkat pelayanan; penetapan rencana kebijakan.
- Identifikasi masalah dapat melalui "pengamatan lapangan ... menggunakan peralatan teknis, misalnya kamera", masukan masyarakat, data historis (termasuk "data spasial dari media elektronik").
- Volume: LHRT (pencacahan ≥4×/tahun, lebih baik bulanan; 7 hari direkomendasikan, minimal 2 hari); VJP = 9% LHRT (jalan kota), 11% (antar kota).
- Kecepatan: spot speed (time mean speed, space mean speed), travel speed (termasuk semua tundaan berhenti), free flow speed.
- Tundaan pada simpang ber-APILL: tundaan lalu lintas (delay traffic) dan tundaan geometrik.
- Kinerja perlengkapan jalan dinilai dari: keberadaan (ada/tidak), lokasi (tepat/tidak), kondisi (baik/rusak), fungsi (berguna/tidak).
- Perkiraan volume: tren historis atau model simulasi; skenario "do nothing" vs "do something".
- **Tingkat pelayanan ruas (A–F)** dengan kecepatan minimal: A ≥80 km/jam; B ≥70; C ≥60; D ≥50; E ≥30 (antar kota) / ≥10 (perkotaan) dengan volume mendekati kapasitas; F <30 km/jam, antrian panjang, "kecepatan maupun volume turun sampai 0".
- **Tingkat pelayanan persimpangan (A–F) berdasarkan tundaan per kendaraan**: A <5 detik; B >5–15; C >15–25; D >25–40; E >40–60; F >60 detik/kendaraan.
- **Target LOS minimal** jaringan primer: arteri primer ≥B; kolektor primer ≥B; lokal primer ≥C; tol ≥B. Jaringan sekunder: arteri sekunder ≥C; kolektor sekunder ≥C; lokal sekunder ≥D; lingkungan ≥D. "Tingkat pelayanan ditetapkan oleh Direktur Jenderal, Gubernur, Bupati dan Walikota sesuai kewenangan."
- Penetapan rencana kebijakan: skema penanganan → pemilihan alternatif (dapat melalui Forum LLAJ) → **"Usulan alternatif penanganan lalu lintas terpilih harus disimulasikan sebelum ditetapkan"** → penetapan (data dukung: peta ruas, tata letak perlengkapan jalan, arah arus).

**Lampiran I — Bab III Pengaturan.** Untuk jalan provinsi, perintah/larangan per ruas termasuk "penetapan lokasi dan jenis APILL yang dipasang pada ruas dan/atau persimpangan" ditetapkan dengan **Keputusan Gubernur**; hasil penetapan "harus disosialisasikan" (media cetak, elektronik, langsung).

**Lampiran I — Bab IV Perekayasaan.** Pemasangan wajib "melakukan uji coba pengoperasian APILL dan kelengkapannya"; pemeliharaan meliputi "memantau keberadaan dan kinerja perlengkapan jalan" dan "mengoperasikan perlengkapan jalan dengan baik sesuai ketentuan teknis". Pemasangan pada semua status jalan harus mendapat persetujuan tertulis Ditjen Hubdat/SKPD LLAJ sesuai kewenangan.

**Lampiran I — Bab VI Pengawasan (monev).** Penilaian = "pemantauan terhadap efektivitas pelaksanaan kebijakan ... melalui penilaian tingkat pelayanan setelah diterapkan kebijakan" dan "analisis ... dengan membandingkan tingkat pelayanan sebelum diterapkan kebijakan dengan tingkat pelayanan setelah diterapkan kebijakan." Tindakan korektif: penyempurnaan atau pencabutan kebijakan.

**Lampiran II — Tata cara (yang menyentuh ITCS).**
- A. Prioritas angkutan massal: "penyediaan fasilitas bus priority pada persimpangan yang dilengkapi APILL" dan "sistem informasi angkutan umum".
- C. Disabilitas: APILL dilengkapi isyarat suara/tanda universal.
- D. Pemisahan berdasarkan aksesibilitas: "pemberian waktu hijau khusus pada APILL untuk angkutan umum" dan "untuk pejalan kaki".
- F. Pengendalian simpang — 9 teknik: prioritas; ber-APILL; APILL + belok kiri langsung; **APILL otonom adaptif**; **Sistem APILL Terkoordinasi (ATCS)**; bundaran; **ITS**; kotak kuning; RHK sepeda motor.
  - Kriteria simpang ber-APILL (minimal): volume masuk rata-rata >750 kend/jam selama 8 jam; delay rata-rata >30 detik; pejalan kaki menyeberang >175/jam selama 8 jam/hari; kecelakaan >5/tahun. Kelengkapan minimal: APILL, marka, rambu peringatan; dapat DIS.
  - Belok kiri langsung: >40 gerakan belok kiri per periode sibuk; lajur khusus.
  - **APILL otonom adaptif**: pada simpang "dengan volume antara kaki simpang sangat bervariasi" dan/atau yang tidak memungkinkan ATCS; **minimal APILL, marka, rambu peringatan, dan alat pendeteksi kendaraan**.
  - **ATCS** ("Sistem APILL terkoordinasi atau dikenal dengan Area Traffic Control System (ATCS) merupakan pengendalian lalu lintas antar simpang ber APILL yang saling terkoordinasi"): syarat minimal **≥3 simpang** dan **jarak antar simpang ≤1 km**; kelengkapan minimal: **APILL, marka, rambu, alat pendeteksi kendaraan, jaringan komunikasi kabel dan/atau nirkabel, serta ruang pusat kendali (Control Centre Room)**; dapat dilengkapi kamera pemantau, DIS, VMS, alat pendeteksi angkutan umum massal, **fase khusus bus priority**, alat pemantau kecepatan dan volume.
  - **ITS** ("pengendalian simpang dengan memanfaatkan TIK ... Intelligent Transportation System"): pada simpang yang telah ber-ATCS dan pada kota sedang/besar/metropolitan; minimal "alat pemantau/pendeteksi kecepatan dan volume kendaraan serta media informasi lalu lintas untuk pengguna jalan."
  - Kotak kuning: hanya pada simpang APILL adaptif/ATCS dan LOS simpang ≥C.
- G. Pengendalian ruas: tidal flow (V/C salah satu arah >0,9; distribusi ≥70:30), SSA (V/C >0,85), HOV, pembatasan parkir (V/C >0,7; kecepatan jam puncak <30 km/jam), pembatasan kecepatan, u-turn (V/C <0,65), **ITS ruas** (detektor, kamera pengendali, VMS, alat pendeteksi kecepatan/volume; "dapat menjadi bagian dari Sistem APILL Terkoordinasi (ATCS) maupun berdiri sendiri"), perlintasan KA (APILL/VMS dapat bagian ATCS).
- H. Lingkungan: APILL tenaga surya; pembatasan kendaraan berdasarkan emisi gas buang.

**Lampiran III — Persetujuan MRLL jalan nasional di DKI.** Gubernur DKI mengajukan ke Dirjen dengan data dukung minimal: peta ruas; **"kajian kinerja lalu lintas dengan melampirkan sekurang-kurangnya indikator kecepatan rata-rata dan nisbah antara volume dan kapasitas"**; tata letak perlengkapan jalan; arah arus; dampak terhadap jaringan sekitar. Dirjen menerbitkan persetujuan/penolakan ≤60 hari kerja; pelapor wajib laporan ≥1×/tahun; Dirjen evaluasi ≥1×/tahun; persetujuan dapat dicabut jika ada penyimpangan prinsip.

### A.4 Permenhub PM 49 Tahun 2014 tentang Alat Pemberi Isyarat Lalu Lintas

**Identitas.** Ditetapkan 25 September 2014, diundangkan 26 September 2014; melaksanakan Pasal 56–57 PP 79/2013; mencabut KM 62/1993. 8 Bab, 48 pasal (*rekonstruksi*), Lampiran I (gambar spesifikasi), Lampiran II (gambar penempatan). Rincian teknis lengkap ada di Bagian B.

**Kewenangan (Pasal 28, *rekonstruksi*).** Penyelenggaraan APILL (penempatan & pemasangan, pemeliharaan, penghapusan — Pasal 27) dilakukan oleh: Dirjen (jalan nasional), **gubernur (jalan provinsi)**, bupati, walikota; jalan tol oleh BUJT setelah penetapan Dirjen. Perpotongan jalan nasional dengan jalan provinsi/kabupaten/kota → **Dirjen**; perpotongan jalan provinsi dengan jalan kabupaten/kota → gubernur. Implikasi: simpang di Jakarta yang melibatkan jalan nasional secara formal berada di bawah Dirjen Hubdat (lihat PM 96/2015 Pasal 5 ayat (2) untuk mekanisme persetujuan).

### A.5 Permenhub PM 76 Tahun 2021 tentang Sistem Manajemen Transportasi Cerdas di Bidang LLAJ (BN 2021/1009, 17 hlm)

**Hanya abstrak yang tersedia.** Isi abstrak: tujuan "meningkatkan pelayanan transportasi jalan yang berkualitas, nyaman, aman, informatif, dan ramah lingkungan, perlu membangun sistem manajemen transportasi cerdas"; dasar hukum: UU 39/2008, UU 22/2009, PP 32/2011, Perpres 40/2015, Perpres 103/2015, PM 110/2018, PM 67/2021; ruang lingkup: **"jenis, fungsi, dan prinsip kerja Sistem Manajemen Transportasi Cerdas, penyelenggaraan Sistem Manajemen Transportasi Cerdas, dan pembinaan dan pengawasan"**; ditetapkan 27 Agustus 2021, berlaku 6 September 2021. **Definisi, komponen ITS, pusat kendali, standar interoperabilitas, integrasi data, dan kewajiban pemda tidak dapat dikutip** karena batang tubuh tidak ada dalam korpus. Tindak lanjut: peroleh salinan lengkap (BN 2021/1009) sebelum menyusun matriks kepatuhan final.

### A.6 Perda DKI Jakarta No. 5 Tahun 2014 tentang Transportasi

**Struktur.** 16 Bab, ±262 pasal. Bab II Rencana Induk Transportasi (Pasal 6–11); Bab III Transportasi Jalan, Bagian Keempat Lalu Lintas Jalan: Paragraf 1 MRLL (Pasal 67–76), Paragraf 2 Andalalin (77), Paragraf 3 Manajemen Kebutuhan Lalu Lintas dan Pencegahan Kemacetan (78–87), Paragraf 4 Tata Tertib (88–); Pasal 95 penindakan PPNS; Bab VII Sistem Informasi Transportasi (232–235); Bab VIII Pembinaan (236–237); Bab X Kerjasama (239); Bab XIV Sanksi Administratif (246); Bab XV Pidana (247–260). Konsiderans mencantumkan UU ITE (UU 11/2008) sebagai dasar.

**Definisi.** Pasal 1 angka 7: "Dinas adalah SKPD yang membidangi urusan perhubungan dan Transportasi"; angka 29 MRLL; angka 34 APILL (identik UU).

**Target (Pasal 8).** "(1) ... ditetapkan target: a. 60% (enam puluh persen) perjalanan penduduk menggunakan sarana Kendaraan Bermotor Umum dan kecepatan rata-rata jaringan Jalan 35 (tiga puluh lima) km/jam untuk Transportasi Jalan". Ayat (2): semua kebijakan sektor transportasi "harus mengutamakan dan memprioritaskan penggunaan sarana Kendaraan Bermotor umum massal." Pasal 9: dicapai bertahap melalui Renstra 5 tahunan; Pasal 10: RIT dievaluasi tiap 5 tahun. Pasal 7 huruf l: RIT memuat "rencana kawasan pembatasan Lalu Lintas."

**MRLL (Pasal 67–75).** Pasal 67 (tujuan & 8 cara, termasuk pengendalian pada persimpangan/ruas); Pasal 69 perencanaan (identik UU Pasal 94); **Pasal 70 ayat (2)**: dalam pelaksanaan kebijakan Pemerintah Daerah menyiapkan lajur sepeda, lajur/jalur khusus angkutan massal, dan **"prioritas di persimpangan untuk Kendaraan Bermotor Umum"**; ayat (3) informasi kepada masyarakat. Pasal 71 huruf c: "optimalisasi operasional rekayasa Lalu Lintas dalam rangka meningkatkan ketertiban, kelancaran, dan efektivitas penegakan hukum." Pasal 73: pengawasan termasuk "tindakan penegakan hukum." **Pasal 74**: "Setiap orang/pengguna Jalan tanpa izin dari Kepala Dinas dilarang: a. membuat, memasang, memindahkan Rambu Jalan, Marka Jalan, Alat Pemberi Isyarat Lalu Lintas, dan fasilitas pendukung; ... i. membuat dan/atau memasang sesuatu yang menyerupai ... Alat Pemberi Isyarat Lalu Lintas". Pasal 75: rincian MRLL diatur Pergub.

**Manajemen kebutuhan lalu lintas & ERP (Pasal 78–86).**
- Pasal 78 ayat (1): kriteria ditambah "keselamatan Lalu Lintas". Ayat (2): 14 cara pembatasan, antara lain (a) sistem satu arah; (b) stiker lisensi kawasan; **(c) "sistem pengendalian Lalu Lintas Jalan berbayar pada jaringan Jalan tertentu dan/atau kawasan tertentu dan/atau waktu tertentu"**; (h) pembatasan sepeda motor; (i) pajak progresif; (k) kuota STNK per tahun sesuai kapasitas jalan; (l) pengendalian kendaraan luar daerah; (n) metode lainnya. Ayat (3) Pergub.
- Pasal 79: ERP untuk peningkatan kinerja lalu lintas dan pelayanan angkutan umum; objek: penggunaan ruas/koridor/kawasan pada waktu tertentu oleh kendaraan perseorangan atau barang.
- **Pasal 80 ayat (1)** kriteria: 2 jalur × ≥2 lajur; angkutan massal SPM; V/C ≥0,9 jam puncak; dan/atau kecepatan rata-rata jam puncak ≤10 km/jam. **Ayat (2)** ruas ERP: "Jalan Sisingamangaraja, Jalan Sudirman, Jalan MH. Thamrin, Jalan Medan Merdeka Barat, Jalan Majapahit, Jalan Gajah Mada, Jalan Hayam Wuruk, Jalan Gatot Soebroto, dan Jalan Rasuna Said"; ayat (3) dapat dikembangkan dengan Pergub; **ayat (4)** "dimulai Pukul 07.00 WIB sampai dengan Pukul 20.00 WIB pada hari kerja."
- **Pasal 81 ayat (2): "Efektivitas pengendalian Lalu Lintas ... diukur berdasarkan peningkatan kecepatan rata-rata perjalanan."** Ayat (4): tarif berprinsip keadilan "memperhitungkan jarak perjalanan dan kondisi arus Lalu Lintas" (tarif dinamis dimungkinkan).
- Pasal 82: dilaksanakan Dinas, dapat bekerja sama dengan BUMD; diawasi Dewan Pengawas (masyarakat, pemda, asosiasi profesi, perguruan tinggi, LSM, instansi terkait).
- Pasal 83–84: dana ERP untuk biaya penyelenggaraan, sisanya untuk angkutan massal dan kinerja lalu lintas, termasuk (84 ayat (2) c) "pemeliharaan dan pengembangan teknologi untuk kepentingan Lalu Lintas dan peningkatan kualitas SDM"; (84 ayat (1) c) "penerapan dan pengembangan teknologi informasi untuk kepentingan pelayanan Angkutan umum massal."
- Pasal 85: Pemerintah Daerah "penyediaan sistem dan peralatan yang diperlukan untuk menerapkan pembatasan."
- Pasal 86: pengemudi dilarang menghambat kelancaran; penanggung jawab kegiatan wajib mencegah kemacetan.

**Penindakan oleh PPNS Dinas (Pasal 95).** Pemda dapat menindak pelanggaran tertentu via PPNS Dinas: memasuki jalur busway; parkir di rumija bukan fasilitas parkir; menyalahgunakan fasilitas pejalan kaki; **"melanggar ketentuan pada kawasan pengendalian Lalu Lintas"**; CFD; menaikkan/menurunkan penumpang bukan di halte; kendaraan bermotor di lajur sepeda; kewajiban pengemudi KBU; laik jalan KBU. (Pelanggaran APILL/rambu umum **tidak** termasuk — tetap ranah Polri berdasarkan UU.)

**Sistem Informasi Transportasi (Pasal 232–235).** Pasal 232: Pemda menyediakan sistem informasi transportasi (data prasarana, sarana, pengelolaan); Pasal 233: "harus dapat diakses dan digunakan oleh masyarakat"; Pasal 234: dapat digunakan untuk penegakan hukum (penyelidikan/penyidikan; penanganan kecelakaan/pelanggaran/kemacetan oleh Polri; pengejaran/penindakan); Pasal 235: Pergub. Pasal 237: Kepala Dinas menilai kinerja penyelenggaraan transportasi tiap 1 tahun. Pasal 239: kerja sama dengan daerah lain/badan hukum melalui perjanjian.

**Sanksi.** Pasal 246 sanksi administratif (teguran, denda administratif, pembekuan/pencabutan izin); Pasal 253: masuk jalur busway kurungan ≤2 bulan/denda ≤Rp50 juta; Pasal 260: larangan lain mengikuti UU LLAJ.

### A.7 Pergub DKI Jakarta No. 68 Tahun 2021 tentang Penyelenggaraan Sistem Transportasi Terpadu dan Terintegrasi (BD 2021/62026)

**Struktur.** 8 Bab, 17 pasal + Lampiran (petunjuk logo Jak Lingko). Ditetapkan 26 Agustus 2021. Melaksanakan Pasal 11 ayat (1) dan Pasal 78 ayat (2) Perda 5/2014.

**Definisi.** Pasal 1 angka 3: Sistem Jak Lingko = sistem terpadu pendukung "peningkatan penggunaan angkutan umum massal dan pembatasan kendaraan bermotor perseorangan"; angka 4: **"Interoperabilitas adalah kemampuan data untuk dibagipakaikan antar sistem elektronik yang saling berinteraksi"**; angka 5 Interkoneksi (antar jaringan telekomunikasi).

**Penyelenggara & kerja sama.** Pasal 5: dilakukan Dinas Perhubungan; BUMD/badan usaha dapat menjadi penyelenggara (wajib logo). Pasal 7: perencanaan oleh Dishub, ditetapkan Keputusan Gubernur, dapat dikerjasamakan dengan memperhatikan pelayanan, efektivitas-efisiensi, analisis biaya-manfaat, kesesuaian regulasi. Pasal 9: pembangunan/pengelolaan oleh Dishub/Perangkat Daerah; BUMD/badan usaha mengajukan permohonan ke Gubernur disertai kajian & proposal, diverifikasi Kepala Dishub.

**Integrasi data (Pasal 10–11) — sangat relevan untuk ITCS.**
- Pasal 10 ayat (1): integrasi sistem operasional meliputi jadwal, rute, sistem pembayaran, dan **"data dan informasi"**. Ayat (4) c: sistem pembayaran wajib memenuhi "Interoperabilitas dan Interkoneksi".
- Ayat (5): Dishub/BUMD/badan usaha "membangun dan/atau mengembangkan sistem integrasi data dan informasi."
- Ayat (6): sistem minimal mengelola 18 jenis data: sarana siap operasi & realisasinya; kesiapan prasarana; capaian km; frekuensi; jumlah penumpang per layanan; naik/turun; perpindahan antar moda; **"keberadaan aktual armada operasi"**; **"waktu tempuh"**; **"headway"**; jadwal; asal-tujuan; **"data kecelakaan dan pelanggaran"**; aduan masyarakat; sistem informasi penumpang; perubahan rencana operasi; publikasi layanan.
- **Ayat (7): "Dinas perhubungan, BUMD dan/atau badan usaha yang berbadan hukum bertanggung jawab untuk menjamin kerahasiaan dan keamanan data dan informasi."**
- Pasal 11 ayat (1): sistem integrasi data "harus terintegrasi dengan sistem informasi Pemerintah Provinsi DKI Jakarta"; ayat (4) **data yang sudah terintegrasi "merupakan milik Pemerintah Provinsi DKI Jakarta"**; ayat (5) dapat diakses "secara online dan realtime oleh pihak lain yang terkait berdasarkan persetujuan Gubernur atau pejabat yang ditunjuk."

**Pembatasan kendaraan perseorangan (Pasal 13).** Meliputi: rekayasa lalu lintas; **jalan berbayar elektronik**; pembatasan lalu lintas; pajak progresif; parkir; **ganjil-genap** ("plat nomor ganjil dan genap"); kendaraan ramah lingkungan; bentuk lain. Ayat (2) dilakukan Dishub; ayat (3) ERP, parkir, dan bentuk lain dapat dikerjasamakan dengan BUMD/badan usaha; **ayat (4) "Data dan informasi terkait pembatasan ... harus terintegrasi ke dalam sistem Pemerintah Provinsi DKI Jakarta."**

**Monev (Pasal 15).** Kepala Dishub memantau periodik; indikator: laik operasi, jumlah pengguna, frekuensi, kondisi prasarana/sarana, load factor, pendapatan/biaya, lintasan, km operasi, SPM; laporan ke Gubernur tiap 3 bulan; BUMD lapor bulanan. Pasal 16: penyesuaian ≤1 tahun.

### A.8 Perpres No. 55 Tahun 2018 tentang Rencana Induk Transportasi Jabodetabek 2018–2029

**Batang tubuh (14 pasal).** Pasal 1: berlaku 2018–2029. Pasal 3: RIT Jabodetabek "merupakan pedoman bagi Pemerintah Pusat dan Pemerintah Daerah" termasuk Pemprov DKI. Pasal 4: tahap I 2018–2019, tahap II 2020–2024, tahap III 2025–2029; setiap K/L dan Pemda "harus menyusun rencana aksi" (waktu, pendanaan, mekanisme) berkoordinasi dengan BPTJ. Pasal 5 ayat (3): Menhub dapat memfasilitasi teknis/pembiayaan untuk antara lain "pelaksanaan manajemen permintaan lalu lintas." Pasal 13: evaluasi 1× per 5 tahun (dapat lebih sering bila ada perubahan teknologi transportasi).

**Lampiran — target 2029 (bagian II, sebagaimana terbaca).** (1) pergerakan orang dengan angkutan umum perkotaan **60%**; (2) waktu perjalanan rata-rata dalam angkutan umum **1 jam 30 menit** pada jam puncak asal–tujuan; (3) kecepatan rata-rata di seluruh jaringan jalan pada jam puncak **minimum 30 km/jam** (baris OCR rusak, angka "30 kilometer/jam" terbaca); (4) cakupan layanan angkutan umum 80% panjang jalan; (5) akses jalan kaki ≤500 m; (6) jaringan feeder terintegrasi; (7) simpul dengan park and ride, perpindahan ≤500 m; (8) perpindahan moda ≤3 kali. Sembilan pilar kebijakan; pilar 6 = **Peningkatan Kinerja Lalu Lintas**.

**Lampiran — Kebijakan 6 Peningkatan Kinerja Lalu Lintas (hlm. 65).** Strategi: (a) MRLL jalan nasional Jabodetabek: perbaikan bottleneck, MRLL kawasan pasar, perbaikan geometrik, perlengkapan jalan, **"Penerapan Electronic Law Enforcement (ELE)"**; (b) manajemen permintaan "Push and Pull": **"Penerapan Electronic Road Pricing (ERP) dan Pengaturan Penggunaan Sepeda Motor"**, MRLL kawasan CBD, **"Penerapan Sistem Prioritas Bus di persimpangan"** (Tabel 6: persimpangan di Jakarta yang dilalui BRT/Transjabodetabek — Pemerintah Daerah), ETC, parkir meter elektronik, pengawasan angkutan barang; (c) **"Penerapan teknologi sistem informasi untuk kepentingan lalu lintas dan angkutan (pengaturan dan pengawasan) secara real time"**: peningkatan sistem informasi lalu lintas di jalan arteri (Tabel 6: ruas Thamrin–Sudirman–Rasuna Said; Gatot Subroto–Medan Merdeka Barat; Hayam Wuruk–Gajah Mada–Majapahit–Sisingamangaraja), **"Pembangunan dan Pengembangan ATCS (Area Traffic Control System)"** untuk DKI Jakarta dan 8 kota/kabupaten lainnya (penanggung jawab Kemenhub/Pemerintah Daerah), pengadaan & pemeliharaan CCTV di jalan arteri. Kebijakan 5 (transportasi terintegrasi) memuat "Pengembangan Sistem Informasi Terpadu" (masterplan, FS, DED oleh Kemenhub; sistem informasi di jalan tol dan arteri oleh PUPR).

### A.9 PKJI 2023 (Pedoman Kapasitas Jalan Indonesia, 09/P/BM/2023) — Bab 5 Kapasitas Simpang APILL
Dibahas lengkap di Bagian D.

### A.10 MKJI 1997 — Bab 2 Simpang Bersinyal
Dibahas sebagai pembanding di Bagian D.5.

### A.11 KepKa LAN No. 1/2023 dan Modul Proyek Perubahan PKN II
Dibahas di Bagian F.

---

## B. Spesifikasi teknis APILL menurut PM 49/2014 (nomor pasal *rekonstruksi*)

**Jenis dan fungsi (Bab II).**
- Pasal 3: APILL terdiri atas lampu tiga warna, dua warna, satu warna.
- Pasal 4: APILL berupa **otonom** ("pengaturan waktu siklusnya hanya dapat dilakukan oleh APILL yang bersangkutan atau berdiri sendiri") dan **terkoordinasi** ("pengaturan waktu siklusnya terkoordinasi dan berinteraksi dengan APILL yang dipasang pada lokasi lain").
- Pasal 6 (tiga warna, untuk kendaraan): merah = berhenti dan tidak boleh melewati garis henti; kuning setelah hijau = merah akan menyala, bersiap berhenti; **kuning bersama merah = hijau akan segera menyala, bersiap bergerak** (jadi fase merah+kuning diakui); hijau = berjalan.
- Pasal 7 (susunan): vertikal atas→bawah merah, kuning, hijau; atau horizontal dari sudut pandang pengguna jalan kanan→kiri merah, kuning, hijau.
- Pasal 8–9 (dua warna, kendaraan dan/atau pejalan kaki): merah & hijau; vertikal merah di atas, hijau di bawah.
- Pasal 10 (satu warna, peringatan bahaya): kuning kelap-kelip = berhati-hati; merah = berhenti (perlintasan KA).

**Waktu siklus (Pasal 11–18).**
- Pasal 11: waktu siklus **terkoordinasi** dan **tidak terkoordinasi**.
- Pasal 12: "Waktu siklus terkoordinasi ... berupa skema rencana siklus antar APILL diatur oleh sistem yang terpusat." (Dasar normatif ATCS/ITCS terpusat.)
- Pasal 13: tidak terkoordinasi terdiri atas siklus tetap, semi-adaptif, adaptif.
- Pasal 14: siklus tetap "paling sedikit memiliki 8 (delapan) rencana siklus."
- Pasal 15: semi-adaptif = rencana siklus tetap pada kaki simpang mayor (≥8 rencana siklus) dan bervariasi pada kaki minor.
- Pasal 16: adaptif = "rencana siklus yang bervariasi pada kaki simpang mayor dan kaki simpang minor menurut situasi arus lalu lintas."
- Pasal 17: penentuan waktu siklus mempertimbangkan aspek **makroskopis** (volume menuju & meninggalkan kaki simpang; kapasitas pendekat; komposisi kendaraan dan pejalan kaki; variasi periodik & insidentil; distribusi arah; tundaan dan antrian; kecepatan; pengaturan arus) dan **mikroskopis** (tundaan; konflik; percepatan).
- Pasal 18: "Tata cara penentuan waktu siklus APILL ... ditetapkan oleh Direktur Jenderal."
- **Tidak ditemukan** dalam PM 49/2014: durasi minimum hijau, durasi kuning, durasi merah semua (all-red), waktu hijau pejalan kaki, waktu kedip (flashing). Nilai praktis diambil dari PKJI 2023 (kuning 3,0 detik; wAH normal 4/5/6 detik; hijau awal/akhir minimal 10 detik; siklus 40–130 detik) — lihat Bagian D.

**Komponen utama dan spesifikasi (Bab III, Pasal 19–26).**
- Pasal 19: luminer, tiang penyangga, pondasi, **perangkat kendali**, kabel instalasi.
- Pasal 20: luminer = lampu, armatur, catu daya. Lampu "koefisien iluminasi paling sedikit 30 (tiga puluh) milicandela per meter persegi dan paling besar 90 (sembilan puluh) milicandela per meter persegi" (satuan sebagaimana tercetak). Komponen optis bulat diameter 20–30 cm; dapat menampilkan piktogram **panah, pejalan kaki, bus, dan/atau sepeda**. **Catu daya: "sumber tenaga dari jaringan listrik setempat atau dengan menggunakan baterai."**
- Pasal 21: armatur wajib berstiker logo perhubungan, diterbitkan Dirjen/gubernur/bupati/walikota sesuai kewenangan.
- Pasal 22: tiang lurus, lengkung, siku, gantry. Pasal 23: pondasi cast in situ / back casting.
- **Pasal 24 (perangkat kendali/controller):** komponen elektronika aktif & pasif; PCB & elektronika penuh; rangka dengan **ketahanan suhu 5–70 °C dan kelembapan nisbi maksimum 95%**.
- **Pasal 25:** APILL dapat dipasangi **alat pendeteksi kendaraan, kamera, Display Information System (DIS)** (iluminasi 30–70 mcd/m²), dan **"peralatan teknologi informasi untuk kepentingan lalu lintas"** yang **"harus memiliki sertifikasi sesuai dengan ketentuan peraturan perundang-undangan."**
- Pasal 26: gambar spesifikasi di Lampiran I.

**Penempatan dan pemasangan (Pasal 29–40).**
- Pasal 29: memperhatikan geometrik, tata guna lahan, jaringan, arus, konstruksi jalan, tanah; harus pada ruang manfaat jalan; dapat bersama rambu & marka.
- Pasal 31 (simpang): di sebelah kiri jalur menghadap arus; dapat ditambah di kanan; jarak ≥60 cm dari bagian terluar armatur ke tepi luar bahu jalan.
- Pasal 32 (ruas): pada pemisah jalur/median; jarak ≥30 cm.
- Pasal 33 (dua warna): di penyeberangan pejalan kaki/pesepeda, sisi kiri, **dilengkapi tombol untuk menyeberang** (pelican); jarak ≥60 cm.
- Pasal 34 (satu warna): sebelum lokasi bahaya; merah sebelum perlintasan KA.
- Pasal 35 (tinggi): tiga warna ≥300 cm (dari permukaan jalan tertinggi ke sisi bawah armatur); dua warna 175–265 cm; satu warna ≥300 cm; di atas rumaja ≥500 cm; rotasi armatur ≤5° dari tegak lurus sumbu jalan.
- Pasal 37: satu tiang maksimum 3 armatur. Pasal 38: bangunan/utilitas/iklan/pohon dilarang menghalangi APILL. Pasal 39: bila tak ada ruang, dapat dipasang pada tembok, kaki jembatan, jembatan layang, tiang utilitas. Pasal 40: tata cara pemasangan oleh Dirjen.

**Pemeliharaan (Pasal 41).** Berkala **"paling sedikit setiap 6 (enam) bulan"**, mempertimbangkan umur teknis komponen, "perkembangan teknologi dan inovasi bidang transportasi dan telematika", rencana pengaturan lalu lintas; meliputi pembersihan penghalang & optik, korosi, pengecatan. **Insidentil**: penggantian komponen rusak mendadak; **"penyesuaian waktu siklus dengan situasi arus lalu lintas aktual"**; penyesuaian letak komponen yang bergeser.

**Penghapusan (Pasal 42).** Berdasarkan umur teknis (**paling lama 5 tahun**), kebijakan pengaturan, keberadaan fisik (rusak/hilang); "dilakukan berdasarkan penilaian kinerja oleh Pejabat"; tata cara penilaian kinerja oleh Dirjen.

**Pembuatan (Pasal 43).** Oleh badan usaha yang memenuhi syarat bahan/peralatan & SDM kompeten, dinilai dan didaftar di Ditjen Hubdat.

**Peralihan & lain-lain.** Pasal 44: APILL lama wajib menyesuaikan ≤2 tahun. Pasal 45: pembinaan & pengawasan teknis Dirjen.

**Tidak ditemukan dalam teks:** ketentuan "tanda rusak"/mode kedip saat gangguan, standar komunikasi/protokol, spesifikasi detektor, ketentuan log/rekaman operasi, mode manual/police panel. Ketentuan "APILL tidak berfungsi" hanya muncul di PP 32/2011 Pasal 34 huruf b sebagai pemicu optimalisasi operasional oleh Polri.

---

## C. Kerangka ITS menurut PM 76/2021 — status: tidak dapat dikaji

> **ERRATUM (2026-09-12, koordinator):** bagian ini ditulis saat file PM 76/2021 masih berupa abstrak 1 halaman. Teks lengkap (17 hlm.) telah diunduh dari BPK dan dibaca; kajian pasal per pasal ada di **R00 §C** dan `docs/kb/03_Peta_Regulasi_Kepatuhan.md` §A.6. Perpol 8/2023 & 2/2025 (ETLE), UU 27/2022 (PDP) dan Pergub ganjil-genap juga tidak tercakup di R05 ini — lihat KB-03 §A.9, A.11, A.11b. Matriks C-01…C-35 di §G.1 tetap kanonis; C-36…C-43 ditambahkan di KB-03 §B.

Sebagaimana dijelaskan di A.5, hanya abstrak yang tersedia. Yang dapat dipastikan dari abstrak: (1) nama resmi objek pengaturan adalah **"Sistem Manajemen Transportasi Cerdas"** (SMTC), bukan "ITS"; (2) ruang lingkup: jenis, fungsi, prinsip kerja; penyelenggaraan; pembinaan dan pengawasan; (3) berdasar pada PP 32/2011 dan PM 67/2021 (yang terakhir tidak ada dalam korpus). Sebagai pengganti sementara, kerangka ITS yang berlaku dan dapat dikutip berasal dari PM 96/2015 Lampiran II F.e (ATCS) dan F.g (ITS), UU 22/2009 Pasal 245–251 (pusat kendali), serta Pergub 68/2021 Pasal 10–11 (integrasi & interoperabilitas data). Rekomendasi: dapatkan teks lengkap PM 76/2021 dan PM 67/2021 sebelum finalisasi arsitektur.

---

## D. Rumus kinerja Simpang APILL menurut PKJI 2023 (Bab 5, hlm. 102–128; Lampiran 12, hlm. 256–280)

### D.1 Notasi dan satuan
| Simbol | Arti | Satuan |
|---|---|---|
| q | arus lalu lintas pendekat | SMP/jam |
| J0 | arus jenuh dasar | SMP/jam (hijau) |
| J | arus jenuh terkoreksi | SMP/jam |
| C | kapasitas pendekat | SMP/jam |
| s | waktu siklus | detik |
| wH | waktu hijau | detik |
| wK | waktu kuning | detik |
| wMS | waktu merah semua (all-red) | detik |
| wAH | waktu antar hijau (= wK + wMS) | detik |
| wHH | waktu hijau hilang total per siklus | detik |
| RH | rasio hijau = wH/s | – |
| Rq/J | rasio arus terhadap arus jenuh | – |
| RAS | rasio arus simpang = Σ (Rq/J kritis) | – |
| RF | rasio fase | – |
| DJ | derajat kejenuhan | – |
| Nq, Nq1, Nq2 | antrian rata-rata awal hijau; sisa; datang saat merah | SMP |
| PA | panjang antrian | m |
| RKH | rasio kendaraan terhenti | – |
| NKH | jumlah kendaraan terhenti | SMP/jam |
| T, TLL, TG | tundaan rata-rata, tundaan lalu lintas, tundaan geometri | detik/SMP |
| LE, L, LM, LK, LBKiJT | lebar efektif, lebar pendekat hulu, lebar masuk, lebar keluar, lebar lajur belok kiri jalan terus | m |
| RBKa, RBKi, RKTB | rasio belok kanan, belok kiri, kendaraan tak bermotor | – |

Tipe pendekat: **P (terlindung)** — tanpa konflik belok kanan dengan arus lawan; **O (terlawan)**.

### D.2 Rumus kapasitas dan waktu isyarat
1. **Kapasitas (Pers. 5-1):** C = J × wH / s.
2. **Lebar efektif (Pers. 5-2, 5-3):** jika LBKiJT ≥2 m atau lajur eksklusif: keluarkan qBKiJT, LE = min{L − LBKiJT ; LM}; periksa untuk tipe P: jika LK < LM × (1 − RBKa) maka LE = LK (analisis hanya arus lurus). Jika LBKiJT <2 m: sertakan qBKiJT, LE = min{L ; LM + LBKiJT ; L × (1 + RBKiJT) − LBKiJT}; periksa LK < LM × (1 − RBKa − RBKiJT) → LE = LK.
3. **Arus jenuh dasar tipe P (Pers. 5-6):** J0 = 600 × LE (SMP/jam). Tipe O: dari Gambar 12-2 s.d. 12-9 sebagai fungsi LE, qBKa, qBKa,O (interpolasi). Koreksi arus >250 SMP/jam: tanpa lajur BKa terpisah, jika qBKa,O >250 dan qBKa <250: J = J(BKa,O=250) − (qBKa,O − 250) × 8; jika keduanya >250: J = J(250,250) − (qBKa,O + qBKa − 500) × 2. Gerakan belok kanan >250 SMP/jam → pertimbangkan fase terlindung.
4. **Arus jenuh terkoreksi (Pers. 5-4):** J = J0 × FHS × FUK × FG × FP × FBKi × FBKa.
   - FUK (Tabel 12-1): >3,0 juta jiwa = **1,05** (berlaku untuk Jakarta); 1,0–3,0 = 1,00; 0,5–1,0 = 0,94; 0,1–0,5 = 0,83; <0,1 = 0,82.
   - FHS (Tabel 12-3), fungsi tipe lingkungan (KOM/KIM/AT), hambatan samping (tinggi/sedang/rendah), tipe fase (terlawan/terlindung), rasio kendaraan tak bermotor 0,00–0,25. Contoh KOM–tinggi–terlindung: 0,93; 0,91; 0,88; 0,87; 0,85; 0,81. KOM–tinggi–terlawan: 0,93; 0,88; 0,84; 0,79; 0,74; 0,70. AT: terlawan 1,00; 0,95; 0,90; 0,85; 0,80; 0,75; terlindung 1,00; 0,98; 0,95; 0,93; 0,90; 0,88. Jika hambatan samping tidak diketahui, anggap **tinggi**.
   - FG: Gambar 12-10 fungsi kelandaian (+ menanjak, − menurun).
   - FP (Pers. 5-5): FP = [Lp/3 − (L − 2) × (Lp/3 − wH)/L] / wH, dengan Lp jarak garis henti ke kendaraan parkir pertama (m), L lebar pendekat (m), wH waktu hijau (nilai normal 27 detik). Tidak diterapkan bila LE ditentukan oleh LK.
   - FBKa (Pers. 5-27): FBKa = 1,0 + RBKa × 0,26 — hanya tipe P, tanpa median, dua arah, LE oleh LM.
   - FBKi (Pers. 5-28): FBKi = 1,0 − RBKi × 0,16 — hanya tipe P tanpa BKiJT, LE oleh LM.
5. **Arus jenuh gabungan dua fase (Pers. 5-7):** J1+2 = (J1 × wH1 + J2 × wH2) / (wH1 + wH2); hijau awal/akhir disarankan 1/4–1/3 total hijau, **minimal 10 detik**.
6. **Rasio arus (Pers. 5-8):** Rq/J = q / J. Rasio arus simpang (Pers. 5-29): RAS = Σi (Rq/J kritis)i. Rasio fase (Pers. 5-30): RF = Rq/J kritis / RAS.
7. **Waktu merah semua (Pers. 5-9):** wMS = max{ (LKBR + PKBR)/vKBR − LKDT/vKDT ; LPK/vPK }, dengan nilai default vKDT = vKBR = 10 m/det (kendaraan bermotor), 3 m/det (kendaraan tak bermotor), 1,2 m/det (pejalan kaki); PKBR = 5 m (MP/KS), 2 m (SM/KTB). Nilai normal wAH (Tabel 5-1): simpang kecil (lebar 6–<10 m) 4 detik/fase; sedang (10–<15 m) 5; besar (≥15 m) 6.
8. **Waktu hijau hilang (Pers. 5-10):** wHH = Σ (wMS + wK)i. **"Panjang waktu kuning pada APILL di kota-kota Indonesia biasanya ditetapkan 3,0 detik."**
9. **Waktu siklus Webster (Pers. 5-11):** s = (1,5 × wHH + 5) / (1 − RAS). Siklus layak (Tabel 12-2): 2 fase 40–80 detik; 3 fase 50–100; 4 fase 80–130. **"Waktu siklus yang melebihi 130 detik harus dihindari."** Jika RAS mendekati/≥1: simpang "melampaui jenuh"; rumus tidak realistik.
10. **Waktu hijau (Pers. 5-12):** wHi = (s − wHH) × (Rq/J kritis)i / Σ(Rq/J kritis). Catatan: kinerja lebih peka terhadap kesalahan pembagian hijau daripada terhadap siklus yang terlalu panjang.

### D.3 Rumus kinerja
11. **Arus jam perencanaan (Pers. 5-13):** qJP = LHRT × K; K perkotaan 7–12%.
12. **EMP (Tabel 5-2):** MP 1,00/1,00; KS 1,30/1,30; **SM 0,15 (terlindung) / 0,40 (terlawan)**. Rasio (Pers. 5-24 s.d. 5-26): RBKi = qBKi/qTotal; RBKa = qBKa/qTotal; RKTB = qKTB/qKB.
13. **Derajat kejenuhan (Pers. 5-14):** DJ = q / C. Kriteria desain umum **DJ ≤ 0,85**; jika DJ >0,85, pengaturan APILL atau geometri perlu ditingkatkan. Bila waktu isyarat benar, DJ hampir sama untuk semua pendekat kritis.
14. **Antrian (Pers. 5-15 s.d. 5-18):** Nq = Nq1 + Nq2. Jika DJ ≤0,5 maka Nq1 = 0; jika DJ >0,5: Nq1 = 0,25 × C × [ (DJ − 1) + √( (DJ − 1)² + 8 × (DJ − 0,5)/C ) ] (catatan: dalam teks PKJI variabel di dalam kurung tercetak "s", tetapi rumus asal MKJI dan dimensi menunjukkan C = kapasitas SMP/jam). Nq2 = s × [(1 − RH)/(1 − RH × DJ)] × q/3600. **PA = Nq × 20 / LM** (m), dengan 20 m² luas rata-rata per SMP. Koreksi overloading: NqMAX dari Gambar 5-9 dengan peluang overloading POL; **perencanaan POL ≤5%; operasional 5–10% dapat diterima**.
15. **Rasio & jumlah kendaraan terhenti (Pers. 5-19, 5-20, 5-31):** RKH = 0,9 × Nq × 3600 / (q × s); NKH = q × RKH (SMP/jam); RKH Total = Σ NKH / qTotal.
16. **Tundaan (Pers. 5-21 s.d. 5-23, 5-32):** Ti = TLLi + TGi. **TLL = s × 0,5 × (1 − RH)² / (1 − RH × DJ) + Nq1 × 3600 / C** (Akcelik). TG = (1 − RKH) × PB × 6 + RKH × 4, PB = porsi kendaraan membelok (nilai normal 6 detik belok tanpa henti, 4 detik berhenti; asumsi 40 km/jam, belok 10 km/jam, 1,5 m/det²). Tundaan simpang: **TI = Σ(q × T) / qTotal**. "Tundaan rata-rata dapat digunakan sebagai indikator tingkat pelayanan." Catatan: hasil tidak berlaku bila kapasitas dipengaruhi faktor luar (blokade hilir, pengaturan manual polisi).

### D.4 Prosedur (Gambar 5-7 evaluasi, 5-8 desain; Formulir SA-I s.d. SA-V)
- **Langkah A (data masukan):** A.1 geometri, pengaturan, lingkungan (SA-I: sketsa fase, L, LBKiJT, LM, LK, median, KOM/KIM/AT, hambatan samping, kelandaian, jarak parkir; kode pendekat U/S/T/B, sub-pendekat U1/U2); A.2 arus per jenis & gerakan LRS/BKa/BKi, konversi SMP, RBKi/RBKa/RKTB (SA-II); A.3 kriteria desain (DJ ≤0,85; batas PA/NKH/T sesuai kebutuhan).
- **Langkah B (penggunaan isyarat):** B.1 fase (awali 2 fase; Gambar 12-21–12-23); B.2 wMS, wAH, wHH (SA-III).
- **Langkah C (waktu isyarat & kapasitas):** C.1 tipe pendekat P/O; C.2 LE; C.3 J0; C.4 enam faktor koreksi; C.5 Rq/J, RAS, RF; C.6 s dan wH; C.7 C (SA-IV). Alternatif fase paling efisien = nilai terendah (RAS + wHH/s).
- **Langkah D (kinerja):** D.1 DJ; D.2 PA (Nq1, Nq2, NqMAX); D.3 RKH, NKH, RKH Total; D.4 TLL, TG, T, tundaan total (T × q), TI (SA-V).
- **Langkah E (perubahan rencana)** bila kriteria tak terpenuhi: pelebaran pendekat (terbaik pada RF kritis); fase terpisah belok kanan (bila tipe O, RBKa tinggi, RF >0,8); pelarangan belok kanan; ulangi B–D hingga DJ ≤0,85.
- **Langkah F (keluaran):** C; atau DJ, PA, NKH, T + deskripsi kinerja; atau desain geometri.
- Pertimbangan tipe simpang: pertahankan DJ ≤0,85; ekonomis (Tabel 12-7, Gambar 12-24); kinerja (Tabel 12-8 perkiraan T rata-rata per tipe); keselamatan (Tabel 12-6: simpang APILL 0,43 laka/10⁶ kend vs simpang 0,60 vs bundaran 0,30); lingkungan: **"Pengaturan isyarat terkoordinasi dan/atau yang teraktualisasi dapat menghasilkan emisi lebih kecil dibandingkan pengaturan isyarat tetap."** Detail teknis (Tabel 12-5) termasuk RHK sepeda motor bila komposisi SM >50% (garis henti mundur ≤20 m), perhentian bus setelah simpang.
- Batasan lingkup: PKJI (seperti MKJI) memodelkan simpang **terisolir dengan kendali waktu tetap**; untuk sistem terkoordinasi/adaptif digunakan sebagai baseline dan evaluator, bukan sebagai algoritme kendali real-time.

### D.5 Perbedaan PKJI 2023 vs MKJI 1997 (Bab 2 Simpang Bersinyal)
| Aspek | MKJI 1997 | PKJI 2023 |
|---|---|---|
| Notasi | S, S0, DS, c, g, LTI, IG, NQ, QL, NS, PSV, D/DT/DG, We, LTOR, FCS/FSF/FG/FP/FRT/FLT, FR/IFR | J, J0, DJ, s, wH, wHH, wAH, Nq, PA, NKH, RKH, T/TLL/TG, LE, BKiJT, FUK/FHS/FG/FP/FBKa/FBKi, Rq/J/RAS |
| Kapasitas | C = S × g/c (Rumus 1) | C = J × wH/s (5-1) — identik |
| Arus jenuh dasar P | S0 = 600 × We (Rumus 4) | J0 = 600 × LE (5-6) — identik |
| emp sepeda motor | 0,2 (terlindung) / 0,4 (terlawan) | **0,15 (terlindung) / 0,40 (terlawan)** |
| FCS/FUK, FSF/FHS, FRT, FLT | tabel & rumus 1+PRT×0,26; 1−PLT×0,16 | nilai identik |
| FP | Fp = [Lp/3 − (WA − 2)(Lp/3 − g)/WA]/g, g normal **26 detik** | sama, wH normal **27 detik** |
| Siklus & hijau | Webster: c = (1,5 LTI + 5)/(1 − ΣFRcrit); gi = (c − LTI) × FRcrit/ΣFRcrit | identik (5-11, 5-12) |
| Antar hijau | normal 4/5/6 detik untuk lebar 6–9 / 10–14 / ≥15 m; kuning 3,0 detik | 4/5/6 detik untuk 6–<10 / 10–<15 / ≥15 m; kuning 3,0 detik |
| Antrian | NQ1, NQ2, QL = NQmax × 20/Wmasuk | identik (5-16, 5-17, 5-18) |
| Angka henti | NS = 0,9 NQ 3600/(Q c); PSV = min(NS, 1) | RKH = 0,9 Nq 3600/(q s) langsung; NKH = q × RKH; tambahan RKH Total; **cap min(…,1) tidak dinyatakan** |
| Tundaan | DT (Akcelik), DG = (1 − PSV) PT 6 + PSV 4 | identik (5-22, 5-23); tambahan TI = Σ(qT)/qTotal |
| Faktor K | tabel 7–12% menurut ukuran kota & jenis jalan | qJP = LHRT × K, K = 7–12% |
| Kriteria desain | DS ≤0,85 (implisit) | DJ ≤0,85 eksplisit; POL 5–10% |
| Tambahan PKJI | – | Tabel 12-8 (perkiraan T per tipe simpang), Tabel 12-6 keselamatan, catatan emisi & koordinasi/aktuasi, RHK |
| Tingkat pelayanan | tidak menetapkan kelas LOS (LOS hanya sebagai istilah) | tidak menetapkan kelas LOS; LOS A–F simpang diambil dari PM 96/2015 |

Kesimpulan: secara metodologis PKJI 2023 adalah pembaruan notasi dan penyajian atas MKJI 1997 dengan model dasar (Webster, Akcelik, model tipe O empiris Indonesia) yang sama; perubahan numerik yang berdampak pada implementasi hanya EMP sepeda motor terlindung (0,2 → 0,15) dan nilai normal wH pada FP (26 → 27 detik).

---

## E. Indikator kinerja MRLL/monev dan target

**Dari PM 96/2015.**
- Indikator LOS (9): V/C; kecepatan (batas atas/bawah menurut kondisi daerah); waktu perjalanan; kebebasan bergerak; keamanan; keselamatan; ketertiban; kelancaran; penilaian pengemudi (juga PP 32/2011 Pasal 19 ayat (3)).
- LOS ruas A–F (kecepatan ≥80/70/60/50/30 atau 10 perkotaan/<30 km/jam); LOS simpang A–F (tundaan <5/5–15/15–25/25–40/40–60/>60 det/kend).
- Target LOS minimal per fungsi jalan (arteri primer ≥B; arteri sekunder ≥C; kolektor sekunder ≥C; lokal sekunder ≥D; lingkungan ≥D).
- Monev: bandingkan LOS sebelum vs sesudah kebijakan; koreksi (penyempurnaan/pencabutan).
- Indikator kinerja perlengkapan jalan: keberadaan, lokasi, kondisi, fungsi.
- Data survei: LHRT (≥4×/tahun; 7 hari), VJP 9% LHRT; kecepatan TMS/SMS/travel/free-flow; tundaan lalu lintas & geometrik.
- Ambang kebijakan: simpang APILL (>750 kend/jam×8 jam; delay >30 det; pejalan kaki >175/jam; >5 laka/tahun); ATCS (≥3 simpang, ≤1 km); tidal flow (V/C >0,9; 70:30); SSA (V/C >0,85); pembatasan parkir (V/C >0,7; <30 km/jam); u-turn (V/C <0,65); kotak kuning (LOS ≥C).
- Kajian ke Dirjen wajib memuat minimal **kecepatan rata-rata dan V/C**.

**Dari PP 32/2011.** Ambang MKLL: perseorangan V/C ≥0,7 & <30 km/jam; sepeda motor V/C ≥0,5; ERP V/C ≥0,9 & ≤10 km/jam; evaluasi MKLL tiap tahun (Pasal 63 ayat (2)).

**Dari Perda 5/2014.** Target **60% perjalanan dengan KBU** dan **kecepatan rata-rata jaringan jalan 35 km/jam** (Pasal 8); efektivitas ERP diukur dari **peningkatan kecepatan rata-rata perjalanan** (Pasal 81 ayat (2)); ERP 07.00–20.00 hari kerja pada 9 ruas (Pasal 80); penilaian kinerja penyelenggaraan transportasi tahunan oleh Kepala Dinas (Pasal 237); RIT dievaluasi 5 tahunan (Pasal 10).

**Dari Perpres 55/2018.** Target 2029: 60% angkutan umum; waktu perjalanan angkutan umum ≤1 jam 30 menit jam puncak; kecepatan rata-rata jaringan jalan jam puncak ≥30 km/jam; cakupan 80%; akses ≤500 m; ≤3 kali pindah moda. Program pilar 6: ELE, ERP, prioritas bus di simpang, ATCS DKI, CCTV arteri, sistem informasi lalu lintas real time; rencana aksi dengan waktu, pendanaan, mekanisme; evaluasi 5 tahunan.

**Dari Pergub 68/2021.** 18 jenis data operasional (waktu tempuh, headway, posisi armada, kecelakaan & pelanggaran); monev tiap 3 bulan ke Gubernur; laporan BUMD bulanan.

---

## F. Struktur Proyek Perubahan PKN Tingkat II (KepKa LAN 1/2023 & Modul LAN)

**Posisi dalam kurikulum (KepKa LAN 1/2023, Lampiran A.1.b).** PKN Tingkat II terdiri dari 4 agenda: (1) Mengelola Diri (Energi Kepemimpinan; Integritas Kepemimpinan); (2) Kepemimpinan Strategis (Kepemimpinan Digital; Kepemimpinan Kewirausahaan; Organisasi Pembelajar); (3) Manajemen Strategis (Manajemen Strategis Sektor Publik; Isu Strategis; **Marketing Sektor Publik**; Kemitraan Swasta dan Pemerintah/PPP); (4) Aktualisasi Kepemimpinan Strategis (Visitasi; Visitasi Kepemimpinan Nasional; Policy Brief; **Proyek Perubahan**). Mata pelatihan Proyek Perubahan mencakup: konsep, penyusunan, seminar rancangan, pembekalan implementasi (off campus), implementasi, pembimbingan, seminar hasil, dan **diseminasi hasil kepada stakeholders**.

**Kriteria substansi (Modul Bab III.B).** Ide terobosan inovatif dari peserta; hasil diagnosis organisasi yang up-to-date; dukungan penuh atasan/institusi; meningkatkan kinerja menuju **organisasi adaptif**; feasible/implementable; menunjukkan **branding**. Kebaruan dinilai dari: dampak positif; solusi masalah; berkesinambungan dan **dapat direplikasi**; kompatibel dengan sistem yang ada. Locus: unit setingkat JPT Pratama.

**Komponen Rancangan Proyek Perubahan (RPP) — minimal 11 bagian (Modul Bab IV.C):**
1. Judul; 2. Deskripsi; 3. **Latar Belakang (Burning Platform)** — kondisi ideal, kondisi saat ini, masalah/kendala, strategi; kondisi ideal dirinci ke **jangka panjang, menengah, pendek**; referensi proyek perubahan terdahulu; 4. **Tujuan** (jangka panjang 1–2 tahun; menengah 6 bulan–1 tahun; pendek = sampai akhir PKN II); 5. **Output** (produk akhir jangka pendek yang diseminarkan) dan **Outcome** (berfungsinya output/manfaat); 6. **Tahapan Perubahan Rencana Strategis** (milestone per time-frame; tabel: jenis kegiatan, pelaksana, target waktu, mulai–selesai, output; strategi pengembangan kompetensi tim/stakeholder); 7. **Rencana Strategi Marketing** (untuk fase penyusunan dan implementasi; identifikasi instansi/individu berpengaruh positif/negatif; **stakeholder internal vs eksternal**; mengacu mata pelatihan Dialog Strategis & Marketing Sektor Publik); 8. Identifikasi potensi kendala dan solusi; 9. Faktor kunci keberhasilan; 10. **Tata kelola proyek** (struktur tim efektif, peserta sebagai team leader); 11. **Persetujuan Project Sponsor** (mentor/atasan langsung, form persetujuan).

**Lima aspek penilaian RPP:** (a) ketepatan dengan tuntutan organisasi adaptif; (b) terobosan inovatif dan cakupan manfaat; (c) tahapan rencana perubahan dan ketepatan strategi organisasi; (d) rencana strategi marketing (peta stakeholders, pemanfaatan sumber daya, strategi marketing); (e) rencana pengembangan kompetensi.

**Implementasi & laporan (Modul Bab V).** Jangka pendek ±2 bulan (setelah seminar RPP hingga Seminar Laboratorium Kepemimpinan); jangka menengah/panjang pasca PKN II dengan **komitmen tertulis** ditandatangani PPK instansi, peserta, dan mentor. **Enam aspek penilaian implementasi:** capaian perubahan terhadap rencana; kepemimpinan strategis; implementasi strategi marketing (ketepatan stakeholder utama, komunikasi, diseminasi & publikasi); keberlanjutan; pemberdayaan organisasi pembelajar; keterkaitan mata pelatihan pilihan. **Struktur laporan:** Ringkasan Eksekutif; Bab I Rencana Proyek Perubahan (termasuk pendahuluan); Bab II Pelaksanaan (enam aspek di atas); Bab III Penutup (lesson learnt, kesimpulan, saran); lampiran bukti dukungan stakeholder; video ≤10 menit; PPT 1 halaman pengembangan potensi diri; unggah ke LMS. Format dapat disesuaikan penyelenggara (infografis, video).

Implikasi untuk dokumen acuan ITCS: dokumen proyek harus dapat dipetakan ke struktur ini — burning platform berbasis data kinerja (kecepatan rata-rata, LOS, tundaan), milestone jangka pendek/menengah/panjang, peta stakeholder (Dishub DKI, Polda Metro/Ditlantas, Ditjen Hubdat/BPTJ, Bapenda, DLH, Transjakarta/Jak Lingko, Diskominfotik, BUMD), strategi marketing/diseminasi, tata kelola tim, dan project sponsor.

---

## G. Implikasi untuk desain aplikasi ITCS

### G.1 Kebutuhan kepatuhan (compliance requirements)
| ID | Kebutuhan | Dasar hukum / pasal |
|---|---|---|
| C-01 | Aplikasi harus memodelkan **status jalan** (nasional/provinsi/kota) per simpang dan menandai simpang yang melibatkan jalan nasional karena penyelenggaraan APILL di sana berada pada Dirjen Hubdat; perubahan rencana/perekayasaan di jalan nasional DKI memerlukan persetujuan Dirjen (workflow persetujuan + arsip surat). | PM 49/2014 Pasal 28 (rekonstruksi); PM 96/2015 Pasal 5 ayat (2)–(3), Lampiran III.B–C |
| C-02 | Penetapan lokasi & jenis APILL per ruas/simpang jalan provinsi harus terdokumentasi sebagai **Keputusan Gubernur**; aplikasi menyimpan referensi SK untuk tiap aset. | PM 96/2015 Lampiran I Bab III.B; PP 32/2011 Pasal 24; UU 22/2009 Pasal 95 |
| C-03 | Rekam **tanggal pemasangan** dan hitung tanggal berlakunya kekuatan hukum (30 hari setelah pemasangan) serta tenggat 60 hari sejak pemberlakuan Perda/Permen. | UU 22/2009 Pasal 102 |
| C-04 | Pemasangan/pemindahan APILL dan alat yang menyerupainya hanya dengan **izin Kepala Dinas**; aplikasi mewajibkan referensi izin sebelum aset aktif. | Perda 5/2014 Pasal 74 |
| C-05 | Setiap perangkat TI di APILL (detektor, kamera, DIS, controller) harus memiliki **sertifikasi**; simpan nomor sertifikat dan logo perhubungan (stiker) sebagai atribut aset. | PM 49/2014 Pasal 25 ayat (3), Pasal 21 |
| C-06 | Jadwal **pemeliharaan berkala ≤6 bulan** per APILL dengan checklist (penghalang, optik, korosi, cat) dan pemeliharaan insidentil (komponen rusak, **penyesuaian waktu siklus terhadap arus aktual**, posisi bergeser); alarm bila jatuh tempo. | PM 49/2014 Pasal 41 |
| C-07 | Manajemen aset: **umur teknis ≤5 tahun**, penghapusan berdasarkan penilaian kinerja; aplikasi menghasilkan laporan penilaian kinerja per aset. | PM 49/2014 Pasal 42 |
| C-08 | Pemantauan **keberadaan dan kinerja perlengkapan jalan** (keberadaan/lokasi/kondisi/fungsi) sebagai fungsi wajib pemeliharaan. | PP 32/2011 Pasal 31 ayat (2); PM 96/2015 Lampiran I Bab II.B.h dan Bab IV.D |
| C-09 | Mode **kendali terpusat/terkoordinasi** (ATCS) diakui sebagai "skema rencana siklus antar APILL diatur oleh sistem yang terpusat"; siklus tetap wajib menyediakan **≥8 rencana siklus (time-of-day plans)**; adaptif mengubah siklus pada kaki mayor & minor menurut arus. | PM 49/2014 Pasal 11–16 |
| C-10 | Algoritme penentuan siklus harus mempertimbangkan aspek makroskopis (volume masuk/keluar, kapasitas pendekat, komposisi termasuk pejalan kaki, variasi periodik/insidentil, distribusi arah, tundaan & antrian, kecepatan) dan mikroskopis (tundaan, konflik, percepatan) — dokumentasikan pemenuhan tiap aspek. | PM 49/2014 Pasal 17 |
| C-11 | ATCS minimal untuk **≥3 simpang berjarak ≤1 km**, dengan APILL, marka, rambu, detektor, jaringan komunikasi, dan Control Centre Room; sistem dapat menambah kamera, DIS, VMS, detektor angkutan umum, **fase bus priority**, alat pemantau kecepatan/volume. | PM 96/2015 Lampiran II.F.e |
| C-12 | Simpang adaptif otonom wajib memiliki **alat pendeteksi kendaraan**; aplikasi tidak boleh mengaktifkan mode adaptif pada simpang tanpa detektor sehat (health check). | PM 96/2015 Lampiran II.F.d |
| C-13 | Modul ITS ruas/simpang minimal menyediakan **pemantau kecepatan & volume** dan **media informasi** kepada pengguna jalan. | PM 96/2015 Lampiran II.F.g, II.G.i |
| C-14 | **Prioritas angkutan umum di persimpangan** (bus priority/waktu hijau khusus) dan hijau khusus pejalan kaki harus tersedia sebagai fitur; Pemda DKI wajib menyiapkan prioritas di persimpangan untuk KBU. | Perda 5/2014 Pasal 70 ayat (2) c; PM 96/2015 Lampiran II.A.5, II.D.3; Perpres 55/2018 Kebijakan 6.b.3 |
| C-15 | **Override manual oleh petugas Polri** (police panel / instruksi TMC) harus didahulukan atas isyarat APILL; aplikasi menyediakan mode manual/optimalisasi operasional dengan log siapa-kapan-mengapa (situasi Pasal 34 PP 32). | UU 22/2009 Pasal 104; PP 32/2011 Pasal 34–35; UU Pasal 97 |
| C-16 | **Preemption kendaraan hak utama** (pemadam, ambulans, dst.) sesuai urutan Pasal 134; aplikasi mendukung prioritas darurat dengan verifikasi. | UU 22/2009 Pasal 134–135 ayat (3) |
| C-17 | Saat kemacetan total (gridlock), logika **kotak kuning** didahulukan; kotak kuning hanya pada simpang adaptif/ATCS dengan LOS ≥C. | UU 22/2009 Pasal 103 ayat (3); PM 96/2015 Lampiran II.F.h |
| C-18 | Kegagalan APILL ("tidak berfungsi") harus memicu **notifikasi ke Polri/TMC** untuk optimalisasi operasional dan tercatat sebagai insiden. | PP 32/2011 Pasal 34 huruf b, Pasal 35 |
| C-19 | Perubahan kebijakan lalu lintas (fase, larangan belok, satu arah, pembatasan) wajib **disimulasikan sebelum ditetapkan** dan disosialisasikan; aplikasi menyimpan hasil simulasi & bukti sosialisasi. | PM 96/2015 Lampiran I Bab II.E.b, Bab III.C; PP 32/2011 Pasal 27 |
| C-20 | Monev wajib membandingkan **LOS sebelum vs sesudah** kebijakan; laporan pelaksanaan MRLL berbasis data & kinerja disampaikan ke **Forum LLAJ**; laporan tahunan ke Dirjen untuk MRLL di jalan nasional. | PM 96/2015 Lampiran I Bab VI; UU 22/2009 Pasal 98; PM 96/2015 Lampiran III.C |
| C-21 | Kajian ke Dirjen minimal memuat **kecepatan rata-rata dan V/C**; aplikasi menghasilkan template kajian (peta, tata letak, arah arus, dampak jaringan). | PM 96/2015 Lampiran III.A–B |
| C-22 | **Pusat kendali** subsistem Pemprov harus terintegrasi ke pusat kendali SIK LLAJ yang dikelola Polri; data harus dapat diakses setiap pembina LLAJ → API/interkoneksi dengan Polri (Ditlantas/NTMC) adalah kewajiban, bukan opsi. | UU 22/2009 Pasal 246–247 |
| C-23 | Data & informasi pusat kendali **harus dapat diakses masyarakat** → portal/API publik (dengan pengecualian data pribadi/penegakan hukum). | UU 22/2009 Pasal 250; Perda 5/2014 Pasal 233 |
| C-24 | **ETLE/penindakan**: aplikasi hanya menyediakan **dukungan bukti elektronik**; penindakan pelanggaran APILL/rambu adalah kewenangan Polri; PPNS Dishub hanya untuk jenis pelanggaran Pasal 95 Perda (jalur busway, kawasan pengendalian lalu lintas, dll.) dan bila di jalan harus didampingi Polri. Alur data pelanggaran → Polri; jangan membuat "denda otomatis" oleh Dishub untuk pelanggaran APILL. | UU 22/2009 Pasal 272, 260, 262 ayat (3), 287; PP 32/2011 Pasal 46; Perda 5/2014 Pasal 95, 234 |
| C-25 | Integrasi pajak kendaraan/uji emisi hanya melalui mekanisme yang sah: pangkalan data pelanggaran/kecelakaan ada di Polri; data pembatasan wajib terintegrasi ke sistem Pemprov; pengenalan TNKB diakui sebagai fungsi SIK LLAJ. Perlu perjanjian kerja sama (Pergub 68 Pasal 7; Perda Pasal 239). | PP 32/2011 Pasal 16; UU 22/2009 Pasal 248 huruf j–k; Pergub 68/2021 Pasal 13 ayat (4); Perda 5/2014 Pasal 239 |
| C-26 | **Kerahasiaan dan keamanan data**: penyelenggara bertanggung jawab menjamin kerahasiaan & keamanan; data terintegrasi milik Pemprov; akses pihak lain hanya dengan persetujuan Gubernur/pejabat → RBAC, audit trail, klasifikasi data, perjanjian akses. (UU PDP tidak ada dalam korpus; wajib dikaji terpisah.) | Pergub 68/2021 Pasal 10 ayat (7), Pasal 11 ayat (4)–(5) |
| C-27 | **Interoperabilitas** (data dapat dibagipakaikan antar sistem elektronik) dan **interkoneksi** sebagai kriteria desain; integrasi dengan sistem informasi Pemprov DKI (Jakarta Smart City) wajib. | Pergub 68/2021 Pasal 1 angka 4–5, Pasal 10 ayat (4) c, Pasal 11 ayat (1) |
| C-28 | ERP/pengendalian berbayar: hanya pada ruas yang memenuhi kriteria (2 jalur × ≥2 lajur; V/C ≥0,9; ≤10 km/jam; angkutan massal SPM), **tidak pada jalan nasional**, 07.00–20.00 hari kerja pada 9 ruas Perda (dapat diperluas Pergub); efektivitas diukur dari peningkatan kecepatan rata-rata; dana untuk kinerja lalu lintas termasuk teknologi. | PP 32/2011 Pasal 79–83; Perda 5/2014 Pasal 78–85 |
| C-29 | Ganjil-genap/pembatasan perseorangan: kriteria V/C ≥0,7 & <30 km/jam & angkutan umum SPM; cara berdasar jumlah penumpang/TNKB; wajib dinyatakan dengan rambu; **dievaluasi setiap tahun** → aplikasi menyediakan dashboard evaluasi tahunan MKLL. | PP 32/2011 Pasal 62–66; Pergub 68/2021 Pasal 13 |
| C-30 | Tundaan simpang dan LOS dilaporkan dengan kelas A–F PM 96/2015; target LOS minimal per fungsi jalan dan target 35 km/jam (Perda) / 30 km/jam (Perpres) sebagai KPI strategis. | PM 96/2015 Lampiran I Bab II.D; Perda 5/2014 Pasal 8; Perpres 55/2018 Lampiran II |
| C-31 | Lingkungan: pusat kendali memberi **informasi kualitas baku mutu udara**; pertimbangkan APILL tenaga surya; pembatasan berdasar emisi gas buang → integrasi uji emisi/KIR sebagai atribut kebijakan pembatasan, bukan penindakan. | UU 22/2009 Pasal 249 ayat (3) g; PM 96/2015 Lampiran II.H |
| C-32 | Aksesibilitas: APILL pejalan kaki dilengkapi tombol; isyarat suara/tanda universal untuk disabilitas. | PM 49/2014 Pasal 33 ayat (2); PM 96/2015 Lampiran II.C |
| C-33 | Kompetensi: MRLL dilaksanakan oleh pejabat/petugas berkompetensi → manajemen pengguna dengan kualifikasi operator. | PM 96/2015 Pasal 1 ayat (4) |
| C-34 | Rencana aksi RIT Jabodetabek (waktu, pendanaan, mekanisme) dan koordinasi BPTJ untuk program ATCS/ERP/prioritas bus. | Perpres 55/2018 Pasal 4 |
| C-35 | Laporan monev Jak Lingko tiap 3 bulan; penilaian kinerja transportasi tahunan → jadwal pelaporan bawaan aplikasi. | Pergub 68/2021 Pasal 15; Perda 5/2014 Pasal 237 |

### G.2 Formula/KPI yang harus diimplementasikan
1. C = J × wH / s; J = J0 × FHS × FUK × FG × FP × FBKi × FBKa; J0 = 600 × LE (tipe P) atau tabel/diagram (tipe O). (PKJI 5-1, 5-4, 5-6; FUK Jakarta = 1,05.)
2. DJ = q / C (PKJI 5-14) dengan ambang 0,85 (peringatan) dan 1,0 (jenuh).
3. wMS (PKJI 5-9), wHH = Σ(wMS + wK) (5-10), s = (1,5 wHH + 5)/(1 − RAS) (5-11), wHi (5-12), validasi rentang siklus Tabel 12-2 dan batas 130 detik; kuning 3,0 detik; hijau awal/akhir ≥10 detik.
4. Nq1, Nq2, Nq, PA = Nq × 20 / LM (5-15 s.d. 5-18) dengan NqMAX/POL.
5. RKH, NKH, RKH Total (5-19, 5-20, 5-31).
6. TLL (5-22), TG (5-23), T, TI = Σ(qT)/qTotal (5-32) → kelas LOS simpang A–F (PM 96/2015).
7. Konversi SMP dengan EMP Tabel 5-2; qJP = LHRT × K (5-13); RBKi, RBKa, RKTB (5-24–5-26).
8. Kecepatan rata-rata perjalanan (travel speed = panjang segmen / waktu tempuh termasuk tundaan berhenti), space mean speed, time mean speed, free flow speed (PM 96/2015) → KPI 35 km/jam (Perda) / 30 km/jam (Perpres) dan LOS ruas.
9. V/C ruas (nisbah volume-kapasitas) sebagai indikator wajib kajian dan ambang kebijakan (0,5/0,65/0,7/0,85/0,9).
10. Indikator kinerja perlengkapan jalan (keberadaan/lokasi/kondisi/fungsi), uptime APILL, jatuh tempo pemeliharaan 6 bulan, umur teknis 5 tahun.
11. Modal share angkutan umum (target 60%), waktu perjalanan angkutan umum jam puncak (≤90 menit), headway, waktu tempuh (Pergub 68 Pasal 10 ayat (6)).
12. Before–after LOS untuk setiap kebijakan (PM 96/2015 Bab VI); evaluasi tahunan MKLL (PP 32 Pasal 63).

### G.3 Hal-hal yang dilarang atau berisiko hukum
- Mengoperasikan/mengubah APILL di simpang yang melibatkan jalan nasional tanpa persetujuan Dirjen Hubdat (PM 96/2015 Pasal 5; PM 49/2014 Pasal 28).
- Memasang/memindahkan APILL atau perangkat menyerupai APILL tanpa izin Kepala Dinas (Perda 5/2014 Pasal 74); mengganggu fungsi APILL (UU Pasal 28, 275).
- Menempatkan aplikasi/Dishub sebagai penindak pelanggaran APILL/kecepatan; penindakan dan alat bukti elektronik adalah ranah Polri (UU Pasal 272, 260, 287; PP 32 Pasal 46); PPNS terbatas Pasal 95 Perda dan wajib didampingi Polri di jalan (UU Pasal 262 ayat (3)).
- Mengabaikan perintah petugas Polri dan kendaraan hak utama dalam logika kendali (UU Pasal 104, 135 ayat (3)).
- Menahan data pusat kendali dari pembina LLAJ lain atau dari masyarakat (UU Pasal 246 ayat (3), 250) — kecuali dibatasi kerahasiaan/keamanan data (Pergub 68 Pasal 10 ayat (7)).
- Memberikan akses data terintegrasi kepada pihak ketiga tanpa persetujuan Gubernur/pejabat (Pergub 68 Pasal 11 ayat (5)); menggunakan data pribadi pemilik kendaraan (pajak, uji emisi, TNKB) tanpa dasar perjanjian/regulasi — UU PDP tidak dalam korpus, perlu kajian tersendiri.
- Menerapkan ERP pada jalan nasional atau ruas yang tidak memenuhi kriteria (PP 32 Pasal 79 ayat (3)); pembatasan tanpa rambu (PP 32 Pasal 62).
- Menetapkan kebijakan tanpa simulasi dan sosialisasi (PM 96/2015 Lampiran I Bab II.E, III.C); tidak melapor ke Forum LLAJ (UU Pasal 98).
- Merancang siklus >130 detik atau tanpa kuning/merah semua yang cukup (PKJI 5.3.3; keselamatan).
- Mengklaim kepatuhan terhadap PM 76/2021 tanpa teks lengkapnya.

---

## H. Kutipan kunci verbatim

1. UU 22/2009 Pasal 1 angka 19: "Alat Pemberi Isyarat Lalu Lintas adalah perangkat elektronik yang menggunakan isyarat lampu yang dapat dilengkapi dengan isyarat bunyi untuk mengatur Lalu Lintas orang dan/atau Kendaraan di persimpangan atau pada ruas Jalan."
2. UU 22/2009 Pasal 7 ayat (2) huruf e: "urusan pemerintahan di bidang Registrasi dan Identifikasi Kendaraan Bermotor dan Pengemudi, Penegakan Hukum, Operasional Manajemen dan Rekayasa Lalu Lintas, serta pendidikan berlalu lintas, oleh Kepolisian Negara Republik Indonesia."
3. UU 22/2009 Pasal 96 ayat (4): "Gubernur bertanggung jawab atas pelaksanaan Manajemen dan Rekayasa Lalu Lintas ... untuk jalan provinsi setelah mendapat rekomendasi dari instansi terkait."
4. UU 22/2009 Pasal 98 ayat (1): "Penanggung jawab pelaksana Manajemen dan Rekayasa Lalu Lintas wajib berkoordinasi dan membuat analisis, evaluasi, dan laporan pelaksanaan berdasarkan data dan kinerjanya."
5. UU 22/2009 Pasal 102 ayat (2): "Alat Pemberi Isyarat Lalu Lintas, Rambu Lalu Lintas, dan/atau Marka Jalan ... mempunyai kekuatan hukum yang berlaku mengikat 30 (tiga puluh) hari setelah tanggal pemasangan."
6. UU 22/2009 Pasal 103 ayat (1): "Alat Pemberi Isyarat Lalu Lintas yang bersifat perintah atau larangan harus diutamakan daripada Rambu Lalu Lintas dan/atau Marka Jalan."
7. UU 22/2009 Pasal 104 ayat (2): "Tindakan sebagaimana dimaksud pada ayat (1) wajib diutamakan daripada perintah yang diberikan oleh Alat Pemberi Isyarat Lalu Lintas, Rambu Lalu Lintas, dan/atau Marka Jalan."
8. UU 22/2009 Pasal 135 ayat (3): "Alat Pemberi Isyarat Lalu Lintas dan Rambu Lalu Lintas tidak berlaku bagi Kendaraan yang mendapatkan hak utama sebagaimana dimaksud dalam Pasal 134."
9. UU 22/2009 Pasal 246 ayat (2): "Sistem Informasi dan Komunikasi Lalu Lintas dan Angkutan Jalan terpadu ... dikendalikan oleh pusat kendali yang mengintegrasikan data, informasi, dan komunikasi dari setiap subsistem."
10. UU 22/2009 Pasal 247 ayat (3): "Pusat kendali sebagaimana dimaksud pada ayat (2) dikelola oleh Kepolisian Negara Republik Indonesia."
11. UU 22/2009 Pasal 250: "Data dan informasi pada pusat kendali Sistem Informasi dan Komunikasi Lalu Lintas dan Angkutan Jalan harus dapat diakses dan digunakan oleh masyarakat."
12. UU 22/2009 Pasal 272: "(1) Untuk mendukung kegiatan penindakan pelanggaran di bidang Lalu Lintas dan Angkutan Jalan, dapat digunakan peralatan elektronik. (2) Hasil penggunaan peralatan elektronik sebagaimana dimaksud pada ayat (1) dapat digunakan sebagai alat bukti di pengadilan."
13. PP 32/2011 Pasal 34: "Optimalisasi operasional rekayasa lalu lintas ... dilakukan dalam situasi: a. perubahan lalu lintas secara tiba-tiba atau situasional; b. alat pemberi isyarat lalu lintas tidak berfungsi; c. adanya pengguna jalan yang diprioritaskan; ..." dan Pasal 35 ayat (1): "... dilaksanakan oleh Kepolisian Negara Republik Indonesia."
14. PP 32/2011 Pasal 46 ayat (3): "Penegakan hukum dapat dilakukan dengan cara langsung atau tidak langsung melalui media elektronik."
15. PP 32/2011 Pasal 79 ayat (3): "Pembatasan lalu lintas sebagaimana dimaksud pada ayat (1) tidak dapat dilakukan pada jalan nasional."
16. PM 96/2015 Pasal 5 ayat (2): "Pelaksanaan kegiatan Manajemen dan Rekayasa Lalu Lintas di jalan nasional yang berada di Provinsi Daerah Khusus Ibukota Jakarta dapat dilakukan oleh gubernur setelah mendapat persetujuan Direktur Jenderal Perhubungan Darat."
17. PM 96/2015 Lampiran II.F.e: "Pengendalian simpang dengan sistem APILL terkoordinasi atau dikenal dengan Area Traffic Control System (ATCS) merupakan pengendalian lalu lintas antar simpang ber APILL yang saling terkoordinasi. ... 1) jumlah simpang yang dikoordinasikan sekurang-kurangnya 3 simpang. 2) jarak antar simpang tidak lebih dari 1 km. ... sekurang-kurangnya dilengkapi dengan APILL, marka, rambu, alat pendeteksi kendaraan, jaringan komunikasi dengan kabel dan/atau tanpa kabel serta ruang pusat kendali (Control Centre Room)."
18. PM 96/2015 Lampiran I Bab II.D.b: "tingkat pelayanan A, dengan kondisi tundaan kurang dari 5 detik perkendaraan; ... tingkat pelayanan F, dengan kondisi tundaan lebih dari 60 detik perkendaraan."
19. PM 96/2015 Lampiran I Bab II.E.b: "Usulan alternatif penanganan lalu lintas terpilih harus disimulasikan sebelum ditetapkan menjadi skema penanganan lalu lintas terpilih."
20. PM 49/2014 Pasal 12 (rekonstruksi): "Waktu siklus terkoordinasi ... berupa skema rencana siklus antar Alat Pemberi Isyarat Lalu Lintas diatur oleh sistem yang terpusat."
21. PM 49/2014 Pasal 16 (rekonstruksi): "Waktu siklus adaptif ... berupa rencana siklus yang bervariasi pada kaki simpang mayor dan kaki simpang minor menurut situasi arus lalu lintas."
22. PM 49/2014 Pasal 25 ayat (3) (rekonstruksi): "Peralatan teknologi informasi untuk kepentingan lalu lintas ... harus memiliki sertifikasi sesuai dengan ketentuan peraturan perundang-undangan."
23. PM 49/2014 Pasal 41 ayat (2) dan (5) (rekonstruksi): "Pemeliharaan berkala ... dilakukan paling sedikit setiap 6 (enam) bulan." / "Pemeliharaan insidentil ... meliputi: ... b. penyesuaian waktu siklus dengan situasi arus lalu lintas aktual."
24. Perda 5/2014 Pasal 8 ayat (1) huruf a: "60% (enam puluh persen) perjalanan penduduk menggunakan sarana Kendaraan Bermotor Umum dan kecepatan rata-rata jaringan Jalan 35 (tiga puluh lima) km/jam untuk Transportasi Jalan."
25. Perda 5/2014 Pasal 74: "Setiap orang/pengguna Jalan tanpa izin dari Kepala Dinas dilarang: a. membuat, memasang, memindahkan Rambu Jalan, Marka Jalan, Alat Pemberi Isyarat Lalu Lintas, dan fasilitas pendukung; ..."
26. Perda 5/2014 Pasal 81 ayat (2): "Efektivitas pengendalian Lalu Lintas sebagaimana dimaksud pada ayat (1) huruf a diukur berdasarkan peningkatan kecepatan rata-rata perjalanan."
27. Pergub 68/2021 Pasal 1 angka 4: "Interoperabilitas adalah kemampuan data untuk dibagipakaikan antar sistem elektronik yang saling berinteraksi."
28. Pergub 68/2021 Pasal 10 ayat (7): "Dinas perhubungan, BUMD dan/atau badan usaha yang berbadan hukum bertanggung jawab untuk menjamin kerahasiaan dan keamanan data dan informasi sebagaimana dimaksud pada ayat (6)."
29. Pergub 68/2021 Pasal 11 ayat (4)–(5): "Data dan informasi yang sudah terintegrasi ke dalam sistem informasi Pemerintah Provinsi DKI Jakarta ... merupakan milik Pemerintah Provinsi DKI Jakarta. ... dapat diolah, dikelola, dimanfaatkan dan diakses secara online dan realtime oleh pihak lain yang terkait berdasarkan persetujuan Gubernur atau pejabat yang ditunjuk."
30. Perpres 55/2018 Lampiran, Kebijakan 6.c: "Penerapan teknologi sistem informasi untuk kepentingan lalu lintas dan angkutan (pengaturan dan pengawasan) secara real time, dengan program meliputi: 1) Peningkatan Sistem Informasi Lalu Lintas di Jalan Arteri; 2) Pembangunan dan Pengembangan ATCS (Area Traffic Control System); 3) Pengadaan dan Pemeliharaan CCTV di Jalan Arteri." (ejaan dinormalisasi dari OCR)
31. PKJI 2023 hlm. 112: "Panjang waktu kuning pada APILL di kota-kota Indonesia biasanya ditetapkan 3,0 detik. Untuk simpang APILL dengan area geometri yang luas dan kurang ideal, maka sebaiknya dihitung."
32. PKJI 2023 hlm. 124: "Waktu siklus yang melebihi 130 detik harus dihindari, kecuali pada kasus sangat khusus (simpang sangat besar), karena hal ini sering menyebabkan menurunnya kapasitas keseluruhan simpang APILL."
33. PKJI 2023 hlm. 104: "Pengaturan isyarat terkoordinasi dan/atau yang teraktualisasi dapat menghasilkan emisi lebih kecil dibandingkan pengaturan isyarat tetap."
34. PKJI 2023 hlm. 115–116: "Jika nilai DJ yang diperoleh terlalu tinggi (misal >0,85), maka perlu dilakukan perubahan rencana yang berkaitan dengan penetapan fase dan waktu isyarat, lebar pendekat dan membuat perhitungan baru."
35. PKJI 2023 hlm. 109 (Catatan): "Model kapasitas Simpang APILL dari negara Barat tentang tipikal keberangkatan arus lalu lintas tidak dapat diterapkan karena teori tersebut didasarkan pada teori gap acceptance ... Model lain yang telah dikembangkan dan dianggap sesuai didasarkan pada pengamatan perilaku pengemudi di Indonesia diterapkan dalam pedoman ini."
36. Modul LAN PKN II hlm. 35: "laporan dibuat dalam 3 (tiga) bagian utama, selain ringkasan eksekutif, yaitu: 1. Ringkasan Eksekutif 2. Bab I Rencana Proyek Perubahan ... 3. Bab II Pelaksanaan Proyek Perubahan ... 4. Bab III Penutup."
37. PM 76/2021 (abstrak): "Dalam Peraturan Menteri Perhubungan tentang Sistem Manajemen Transportasi Cerdas di Bidang Lalu Lintas dan Angkutan Jalan meliputi jenis, fungsi, dan prinsip kerja Sistem Manajemen Transportasi Cerdas, penyelenggaraan Sistem Manajemen Transportasi Cerdas, dan pembinaan dan pengawasan."

---

## Daftar tindak lanjut sumber
1. Peroleh batang tubuh PM 76/2021 (BN 2021/1009) dan PM 67/2021 (rujukan dalam abstrak) — kritis untuk Bagian C.
2. Peroleh PP 79/2013 (Jaringan LLAJ, Pasal 56–57 dasar PM 49/2014) dan PP 37/2011 (Forum LLAJ) — disebut dalam konsiderans, tidak dalam korpus.
3. Peroleh Pergub DKI turunan Perda 5/2014 tentang MRLL (Pasal 75), Sistem Informasi Transportasi (Pasal 235), ERP (Pasal 78 ayat (3), 82 ayat (4)), dan regulasi ganjil-genap.
4. Peroleh peraturan Dirjen Hubdat tentang tata cara penentuan waktu siklus dan penilaian kinerja APILL (PM 49/2014 Pasal 18, 42 ayat (6)).
5. Kaji UU 27/2022 Perlindungan Data Pribadi dan Perpol tentang ETLE untuk kepatuhan data — tidak ada dalam korpus.
6. Raperda RIT Jakarta: file kosong; perlu sumber ulang.
