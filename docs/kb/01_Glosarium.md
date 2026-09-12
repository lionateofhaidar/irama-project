# 01 — Glosarium ITCS (ID/EN)

**Cara pakai file ini**
- Cari istilah dengan Ctrl+F; tiap baris = 1 istilah, 1 kalimat definisi, tag sumber, catatan implementasi.
- Tag sumber: [R0x bagian] = catatan studi di `docs/sources/_ringkasan/`; [PM 49 Ps.N] dsb. = regulasi di `docs/sources/_teks_ekstraksi/`.
- Istilah Indonesia resmi (regulasi/PKJI) ditulis dulu, padanan Inggris di kurung. "(tidak ada di sumber)" = tidak ditemukan dalam korpus.
- Untuk rumus lihat `02_Lembar_Rumus.md`; untuk pasal lihat `03_Peta_Regulasi_Kepatuhan.md`.

## A. Perangkat & elemen sinyal

| Istilah (ID/EN) | Definisi | Sumber | Catatan implementasi |
|---|---|---|---|
| APILL (Alat Pemberi Isyarat Lalu Lintas / traffic signal) | Perangkat elektronik isyarat lampu (dapat + bunyi) untuk mengatur lalu lintas orang/kendaraan di persimpangan atau ruas. | [UU 22/2009 Ps.1 angka 19; PM 49 Ps.1] | Entitas inti aset; wajib berizin Kepala Dinas (Perda 5/2014 Ps.74). |
| Lampu tiga/dua/satu warna | 3 warna (M-K-H) untuk kendaraan; 2 warna (M-H) untuk kendaraan/pejalan kaki; 1 warna (kuning kedip/merah) untuk peringatan bahaya. | [PM 49 Ps.3–10; PP 79/2013 Ps.42] | Tipe head di model data channel. |
| Merah+kuning (red+amber) | Kuning menyala bersama merah = hijau akan segera menyala, bersiap bergerak. | [PM 49 Ps.6(4)b; PP 79/2013 Ps.43c] | State machine fase harus punya interval `u` (SUMO: `u`). |
| APILL otonom vs terkoordinasi | Otonom: siklus diatur sendiri; terkoordinasi: siklus berinteraksi dengan APILL lain via sistem terpusat. | [PM 49 Ps.4, 12] | Flag mode per simpang. |
| Siklus tetap / semi-adaptif / adaptif | Tetap ≥8 rencana siklus; semi-adaptif tetap di kaki mayor & variabel di minor; adaptif variabel di semua kaki menurut arus. | [PM 49 Ps.13–16] | Enum mode kendali; ≥8 TOD plan wajib. |
| Perangkat kendali (traffic controller) | Unit elektronik yang menjalankan program penyalaan; syarat 5–70 °C, RH ≤95%, modular, ≥8+8 signal group, ≥4 program, conflict monitor. | [PM 49 Ps.24; SK 7234/2013 Bab II] | Atribut controller: signal groups, plans, fault/flash status. |
| Signal group (kelompok sinyal) | Sekumpulan lampu yang selalu menampilkan isyarat sama (padanan channel/stage output). | [SK 7234/2013 Bab II.D.2] | ≥8 kendaraan + 8 pejalan kaki, dikembangkan ≤32. |
| Luminer / armatur | Bagian APILL penghasil cahaya (lampu, armatur, catu daya); optik Ø20–30 cm, LED ≥300/500 cd. | [PM 49 Ps.20; SK 7234 Bab II.5.e] | Inventaris komponen. |
| DIS (Display Info Simpang) | Papan LED di tiang overhead untuk info/hitung mundur 5–7 s, dapat diubah remote dari pusat ATCS, RS-485. | [SK 7234 Bab II.5.i; PM 49 Ps.25] | Perangkat pendamping simpang. |
| Count-down timer | Penghitung mundur menjelang perubahan lampu; boleh dipasang pada APILL. | [SK 7234 Bab II.3.m] | Berpotensi mengganggu koordinasi pejalan kaki [R04 A.8]. |
| Detektor kendaraan (vehicle detector) | Alat pendeteksi keberadaan/kecepatan (magnetik, video, radar), ≥4 zona, output gap & occupancy. | [SK 7234 Bab II.5.h; PM 49 Ps.25] | Wajib untuk APILL adaptif/ATCS [PM 96 Lamp.II.F.d–e]. |
| Detektor stop-bar / advance / setback | Zona di garis henti (presence, antrian) vs 350–400 ft di hulu (arrival profile, decision zone). | [NCHRP 812 §4.1; NCDOT App.B] | Jenis detektor menentukan metrik ATSPM yang bisa dihitung. |
| Decision zone (dilemma zone tipe II) | Area ≈5,5–2,5 s waktu tempuh dari stop bar; max-out/force-off menghilangkan proteksinya. | [NCHRP 812 Exhibit 4-7] | Advance detection & gap reduction. |
| Kamera ANPR (Automatic Number Plate Recognition) | Kamera pembaca TNKB; di ITCS DKI 4 per simpang untuk ETLE/pajak/emisi. | [Majalah h.9; Antara 5051249] | Data pribadi → UU PDP. |
| Kamera Viero / fisheye | Kamera analitik lalu lintas per kaki simpang + kamera 360° di ITCS DKI. | [Majalah h.9] | Sumber deteksi virtual. |
| Junction controller box | Kabinet simpang berisi PoE/industrial switch, edge AI processor, interface RS232 ke controller. | [Majalah h.9] | Edge layer. |
| Kabinet / rumah perangkat kendali | Plat aluminium 2 mm, kotak kendali manual terpisah, pintu berkunci. | [SK 7234 Bab II.5.b] | Alarm pintu = kebutuhan keamanan [TSPH hlm.193]. |
| Police panel / kendali manual | Kotak/peralatan untuk petugas memperpanjang/memperpendek hijau dan kedip. | [SK 7234 Bab II.3.g] | Override petugas wajib diutamakan [UU Ps.104]. |
| Conflict monitor / MMU | Fasilitas mendeteksi conflict green/conflict signal → otomatis flashing. | [SK 7234 Bab II.3.i; NCHRP 812 §4.2] | Status fault wajib dipantau. |
| Flashing (kedip) | Mode operasi kuning kedip (jalan utama) / merah kedip; start-up sequence kuning kedip → kuning tetap. | [SK 7234 Bab II.3.b,e; NTCIP `unitFlashStatus`] | Mode fallback terakhir. |
| VMS / rambu elektronik | Variable Message Sign; subsistem ATMS pemantauan & pengendali rambu elektronik. | [PM 76 Ps.7(2)c; PM 96 Lamp.II.F.e] | Output fungsi khusus dari pusat. |

## B. Konsep waktu sinyal (signal timing)

| Istilah | Definisi | Sumber | Catatan |
|---|---|---|---|
| Fase (phase) | Kondisi APILL dalam satu siklus yang memberi hak jalan pada ≥1 gerakan (Indonesia); di NEMA = proses timing yang melayani ≥1 movement. | [Dirjen 273/1996 Bab I.A.11; NCHRP 812 §5.1.1] | Dukung dua paradigma: stage-based & ring-barrier. |
| Tahap (stage) | Bagian siklus dengan kondisi isyarat konstan (Indonesia); stage-based control umum di luar AS. | [Dirjen 273 Bab I.A.10; arXiv 2308.01952 §II] | SUMO: "fase baru tiap ada sinyal berubah" [R03 B.1]. |
| Movement (pergerakan) | Aksi pengguna di simpang, mis. belok kanan dari utara; 12 gerakan kendaraan + 4 pejalan kaki di simpang 4 kaki. | [NCHRP 812 §3.1] | Entitas Movement. |
| Penomoran fase NEMA | Genap = through (2,6 utama; 4,8 minor), ganjil = belok kiri (AS); 2 & 6 = fase koordinasi. | [NCHRP 812 §5.1.1] | Di Indonesia (lalu lintas kiri) belok kanan = konflik; peta ulang. |
| Ring-and-barrier | Ring = urutan fase saling konflik; barrier = titik kedua ring harus berakhir bersama. | [NCHRP 812 §5.1.2; NTCIP `sequenceTable`] | Fase 1,2,5,6 kompatibel; 3,4,7,8 kompatibel. |
| Overlap | Output terpisah yang dikendalikan parent phase (+) dan modifier phase (−), bisa trailing. | [NCHRP 812 §5.1.4; NTCIP `overlapTable`] | Entitas Overlap. |
| Interval | Durasi indikasi tidak berubah (green/yellow/red/FDW). | [NCHRP 812 Glossary] | — |
| Waktu siklus (cycle length, s / c / C) | Waktu satu urutan fase lengkap; sama untuk semua simpang dalam grup koordinasi. | [PKJI 5.3.4; NCHRP 812 §7.3] | 40–130 s; >130 s dihindari [PKJI hlm.124]. |
| Split | Porsi siklus per fase (hijau + kuning + red clearance), detik atau %. | [NCHRP 812 §7.3; NTCIP `splitTime`] | Σ split ≤ cycle. |
| Offset | Selisih waktu titik acuan siklus lokal terhadap master/system zero. | [NCHRP 812 §7.3; NTCIP `patternOffsetTime`] | Referensi: awal kuning fase koordinasi disarankan [R01 C.3]. |
| Pattern (rencana koordinasi) | Set unik cycle + split + offset + sequence (NTCIP). | [NCHRP 812 §7.3; NTCIP §1.3] | 1–253; 254 Free; 255 Flash. |
| Rencana siklus / TOD plan | Program waktu yang dipilih menurut waktu-hari; PM 49 mensyaratkan ≥8; SK 7234 ≥4–16 program, 10 perubahan/hari. | [PM 49 Ps.14; SK 7234 Bab II.3.a, f.1] | Fallback wajib. |
| Force-off (floating/fixed) | Titik siklus fase non-koordinasi harus berakhir; floating: sisa ke fase koordinasi; fixed: sisa ke fase berikutnya (kurangi early return). | [NCHRP 812 §7.3; NTCIP `coordForceMode`] | Parameter pattern. |
| Permissive period | Jendela controller boleh meninggalkan fase koordinasi ke fase lain. | [NCHRP 812 §7.3] | — |
| Yield point | Awal permissive pertama; titik terawal fase koordinasi boleh diterminasi; titik ganti plan. | [NCHRP 812 §7.3] | — |
| Early return to green | Fase koordinasi mulai lebih awal karena fase minor gap-out → platoon berhenti di hilir. | [NCHRP 812 §7.6] | Sumber penyimpangan green wave. |
| Transisi (dwell/max dwell/add/subtract/shortway) | Metode controller mengejar offset baru saat ganti pattern; ≥30 menit per pattern; selesai ≤3–5 siklus. | [NCHRP 812 §7.5.3; NTCIP `coordCorrectionMode`] | KPI: frekuensi & durasi transisi. |
| Waktu hijau minimum/maksimum (min/max green) | Batas bawah/atas hijau; min dari driver expectancy/queue clearance; max membatasi delay & melindungi dari detektor rusak. | [NCHRP 812 §6.1.3–6.1.4] | Guard-rail: min ≥7–10 s, max ≤60 s [R04 F]. |
| Passage time / gap / unit extension | Timer perpanjangan hijau yang di-reset tiap aktuasi; gap-out bila habis. | [NCHRP 812 §6.1.5; NTCIP `phasePassage`] | — |
| Gap-out / max-out / force-off (terminasi) | Alasan fase berakhir: celah kendaraan habis / mencapai max green / dipaksa koordinasi. | [NCHRP 812 §6.1.5; NTCIP `ringStatus`] | Dasar Phase Termination ATSPM. |
| Gap reduction (volume-density) | Penurunan linier allowable gap dari passage ke minimum gap setelah time/cars before reduction. | [NCHRP 812 §6.1.5; NTCIP phase objects] | — |
| Variable/added initial | Min green bertambah per aktuasi saat merah (1,2–2,0 s/aktuasi) hingga max initial. | [NCHRP 812 Exhibit 6-5] | — |
| Recall (min/max/soft/ped) | Panggilan otomatis ke fase tanpa deteksi; max recall ≈ pretimed. | [NCHRP 812 §6.1.8; NTCIP `phaseOptions`] | Mode gagal detektor. |
| Dual entry | Fase kompatibel ikut menyala meski hanya satu dipanggil. | [NCHRP 812 §6.1.7] | — |
| Memory mode (locking/non-locking) | Panggilan ditahan sampai dilayani (locking) atau hilang saat kendaraan pergi (non-locking). | [NCHRP 812 §6.1.8] | — |
| Kuning (yellow change, wK) | Interval peringatan setelah hijau; Indonesia biasanya 3,0 s; MUTCD 3–6 s. | [PKJI 5.3.3; NCHRP 812 §6.1.1] | Tidak boleh dipotong oleh priority/preempt. |
| Merah semua / all-red (wMS / red clearance) | Interval semua merah untuk pengosongan konflik; dihitung dari jarak & kecepatan. | [PKJI 5-9; NCHRP 812 §6.1.2] | — |
| Waktu antar hijau (wAH / intergreen) | wK + wMS; nilai normal 4/5/6 s untuk simpang kecil/sedang/besar. | [PKJI Tabel 5-1] | — |
| Waktu hijau hilang (wHH / LT / lost time) | Σ(wMS + wK) per siklus. | [PKJI 5-10; Dirjen 273 Bab IV.B] | Input Webster. |
| Walk / FDW / LPI | Interval pejalan kaki: walk ≥7 s (4 s bila rendah), flashing don't walk = clearance, leading pedestrian interval ≥3 s. | [NCHRP 812 §6.1.6] | Tak boleh dipotong priority. |
| Pretimed / semi-actuated / fully-actuated / coordinated | Mode kendali: tanpa deteksi / deteksi minor saja / deteksi semua / common cycle+split+offset. | [NCHRP 812 §3.1.2; FHWA 2008 Tabel 5-1] | Tingkat 0–1 mesin kendali. |
| Traffic responsive (TRPS) | Pemilihan pattern dari pustaka berdasarkan V+K·O detektor sistem (generasi 1). | [NCHRP 812 §9.3; arXiv 2308.01952] | Bukan adaptif. |
| Adaptive signal control (ASCT) | Menghitung ulang parameter timing dari deteksi; "not set-and-forget"; tidak menyelesaikan masalah kapasitas. | [NCHRP 812 §9.4] | Generasi 2–3. |
| Green wave / progression / bandwidth | Koordinasi arteri dengan common cycle + offset agar platoon tidak berhenti; bandwidth = waktu hijau efektif sepanjang koridor. | [NCHRP 812 §7.2; arXiv 2507.22511] | Actuated murni merusak green wave. |
| Time-space diagram (TSD) / cyclic TSD | Diagram jarak vs waktu trajektori platoon; versi cyclic (τ = t mod C) untuk data probe multi-hari. | [NCHRP 812 §7.2.1; arXiv 2212.02315] | Alat evaluasi offset. |
| Double/half cycling | Simpang minor berjalan 2× atau ½ siklus grup. | [NCHRP 812 §7.4] | — |
| Oversaturation / spillback / starvation | DS ≥1; antrian meluber ke simpang hulu; hijau tak terpakai karena antrian hilir. | [NCHRP 812 §12; PKJI 5.3.1] | Toolkit jenuh: split reallocation, gating, negative offset. |
| Gating / metering / perimeter control | Menahan arus di link eksterior/perimeter agar inti tidak jenuh; PI regulator berbasis MFD. | [NCHRP 812 §12.3; arXiv 2210.10453] | Tingkat 2 kendali. |
| Retiming | Peninjauan ulang waktu sinyal; Dirjen ≥1×/3 bulan; praktik AS ≤3 tahun. | [Dirjen 273 Bab I.H; FHWA 2008 §2.3] | Jadwal otomatis. |

## C. Kapasitas & kinerja simpang (PKJI/MKJI/HCM)

| Istilah | Definisi | Sumber | Catatan |
|---|---|---|---|
| smp / skr / SMP (satuan mobil penumpang / PCE) | Satuan arus ekuivalen mobil penumpang; EMP MP 1,0; KS 1,3; SM 0,15 (P) / 0,40 (O); Dirjen: MC 0,2/0,4, UM 0,5/1,0. | [PKJI Tabel 5-2; Dirjen 273 Tabel 3-1] | Perbedaan EMP SM 0,2→0,15 [R05 D.5]. |
| Pendekat tipe P / O (protected/opposed) | P: pelepasan tanpa konflik belok kanan dengan arus lawan; O: dilepas bersama arus lawan. | [PKJI 5.3.3; Dirjen 273 Gambar 5-1] | Menentukan J0 (rumus vs grafik). |
| Mulut persimpangan (MP) / pendekat (approach) | Daerah kaki simpang untuk antrian sebelum garis henti. | [Dirjen 273 Bab I.A.13] | — |
| Lebar efektif (LE / We) | Lebar pendekat yang efektif melepas arus setelah koreksi LTOR & lebar keluar. | [PKJI 5-2, 5-3] | — |
| LTOR / BKiJT (belok kiri jalan terus) | Belok kiri boleh langsung saat merah; dikeluarkan dari analisis bila lajur ≥2 m. | [PKJI 5.3.3; Dirjen 273 Bab V.B] | — |
| Arus jenuh (J / S; saturation flow) | Arus maksimum per jam hijau; J0 = 600·LE (tipe P) × faktor koreksi. | [PKJI 5-4, 5-6] | — |
| Faktor koreksi FUK/FHS/FG/FP/FBKa/FBKi | Ukuran kota / hambatan samping / kelandaian / parkir / belok kanan / belok kiri. | [PKJI Tabel 12-1, 12-3; 5-5, 5-27, 5-28] | FUK Jakarta = 1,05. |
| Rasio arus (Rq/J / FR) & RAS/IFR | q/J per pendekat; RAS = Σ nilai kritis per fase. | [PKJI 5-8, 5-29] | — |
| Kapasitas (C = J·wH/s) | Kapasitas pendekat SMP/jam. | [PKJI 5-1] | — |
| Derajat kejenuhan (DJ / DS / v/c) | q/C; kriteria desain ≤0,85; ≥1 jenuh. | [PKJI 5-14; FHWA 2008 §3.3.5] | Ambang kebijakan MKLL 0,5/0,7/0,85/0,9. |
| Antrian (Nq1, Nq2, NqMAX, PA/QL) | Sisa antrian fase sebelumnya + datang saat merah; PA = Nq·20/LM (m). | [PKJI 5-15…5-18] | POL 5% desain / 5–10% operasi. |
| Rasio kendaraan terhenti (RKH / NS / p_SV) | Proporsi kendaraan berhenti ≥1×; 0,9·Nq·3600/(q·s). | [PKJI 5-19] | — |
| Tundaan (T = TLL + TG) | Tundaan lalu lintas (Akcelik) + tundaan geometrik (belok/berhenti). | [PKJI 5-21…5-23; PM 96 Lamp.I] | Indikator LOS. |
| Tundaan simpang (TI / D_I) | Σ(q·T)/qTotal. | [PKJI 5-32] | — |
| Tingkat pelayanan (LOS) simpang PM 96 | A <5; B 5–15; C 15–25; D 25–40; E 40–60; F >60 det/kend. | [PM 96/2015 Lamp.I Bab II.D] | Wajib untuk dashboard; ≠ HCM. |
| LOS HCM (simpang bersinyal) | A ≤10; B 10–20; C 20–35; D 35–55; E 55–80; F >80 s/veh (control delay). | [FHWA 2008 §3.4.1] | Benchmark internasional; rumus tidak ada di HCM overview. |
| LOS ruas PM 96 | Berdasarkan kecepatan: A ≥80; B ≥70; C ≥60; D ≥50; E ≥30 (≥10 perkotaan); F <30 km/jam. | [PM 96 Lamp.I Bab II.D] | — |
| Control delay (HCM) | Tundaan akibat kendali sinyal (d1 uniform, d2 incremental, d3 initial queue). | [CED HCM overview — rumus tidak ada] | (rumus tidak ada di sumber) |
| Volume vs demand | Volume ≠ demand bila ada antrian. | [NCHRP 812 §3.3.2] | Data quality rule. |
| LHRT / VJP (qJP) / faktor K | Lalu lintas harian rata-rata tahunan; volume jam perencanaan = K×LHRT, K 7–12%. | [PKJI 5-13; PM 96 Lamp.I] | — |
| Travel speed / free-flow speed / TMS / SMS | Kecepatan tempuh (termasuk tundaan berhenti) / kecepatan arus bebas / time & space mean speed. | [PM 96 Lamp.I Bab II.B] | KPI 35 km/jam Perda; 30 km/jam Perpres. |
| Warrant APILL | Kriteria pemasangan: >750 kend/jam ×8 jam; delay >30 s; >175 pejalan kaki/jam; >5 laka/tahun. | [PM 96 Lamp.II.F.b; Dirjen 273 Bab I.D] | Modul kelayakan. |
| Critical movement analysis / QEM | Metode HCM/NCHRP menentukan volume kritis per barrier & cycle awal. | [NCHRP 812 §5.2; FHWA 2008 §3.3] | — |
| Bandwidth efficiency / attainability | (B_A+B_B)/2C; bandwidth / g_crit. | [FHWA 2008 §3.5.1] | KPI koridor. |
| Platoon ratio / arrival type | AoG dinormalisasi proporsi hijau; arrival type 1–6. | [NCDOT A.5; TSPH Tabel 49] | Rumus eksplisit (tidak ada di sumber). |

## D. Kelembagaan, regulasi & program

| Istilah | Definisi | Sumber | Catatan |
|---|---|---|---|
| LLAJ | Lalu Lintas dan Angkutan Jalan. | [UU 22/2009] | — |
| MRLL (manajemen & rekayasa lalu lintas) | Perencanaan, pengadaan, pemasangan, pengaturan, pemeliharaan perlengkapan jalan untuk kamseltibcar. | [UU Ps.1 angka 29, Ps.93–98] | Gubernur untuk jalan provinsi; Polri operasional. |
| MKLL (manajemen kebutuhan lalu lintas / TDM) | Pembatasan kendaraan (perseorangan, barang, motor, parkir, retribusi/ERP). | [UU Ps.133; PP 32 Ps.60–83] | Ambang V/C & kecepatan legal. |
| Andalalin | Analisis dampak lalu lintas pembangunan. | [PP 32 Ps.47–59] | Bukan lingkup ITCS. |
| ERP / PL2SE / retribusi pengendalian lalu lintas | Jalan berbayar elektronik; syarat V/C ≥0,9, ≤10 km/jam, 2×2 lajur, tidak di jalan nasional; 9 ruas & 07.00–20.00 hari kerja di DKI. | [PP 32 Ps.79–83; Perda 5/2014 Ps.78–85] | Integrasi jangka panjang ITCS. |
| KRE (Kawasan Rendah Emisi / LEZ) | Kawasan pembatasan berdasar emisi; target integrasi ITCS jangka panjang. | [Majalah h.4, h.11; PM 96 Lamp.II.H] | — |
| Ganjil-genap | Pembatasan berdasarkan TNKB; 26 ruas DKI; Senin–Jumat 06.00–10.00 & 16.00–21.00; pengecualian ambulans, pemadam, angkutan umum plat kuning, listrik, motor, dll. | [Pergub 155/2018 jo. 88/2019 Ps.1, 3, 4; 76/2020 Ps.4A] | Data harus terintegrasi ke sistem Pemprov [Pergub 68 Ps.13(4)]. |
| ETLE (Electronic Traffic Law Enforcement) | Penindakan pelanggaran dengan alat elektronik sebagai alat bukti; ranah Polri. | [UU Ps.272, 260; PP 32 Ps.46(3)] | ITCS = penyedia bukti, bukan penindak. |
| TNKB / pelat nomor | Tanda Nomor Kendaraan Bermotor; pengenalan TNKB = fungsi SIK LLAJ. | [UU Ps.248] | Data pribadi (UU PDP). |
| PPNS Dishub | Penyidik PNS; hanya pelanggaran Perda Ps.95 (busway, kawasan pengendalian, dll.); di jalan wajib didampingi Polri. | [UU Ps.262; Perda 5/2014 Ps.95] | — |
| SIK LLAJ (Sistem Informasi & Komunikasi LLAJ) | Subsistem terpadu data LLAJ; pusat kendali dikelola Polri; data dapat diakses pembina & masyarakat. | [UU Ps.245–251] | ITCS = subsistem pemprov yang terintegrasi. |
| SMTC / ITS (Sistem Manajemen Transportasi Cerdas) | Proses TI/elektronika/telekomunikasi terintegrasi untuk perencanaan–pengawasan transportasi jalan; 12 jenis. | [PM 76/2021 Ps.1, 6] | Dasar hukum ITCS. |
| ATMS (sistem manajemen lalu lintas tingkat lanjut) | Jenis SMTC: ATCS, pemantauan real time, VMS, kecelakaan, ETLE, waktu tempuh, prioritas bus; semua perangkat online & dapat disetel dari ruang kendali. | [PM 76 Ps.7] | Definisi modul minimal ITCS. |
| ATIS / APTS | Sistem informasi pengguna jalan / transportasi umum tingkat lanjut (termasuk sinyal prioritas bus). | [PM 76 Ps.8, 11] | — |
| ATCS (Area Traffic Control System / Sistem APILL Terkoordinasi) | Pengendalian antar simpang ber-APILL terkoordinasi; ≥3 simpang, ≤1 km, detektor, komunikasi, ruang kendali. | [PM 96 Lamp.II.F.e] | Syarat corridor grouping. |
| ITCS (Intelligent Traffic Control System) | Sebutan Dishub DKI untuk APILL adaptif berbasis AI (recognition + predictive) terhubung TMC + integrasi data. | [Majalah h.4–9] | Objek acuan proyek. |
| Ruang pusat kendali / TMC / UP SPLL | Control Centre Room; di DKI = Unit Pengelola Sistem Pengendalian Lalu Lintas, Jl. Abdul Muis. | [PM 96 Lamp.II.F.e; Majalah h.15–16] | ±25 operator/shift; CRM SLA 3 jam. |
| Forum LLAJ | Forum koordinasi antarinstansi penyelenggara LLAJ; penerima laporan MRLL. | [UU Ps.13, 98; PP 37/2011] | Pelaporan wajib. |
| BPTJ | Badan Pengelola Transportasi Jabodetabek; penyelenggara SMTC jalan nasional di Jabodetabek. | [PM 76 Ps.19(2)b] | Kewenangan simpang jalan nasional. |
| Dirjen Hubdat | Direktur Jenderal Perhubungan Darat; APILL jalan nasional & perpotongan; persetujuan MRLL DKI di jalan nasional. | [PM 49 Ps.28; PM 96 Ps.5(2)] | Workflow persetujuan. |
| Jak Lingko | Sistem transportasi terpadu-terintegrasi DKI (Pergub 68/2021); data interoperabel milik Pemprov. | [Pergub 68 Ps.1, 10–11] | Sumber AVL/headway. |
| RITJ / RIT Jabodetabek | Rencana Induk Transportasi (Perpres 55/2018, target 2029: 60% angkutan umum, ≥30 km/jam). | [Perpres 55/2018 Lamp.] | KPI strategis. |
| Perda 5/2014 target | 60% perjalanan dengan KBU; kecepatan rata-rata jaringan 35 km/jam. | [Perda 5/2014 Ps.8] | KPI publik. |
| Proyek Perubahan / RPP (PKN II) | Dokumen inovasi kepemimpinan LAN: burning platform, milestone jangka pendek/menengah/panjang, stakeholder map, marketing 4P+1C. | [Modul LAN; KepKa LAN 1/2023] | Format dokumen acuan. |
| TSMP / CMF | Traffic Signal Management Plan; Capability Maturity Framework (level 1–4). | [TSPH hlm.22–29] | Tata kelola program. |
| GcOST | Goals → context → Objectives → Strategies → Tactics. | [TSPH hlm.9–17] | — |
| ConOps / System Requirements / Verification / Validation | Dokumen systems engineering; validasi tidak boleh didelegasikan ke vendor; verification plan sebelum RFP. | [HOP-11-027 hlm.11–18] | — |
| NEMA TS 8 | Standar keamanan siber & fisik ITS untuk pengadaan. | [TSPH hlm.192] | — |
| e-Katalog LKPP / TKDN | Katalog pengadaan pemerintah; Tingkat Komponen Dalam Negeri produk ATCS/controller. | [pencarian web 2026-09-12] | Jalur penjualan ke pemda. |
| Data pribadi (UU PDP) | Data orang perseorangan yang teridentifikasi/dapat diidentifikasi; data spesifik termasuk biometrik & catatan kejahatan; pemrosesan berisiko tinggi wajib DPIA; pengendali wajib menunjuk pejabat PDP untuk pelayanan publik. | [UU 27/2022 Ps.1, 4, 16, 20, 34, 53] | ANPR/CCTV/pelat = data pribadi. |

## E. Prioritas, preemption, integrasi

| Istilah | Definisi | Sumber | Catatan |
|---|---|---|---|
| Preemption | Transfer kendali normal ke mode khusus (rel, kendaraan darurat); memutus koordinasi. | [NTCIP 1202; NCHRP 812 §10] | Yellow/all-red tak boleh dipotong. |
| Priority (prioritas) | Perlakuan istimewa satu kelas kendaraan tanpa melepas koordinasi (NTCIP 1211). | [TSP Handbook h.4; NCHRP 812 Exhibit 10-1] | Preempt > priority. |
| TSP (Transit Signal Priority) | Prioritas bus: green extension, early green/red truncation, phase insertion, rotation, queue jump. | [TSP Handbook h.7–8] | Default extension ≤10 s, 1 aktivasi/siklus. |
| Conditional priority | Prioritas hanya bila memenuhi syarat (terlambat ≥2 menit, headway, in-service). | [TSP Handbook h.22, h.61] | Butuh AVL TransJakarta. |
| PRG / PRS | Priority Request Generator (di bus/wayside/center) / Server (di controller/central). | [TSP Handbook h.59–62] | Arsitektur NTCIP 1211. |
| TSD / TED | Time of service desired / time of estimated departure dalam permintaan prioritas. | [NCHRP 812 §10.2] | Scheduling multi-request. |
| Check-in / check-out | Deteksi masuk zona prioritas (100–150 m) / keluar di stop line untuk menghentikan extension. | [TSP Handbook h.66; Lamp.A3] | — |
| Lockout / recovery | Larangan prioritas siklus berikutnya; pemulihan ke koordinasi 1–2 siklus. | [TSP Handbook h.5, h.22] | — |
| EVP (Emergency Vehicle Preemption) | Preempt untuk kendaraan darurat; vehicle-based (optical/RF) vs system-based (AVL/CAD + geofence). | [FHWA HOP-24-019] | Rata-rata 25 s; pulih 1 siklus. |
| Mixed-criticality EVP | Preempt hanya bila target respons terancam; level purple/red/orange; conflict graph multi-EV. | [arXiv 2109.03210] | Desain EVP bertingkat. |
| Track clearance / dwell / exit phase | Fase pengosongan konflik / fase ditahan selama preempt / fase saat keluar. | [NTCIP `preemptTable`; NCHRP 812 §10.5] | — |
| Kendaraan hak utama | Pemadam, ambulans, dst. (UU Ps.134); APILL tidak berlaku bagi mereka. | [UU Ps.134–135] | — |
| VIP green wave | Hijau berurutan untuk kendaraan tertentu sepanjang koridor (fitur TKDN/ITCS). | [Tempo TKDN Solo; PM 76 Ps.7(4)a] | — |
| AVL / APC / CAD | Automatic Vehicle Location / Passenger Counter / Computer-Aided Dispatch. | [TSP Handbook; HOP-24-019] | Sumber data prioritas. |
| MoU integrasi data | Nota kesepahaman Dishub–Polda–Bapenda–DLH–pengelola tol untuk pemanfaatan data ITCS. | [Majalah h.11] | Risiko utama proyek. |

## F. Algoritma & riset

| Istilah | Definisi | Sumber | Catatan |
|---|---|---|---|
| Webster | Rumus siklus optimum C = (1,5L+5)/(1−Y). | [PKJI 5-11; FHWA 2008 Eq.6-1] | Tingkat 0. |
| Generasi kendali UTCS 0–3 | 0 TOD; 1 traffic responsive; 2 adaptive COS adjustment; 3 real-time (tanpa COS). | [arXiv 2308.01952 Tabel I] | — |
| SCOOT | Adaptif Inggris: optimizer split/offset/cycle, hold/force-off ke controller, cyclic flow profile. | [FHWA 2008 §9.4] | Paling luas dipakai. |
| SCATS | Adaptif Australia: hierarkis, pilih split plan dari pustaka, degree of saturation stop-line. | [FHWA 2008 §9.4; R04 A.1] | — |
| RHODES / OPAC / ACS-Lite / InSync / SURTRAC | Rolling-horizon peer-to-peer / virtual fixed cycle / penyesuaian TOD tiap 5–15 menit / video+AI (deployment terbanyak AS) / scheduling MILP Pittsburgh. | [FHWA 2008 §9.4; T414 Tabel 3; R04 A.1] | InSync tidak dibahas NCHRP 812. |
| Max-pressure (MP) | Heuristik terdesentralisasi: pilih fase dengan pressure (antrian hulu − hilir tertimbang) terbesar; maximum stability. | [arXiv 2202.03290; R04 A.4] | Baseline adaptif terkuat. |
| Cyclic MP | MP dengan cycle/offset tetap; hanya mengatur split; min green 7 s; perubahan ≤5 s/siklus; QP integer. | [arXiv 2210.10453 §3.1.1] | Tingkat 2 rekomendasi. |
| OCC-MP / Transit-MP / mTransit-MP | MP dengan bobot occupancy penumpang; versi CV jarang + halte + fallback historis. | [arXiv 2406.19269; 2511.00309] | TSP kondisional. |
| D-MP | MP berbasis delay (dari probe) alih-alih antrian. | [arXiv 2202.03290] | — |
| MFD / perimeter control (PC) | Macroscopic Fundamental Diagram; PI regulator menjaga akumulasi region di setpoint. | [arXiv 2210.10453 §3.2] | PC+MP 25% node = −15,6% VHT. |
| MPC / rolling horizon | Optimasi prediktif 60 s, eksekusi 5 s, ulangi. | [NCHRP 812 §9.4.2.2; R04 A.1] | — |
| RL / MARL / CTDE | Reinforcement learning (single/multi-agent; centralized training decentralized execution); belum pernah deployed. | [arXiv 2206.11996; 2211.14426] | Advisor/shadow mode saja. |
| Invalid action masking | Pembatasan aksi RL ke kombinasi fase legal (ring-barrier). | [arXiv 2603.15283; 2411.19359] | Guard-rail. |
| Digital twin / digital shadow | Twin: koneksi dua arah otomatis fisik↔virtual; shadow: satu arah. | [arXiv 2510.05374; PMC11435829] | SUMO NEMA sebagai twin. |
| SIL / HIL / shadow mode | Software-/hardware-in-the-loop; shadow = keputusan dicatat tak diaktuasi sebelum live. | [arXiv 2510.05374 §8.4] | Protokol validasi. |
| SUMO / TraCI / netconvert / tlLogic | Simulator mikro open-source; API TCP kendali; pembangun jaringan; definisi program lampu (static/actuated/delay_based/NEMA). | [SUMO docs; R03 B] | — |
| sumolights | Framework open-source pembanding controller (Webster, MP, SOTL, DQN, DDPG). | [arXiv 1909.00395] | MP terbaik. |
| Probe / connected vehicle data | Trajektori GPS komersial (3–6% penetrasi) untuk evaluasi koridor. | [arXiv 2212.02315] | GPS TransJakarta/ojol. |
| GLOSA | Green Light Optimal Speed Advisory via SPaT. | [arXiv 2507.22511] | Fitur lanjutan. |
| SPaT / MAP | Pesan V2I status fase & geometri (SAE J2735). | [TSPH hlm.245] | Masa depan. |

## G. Data, protokol & KPI

| Istilah | Definisi | Sumber | Catatan |
|---|---|---|---|
| NTCIP 1202 | Standar objek (MIB) controller sinyal aktuasi via SNMP/STMP; v02 (2005) tanpa TSP/hi-res/SPaT. | [NTCIP §1–2; R03 A] | Model data acuan. |
| Objek tipe C / P / P2 / S | Control (SET langsung) / Parameter / Parameter wajib transaksi / Status read-only. | [NTCIP Annex A.1.1] | Pisahkan perintah vs plan. |
| dbCreateTransaction / consistency check (Annex B) | Transaksi database + verifikasi konsistensi sebelum plan diterapkan. | [NTCIP Annex B, C.4] | Replikasi validasi di server. |
| Backup timer (`unitBackupTime`) | Bila central tidak menulis objek kontrol dalam interval, controller kembali ke mode lokal. | [NTCIP §2.4.3] | Heartbeat wajib; fail-safe. |
| `systemPatternControl` / `systemSyncControl` | Objek pilih pattern (1–253/Free/Flash/Standby) & sinkron siklus. | [NTCIP §2.5.14–15] | — |
| Hold / force-off / omit / veh call (phaseControlGroup) | Primitif kendali fase dari pusat. | [NTCIP §2.2.5] | Dasar TSP/adaptif di central. |
| NTCIP 1211 (SCP) | Standar Signal Control & Prioritization (PRG/PRS). | [TSPH hlm.191; R06 A] | (teks tidak ada di korpus) |
| Block object / OER | Upload/download blok parameter terkodekan OER. | [NTCIP §2.12, §3] | Backup/restore. |
| Conformance group | Kelompok objek wajib/opsional (hanya Phase & Detector wajib). | [NTCIP Annex A.2] | Syaratkan di pengadaan. |
| High-resolution event log | Log event 0,1 s (fase, detektor, preempt, plan) dengan kode enumerasi Indiana. | [HOP-20-002 hlm.9; NCDOT §1.2] | Sumber kebenaran KPI. |
| ATSPM | Automated Traffic Signal Performance Measures dari hi-res log. | [HOP-20-002; NCDOT] | Observer independen algoritma. |
| PCD (Purdue Coordination Diagram) | Plot kedatangan (advance detector) vs waktu-dalam-siklus; AoG & platoon ratio. | [NCDOT A.5] | Penalaan offset. |
| AoG / AoR | Percent arrivals on green / on red. | [NCHRP 812 Exhibit 3-17; NCDOT A.5, A.11] | — |
| Split failure (GOR & ROR5) | Green occupancy ratio & red occupancy ratio 5 s pertama keduanya ≥80%. | [NCDOT A.8; HOP-20-002 hlm.24] | Butuh stop-bar presence. |
| Phase termination / split monitor | Klasifikasi gap/max/force-off/skip per siklus; durasi aktual vs split. | [NCDOT A.1–A.2] | Tanpa detektor tambahan. |
| Approach delay / ped delay / preemption details / YRA | Delay dari aktuasi advance ke hijau / tombol ke walk / waktu request-service-dwell / yellow & red actuations. | [NCDOT A.3, A.4, A.10, A.13] | — |
| Watchdog | Job harian: no data <500 rekaman; force-off/max-out >90% (≥50 aktivasi 01–05); advance <100 kend 17–18; stuck ped >200. | [HOP-20-002 hlm.20] | Alert → work order. |
| Link Pivot | Optimasi offset koridor dari distribusi kedatangan hulu-hilir. | [NCDOT A.6] | Rumus (tidak ada di sumber). |
| Purdue/Indiana enumerations | Kode event hi-res lintas vendor. | [NCDOT App.C] | Angka kode wajib diverifikasi. |
| Interoperabilitas / interkoneksi | Kemampuan data dibagipakaikan antar sistem / keterhubungan jaringan telekomunikasi. | [Pergub 68 Ps.1 angka 4–5] | Kriteria desain. |
| Travel time reliability (PTI, BTI) | Planning time index, buffer time index dari distribusi waktu tempuh. | [TSPH Tabel 48; NYSERDA] | KPI koridor. |
| Before–after vs on–off | Desain evaluasi: sebelum/sesudah instalasi vs adaptif on/off bergantian setelah instalasi. | [T414 hlm.58; NYSERDA hlm.2] | Modul evaluasi. |
| CRM / call center Dishub | Sistem pengaduan; SLA penyelesaian maks 3 jam. | [BeritaJakarta 145079] | Integrasi tiket. |
| TomTom Traffic Index | Indeks kemacetan kota (Jakarta 2023 rank 30/31, 53% → 2024 rank 90, 43%; Bandung #12, Medan #15). | [Antara 5050989; pencarian 2026-09-12] | Konteks, bukan KPI internal. |

**Pointer ke detail**
- Regulasi & pasal: `03_Peta_Regulasi_Kepatuhan.md`; R05; R00 B–H.
- Rumus: `02_Lembar_Rumus.md`; R01 B; R05 D; R00 G.
- Signal timing & koordinasi: R01 B–C; NTCIP: R03 A; ATSPM: R03 C.
- Algoritma: R04 A–F; TSP/EVP: R06 A–B; konteks Jakarta: R06 D; ANALISIS_MAJALAH.
