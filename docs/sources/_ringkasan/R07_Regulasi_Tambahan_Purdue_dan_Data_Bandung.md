# R07 — Regulasi Tambahan (Kota Bandung, Jawa Barat, DKI/ERP), Rumus & Algoritma Purdue (POG, Platoon Ratio, Link Pivot), dan Profil Data Kota Pilot Bandung

Disusun: 2026-09-12 (riset lanjutan untuk platform IRAMA; kota pilot: Bandung). Semua kutipan pasal diambil dari `docs/sources/_teks_ekstraksi/*.txt` (pdftotext -layout); nomor halaman = nomor tercetak di dokumen (bila tidak tercetak, ditulis "PDF hal."). Data Bandung diambil dari `docs/sources/08_Data_Kota_Pilot_Bandung/` (arsip teks + `_urls.tsv`). Tahap T1–T5 mengikuti konvensi `Pra-Perencanaan/04`. Bila suatu ketentuan **tidak ditemukan** dalam teks, dinyatakan eksplisit.

> **ERRATUM (2026-09-15, koordinator):** kolom Tahap dan rekomendasi pilot di dokumen ini mengikuti skema tahapan 2026-09-12 (`Pra-Perencanaan/04`, kini `docs/planning/04`), yang sudah direvisi pada 2026-09-14. Yang berlaku sekarang: T1 dan T2 mengolah satu simpang dari rekaman; T3 menambah deteksi kejadian, pemantauan, laporan wajib, controller baca-saja, dan uji lapangan; T4 memulai kendali, adaptif per simpang, offset dasar, prioritas bus dan darurat (TSP/AVL BEMO), serta integrasi instansi; T5 mencakup optimasi koridor dan jaringan, termasuk Link Pivot (§B.4) dan penalaan offset dari probe. Koridor K-A sampai K-D (§C.3) tetap berguna sebagai kandidat lokasi: simpang T1–T2 dapat dipilih dari K-A, sedangkan koordinasi koridor baru dikerjakan di T4 dan T5. Rujukan tahap per fitur: `docs/planning/05`; keputusan user: `docs/kb/10` §B2.

Catatan kualitas sumber:
- `Perda_Bandung_12_2024_...txt` (98 hal.) teks utuh tetapi OCR asli mengandung salah eja ("Manajernen", "darr/atau"); kutipan dinormalkan tanpa mengubah makna.
- `Perwal_Bandung_20_2023_Penyelenggaraan_SPBE.pdf` (60 hal.) **hasil scan tanpa lapisan teks** (60 byte teks; JDIH dan BPK memuat berkas yang sama); isi hanya dari abstrak BPK.
- `Permenhub_PM_49_2014_...txt` kehilangan label pasal (lihat R05); amanat "tata cara penentuan waktu siklus" **tidak dapat diverifikasi ulang** dari teks ekstraksi.
- Paper asli Link Pivot (Day & Bullock 2011, TRR 2259-04) berbayar; algoritma direkonstruksi dari poster ATSPM Workshop 2016 (penulis sama) + TRB 11-0036 + laporan JTRP 2008/2014.

---

## A. Regulasi baru: pasal → isi → implikasi aplikasi → tahap

### A.1 Perda Kota Bandung No. 12 Tahun 2024 tentang Penyelenggaraan Perhubungan (BD 2024; 98 hal.) — **mencabut Perda 16/2012, 4/2017, 3/2020**

Status: berlaku (BPK Details/315103). Struktur relevan: Bab IX Sistem Manajemen Transportasi Cerdas (Ps.103–106); Bab XI Sistem Informasi & Telekomunikasi Perhubungan (Ps.111–114); Bab XIII MRLL (Ps.121–144); Bab tentang angkutan massal (Ps.175–179); Forum LLAJ (hal. 84).

| Pasal (hal.) | Isi | Implikasi untuk aplikasi | Tahap |
|---|---|---|---|
| Ps.103 ayat (1)–(2) (hal. 44) | Pemkot "dapat menerapkan Sistem Manajemen Transportasi Cerdas" dengan aplikasi TI, perangkat elektronik, jaringan telekomunikasi; sistem "bersifat **sistem terbuka, berkesinambungan dan sesuai dengan standar** yang ditetapkan". | Landasan hukum kota untuk platform berstandar terbuka (NTCIP/API terbuka) — selaras ADR standar terbuka; syarat "berkesinambungan" → rencana O&M multi-tahun. | T1 |
| Ps.103 ayat (3)–(4) (hal. 44–45) | STC sebagai **pengumpul dan pengolah data**: kecepatan vs batas, pola aliran/fluktuasi volume, kepadatan per satuan panjang, waktu perjalanan asal–tujuan, cuaca, kondisi & geometrik jalan, **identitas kendaraan**, kondisi sarana-prasarana. | Definisi katalog data minimum ITCS kota (volume, kecepatan, kepadatan, travel time, cuaca, geometrik, plat). "Identitas kendaraan" = data pribadi → PDP (UU 27/2022) dan Perpol 8/2023 berlaku. | T1–T3 |
| Ps.103 ayat (5)–(6) (hal. 45) | Data digunakan sebagai dasar **perencanaan MRLL & MKLL** oleh Pemerintah/Pemkot dan **layanan informasi kepada masyarakat** yang ditempatkan pada prasarana, kendaraan, ruang jalan, tempat lain (ditetapkan Wali Kota). | Modul laporan MRLL (ATSPM → rekomendasi) dan kanal informasi publik (VMS/web/API terbuka). | T2–T3 |
| Ps.104 (hal. 45) | Tujuan STC: pengawasan lalu lintas & transportasi publik; **deteksi dan identifikasi pergerakan**; komunikasi kendaraan–infrastruktur (V2I); pengumpulan/pemrosesan data untuk perencanaan & pengaturan; **informasi real-time** kepada pengguna jalan. | Persyaratan fungsional tingkat kota: deteksi (detektor/CCTV analitik), V2I (T5), feed real-time. | T1 (deteksi) → T5 (V2I) |
| Ps.105 (hal. 45–46) | Komponen STC: (a) sistem manajemen lalu lintas tingkat lanjut (ATMS), (b) informasi pengguna jalan (ATIS), (c) keselamatan & kontrol kendaraan, (d) operasi kendaraan komersial, (e) transportasi umum tingkat lanjut (APTS), (f) pembayaran elektronik, (g) manajemen darurat, (h) antarkota, (i) manajemen kebutuhan perjalanan, (j) parkir, (k) pengendalian otonom, (l) lainnya; "dapat dilakukan sesuai kebutuhan". | Taksonomi PM 76/2021 diturunkan ke kota — IRAMA = (a) inti, (b) & (e) & (g) sebagai modul (TSP/EVP), (i) opsional (ERP/ganjil-genap). Bahasa taksonomi ini dipakai di dokumen pengadaan. | T1 (a) → T3 (b,e,g) → T5 (i,k) |
| Ps.106 (hal. 46) | Ketentuan lebih lanjut STC diatur dengan **Peraturan Wali Kota**. | Perwal STC Kota Bandung **belum ditemukan** (pencarian JDIH) → peluang: draf Perwal ATCS/ITCS sebagai deliverable proyek. | T1 |
| Ps.111–112 (hal. 48–49) | Pemkot membangun **sistem TIK Transportasi Kota** untuk "perencanaan, pengaturan, pengendalian, dan pengawasan serta operasional"; layanan data "saling terhubung dan terintegrasi berbasis elektronik"; dapat diakses melalui situs resmi; **dikelola oleh Dinas bekerja sama dengan Perangkat Kota yang membidangi TIK** (Diskominfo). | Model kepemilikan: Dishub = pemilik data/proses, Diskominfo = penyelenggara infrastruktur (server/hosting/keamanan). Arsitektur harus mendukung pemisahan peran ini (IAM, tenant). | T1 |
| Ps.113 (hal. 49) | Muatan minimal data: regulasi & kebijakan; **kondisi lalu lintas**; **pengendalian dan pengawasan lalu lintas**; informasi lainnya. | Dasar hukum publikasi dashboard/open data kondisi lalu lintas dan status pengendalian (mis. status APILL). | T2 |
| Ps.121–122 (hal. 51–52) | Perencanaan MRLL: identifikasi masalah, inventarisasi arus, angka pelanggaran & kecelakaan, penetapan tingkat pelayanan, rencana kebijakan; **dilakukan Wali Kota setelah rekomendasi** Kemenhub, Kemen PU, **Polri (operasional MRLL)**, dan **Pemprov Jawa Barat**; berkoordinasi dengan kab/kota berbatasan. | Alur persetujuan rencana waktu sinyal/koordinasi: fitur "paket rekomendasi MRLL" harus menghasilkan dokumen untuk Polri & Pemprov; koordinasi lintas batas (Cimahi/Kab. Bandung). | T2 |
| Ps.123–124 (hal. 52–53) | Data identifikasi: geometrik simpang, perlengkapan jalan, lokasi potensi kecelakaan & kemacetan, kapasitas, **kinerja lalu lintas**; inventarisasi: volume, komposisi, variasi, distribusi arah, **kecepatan dan tundaan**, **kinerja perlengkapan jalan**, perkiraan volume. | Katalog KPI ATSPM (volume/pendekat, tundaan, kecepatan, kesehatan perangkat) memenuhi kewajiban ini secara otomatis. | T1–T2 |
| Ps.130–131 (hal. 54) | Kebijakan lalu lintas "pada setiap ruas Jalan dan/atau persimpangan" ditetapkan Wali Kota; diinformasikan kepada masyarakat. | Setiap rencana waktu/koordinasi = kebijakan per simpang → perlu jejak audit versi rencana + publikasi. | T2 |
| Ps.135–137 (hal. 56–57) | Perekayasaan: pengadaan/pemasangan/perbaikan/pemeliharaan perlengkapan jalan (termasuk APILL) **oleh Dinas**; pemeliharaan mencakup "**memantau keberadaan dan kinerja perlengkapan jalan**", mengganti yang rusak. | Modul health monitoring APILL/detektor/kamera (watchdog) memenuhi Ps.137 ayat (2) huruf a. | T1 |
| Ps.138 (hal. 57) | "Optimalisasi operasional rekayasa Lalu Lintas … dilaksanakan oleh **Dinas setelah berkoordinasi dengan Kepolisian** Negara Republik Indonesia." | Operasi harian ruang kendali (intervensi manual, skenario) = kewenangan Dishub dengan koordinasi Polri (bandingkan PP 32/2011 Ps.35 yang menempatkan Polri sebagai pelaksana) → fitur log koordinasi/notifikasi ke Polri untuk intervensi situasional. | T1 |
| Ps.179 ayat (1) (hal. 70) | Infrastruktur angkutan massal berbasis jalan: koridor busway, "**pembangunan pusat kendali dan bus location system**", tiket, park-and-ride, integrasi moda, **peningkatan kapasitas simpang**. | Dasar TSP: integrasi AVL Trans Metro Bandung (BEMO) ke IRAMA; prioritas bus di simpang = "peningkatan kapasitas simpang". | T3 |
| Forum LLAJ (hal. 84) | Forum LLAJ bertugas koordinasi; keanggotaan sesuai UU 22/2009. | Laporan kinerja periodik ke Forum LLAJ (UU Ps.98) — fitur ekspor laporan. | T2 |

### A.2 Perda Provinsi Jawa Barat No. 5 Tahun 2024 tentang Penyelenggaraan Perhubungan (121 hal., ditetapkan 17 Mei 2024) — mencabut Perda Jabar 3/2011 & 4/2017

| Pasal (hal.) | Isi | Implikasi | Tahap |
|---|---|---|---|
| Ps.1 angka 13, 15, 23 (hal. 6) | Definisi Jalan Provinsi, APILL ("perangkat elektronik yang menggunakan isyarat lampu…"), MRLL. | Konsisten UU 22/2009. | — |
| Ps.14 (hal. 16) | Pengelolaan lalu lintas di **Jalan Provinsi** via MRLL, MKLL, Andalalin; ayat (3) "dikembangkan secara terintegrasi … **memanfaatkan teknologi informasi**". | Simpang di jalan provinsi dalam kota Bandung berada di kewenangan Dishub Jabar → IRAMA perlu model multi-yurisdiksi (kepemilikan simpang per status jalan). | T1 (model data) |
| Ps.15 (hal. 16–17) | MRLL di ruas, persimpangan, jaringan; kegiatan perencanaan–pengawasan; **dilaksanakan oleh Dinas (provinsi)**. | Peran Dishub Jabar sebagai pengguna/penyetuju untuk simpang jalan provinsi. | T2 |
| Ps.16 (hal. 17–18) | Tingkat pelayanan: V/C, kecepatan, waktu perjalanan, dst.; pengendalian simpang: tak bersinyal, bersinyal (**APILL**), bundaran, tak sebidang, "**pengendalian simpang dengan memanfaatkan teknologi**". | Kategori "simpang berteknologi" (ATCS/adaptif) diakui eksplisit di tingkat provinsi. | T1 |
| Ps.20 (hal. 20) | Jika kab/kota menginisiasi MRLL pada ruas jalan provinsi yang bersinggungan dengan jalan kab/kota, pelaksanaan **melalui persetujuan Pemprov (Dinas)**. | Koordinasi koridor lintas status jalan (mis. Jl. Dr. Djunjunan/Pasteur, Soekarno-Hatta perlu cek status) → alur persetujuan dalam aplikasi. | T2 |
| Ps.166 (hal. 78) | Gubernur membangun **sistem informasi perhubungan**: data moda, penumpang, muatan, status/kelas jalan, "**data dukung pengendalian pergerakan lalu lintas**"; **terintegrasi dengan sistem kab/kota**; dibangun Dinas berkoordinasi Diskominfo provinsi. | Titik integrasi IRAMA Bandung ↔ Pemprov (API pertukaran data lalu lintas); peluang replikasi ke kota lain di Jabar lewat provinsi. | T3–T4 |

### A.3 Perwal Kota Bandung No. 101 Tahun 2022 — Kedudukan, Susunan Organisasi, Tugas & Fungsi Dinas Perhubungan (37 hal.; berlaku 13-09-2022, menggantikan Perwal 121/2021)

| Pasal (hal.) | Isi | Implikasi | Tahap |
|---|---|---|---|
| Ps.3 (hal. 6) | Struktur: Sekretariat (Sub Bagian **Program, Data dan Informasi**); **Bidang Lalu Lintas dan Perlengkapan Jalan** (Seksi Lalu Lintas Jalan; Seksi Perlengkapan Jalan); Bidang Angkutan & PKB; Bidang Sarana & Prasarana Transportasi (Seksi Alat Penerangan Jalan; Seksi Sarana & Prasarana); **Bidang Pengendalian Operasional** (Seksi Ketertiban Transportasi; Seksi Pengaturan, Pengawasan dan Pengendalian Jalan); UPTD. | Pemetaan peran aplikasi: pemilik produk = Kabid Lalu Lintas; operator ruang kendali & lapangan = Bidang Dalops; data/laporan = Sub Bagian PDI; PJU pintar = Bidang Sarpras. | T1 |
| Ps.10 ayat (4) huruf f–i (hal. 17–18) | Kepala Seksi Lalu Lintas Jalan: "**pengukuran kinerja lalu lintas berbasis teknologi informasi**"; MRLL jaringan jalan kota; "perencanaan, pemasangan, pemeliharaan dan evaluasi terhadap **APILL beserta perangkat pendukungnya**"; "perencanaan, pemasangan, pemeliharaan, pengembangan dan evaluasi terhadap **kamera pengawas lalu lintas (CCTV) yang terintegrasi**". | ATCS/ITCS secara organik ada di **eselon IV** (Seksi) — kapasitas SDM terbatas → aplikasi harus rendah beban operasi (otomasi laporan, alarm). KPI ATSPM = "pengukuran kinerja berbasis TI". | T1 |
| Ps.11 (hal. 18) | Seksi Perlengkapan Jalan: perlengkapan jalan **selain APILL** dan alat pengendali/pengaman. | Batas cakupan aset: APILL & CCTV di Seksi Lalu Lintas Jalan; rambu/marka di Seksi Perlengkapan Jalan (modul aset opsional). | T2 |
| Ps.20 (hal. 31–32) | Seksi Pengaturan, Pengawasan & Pengendalian Jalan: pembinaan & pemantauan pengaturan lalu lintas; car free day/night; "**pemantauan dan pengembangan sistem penyelenggaraan pengaturan, pengawasan dan pengendalian transportasi**". | Pengguna operasional harian (gatur, event) → fitur skenario/plan khusus event, jadwal CFD. | T1–T2 |

### A.4 Perwal Kota Bandung No. 49 Tahun 2021 — UPTD pada Dinas Perhubungan (18 hal.)

| Pasal (hal.) | Isi | Implikasi | Tahap |
|---|---|---|---|
| Ps.2–3 (hal. 5) | Dibentuk 3 UPTD Kelas A: **Pengelolaan Perparkiran, Pengelolaan Terminal, Angkutan**. | **Tidak ada UPT ATCS/pusat kendali** (berbeda dengan DKI yang punya unit khusus). Opsi kelembagaan: tetap di Seksi (T1) atau usulan UPTD Pengendalian Lalu Lintas (T3+) — masukan untuk Perwal STC (A.1 Ps.106). | T1/T3 |
| Ps.10 (hal. 12) | UPTD Angkutan: operasional pengelolaan angkutan (operator Trans Metro Bandung; berstatus BLUD menurut Wikipedia/uptangkutan-bandung.id). | Mitra TSP & sumber AVL (BEMO) = UPTD Angkutan. | T3 |

### A.5 Perwal Kota Bandung No. 20 Tahun 2023 — Penyelenggaraan SPBE (60 hal.; berlaku 13-07-2023; mencabut Perwal 60/2021 & 1338/2017) — **hanya abstrak (PDF scan)**

| Materi (abstrak BPK) | Implikasi | Tahap |
|---|---|---|
| Ruang lingkup: Tata Kelola SPBE, Manajemen SPBE, **Audit TIK SPBE**, Penyelenggara SPBE, Pemantauan & Evaluasi SPBE. | IRAMA di Bandung wajib terdaftar dalam arsitektur & peta rencana SPBE kota (Perwal 85/2021 arsitektur 2021–2025 dicabut Perwal 28/2023; peta rencana Perwal 106/2021 diubah 31/2023), tunduk audit TIK, dan manajemen keamanan informasi (Perwal 29/2023). Hosting: koordinasi Diskominfo (sejalan Perda 12/2024 Ps.112 ayat 3). | T1 (registrasi), T2 (audit) |
| Ketentuan pasal rinci **tidak dapat dikutip** (scan). | Workaround: rujuk induk Perpres 95/2018 SPBE dan Perpres 39/2019 Satu Data (belum di korpus) — tandai sebagai kebutuhan unduhan lanjutan. | — |

### A.6 Pergub DKI Jakarta No. 25 Tahun 2017 — Pengendalian Lalu Lintas dengan Pembatasan Kendaraan Bermotor melalui Sistem Jalan Berbayar Elektronik (13 hal.) — **DICABUT** oleh Pergub 20/2022 (2 hal.)

| Pasal (PDF hal.) | Isi | Implikasi | Tahap |
|---|---|---|---|
| Ps.1 angka 5, Ps.4 (4–5) | "Unit Pengelola Sistem Jalan Berbayar Elektronik" = **unit pelaksana teknis di bawah Dinas Perhubungan** yang menyelenggarakan pembangunan & operasional. | Pola kelembagaan ERP: UPT/BLUD tersendiri; ERP bukan modul ATCS tetapi konsumen data ATCS. | T5 |
| Ps.6 ayat (1) (5) | Kriteria ruas ERP: 2 jalur × ≥2 lajur; angkutan umum massal SPM; **V/C ≥ 0,9 pada jam puncak**; kecepatan rata-rata jam puncak **≤ 10 km/jam**; ayat (2) memperhatikan kualitas lingkungan. | Sama dengan PP 32/2011 Ps.79 → IRAMA dapat menghasilkan bukti kelayakan (V/C, kecepatan) per koridor dari data detektor/probe. | T3 (KPI) → T5 |
| Ps.7 (6) | 9 ruas awal (Sisingamangaraja, Sudirman, Thamrin, Medan Merdeka Barat, Majapahit, Gajah Mada, Hayam Wuruk, Gatot Subroto, Rasuna Said); bertahap berdasarkan kajian Dishub. | Contoh penetapan koridor lewat Pergub (bukan Perda) — di Bandung padanannya Perwal. | — |
| Ps.10–11 (7–8) | Tarif disesuaikan "kepadatan lalu lintas dan kecepatan kendaraan di lapangan; koridor/segmen/waktu" → **tarif dinamis**. | Tarif dinamis membutuhkan ukuran kepadatan/kecepatan real-time → antarmuka data IRAMA → sistem ERP. | T5 |
| Ps.14–16 (8–9) | Perangkat harus **tersertifikasi Kominfo**; terbukti dipakai di kota dunia; mendukung penegakan hukum **Polri**; dapat diintegrasikan dengan kebijakan transportasi daerah; Kadis menetapkan spesifikasi. | Pola persyaratan perangkat yang bisa ditiru untuk spesifikasi kamera/detektor ITCS (sertifikasi, interoperabilitas). | T1 (spek) |
| Ps.17–20 (9–10) | Prabayar; pembangunan oleh Unit Pengelola, dapat kerja sama badan usaha via pelelangan umum; **kontrak berbasis kinerja**; pembayaran dari pendapatan Unit Pengelola. | Contoh skema KPBU/performance-based untuk sistem lalu lintas — relevan opsi pembiayaan IRAMA (docs/planning/03). | T3+ |
| Ps.23 (11–12) | Monev periodik oleh Unit Pengelola, Dishub, Biro Perekonomian: kinerja lalu lintas ruas/koridor; jumlah kendaraan; V/C; **kecepatan rata-rata harian**; dampak sosial-ekonomi. | Daftar KPI monev = keluaran modul laporan IRAMA. | T2–T3 |
| Pergub 20/2022 Menimbang a | Dicabut karena "ketidaksesuaian kebijakan Jalan Berbayar Elektronik dengan kebutuhan hukum saat ini". | ERP di DKI menunggu Perda (Raperda PL2SE); Bandung: jangan jadikan ERP prasyarat produk. | T5 (opsional) |

Pergub DKI khusus MRLL (turunan) **tidak ditemukan** di pencarian (yang ada Pergub 531/2015 Tim Evaluasi Andalalin dan Pergub 68/2021 yang sudah di korpus).

### A.7 Permenhub PM 67 Tahun 2021
Judul terverifikasi: "**Organisasi dan Tata Kerja Kementerian Perhubungan**" (peraturan.go.id; JDIH Kemenhub). **Tidak relevan** LLAJ/perlengkapan jalan → tidak diunduh.

### A.8 Peraturan/Keputusan Dirjen Hubdat tentang tata cara penentuan waktu siklus APILL
Hasil pencarian: tidak ada Perdirjen berjudul "tata cara penentuan waktu siklus". Yang ada: **Keputusan Dirjen Perhubungan Darat SK.326/KP.108/DRJD/2018 tentang Pengaturan Lalu Lintas di Persimpangan Berdiri Sendiri dengan APILL** (pembaruan Kep. Dirjen 273/HK.105/DRJD/96 yang sudah ada di korpus). Salinan resmi **tidak dapat diunduh** (JDIH Kemenhub: pencarian nomor 326/2018 kosong; WAF "Request Rejected"). Isinya dikutip tesis PTDI-STTD (digilib.ptdisttd.ac.id/5857, Bab III hal. 26–27, diunduh ke scratchpad): kriteria pemasangan APILL — arus rata-rata **> 750 kend/jam selama 8 jam/hari**, atau **tundaan rata-rata > 30 detik**, atau **> 175 pejalan kaki/jam selama 8 jam**, atau sering kecelakaan, atau kombinasinya; jenis APILL 3/2/1 warna; fungsi (standarisasi ruang simpang, keteraturan, kapasitas, kurangi kecelakaan); belok kiri langsung pada prinsipnya diperbolehkan. Parameter siklus (waktu siklus, fase, hijau, rasio g/c, merah semua, kuning, antar hijau, waktu hilang) dalam tesis mengacu MKJI 1997 — sama dengan PKJI 2023 di korpus. Implikasi: T1 — validator rencana waktu (min/max hijau, antar hijau, waktu hilang) memakai PKJI 2023 + Kep. Dirjen 273/1996; kriteria 750 kend/jam & tundaan 30 dtk dapat dipakai sebagai aturan "kelayakan APILL/penonaktifan ke kedip" (menjawab kritik Gubernur Jabar Juli 2025 bahwa APILL di lokasi sepi "bikin macet").

---

## B. Rumus & algoritma Purdue (POG, Platoon Ratio, Arrival Type, AOG, Link Pivot) + ATSPM UDOT

### B.1 Percent on Green (POG) dan Platoon Ratio — laporan JTRP 2014 (Day, Bullock dkk., "Performance Measures for Traffic Signal Systems: An Outcome-Oriented Approach", TPF-5(258), doi 10.5703/1288284315333; 132 hal.)
- Eq. 6.4 (hal. 71): faktor progresi HCM PF = (1 − P)·f_PA / (1 − g/C), P = proporsi kendaraan tiba saat hijau, f_PA = faktor penyesuaian platoon (default 1,0).
- **Eq. 6.5 (hal. 71–72): P = N_g / (N_r + N_g) = N_g / N**, N_r = kendaraan tiba saat merah, N_g saat hijau, N total dalam satu siklus (merah pendahulu + hijau berikutnya). Catatan: teks OCR menulis "P ≈ Nr/(Nr+Ng)"; definisi naratif dan Tabel 6.2 (P2,i = Ng/N, mis. 19/23 = 0,826) menegaskan **P = N_g/N**.
- **Eq. 6.6 (hal. 72): Platoon Ratio R_p = P / (g/C)** — "membagi P dengan rasio g/C" untuk mengoreksi pengaruh porsi hijau.
- Tabel 6.1 (hal. 72), berdasarkan HCM Exhibit 15-4: AT 1: R_p ≤ 0,50 (default 0,333, very poor); AT 2: 0,50 < R_p ≤ 0,85 (0,667, unfavorable); AT 3: 0,85 < R_p ≤ 1,15 (1,000, random); AT 4: 1,15 < R_p ≤ 1,50 (1,333, favorable); AT 5: 1,50 < R_p ≤ 2,00 (1,667, highly favorable); AT 6: R_p > 2,00 (2,000, exceptional); kolom **AT terinterpolasi** (linier antar batas; AT = 2R_p + 1 untuk R_p ≤ 0,5; … ; AT = 2R_p + 2 untuk 1,5 < R_p ≤ 2; AT = 6 di atas 2).
- Tabel 6.2 (hal. 73): contoh per siklus: t_BOC, N_g, N, P, C, g, g/C, AT (mis. 19/23 → P = 0,826; g/C = 0,44 → AT 5,75).
- Eq. 6.7 (hal. 73): tundaan dari profil kedatangan terukur d = ∫ [q(t0) + A(t) − D(t)] dt (luas antara kurva kumulatif tiba & berangkat) — versi diskret pada §6.4.
- §6.5 (hal. 75): Purdue Coordination Diagram (PCD) = plot waktu-dalam-siklus kedatangan detektor setback vs BOG/EOG; §6.6 (hal. 79) flow profile; §6.7 (hal. 84) pembentukan & dispersi platoon.
- **Tidak ada** bagian "Link Pivot" dalam laporan ini (grep "pivot" = 0).

### B.2 Rumus yang sama versi 2008 — JTRP 2008 "Real-Time Arterial Traffic Signal Performance Measures" (Day, Smaglik, Bullock, Sturdevant; 244 hal.)
- **Eq. 4.17 (hal. 110): R_p = (C / g_i) · POG**; **Eq. 4.18 (hal. 110): POG = N_g / (N_g + N_r)**.
- Tabel 4.10 (hal. 112): definisi AT + persamaan interpolasi (identik Tabel 6.1 di atas); Gambar 4.19 (hal. 113) AT terinterpolasi vs integer.

### B.3 Arrivals on Green (AOG), tundaan, stops dari profil aliran — Day, Brennan, Hainen, Remias, Bullock 2011 (TRB Paper 11-0036, "Reliability, Flexibility, and Environmental Impact of Alternative Arterial Offset Optimization Objective Functions", Purdue e-Pubs civeng/10; 34 hal.)
Profil aliran per bin waktu-dalam-siklus (lebar bin w detik; N_i = jumlah kedatangan di bin i selama Q siklus; G_i = probabilitas hijau di bin i; s = arus jenuh):
- Eq. 1 (paper hal. 4): antrian q_i = max(0, q_{i−1} + N_i − c_i).
- Eq. 2 (hal. 4): kapasitas bin c_i = s·Q·G_i.
- Eq. 3 (hal. 4): **tundaan total d = w·Σ_i q_i** (luas antara profil kedatangan & keberangkatan).
- Eq. 4 (hal. 4–5): stops S_i = N_i·(1 − G_i) bila q_i = 0; S_i = N_i bila q_i > 0.
- Eq. 5 (hal. 5): indeks kinerja PI = d + k·Σ S_i (k = 20 detik/stop, gaya TRANSYT).
- **Eq. 6 (hal. 5): AOG N_g = Σ_i G_i·N_i** ("dot product" vektor G dan N).
- Objektif IV (hal. 5): AOG dengan **queue clearance** — 10 detik pertama pita hijau dianggap merah saat optimasi agar antrian sisa terbersihkan sebelum platoon utama tiba. Hasil (hal. 18 dst.): keempat objektif memberi perbaikan sebanding; objektif AOG paling sederhana & tanpa asumsi arus jenuh.

### B.4 Algoritma Link Pivot — poster ATSPM Workshop 2016 (Day, Lavrenz, Stevens, Miller, Bullock, TRB 16-0111, "Extending Link Pivot Offset Optimization to Arterials with Single Controller Diverging Diamond Interchange", Purdue e-Pubs atspmw/2016/Posters/12; 2 hal.) — mengutip Day & Bullock 2011 (doi 10.3141/2259-04), berbasis "Combination Method" 1960-an
Diagram alir "Link Pivot Algorithm for a Simple Arterial Corridor" (poster hal. 1):
1. Tentukan simpang awal j0 dan akhir j_max; set j = j0.
2. Untuk simpang j: δ = 0; hitung tundaan awal d_base pada **link j→j+1 untuk dua arah** (dari PCD/profil kedatangan kedua pendekat link tersebut, dengan kedatangan digeser +δ untuk arah hilir dan −δ untuk arah hulu — "pivot" pada link).
3. Tambahkan δ ke **semua offset dari j0 sampai j** dan hitung tundaan d_δ (atau, dalam objektif AOG, hitung N_g); jika d_δ < d_base simpan δ, jika tidak buang; δ = δ + 1; ulangi sampai δ > C − 1 (uji seluruh siklus).
4. j = j + 1; kembali ke langkah 2 sampai j = j_max; selesai.
5. Akumulasi (tampilan "graph-theoretical", poster hal. 1): dengan increment optimal per link δ1, δ2, δ3 dan penyesuaian global opsional x, offset akhir a_1 = δ1 + δ2 + δ3 + x; a_2 = δ2 + δ3 + x; a_3 = δ3 + x (simpang hilir menerima jumlah semua increment link di hilirnya). Prinsip: "Previously optimized link flows are preserved by adding new adjustments to all of the previously optimized intersections".
6. Rumus pembaruan: **O_new = (O_old + Δ) mod C**; untuk diamond satu kontroler: O[Ring2] = (O[Ring1] + R) mod C, R_new = (R_old − Δ_Ring1 + Δ_Ring2) mod C.
Definisi "link delta" (rekonstruksi dari langkah 2–3): δ_j* = arg max_δ [AOG_hilir(δ) + AOG_hulu(−δ)] atau arg min tundaan gabungan dua arah pada link j; kompleksitas O(n·C) evaluasi profil — deterministik (alasan Day & Bullock 2011 merekomendasikannya dibanding GA/hill-climbing; abstrak TRR 2259-04). Bukti lapangan poster (hal. 2): AOG naik mis. 68,6 % → 83,9–90,5 % per pendekat SR 1 Fort Wayne.
Implikasi IRAMA: Link Pivot = kandidat algoritma optimasi offset **T2** (butuh hi-res event + detektor setback per pendekat koordinasi); objektif AOG (B.3 Eq. 6) sebagai default, varian queue-clearance untuk simpang jenuh (Kircon); input dapat diganti data probe/CV (Day & Bullock 2016, civeng/26) untuk simpang tanpa detektor (T4).

### B.5 Repositori kode terbuka ATSPM UDOT (GitHub)
- `github.com/udotdevelopment/ATSPM` — v4.3 ke bawah, **deprecated**; lisensi Apache-2.0; .NET/C#/ASP.NET + SQL Server; 20 bintang (per 2026-08). Struktur modul (pohon repo via API, disimpan `02_.../ATSPM_UDOT_GitHub_tree_v4_api.json`): **SPM** (situs web utama) + SPMUserAndRoleManagement, SPMWatchDogNew; **MOE.Common** (model & logika inti, + ModelGenerator, ChartTests); **ATSPM.Application.Business / .Reports**, **ATSPM.Models**, **ATSPM.IRepositories**, **ATSPM.Repositories.EntityFramework**, **AtspmApi**; **dekoder log kontroler per vendor**: DecodeASC3Logs, DecodeSiemensLogs, DecodePeekLogs, DecodeTrafficwareLogs, ASCLogCSVreader, FileByFileASC3Decoder, ProducerConsumerASC3Import, GetMaxTimeRecords/AsyncGetMaxTimeRecords (Intelight MaxTime), WavetronicsSpeedListener; **pengumpul data**: FTPfromasc3, FTPFromOneController, FTPTimerService, FTPSClient; **agregasi** (AggregateApproachCycle, ApproachEvent, ApproachPCDCycle, ApproachSpeed, ApproachSplitFail, DetectorEventCount, LeftTurnGap, SignalEventData, SignalPedDelay, SignalPhaseTermination, SignalPlan, SignalPreemptPriority, SplitMonitor, TurningMovementCounts, YellowRedActivation); alat: LeftTurnReport(+API), InrixConfigurationTool, ImportChecker, ConvertDBForHistoricalConfigurations, Installer/BuildDeployPackage; dokumen keamanan (OWASP/CWE/Fortify report).
- `github.com/OpenSourceTransportation/Atspm` — **v5** (aktif; pembaruan terakhir 2026-08-25); monorepo `Atspm/` (disimpan `..._tree_v5_Atspm_dir_api.json`): **Application** (domain/logika), **Infrastructure**, **Data**, layanan API terpisah **ConfigApi / DataApi / ReportApi / IdentityApi**, **WebUI** (front-end), **WatchDog**, **EventLogUtility**, **DeviceEmulator**, **DatabaseInstaller**, penyedia basis data **SqlDatabaseProvider / PostgreSQLDatabaseProvider / MySqlDatabaseProvider / OracleDatabaseProvider / SqlLiteDatabaseProvider**, `docker-compose.yml` + nginx + pure-ftpd; masing-masing dengan proyek *Tests. README v5 tidak terambil (1 byte via raw; README ada di dalam `Atspm/`).
- Implikasi: v5 = arsitektur layanan (config/data/report/identity) + multi-DB + Docker — pola yang cocok ditiru IRAMA (PostgreSQL/TimescaleDB, kontainer); dekoder per vendor v4 = daftar format log kontroler yang perlu didukung (ASC/3, Siemens, Peek, Trafficware, MaxTime) bila kontroler impor dipakai; untuk kontroler lokal (Qumicon/Javis) perlu adaptor sendiri.

---

## C. Profil data kota pilot Bandung & kandidat koridor pilot

### C.1 Fakta kunci (bertag sumber di `08_Data_Kota_Pilot_Bandung/`)
| Aspek | Temuan | Sumber |
|---|---|---|
| Jumlah APILL | **150 titik lampu lalu lintas** (data kondisi APILL Dishub 2022; mayoritas simpang empat, ada simpang lima/tiga/ruas) — artikel menyebut "seluruh titik … termasuk kategori ATCS" | Teks_detik_150_titik (12-07-2025) |
| Simpang terhubung ATCS | Kadishub Rasdian Setiadi (23-07-2026): 150 APILL, "**66 simpang telah dilengkapi CCTV yang terhubung langsung ke pusat kendali ATCS**"; ATCS terhubung dalam **4 trase (utara, timur, selatan, barat)**; beberapa titik berpengeras suara; prioritas ambulans/damkar/VVIP diatur dari pusat; beberapa CCTV rusak akibat galian utilitas (Jl. Aceh, Jl. R.E. Martadinata) | Teks_tribun_66_simpang |
| Portal publik | atcs-dishub.bandung.go.id: **24 lokasi simpang berkamera publik, 46 kamera** (SP = kamera simpang; VID = kamera per pendekat, 2–4 arah di Gedebage, Samsat/Kircon, Buah Batu, Batununggal, M. Toha, Tol Pasteur, Paskal–RSHS); koordinat tersedia (CSV/JSON) | ATCS_Bandung_lokasi_kamera_portal_2026-09-12.csv; Teks_atcs_portal |
| Ruang kendali | **Balai Kota Bandung, Jl. Wastukencana No. 2** (Gedung Barat lt. 3 menurut cuplikan pencarian; govserv.org & serbabandung menyebut Balai Kota) | Teks_serbabandung_atcs (26-12-2023) |
| Komponen sistem (deskripsi resmi) | Server & workstation, wall map, local controller, video surveillance, **vehicle detector "yang mendeteksi kendaraan yang terpantau melalui kamera CCTV"** (deteksi berbasis video), fungsi responsif & terkoordinasi, prioritas kendaraan hak utama (UU 22/2009 Ps.134), informasi rute alternatif, rekaman data lalu lintas/kecelakaan, dukungan TMB | Teks_atcs_portal |
| Vendor/merek | **Tidak disebut** di semua sumber yang terambil (portal, berita, pencarian LPSE). Diketahui: BEMO (pelacakan TMB) dikembangkan **LSKK** (perusahaan lokal Bandung); GSI Indonesia (artikel 2026) hanya vendor CCTV umum. KB-09 mencatat vendor nasional Qumicon/Javis untuk kota lain, bukan Bandung. | Teks_lskk_bemo; Teks_gsi_cctv_atcs; `_urls.tsv` |
| Status teknologi 2026 | Wali Kota Farhan (17-04-2026): ATCS "**masih belum full menggunakan AI, masih semi manual**", teknologi "sudah mulai usang", **belum ada satu pun lampu lalu lintas ber-AI**; rencana upgrade AI, prioritas **pintu masuk/perbatasan kota** & titik rawan macet, tahap awal lalu diperluas; kajian infrastruktur & jaringan (Mei 2026); PRFM (keterangan foto 4-2-2026): "uji coba AI pada traffic light sejak akhir 2025, terutama Pasteur" | Teks_kompas_atcs_ai_2026; Teks_radar_ai_titik_krusial_2026; Teks_radar_ai_mulai_dipakai_2026; Teks_jabarekspres_ai_2026; Teks_prfm_ai |
| Tekanan politik | Gubernur Jabar Dedi Mulyadi (11-07-2025): traffic light "justru bikin macet", analisis pengaturan waktu; Stopan Kircon (Soekarno-Hatta–Ibrahim Adjie) merah ±410 dtk vs hijau 80–90 dtk (pengukuran detikJabar) | Teks_detik_150_titik |
| Kemacetan | TomTom 2024: Bandung **#1 Indonesia**, 32 mnt 37 dtk per 10 km; > 2,5 juta kendaraan; Wali Kota: 3 titik utama = Soekarno-Hatta barat–timur (06–10 & 16–19), A. Yani–A.H. Nasution, tiga ruas ke utara (Dago/Ir. H. Juanda, Sukajadi, Setiabudi) sore 16–19 | Teks_ayobandung_farhan (11-12-2025) |
| Titik rawan macet Dishub (Nataru 2024/25, 16 titik) | Surya Sumantri–Dr. Djunjunan (**Pasteur**), Sukajadi (PVJ), Setiabudi (Ledeng), Cipaganti–Setiabudi, Cihampelas, Soekarno-Hatta–Kopo, Tamblong–Asia Afrika–Braga, Soekarno-Hatta–M. Toha, –Buahbatu, –Bundaran Cibiru, –Kircon (Samsat), A. Yani (Cicaheum), Dago Bengkok, Jajaway, Pusdai–Suci, Cimencrang–Darwati | Teks_sonora_16_titik; Teks_strategi_titik_macet; Teks_detik_nataru_16 |
| Titik rawan Polrestabes (Nataru 2025/26, 18) | Sukajadi/PVJ, Setiabudhi, Cihampelas, Tamblong, Soekarno-Hatta (M. Toha, Buah Batu, Kircon), Gatot Subroto–Pelajar Pejuang, Cimencrang–Darwati, … | Teks_pr_18_jalur |
| DPRD (2022/23) | "**45 titik persimpangan** yang mengalami kemacetan" (Jl. Jakarta, M. Toha, Pasteur, Kopo, rekayasa Sukajadi–Cipaganti); 250 petugas gatur | Teks_jabarnews_macet |
| Trans Metro Bandung (TMB) | Operator **BLUD UPTD Angkutan Dishub Kota Bandung**; sejak 23-09-2009; **5 koridor utama + 2 feeder**; tarif Rp4.000/Rp2.000 (QRIS Rp3.000/Rp1.000). Rute: K1 Cibiru–Cibeureum via **Soekarno-Hatta**; K2 Cicaheum–Cibeureum via A. Yani–Ibrahim Adjie–Jl. Jakarta–Asia Afrika–Sudirman; K3 Cicaheum–Sarijadi via **A. Yani–PHH Mustofa–Surapati–Cikapayang–Flyover Pasupati–Dr. Djunjunan–Surya Sumantri**; K4 Antapani–Leuwipanjang via Laswi–Pelajar Pejuang–BKR–Kopo–Soekarno-Hatta; K5 Antapani–Stasiun Hall via Martadinata–Merdeka–Lembong–Tamblong–Asia Afrika; Feeder 1 Stasiun Hall–Gunung Batu via Wastukencana–Cihampelas–Pasteur; Feeder 2 Summarecon–Elang. Jam operasi ±05.00–17.30. | Teks_uptangkutan_tmb; Teks_wiki_tmb |
| AVL/GPS publik | **BEMO – Bandung Easy Mobility** (bemo.uptangkutan-bandung.id; Android/iOS): posisi real-time TMB, Bandros, bus sekolah, halte, rute — dikembangkan LSKK. **Tidak ada feed GTFS/GTFS-RT publik terdokumentasi** (Wikipedia & situs BEMO tidak menyebut; MobilityDatabase tidak terverifikasi). | Teks_wiki_tmb; Teks_lskk_bemo; raw_bemo.html |
| Metro Jabar Trans (BRT Bandung Raya) | Pemprov Jabar, skema Buy-the-Service Kemenhub, beroperasi 21-12-2021 (eks Trans Metro Pasundan, rebranding 1-1-2025); **6 koridor + 2 feeder** (Leuwipanjang–Soreang, Kota Baru Parahyangan–Alun-alun, Dipatiukur–Jatinangor, Simpang Soetta Kiaracondong–Pasar Baru ABC, Simpang Cicadas Kiaracondong–Plaza Telkom Rajawali, dll.); tarif Rp4.900; PIS live tracking mjt.trans.my.id (web/aplikasi MitraDarat) | Teks_wiki_mjt; raw_mjt_live.html |
| Open data | opendata.bandung.go.id memiliki dataset "Kondisi APILL di Kota Bandung" dan "Lokasi CCTV ATCS Kota Bandung" (Dishub) tetapi halaman berbasis Tableau/JS — **tabel tidak terambil**; katalog.data.go.id "Data Lampu Lalu Lintas Terintegrasi ITS-ATCS" timeout; data.bandung.go.id/atcs 400/500 | `_urls.tsv` |
| Kerentanan | Mei 2026: ±20 kamera Pasteur–Tamansari mati karena node penghubung dirusak (arsip 07); Juli 2026: CCTV Jl. Aceh & Martadinata rusak galian utilitas | 07/Teks_bandung_20_cctv_atcs_rusak_2026; Teks_tribun_66_simpang |

### C.2 Jarak antar-simpang ATCS (haversine dari koordinat portal; garis lurus, ±5–10 % lebih pendek dari jarak jalan)
- **Soekarno-Hatta** (barat→timur): Caringin →1.279 m→ Cibaduyut →813 m→ Inhoftank →754 m→ M. Toha →1.839 m→ Batununggal →845 m→ Buah Batu →967 m→ Ibrahim Adjie (Kircon) →5.684 m→ Gedebage.
- **Pasteur–Cikapayang–Dago**: Tol Pasteur/Surya Sumantri →1.988 m→ HOS Tjokroaminoto (Paskal–RSHS) →540 m→ Cipaganti →215 m→ Cihampelas →629 m→ Tamansari–Cikapayang →357 m→ Djuanda–Cikapayang →136 m→ Djuanda–Sulanjana →750 m→ Surapati–Sentot Alibasa (Telkom).
- **PHH Mustofa (Suci)**: Pahlawan →1.046 m→ Cikutra →738 m→ Cimuncang →412 m→ Padasuka →163 m→ A. Yani (Cicaheum).
- **Pusat kota**: Djuanda–Sulanjana →1.091 m→ Aceh–Merdeka →942 m→ Lembong–Sumatera →435 m→ Tamblong–Asia Afrika.

### C.3 Kandidat koridor pilot (3–5 simpang, jarak ≤ 1 km)
| # | Koridor | Simpang (jarak) | Alasan memilih | Risiko/catatan |
|---|---|---|---|---|
| **K-A (utama)** | **Pasteur–Cikapayang–Dago** (Jl. Dr. Djunjunan/Pasteur → Cikapayang → Ir. H. Juanda) | Paskal–RSHS → Cipaganti (540 m) → Cihampelas (215 m) → Tamansari–Cikapayang (629 m) → Djuanda–Cikapayang (357 m) → Djuanda–Sulanjana (136 m): **6 simpang, ±1,9 km**, semua ≤ 1 km | (1) Titik rawan macet Dishub & Polrestabes (Pasteur, Cihampelas, Cipaganti) dan ruas "ke utara/Dago" versi Wali Kota; (2) **lokasi uji coba AI Dishub sejak akhir 2025 (Pasteur)** → dukungan politik & pembanding before/after; (3) dilalui **TMB K3 & Feeder 1** → TSP; (4) semua simpang sudah berkamera & terhubung ("trase" Pasteur–Tamansari); (5) jarak pendek → koordinasi/Link Pivot efektif (platoon utuh); (6) akses wisata akhir pekan (Dago/Cihampelas) = kasus pola waktu. | Node komunikasi pernah dirusak (Mei 2026) → perlu redundansi; flyover Pasupati di atas Cikapayang & satu-arah sebagian (Cihampelas/Cipaganti) → model fase khusus; status jalan Dr. Djunjunan perlu dicek (kemungkinan nasional/provinsi → persetujuan Ps.20 Perda Jabar / PM 96/2015). |
| **K-B** | **Soekarno-Hatta timur** (Batununggal → Buah Batu → Ibrahim Adjie/Kircon) | 3 simpang: 845 m + 967 m (**±1,8 km**); opsi perluasan barat ke M. Toha (+1.839 m, di luar ambang) | (1) **Stopan Kircon** = simbol keluhan publik (merah 410 dtk) & sorotan Gubernur → dampak politik terbesar; (2) simpang dengan kamera per pendekat (VID 3–4 arah) → deteksi video per pendekat tersedia; (3) **TMB K1** & MJT (Simpang Soetta Kiaracondong) lewat → TSP; (4) arteri primer volume tertinggi (jam puncak 06–10, 16–19). | Soekarno-Hatta kemungkinan **jalan nasional** (Kadishub: CCTV aktif "di jalan nasional") → MRLL butuh persetujuan Dirjen/BPTD; simpang jenuh → objektif AOG perlu varian queue-clearance; jarak antar-simpang mendekati 1 km → dispersi platoon. |
| **K-C** | **Soekarno-Hatta barat / Kopo** (Cibaduyut → Inhoftank → M. Toha) | 3 simpang: 813 m + 754 m (**±1,6 km**) | Titik macet Kopo & M. Toha (Dishub/DPRD/Polrestabes); TMB K1/K4; flyover Kopo dan U-turn bawah flyover (DPRD minta evaluasi efektivitas) = kasus evaluasi rekayasa berbasis data. | Sama seperti K-B (status jalan nasional); kamera hanya SP (bukan per pendekat) di Cibaduyut/Inhoftank → perlu tambahan detektor. |
| K-D (cadangan) | **PHH Mustofa/Suci** (Cikutra → Cimuncang → Padasuka → Cicaheum) | 4 simpang: 738 + 412 + 163 m (**±1,3 km**) | Titik "Pusdai–Suci" & A. Yani/Cicaheum (Dishub); TMB K2/K3 (Cicaheum) → TSP; jalan kota (kewenangan penuh Pemkot, tanpa persetujuan provinsi/nasional). | Hanya kamera SP; Padasuka–Cicaheum 163 m (simpang berdekatan → satu kontroler/overlap). |

Rekomendasi: **K-A sebagai pilot T1–T2** (kewenangan lebih sederhana bila ruas kota, momentum uji coba AI, TSP siap), **K-B sebagai showcase T2–T3** setelah persetujuan pengelola jalan nasional; K-D cadangan bila kewenangan menjadi kendala.

---

## D. Kegagalan unduhan & workaround
| Sasaran | Masalah | Workaround/substitusi |
|---|---|---|
| Perda Kota Bandung 16/2012 (+ perubahan 4/2017, 3/2020) | Ternyata **dicabut** oleh Perda 12/2024 | Diunduh Perda 12/2024 (utuh); 16/2012 disimpan sebagai arsip historis (nama file berakhiran _DICABUT); 4/2017 & 3/2020 tidak disimpan |
| Perda Jabar 3/2011 & 4/2017 | Dicabut Perda Jabar 5/2024 | Diunduh Perda 5/2024 |
| Perwal Bandung 20/2023 SPBE | PDF scan (JDIH = BPK), tanpa OCR (tesseract/ocrmypdf tidak terpasang) | Abstrak BPK; rujukan Perwal 29/2023 (keamanan informasi), 28/2023 (arsitektur), 31/2023 (peta rencana) dicatat untuk unduhan lanjutan; induk Perpres 95/2018 |
| Pergub DKI 25/2017 ERP | Sudah dicabut (Pergub 20/2022) | Keduanya diunduh; dipakai sebagai pola desain, bukan hukum berlaku |
| Pergub DKI turunan MRLL | Tidak ditemukan | Pergub 68/2021 (sudah di korpus) + PP 32/2011 |
| Permenhub PM 67/2021 | Tidak relevan (Ortaker Kemenhub) | Dilewati |
| Kep. Dirjen SK.326/KP.108/DRJD/2018 (APILL persimpangan berdiri sendiri) | JDIH Kemenhub: pencarian kosong / WAF; tidak ada salinan publik | Kutipan tesis PTDI-STTD (kriteria pemasangan, definisi siklus) + Kep. Dirjen 273/1996 + PKJI 2023 |
| Perdirjen "tata cara penentuan waktu siklus" | Tidak ada dokumen dengan judul tsb. | Idem; amanat PM 49/2014 tidak dapat diverifikasi dari teks ekstraksi (label pasal hilang) |
| Day & Bullock 2011 TRR 2259-04 (Link Pivot) | Paywall SAGE; PURR hanya animasi 84 MB | Poster ATSPMW 2016 + TRB 11-0036 (civeng/10) + JTRP 2008/2014 |
| Purdue civeng/25 (paper DDI penuh), udottraffic ATSPM_Reporting_Details.pdf, MDPI 2022 | 403 | Poster 2 hal. (memuat diagram alir & rumus); FHWA-HOP-20-002 di korpus |
| Python `urllib`/`requests` di scratchpad | `requests` tidak terpasang; path > 260 karakter (MAX_PATH) membuat `open()`/`pdftotext` gagal | Unduh dengan curl (loop dari TSV); ekstraksi setelah dipindah ke folder proyek (path lebih pendek) |
| data.bandung.go.id/atcs, katalog.data.go.id | 400/500, timeout | Endpoint AJAX portal ATCS (`/ajax/lokasi`, `/ajax/cctv-list`) → 24 lokasi/46 kamera + koordinat |
| opendata.bandung.go.id (Kondisi APILL; Lokasi CCTV ATCS) | SPA/Tableau, data tidak dalam HTML | Angka agregat dari berita (150 APILL, 66 simpang); dataset dicatat untuk pengambilan manual/Playwright |
| pasjabar "6 kawasan termacet" | 404 | Daftar titik dari Dishub/Polrestabes/AyoBandung |
| Vendor/merek ATCS Bandung | Tidak disebut di sumber daring; LPSE tidak terindeks | Dicatat sebagai pertanyaan terbuka untuk kunjungan lapangan/PPID |
| README ATSPM v5 | raw README 1 byte (README ada di subfolder) | Pohon direktori via API GitHub (disimpan) |
