# 09 — Konteks Jakarta dan Kota-Kota Target

**Cara pakai:** profil ringkas untuk positioning produk, pemilihan pilot, dan pitch ke pemda. Setiap sel memuat tag sumber; angka hanya dari sumber. Kolom "Kesenjangan" = kebutuhan nyata lapangan yang boleh dijadikan dasar fitur (prinsip: kreativitas berbasis kebutuhan riil). Arsip teks sumber ada di `07_Konteks_Kota_Target/Teks_*.md` (kota target) dan `04_Konteks_Jakarta_ITCS/` (Jakarta). Data yang belum diverifikasi ditandai (?).

---

## A. DKI Jakarta (acuan end-state)
| Aspek | Isi | Sumber |
|---|---|---|
| Urgensi | TomTom 2024: peringkat 90 dunia, kemacetan 43% (2023: 53%, #30/31); 24,35 juta kendaraan (2024); modal share angkutan umum 22,19% vs target 60% Perda 5/2014 | R06 D.1, D.6 |
| Status ITCS | 321 simpang prioritas; ±65 ber-ITCS (2025); 20 uji coba 2023; 25 dikontrak 2025 (Rp120 M); target 321 pada 2030; sisanya ATCS statis | R06 D.1; ANALISIS_MAJALAH |
| Fitur yang diklaim | Actuated, self-adaptive, coordinated green wave, VIP green wave, bus priority, recognition (jenis, pelat, pelanggaran), predictive (volume, hijau optimal), digital twin 3D | R06 D.2 |
| Arsitektur | 4 kamera analitik + 1 fisheye + 4 ANPR/simpang; junction box edge AI; RS232 ke controller; Metro-E/fiber; TMC Abdul Muis: server traffic/analytic/VMS/storage, video wall; 25 operator/shift; call center–CRM SLA 3 jam | ANALISIS_MAJALAH §3.4; R06 D.3 |
| Integrasi | Ditlantas PMJ (ETLE), Bapenda (pajak), DLH (uji emisi), pengelola tol; KRE & PL2SE/ERP (jangka panjang) | ANALISIS_MAJALAH §3.6 |
| Vendor/teknologi | PT TKDN (APILL Gen-5, digital twin 3D); kamera "Viero"; spesifikasi teknis tidak publik | R06 D.5 |
| Kritik | Instran/MTI/DPRD: akar masalah kendaraan pribadi; perlu TDM/ERP & single data; klaim +20–30% tanpa MOE | R06 D.6 |
| Pengambil keputusan | Gubernur/Wagub (promotor), Kadishub, UP SPLL, Bapenda, DLH, Ditlantas PMJ, BPTJ (jalan nasional) | ANALISIS_MAJALAH §3.7 |
| Implikasi produk | Jakarta = benchmark T4/T5, bukan pasar masuk pertama (sudah ada vendor & kontrak) | — |

## B. Kota-kota target (di luar DKI)

| Kota | Urgensi (TomTom 2024 / keluhan) | Status ATCS (yang terdokumentasi) | Kesenjangan / kebutuhan nyata | Peluang masuk | Pengambil keputusan & anggaran | Sumber |
|---|---|---|---|---|---|---|
| **Bandung** | **#12 dunia, termacet #1 Indonesia**; 10 km = 32 mnt 37 dtk; kemacetan 48%; 108 jam hilang/tahun | ATCS Dishub sejak lama; 293 CCTV di simpang besar; ruang ATCS Balai Kota; rencana upgrade ATCS→ATMS (2023); portal CCTV publik | Mei 2026: ±20 kamera mati karena node dirusak (Pasteur–Tamansari) → rapuh terhadap kegagalan node; ATMS belum terwujud; data.bandung.go.id/atcs tidak dapat diakses (500) | Modul health/resiliensi + upgrade ATCS→ATMS bertahap; pilot koridor Pasteur–Dago; benchmark TomTom sebagai KPI politik | Wali Kota, Kadishub Bandung; APBD kota; potensi hibah Kemenhub (Bandung tercatat penerima ATCS sejak ≤2014) | 07/tomtom2024_tempo; 07/bandung_20_cctv; 07/kemenhub_atcs_prioritas; WebSearch (pasjabar 2023, 293 CCTV) |
| **Medan** | **#15 dunia, #2 Indonesia** | ITS/ATCS mulai 2020 (Kadishub Iswar): 18 simpang inti dikendalikan; portal live CCTV `atcsdishub.medan.go.id`; jurnal: implementasi "belum maksimal karena kendala" | Anggaran pemeliharaan traffic light ±Rp3 M/th "tidak cukup"; banyak simpang belum ber-APILL; DPRD menyoroti lampu rusak | Produk berbiaya rendah + pemeliharaan terukur; integrasi ke ITS 2020 eksisting; Wali Kota Rico Waas (?) menjadikan kemacetan isu | Wali Kota, Kadishub, DPRD Komisi IV; APBD terbatas | 07/medan_its_2020; 07/medan_jurnal; WebSearch |
| **Surabaya** | #3 Indonesia (TomTom 2024); Wali Kota Eri Cahyadi menegur Dishub soal antrean (Jul 2024) | SITS di Terminal Bratang: **136 simpang, 580 kamera** terhubung; ATCS berbasis SCATS (?) sejak 2010 (40 simpang); >1.000 titik CCTV (2026); aplikasi SITS CCTV | **Hanya 8 unit sensor adaptif** dari ideal ~400; Wali Kota minta sensor durasi dianggarkan 2025; kamera sebagian mati | **Peluang paling konkret**: kebutuhan sensor/kendali adaptif skala besar sudah diminta kepala daerah; integrasi ke SITS eksisting; hitung antrean dari kamera yang sudah ada | Wali Kota Eri Cahyadi, Kadishub Tundjung Iswandaru; APBD kota besar | 07/surabaya_sits_136; 07/surabaya_unesa; 07/surabaya_smartcity |
| **Palembang** | #4 Indonesia (TomTom 2024); Sekda minta Dishub lebih disiplin di lapangan | ATCS di 15 simpang (2019) + rencana 13 (2020, Rp15 M) → 28; kebutuhan 52 simpang; fokus CCTV + pengeras suara teguran; kerja sama Polri untuk penindakan; rencana "ditingkatkan menjadi ITS" | Cakupan baru ~half; fungsi masih pemantauan/teguran, belum adaptif | Paket "dari CCTV ke adaptif": pakai kamera eksisting untuk hitung antrean; roadmap 28→52 | Wali Kota, Kadishub; APBD (Rp15 M untuk 13 titik ≈ Rp1,15 M/titik) | 07/palembang_15_simpang; 07/palembang_idntimes |
| **Kota Bekasi** | Perbatasan DKI; "beberapa titik sering macet" (Plt Walkot) | Ruang ATCS diresmikan Mar 2023 di Mako Dishub; **120 CCTV** terpasang; traffic update rutin | Fungsi utama pemantauan; jumlah simpang terkendali tidak disebut; SDM ditekankan | Onboarding cepat (CCTV sudah ada); koordinasi lintas batas dengan DKI (rapat sinkronisasi ATCS Jabodetabek 2022) | Wali Kota, Kadishub Kota Bekasi | 07/bekasi_ruang_atcs_2023; 07/bogorkab_rapat_sinkronisasi (judul) |
| **Kota Tangerang** | Perbatasan DKI; klaim "sukses atasi kemacetan" via ATCS sejak 2018 | ATCS + CCTV di **33 simpang**; Traffic Public Announcement; Command Centre Dishub; target 42 ATCS (?) | Klaim tanpa MOE; kendali adaptif tidak disebut | Modul evaluasi kinerja (bukti klaim) + upgrade adaptif di koridor; koordinasi lintas batas | Wali Kota, Kadishub Achmad Suhaely | 07/tangerang_smartcity; 07/tangerang_33_simpang |
| **Kab. Tangerang** | Perbatasan; fokus kemacetan Pasar Kemis/Karawaci/Kukun | FS & DED selesai 2019; target 23 ATCS (2023); mulai 3 simpang 2020 | Bertahap & anggaran terbatas | Layanan FS/DED digital + pilot 3 simpang | Kadishub (Kabid LLAJ Norman David) | 07/tangerangkab_23_atcs_2020 |
| **Tangerang Selatan** | Perbatasan; kemacetan Rawa Buntu, BSD (?) | ATCS streaming publik `atcs.tangerangselatankota.go.id`; CCTV di simpang utama, sekolah, pusat belanja | Jumlah & kendali adaptif tidak terdokumentasi | Pemantauan → adaptif | Kadishub Tangsel | WebSearch (tangeranglife) |
| **Kota Depok** | Perbatasan; kemacetan Margonda | 2024: 9 CCTV lalu lintas baru; aplikasi SIMDISHUB "terintegrasi ATCS"; Biskita TransDepok (Kemenhub) | Cakupan ATCS kecil; fokus angkutan umum → peluang bus priority | Bus priority Biskita + pemantauan; integrasi SIMDISHUB | Kadishub Zamrowi; kerja sama Kemenhub/BPTJ | 07/depok_dishub_program_2024 |
| **Kota Bogor** | Perbatasan; kemacetan pusat kota | ATCS Dishub Kota Bogor (akun "BITS"); penerima ATCS Kemenhub (≤2014) | Detail tidak terdokumentasi | Verifikasi lapangan | Kadishub Kota Bogor | WebSearch |
| **Kab. Bogor** | Perbatasan; Cibinong–Bojonggede–Sentul | ITS/ATCS 2015–2019 di **16 simpang** (Sentul, Pemda, Cibinong, Bojonggede, Citeureup, dst.); CCTV Pakansari; 435 personel saat mudik; kerja sama BPTJ (skybridge, park & ride) | Fungsi: pantau + kerahkan personel; adaptif terbatas | Prioritas koridor Bojonggede–Cibinong; integrasi BPTJ | Kadishub Kab. Bogor | 07/bogorkab_layanan_its_atcs; 07/bogorkab_kinerja_2025; 07/bogorkab_antara |
| Pembanding: **Kab. Bandung Barat** | Wisata Lembang | ATCS Rp19 M: 129 kamera/50 titik (2022), 40 titik (2024) + pengeras suara | Turun 50→40 titik (?) | — | — | 07/bandungbarat_rp19m; WebSearch |
| Pembanding: **Batam, Makassar, Bukittinggi** | — | Hibah Kemenhub: Batam Rp17,2 M (BAST 2024; 2014–2019 total ±9 simpang); Makassar 4 simpang Rp4,3 M (2019) + 4 (2020, Rp3,5 M), 5 kamera/simpang; Bukittinggi Rp9,39 M | Aset hibah diserahterimakan terlambat → O&M tertunda | Menawarkan O&M + software di atas aset hibah | Ditjen Hubdat/BPTD | 07/batam_antara; 07/makassar; 07/bukittinggi |

**Pola lintas kota (untuk positioning):**
1. Semua kota sudah punya **CCTV + ruang kendali**; hampir semua **belum adaptif** (Surabaya 8/136 eksplisit). → Produk harus **memanfaatkan kamera eksisting** dan menambah kendali adaptif secara bertahap.
2. Alur kerja nyata = pantau CCTV → tegur via pengeras suara → kirim personel. → MVP harus mendukung alur ini (insiden, dispatch, TPA) sebelum "AI".
3. Anggaran tipikal: Rp1–4 M per simpang (hibah/APBD), pemeliharaan sangat kecil (Medan Rp3 M/th). → Model harga per simpang rendah + langganan pemeliharaan.
4. Kepala daerah menagih hasil (Surabaya, Palembang, Medan DPRD). → Laporan kinerja yang bisa dipublikasikan adalah fitur inti.
5. Wilayah Jabodetabek sudah ada forum sinkronisasi ATCS (2022) → peluang produk lintas-yurisdiksi/koordinasi batas dengan DKI.

## C. Lanskap vendor & jalur pengadaan
| Item | Isi | Sumber |
|---|---|---|
| PT Javis Teknologi Albarokah (Sleman) | R&D traffic light & ATCS sejak 2009; produk ATMS, VID AI Detector, APILL Otonom Cerdas, bus priority, PJU surya; 50+ tim, 100+ proyek; ISO, SNI, TKDN, TDBU; ada di INAPROC (contoh luminer PJU Rp5,4 jt TKDN+BMP 66,55%) | 07/vendor_javis_about; WebSearch |
| PT Qumicon Indonesia | ATCS produk unggulan; 30 tahun; >100 karyawan; pelanggan termasuk 5 kota administrasi DKI (?) | 07/vendor_qumicon_home; 07/vendor_qumicon_atcs |
| PT Teknologi Karya Digital Nusa (TKDN) | Vendor ITCS Jakarta (APILL Gen-5, digital twin, AI predictive); Tbk | R06 D.5 |
| Lainnya (e-katalog) | "Kit Mainboard APILL ATCS Controller 24V DC", "Traffic Controller ATCS/ITS 8 SG DC backup battery" terdaftar di e-katalog LKPP; ATCS Surakarta sebagai paket produk | WebSearch e-katalog |
| Pengadaan | E-katalog LKPP/INAPROC (produk TKDN, UMKM); Perpres 46/2025 Ps.66: prioritas produk TKDN+BMP >40% → boleh beli TKDN >25%; alokasi 40% untuk usaha kecil/koperasi; hibah ATCS Kemenhub via BPTD (BMN diserahterimakan ke pemda); KPBU jarang untuk perlengkapan jalan (contoh PJU) | 07/tkdn_perpres46_cnbc; WebSearch |
| Implikasi | Perlu sertifikasi TKDN (software dinilai via Kemenperin), pendaftaran INAPROC, kemitraan pabrikan controller lokal (Javis/Qumicon) agar paket lengkap; jual sebagai penyedia software/ATMS di atas perangkat mereka | — |

---

**Pointer ke detail:** R06 D (Jakarta), ANALISIS_MAJALAH (arsitektur & milestone DKI), `07_Konteks_Kota_Target/_urls.tsv` (daftar URL), KB 08 (risiko), docs/planning/03 (pasar & kota target — turunan dari file ini). Yang gagal diakses: data.bandung.go.id/atcs (500), pasjabar ATCS→ATMS (404, isi diambil dari cuplikan pencarian), jdih.lkpp Perpres 46/2025 (timeout), ResearchGate Kab. Bogor.
