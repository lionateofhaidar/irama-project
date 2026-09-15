# 04 — Katalog Kebutuhan Terkonsolidasi (KB-REQ)

**Cara pakai.** Ini SATU daftar kebutuhan kandidat untuk aplikasi ITCS, hasil penggabungan & deduplikasi dari R01 (manual timing), R02 (ASCT systems engineering, ID `ITCS-*`), R03 (NTCIP/SUMO/ATSPM), R04 (paper), R05 (regulasi, ID `C-*`), R06 (TSP/EVP/konteks, ID `F-*`), dan R00 (bacaan langsung). Setiap baris = satu pernyataan "Sistem harus…" yang dapat diverifikasi. Kolom **Tahap** mengikuti tahapan kanonis `docs/planning/04` (T1 Purwarupa Hitung dan Rekomendasi; T2 Vision Tracker dan Optimasi Simpang; T3 Deteksi Kejadian dan Pemantauan Operasional; T4 Kendali Adaptif Terpadu; T5 Platform Mobilitas Kota) dan diselaraskan pada 2026-09-15 dengan inventaris fitur `docs/planning/05`. Nilai yang berubah ditandai "(dulu …)" menurut skema lama 2026-09-12 (T1 MVP monitoring + plan management + KPI; T2 siap jual, server terbatas; T3 transisi adaptif; T4 setara ITCS; T5 end-state). Kolom ini tetap usulan untuk SRS; bila bertentangan dengan `05`, ikuti `05`. Nilai "XX" harus ditetapkan saat planning rinci. Kolom **Verif**: D = Demonstration, T = Test, A = Analyze, I = Inspection (FHWA HOP-11-027 hlm. 58).

Tag sumber: `R02:ITCS-NET-01` = R02 bagian H.1 ID ITCS-NET-01; `R05:C-07` = R05 G.1 C-07; `R06:F-03` = R06 F.1 F-03; `R01:I.3-5` = R01 bagian I.3 butir 5; `R03:D.2` = R03 bagian D.2; `R04:F-GR3` = R04 bagian F guard-rail 3; `R00:B` = R00 bagian B; `PM49 Ps.14` = pasal regulasi.

---

## A. Kebutuhan fungsional

### A1. Hukum & tata kelola (Kategori: Hukum)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-001 | memodelkan status jalan (nasional/provinsi/kota/tol) per simpang dan menandai simpang yang memerlukan persetujuan Dirjen Hubdat/BPTJ sebelum perubahan rencana, dengan workflow persetujuan & arsip surat. | R05:C-01; PM 49 Ps.28; PM 96 Ps.5(2); PM 76 Ps.19 | Wajib hukum | T1 (atribut status jalan), **T3** (alur persetujuan) (dulu T2) | I |
| KB-REQ-002 | menyimpan referensi Keputusan Gubernur/izin Kepala Dinas untuk setiap aset APILL dan menolak status "aktif" tanpa referensi izin. | R05:C-02, C-04; Perda 5/2014 Ps.74 | Wajib hukum | **T3** (dulu T2) | I |
| KB-REQ-003 | mencatat tanggal pemasangan tiap APILL dan menghitung tanggal berlaku kekuatan hukum (30 hari) serta tenggat 60 hari sejak pemberlakuan Perda/Permen. | R05:C-03; UU 22/2009 Ps.102 | Wajib hukum | **T3** (dulu T2) | T |
| KB-REQ-004 | menyimpan nomor sertifikasi setiap perangkat TI di APILL (detektor, kamera, DIS, controller) dan stiker logo perhubungan sebagai atribut aset. | R05:C-05; PM 49 Ps.21, Ps.25(3) | Wajib hukum | **T3** (dulu T2) | I |
| KB-REQ-005 | menyediakan mode override manual petugas Polri/TMC yang didahulukan atas logika otomatis, dengan log siapa-kapan-mengapa. | R05:C-15; UU Ps.104; PP 32 Ps.34–35 | Wajib hukum | **T4** (dulu T1) | D |
| KB-REQ-006 | memberi notifikasi ke Polri/TMC dan mencatat insiden saat APILL "tidak berfungsi" (flash/fault/offline). | R05:C-18; PP 32 Ps.34 b | Wajib hukum | **T3** (dari kamera), **T4** (dari controller) (dulu T1) | T |
| KB-REQ-007 | mendukung preemption kendaraan hak utama sesuai urutan UU Ps.134 (pemadam > ambulans > …) dengan verifikasi permintaan. | R05:C-16; UU Ps.135(3); PM 76 Ps.7(4)a | Wajib hukum | **T4** (dulu T3) | D |
| KB-REQ-008 | menyimpan hasil simulasi dan bukti sosialisasi sebelum kebijakan lalu lintas (fase, larangan belok, satu arah) ditetapkan. | R05:C-19; PM 96 Lamp. I II.E, III.C | Wajib hukum | **T2** (bukti simulasi), T3 (lengkap dengan sosialisasi) (dulu T3) | I |
| KB-REQ-009 | menghasilkan laporan before–after LOS per kebijakan, laporan MRLL ke Forum LLAJ, laporan tahunan ke Dirjen (jalan nasional), laporan triwulan ke Gubernur, dan evaluasi MKLL tahunan. | R05:C-20, C-35; PM 96 Lamp. I VI; UU Ps.98; Pergub 68 Ps.15; PP 32 Ps.63(2) | Wajib hukum | **T2** (laporan kajian eksisting vs rekomendasi), **T3** (laporan wajib dan sebelum-sesudah lapangan), T4 (efektivitas ke Dirjen), T5 (evaluasi MKLL) (dulu T1 dasar, T2 lengkap) | D |
| KB-REQ-010 | menghasilkan template kajian ke Dirjen yang minimal memuat kecepatan rata-rata & V/C, peta ruas, tata letak perlengkapan, arah arus, dampak jaringan. | R05:C-21; PM 96 Lamp. III | Wajib hukum | T3 | I |
| KB-REQ-011 | menyediakan interkoneksi/API dengan pusat kendali SIK LLAJ Polri (Ditlantas/NTMC) sehingga data dapat diakses setiap pembina LLAJ. | R05:C-22; UU Ps.246–247 | Wajib hukum | **T4** (dulu T3) | T |
| KB-REQ-012 | menyediakan portal/API publik untuk data pusat kendali (kecuali data pribadi/penegakan hukum). | R05:C-23; UU Ps.250; Perda Ps.233 | Wajib hukum | **T3** (dashboard publik), **T5** (API publik) (dulu T2) | D |
| KB-REQ-013 | bertindak hanya sebagai penyedia bukti elektronik untuk ETLE (event + bukti + pelat + waktu) dan TIDAK menerbitkan sanksi/denda pelanggaran APILL secara mandiri. | R05:C-24; UU Ps.272, 260, 262(3), 287; PP 32 Ps.46 | Wajib hukum | T3 (bukti tanpa pelat), **T4** (kiriman ke Back Office ETLE) (dulu T3) | I |
| KB-REQ-014 | melakukan pertukaran data pajak kendaraan/uji emisi/TNKB hanya berdasarkan perjanjian kerja sama tercatat, dengan kajian UU PDP. | R05:C-25; PP 32 Ps.16; Pergub 68 Ps.13(4); Perda Ps.239 | Wajib hukum | **T4** (dulu T3) | I |
| KB-REQ-015 | menerapkan klasifikasi data, RBAC berbasis peran & yurisdiksi, audit trail, dan perjanjian akses; data terintegrasi milik Pemprov; akses pihak ketiga hanya dengan persetujuan Gubernur/pejabat. | R05:C-26; R02:ITCS-SEC-01; Pergub 68 Ps.10(7), 11(4)–(5) | Wajib hukum | **T2** (akun, peran, dan audit dasar), **T3** (tata kelola data Dishub), **T4** (RBAC per yurisdiksi) (dulu T1 RBAC, T2 audit lengkap) | T |
| KB-REQ-016 | memenuhi interoperabilitas & interkoneksi data dan terintegrasi ke sistem informasi Pemprov (JSC/JAKI). | R05:C-27; Pergub 68 Ps.1(4–5), 10(4)c, 11(1); PM 76 Ps.20 | Wajib hukum | T3 (aduan kota), **T4** (sistem informasi pemda), T5 (provinsi) (dulu T3) | T |
| KB-REQ-017 | menyediakan modul evaluasi ERP/pembatasan yang memeriksa kriteria legal (V/C ≥0,9 & ≤10 km/jam; ≥2×2 lajur; bukan jalan nasional; 07.00–20.00 hari kerja pada 9 ruas Perda) dan mengukur efektivitas dari kenaikan kecepatan rata-rata. | R05:C-28; PP 32 Ps.79–83; Perda Ps.78–85 | Sebaiknya | T5 | A |
| KB-REQ-018 | menyediakan dashboard evaluasi tahunan MKLL (ganjil-genap: V/C ≥0,7 & <30 km/jam; jam & ruas Pergub 88/2019). | R05:C-29; PP 32 Ps.62–66; Pergub 68 Ps.13; Pergub 88/2019 | Sebaiknya | **T5** (dulu T4) | A |
| KB-REQ-019 | mencatat kompetensi/kualifikasi operator dalam manajemen pengguna (MRLL oleh petugas berkompetensi; unit pengelola & SDM SMTC). | R05:C-33; PM 96 Ps.1(4); PM 76 Ps.21 | Wajib hukum | **T3** (dulu T2) | I |
| KB-REQ-020 | menyimpan ruang lingkup, rencana aksi (waktu, pendanaan, mekanisme) dan koordinasi BPTJ untuk program ATCS/ERP/prioritas bus sesuai RIT Jabodetabek. | R05:C-34; Perpres 55/2018 Ps.4 | Opsional | T4 | I |
| KB-REQ-021 | menyediakan informasi kualitas baku mutu udara di pusat kendali dan mendukung pembatasan berbasis emisi sebagai atribut kebijakan (bukan penindakan). | R05:C-31; UU Ps.249(3)g; PM 96 Lamp. II.H | Sebaiknya | T4 | D |
| KB-REQ-022 | mendokumentasikan pemenuhan 12 aspek makroskopis/mikroskopis penentuan siklus (PM 49 Ps.17) untuk setiap algoritme kendali yang diaktifkan. | R05:C-10; R00:B | Wajib hukum | **T2** (mode optimasi), **T4** (algoritme adaptif) (dulu T3) | A |

### A2. Kendali sinyal (Kategori: Kendali)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-030 | mendukung mode kendali per simpang: fixed-time TOD, semi-adaptif, adaptif, terkoordinasi terpusat, free/actuated, flash, manual — dengan **≥8 rencana siklus (TOD plan)** tersimpan per controller sebagai fallback wajib. | R05:C-09; R06:F-01; PM 49 Ps.11–16; R02:ITCS-FB-04 | Wajib hukum | **T2** (jadwal rekomendasi ≥8 rencana), **T4** (mode kendali dan TOD lewat pusat) (dulu T1 plan mgmt, T2 TOD via central) | D |
| KB-REQ-031 | memodelkan mesin fase dual-ring/barrier (kompatibilitas, skip, pemberian sisa waktu, dual entry, simultaneous gap) DAN stage-based (tahap/fase MKJI) dalam satu model. | R01:I.3-1; R00:I; R03:A.10 | Wajib operasional | T2 (tahap dan fase gaya Indonesia di editor jadwal), **T4** (model dual-ring/barrier NTCIP) (dulu T2) | T |
| KB-REQ-032 | mengimplementasikan logika aktuasi lokal: min green → passage timer → gap-out (3 syarat) → max-out; gap reduction; variable initial; recall & memory mode; detector delay/extend/switch/queue/call. | R01:I.3-2; NTCIP phaseTable | Wajib operasional | **T4** (dulu T3 simulasi/twin, T4 lapangan) | T |
| KB-REQ-033 | menerapkan batas min/max phase time, batas cycle (nilai/rentang), batas perubahan cycle & split antar siklus (default ≤5 s/siklus), dan batas frekuensi perubahan arah koordinasi. | R02:ITCS-ALG-01; R04:A.5; R01:I.2 | Wajib operasional | T1 (hijau minimum dan rentang siklus di validator), **T4** (batas perubahan per siklus) (dulu T3) | T |
| KB-REQ-034 | memvalidasi setiap nilai timing terhadap rumus/kebijakan: kuning ≥3 s (ITE), all-red = waktu pengosongan (Dirjen 273/PKJI 5-9), ped walk/clearance minimum, siklus 40–130 s, hijau awal/akhir ≥10 s — menolak nilai di bawah batas. | R01:I.3-3; R00:G; R05:D; PKJI hlm.112, 124 | Wajib operasional | T1 | T |
| KB-REQ-035 | menghitung cycle/split awal dengan critical movement analysis/Webster/PKJI (C, J, DJ, IFR, PR, c, g) sebagai "Kalkulator APILL". | R01:I.3-4; R00:G; R05:G.2 | Wajib operasional | T1 | T |
| KB-REQ-036 | menjalankan koordinator: master clock (sync reference + DST), offset reference point (default awal kuning fase koordinasi), yield point, permissive, force-off fixed/floating, inhibit max, walk modes, actuated coordinated phase, early-return handling. | R01:I.3-5; R02:ITCS-GW-01 | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-037 | menjalankan transition engine (dwell/max dwell/add/subtract/shortway) dengan batas per siklus ≈20 %, selesai ≤3–5 siklus, min 30 menit per pattern, dan mencatat frekuensi & durasi transisi sebagai KPI. | R01:I.3-6; R01:C.6 | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-038 | mendukung pemilihan pola traffic-responsive (V+K·O, bobot, smoothing 50 %, threshold dengan hysteresis, group-wide switch). | R01:I.3-8 | Sebaiknya | **T4** (dulu T3) | T |
| KB-REQ-039 | menyediakan kendali adaptif real-time inti berupa **cyclic Max-Pressure terkoordinasi**: cycle & offset tetap per koridor, MP mengalokasikan split dari antrian/occupancy ternormalisasi kapasitas link, proyeksi ke green feasible (min green ≥7–10 s, max green, perubahan ≤5 s/siklus, integer). | R04:F-T2; R04:A.5 | Wajib operasional | **T5** (dulu T3 koridor pilot, T4 jaringan) | T |
| KB-REQ-040 | memilih subset simpang kritis untuk MP (skor occupancy rata-rata, varians, fraksi waktu ≥80 % kapasitas) dan mendukung MP parsial 10–25 % simpang. | R04:A.5 | Sebaiknya | **T5** (dulu T3) | A |
| KB-REQ-041 | menyediakan perimeter/gating control berbasis akumulasi kendaraan regional (PI regulator, hysteresis start/stop, batas min 15 % saturation flow gerbang) untuk kawasan CBD saat jenuh. | R04:F-T2; R04:GR7; R01:F.5 | Sebaiknya | **T5** (dulu T4) | T |
| KB-REQ-042 | mendukung metering/penyimpanan antrian di lokasi terkonfigurasi, pembatasan cycle grup saat antrian terdeteksi, deteksi antrian dari kamera AI. | R02:ITCS-QUE-01; Req 2.1.3.0-1..8 | Wajib operasional | T2–T3 (deteksi antrian dari kamera), **T5** (metering dan pembatasan siklus grup) (dulu T4) | D |
| KB-REQ-043 | menyediakan mode non-sequence-based dengan "maximum time between successive displays of each phase" untuk kondisi jenuh. | R02:ITCS-ALG-04; Req 2.3.0-4 | Sebaiknya | **T5** (dulu T4) | T |
| KB-REQ-044 | mendeteksi repeated phase failure (max-out/force-off berulang, occupancy tinggi) dan menyesuaikan operasi. | R02:ITCS-ALG-02; Req 2.1.1.0-9 | Wajib operasional | T3 (deteksi dari data kamera), **T4** (penyesuaian operasi) (dulu T3) | T |
| KB-REQ-045 | merespons lebih cepat dari normal (nilai "lebih cepat" didefinisikan kuantitatif) saat perubahan demand besar (insiden/event) terdeteksi, dalam batas operator. | R02:ITCS-ALG-03; Req 2.6.0-4 | Sebaiknya | T4 | T |
| KB-REQ-046 | memungkinkan operator menetapkan objective per grup & periode (smooth flow / throughput / equity / queue management / isolated efficiency) dan mengubahnya otomatis saat kriteria kondisi terpenuhi. | R02:ITCS-OBJ-01; Req 2.1.1.0-7 | Sebaiknya | **T5** (dulu T4) | D |
| KB-REQ-047 | menyediakan oversaturation toolkit: split reallocation, batas cycle (Lieberman), phase truncation, re-service, green flush hilir→hulu (≤255 s), offset negatif/simultan, gating; dengan periode loading/oversaturated/recovery. | R01:I.3-11; STM2 §12 | Sebaiknya | **T5** (dulu T4) | D |
| KB-REQ-048 | mengelola plan kondisi khusus (cuaca, insiden, event, evakuasi, flush) dengan trigger (kecepatan/occupancy/konfirmasi), aktivasi per koridor, kriteria deaktivasi, MoU lintas yurisdiksi, debrief. | R01:I.3-12; R06:F-15; STM2 §11 | Sebaiknya | T3 (deteksi kejadian pemicu), **T4** (plan kondisi khusus) (dulu T3) | D |
| KB-REQ-049 | memberikan RL/AI hanya sebagai advisor/penala parameter via **shadow mode** (keputusan dicatat, tidak diaktuasi) dengan lapisan veto statistik; tidak sebagai pengendali langsung tanpa validasi bertahap SIL→HIL→shadow→phased live. | R04:F-T4; R04:GR9; R04:A.3 | Wajib operasional | T4 (shadow), T5 (advisor live) | D |
| KB-REQ-050 | mempertahankan operasi adaptif di simpang non-preempted selama preemption dan resume otomatis setelah dilepas; mendukung rute preemption terjadwal dengan penundaan berbasis travel time. | R02:ITCS-PRE-01; Req 11.0-1..8 | Wajib operasional | T4 | T |
| KB-REQ-051 | tidak menghalangi fitur controller lokal (phase re-service, overlap, variable sequence, omit, FYA, detector switching, timing sesuai kebijakan) dan mengakomodasi per-lane detection. | R02:ITCS-CTL-01; Req 7.0-x | Wajib operasional | **T4** (dulu T3) | I |
| KB-REQ-052 | mengakomodasi waktu penyeberangan pejalan kaki selama adaptif, exclusive pedestrian phase, ped recall via TOD, LPI/early walk hingga XX s; minimum walk/FDW tidak pernah dipotong oleh priority. | R02:ITCS-PED-01; R06:F-16; R04:GR1 | Wajib operasional | T1 (hijau minimum memperhitungkan penyeberangan), **T4** (adaptif dan prioritas) (dulu T3) | T |
| KB-REQ-053 | mendukung fase khusus busway/angkutan umum & waktu hijau khusus angkutan umum/pejalan kaki, serta konfigurasi fase khusus VVIP green wave. | R05:C-14; PM 96 Lamp. II.A.5, D.3; R06:D.2 | Wajib hukum | T3 (evaluasi skema fase alternatif), **T4** (fase khusus angkutan umum dan green wave VIP) (dulu T3) | D |

### A3. Prioritas transit & darurat (Kategori: Kendali/Integrasi)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-060 | menyediakan modul TSP dengan strategi default green extension + early green (red truncation); opsi phase insertion/queue jump/rotation per simpang; parameter per simpang & TOD. | R06:F-02; TSP Handbook h.7–8 | Wajib operasional | **T4** (dulu T3) | D |
| KB-REQ-061 | menerapkan prioritas bus kondisional berbasis occupancy (OCC/Transit-MP) dan/atau headway/keterlambatan dari AVL (≥2 menit terlambat; 4 level; bus non-revenue & bus di halte dikecualikan; paling terlambat menang). | R06:F-03; R04:A.6–A.7 | Wajib operasional | **T5** (dulu T3 rule-based, T4 OCC-MP); prioritas berbasis aturan ada di T4 (KB-REQ-060) | T |
| KB-REQ-062 | menjalankan Priority Request Server terpusat: 1 aktivasi/siklus/pendekat, lockout siklus berikutnya, reservice-inhibit timer, delay timer, recovery/compensation, log setiap permintaan (diminta/diberikan/ditolak, durasi, jenis, lockout, waktu recovery). | R06:F-04; R02:ITCS-PRI-01; NTCIP 1211 PRG/PRS | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-063 | menerima transit priority call dari detektor/OBU bus dan dari sistem eksternal (TransJakarta center) — PRG-4 dan PRG-1/2/3. | R02:ITCS-PRI-01; Req 12.0-8; R06:A.6 | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-064 | menempatkan logika kelayakan bus (schedule adherence, occupancy) di sistem transit; ITCS hanya menerima request terverifikasi (atau menghitungnya dari data AVL yang diterima). | R02:ITCS-PRI-02; App. C hlm.170 | Sebaiknya | **T4** (dulu T3) | I |
| KB-REQ-065 | menyediakan check-in (100–150 m / ~15 s hulu) dan check-out (stop line) untuk bus dan EV agar extension dihentikan segera setelah kendaraan lewat (geofence + ANPR/kamera sebagai konfirmasi). | R06:F-07; TSP h.66, h.29 | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-066 | menyediakan modul EVP dengan hierarki preempt terkonfigurasi (pemadam > ambulans > VVIP), urutan entry–track clearance–dwell–exit, larangan memotong yellow/all-red, pemendekan walk/FDW terkontrol, transisi kembali ke koordinasi (recovery ≤1–2 siklus). | R06:F-05; NTCIP preempt objects; STM 2008 §9.1 | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-067 | mendukung system-based EVP (AVL/CAD Damkar & ambulans + geofence GPS per simpang, route-agnostic, pemicu kecepatan/jarak) dan EVP bertingkat (preempt hanya bila target respons terancam; conflict graph multi-EV). | R06:F-06; R04:A.18 | Sebaiknya | T4 | T |
| KB-REQ-068 | menyimpan parameter prioritas (detik extension/truncation, ambang keterlambatan) sebagai konfigurasi ber-riwayat dengan persetujuan lintas instansi (MoU digital). | R06:F-13; TSP h.23 | Sebaiknya | **T4** (dulu T3) | I |
| KB-REQ-069 | menerapkan hierarki override tegas: preemption darurat/rel > priority transit > adaptif; konflik diuji di simulasi. | R06:F.5; TSP h.31, h.62 | Wajib operasional | **T4** (dulu T3) | T |

### A4. Deteksi (Kategori: Deteksi)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-080 | kompatibel dengan teknologi deteksi yang ditetapkan (kamera AI/video, radar, loop, magnetik) dengan layout stop-line per lajur + advance/far-side untuk arrival profile (sensor density level 3.0). | R02:ITCS-DET-01; TSPH Tab.43; SK 7234 (≥4 zona, gap & occupancy) | Wajib operasional | T1 (kamera CCTV lewat Vision Tracker), **T3** (inventaris), **T4** (deteksi untuk kendali) (dulu T2 inventaris, T3 kendali) | I |
| KB-REQ-081 | memantau kesehatan detektor (constant call, no activity, erratic count, anomali vs profil) dan melaporkan % detektor berfungsi; membandingkan hitungan dengan profil historis. | R02:ITCS-DET-02; R01:I.3-13; NTCIP vehicleDetectorAlarms | Wajib operasional | T1–T2 (mutu rekaman dan halaman kualitas data), **T3** (kesehatan kamera), **T4** (kesehatan detektor) (dulu T1 bila data ada, T2) | T |
| KB-REQ-082 | tidak mengaktifkan mode adaptif pada simpang tanpa detektor sehat (health check prasyarat). | R05:C-12; PM 96 Lamp. II.F.d | Wajib hukum | **T4** (dulu T3) | T |
| KB-REQ-083 | memperlakukan deteksi kamera/AI sebagai virtual detector (memicu VehCall di lapangan / E1-E2 di simulasi) dan sebagai sumber HiResEvent detector on/off. | R03:D.2-4 | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-084 | menerapkan aturan kualitas data: volume ≠ demand saat antrian; estimasi demand dari upstream/observasi antrian; validasi sumber sebelum dipakai; menghitung & melaporkan kualitas data relatif akibat detector fault. | R01:I.3-14; R02:ITCS-LOG-03; Req 6.0-8 | Wajib operasional | T2 | A |
| KB-REQ-085 | menggunakan data probe/GPS (TransJakarta, ojol, navigasi) yang diagregasi multi-hari untuk evaluasi progression (cyclic TSD, PPD, AoG) dan estimasi turning ratio/OD, bukan untuk kendali detik-ke-detik bila penetrasi <20–30 %. | R04:A.19; R04:F-T3 | Sebaiknya | T4 (GPS logger untuk offset dasar), **T5** (analitik probe koridor) (dulu T2 evaluasi, T4) | A |
| KB-REQ-086 | menyediakan sumber data alternatif (detektor tetangga, data historis) secara real-time tanpa intervensi operator saat data detektor tidak valid. | R02:ITCS-FB-02; Req 13.1.0-2 | Wajib operasional | **T4** (dulu T3) | T |

### A5. Komunikasi & antarmuka controller (Kategori: Komunikasi)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-090 | menyediakan Controller Abstraction Interface tunggal dengan adaptor NTCIP 1202/1201 (SNMP/STMP), adaptor RS-232/serial vendor (controller eksisting), dan adaptor TraCI/SUMO (digital twin). | R03:D.2; R02:ITCS-IF-03 | Wajib operasional | **T2** (adaptor SUMO), **T3** (baca status), **T4** (perintah dan adaptif) (dulu T1 baca status, T2 perintah, T3 adaptif) | T |
| KB-REQ-091 | mengendalikan real-time hanya lewat objek kontrol tipe C (systemPatternControl, systemSyncControl, phase/ring ControlGroup, preemptControlState, specialFunctionOutputControl) dan mengirim heartbeat lebih sering dari `unitBackupTime` sehingga controller kembali ke mode lokal bila pusat putus. | R03:A.15; NTCIP §2.4.3 | Wajib operasional | **T4** (dulu T2) | T |
| KB-REQ-092 | mengubah parameter plan (P/P2) hanya lewat transaksi `dbCreateTransaction` dengan validasi consistency check (Annex B) di sisi server sebelum download, dan menyimpan `dbVerifyError`. | R03:A.14–A.15 | Wajib operasional | **T4** (dulu T2) | T |
| KB-REQ-093 | melakukan conformance discovery (baca `max*`, uji GET per grup) untuk mengisi kapabilitas controller (PRL) dan menandai perintah yang tidak didukung. | R03:D.2-1 | Sebaiknya | **T3** (dulu T2) | T |
| KB-REQ-094 | memilih controller/komunikasi secara technology-independent: interface NTCIP 1202/1211/1201 wajib untuk pengadaan baru; pilihan controller tidak dibatasi software adaptif; server platform standar terpisah dari software. | R02:ITCS-IF-03; ConOps 6.0-6.0-2; TSPH hlm.190 | Wajib operasional | **T4** (dulu T2) | I |
| KB-REQ-095 | mengklasifikasikan fungsi berdasarkan kebutuhan reliabilitas/latensi (adaptif & status real-time = tinggi; database transfer = rendah; video = bandwidth tinggi), memantau uptime komunikasi, dan menjaga demand ≤50 % kapasitas throughput. | R02:G.7; TSPH hlm.169–171, 194 | Sebaiknya | **T4** (dulu T2) | A |
| KB-REQ-096 | mendukung Signal System Master/koordinasi lokal per grup agar koordinasi tetap berjalan saat link ke TMC putus. | R02:H.2; STM2 §7.2.2 | Sebaiknya | **T4** (dulu T3) | T |
| KB-REQ-097 | mendukung interface eksternal menurut Interface Control Document (information/application/lower layer protocol, agregasi, frekuensi simpan/lapor, durasi simpan) dan menerima perintah dari sistem eksternal (cycle length, arah progression, strategi adaptif, non-adaptif). | R02:ITCS-IF-01, IF-02; Req 3.0-1 | Wajib operasional | T3 (ICD aduan kota), **T4** (instansi dan perintah eksternal) (dulu T3) | T |
| KB-REQ-098 | mendukung batas sistem/crossing arterials: fixed cycle sama dengan sistem tetangga, minimalkan interupsi lalu lintas masuk, koordinasi adaptif di rute bersilangan. | R02:D.8; Req 4.0-1 | Sebaiknya | **T5** (dulu T4) | T |

### A6. Fallback, alarm, kesehatan (Kategori: Operasi-Pemeliharaan)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-100 | beralih ke operasi non-adaptif (TOD central/lokal atau free) tanpa mengganggu arus ketika: detektor tertentu gagal; jumlah detektor gagal per controller/grup melebihi ambang; link komunikasi gagal; adaptive processor gagal; occupancy ekstrem; perintah operator; jadwal; perintah sistem eksternal — dengan hierarki adaptif → central TOD/TRPS → SSM/lokal TOD → free actuated → flash. | R02:ITCS-FB-01; Need 4.14.0-1; R04:GR4; R03:D.5 | Wajib operasional | **T4** (dulu T2 TOD, T3 adaptif) | T |
| KB-REQ-101 | menyediakan semua input detektor lokal ke controller lokal saat adaptive processor gagal. | R02:ITCS-FB-03; Req 13.3-4 | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-102 | menerbitkan alarm ke penerima ditentukan dalam ≤XX menit sejak deteksi kegagalan (detektor, komunikasi, processor, pintu kabinet, flash/conflict, power) dan meneruskannya ke sistem maintenance/CRM sebagai tiket. | R02:ITCS-ALM-01; R06:F-10; Req 13.x-2/3 | Wajib operasional | **T3** (kamera dan tiket), **T4** (controller dan detektor) (dulu T1) | T |
| KB-REQ-103 | memantau 14 item equipment monitoring (detector fail on/off, count irregularity, controller status, parameter mismatch vs DB, timing irregularity, clock sync, transition frequency, flash/conflict frequency, power, comm quality, response time, repair frequency). | R01:G.2 Exhibit 8-16; R01:I.3-13 | Wajib operasional | **T3** (subset kamera), **T4** (lengkap) (dulu T1 subset, T2) | T |
| KB-REQ-104 | menjalankan Watchdog harian ATSPM (no data <500 rekaman/24 jam; force-off/max-out >90 % dari ≥50 aktivasi 01–05; advance counts <100 kend 17–18; stuck ped >200 aktuasi 01–05; ambang dapat diubah). | R03:C.3-14; HOP-20-002 p.20 | Sebaiknya | **T4** (dulu T2) | T |
| KB-REQ-105 | mengelola aset APILL: inventaris komponen & penandaan (serial, pabrik, tahun), umur teknis ≤5 tahun, jadwal pemeliharaan berkala ≤6 bulan dengan checklist, pemeliharaan insidentil (komponen rusak, penyesuaian siklus, posisi bergeser), alarm jatuh tempo, laporan penilaian kinerja per aset, horizon perencanaan 5 tahun. | R05:C-06, C-07, C-08; R00:B, H; PM 49 Ps.41–42; SK 7234 | Wajib hukum | **T3** (dulu T1) | D |
| KB-REQ-106 | memantau keberadaan/lokasi/kondisi/fungsi perlengkapan jalan (APILL, rambu, marka, DIS, VMS, detektor bus) sebagai indikator kinerja perlengkapan. | R05:C-08; PM 96 Lamp. I II.B.h | Wajib hukum | **T3** (dulu T2) | I |
| KB-REQ-107 | mencatat uji coba pengoperasian APILL & kelengkapannya saat pemasangan (commissioning) dan verifikasi deteksi & komunikasi. | PM 96 Lamp. I IV; STM2 §9.4.3 | Wajib hukum | **T4** (dulu T2) | I |
| KB-REQ-108 | menyediakan tiket keluhan publik (form 7 langkah, kategori diagnostik Exhibit 8-17) terhubung CRM dengan SLA 3 jam terukur. | R01:I.5; R06:F-18; Beritajakarta 145079 | Wajib operasional | **T3** (dulu T2) | D |

### A7. Data, logging, digital twin (Kategori: Data)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-110 | mencatat high-resolution event log ber-timestamp 0,1 s (kode enumerasi resmi Indiana/Purdue 2012: 0–11 fase, 21–23/43–45 pejalan kaki & call, 81–82/89–90 detektor, 102–111 preempt, 131–133/150–151 koordinasi) untuk: calls kendaraan/pejalan kaki, awal-akhir fase/interval, jenis terminasi, preempt/priority, transisi/plan change, alarm — dari controller lapangan maupun simulator. | R02:ITCS-LOG-01; R03:C.2; Req 6.0-1, 18.0-3 | Wajib operasional | **T3** (dari status lampu kamera dan SUMO), **T4** (dari controller dan edge) (dulu T2 bila controller mendukung, T3) | T |
| KB-REQ-111 | menyimpan input algoritma (volume, occupancy, queue, phase utilization, arrivals on green, band efficiency) dan **semua nilai perhitungan antara yang dipengaruhi parameter kalibrasi** ≥XX hari, dapat diekspor CSV/SQL. | R02:ITCS-LOG-02; Req 6.0-4/5, 18.0-1/2 | Wajib operasional | **T2** (dulu T3) | T |
| KB-REQ-112 | menyimpan 8 jenis data PM 76 Ps.4(4): kecepatan vs batas, pola aliran/fluktuasi, kepadatan, waktu perjalanan asal-tujuan, cuaca, kondisi & geometrik jalan, identitas kendaraan, kondisi sarana-prasarana; plus rekaman data operasional & historis Ps.7(4)f–g. | R00:C; PM 76 Ps.4(4), 7(4) | Wajib hukum | T1–T2 (volume, pola arus, geometri), **T3** (kecepatan dan waktu tempuh antarkamera), **T4** (cuaca, identitas kendaraan, kondisi sarana) (dulu T2) | I |
| KB-REQ-113 | mencatat setiap perintah ke controller (operator/algoritme, objek, nilai, hasil, transaction id) dalam audit log tak-terhapus, tervalidasi skema; LLM/AI tidak berada di control loop. | R03:D.1 CommandLog; R04:GR8; R04:A.17 | Wajib operasional | **T4** (dulu T1); audit perubahan konfigurasi dan rekomendasi sejak T2 | T |
| KB-REQ-114 | menyediakan data warehouse/arsip dengan retensi, ekspor, dan kemampuan merekreasi kejadian historis (menjawab komplain "menunggu 30 menit"). | R02:C.3 Need 4.11; Req 6.0-6/7 | Wajib operasional | T2 (arsip dan retensi), **T3** (rekreasi kejadian) (dulu T2) | D |
| KB-REQ-115 | menyediakan development/test server dan simulator (SUMO NEMA sebagai digital twin) untuk menguji timing/firmware/algoritme sebelum live; pipeline ATSPM yang sama dipakai untuk log lapangan & simulasi. | R02:ITCS-ENV-01; R03:D.2-3, D.3-8 | Wajib operasional | **T2** (SUMO satu simpang), T3 (twin per simpang) (dulu T3) | D |
| KB-REQ-116 | mengimpor plan APILL eksisting (CSV) ke SUMO (`tls_csvSignalGroups.py`) dan memvalidasi konsistensi ATSPM simulasi vs lapangan sebelum menguji algoritme baru. | R03:D.2-3 | Sebaiknya | **T2** (impor jadwal eksisting ke SUMO), T3 (kalibrasi terhadap lapangan) (dulu T3) | T |
| KB-REQ-117 | menyimpan arsip volume/antrian per menit dan model prediksi kejenuhan (waktu, cuaca, libur, event) untuk pra-penyesuaian siklus; digital twin 3D opsional. | R06:F-14; Antara 3635259 | Sebaiknya | T4 (prediksi), T5 (twin 3D) | A |
| KB-REQ-118 | merencanakan storage hi-res ~puluhan MB/simpang/hari (9 GB/hari untuk ~390 sinyal) dan agensi memiliki akses raw data (tidak bergantung vendor). | R03:D.5; HOP-20-002 p.54; NCDOT Exh.5-5 | Sebaiknya | **T4** (dulu T2) | A |

### A8. Integrasi eksternal (Kategori: Integrasi)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-120 | menyediakan API/ICD dengan Ditlantas PMJ (ETLE: event pelanggaran + bukti), Bapenda (status pajak per pelat), DLH (status uji emisi per pelat, agregat per ruas), TransJakarta (AVL/APC/jadwal/headway), Damkar/AGD 119/112 (CAD), pengelola tol, BPTJ/Kemenhub (laporan efektivitas), TMC lain. | R06:F-11, F.4; R02:ITCS-IF-01; RPP h.9, h.11 | Wajib operasional | **T4** (dulu T3) | T |
| KB-REQ-121 | mengirim data operasional/kontrol/monitoring/koordinasi/kinerja ke sistem eksternal XX dan melaporkan real-time ke sistem eksternal (ICM). | R02:D.7; Req 3.0-1.0-1..5 | Sebaiknya | **T4** (dulu T3) | T |
| KB-REQ-122 | mengaktifkan rambu/DMS/VMS/DIS berdasarkan kondisi terukur dan mengubah konten DIS/countdown secara remote dari pusat (RS-485). | R02:C.3 4.17; R00:H; PM 76 Ps.7(2)c | Sebaiknya | **T4** (dulu T3) | D |
| KB-REQ-123 | menyediakan dashboard publik #LANCAR-Jakarta (atau merek daerah) dengan KPI terdefinisi & metode dipublikasikan. | R06:F-12; RPP h.4, h.17; UU Ps.250 | Wajib operasional | **T3** (dulu T2) | D |

### A9. TMC / antarmuka operator (Kategori: TMC-UI)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-130 | menyediakan peta live simpang (status mode, lampu, alarm), video/CCTV, dan status koordinasi/transisi per simpang (cycle length plot). | R01:I.5; R02:H.2; PM 76 Ps.7(4)b | Wajib operasional | **T2** (peta simpang dan LOS di dashboard), **T3** (status lampu, peringatan, CCTV live view), **T4** (status koordinasi) (dulu T1) | D |
| KB-REQ-131 | menyediakan editor ring-barrier & timing sheet dengan validasi rumus, time-space diagram interaktif (band, offset drag, sequence), manajer pattern/TOD/DOW & alternate plan dengan tombol aktivasi manual dan log siapa-kapan. | R01:I.5 | Wajib operasional | **T2** (editor jadwal dan TOD), **T4** (diagram waktu-ruang dan aktivasi manual) (dulu T1 editor dan TOD, T2 TSD) | D |
| KB-REQ-132 | menyediakan dashboard kinerja: PCD, split monitor, AOG per plan, travel time, before–after comparison, per audiens (pimpinan ringkas; engineer teknis; teknisi alert→work order). | R01:I.5; R02:G.5; R03:D.3-7 | Wajib operasional | T2 (dashboard tiga halaman, eksisting vs rekomendasi), **T3** (sebelum-sesudah lapangan), **T4** (PCD, split monitor, AoG) (dulu T2) | D |
| KB-REQ-133 | menyediakan konsol preferential treatment (permintaan aktif TSD/TED, level, log layanan, decision tree TSP, monitor preempt) dan modul ASCT (parameter constraint, on/off schedule, tinjauan keputusan, backup plan, failure mode). | R01:I.5 | Wajib operasional | **T4** (dulu T3) | D |
| KB-REQ-134 | mendukung akses monitoring/kontrol dari TMC, fasilitas maintenance, LAN/WAN, TMC agensi lain, kabinet lokal, kendaraan maintenance, remote via internet — dengan hak sesuai peran/yurisdiksi. | R02:ITCS-ACC-01; Req 5.0-2 | Wajib operasional | **T3** (pemantauan jarak jauh), **T4** (kendali per yurisdiksi) (dulu T2) | D |
| KB-REQ-135 | menyediakan master graphics simpang (≥1280×768, label simpang & detektor), field diary, notifikasi sebelum kunjungan lapangan, dan larangan upload timing di luar jam teknisi (workflow & audit). | R01:I.5; NCDOT | Sebaiknya | T2 (diagram simpang), **T4** (field diary dan kunci unggah jadwal) (dulu T2) | I |
| KB-REQ-136 | menampilkan transparansi keputusan algoritme: kondisi terukur yang menjadi dasar keputusan & nilai antara (anti black-box) untuk operator, publik, dan pejabat. | R02:ITCS-RPT-01; Req 18.0-1/2, 6.0-11 | Wajib operasional | **T2** (dulu T3) | D |

### A10. KPI & evaluasi (Kategori: KPI) — rincian di `07_KPI_dan_Monev.md`

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-140 | menghitung KPI simpang PKJI/MKJI real-time & harian (C, J, DJ, Nq/PA, RKH/NKH, TLL/TG/T/TI) dan kelas LOS A–F PM 96/2015, plus padanan HCM untuk benchmark. | R06:F-08; R05:G.2; R00:E, G | Wajib hukum | T1 | T |
| KB-REQ-141 | menghitung ATSPM: phase termination, split monitor, PCD/AoG/platoon ratio, split failure (GOR & ROR5 ≥80 %), approach delay, AoR, TMC/approach volume (PHF/K/D), ped delay, preemption details, approach speed, YRA, link pivot. | R02:ITCS-KPI-01; R03:C.3; TSPH Tab.46–48 | Wajib operasional | T2 (volume dan PHF), **T3** (dari status lampu kamera: split failure, YRA, ped delay, AoR), **T4** (phase termination, PCD, AoG dari controller), **T5** (Link Pivot) (dulu T2 subset sesuai detektor, T3) | T |
| KB-REQ-142 | menghitung KPI koridor/jaringan: travel time & average speed, reliability (95th, buffer/planning index), stops/km, bandwidth efficiency/attainability, throughput input/output, emisi/BBM (model), target 35 km/jam (Perda) / 30 km/jam (Perpres). | R01:I.4; R05:E; Perda Ps.8; Perpres 55 | Wajib operasional | **T3** (waktu tempuh antarkamera), **T4** (bandwidth offset dasar), **T5** (KPI koridor dan jaringan lengkap) (dulu T2) | A |
| KB-REQ-143 | menghitung KPI kesehatan (comms uptime, % detektor berfungsi, % sinyal offline, transisi, false preemption/priority, MTTR) dan program (retiming age ≤3 tahun, B/C tahunan NCDOT). | R02:ITCS-KPI-01; R01:G.3 | Wajib operasional | **T3** (kesehatan kamera, % simpang terpantau), **T4** (detektor, komunikasi, umur retiming) (dulu T1 kesehatan, T2 program) | T |
| KB-REQ-144 | menyediakan modul evaluasi before–after dengan desain on/off bergantian, evaluasi bertahap (pra-optimasi, pasca-optimasi, pasca-adaptif/TSP), statistik multi-hari, dan pemisahan manfaat retiming vs sistem. | R06:F-09; R02:E.3, E.5; R01:G.3 | Wajib operasional | T2 (eksisting vs rekomendasi), **T3** (sebelum-sesudah lapangan), **T4** (on/off bergantian) (dulu T2) | A |
| KB-REQ-145 | memantau metrik keselamatan (max-out/force-off frequency, red-light running/YRA, ped delay, konflik) dan fairness per gerakan (side-street delay, gerakan volume rendah), bukan hanya delay. | R04:GR10; R01:G.1; R02:H.3 | Sebaiknya | T3 | A |
| KB-REQ-146 | melaporkan perbandingan day-to-day, hour-of-week, day-of-year, dan laporan dalam bentuk yang dapat dipahami publik/pejabat. | R02:ITCS-RPT-01; Req 6.0-9/11 | Sebaiknya | T2 | D |

### A11. Pelatihan & dukungan (Kategori: Pelatihan)

| ID | Kebutuhan (Sistem harus…) | Sumber | Prioritas | Tahap | Verif |
|---|---|---|---|---|---|
| KB-REQ-150 | dilengkapi modul e-learning/SOP operator (bimtek operasional ITCS, checklist verifikasi harian, kalibrasi, troubleshooting, PM, konfigurasi, administrasi) sesuai matriks kompetensi Mampu/Mau RPP. | R06:F-18; R02:ITCS-SUP-01; RPP h.19–20 | Sebaiknya | T2 (panduan pemakaian engineer), **T4** (e-learning dan sertifikasi operator) (dulu T2) | I |
| KB-REQ-151 | disertai kontrak maintenance dengan response time, update software XX tahun, warranty XX tahun; vendor tidak menyusun dokumen SE agensi. | R02:ITCS-SUP-01; MSE-ASCT hlm.11 | Wajib operasional | T2 | I |
| KB-REQ-152 | mendukung staffing rule-of-thumb (1 engineer/75–100 sinyal; 1 teknisi/40–50; TMC 24/7) melalui roster & beban kerja di modul operasi. | R01:H.3 | Opsional | T4 | I |

---

## B. Kebutuhan non-fungsional

| ID | Kebutuhan | Sumber | Prioritas | Tahap |
|---|---|---|---|---|
| KB-REQ-160 | **Kinerja/latensi:** poll status controller ≤1 s untuk status lampu/ring, ≤10–60 s untuk alarm & V/O; keputusan adaptif per siklus (cyclic MP) atau 5–10 s (acyclic) selesai dalam <1 s per simpang; rolling horizon 60 s/5 s bila dipakai. | R03:D.2-1; STM2 §9.4.2.2; R04:A.6 | Wajib operasional | **T4** (dulu T3) |
| KB-REQ-161 | **Skalabilitas:** minimum 321 simpang bersamaan, ekspansi ≥500 tanpa perubahan arsitektur; grup koordinasi independen namun konsisten. | R02:ITCS-NET-01, NET-02; T414 hlm.46 | Wajib operasional | **T1** (skema siap banyak simpang), T4 (skala kota) (dulu T2 desain, T4 skala) |
| KB-REQ-162 | **Ketersediaan:** kegagalan pusat tidak menghentikan lampu (fallback lokal); uptime komunikasi & server dipantau; disaster preparedness (akses data bila TMC lumpuh); UPS/BBU kabinet. | R02:G.4, G.7; TSPH hlm.33–35, 193 | Wajib operasional | **T4** (dulu T2) |
| KB-REQ-163 | **Keamanan siber:** NEMA TS 8 & NCHRP 03-127; SNMPv3/TLS bila tersedia; jaringan berlapis; kabinet IP-addressable dengan kunci elektronik & alarm pintu; server di balik firewall; 21 elemen security policy (Req 5.0-1). | R02:ITCS-SEC-01; TSPH hlm.192–193; R03:ARC-IT | Wajib operasional | T2 (keamanan data di laptop), **T3** (VPN untuk stream), **T4** (NEMA TS 8, mTLS, segmentasi) (dulu T2) |
| KB-REQ-164 | **Privasi:** data ANPR/pelat/pajak/emisi diperlakukan sebagai data pribadi (UU 27/2022): dasar hukum pemrosesan, minimisasi, retensi, hak subjek, DPIA; anonimisasi untuk dashboard publik. | R05:C-25/C-26; UU PDP | Wajib hukum | **T2** (penyamaran dan retensi video), T3 (DPIA data Dishub), **T4** (ANPR) (dulu T3) |
| KB-REQ-165 | **Keterbukaan & standar:** sistem terbuka, berkesinambungan, sesuai standar (PM 76 Ps.4(2)); NTCIP 1202/1211/1201; format ekspor terbuka (CSV/SQL); tidak vendor lock-in. | R00:C; R02:G.7 | Wajib hukum | **T1** (format terbuka dan ONNX), **T3–T4** (NTCIP) (dulu T2) |
| KB-REQ-166 | **Kualitas data & transparansi:** semua nilai antara algoritme tersimpan & dapat dijelaskan; kualitas data relatif dilaporkan. | R02:ITCS-LOG-02/03 | Wajib operasional | **T2** (dulu T3) |
| KB-REQ-167 | **Kegunaan:** laporan per audiens (pimpinan/engineer/teknisi/publik); bahasa Indonesia; master graphics per simpang. | R02:G.5; R01:I.5 | Sebaiknya | T2 |
| KB-REQ-168 | **Auditabilitas:** setiap perubahan konfigurasi/perintah/parameter prioritas ber-riwayat dan tak-terhapus; field diary. | R03:D.1; R06:F-13 | Wajib operasional | **T2** (konfigurasi dan rekomendasi), **T4** (perintah controller) (dulu T1) |
| KB-REQ-169 | **Maintainability:** modular; controller platform standar terpisah dari software; dev/test server; dokumentasi & pelatihan. | R02:ITCS-ENV-01; ConOps 6.0-6.0-1 | Sebaiknya | T2 |

## C. Constraint (bukan requirement; harus diakui dalam desain)

| ID | Constraint | Sumber |
|---|---|---|
| KB-CON-01 | Sebagian besar controller eksisting Jakarta/kota lain berkomunikasi **RS-232 vendor** (bukan NTCIP); tidak semua punya hi-res logger; termination type tidak terekam tanpa koneksi ke controller. | RPP h.9; R03:D.2-2; NCDOT §5.1 |
| KB-CON-02 | **Tanpa server sampai T3 selesai**: T1–T3 berjalan di laptop tim tanpa pengadaan, sehingga video diolah per batch dan pilot live dibatasi pada sedikit kamera; mulai T4 hindari streaming video terpusat & simulasi berat di produksi; hi-res log ~puluhan MB/simpang/hari perlu perencanaan storage. | Mandat user; U-22 (KB-10); R03:C.1 |
| KB-CON-03 | Jaringan lapangan heterogen (fiber/Metro-E/wireless/seluler); latensi & kehilangan koneksi adalah kegagalan nyata; heartbeat/backup timer wajib. | R02:A.2 (Chen 2022); NTCIP §2.4.3 |
| KB-CON-04 | Kewenangan terbelah: Polri (operasional MRLL, penegakan hukum, pusat kendali SIK LLAJ), Dishub (MRLL/perlengkapan), Dirjen/BPTJ (jalan nasional). | R05:A.1; UU Ps.7, 12, 247 |
| KB-CON-05 | NTCIP 1202 v02 tidak memuat TSP/hi-res/SPaT; NTCIP 1211/v03 belum ada dalam korpus (harus diperoleh). | R03:A.16 |
| KB-CON-06 | Detektor kamera terdegradasi saat malam/hujan/glare; overestimasi antrian lebih aman daripada underestimasi. | R04:A.2 |
| KB-CON-07 | ASCT tidak menyelesaikan kapasitas jenuh (DS ≥1) dan manfaat lebih kecil pada AADT >55.000; side-street delay bisa naik 3–6 %. | R02:F.2; R06:E; STM2 §12.3.4 |
| KB-CON-08 | Skala 321 simpang jauh melampaui praktik umum (65 % agensi AS hanya 5–15 sinyal adaptif) → wajib bertahap per koridor. | T414 hlm.46 |
| KB-CON-09 | Rumus PKJI/MKJI memodelkan simpang terisolir fixed-time; dipakai sebagai baseline/evaluator, bukan algoritme real-time. | R05:D.4 |
| KB-CON-10 | Umur pakai ASCT rata-rata 6–7 tahun karena isu institusional (SDM, maintenance), bukan teknologi. | T414 hlm.57 |

---

**Pointer ke detail:** R02 H.1 (requirement kandidat & arsitektur), R05 G (kepatuhan & larangan), R06 F (fitur, parameter TSP/EVP, API), R01 I (entitas, parameter, algoritma, KPI, UI), R03 D (skema data, adaptor, pipeline, API), R04 F (tingkatan & guard-rail), R00 B–H (regulasi & pedoman Indonesia). Rumus di `02_Lembar_Rumus.md`; algoritma di `05_Kartu_Algoritma_Kendali.md`; entitas & API di `06_Model_Data_dan_Antarmuka.md`; KPI di `07_KPI_dan_Monev.md`.
