# 04 — Konsep Tahapan Pengembangan (Tahap 1–5)

Status: draf pra-perencanaan, 2026-09-12. Semua angka server/durasi/tim adalah **ASUMSI** untuk diputuskan di planning rinci. Tag sumber: [R00]…[R06] = catatan studi di `docs/sources/_ringkasan/`; [KB] = basis pengetahuan; [Majalah] = analisis majalah RPP.

## 0. Prinsip desain lintas tahap (berlaku sejak T1)

| # | Prinsip | Alasan lapangan / sumber |
|---|---|---|
| P1 | **Edge-first & fail-safe**: controller lokal selalu memegang ≥8 rencana siklus TOD dan mode actuated sendiri; pusat hanya mengirim "perintah tipe C" + heartbeat; putus komunikasi → kembali ke TOD lokal tanpa gangguan | PM 49/2014 Ps.14 (≥8 rencana siklus); NTCIP `unitBackupTime` [R03 A.6]; kendala komunikasi/detektor = penyebab utama ATCS gagal [R02 F.5, R06 E.4] |
| P2 | **Standar terbuka**: model data & antarmuka meniru NTCIP 1202 (v03 ke depan) / 1211; controller non-standar dijembatani adaptor RS-232 di edge; tidak ada lock-in vendor | PM 76/2021 Ps.4 "sistem terbuka, sesuai standar"; TSPH hlm. 189 [R02 G.7]; [R03 D.2] |
| P3 | **Anti black-box**: setiap keputusan kendali menyimpan input & nilai perhitungan antara; ATSPM/PKJI berjalan sebagai *observer* independen | HOP-11-027 Req 18.0-1/2, 6.0-11 [R02 D.16]; HOP-20-002 p.29 [R03 C.5]; klaim ITCS DKI tanpa MOE [R06 D.1] |
| P4 | **Hemat server**: agregasi & kompresi di edge, hi-res log dikirim batch, retensi bertingkat, video tidak disimpan di pusat (T1–T3) | ±23 MB/simpang/hari hi-res [R03 C.1]; resource pemda terbatas (mandat user) |
| P5 | **Bertahap per koridor**: unit deployment = koridor ≥3 simpang berjarak ≤1 km, dengan before–after on/off | PM 96/2015 Lampiran II.F.e [R00 E]; STM2 §9.4.5 & T414 (65% agensi hanya 5–15 sinyal adaptif) [R01 D.6, R02 F.5] |
| P6 | **KPI regulasi built-in**: LOS PM 96/2015, rumus PKJI 2023, laporan Forum LLAJ/Dirjen/Gubernur otomatis | [R05 E, G.2]; [R00 E, G] |
| P7 | **Human-in-the-loop**: override operator & petugas Polri didahulukan; mode manual tercatat; tidak ada penindakan otomatis oleh aplikasi | UU 22/2009 Ps.104, 247, 272 [R05 A.1, G.3] |
| P8 | **Kreatif tapi berpijak**: fitur baru harus menjawab kendala terdokumentasi (detektor rusak, SDM, pemeliharaan, detik prioritas "menyusut", data tidak tunggal) | [R06 E.4]; TSP Handbook h.23 [R06 A.4]; MTI "single data" [R06 D.6] |

## 1. Ringkasan lima tahap

| Tahap | Nama kerja | Satu kalimat | Unit deployment | Status akhir |
|---|---|---|---|---|
| **T1** | MVP "Lihat & Kelola" | Inventaris APILL + status real-time + plan TOD terkelola + KPI PKJI/PM 96 dari data yang sudah ada — tanpa mengubah kendali lapangan | 1 koridor (3–5 simpang) pilot, simulasi SUMO sebagai controller | Checkpoint internal; bukti konsep dapat didemokan |
| **T2** | Siap jual "Kendali Terkoordinasi" | Central TOD/koordinasi (pattern, offset, transisi), health monitoring & alarm, tiket keluhan, ATSPM dasar dari log controller, laporan wajib — berjalan di 1 VM/on-prem mini | 1 kota kecil–sedang (10–40 simpang) | Produk komersial v1 untuk pemda dengan ATCS dasar/CCTV |
| **T3** | Transisi "Responsif" | Traffic-responsive plan selection, actuated dari kamera/loop, green wave dengan penalaan offset berbasis probe, TSP sederhana, digital twin per koridor, ETLE-ready (bukti) | 1–3 koridor adaptif di kota besar | Versi antara; membuktikan manfaat terukur sebelum adaptif penuh |
| **T4** | Setara ITCS "Adaptif Terpadu" | Cyclic max-pressure terkoordinasi + perimeter control, TSP kondisional & EVP bertingkat, integrasi ETLE/pajak/emisi/AVL/CAD, TMC multi-koridor, AI recognition/predictive sebagai layanan | Kota besar 50–300+ simpang | Setara fungsi ITCS DKI (bukan tiruan) |
| **T5** | End-state "Platform Mobilitas Kota" | Multi-tenant lintas kota, digital twin kota, marketplace algoritma via shadow mode, TDM berbasis data (ganjil-genap/ERP), data terbuka publik, analitik probe, RL advisor | Regional/nasional | Rekomendasi end-state (melampaui ITCS) |

Mengapa "setara ITCS" tercapai di **T4**: seluruh subsistem ATMS yang diwajibkan PM 76/2021 Ps.7(2) (ATCS, pemantauan real time, VMS, insiden, ETLE, waktu tempuh, prioritas bus) dan layanan Ps.7(4) (prioritas kendaraan khusus, pemantauan visual, informasi, penindakan, deteksi kerusakan, rekaman operasional & historis, kecepatan) sudah lengkap, ditambah fitur yang diklaim ITCS DKI (actuated, self-adaptive, green wave, bus priority, recognition, predictive, digital twin) [Majalah §4; R06 D.2]. Yang melampaui di **T5**: multi-kota, keterbukaan data (UU Ps.250), TDM berbasis data (PP 32 Ps.65–79 ambang V/C & kecepatan), marketplace algoritma yang tervalidasi shadow-mode, dan analitik probe tanpa detektor.

## 2. Tahap 1 — MVP "Lihat & Kelola"

**Tujuan.** Membuktikan bahwa platform dapat memodelkan simpang/APILL/plan sesuai standar Indonesia, menampilkan status & KPI, dan mengelola rencana waktu — dengan controller *simulasi* (SUMO NEMA) dan/atau 1 controller nyata read-only.

**Definisi selesai (exit criteria).**
1. Inventaris ≥5 simpang lengkap (geometri pendekat, fase/tahap, detektor, aset PM 49) dan peta status real-time dari SUMO/TraCI.
2. Kalkulator PKJI 2023 lulus uji terhadap contoh perhitungan Dirjen 273/1996 (Yogyakarta: c=70 s, g=28/30 s, C=824, DS=0,44) dan MKJI [R00 G].
3. Plan manager menyimpan ≥8 plan TOD per simpang, memvalidasi kuning/all-red (ITE) dan konsistensi ring/barrier (Annex B) sebelum "download" ke simulator.
4. Pipeline hi-res event (0,1 s) dari `whetherOutputState` SUMO → 4 metrik ATSPM (phase termination, split monitor, PCD/AoG, split failure).
5. Dashboard LOS PM 96/2015 per simpang & laporan before–after (on/off di simulasi).
6. Demo end-to-end 20 menit tanpa intervensi engineer.

**Nilai bagi pembeli (calon).** Bukti bahwa produk memahami regulasi Indonesia (PKJI, PM 49, PM 96) dan bisa dipakai tanpa mengganti controller.

**Lingkup inti.** Inventaris & aset; peta & status; plan manager + kalkulator; adaptor simulasi (TraCI) + 1 adaptor read-only (NTCIP GET atau parser log vendor); ATSPM dasar; KPI/LOS; RBAC dasar; audit log. Detail di file 05 (F-T1-xx).

**Asumsi infrastruktur.** 1 laptop/VM 4 vCPU/16 GB; Docker Compose; PostgreSQL+Timescale; SUMO lokal. Tidak ada video.

**Sumber data realistis.** SUMO; contoh data survei manual (LHR, geometri) dari dokumen Dishub; log controller vendor (bila tersedia) sebagai file.

**Integrasi.** Tidak ada integrasi eksternal (sengaja).

**Kepatuhan yang dicapai.** C-06/07 (jadwal pemeliharaan 6 bulan, umur 5 tahun), C-09 (≥8 plan), C-30 (LOS PM 96), C-19 sebagian (simulasi sebelum penetapan) [R05 G.1].

**Validasi.** SIL (SUMO) saja; uji regresi kalkulator terhadap contoh resmi.

**Durasi & tim (ASUMSI).** 8–12 minggu; 3–4 orang (1 backend, 1 frontend, 1 traffic engineer paruh waktu, 1 PM/QA).

**Risiko.** Under-estimasi kompleksitas ring/stage (Indonesia stage-based vs NEMA ring) [R00 I]; grafik PKJI tipe O/F_G/NQ perlu digitalisasi [R00 G].

**Sengaja TIDAK dilakukan.** Kendali controller nyata; video; adaptif; integrasi instansi; AI kamera.

## 3. Tahap 2 — Siap Jual "Kendali Terkoordinasi"

**Tujuan.** Produk yang bisa dijual ke pemda yang sudah punya APILL/ATCS dasar + CCTV: kendali terpusat TOD & koordinasi, kesehatan perangkat, keluhan, laporan — hemat server.

**Definisi selesai.**
1. Dua adaptor lapangan berjalan di edge: NTCIP 1202 (SNMP) dan minimal 1 protokol vendor RS-232 lokal (mis. controller di e-katalog) dengan pemetaan ke model data yang sama; heartbeat < `unitBackupTime`; fallback TOD lokal teruji dengan mencabut jaringan [R03 A.15].
2. Pattern/offset/split dapat diubah dari TMC melalui transaksi tervalidasi; transisi terpantau (frekuensi transisi = KPI) [R01 C.6].
3. Health monitoring: detektor gagal (no activity/max presence/erratic), komunikasi (poll sukses), clock drift, flash/conflict, pintu kabinet; watchdog harian ambang HOP-20-002; alarm → tiket [R01 G.2, R03 C.3].
4. Tiket keluhan publik dengan SLA (SOP DKI: 3 jam) & matriks diagnosis Exhibit 8-17 [R01 G.2, R06 D.3].
5. ATSPM dari log controller nyata (bila controller punya logger) atau dari edge logger; PCD/AoG untuk ≥1 koridor.
6. Laporan otomatis: LOS before–after per kebijakan (PM 96 Bab VI), laporan MRLL ke Forum LLAJ (UU Ps.98), kajian kecepatan & V/C (PM 96 Lampiran III), laporan triwulan (Pergub 68) [R05 G.1].
7. Integrasi CCTV eksisting sebagai *live view* (RTSP→WebRTC) tanpa perekaman di pusat.
8. Berjalan stabil 30 hari di 1 VM 8 vCPU/32 GB (ASUMSI) untuk ≤40 simpang, ≤60 kamera view.
9. Dokumen pemasaran: bukti manfaat dari pilot (on/off) dalam bahasa PKJI/PM 96.

**Nilai bagi pembeli.** Mengubah ATCS "CCTV + remote plan" menjadi sistem yang bisa dipertanggungjawabkan (KPI, laporan, SLA), tanpa ganti controller & tanpa server besar; siap e-katalog.

**Lingkup inti.** Semua T1 + adaptor nyata, TMC console, override manual & log Polri, alarm/health/watchdog, tiket, laporan wajib, CCTV live, TOD scheduler & special plans manual, user/tenant tunggal, mobile teknisi (field diary).

**Asumsi infrastruktur.** 1 VM 8 vCPU/32 GB/1 TB atau mini-server on-prem di kantor Dishub; edge gateway per simpang atau per kabinet (Raspberry Pi/industrial PC); komunikasi eksisting (fiber/4G).

**Sumber data.** Log controller/edge logger; detektor eksisting (loop/video) via controller; survei manual untuk kalibrasi PKJI; CCTV.

**Integrasi.** CRM/aduan kota (opsional), email/WhatsApp alarm, SSO pemda (opsional).

**Kepatuhan.** C-01…C-09, C-15, C-18, C-20, C-21, C-26, C-27, C-33, C-35 [R05 G.1]; PM 76 Ps.7(3) (semua perangkat online & dapat diubah dari ruang kendali) untuk simpang ter-cakup.

**Validasi.** HIL dengan 1 controller di bench → shadow (perintah dicatat, tidak dikirim) 2 minggu → live off-peak → on/off before–after 4 minggu.

**Durasi & tim (ASUMSI).** 4–6 bulan setelah T1; 5–7 orang (+1 embedded/edge, +1 field engineer).

**Risiko.** Protokol vendor tertutup (mitigasi: edge logger I/O kabinet seperti NCDOT, adaptor generik); kualitas komunikasi pemda; kepemilikan data log oleh vendor lama [R03 C.5]; SDM operator [R02 F.5].

**Sengaja TIDAK dilakukan.** Adaptif real-time; AI kamera; integrasi Polda/Bapenda/DLH; penyimpanan video; multi-tenant.

## 4. Tahap 3 — Transisi "Responsif"

**Tujuan.** Menambahkan kecerdasan bertahap yang manfaatnya terukur sebelum adaptif penuh: traffic-responsive plan selection, actuated berbasis detektor kamera, green wave tertala data, TSP sederhana, digital twin per koridor.

**Definisi selesai.**
1. TRPS (V+K·O, hysteresis, dwell ≥30 menit) beroperasi pada ≥1 koridor dengan pustaka ≥6 pattern [R01 D.3].
2. Detektor virtual dari kamera AI di edge (count/occupancy per lajur) dengan health check; actuated/semi-actuated diaktifkan pada simpang yang lulus health check ≥7 hari [C-12].
3. Penalaan offset berbasis probe GPS (cyclic TSD/PPD, Link Pivot) menaikkan AoG koridor pilot ≥10 poin (target; ASUMSI) [R04 A.19, R03 C.3].
4. Digital twin SUMO per koridor terkalibrasi (galat volume ≤15%, ASUMSI) dan dipakai untuk uji plan sebelum penetapan (PM 96 "harus disimulasikan").
5. TSP sederhana (green extension/early green ≤10 s, 1 aktivasi/siklus, lockout) untuk koridor bus dengan AVL; dampak side-street terukur [R06 F.2].
6. Modul bukti ETLE-ready: event pelanggaran (mis. red-light running dari YRA) dengan bukti & metadata siap diserahkan ke Polri — bukan penindakan [C-24].
7. Special-condition plans (insiden/banjir/event) dengan trigger & kriteria deaktivasi [R01 F].

**Nilai bagi pembeli.** Manfaat kelancaran terukur (travel time, AoG, split failure) dengan investasi detektor minimal; jalur menuju ITCS tanpa "big bang".

**Asumsi infrastruktur.** Edge AI box per simpang terpilih (GPU ringan) atau kamera dengan analitik bawaan; pusat 2 VM (aplikasi + data) atau 1 server 16 vCPU/64 GB (ASUMSI); simulasi di worker terpisah.

**Sumber data.** Kamera AI (count/occupancy), probe GPS (bus/ojol/aplikasi navigasi via kerja sama), AVL TransJakarta/BRT kota, log hi-res.

**Integrasi.** AVL operator bus; penyedia probe; sistem informasi pemda (JSC-like).

**Kepatuhan.** + C-11 (ATCS ≥3 simpang), C-12, C-13, C-14 (prioritas angkutan umum), C-19 penuh (simulasi), C-24 (ETLE hanya bukti), UU PDP untuk data pelat.

**Validasi.** SIL (twin) → shadow → live off-peak → on/off; ATSPM sebagai observer; evaluasi bertahap pra-optimasi/pasca-optimasi/pasca-TSP [R06 A.9].

**Durasi & tim (ASUMSI).** 6–9 bulan; 8–10 orang (+ML/vision engineer, +data engineer).

**Risiko.** Kualitas deteksi kamera saat hujan/malam [R04 A.2]; penetrasi probe rendah (agregasi multi-hari) [R04 A.19]; MoU AVL.

**Sengaja TIDAK dilakukan.** Max-pressure penuh; perimeter control; EVP jaringan; integrasi pajak/emisi.

## 5. Tahap 4 — Setara ITCS "Adaptif Terpadu"

**Tujuan.** Setara fungsi ITCS DKI: adaptif real-time terkoordinasi, prioritas kondisional & darurat, integrasi lintas instansi, TMC skala kota, AI recognition/predictive.

**Definisi selesai.**
1. **Cyclic max-pressure terkoordinasi** (cycle & offset tetap per koridor; MP mengatur split; min green ≥7–10 s; perubahan ≤5 s/siklus; integer) aktif di simpang kritis terpilih (skor okupansi/varians/durasi ≥80%) ≥20% simpang kota; **perimeter control** CBD dengan hysteresis [R04 A.5, F].
2. **TSP kondisional** berbasis occupancy/headway (OCC/Transit-MP; bus di halte tidak dihitung; fallback historis) dan **EVP bertingkat** (hanya bila target respons terancam; conflict graph; recovery ke koordinasi) dengan AVL/CAD pemadam & ambulans [R04 A.6–A.7, A.18].
3. Integrasi API: ETLE Polda (bukti), Bapenda (status pajak per pelat, query), DLH (uji emisi agregat per ruas), pengelola tol, JSC/portal kota — semua via perjanjian & kontrol PDP [R06 F.4].
4. AI recognition (jenis kendaraan, pelat, pelanggaran) & predictive (prakiraan volume 15–60 menit; hijau maksimum optimal) sebagai layanan dengan nilai antara transparan.
5. TMC skala kota: video wall, ≥25 operator/shift, SLA keluhan 3 jam, laporan efektivitas ke Dirjen/BPTJ/Gubernur [R06 D.3].
6. Bukti manfaat on/off pada ≥3 koridor: tundaan/LOS PM 96, travel time, AoG, split failure, side-street delay.
7. Keamanan: NEMA TS 8, mTLS edge, RBAC per yurisdiksi, audit penuh.

**Nilai bagi pembeli.** Kota besar mendapat kemampuan ITCS dengan standar terbuka, biaya server terkendali, dan bukti manfaat yang bisa dipertanggungjawabkan ke DPRD.

**Asumsi infrastruktur.** Cluster kecil (3 node) atau cloud pemda; TimescaleDB terpartisi; message bus; edge AI di simpang kritis; k8s opsional.

**Sumber data.** Kamera AI, ANPR, loop/radar, AVL, CAD, probe, cuaca, event kota.

**Kepatuhan.** Seluruh C-01…C-35; PM 76 Ps.7 lengkap; UU PDP; NTCIP 1211 untuk prioritas.

**Validasi.** Seperti T3 + uji konflik TSP/EVP/VVIP di twin; audit keamanan; evaluasi keselamatan (crash review).

**Durasi & tim (ASUMSI).** 9–15 bulan; 12–18 orang.

**Risiko.** Kewenangan Polri/BPTJ (mitigasi: workflow persetujuan & integrasi pusat kendali) [R05 A.1]; MoU antar-instansi (risiko RPP DKI) [Majalah §3.1]; side-street delay naik [R02 F.2]; SDM (30% agensi tidak paham prinsip ASCT) [R02 F.5].

**Sengaja TIDAK dilakukan.** RL sebagai pengendali langsung; ERP; multi-kota.

## 6. Tahap 5 — End-state "Platform Mobilitas Kota" (rekomendasi)

**Tujuan.** Melampaui ITCS satu kota menjadi platform mobilitas multi-kota yang terbuka, dapat diaudit, dan berkembang lewat algoritma tervalidasi.

**Komponen rekomendasi (kreatif, berpijak pada kebutuhan).**
1. **Multi-tenant lintas kota** dengan benchmark antar kota (AoG, LOS, uptime) — menjawab kebutuhan Kemenhub/BPTJ mengawasi efektivitas (PM 76 Ps.22–24) dan pemda kecil berbagi TMC (T414: agensi kecil 5–15 sinyal).
2. **Digital twin kota** (SUMO mesoscopic + mikro per koridor) untuk what-if kebijakan (ganjil-genap, penutupan jalan, event) — PM 96 mewajibkan simulasi sebelum penetapan.
3. **Marketplace algoritma dengan shadow mode**: algoritma pihak ketiga/universitas diuji di twin → shadow → live bertahap, dengan lapisan veto statistik [R04 A.3, A.15]; mengubah riset lokal menjadi manfaat terukur.
4. **TDM berbasis data**: ambang legal V/C ≥0,7 & <30 km/jam (perseorangan), ≥0,9 & ≤10 km/jam (ERP) dihitung otomatis per ruas → rekomendasi kebijakan & evaluasi tahunan wajib (PP 32 Ps.63) [R05 A.2]; integrasi ganjil-genap/ERP.
5. **Data terbuka publik & API** (UU Ps.250; Perda Ps.233): status simpang, LOS, waktu tempuh, log prioritas (anonim) — membangun kepercayaan & mengundang inovasi (MTI "single data").
6. **Analitik probe tanpa detektor** untuk kota yang belum punya detektor: evaluasi progression dari GPS penetrasi 3–6% [R04 A.19].
7. **RL/AI sebagai advisor** (penala parameter MP/setpoint PC), bukan pengendali; pelatihan multi-OD; shadow mode [R04 A.16].
8. **Keselamatan & VRU**: fusi kamera+radar untuk konflik pejalan kaki, YRA, LPI otomatis [R04 A.3].
9. **Layanan ekosistem**: GLOSA/SPaT ke aplikasi navigasi (PM 76 Ps.8 ATIS), informasi headway TransJakarta/BRT, emisi per koridor.
10. **Tata kelola SDM**: e-learning bersertifikat (matriks Mampu/Mau RPP), core competencies (TSPH), audit perubahan detik prioritas (MoU digital).

**Asumsi infrastruktur.** Cloud multi-region atau data center pemerintah; k8s; data lake; tenant isolation.

**Definisi selesai (indikatif).** ≥3 kota tenant; ≥1 algoritma eksternal lulus shadow→live; API publik dengan SLA; evaluasi TDM tahunan otomatis untuk ≥1 kota.

## 7. Tabel perbandingan: ITCS DKI vs T4 vs T5

| Fitur | ITCS DKI (klaim majalah/berita) | T4 | T5 |
|---|---|---|---|
| Deteksi lapangan | 4 kamera analitik + fisheye + 4 ANPR per simpang, edge AI, RS232 ke controller [Majalah §3.4] | Kamera AI/ANPR/loop/radar; adaptor NTCIP & RS-232; virtual detector | + fusi radar untuk VRU; probe tanpa detektor |
| Kendali | Actuated, self-adaptive, coordinated green wave, VIP green wave, bus priority [R06 D.2] | Cyclic MP terkoordinasi + PC, TRPS, actuated, TSP kondisional, EVP bertingkat | + marketplace algoritma, RL advisor |
| AI | Recognition, predictive, digital twin 3D | Recognition, predictive (nilai antara transparan), twin per koridor | Twin kota, what-if kebijakan |
| Integrasi | ETLE, Bapenda, DLH, tol; KRE & PL2SE (rencana) | ETLE (bukti), Bapenda, DLH, tol, AVL, CAD, JSC | + ERP/ganjil-genap berbasis data, API publik |
| TMC | Video wall, 25 operator/shift, CRM SLA 3 jam | Sama + ATSPM observer, laporan wajib otomatis | Multi-kota, benchmark |
| Evaluasi | Klaim 20–30% tanpa MOE | On/off before–after, LOS PM 96, AoG, split failure | + evaluasi TDM tahunan, audit publik |
| Standar | Tidak dipublikasikan (vendor) | NTCIP 1202/1211, NEMA TS 8, PKJI, PM 96 | + data terbuka, ISO 23247 twin |
| Skala | 321 simpang satu kota | 50–300+ simpang satu kota | Regional/nasional |

## 7b. Revisi setelah keputusan user 2026-09-13 (berlaku di atas teks di atas)
- **Tim 2 orang, tanpa field engineer, dana terbatas (U-06):** T1 = simulation-first (SUMO + data rekaman/survei sendiri, tanpa edge, tanpa akses sistem Dishub); T2 "siap jual" = **demo stabil + paket kesiapan pilot** (edge agent yang dipasang teknisi Dishub/vendor dengan checklist, remote support), bukan deployment oleh tim sendiri. Durasi realistis: T1 3–4 bulan, T2 6–9 bulan [asumsi]. Hanya fitur Must yang dikerjakan sebelum ada pembeli.
- **Edge-light di T2 (U-03):** agen edge minimal (adaptor + buffer + heartbeat) di mini-PC/Pi hanya untuk controller serial-only; controller IP dipoll dari pusat; edge penuh (AI box, provisioning armada, OTA) pindah ke T3.
- **Pelat kendaraan diproses sendiri sejak T3 (U-08):** F-T4-125 (ANPR) maju ke T3 sebagai output; konsekuensi: DPIA, kebijakan privasi, pejabat PDP (C-37…C-39) dan F-T3-116 wajib selesai sebelum fitur aktif.
- **Pilot Bandung (U-02):** unit pilot = 1 koridor 3–5 simpang di Bandung; design partner Dishub Kota Bandung dicari sejak akhir T1; Surabaya target ke-2.
- **Pengadaan & data:** lihat `11_Kebutuhan_Pengadaan_per_Tahap.md` dan `13_Kebutuhan_Data_per_Tahap.md`; survei controller: `12_Kuesioner_Survei_Kontroler.md`.

## 8. Prasyarat lintas tahap sebelum planning rinci
- Keputusan nama & positioning (file 01–02), kota pilot & mitra vendor controller lokal (file 03).
- Keputusan arsitektur awal (file 06) & ADR.
- Kesediaan 1 controller bench + akses protokol (NTCIP atau dokumentasi RS-232) untuk T2.
- Akses data pilot: LHR/geometri simpang, log controller, CCTV RTSP.
