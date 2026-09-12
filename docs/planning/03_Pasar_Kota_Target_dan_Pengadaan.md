# 03 — Pasar, Kota Target, dan Jalur Pengadaan

Status: draf pra-perencanaan (2026-09-12). Tag sumber: [KB] = docs/sources/_ringkasan (R00–R06); [W] = hasil pencarian web sesi ini (URL di catatan kaki tiap bagian); [A] = **asumsi** yang harus divalidasi. Angka tanpa sumber diberi tag [A].

## 1. Segmentasi pasar

| Segmen | Contoh | Ciri kebutuhan | Kapasitas bayar & jalur | Prioritas |
|---|---|---|---|---|
| **Kota metropolitan non-DKI** | Bandung, Medan, Surabaya, Palembang (juga Semarang, Makassar, Yogyakarta) | Sudah punya ATCS/CC-Room generasi CCTV+koordinasi TOD; ingin "adaptif/AI" seperti DKI; kendala detektor rusak, SDM, pemeliharaan [KB R06 E] | APBD kota (Dishub), DAK/hibah Kemenhub [W-3]; e-katalog | **1** — urgensi tertinggi (TomTom 2024: 4 kota di atas Jakarta) |
| **Bodetabek** | Kota Bekasi, Depok, Bogor, Tangerang, Tangsel; Kab. Bogor, Tangerang, Bekasi | ATCS kecil (5–40 simpang), banyak simpang masih statis; koordinasi lintas batas dengan DKI (rapat sinkronisasi ATCS Jabodetabek 2022) [W-3]; jalan nasional di bawah BPTJ [KB R00 C] | APBD kota/kab lebih kecil; cocok paket pilot koridor & SaaS | **2** — pintu masuk cepat, referensi dekat DKI |
| **Pemprov** (Jabar, Jatim, Sumut, Sumsel, Banten) | Dishub provinsi | Jalan provinsi lintas kota; koordinasi antar-kota; monev regional | APBD provinsi | 3 |
| **BPTJ / Ditjen Hubdat Kemenhub** | ATCS jalan nasional Jabodetabek; hibah ATCS ke kota | Standardisasi, interoperabilitas, monev nasional; program RITJ pilar 6 "Pembangunan & Pengembangan ATCS" [KB R05 A.8] | APBN | 3 (jalur pengaruh & standar) |
| **Pengelola kawasan/tol/BUMD** | Jasa Marga, Hutama Karya, kawasan industri, TransJakarta/BUMD transit | Data arus menuju gerbang, prioritas bus, simpang akses kawasan | Korporasi | 4 (mitra data, bukan pembeli awal) |

## 2. Profil urgensi kota target

| Kota | Kemacetan (TomTom 2024) | Status ATCS yang diketahui | Kendala/celah yang diberitakan | Peluang masuk |
|---|---|---|---|---|
| **Bandung** | **#12 dunia, #1 Indonesia**; 10 km = 32 mnt 37 dtk [W-1] | ATCS Dishub dengan CC-Room di Balai Kota; portal CCTV publik; sejarah SCATS (Telnic→Marktel, dukungan SCATS dihentikan, sistem proprietary) [W-2, W-6] | Sistem warisan proprietary; fokus CCTV; jumlah simpang adaptif & kondisi detektor tidak dipublikasikan [A] | Lapisan adaptif + KPI di atas controller eksisting; kota paling "malu" secara ranking → urgensi politik tinggi |
| **Medan** | **#15 dunia, #2 Indonesia** [W-1] | ATCS Dishub Medan (portal atcsdishub.pemkomedan.go.id, medsos aktif); ITS dengan sinkronisasi timing + CCTV [W-2] | Detail jumlah simpang & mode kendali tidak dipublikasikan [A]; LRT direncanakan | Sama dengan Bandung; kota besar tanpa vendor dominan yang terlihat |
| **Surabaya** | #3 Indonesia [W-1] | **SITS** (Surabaya Intelligent Transport System) sejak ±2010-an; >90 titik CCTV; akun "SITS ATCS Surabaya"; pernah memakai sensor FLIR TrafiCam [W-2, W-6] | Sistem matang → bar masuk lebih tinggi; kebutuhan: analitik/ATSPM, prioritas Trans Semanggi/BRT | Modul analitik & evaluasi (bukan pengganti ATCS); kompetisi dengan vendor petahana |
| **Palembang** | #4 Indonesia [W-1] | 15 simpang utama terkoneksi ATCS terpusat di Dishub (Bandara, Tanjung Api-Api, Angkatan 45, Jakabaring, dsb.) [W-2] | Cakupan kecil; LRT ada tetapi prioritas simpang belum | Paket "dari 15 ke 50 simpang" bertahap |
| **Jakarta (DKI)** | #5 Indonesia, #90 dunia [KB R06 D] | ITCS 65/321 simpang; Rp120 M untuk 25 simpang 2025; vendor TKDN [KB] | Sudah punya vendor & anggaran besar | Bukan target awal; jadi *benchmark* dan mitra data koridor lintas batas |
| **Bekasi (kota)** | — | Ruang ATCS baru (Maret 2023), 120 CCTV [W-3] | Fokus CCTV; adaptif belum jelas [A] | Pilot koridor perbatasan DKI–Bekasi |
| **Depok** | — | 110 CCTV di 40 titik; integrasi ke aplikasi SIMDISHUB [W-5] | Sama: CCTV-first | Pilot koridor Margonda [A] |
| **Tangerang (kota)** | — | Inovasi optimalisasi ATCS diklaim sukses (Smart City Tangerang) [W-3] | — | Referensi keberhasilan lokal |
| **Tangsel** | — | ATCS 3 unit (2016) + 2 unit; CCTV online publik [W-5] | Cakupan sangat kecil | Pilot murah |
| **Kab. Tangerang / Kab. Bogor** | — | Uji coba APILL ATCS Pasar Kemis; dashboard CCTV; Kab. Bogor tuan rumah sinkronisasi ATCS Jabodetabek [W-3, W-5] | Simpang tersebar, jarak antar simpang >1 km (syarat ATCS PM 96 tidak terpenuhi di banyak lokasi) | Mode "APILL otonom adaptif" per simpang [KB R00 E] |
| Lainnya (Yogyakarta, Surakarta, Kudus, Bukittinggi) | — | Yogya target seluruh simpang ber-ATCS 2025 (38 simpang), Rp350–400 jt/simpang; Surakarta punya paket ATCS di e-katalog; Kudus Rp1,3–1,8 M/simpang; Bukittinggi hibah Kemenhub Rp9,4 M [W-3, W-4] | Harga per simpang sangat bervariasi → pasar belum terstandar | Bukti bahwa pemda kecil pun membeli ATCS |

Catatan: data jumlah simpang ber-ATCS per kota untuk 2024–2025 tidak tersedia publik dalam pencarian; harus divalidasi lewat kunjungan/permintaan data ke Dishub (lihat 08 Pertanyaan Terbuka).

## 3. Siapa membeli dan memutuskan (buying center Dishub kota)

| Peran | Kepentingan | Pengaruh | Pesan yang tepat |
|---|---|---|---|
| **Kepala Dinas Perhubungan** | Kinerja politik (ranking macet, keluhan), realisasi anggaran, inovasi (proyek perubahan/PKN) [KB majalah] | Sangat tinggi (pengguna anggaran) | Hasil terukur dalam 6–12 bulan; branding; kepatuhan regulasi |
| **Kabid Lalu Lintas / Kabid Pengendalian & Operasional** | Operasi harian, keluhan warga, koordinasi Polantas | Tinggi (penyusun KAK) | Alat kerja yang mengurangi beban; KPI otomatis; fallback aman |
| **Kepala UP/UPTD Pengendali Lalu Lintas / CC-Room** | Sistem berjalan 24/7, perangkat sehat, SDM | Tinggi (pengguna utama) | Kesehatan perangkat, kemudahan operator, tidak black-box |
| **Bappeda / Bapperida** | Kesesuaian RPJMD/RKPD, Renstra, indikator kinerja | Tinggi (gerbang anggaran) | Indikator (kecepatan rata-rata, LOS) sesuai PM 96; program prioritas smart city |
| **Diskominfo / Smart City** | Integrasi data, hosting, keamanan, portal publik | Sedang–tinggi (hosting & SPBE) | Interoperabilitas, API terbuka, SPBE, hosting di infrastruktur pemda |
| **DPRD (Komisi perhubungan) & Inspektorat/BPK** | Akuntabilitas belanja, dampak nyata [KB R06 D kritik DPRD] | Sedang (persetujuan anggaran) | Bukti before–after, biaya per simpang transparan |
| **Ditlantas Polda / Satlantas Polres** | Penegakan hukum, TMC, pengaturan situasional (kewenangan operasional MRLL, UU Ps.7/12) [KB R05] | Tinggi sebagai mitra wajib | Integrasi ke pusat kendali Polri, override petugas, dukungan ETLE (bukti) |
| **ULP/UKPBJ & Bagian Hukum** | Kepatuhan Perpres PBJ, TKDN, e-katalog | Gerbang prosedural | Produk tayang di e-katalog, sertifikat TKDN/BMP |
| **Operator angkutan (BUMD bus/BRT), Damkar, RS/AGD** | Prioritas & preemption | Rendah–sedang (pendukung) | Manfaat langsung: headway, response time |

## 4. Jalur pengadaan yang realistis

| Jalur | Cocok untuk | Syarat/kendala | Catatan sumber |
|---|---|---|---|
| **E-katalog LKPP / INAPROC (katalog elektronik nasional/lokal/sektoral)** | Lisensi software + jasa implementasi per simpang; paket ATCS (contoh: produk "Area Traffic Control System (ATCS) Pemerintah Daerah Kota Surakarta", "Traffic Controller ATCS/ITS 8 SG", "Kit Mainboard APILL ATCS") [W-4] | Penyedia harus tayang (etalase produk/jasa TI), harga dan spesifikasi terbuka; pemda memilih via e-purchasing tanpa tender → **jalur utama**; prioritas produk TKDN+BMP ≥40% (wajib beli PDN bila TKDN ≥25%) [W-2 Perpres 46/2025, PP 29/2018] | Tayang di etalase "Perangkat Lunak/Aplikasi" dan "Perlengkapan Jalan/ATCS" |
| **Tender/seleksi (jasa konsultansi & pengadaan sistem)** | Proyek besar (>Rp200 jt jasa; paket integrasi kota) | Kompetitif; risiko low-bid (peringatan FHWA HOP-11-027 [KB R02]) | Dorong RFP best-value + spesifikasi NTCIP terbuka |
| **Swakelola / kerja sama (Perda 5/2014 Ps.239; Pergub 68 Ps.7)** | Pilot/riset dengan perguruan tinggi/BUMD; PoC gratis | Butuh payung hukum (PKS), bukan pendapatan langsung | Pintu masuk pilot 3–5 simpang |
| **Hibah/bantuan Kemenhub (DAK, bantuan ATCS)** | Kota sedang (Bukittinggi Rp9,4 M 2019–2020) [W-3] | Spesifikasi ditentukan Kemenhub; vendor dipilih pusat | Ikut standar Ditjen Hubdat (SK.7234/2013, PM 49 Ps.25 sertifikasi) |
| **KPBU / kerja sama pemanfaatan** | Skala provinsi/kota besar dengan ERP | Kompleks, lama | Tahap 4–5 saja |
| **Penjualan ke vendor/integrator (B2B2G)** | Menjadi lapisan software di atas paket vendor controller lokal (Javis, Qumicon, TKDN, Marktel, dsb.) | Bergantung mitra; margin kecil | Alternatif bila belum tayang e-katalog |

**Persyaratan kepatuhan produk** (dari bahan acuan): perangkat TI di APILL harus bersertifikat (PM 49/2014 Ps.25) [KB R00 B]; spesifikasi controller/detektor/DIS SK.7234/2013 [KB R00 H]; sistem terbuka & berstandar (PM 76/2021 Ps.4) [KB R00 C]; NTCIP 1202/1211 sebagai standar interoperabilitas [KB R02, R03]; keamanan data (Pergub 68 Ps.10(7), UU PDP) [KB R05]; **TKDN**: software buatan lokal dapat mengajukan sertifikat TKDN (jasa/software) untuk memenuhi preferensi PDN [W-2]; SNI/TDBU relevan untuk perangkat keras, bukan software [A].

**Siklus anggaran APBD (Permendagri 86/2017 & 77/2020)** [W-2b]: rancangan awal RKPD mulai Desember dua tahun sebelum tahun anggaran; rancangan RKPD kab/kota selesai minggu I April; KUA-PPAS ke DPRD paling lambat pertengahan Juni; RAPBD dibahas Agustus–November; APBD ditetapkan Desember. **Implikasi:** untuk masuk APBD tahun N+1, kegiatan harus sudah ada di Renja Dishub & RKPD paling lambat **Januari–Maret tahun N** (musrenbang/forum OPD); jendela pendekatan terbaik: **Oktober–Februari**. Alternatif lebih cepat: APBD Perubahan (pembahasan ±Agustus–September) untuk paket kecil, atau e-purchasing dari anggaran "pemeliharaan/pengembangan ATCS" yang sudah ada.

## 5. Pesaing dan substitusi

| Kelompok | Nama (yang terverifikasi di pencarian) | Kekuatan | Kelemahan yang bisa dimanfaatkan |
|---|---|---|---|
| Vendor ATCS lokal (hardware + software) | **PT Javis Teknologi Albarokah** (ATMS, VID AI Detector, APILL otonom cerdas, prioritas bus; ISO/SNI/TKDN/TDBU; 100+ proyek) [W-4]; **PT Qumicon Indonesia** (ATCS, CC-Room) [W-4]; **PT Teknologi Karya Digital Nusa (TKDN)** — ITCS DKI, APILL Gen-5 digital twin [KB R06]; **Marktel** (eks-Telnic, sistem proprietary, Bandung/Jakarta) [W-6]; PT Firza Meka Trindo (traffic light ATCS) [W-4] | Punya controller & etalase e-katalog; TKDN; relasi Dishub; paket turnkey | Proprietary/black-box; software analitik lemah [A]; KPI jarang berbasis PKJI/PM 96; lock-in |
| Vendor global | SCATS (dulu via Telnic), SCOOT/Siemens (kini Yunex Traffic), SWARCO; FLIR TrafiCam (sensor) [W-6] | Terbukti global | Mahal, dukungan lokal terputus (kasus SCATS Bandung/Jakarta) [W-6] |
| Perguruan tinggi/riset | Smart City UI "Adaptive Traffic Monitoring System" [W-6] | Murah, inovatif | Bukan produk berkelanjutan |
| **Substitusi** | "CCTV saja" + operator manual; retiming manual berkala; tidak melakukan apa-apa | Murah, sudah ada | Tidak adaptif; tidak ada KPI; keluhan sebagai ukuran kinerja (TSPH) [KB R02] |

## 6. Proposisi nilai pembeda (dari bukti bahan acuan)

1. **Berdiri di atas controller eksisting** (NTCIP 1202 + adaptor RS-232 vendor) — tidak memaksa ganti APILL; biaya per simpang jauh di bawah paket turnkey Rp350 jt–1,8 M [W-4] [A: target biaya software < 20% biaya paket].
2. **Fallback wajib & aman**: ≥8 rencana TOD, degradasi otomatis (PM 49 Ps.14; FHWA HOP-11-027 Req 2.1.1) — menjawab kendala #1 ATCS Indonesia (detektor/komunikasi rusak) [KB R02, R06].
3. **KPI resmi Indonesia bawaan**: DJ, tundaan, LOS PM 96/2015, PKJI 2023, before–after — laporan yang dapat dipakai Bappeda/DPRD/Forum LLAJ [KB R05].
4. **Transparan, anti black-box**: nilai perhitungan antara terlihat (Req 18.0-2) [KB R02]; algoritma yang dapat dijelaskan (cyclic max-pressure) sebelum AI [KB R04].
5. **Ringan di server**: mulai dari analitik & koordinasi (tanpa video di server), edge untuk kamera; skala bertahap 5 → 25 → 100 simpang.
6. **Bertahap & terukur** (T1–T5) dengan pilot koridor dan validasi on/off — sesuai praktik SE FHWA dan monev PM 96.
7. **Lokal & berstandar**: bahasa, regulasi, e-katalog, TKDN; dukungan integrasi Polri/ETLE (sebagai penyedia bukti), TransJakarta/BRT AVL, Damkar.

## 7. Model bisnis kandidat (semua harga = [A] asumsi awal untuk diuji)

| Model | Deskripsi | Asumsi harga awal | Cocok tahap |
|---|---|---|---|
| Lisensi perpetual per simpang + AMS tahunan | Software on-prem di Dishub/Diskominfo; AMS 15–20%/tahun | Rp25–60 jt/simpang [A]; AMS 20% [A] | T2–T4 |
| Langganan (SaaS/on-prem terkelola) per simpang/bulan | Termasuk update & dukungan | Rp1–3 jt/simpang/bulan [A] | T2–T5 (Bodetabek/kota kecil) |
| Paket koridor | 5–10 simpang + kalibrasi + pelatihan | Rp300–800 jt/koridor [A] | T2 |
| Jasa integrasi & retiming | Survei, plan TOD PKJI, integrasi controller, kalibrasi adaptif | Rp15–30 jt/simpang [A]; retiming ≤3 tahun (NTOC) [KB R01] | T1–T5 |
| Modul analitik/ATSPM saja | Untuk kota yang sudah punya ATCS (Surabaya) | Rp10–20 jt/simpang/tahun [A] | T2–T3 |
| B2B2G lisensi ke vendor controller | Vendor menjual paket, kita lisensi software | Royalti 10–20% [A] | T2–T3 |
Pembanding pasar: paket ATCS turnkey Rp350–400 jt/simpang (Yogyakarta), hingga Rp1,3–1,8 M/simpang (Kudus); DKI Rp120 M/25 simpang ≈ Rp4,8 M/simpang (termasuk kamera AI, ANPR, fiber) [W-4; KB].

## 8. Go-to-market bertahap

1. **Pilot pembuktian (T1→T2, 3–6 bulan):** 1 kota Bodetabek + 1 kota metropolitan; koridor 3–5 simpang (≥3 simpang ≤1 km sesuai PM 96 [KB R00 E]); skema kerja sama/swakelola berbiaya rendah; ukur before–after (on/off) dengan MOE PM 96/PKJI + probe GPS; publikasi bersama Dishub.
2. **Tayang e-katalog & sertifikasi** (paralel): TKDN software, etalase produk/jasa; dokumen KAK template untuk Dishub.
3. **Skala kota (T2–T3):** 25–50 simpang di 2–3 kota; kemitraan vendor controller lokal untuk hardware; pelatihan operator (matriks Mampu/Mau ala RPP DKI [KB majalah]).
4. **Referensi & standar (T3–T4):** ikut program RITJ/BPTJ, Forum LLAJ, kolaborasi ITS Indonesia; modul prioritas BRT (Trans Semanggi, Trans Metro Bandung, TransJakarta lintas batas).
5. **Regional/provinsi & end-state (T4–T5):** koordinasi lintas kota, digital twin, integrasi ERP/KRE.

### Sumber web sesi ini
- [W-1] Tempo/Expat Life: TomTom Traffic Index 2024 — Bandung #12, Medan #15; urutan Indonesia Bandung, Medan, Surabaya, Palembang, Jakarta (https://en.tempo.co/read/2027683/12-most-congested-cities-in-the-world; https://x.com/expatlifeindo/status/1884136639859224757; https://jakartaglobe.id/news/pramono-on-why-jakarta-is-no-longer-indonesias-most-congested-city)
- [W-2] ATCS Bandung (https://atcs-dishub.bandung.go.id/), Medan (https://atcsdishub.pemkomedan.go.id/), Palembang 15 simpang (https://buanaindonesia.co.id/sumsel/43110-2/), Surabaya SITS (https://dishub.surabaya.go.id/portal/; https://www.instagram.com/sits_dishubsurabaya/)
- [W-2b] Permendagri 86/2017 (https://peraturan.bpk.go.id/Details/311927/permendagri-no-86-tahun-2017)
- [W-3] Sinkronisasi ATCS Jabodetabek 2022 (https://dishub.bogorkab.go.id/rapat-sinkronisasi-pengoperasian-atcs-di-wilayah-jabodetabek/); Bekasi ruang ATCS 2023 (https://www.bekasikota.go.id/detail/dishub-kota-bekasi-resmi-miliki-ruang-atcs-dan-gedung-baru-pengujian-kendaraan-bermotor); Kemenhub ATCS prioritas angkutan massal (https://kemenhub.go.id/post/read/atcs-prioritaskan-perjalanan-angkutan-massal-perkotaan-60768); hibah Bukittinggi (https://infopublik.id/kategori/nusantara/680817/index.html); Tangerang (https://smartcity.tangerangkota.go.id/dimensi/kategori/detail/inovasi-dishub-kota-tangerang-optimalkan-atcs-sukses-atasi-kemacetan-di-kota-tangerang)
- [W-4] E-katalog LKPP produk ATCS (https://e-katalog.lkpp.go.id/id/search/produk/area-traffic-control-system--atcs--pemerintah-daerah-kota-surakarta/92355; https://e-katalog.lkpp.go.id/katalog/produk/detail/54859132; https://e-katalog.lkpp.go.id/katalog/produk/detail/82160981); Javis (https://www.javis.co.id/id/); Qumicon (https://qumicon.co.id/); Yogyakarta Rp400 jt/simpang & 38 simpang (https://www.antaranews.com/berita/3094433/...; https://warta.jogjakota.go.id/detail/index/31268; https://warta.jogjakota.go.id/detail/index/43062/...); Kudus Rp1,3 M (https://jatengpos.co.id/pati-raya/2026/07/24/dishub-kudus-pasang-atcs-rp-13-miliar/); Perpres 46/2025 & TKDN (https://jdih.lkpp.go.id/regulation/peraturan-presiden/peraturan-presiden-nomor-46-tahun-2025; https://alatanindonesia.id/blog/perpres-no-46-tahun-2025-perbarui-kebijakan-tkdn-ini-yang-perlu-anda-tahu; https://www.hukumonline.com/klinik/a/aturan-perhitungan-tingkat-komponen-dalam-negeri-lt67459c6f2faf4/)
- [W-5] Depok 110 CCTV/40 titik & SIMDISHUB (https://berita.depok.go.id/dishub-kota-depok-sukses-realisasikan-berbagai-program-transportasi-dan-infrastruktur-di-tahun-2024); Tangsel ATCS (https://bappeda.tangerangselatankota.go.id/main/news/view/666); Kab. Tangerang uji coba Pasar Kemis (https://side.merahputih.com/dn/dishub-kabupaten-tangerang-uji-coba-atcs-di-simpang-4-pasar-kemis)
- [W-6] SCATS/Telnic→Marktel, FLIR TrafiCam Jakarta–Surabaya (https://www.skyscrapercity.com/threads/lampu-lalu-lintas-di-indonesia-indonesian-traffic-control-system.1763166/; https://www.flir.com/en-eu/discover/traffic/roads-tunnels/traficam-sensors-help-meet-indonesias-ambitious-traffic-management-plans-in-jakarta-and-surabaya/); Yunex/SWARCO (https://www.swarco.com/solutions/traffic-management; https://www.globalhighways.com/yunex-traffic); Smart City UI (https://smartcity.ui.ac.id/what-we-do/products/systems/product-detail/adaptive-traffic-monitoring-system.html)
