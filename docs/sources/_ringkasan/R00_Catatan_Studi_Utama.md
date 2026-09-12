# R00 — Catatan Studi Utama (dibaca langsung oleh Claude)

Tanggal: 2026-09-12. File ini berisi catatan bacaan saya sendiri atas dokumen-dokumen inti (bukan hasil sub-agen). Catatan sub-agen ada di R01–R06; hasil pembacaan penuh dan verifikasi silang saya atas R01–R06 ada di bagian J, dan sintesis lintas-sumber di bagian K.

---

## A. Majalah RPP "LANCAR-Jakarta" (22 halaman) — SELESAI dibaca penuh
Lihat analisis lengkap: `../05_Website_Acuan_Majalah_RPP/ANALISIS_MAJALAH_RPP_LANCAR-JAKARTA.md`.
Inti yang menentukan desain aplikasi:
1. Objek yang dibangun = **ITCS**: APILL adaptif berbasis AI (recognition + predictive), terhubung ke TMC, dengan data yang dipakai lintas instansi (ETLE, pajak, emisi).
2. Skala: 321 simpang prioritas (65 sudah ITCS; 256 target; kontrak 25 → operasi 5 → 20 → 40 → 191).
3. Komponen lapangan eksisting: 4 kamera analitik (Viero) + 1 fisheye + 4 ANPR per simpang; junction box dengan edge AI processor; RS232 ke APILL controller; Metro-E/fiber.
4. Pusat: server traffic, analytic, VMS, storage; video wall; ±25 operator/shift; call center + CRM (SLA 3 jam).
5. Integrasi: Polda (ETLE), Bapenda (pajak), DLH (uji emisi), pengelola tol; ke depan KRE & PL2SE (ERP).
6. KPI yang diklaim: kinerja lalu lintas +20–30%; TomTom rank 30→90; kemacetan 53%→43%.

## B. Permenhub PM 49/2014 — Alat Pemberi Isyarat Lalu Lintas — SELESAI dibaca penuh
Poin yang mengikat desain:
- **Definisi (Ps.1):** APILL = perangkat elektronik isyarat lampu (dapat + bunyi) untuk mengatur lalu lintas orang/kendaraan di persimpangan atau ruas.
- **Jenis (Ps.3–4):** lampu 3 warna / 2 warna / 1 warna; **APILL otonom** vs **APILL terkoordinasi** (siklus terkoordinasi dan berinteraksi dengan APILL lokasi lain).
- **Makna warna (Ps.6):** merah = berhenti di garis henti; kuning setelah hijau = bersiap berhenti; **kuning bersama merah = bersiap bergerak** (red+amber sebelum hijau — perlu didukung di state machine fase; juga diatur PP 79/2013 Ps.43); hijau = berjalan. Susunan vertikal M-K-H atas→bawah, horizontal M-K-H kanan→kiri (Ps.7; PP 79/2013 Ps.42).
- **Waktu siklus (Ps.11–17):** terkoordinasi (skema rencana siklus antar-APILL diatur **sistem terpusat**, Ps.12) vs tidak terkoordinasi: **siklus tetap** (≥ **8 rencana siklus**, Ps.14), **semi-adaptif** (tetap di kaki mayor ≥8 rencana; bervariasi di kaki minor, Ps.15), **adaptif** (bervariasi di kaki mayor & minor menurut situasi arus, Ps.16).
- **Aspek penentuan siklus (Ps.17):** makroskopis — volume menuju/meninggalkan kaki simpang, kapasitas pendekat, komposisi lalu lintas & pejalan kaki, variasi periodik & insidentil, distribusi arah, tundaan & antrian, kecepatan, pengaturan arus; mikroskopis — tundaan, konflik, percepatan. → menjadi daftar input data model kendali.
- Tata cara penentuan siklus ditetapkan Dirjen (Ps.18) → rujuk PKJI/MKJI dan Kep. Dirjen 273/1996 (bagian G).
- **Komponen (Ps.19–25):** luminer (lampu 30–90 mcd/m², optik Ø20–30 cm, piktogram panah/pejalan kaki/bus/sepeda), tiang, pondasi, **perangkat kendali** (rangka tahan 5–70 °C, RH ≤95%), kabel. **Ps.25: APILL dapat dipasangi alat pendeteksi kendaraan, kamera, DIS, peralatan TI untuk lalu lintas (harus bersertifikat).** DIS 30–70 mcd/m².
- **Penyelenggaraan (Ps.27–28):** penempatan/pemasangan, pemeliharaan, penghapusan; **gubernur untuk jalan provinsi**; perpotongan jalan nasional → Dirjen; jalan tol → penyelenggara tol dengan penetapan Dirjen. (Relevan: pemetaan kewenangan tiap simpang di Jakarta — jalan nasional di Jakarta di bawah BPTJ/Dirjen.)
- **Penempatan (Ps.29–39):** sisi kiri menghadap arus (boleh ditambah kanan); ≥60 cm dari tepi bahu; tinggi armatur ≥300 cm (3 warna), 175–265 cm (2 warna pejalan kaki, dengan tombol), ≥500 cm bila di atas rumaja; rotasi ≤5°; maks 3 armatur per tiang.
- **Pemeliharaan (Ps.41):** berkala ≥ tiap **6 bulan** (pertimbangkan umur teknis, perkembangan teknologi telematika, rencana pengaturan); insidentil: ganti komponen rusak mendadak, **penyesuaian waktu siklus dengan situasi arus aktual**, penyesuaian letak.
- **Penghapusan (Ps.42):** umur teknis maks **5 tahun**; berdasarkan penilaian kinerja.
- **Peralihan (Ps.44):** APILL lama wajib menyesuaikan dalam 2 tahun.
**Implikasi aplikasi:** modul aset APILL (inventaris komponen, umur teknis, jadwal pemeliharaan 6-bulanan, log insidentil), state machine dengan red+amber, klasifikasi mode kendali (tetap/semi-adaptif/adaptif/terkoordinasi) dan ≥8 rencana siklus (TOD plan) sebagai fallback wajib.

## C. Permenhub PM 76/2021 — Sistem Manajemen Transportasi Cerdas (ITS) di bidang LLAJ — SELESAI dibaca penuh (17 hal.)
Ini **dasar hukum ITCS** yang dirujuk Dishub. (Catatan: sub-agen R05 hanya sempat membaca abstraknya; bagian ini melengkapi celah tersebut.)
- **Ps.1(1):** SMTC = proses TI, elektronika, telekomunikasi terintegrasi untuk perencanaan, pembangunan, pengoperasian, pengawasan layanan transportasi jalan.
- **Ps.4:** dilakukan dengan aplikasi TI, perangkat elektronik, jaringan telekomunikasi; **bersifat sistem terbuka, berkesinambungan, sesuai standar**; berfungsi pengumpul & pengolah data; **jenis data (ay.4):** kecepatan vs batas, pola aliran/fluktuasi volume, kepadatan (kend/km), waktu perjalanan asal-tujuan, cuaca, kondisi & geometrik jalan, **identitas kendaraan**, kondisi sarana-prasarana. Data → dasar MRLL & MKLL (ay.5) dan layanan informasi masyarakat (ay.6: di prasarana, kendaraan, ruang jalan, tempat lain).
- **Ps.5 tujuan:** pengawasan lalu lintas & transportasi publik; deteksi & identifikasi pergerakan; komunikasi kendaraan–infrastruktur; pengumpulan & pemrosesan data untuk perencanaan & pengaturan; informasi real time ke pengguna jalan.
- **Ps.6 jenis SMTC (12):** a) **sistem manajemen lalu lintas tingkat lanjut (ATMS)**; b) informasi pengguna jalan (ATIS); c) keselamatan & kontrol kendaraan; d) operasi kendaraan komersial; e) transportasi umum tingkat lanjut (APTS); f) pembayaran elektronik; g) manajemen darurat; h) antarkota; i) manajemen kebutuhan perjalanan (TDM); j) parkir; k) pengendalian otonom; l) lainnya.
- **Ps.7 ATMS (inti ITCS):** (1) meningkatkan aliran arus & info real time, **terintegrasi dengan ruang kendali lalu lintas**. (2) subsistem: **a. pengaturan & pengendalian lalu lintas kawasan (ATCS); b. pemantauan lalu lintas real time; c. pemantauan & pengendali rambu elektronik (VMS); d. pemantauan kejadian kecelakaan; e. pemantauan jalan penghubung; f. penegakan hukum lalu lintas secara elektronik (ETLE); g. deteksi waktu tempuh; h. deteksi prioritas bus otomatis.** (3) **prinsip kerja wajib: seluruh peralatan terhubung via jaringan komunikasi ke ruang kendali; seluruh peralatan dapat diubah pengaturannya dari ruang kendali.** (4) layanan: **a. prioritas kendaraan khusus (angkutan umum massal jalan, ambulans, pemadam, pimpinan lembaga negara, tamu negara); b. pemantauan visual dari ruang kendali; c. informasi ke pengguna jalan (suara/tulisan/gambar); d. sistem penindakan pelanggaran; e. deteksi kerusakan peralatan dari ruang kendali; f. rekaman data operasional (status kondisi & kinerja peralatan); g. rekaman data historis lalu lintas; h. deteksi kecepatan.**
- **Ps.8 ATIS:** info kepadatan, jalur alternatif, parkir, jalan berbahaya, cuaca, radio; harus dapat diakses daring/ponsel/rambu elektronik dan terbaru.
- **Ps.11 APTS:** info rute/jadwal/ETA; **menggunakan sistem sinyal prioritas bus untuk perubahan fase & sinyal khusus di simpang bersinyal; mengurangi tundaan angkutan umum prioritas di simpang.**
- **Ps.13 manajemen darurat:** info & penanganan kecelakaan/kepadatan, polisi, ambulans, RS terdekat, derek, pemadam.
- **Ps.15 TDM:** pembatasan via identifikasi kendaraan, **jalan berbayar elektronik (ERP)**, pengenalan TNKB (ANPR).
- **Ps.18:** pedoman teknis & standar ditetapkan Dirjen.
- **Ps.19 penyelenggara:** Menteri (jalan nasional; **di Jabodetabek didelegasikan ke Kepala BPTJ**), **gubernur (jalan provinsi)**, bupati/walikota; dapat dikerjasamakan dengan badan usaha (perencanaan, pembangunan, pengoperasian, pemeliharaan).
- **Ps.20:** dapat saling terintegrasi dengan sistem informasi K/L dan Pemda. **Ps.21:** wajib ada **unit kerja pengelola** dan **SDM berkompetensi** SMTC.
- **Ps.22–24:** pembinaan (bantek, bimtek, sosialisasi) & pengawasan (penilaian efektivitas, tindakan korektif).
**Implikasi aplikasi:** daftar modul minimal ITCS = ATCS + monitoring real time + VMS + incident + ETLE-integration + travel-time + bus priority; wajib arsitektur terpusat (semua perangkat online & dapat dikonfigurasi dari TMC), device health monitoring, operational log, historical data store, speed detection, priority for 5 kelas kendaraan khusus; data model harus memuat 8 jenis data Ps.4(4); sistem terbuka & berstandar (→ NTCIP/ISO). Kewenangan: simpang di jalan nasional Jakarta melibatkan BPTJ.

## D. Pergub DKI 68/2021 — Sistem Transportasi Terpadu & Terintegrasi (Jak Lingko) — SELESAI dibaca penuh
- Fokus integrasi angkutan massal & pembatasan kendaraan pribadi (turunan Perda 5/2014 Ps.11 & 78).
- **Ps.10(6):** sistem integrasi data & informasi minimal mengelola: armada siap operasi, km tempuh, frekuensi, penumpang naik/turun, perpindahan antarmoda, **keberadaan aktual armada (AVL)**, **waktu tempuh, headway, jadwal**, asal-tujuan, kecelakaan & pelanggaran, aduan, informasi penumpang. (7) wajib menjamin kerahasiaan & keamanan data.
- **Ps.11:** harus terintegrasi dengan sistem informasi Pemprov DKI; data terintegrasi **milik Pemprov**; dapat diakses online real time oleh pihak terkait atas persetujuan Gubernur.
- **Ps.13:** pembatasan kendaraan pribadi: rekayasa lalu lintas, **ERP**, pembatasan lalu lintas, pajak progresif, parkir, **ganjil-genap**, kendaraan ramah lingkungan; datanya harus terintegrasi ke sistem Pemprov.
- **Ps.15:** monev periodik; laporan ke Gubernur tiap 3 bulan.
**Implikasi aplikasi:** bus priority ITCS dapat memakai data AVL/headway TransJakarta yang secara hukum sudah wajib tersedia; ITCS harus terintegrasi ke sistem informasi Pemprov (Jakarta Smart City/JAKI); keamanan data & pelaporan triwulanan.

## E. Permenhub PM 96/2015 — Pedoman Pelaksanaan Kegiatan MRLL — bagian kunci SELESAI dibaca
- **Definisi:** tingkat pelayanan = ukuran kuantitatif & kualitatif kondisi operasional; tundaan = waktu tambahan melewati persimpangan dibanding tanpa persimpangan; volume (kend/jam atau smp/jam); kapasitas; nisbah V/C; kecepatan (km/jam).
- **Perencanaan MRLL (8 kegiatan, 5 wajib):** identifikasi masalah; inventarisasi & analisis situasi arus (volume, komposisi, variasi, distribusi arah, pengaturan arus, kecepatan & tundaan, kinerja perlengkapan jalan, prakiraan volume); daya tampung jalan; penetapan tingkat pelayanan; rencana kebijakan. Pengamatan boleh visual atau **peralatan teknis (kamera)**; data historis.
- **Kecepatan:** travel speed (termasuk tundaan berhenti) vs free-flow speed. **Tundaan simpang ber-APILL** = tundaan lalu lintas + tundaan geometrik.
- **Indikator tingkat pelayanan (9):** V/C, kecepatan batas atas/bawah, waktu perjalanan, kebebasan bergerak, keamanan, keselamatan, ketertiban, kelancaran, penilaian pengemudi.
- **Tingkat pelayanan PERSIMPANGAN (tundaan per kendaraan):** A <5 s; B 5–15 s; C 15–25 s; D 25–40 s; E 40–60 s; F >60 s. (Beda dengan HCM: A ≤10, B 10–20, C 20–35, D 35–55, E 55–80, F >80.) → **threshold LOS dashboard ITCS harus memakai PM 96/2015.**
- **Target LOS minimum ruas:** arteri primer B, kolektor primer B, lokal primer C, tol B; arteri sekunder C, kolektor sekunder C, lokal sekunder D, lingkungan D.
- **Pengawasan:** pemantauan efektivitas via penilaian LOS setelah kebijakan; analisis **before–after LOS**; tindakan korektif.
- **Warrant simpang ber-APILL:** volume masuk rata-rata >750 kend/jam selama 8 jam; delay rata-rata >30 s; pejalan kaki >175/jam selama 8 jam; kecelakaan >5/tahun.
- **APILL otonom adaptif:** untuk simpang dengan volume antar kaki sangat bervariasi, atau tidak memungkinkan ATCS; wajib **alat pendeteksi kendaraan**.
- **Sistem APILL Terkoordinasi (ATCS):** syarat **≥3 simpang**, **jarak ≤1 km**; minimal APILL, marka, rambu, **detektor, jaringan komunikasi, ruang pusat kendali**; dapat dilengkapi **kamera, DIS, VMS, pendeteksi angkutan umum massal, fase bus priority, pemantau kecepatan & volume.**
- **Pengendalian simpang dengan ITS:** pada simpang ber-ATCS di kota sedang/besar/metropolitan; minimal pemantau kecepatan & volume + media informasi.
- **Marka kotak kuning:** hanya pada simpang APILL adaptif/ATCS dengan LOS ≥ C. **RHK sepeda motor** pada simpang dengan lajur belok kiri langsung.
- **Prioritas angkutan massal:** **bus priority pada persimpangan ber-APILL** dan waktu hijau khusus angkutan umum & pejalan kaki.
- **Perekayasaan:** pemasangan wajib **uji coba pengoperasian APILL & kelengkapannya**.
**Implikasi aplikasi:** skema LOS PM 96; modul warrant/kelayakan simpang; corridor grouping ≥3 simpang ≤1 km; inventaris perlengkapan pendukung; laporan before–after.

## G. Kep. Dirjen Hubdat 273/HK.105/DRJD/96 — Pedoman Teknis Pengaturan Lalu Lintas di Persimpangan Berdiri Sendiri dengan APILL — SELESAI dibaca
Metode perhitungan fixed-time yang menjadi rujukan resmi (sejalan MKJI 1997 & PKJI 2023). Definisi: **tahap**, **fase**, **siklus**, **MP (mulut persimpangan)**, **skr**.
- **Kriteria pemasangan APILL:** >750 kend/jam selama 8 jam; atau tundaan >30 s; atau >175 pejalan kaki/jam; atau sering kecelakaan.
- **Evaluasi:** perhitungan waktu APILL ditinjau ulang **sekurang-kurangnya sekali per 3 bulan**.
- **Nilai acuan:** VJP = K × LHR (K 7–12%); belok 15%; komposisi per ukuran kota; fase default 2; fase belok kanan terpisah bila RT >200 skr/jam; waktu hijau antara 5/6/7 s; kuning **3 detik**.
- **skr:** LV 1,0; HV 1,3; MC 0,2 (P) / 0,4 (O); UM 0,5 (P) / 1,0 (O). Tipe MP **P (protected)** vs **O (opposed)**.
- **Waktu pengosongan:** CT_i = max[(L_EV + l_EV)/V_EV − L_AV/V_AV]; V = 10 m/s (bermotor), 3 m/s (KTB), 1,2 m/s (pejalan kaki); l_EV = 5 m / 2 m. **LT = Σ(all-red + kuning).**
- **We:** aturan LTOR >2 m / ≤2 m; cek W_EXIT untuk tipe P.
- **S0 = 600 × We** (tipe P); tipe O dari grafik.
- **Faktor koreksi:** F_CS (>3 jt 1,05 …); F_SF; F_G; F_P = {L_P/3 − (W_A − 2)(L_P/3 − g)/W_A}/g; F_RT = 1 + 0,26·p_RT; F_LT = 1 − 0,16·p_LT. **S = S0·F_CS·F_SF·F_G·F_P·F_RT·F_LT.**
- **FR = Q/S; IFR = Σ FR_crit; PR_i = FR_crit,i / IFR.**
- **c = (1,5·LT + 5)/(1 − IFR)**; siklus 2 fase 40–80 s, 3 fase 50–100 s, 4 fase 80–130 s; >130 s dihindari. **g_i = (c − LT)·PR_i**; hijau <10 s dihindari.
- **C = S·g/c; DS = Q/C.**
- **Unjuk kerja:** NQ1 (grafik; 0 jika DS<0,5); NQ2 = Q·(c − g); NQ_MAX (P_OL 5%/5–10%); **QL = NQ_MAX·20/W_ENTRY**; **p_SV = 1 + NQ/c − g/c** (≤1); **D_j = (A_j·c + B_j/Q_j)·0,90**, A_j = (1 − GR)²/[2(1 − GR·DS)], B_j = DS²/[2(1 − DS)]; D_I = Σ(Q_j D_j)/ΣQ_j; LOS A <5 … F >60 det/skr.
**Implikasi aplikasi:** mesin perhitungan KPI & perencanaan plan fixed-time/TOD ("Kalkulator APILL"), baseline & sanity check untuk output adaptif, laporan before–after. PKJI 2023 (R05 D) memberi notasi terbaru (J, DJ, wH, Nq, PA, RKH, TLL/TG) dengan model yang sama; perbedaan numerik hanya EMP SM 0,2→0,15 dan wH normal 26→27 s.

## H. Perdirjen Hubdat SK.7234/AJ.401/DRJD/2013 — Juknis Perlengkapan Jalan, Bab II APILL — SELESAI dibaca
- **Perencanaan:** inventarisasi, survei kebutuhan, **perkiraan kebutuhan 5 tahun**.
- **Kondisi kerja:** 5–70 °C; RH 0–95%.
- **Controller:** modular; **≥8 signal group kendaraan + 8 pejalan kaki, ≥32 dapat dikembangkan**; **≥4 program, ≥16 dapat dikembangkan**; pemindahan program & kedip otomatis/manual; siklus ≤999 s; **start-up: kuning kedip → kuning tetap**; **kendali manual petugas (perpanjang/perpendek hijau, kedip)**; indikator fault; **conflict green/conflict signal → flashing otomatis**; MCB/ELCB/petir; 100–240 VAC; **dapat dilengkapi detektor (APILL responsif), interface komunikasi data ATCS, DIS, count-down timer**; antar tiang kabel/RF.
- **Master/Slave:** master 8 signal group, 4 program tetap, 1 flashing, **10 plan wireless/hari**; slave 3 signal.
- **Detektor (APILL-ATCS):** keberadaan/kecepatan; overhead/permukaan; **magnetik/video/radar**; software; **≥4 zona**; **output gap & occupancy**.
- **DIS:** overhead; huruf/angka/simbol; **remote dari Pusat Kendali ATCS**; **countdown 5–7 s** menjelang hijau; ≥48×160 px; **RS-485 1200–9600 bps**; IP65.
- **Power:** PLN + stabilizer; grounding ≤10 Ω.
**Implikasi aplikasi:** model data controller (signal group ≥8+8 hingga 32; plan ≥4–16; TOD ≥10 perubahan/hari; status flashing/fault/conflict; mode manual override; start-up sequence); detektor per zona (≥4/pendekat, gap & occupancy); DIS/countdown terkonfigurasi dari pusat; inventaris penandaan; horizon 5 tahun.

## I. Shams, Emtenan, Day (2023) — "A Taxonomy of Adaptive Traffic Signal Control" (arXiv 2308.01952) — dibaca (pendahuluan, taksonomi, kesimpulan)
- Vokabulari: **COS** = cycle, offset, split. 2/4/**8 fase dua ring (NEMA)**; di luar AS **stage-based** lebih umum (relevan Indonesia).
- **Actuated** tidak dianggap adaptif; **actuated-coordinated**: COS + aktuasi.
- **Generasi UTCS:** 0 TOD COS; **1-GC traffic responsive** (pilih pola dari pustaka via V+K·O); **2-GC** penyesuaian adaptif COS (SCATS/SCOOT); **3-GC real-time** (umumnya tanpa COS; max-pressure, RL, DP/MILP).
- Taksonomi: reactive/proactive, scope (local/system/hierarchical), continuous vs planning-horizon, rule-based vs optimization, cyclic/acyclic. 88 metode; RL 17 (paling banyak 2011–22), DP 10, MILP 8, MP 4.
**Implikasi:** arsitektur bertingkat gen 0 → 1 → 2 → 3 (hanya simpang terpilih dengan guard-rail); dukung **stage-based** sekaligus **ring-barrier**.

## J. Verifikasi hasil sub-agen R01–R06 (semua dibaca penuh oleh saya; verifikasi acak terhadap teks sumber)
| File | Ukuran | Verifikasi acak (grep ke `_teks_ekstraksi`) | Catatan |
|---|---|---|---|
| R01 Signal Timing Manuals (NCHRP 812, FHWA 2008, NCDOT) | ±11.100 kata | gap-out 3 syarat; "not set-and-forget"; ≥30 menit per pattern; SCOOT hold/force-off; Webster C=(1,5L+5)/(1−Y); B/C 40:1 — **cocok** | badan persamaan NCHRP 812 tidak terekstraksi → dilengkapi dari FHWA 2008 dan ditandai [rekonstruksi]; ATSPM/InSync tidak ada di ketiga dokumen |
| R02 ASCT SE & Benefits (HOP-11-027, T414, NYSERDA, EDC-1, HOP-23-041) | ±10.900 kata | biaya $55.534/$10.252/$3.814; Req 18.0-2; "complaints as the primary measure" — **cocok** | tabel T414 berupa gambar; angka dari narasi |
| R03 NTCIP/SUMO/ATSPM | ±11.400 kata | `unitBackupTime` "revert to Backup Mode"; sumolights (59,21,54) vs (158,169,85); split failure ≥80%; 1/10-second — **cocok** | NTCIP yang ada v02 (2005): tanpa TSP/hi-res/SPaT; kode enumerasi Indiana ditandai "verifikasi" |
| R04 Paper akademis (20 sumber) | ±8.600 kata | min green 7 s & rate-limit 5 s; VHT −14,5/−10,6/−15,6%; OCC-MP 0,36–2,64% vs 3,50–25,75%; "never been deployed"; EVP 96%/−36% — **cocok** | — |
| R05 Regulasi & PKJI | ±11.700 kata | UU Ps.247(3); PP 32 Ps.79(3); Perda Ps.8; PKJI ">130 detik"; EMP SM 0,15; Webster PKJI — **cocok** | PM 76/2021 dibaca sub-agen saat masih abstrak → dilengkapi bagian C di atas |
| R06 TSP/EVP/HCM/Jakarta | ±8.900 kata | "mysteriously diminish"; TransLink 4 levels; EVP 25 s & −71%; HCM "average travel speed" — **cocok** | HCM overview tidak memuat rumus control delay (dinyatakan jujur) |

## K. Sintesis lintas-sumber — apa yang harus dibangun (bahan masuk ke tahap perencanaan)
1. **Landasan hukum & kepatuhan** (R05, R00 B–H): ITCS = subsistem SMTC/ATMS (PM 76/2021 Ps.7) yang wajib terintegrasi ke pusat kendali SIK LLAJ Polri (UU Ps.246–247), menyediakan override petugas (UU Ps.104), preemption hak utama (Ps.135), fallback ≥8 plan (PM 49 Ps.14), LOS PM 96, warrant ATCS ≥3 simpang ≤1 km, data milik Pemprov & kerahasiaan (Pergub 68), ETLE hanya sebagai penyedia bukti (UU Ps.272), UU PDP untuk data ANPR/pajak/emisi, simpang jalan nasional via Dirjen/BPTJ.
2. **Model data & antarmuka controller** (R01 I.1, R03 D.1, R00 H): intersection → ring/barrier & stage → phase/overlap → detector; pattern = cycle+split+offset+sequence; TOD/day plan; preempt; priority request (NTCIP 1211 semantik); hi-res event log 0,1 s; kesehatan perangkat; mode manual; dua adaptor (NTCIP/SNMP untuk controller standar, RS-232 vendor untuk eksisting) di balik satu Controller Abstraction Interface; perintah real-time hanya via objek C + heartbeat < backup timer; plan via transaksi tervalidasi.
3. **Mesin kendali bertingkat** (R04 F, R01 D, R02 D): Tingkat 0 fixed-time TOD (Webster/PKJI, ≥8 plan) → 1 actuated ring-barrier (min/max green, gap, ped) → 2 **cyclic max-pressure terkoordinasi** (cycle & offset tetap per koridor, MP hanya mengatur split, min green ≥7–10 s, perubahan ≤5 s/siklus, integer) di **20–25% simpang kritis** + **perimeter control** CBD saat jenuh → 2b prioritas bus kondisional berbasis occupancy/headway (OCC/Transit-MP; green extension/early green ≤10 s; 1 aktivasi/siklus; lockout) & EVP bertingkat (hanya bila target respons terancam; conflict graph; recovery) → 3 analitik probe/GPS mingguan (cyclic TSD, PPD, AoG) → 4 digital twin (SUMO NEMA) + RL hanya sebagai advisor via shadow mode dengan veto statistik.
4. **Guard-rail keselamatan** (R04 F, R01 B.4, R05 D): yellow 3 s & all-red dihitung; ped walk/clearance tak boleh dipotong oleh priority; max green ≤60 s; watchdog data stale → degradasi actuated → TOD; transisi ≤3–5 siklus, ≥30 menit per pattern; validasi Annex B sebelum download plan; audit log tiap perintah; operator override.
5. **KPI & monev** (R01 G, R03 C, R05 E, R06 F.3): PKJI/PM 96 (DJ, tundaan, PA, RKH, LOS A–F) untuk kepatuhan & komparabilitas lokal; ATSPM (phase termination, split monitor, PCD/AoG/platoon ratio, split failure GOR/ROR5 ≥80%, approach delay, ped delay, preemption details, watchdog) untuk operasi harian; travel time/reliability dari probe (target 35 km/jam Perda / 30 km/jam Perpres); kesehatan perangkat (% detektor berfungsi, uptime komunikasi, transisi); before–after on/off; laporan Forum LLAJ, Dirjen (tahunan), Gubernur (triwulan).
6. **Tata kelola & SDM** (R02 G, R01 H, R06 A.10): systems engineering ConOps→requirements→verification→validation (traceability), procurement best-value dengan NTCIP wajib, NEMA TS 8, TSMP & CMF, retiming ≤3 tahun, 1 engineer/75–100 sinyal & 1 teknisi/40–50, pelatihan kalibrasi, MoU detik prioritas tertulis, deployment bertahap per koridor (5 → 25 → 65 → 321) dengan pilot & experimental plan.
7. **Konteks & risiko Jakarta** (R06 D–E, R02 H.3): 321 simpang, 65 ITCS, 25 dikontrak 2025 (Rp120 M); klaim +20–30% tanpa MOE terdefinisi → modul evaluasi wajib; kendala tipikal ATCS Indonesia (detektor rusak, komunikasi, SDM, pemeliharaan, DS ≥1); side-street delay bisa naik; umur ASCT 6–7 tahun karena isu institusional.
