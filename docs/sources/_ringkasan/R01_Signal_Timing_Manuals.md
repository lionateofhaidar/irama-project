# R01 — Catatan Studi: Manual Pengaturan Waktu Sinyal (Signal Timing Manuals)

**Sumber yang dipelajari (teks hasil pdftotext):**

| Kode | Dokumen | Ukuran | Cara sitasi di catatan ini |
|---|---|---|---|
| **STM2** | NCHRP Report 812, *Signal Timing Manual, Second Edition* (Urbanik dkk., TRB, 2015) | 12.968 baris / ~890 KB | `STM2 §x.y, hal. b-n` (halaman per bab, mis. 7-13) |
| **TSTM** | FHWA-HOP-08-024, *Traffic Signal Timing Manual* (Koonce dkk., FHWA, Juni 2008) | 13.794 baris / ~835 KB | `TSTM §x.y, hal. b-n` |
| **NCDOT** | NCDOT COST Section, *Signal System Timing Philosophy Manual* v2.0 (1 Feb 2017) | 2.256 baris / ~130 KB | `NCDOT <nama dokumen>, hal. n` (manual ini berupa katalog dokumen lepas, tiap dokumen berhalaman sendiri) |

**Catatan metodologis.** Nomor halaman STM2 tidak tercetak dalam teks ekstraksi; saya merekonstruksinya dari pemisah halaman (form feed) dan mencocokkannya dengan daftar isi (verifikasi: §3.4 jatuh di 3-19, §7.4 di 7-17, §12.4 di 12-21 — semuanya cocok dengan daftar isi resmi). Rumus-rumus STM2 (Persamaan 6-1, 6-2, 6-4, 7-1, 9-1, 9-2, 10-1) **tidak terekstraksi badannya** (hanya keterangan variabel); saya melengkapi dari TSTM 2008 yang memuat persamaan yang sama dalam teks, dan menandainya dengan *[rekonstruksi]* jika bentuknya saya susun kembali dari keterangan variabel. Semua gambar/exhibit hanya tersedia judul dan tabelnya.

---

## A. Peta Isi Ketiga Dokumen

### A.1 NCHRP 812 — Signal Timing Manual 2nd Ed. (STM2, 2015)

STM2 adalah revisi dari TSTM 2008. Fokus barunya adalah **proses berbasis hasil (outcome based process)**: tentukan lingkungan operasi → identifikasi pengguna → tetapkan prioritas pengguna/pergerakan → pilih tujuan operasional & ukuran kinerja → pilih strategi & nilai timing → implementasi & observasi (Exhibit 1-1, hal. 1-2). Empat bab baru untuk pengguna lanjut: sistem lanjut, perlakuan preferensial, kondisi khusus, kondisi jenuh (hal. 1-1).

| Bab | Halaman | Isi pokok |
|---|---|---|
| 1 Introduction | 1-1 – 1-4 | Fokus edisi kedua, organisasi, proses berbasis hasil. |
| 2 Signal Timing Program | 2-1 – 2-3 | Elemen program timing yang sukses; manfaat program regional. |
| 3 Signal Timing Concepts | 3-1 – 3-30 | Komponen sinyal, jenis kendali (pretimed/semi/fully-actuated; free vs coordinated; adaptive), pertimbangan awal (yurisdiksi, lingkungan, klasifikasi jalan, jaringan), pengumpulan data (Exhibit 3-11), **15 tujuan operasional** dan **ukuran kinerja** (Exhibit 3-17, 3-25). |
| 4 Signal Design | 4-1 – 4-27 | Deteksi (jenis, lokasi, zona keputusan/decision zone, Exhibit 4-7), perangkat kabinet (Type 332/336, NEMA TS-1/TS-2, ITS; kontroler 170/2070/ATC), display (FYA, dll.), desain sistem (komunikasi), pertimbangan desain komprehensif. |
| 5 Introduction to Timing Plans | 5-1 – 5-31 | Penomoran pergerakan & fase NEMA, konsep ring-and-barrier, opsi fase belok kiri, overlap, penugasan detektor & load switch, **analisis pergerakan kritis (critical movement analysis)**, peran perangkat lunak (deterministik vs mikrosimulasi, HITL/SITL). |
| 6 Intersection/Uncoordinated Timing | 6-1 – 6-28 | Parameter dasar: yellow change, red clearance, minimum green (driver expectancy/queue clearance/variable initial/sepeda), maximum green, passage time & gap reduction, interval pejalan kaki (walk/FDW/LPI), dual entry, recall & memory mode, konfigurasi detektor (delay/extend/switching), rencana time-of-day. |
| 7 System/Coordinated Timing | 7-1 – 7-38 | Kapan koordinasi; time-space diagram; master/local clock; bandwidth; parameter koordinasi (coordinated phase, cycle, split, force-off fixed/floating, permissive, yield point, pattern sync reference, offset reference point, offset); panduan nilai; Webster; sistem alternate; walk modes; actuating coordinated phase; **logika transisi**; kompleksitas (early return to green, dsb.). |
| 8 Implementation and Maintenance | 8-1 – 8-22 | Transfer rencana ke lapangan, observasi & penyesuaian, studi before-after, **monitoring** (operasional, high-resolution data, Purdue Coordination Diagram; monitoring perangkat Exhibit 8-16), permintaan layanan publik (Exhibit 8-17), pembaruan pemeliharaan, **kebutuhan staf**. |
| 9 Advanced Signal Systems | 9-1 – 9-18 | **Systems Engineering** (ConOps, requirements, design, verification, validation), fitur koordinasi lanjut (actuated coord. phase, dynamic phase length, phase re-service), **Traffic Responsive Plan Selection** (target-based vs threshold-based, V+KO, signature/pattern), **ASCT** (tujuan, arsitektur, metode kalkulasi, deteksi, komunikasi, instalasi, O&M, validasi). |
| 10 Preferential Treatment | 10-1 – 10-27 | Preemption vs priority (definisi NTCIP 1202/1211), proses 5 langkah, jenis deteksi, strategi timing (green extension, red truncation, phase insertion, sequence change, phase skipping), **strategi pemulihan (recovery)**, logging, scheduling multi-request (TSD/TED), setelan preemption & priority, **rail preemption** (MWT, RTT, TCGI, preempt trap, gate-down, TTG), kendaraan darurat, **TSP** (conditional, decision tree), truk. |
| 11 Special Conditions | 11-1 – 11-12 | Cuaca (reduksi kecepatan & saturation flow; strategi: tambah red clearance, min green, recall, weather plan), insiden (alternate route, kriteria aktivasi/deaktivasi, flush plan), special event. |
| 12 Oversaturated Conditions | 12-1 – 12-21 | Gejala (overflow queue, spillback, storage bay spillback/blocking, starvation, cross-intersection blocking), tujuan (throughput/queue management), strategi per simpang/arteri/jaringan (split reallocation, cycle increase, one controller, green extension, re-service, truncation, lead-lag, green flush, offset negatif/simultan, gating/metering), catatan adaptif. |
| App. A Glossary | A-1 – … | Definisi istilah (dipakai untuk bagian terminologi di bawah). |

### A.2 FHWA-HOP-08-024 — Traffic Signal Timing Manual (TSTM, 2008)

| Bab | Halaman | Isi pokok |
|---|---|---|
| 1 Introduction | 1-1 – 1-8 | Latar belakang, organisasi. |
| 2 Signal Timing Policy | 2-1 – 2-17 | Pengembangan kebijakan, proses, **ukuran kinerja & perspektif nasional** (National Traffic Signal Report Card 5 area; statistik manfaat B/C 17:1–62:1), pendanaan, contoh program. |
| 3 Operational and Safety Analysis | 3-1 – 3-29 | Terminologi; karakteristik; **kapasitas & critical movement analysis** (start-up lost time, saturation flow, effective green, capacity, v/c, QEM); ukuran kinerja simpang (control delay, LOS, antrean); ukuran kinerja arteri/jaringan (stops, travel speed, arterial LOS, **bandwidth efficiency & attainability**, emisi, PI); safety assessment; warrants. |
| 4 Traffic Signal Design Concepts | 4-1 – 4-31 | Phasing, display belok kiri, urutan fase, ped phasing, right-turn, **detection fundamentals** (pulse/presence, locking/non-locking, indecision zone), aplikasi deteksi. |
| 5 Basic Signal Timing Procedure & Controller Parameters | 5-1 – 5-43 | **Mode operasi** (pre-timed/semi/fully-actuated/coordinated, Tabel 5-1); interval & parameter dasar (min/max green, change period Kell & Fullerton, ped timing); parameter aktuasi (recall, passage time & MAH, simultaneous gap, dual entry); **volume-density** (gap reduction, variable initial); parameter detektor (delay, extend, call, queue); time-base controls. |
| 6 Coordination | 6-1 – 6-49 | Terminologi; prinsip; **mekanika koordinasi** (cycle, yield point, split, force-off, permissive, offset & reference point per tipe kontroler, master clock); time-space diagram; **transition logic** (dwell, max dwell, add, subtract, shortway); panduan rencana (coordinated phase, cycle length: manual/Webster/HCM/network, split, offset); kompleksitas. |
| 7 Developing Signal Timing Plans | 7-1 – 7-30 | Scoping, data, model, implementasi, evaluasi. |
| 8 Signal Timing Maintenance | 8-1 – 8-13 | Aktivitas pemeliharaan timing, inventaris, day-to-day, **kebutuhan staf** (Tabel 8-2). |
| 9 Advanced Signal Timing Concepts | 9-1 – 9-16 | **Preemption** (MUTCD transisi masuk/keluar), **TSP** (NTCIP 1211: PRG/PRS), **Traffic Responsive** (V+kO, hysteresis), **Adaptive** (proses 4 langkah; **SCOOT, SCATS, RHODES, OPAC, ACS-Lite**), special event/incident/evacuation, cuaca. |

### A.3 NCDOT Signal System Timing Philosophy Manual v2.0 (2017)

Bukan manual teknis mendalam, melainkan **katalog dokumen tata kelola program** (COST = Central Office System Timing Section; 326 sistem closed-loop + 54 time-based = 2.360 simpang; NCDOT *Roles and Responsibilities*, hal. 1). Strukturnya:

| Kategori | Dokumen | Isi pokok |
|---|---|---|
| Program Management | Corridor Selection Process (hal. 1-2); Performance Goals; Data Needs and Applications | Siklus retiming 3 tahun (kritis 18 bulan, non-kritis 5–6 tahun); target 40%/20% pengurangan travel time; matriks sumber data (counts, Tru-Traffic, split monitor, Bluetooth, high-resolution data, probe). |
| Timing | Project Process; Context of a Corridor; Establishing Operational Objectives (hal. 1-9); Field Visit Protocol; Data Collection; Final Report Recommendations; "High Priority Ped" Tool (Oasis); Alternative Timing Plans (hal. 1-2) | **Hierarki Objective → Strategy → Tactic** (Tabel 1-3); kriteria derajat kejenuhan (v/c<0,85; >1,0); gejala lapangan; rencana insiden/badai/sementara/special event (nomor plan 51-59). |
| Assessment | Standard Practice for Performing Travel Time Runs (hal. 1-2); Cost Benefit Analysis (hal. 1-5) | Protokol floating car ≥6 run/arah; formula manfaat tahunan (delay & stops). |
| Monitoring | Roles and Responsibilities (hal. 1-2); Impacts on a Corridor | Pembagian peran Division/COST/PEF; dampak konstruksi & pengembangan baru. |
| Strategic Planning | Continuous Data Options (hal. 1-4); Historical Documentation; ICM; DDI; Emissions Data | HRCD, Bluetooth, probe, Wi-Fi, DSRC, system detectors. |
| Supporting | Scope of Services FY2017 (hal. 1-7) | 10 tugas proyek retiming, format laporan. |

---

## B. Konsep Dasar Signal Timing

### B.1 Terminologi inti

- **Movement (pergerakan)**: aksi pengguna di simpang, mis. belok kiri arah utara atau pejalan kaki di zebra barat; bisa *permitted* (harus mengalah) atau *protected* (hak jalan eksklusif) (STM2 §3.1, hal. 3-2; Glossary A-7). Simpang 4 kaki punya 12 pergerakan kendaraan satu arah + 4 pergerakan pejalan kaki dua arah; HCM memberi nomor belok kanan = nomor through + 10 (STM2 §5.1.1, hal. 5-1).
- **Phase (fase)**: "a timing process, within the signal controller, that facilitates serving one or more movements at the same time" (STM2 §5.1.1, hal. 5-1).
- **Interval**: durasi ketika indikasi sinyal tidak berubah (red, yellow, green, FDW) (STM2 Glossary A-6; TSTM §5.3, hal. 5-5 mengutip NTCIP 1202).
- **Penomoran fase NEMA** (STM2 §5.1.1, hal. 5-2 – 5-3): fase genap = through (2 & 6 jalan utama, 4 & 8 jalan minor); fase ganjil = belok kiri (1 & 5 utama, 3 & 7 minor); fase pejalan kaki mengikuti nomor fase through paralel (2P, 6P, 4P, 8P). Konvensi manual: **fase 2 & 6 = fase terkoordinasi**.
- **Ring-and-barrier** (STM2 §5.1.2, hal. 5-4): *ring* = urutan fase yang saling konflik; *barrier* = titik di mana kedua ring harus berakhir bersamaan (biasanya memisahkan fase jalan utama dan minor). Aturan: fase mana pun di Ring 1 boleh berjalan bersama fase mana pun di Ring 2 di antara barrier yang sama (1,2,5,6 kompatibel; 3,4,7,8 kompatibel); fase bisa dilewati (skipped) atau memberi sisa waktunya ke fase berikutnya dalam ring yang sama.
- **Opsi fase belok kiri** (STM2 §5.1.3, Exhibit 5-4, hal. 5-5 – 5-10): permitted, protected, protected-permitted (butuh FYA atau 5-section head), split phasing, prohibited (bisa per jam). Urutan: lead-lead (paling umum), lag-lag, lead-lag (untuk progresi terkoordinasi; risiko *yellow trap* pada protected-permitted tanpa FYA; kontroler modern punya fitur "anti-backup"/"trap protected phase", hal. 5-7).
- **Overlap** (STM2 §5.1.4, hal. 5-11 – 5-16): keluaran terpisah dengan load switch sendiri, dikendalikan *parent phase* (menjumlah) dan *modifier phase* (mengecualikan, mis. "Pedestrian Protect/Omit on Green" untuk overlap belok kanan vs pejalan kaki). *Trailing overlap* melanjutkan setelah parent phase berakhir (untuk simpang berdekatan).
- **Detector assignment & load switch** (STM2 §5.1.5–5.1.6, hal. 5-16 – 5-18): tiap detektor punya nomor unik; fungsi *call* aktif hanya saat fase tidak hijau, *extend* hanya saat hijau. Load switch 3 output (R/Y/G); ped memakai G=walk, R=don't walk (flash 0,5 s); FYA sering memakai output "yellow" ped.

### B.2 Jenis kendali (controller modes)

Menurut STM2 §3.1.2 (hal. 3-4 – 3-5) dua karakteristik pembeda kontroler: (1) cara menafsirkan permintaan lokal, (2) hubungan dengan kontroler lain.

| Mode | Definisi | Kapan cocok (TSTM Tabel 5-1, hal. 5-3) |
|---|---|---|
| **Pretimed (fixed-time)** | Tanpa deteksi; interval tetap; dicapai di kontroler modern dengan max green = green tetap + *maximum recall* (TSTM hal. 5-4) | CBD grid rapat, volume konsisten, ≤3 fase; work zone |
| **Semi-actuated** | Deteksi hanya di jalan minor; fase utama non-actuated dan *dwell* di hijau | Arteri terkoordinasi; utama <40 mph, minor ringan |
| **Fully-actuated** | Deteksi semua pendekat; "fully adaptive to local traffic conditions" | Simpang terisolasi, rural cepat, pertemuan dua arteri |
| **Coordinated (actuated-coordinated)** | Memaksakan *common cycle length*, split, offset; fase terkoordinasi dijamin sebagian hijau; sebagian fase terkoordinasi boleh diaktuasi (STM2 hal. 3-4, 7-31) | Arteri padat dengan simpang berdekatan (≤½ mil) |
| **Traffic responsive** | Memilih rencana dari pustaka berdasarkan detektor sistem (STM2 §9.3) | Fluktuasi besar & persisten (≥30 menit) |
| **Adaptive (ASCT)** | Menghitung ulang parameter dari deteksi; "does not operate with time-of-day plans" (Glossary A-1); "should only be considered after the capabilities of traditional systems have been fully considered" (STM2 hal. 3-5) | Variabilitas tak terduga |

### B.3 Deteksi: jenis, mode, penempatan

- **Mode detektor**: *pulse* (pulsa 0,10–0,15 s; hanya untuk detektor sistem penghitung) vs *presence* (aktuasi selama kendaraan berada di zona; direkomendasikan) (TSTM §4.7.2, hal. 4-23; STM2 §4.1 hal. 4-2, §6.1.5 hal. 6-10).
- **Memory mode kontroler**: *non-locking* (default; panggilan hilang begitu kendaraan pergi — memungkinkan RTOR/belok permitted tanpa memanggil fase) vs *locking* (aktuasi pertama saat merah ditahan sampai fase dilayani; untuk setback tanpa stop-bar) (STM2 §6.1.8, hal. 6-21; TSTM §4.7.3, hal. 4-23 – 4-24).
- **Fungsi deteksi** (STM2 §4.1, hal. 4-2): identifikasi kehadiran, extend fase, identifikasi gap, terminasi aman (decision zone), monitoring MOE, penghitungan volume/klasifikasi.
- **Prioritas lokasi deteksi** (STM2 hal. 4-4): (1) stop bar jalan minor & lajur belok kiri; (2) setback jalan utama; (3) stop bar jalan utama. Stop bar presence bisa *drop call*; setback memberi proteksi *decision zone* dan gap-out efisien; kombinasi keduanya paling efisien dengan fitur *stop bar detector disconnect* setelah antrean bersih (hal. 4-5).
- **Decision zone (Type II dilemma zone)** ≈ 5,5 s sampai 2,5 s waktu tempuh dari stop bar (Exhibit 4-7, hal. 4-6: 35 mph → 285–125 ft; 55 mph → 445–200 ft). Setiap max-out/force-off menghilangkan proteksi (hal. 4-7). TSTM hal. 4-25: detektor terjauh di awal indecision zone (5–5,5 s travel time pada kecepatan persentil-85), detektor berikutnya untuk kecepatan 10 mph lebih rendah, biasanya 3–4 detektor.
- **Pendekat kecepatan rendah**: zona stop-bar besar (60–80 ft) memungkinkan passage time ≈ 0 (STM2 hal. 4-7).
- **Delay detektor** untuk lajur belok kanan (RTOR) 8–12 s; anti-panggilan salah di lajur belok kiri 2–5 s (STM2 Exhibit 6-24, hal. 6-25); belok kiri prot-perm dengan opposing on recall 3–7 s (TSTM hal. 5-27). **Extend/carry-over** ≤2 s (STM2 hal. 6-25; TSTM 0,1–2,0 s hal. 5-27). **Detector switching**: detektor lajur kiri memperpanjang fase through saat interval permitted (STM2 Exhibit 6-26, hal. 6-27). Parameter NTCIP: *call*, *queue* (TSTM §5.6.4–5.6.5, hal. 5-28).
- **Teknologi**: in-ground (loop induktif, magnetometer) vs above-ground (video, microwave/radar) (STM2 Exhibit 4-3, hal. 4-3); rujukan FHWA *Traffic Detector Handbook* 3rd ed.

### B.4 Parameter fase dasar dan nilai tipikal

**Yellow change** (STM2 §6.1.1, hal. 6-3 – 6-4; TSTM §5.3.2, hal. 5-12 – 5-13). Rumus ITE (STM2 Eq. 6-1; TSTM Eq. 5-2 suku pertama):

```
Y = t + 1.47·v / (2·(a + 32.2·g))         [satuan US: v mph, a ft/s², g desimal]
Y = t + v / (2·(a + 9.81·g))              [SI: v m/s, a m/s²]
```
dengan t = 1,0 s, a = 10 ft/s² (≈3,0 m/s²) (NCHRP 731). Kecepatan = persentil-85 atau batas kecepatan. MUTCD: 3–6 s, minimum 3 s. Tabel STM2 Exhibit 6-2: 25 mph→3,0; 30→3,2; 35→3,6; 40→3,9; 45→4,3; 50→4,7; 55→5,0; 60→5,4 s; koreksi ±0,1 s per 1 % gradien (turunan +, tanjakan −).

**Red clearance** (STM2 §6.1.2, hal. 6-4 – 6-5; TSTM Eq. 5-2 suku kedua): opsional; `R = (W + Lv) / (1.47·v)` dengan W lebar simpang (stop bar sampai tepi luar lajur konflik terjauh), Lv = 20 ft (TSTM) — NCHRP 731 mengurangi 1 s karena kendaraan tidak masuk sampai 1 s setelah hijau; Exhibit 6-3 (mis. 30 mph, W=70 ft → 1,0 s). MUTCD: red clearance ≤ 6 s. Survei praktisi: 0,5–2,0 s (TSTM hal. 5-12). Bukti keselamatan jangka panjang lemah (studi MnDOT).

**Minimum green** (STM2 §6.1.3, hal. 6-5 – 6-8): berdasarkan (a) *driver expectancy* — Exhibit 6-4: through arteri utama >40 mph 10–15 s; ≤40 mph 7–15; minor arterial 4–10; kolektor/lokal 2–5; belok kiri 2–10 s (versi TSTM Tabel 5-3: belok kiri 2–5 s); (b) *queue clearance* tanpa stop-bar: `Gq = 3 + 2·n`, `n = d / Lv` (Lv = 25 ft) (STM2 Eq. 6-2/6-3 — badan rumus dari TSTM Tabel 5-4 catatan 2); (c) sepeda: `Gmin + Y + Rclear = 6 + (w + 6) / 14.7` (Caltrans; STM2 Eq. 6-4 *[rekonstruksi, cocok dengan Exhibit 6-7]*); (d) ped tanpa tombol: `Gp = PW + PC` (TSTM Eq. 5-1). **Variable initial / added initial**: min green sebagai batas bawah, max initial = Gq; +2,0 s per aktuasi (1 lajur), 1,5 s (2 lajur), 1,2 s (≥3 lajur) (STM2 Exhibit 6-5; TSTM hal. 5-25; LADOT: `AI = 2 + 3·(MI−3)/2` *[bentuk dari teks ekstraksi tidak sepenuhnya jelas]*).

**Maximum green** (STM2 §6.1.4, hal. 6-8 – 6-10): timer mulai saat ada *conflicting call*; membatasi delay & siklus; melindungi dari detektor rusak (mode gagal detektor = *continuous call*). Nilai Exhibit 6-9: through utama >40 mph 50–70; ≤40 mph 40–60; minor 30–50; kolektor 20–40; kiri 15–30 s. TSTM Tabel 5-6: `Gmax = (V·C)/(1200·n) + 1` (min 15 s), atau 1,25–1,5 × green minimum-delay pretimed; hingga 1,7× saat volume rendah (hal. 5-10 – 5-11). Bervariasi per waktu (Max 2, Max 3).

**Passage time (unit extension / gap)** (STM2 §6.1.5, hal. 6-10 – 6-15): timer mundur mulai saat aktuasi hilang, direset oleh aktuasi berikut. Fase gap-out hanya bila: (1) min green habis, (2) ada panggilan konflik, (3) passage timer habis. Nilai (Exhibit 6-12, headway 3 s): zona 6 ft: 2,3–2,7 s; 20 ft: 1,9–2,5; 40 ft: 1,4–2,3; 60 ft: 0,8–2,0; 80 ft: 0,3–1,8 s. Setback tunggal 2–3 s. TSTM Eq. 5-5: `PT = MAH − (Lv + Ld)/(1.47·va)`, MAH = 3,0 s (tanpa gap reduction), 4,0 s (dengan), +0,1 s tanjakan curam, +1,0 s truk banyak; va = 0,88 × v85 (hal. 5-20 – 5-21). *Simultaneous gap-out*: kedua ring harus gap-out bersama sebelum barrier; tidak disarankan pada volume sedang-tinggi (STM2 hal. 6-11 – 6-12) tetapi diaktifkan bila ada advance detection untuk terminasi aman (TSTM hal. 5-21).

**Gap reduction (volume-density)** (STM2 hal. 6-14; TSTM §5.5.1, hal. 5-22 – 5-24): *time before reduction* (mulai saat ada panggilan konflik; ≥10 s, contoh = min green) → reduksi linier selama *time to reduce* (contoh = ½(max−min green)) sampai *minimum gap* (MAH 2,0 s; Tabel 5-11).

**Interval pejalan kaki** (STM2 §6.1.6, hal. 6-16 – 6-20; TSTM §5.3.3, hal. 5-14 – 5-16): walk → FDW → steady don't walk. MUTCD: walk ≥7 s (boleh 4 s bila volume rendah; 10–15 s di CBD/sekolah); clearance `PCT = Dc / vp`, vp = 3,5 ft/s (1,07 m/s); FDW yang diprogram = PCT − (Y + R) atau = PCT (kebijakan konservatif); countdown ped harus selesai sebelum kuning; steady DW ≥3 s sebelum pelepasan konflik. **Leading Pedestrian Interval** ≥3 s. Opsi extended push-button untuk kecepatan hingga 4 ft/s. Total ped tidak boleh dipotong oleh max green — fase kendaraan diperpanjang sampai FDW selesai (hal. 6-17).

**Dual entry** (STM2 §6.1.7, hal. 6-20): fase kompatibel ikut menyala meski hanya satu yang dipanggil (umum untuk through).

**Recall** (STM2 §6.1.8, hal. 6-20 – 6-22): *minimum (vehicle) recall*, *maximum recall* (≈ pretimed), *soft recall* (panggil bila tak ada panggilan konflik — tipikal untuk fase 2/6 di free), *pedestrian recall*, *red rest*, *green rest*. Setelan tipikal fully-actuated (Exhibit 6-22): soft recall hanya 2 & 6, lainnya off, locking off.

**Time-of-day plans** (STM2 §6.3, hal. 6-27): parameter bervariasi per jam/hari/musim (mis. max green 20 s → 30 s saat puncak); TSTM §5.7: parameter time-base umum = Max 2, phase omit, min recall; NTCIP *pattern* = cycle, offset, split/force-off, sequence + recall/omit per fase (hal. 5-29).

### B.5 Kapasitas, lost time, v/c, pergerakan kritis, tundaan

Sumber utama TSTM §3.3 (hal. 3-5 – 3-13) dan STM2 §5.2 (hal. 5-19 – 5-26).

- **Start-up lost time** ≈ 2 s (TSTM), 3 s (STM2 Eq. 6-2); **saturation flow** `s = 3600 / h` (h = headway jenuh; h=2,2 s → 1.636 vphpl; tipikal 1.500–2.000 pcphpl; ideal 1.900); pendekatan praktis 1.800 vph = 2 s/kendaraan.
- **Effective green** `g = G + Y + R − (l1 + l2)` (TSTM Eq. 3-1); default HCM lost time 4 s/fase; STM2 Exhibit 5-30 memakai 5 s/fase (8 fase → 20 s/siklus).
- **Capacity** `c = s · g / C` (TSTM Eq. 3-2); **v/c** `X = v / c = v·C / (s·g)` (Eq. 3-3). Ambang: <0,85 undersaturated stabil; 0,85–1,00 tidak stabil; >1,00 oversaturated (Tabel 3-2, hal. 3-12). Untuk progresi tanpa henti, v/c fase through terkoordinasi sebaiknya ≤ ~0,85 (hal. 3-10).
- **Critical movement analysis / QEM** (STM2 §5.2; TSTM Tabel 3-1): (1) volume per lajur (peak-15-min, PHF, truk = 2 pcu, lane imbalance); (2) pasangan fase konflik antar barrier: bandingkan (1+2) vs (5+6), (3+4) vs (7+8) — ambil lajur tertinggi; split phasing: jumlahkan lajur tertinggi tiap pendekat; (3) *critical sum* CS = kritis utama + kritis minor; (4) estimasi siklus: Exhibit 5-30 (headway 2,5 s, 5 s lost/fase): C=60 → 933 vph; 90 → 1.089; 110 → 1.145; 120 → 1.167 vph. TSTM: `Xcm = CS / (RS·(1 − L/C))`, RS = 1.530 × PHF × fa (fa = 0,90 CBD) (Contoh 3-1, hal. 3-13); split awal ∝ volume kritis dengan v/c sama.
- **Siklus optimum Webster** (STM2 Eq. 7-1, hal. 7-24; TSTM Eq. 6-1, hal. 6-32): `C = (1.5·L + 5) / (1 − Y)`, Y = Σ (volume lajur kritis / saturation flow), L = lost time/siklus; hanya valid undersaturated dan fokus kendaraan. **HCM QEM**: `C = L / (1 − min(CS, RS)/RS)`, RS = 1.710·PHF·fa, min 60 s, maks ditentukan yurisdiksi (mis. 150 s) (TSTM Eq. 6-2, hal. 6-33). Peringatan: siklus 120→180 s hanya +2 % kapasitas (TSTM Gambar 6-16, hal. 6-28); STM2 hal. 12-7: hijau >30 s menurunkan saturation flow.
- **Control delay & LOS HCM** (TSTM §3.4.1, hal. 3-14): rumus HCM Bab 16 tidak ditulis eksplisit, hanya faktor (volume, kapasitas, cycle, g, arrival type/PF). LOS: A ≤10; B 10–20; C 20–35; D 35–55; E 55–80; F >80 s/kend. **Arterial LOS** berdasarkan kecepatan (Tabel 3-6, hal. 3-19).
- **Antrean praktis** (TSTM §3.4.3, hal. 3-16 – 3-17): `Q_avg = v·C/3600` (semua tiba saat merah) atau `v·(C−g)/3600`; `Q95 ≈ 2·Q_avg`; 25 ft/kendaraan; green ≈ 2 + 2·Q.
- **Bandwidth efficiency** `E = (B_A + B_B)/(2C)` (PASSER II: 0,00–0,12 buruk; 0,13–0,24 cukup; 0,25–0,36 baik; ≥0,37 sangat baik) dan **attainability** `= bandwidth / g_crit` (TSTM Eq. 3-7/3-8, hal. 3-20 – 3-21).
- **Performance Index** Synchro: `PI = D·1 + St·10 + QP·100` (per 3600) (TSTM Eq. 6-3, hal. 6-35).
- Perbedaan **demand vs volume** ditegaskan: "Traffic volumes do not represent traffic demand if queuing exists" (STM2 hal. 3-12).

### B.6 Ukuran kinerja dasar (dirinci di G)

STM2 Exhibit 3-17 (hal. 3-22) menghubungkan ukuran kinerja ↔ parameter timing ↔ metode pengumpulan; **15 tujuan operasional** dirinci di §3.4.1 (hal. 3-20 – 3-21): 7 kendaraan (safety, capacity allocation, corridor progression, secondary progression, environmental, queue length management, vehicle & driver costs), 3 pejalan kaki, 2 sepeda, 3 transit.

---

## C. Koordinasi (Coordination)

### C.1 Kapan dikoordinasikan
Simpang ≤ ½ mil (≈800 m) hampir selalu bermanfaat dikoordinasikan; >½ mil perlu tinjauan platoon; bisa >1 mil bila variasi arus antar simpang kecil (STM2 §7.1, hal. 7-1). Simpang <500 ft (7–10 s) butuh manajemen antrean & siklus pendek, bahkan satu kontroler (STM2 hal. 3-8, 12-8). Keluhan warga terbanyak: delay di jalan minor saat tak ada konflik — jangan menjalankan koordinasi terlalu malam (hal. 7-2, 3-12).

### C.2 Time-space diagram, master/local clock, bandwidth
- Sumbu: waktu (horizontal) vs jarak (vertikal), harus **berskala** (STM2 §7.2.1, hal. 7-2). Master clock (system/field master/central) vs local clock; keduanya harus sama (§7.2.2, hal. 7-2 – 7-3). Trajektori kendaraan: 5 kondisi (stopped, perception-reaction, acceleration, running speed, stopping) (Exhibit 7-6, hal. 7-7).
- **Bandwidth**: "the maximum amount of green time for a designated coordinated movement as it passes through a corridor at an assumed constant speed" (Glossary A-1); idealisasi — tidak memperhitungkan akselerasi, dispersi, antrean hilir; tergantung *progression speed*; berbeda per arah; koridor panjang sebaiknya dipecah dengan *programmed stop*; saat jenuh bandwidth "may never occur" (§7.2.6, hal. 7-8 – 7-9). Lead-lag di simpang tengah memperlebar band (Exhibit 7-10).

### C.3 Parameter koordinasi (istilah NTCIP 1202: *pattern* = cycle + split + offset + sequence) — STM2 §7.3 (hal. 7-11 – 7-17)

| Parameter | Definisi | Panduan (STM2 §7.4; TSTM §6.3/6.6) |
|---|---|---|
| **Coordinated phase(s)** | Fase yang selalu mendapat jatah hijau minimum tiap siklus (biasanya 2 & 6) | Bisa fase belok bila O-D menuntut (7-17); diamond interchange contoh pengecualian (TSTM 6-27) |
| **Cycle length** | Waktu satu urutan fase lengkap; sama untuk semua simpang dalam kelompok kecuali *double/half cycling* | Metode: manual (alternate: single/double/triple; Exhibit 7-18 — kecepatan progresi = jarak blok / (½, ¼, ⅙ siklus); quarter-cycle offset grid Portland 60 s/13 mph), critical intersection (Webster), network (Synchro/PASSER/TRANSYT). Umumnya ≤120 s (TSTM 6-28); siklus panjang memperburuk bila throughput > kapasitas hilir, turn-bay meluap, headway naik, variabilitas hijau aktuasi (split >50 s) (STM2 7-18) |
| **Split** | Porsi siklus per fase = green + yellow + red clearance; detik atau %; Σ ≤ C | Kebijakan: (a) kapasitas desain untuk minor, sisa ke koordinasi; (b) v/c sama untuk pergerakan kritis; pertimbangkan ped, transit, bandwidth (7-25 – 7-26) |
| **Force-off** | Titik siklus di mana fase non-koordinasi harus berakhir walau masih ada permintaan; tak bisa memotong min time/clearance | *Floating* (fase dibatasi split-nya; sisa ke fase koordinasi) vs *fixed* (fase berikut boleh mewarisi waktu tak terpakai hingga force-off tetapnya; mengurangi *early return to green*). Fase tepat setelah fase koordinasi tak pernah mewarisi. **Inhibit Max** mematikan max green saat koordinasi (7-13 – 7-14, 7-26) |
| **Permissive period** | Jendela waktu kontroler boleh meninggalkan fase koordinasi ke fase non-koordinasi | Simultaneous vs sequential; umumnya kontroler memaksimalkan otomatis (7-14 – 7-15, 7-26) |
| **Yield point** | Awal permissive pertama = titik terawal fase koordinasi boleh diterminasi; juga titik pergantian TOD plan | Dihitung kontroler dari offset reference & walk mode (7-15, 7-26) |
| **Pattern sync reference** | Awal master clock harian (tengah malam, 01:00, 03:00) | Pilih saat volume rendah; butuh referensi waktu andal (GPS); perhatikan DST (7-15, 7-27) |
| **Offset reference point** | Titik siklus lokal yang diacu terhadap master clock | Opsi: awal hijau koordinasi pertama (NTCIP resmi; tidak teramati karena early return), awal hijau keduanya, awal FDW, **awal kuning fase koordinasi pertama** (dipakai manual; teramati di lapangan). Harus konsisten se-sistem (7-15 – 7-16, 7-27). TSTM: TS1 = awal 2&6, TS2 = awal hijau fase pertama, 170 = awal kuning (6-13) |
| **Offset** | Waktu (detik/%) antara master zero dan offset reference point lokal | Berdasarkan kecepatan, jarak, volume; platoon tiba di awal hijau atau setelah antrean minor terlepas; kontroler modern memantau arrival-on-green untuk fine-tuning (7-16, 7-27) |

### C.4 Pejalan kaki dan walk modes dalam koordinasi (STM2 §7.5.1, hal. 7-28 – 7-31)
Bila split tak cukup untuk ped, kontroler melewati force-off dan harus *transition* — bisa lebih efisien daripada melayani ped tiap siklus jika ped jarang. Walk modes: **rest in walk** (dwell di walk selama hijau koordinasi; FDW melewati yield point), **rest in don't walk** (butuh deteksi ped), **extended walk** (kompromi). *Pedestrian re-service* memungkinkan walk dua kali per siklus.

### C.5 Mengaktuasi fase terkoordinasi (STM2 §7.5.2, hal. 7-31 – 7-32; §9.2.1)
Sebagian akhir split fase koordinasi diaktuasi → boleh gap-out, memberi waktu ke minor & belok, meningkatkan proteksi decision zone; nilai terlalu besar → early return & platoon tertahan.

### C.6 Logika transisi (STM2 §7.5.3, hal. 7-32 – 7-35; TSTM §6.5, hal. 6-22 – 6-26)
Pemicu: jadwal TOD, operator manual, traffic responsive, preemption, adaptive pattern selection, koreksi jam, ped melebihi split, power loss. Algoritma 1–5 siklus; batas penyesuaian per siklus (contoh ±20 %). Mode:
- **Dwell**: tahan di fase koordinasi sampai offset baru (deterministik, semua waktu ke fase koordinasi).
- **Max Dwell**: dwell dengan batas per siklus.
- **Add (lengthen)**: perpanjang semua fase proporsional; disukai bila ada preemption (fase yang dilewati tidak dipotong).
- **Subtract (shorten)**: perpendek fase sampai batas min green/ped; efektif untuk koreksi kecil.
- **Shortway/bestway/smooth**: pilih add atau subtract tercepat; "least disruptive" kecuali ada preemption atau near-saturated.
Rekomendasi: tetap dalam satu pattern **≥30 menit**; hindari ganti saat padat; mulai plan puncak lebih awal (STM2 hal. 7-33; TSTM 6-26; NCDOT *Tactics* "Minimize Number/Duration of Transitions", hal. 7).

### C.7 Kompleksitas (STM2 §7.6, hal. 7-35 – 7-38)
Urutan fase kiri (lead-lag; sekuens bisa berbeda per TOD dengan FYA); **early return to green** (fase koordinasi mulai lebih awal karena minor gap-out — menyebabkan stop di hilir; mitigasi: geser offset atau fixed force-off); volume minor besar; interaksi turn-bay; **critical intersection control** (semua pakai siklus kritis; double/half cycling; atau simpang kritis *free* dan minor terkoordinasi siklus pendek).

---

## D. Kendali Adaptif (Adaptive Signal Control) menurut Manual

### D.1 Definisi dan posisi dalam hierarki
- STM2 §9.4 (hal. 9-11): "ASCT is a signal system technology that uses detection data and algorithms to adjust signal timing parameters for current conditions"; berbeda dari traffic responsive yang hanya memilih rencana pra-program; "ASCT systems are not 'set-and-forget' systems"; "It is critical to acknowledge that ASCT cannot solve underlying system capacity issues" (sidebar 9-11).
- TSTM §9.4 (hal. 9-8 – 9-9): "vehicular traffic in a network is detected at an upstream and/or downstream point and an algorithm is used to predict when and where the traffic will be and to make signal adjustments... based on those predictions"; manfaat rata-rata ~10 %, hingga 50 % pada kondisi buruk; kadang tidak lebih baik dari actuated yang ditala baik; unggul ketika arus fluktuatif harian, perubahan tata guna lahan, insiden, preemption; menunda onset oversaturation dan pulih lebih cepat; pada volume sangat rendah fixed-time bisa lebih baik.
- STM2 §12.3.4 (hal. 12-21): kemampuan adaptif memitigasi oversaturation "has not been demonstrated"; fitur intinya (cycle adjust, split reallocation, offset adjust, sequence modification) menunda onset kemacetan.

### D.2 Urutan pertimbangan sebelum ASCT (STM2 §9.2, hal. 9-3 – 9-4)
Selidiki dulu fitur koordinasi lanjut: *actuating the coordinated phase*, **dynamic phase length** (extended/adaptive split — menggeser force-off tanpa mengubah siklus; butuh estimasi permintaan dari antrean detektor), **phase re-service/conditional service** (fase dilayani >1× per siklus saat volume rendah-sedang).

### D.3 Traffic Responsive Plan Selection (TRPS) — STM2 §9.3 (hal. 9-4 – 9-11); TSTM §9.3 (hal. 9-7 – 9-8)
- Memilih dari pustaka rencana; syarat: rencana lama minimal berjalan sekian waktu dan rencana baru harus lebih baik sekian %; semua sinyal dalam grup berganti bersamaan; bisa override TOD atau manual/special event.
- **Target-based (UTCS, FHWA 1970-an)**: bandingkan volume ekuivalen `V + K·O` tiap detektor terhadap *signature* target tiap pattern; Eq. 9-1 *[rekonstruksi]*: `err_j = Σ_i w_i · |(V_i + K·O_i) − T_ij|`; pilih pattern dengan err terendah bila lebih rendah dari persentase nilai pattern berjalan. K menskalakan okupansi ke volume (K=17 → 100 % okupansi ≈ 1.700 vplph di sisi keluar; K 5–7 dekat stop bar).
- **Threshold-based**: *computation channel* `CC = Σ_i w_i·(V_i + K·O_i)` (Eq. 9-2) dibandingkan ambang masuk/keluar (hysteresis; Exhibit 9-2: offset 2→3 masuk 52, keluar 49). Indeks: cycle ∝ volume arteri (V+KO); split ∝ rasio arteri/minor; offset ∝ rasio inbound/outbound.
- Contoh matriks pattern: 6 tipe cycle/split × 5 tipe offset = 30 pattern (Exhibit 9-6); signature target per detektor (Exhibit 9-7).
- Deteksi sistem: setback jauh dari stop bar, zona kecil 6×6 ft, sisi keluar, per lajur; toleransi detektor gagal (nilai 0/diabaikan; terlalu banyak gagal → TRPS nonaktif); smoothing 50 % lazim; efektif untuk perubahan besar & persisten ≥30 menit (hal. 9-10 – 9-11). TSTM: hysteresis tetap sering menyebabkan perubahan terlalu sering; lambat merespons insiden mendadak (hal. 9-8).

### D.4 Arsitektur & karakteristik ASCT (STM2 §9.4.2, hal. 9-12 – 9-15)
- Struktur dasar: **deteksi → kalkulasi rencana → pemilihan setelan berikutnya**; kebanyakan tertinggal ≥1 siklus.
- **Adaptive groups/subsystems** dengan siklus bersama; *cross-coordination* multi-rute; simpang perbatasan bisa pindah subsistem berdasarkan *suitability factor*.
- **Dua metode kalkulasi**: (1) *download* parameter baru (cycle/split/offset) ke kontroler lokal yang tetap memakai gap-out & force-off — pencarian dibatasi di sekitar nilai kini (split 15 → 10–20 s; siklus 100 → 110–120 s) untuk membatasi transisi & over-reaksi; (2) *override* kontroler melalui perintah **hold/force-off** atau kendali panggilan fase (hardwire pada 332/336/TS-1; SIU pada TS-2/ITS) — memungkinkan **rolling-horizon**: evaluasi ratusan opsi durasi/urutan untuk 60 s ke depan, terapkan 5 s pertama, ulangi.
- **Parameter tuning**: min/max green, kepatuhan ped, langkah perubahan, batas cycle/offset, hal yang dilarang diubah (sequence, skip).
- **Deteksi**: 5 lokasi potensial — stop bar (degree of saturation, antrean), setback (decision zone, profil kedatangan; makin jauh makin baik; jauhi driveway), mid-block, upstream (sisi hilir simpang hulu), setback di mulut turn bay; tak ada sistem yang butuh kelimanya tetapi deteksi semua fase wajib; lane-by-lane terbaik; stop bar pendek lebih akurat (praktik: ≥50 ft masih diterima).
- **Komunikasi** vital; IP (kabel/nirkabel) mempermudah; ASCT bisa membaca detektor langsung atau via kontroler.
- **Konfigurasi fase**: sebagian hanya 8 fase dual-ring; banyak berbasis *stage* (kombinasi fase 1+6, 1+5, 2+5, 2+6 dst. harus dikonfigurasi).
- **Tujuan agensi** (Exhibit 9-8, hal. 9-12): pipeline, smooth flow, equitable access, manage queues, mitigate oversaturation, accommodate long-term variability, manage events & incidents — kepuasan bergantung kecocokan fungsi objektif ASCT dengan tujuan agensi; kebanyakan ASCT belum bisa berganti objektif per TOD (hal. 9-11 – 9-12).

### D.5 Algoritma spesifik (TSTM §9.4, hal. 9-11 – 9-13)

| Sistem | Deteksi | Mekanisme | Catatan |
|---|---|---|---|
| **SCOOT** (UK) | Stop-line + advance 150–1.000 ft hulu (atau exit loops) | Tiga optimizer: *split* (geser perubahan fase beberapa detik untuk meminimalkan degree of saturation), *offset* (per siklus, memakai cyclic flow profiles, geser semua offset), *cycle* (per *region* dengan min/max; targetkan node terpadat 90 % saturasi; turunkan siklus bila semua <90 %). Kirim **hold/force-off** ke kontroler; estimasi panjang antrean | Paling luas dipakai |
| **SCATS** (Australia) | Hitung di stop line + ukur gap | Memilih *split plan* dari pustaka dan menskalakannya pada rentang cycle; kontroler lokal tetap gap-out/force-off | Data per detik ke pusat |
| **RHODES** | Upstream + stop bar semua pendekat | Peer-to-peer; prediksi kedatangan 45–60 s; re-solve tiap 5 s; hold/force-off | Banyak parameter kalibrasi |
| **OPAC** "Virtual Fixed Cycle" | Detektor 10–15 s hulu | Rolling-horizon prediktif; maksimalkan throughput; ubah split/offset/cycle, urutan tetap; sinkronisasi jaringan via fixed plan offline atau *virtual cycle* online | Hold/force-off |
| **ACS-Lite** | Modest | Unit master mengunduh cycle/offset/split tiap **5–15 menit**; model sederhana, kalibrasi ringan | Paling lambat merespons |
| *InSync* | — | **Tidak dibahas** di ketiga dokumen (tidak ada). | — |

### D.6 Instalasi, O&M, validasi (STM2 §9.4.3–9.4.5, hal. 9-15 – 9-18)
Instalasi: perangkat ASCT di kabinet, IT/database/server; kalibrasi parameter adaptif & model; jam adaptif on/off; integrasi preemption, TSP, countdown ped; pemisahan kabel detektor per lajur; verifikasi deteksi & komunikasi. O&M: tinjau keputusan ASCT untuk rekalibrasi; analisis MOE rutin; **backup timing plans**; **failure mode** terdefinisi (koordinasi vs free) bila deteksi/komunikasi/ASCT gagal; backup database; PIC vendor. Validasi: nyatakan tujuan & MOE jelas; validasi kinerja jalan minor dengan data resolusi tinggi; lengkapi probe dengan re-identifikasi; evaluasi bahu puncak (di puncak jenuh ASCT mungkin tidak unggul); simulasi insiden; before/after berdekatan; pendekatan **on/off bergantian hari**; retiming tepat sebelum ASCT membuat hasil validasi kurang mengesankan.

---

## E. Perlakuan Preferensial (Preferential Treatment)

### E.1 Definisi (STM2 Exhibit 10-1, hal. 10-1; TSTM §9.1–9.2)
- **Preemption** (NTCIP 1202): transfer kendali normal ke mode khusus untuk rel, kendaraan darurat, dsb. — memutus koordinasi. MUTCD (TSTM hal. 9-2): saat masuk preemption, kuning & all-red **tidak boleh** dipotong; walk/ped clearance **boleh** dipotong/dihilangkan; kembali ke hijau dari kuning tanpa red clearance diizinkan. Saat keluar: kuning/all-red pendekat yang di-preempt tidak boleh dipotong; kuning→hijau dilarang. Pemulihan sistem terkoordinasi DC: 30 s – 7 menit (TSTM hal. 9-2).
- **Priority** (NTCIP 1211): perlakuan satu kelas kendaraan atas lainnya "without causing the traffic signal controller to drop from coordinated operations". Komponen NTCIP 1211: detection → **Priority Request Generator (PRG)** → **Priority Request Server (PRS)** → AVL/TMC logging (TSTM hal. 9-5 – 9-6).

### E.2 Proses 5 langkah (STM2 §10.2, hal. 10-2 – 10-3)
1. **Upstream detection** — permintaan segera (firmware lama) atau *time of service desired* (TSD) & *time of estimated departure* (TED) (NTCIP 1211); deteksi terlalu jauh buruk karena variabilitas kedatangan.
2. **Transition selection** — pilih strategi (green extension, red truncation…) sesuai status kontroler & permintaan berprioritas lebih tinggi.
3. **Timing transition** — terminasi aman fase konflik, transfer hak jalan.
4. **Dwell** — tahan sampai check-out (detektor hilir) atau timeout; *limited service* (layani fase non-konflik) disukai.
5. **Recovery** — fase pemulihan; 1–5 siklus untuk kembali ke koordinasi.

### E.3 Teknologi deteksi (STM2 Exhibit 10-4, hal. 10-4 – 10-5)
GPS berbasis kendaraan (tanpa line-of-sight, notifikasi clear, jangkauan lebih jauh; sulit di urban canyon), loop hard-wired, **infrared/optical** (paling luas; butuh line-of-sight; terganggu cuaca/pohon), radio/RF tag, sound (siren; kurang presisi), push button (pemadam), track circuits (rel; advance/simultaneous/gate-down).

### E.4 Strategi timing (STM2 §10.2.2, hal. 10-5 – 10-8)
- **Green/phase extension** (tetap atau sampai check-out, dengan maksimum) — paling kecil delay-nya; utamakan bila ada permintaan bersaing.
- **Red truncation/early green** — memperpendek fase non-prioritas sebatas min green & clearance ped.
- **Phase insertion** — fase khusus (mis. queue jump, Phase 9).
- **Sequence change** — lead ↔ lag.
- **Phase skipping** — lewati fase non-prioritas (mis. protected interval kiri).
Faktor: kapabilitas firmware, kebijakan, cycle, kompleksitas fase, arus silang, proteksi ped, min phase, akurasi check-out. Preemption sering → pertimbangkan operasi tak terkoordinasi.

### E.5 Strategi pemulihan (recovery/exit) (STM2 §10.2.3, hal. 10-9 – 10-10)
Return to normal; **return to free** (periode tertentu untuk membersihkan antrean); **return to coordinated** (lacak parameter koordinasi di latar → langsung sinkron tanpa transisi); return to alternate plan; **return to interrupted phase(s)** (priority return); return to defined phase(s); **queue delay recovery** (dinamis ke pergerakan dengan delay/volume tertinggi berbasis deteksi).

### E.6 Setelan kontroler
**Preemption** (STM2 §10.4.1, hal. 10-12 – 10-14): preemption phase(s); limited service (dwell) phases; recovery (exit) phases; preemption number (≥6 plan: 2 rel + 4 EV); **preemption priority** (rel > EV; sama prioritas → FCFS); duration (min/max/hold while active); min green & walk saat preemption (min green ≥2 s); FDW (MUTCD boleh dipotong); **preemption delay** (biasanya 0; untuk mencegah false preempt); **preemption memory** (aktif; risiko phantom preempt bila detektor rusak).
**Priority** (§10.4.2, hal. 10-14): priority phasing sequence (hindari yellow trap), minimum phase duration & fase yang tak boleh dipotong, durasi extension, min green fase non-prioritas, interval ped tak boleh dipotong.
**Scheduling multi-request** (§10.3, hal. 10-10 – 10-12): level prioritas per pengguna (bus > truk); permintaan tertinggi dilayani pada waktu terjadwalnya; butuh **TSD** per kendaraan; preemption tak dijadwalkan tetapi transisi ke preemption bisa lebih efisien.
**Logging** (§10.2.4, hal. 10-10): kapan, di mana, bagaimana, siapa meminta — untuk manajemen hak prioritas.

### E.7 Rail preemption (STM2 §10.5, hal. 10-14 – 10-23)
- Wajib bila crossing aktif ≤200 ft dari simpang (MUTCD); >200 ft perlu analisis antrean.
- **MWT = MT (≥20 s) + CT** (Eq. 10-1); CT = 1 s per 10 ft jarak bersih >35 ft; lapangan lebih panjang karena buffer time & equipment response time. Simultaneous preempt MWT umumnya ≤35 s.
- Masuk preemption: transfer ke **Track Clearance Green Interval (TCGI)**; **RTT** (right-of-way transfer time = min green aktif + ped (bila kebijakan) + Y + R; = 0 bila sedang di fase TCGI) + waktu bersihkan antrean < MWT.
- **Advance preemption** bila simultaneous tak cukup atau ped tak boleh dipotong; risiko **preempt trap** (TCGI berakhir sebelum gate turun; antrean baru terjebak) → mitigasi: *not-to-exceed timer* rel + TCGI ≥ advance time; **gate-down preempt** (dua preempt: advance menahan TCGI sampai konfirmasi gate-down, lalu TCGI terjadwal); schedule-based/**time-to-green (TTG)** untuk LRT Portland.
- Dwell: red flash; flashing yellow/red; steady red; **limited service (disukai)**; rest in green paralel rel. Setelan: TCGI, track clearance green time (worksheet TxDOT), exit phases (biasanya fase melintasi rel dulu).

### E.8 Kendaraan darurat (STM2 §10.6, hal. 10-23; TSTM §9.1)
Sering hanya truk pemadam yang di-preempt; ambulans/polisi lebih lincah; pertimbangkan **priority** alih-alih preemption untuk mengurangi gangguan; *preempt confirmatory lights* harus jelas; interoperabilitas multi-vendor.

### E.9 Transit Signal Priority (STM2 §10.7, hal. 10-23 – 10-25; TSTM §9.2, hal. 9-4 – 9-6)
Strategi paling umum: green extension & red truncation (extension lebih ringan). **Conditional TSP** berbasis: *schedule adherence/lateness* (AVL + CAD), *location* (in service, en route, bukan di halte; pintu tertutup sebagai syarat), *passenger counter* (ridership), *level of priority* antar rute yang tumpang tindih; contoh **decision tree** Portland (Exhibit 10-24). King County: bus hanya melapor kehadiran (AVI), sistem sinyal yang membuat permintaan — delay transit −40 %, variabilitas −35–40 %; Portland: bus memutuskan sendiri (optical, hanya bila terlambat), FIFO — travel time −10 %, variabilitas −19 %, hemat 1 bus (TSTM hal. 9-6).

### E.10 Truk (STM2 §10.8, hal. 10-25 – 10-27)
Dual upstream detector (panjang & kecepatan minimum) di luar decision zone truk (≤8 s); hanya *green extension* low-priority; tidak ada early green; koordinasi dipertahankan.

---

## F. Kondisi Khusus: Oversaturation, Special Events, Cuaca, Insiden

### F.1 Kerangka umum (STM2 §11, hal. 11-1)
Lima pertanyaan: kondisi apa yang mengubah permintaan/kapasitas; bagaimana pola berubah; **kriteria aktivasi**; strategi; **kriteria deaktivasi**.

### F.2 Cuaca (STM2 §11.1, hal. 11-2 – 11-6)
Dampak: kecepatan turun (arteri 6–20 %, freeway hingga 42 %, Exhibit 11-4), saturation flow turun (hujan −4,7 %; hujan seharian −8,5–12,3 %; salju −10–19 %; kabut −11,4 %; Exhibit 11-5), start-up lost time naik hanya pada kondisi ekstrem (2,0→2,5–3,0 s), kecepatan pejalan kaki justru naik; deteksi video terganggu es/kabut. Strategi: (1) tambah red clearance 1–2 s (pendekat turunan curam, riwayat tabrak sudut, simpang terpencil; dynamic red extension via detektor); (2) tambah min green pada tanjakan; (3) **phase recall** manual/otomatis bila deteksi rusak (efektif pretimed); (4) **weather-responsive coordination plans** (UDOT: desain untuk −30 % free-flow speed; kriteria: permintaan supervisor, event >20 menit, penurunan kecepatan terdeteksi, koridor macet; per koridor; dipantau CCTV; ConnDOT: naikkan siklus & ubah offset). TSTM §9.6: Charlotte NC memakai siklus lebih panjang/plan puncak untuk menurunkan kecepatan (keselamatan).

### F.3 Insiden (STM2 §11.2, hal. 11-6 – 11-9; TSTM §9.5)
Alternate route lokal vs regional; **recovery plan** terdokumentasi (Exhibit 11-7: nomor plan, segmen, sinyal terdampak & pengelola, tujuan, asumsi, perubahan timing — mis. menetapkan belok kanan sebagai fase koordinasi, +15 s min green, kriteria implementasi & penghentian). Faktor aktivasi: durasi, tipe/keparahan, jumlah lajur tertutup, kondisi arus, TOD/DOW, kapasitas & pemantauan rute alternatif, kapabilitas kontroler. Deaktivasi: insiden dibersihkan; kapasitas parsial cukup; rute alternatif memburuk. Strategi: plan siklus lebih panjang; plan kustom; **contingency "flush" plan**; kendali manual. MoU lintas yurisdiksi. NCDOT *Alternative Timing Plans*: profil koridor (stakeholder, rute, laneage, jumlah sinyal, lokasi/scope/durasi insiden, komunikasi), cycle standar/non-standar, **triggers** (kecepatan rata-rata, konfirmasi insiden), protokol aktivasi (pemilik, akses, nomor plan 51–59), validasi off-peak; badai mengikuti proses sama.

### F.4 Planned special events (STM2 §11.3, hal. 11-9 – 11-12)
Definisi FHWA; dampak pada partisipan, non-attendee, transit; komponen rencana (akses & parkir, pejalan kaki, arus, kendali, info en-route, surveilans, TIM); **post-event debrief** dalam beberapa hari. Strategi timing sama dengan insiden + kapasitas (larangan parkir, bahu, reversible/contraflow, pembatasan akses). Monitoring real-time: lacak kinerja, identifikasi lokasi buruk & penyebab/kontingensi, info ke pengambil keputusan/publik, evaluasi pasca. ≥1 teknisi sinyal di tim manajemen event.

### F.5 Oversaturation (STM2 §12, hal. 12-1 – 12-21; TSTM §8.3 hal. 8-5 – 8-6; NCDOT *Establishing Operational Objectives* hal. 8-9)
- **Tiga periode kinerja**: loading, oversaturated, recovery — strategi berbeda per periode (Exhibit 12-1). Karakterisasi: jumlah simpang, arah, durasi, perubahan, frekuensi, penyebab, gejala.
- **Gejala** (Exhibit 12-2, hal. 12-2): overflow queue; approach spillback ("de facto red"; penyebab di simpang hilir); storage bay spillback; storage bay blocking; starvation; cross-intersection blocking.
- **Tujuan**: maksimalkan throughput (input vs output sistem; loading: maks input & output; oversaturated: pakai kapasitas fisik untuk maks input; recovery: bubarkan antrean) atau **manage queues** (biarkan antrean terbentuk di tempat paling tidak merugikan). Minimalkan delay tidak realistis (hal. 12-5).
- **Strategi** (Exhibit 12-9, hal. 12-6): simpang — split reallocation (dari fase v/c rendah; jaga v/c<1; pilih fase dengan storage hulu terbesar), cycle length increase (miskonsepsi siklus panjang; hijau >30 s menurunkan saturation flow; batas atas Lieberman-Chang-Prassas — mis. split ratio 0,5 & link 700 ft → maks 150 s; terapkan sebelum antrean terbentuk), satu kontroler untuk simpang <10 s (≈500 ft), green extension berbasis ambang okupansi (ramp), phase re-service (kiri lead & lag; alternating minor tiap siklus = double cycling dengan overlap), **phase truncation** (akhiri hijau saat arus di detektor minimal — NCHRP 3-66); arteri — lead-lag (kiri meluap → lead; through melewati bay → lag), **green flush** (preemption berurutan dari hilir ke hulu; batas 255 s; operator TMC Sacramento via CCTV; efektif bila minor ≤20 % volume), flushing via plan siklus panjang, **simultaneous offsets** ("store and forward"), **negative offsets** (hijau hilir lebih awal), offset anti-spillback, offset anti-starvation, kombinasi (Exhibit 12-22: queue ratio 0,5 pada link 800 ft → offset relatif −30 s s.d. +10 s); jaringan — **metering/gating** (tahan di link eksterior dengan storage; lepas saat recovery; via TOD, logika, atau operator TMC).
- TSTM langkah retiming jenuh: evaluasi kualitatif → offset hilir untuk lepas belok kiri → phasing anti-spillback → ped phasing → split → cycle → tindakan lain (driveway, parkir, halte far-side).
- NCDOT: undersaturated v/c<0,85; oversaturated v/c>1,0; catat skala dampak & faktor penyebab (event, crash, cuaca, work zone, konflik moda, operasi sinyal, geometri, permintaan).

---

## G. Ukuran Kinerja, Monitoring, Evaluasi

### G.1 Ukuran kinerja yang direkomendasikan (STM2 §3.4.2, hal. 3-21 – 3-28; Exhibit 3-17)

| Ukuran | Level | Parameter yang memengaruhi | Metode |
|---|---|---|---|
| **Percent arrival on green (AOG)** | simpang & sistem | cycle, offset, sequence | deteksi akurat + logging kontroler; probe GPS |
| Rasio arrival on green : arrival on red | sistem | idem | probe, Bluetooth/re-identifikasi |
| **Stops per mile** | sistem | cycle, split, offset, sequence | estimasi model, probe |
| **Travel time / average speed** | sistem | idem | probe, permanent travel-time collectors |
| **Delay** (unit s/veh; total veh-hr) | simpang & sistem | cycle, split, offset | queue detection + status sinyal; **phase termination logging** |
| **Phase/split failures** | simpang & sistem | cycle, split | gap-out vs max-out/force-off logging (Exhibit 3-18/3-19) |
| Queuing | simpang & sistem | cycle, split | observasi/otomasi (video, radar) |
| Safety-related: crash, conflict points, ped/bike conflicts, **max-out/force-off frequency**, **red-light violations** | simpang | detection, clearance, cycle, offset, sequence | kamera, logging |
| Composite index (mis. OCTA CSPI: speed, green/red, stops/mile) | sistem | cycle, split, offset | kombinasi |

Prinsip: "Users perceive stops first and their delay second" (hal. 3-21); pilih ukuran sesuai tujuan, bukan karena mudah diukur; tujuan non-kendaraan bisa kualitatif (Exhibit 3-25). TSTM §2.3: delay/person, travel time, antrean persentil 50/95, emisi; NTOC Report Card 5 area (program management, monitoring & data, retiming ≤3 tahun, maintenance, hardware ≤10 tahun). TSTM §3.5: stops penting untuk emisi & persepsi; bandwidth efficiency/attainability; PI.

### G.2 Monitoring sistem (STM2 §8.3.2, hal. 8-9 – 8-17)
- Empat aktivitas: **operational monitoring** (low-tech: kunjungan terjadwal, rute komuter staf, permintaan publik, pantau pertumbuhan & pola tabrakan; high-tech: aplikasi mobile intended-vs-actual, **log performance measure kontroler/sistem**, permanent travel-time collectors — Exhibit 8-13), **equipment monitoring**, tinjau perubahan kebijakan/standar, respons permintaan publik.
- **High-resolution event data** (0,1 s: detektor on/off, fase G/Y/R) — dipakai Indiana, Utah, Minnesota; **Purdue Coordination Diagram (PCD)**: titik kedatangan (setback) vs waktu-dalam-siklus per waktu hari, garis awal/akhir hijau; contoh perbaikan offset AOG 53,2 % → 86,6 % (Exhibit 8-14/8-15, hal. 8-11 – 8-12). *ATSPM* sebagai istilah tidak muncul di ketiga dokumen (**tidak ada**), tetapi konsep dan metriknya (PCD, split failure, AOG) diuraikan di STM2 §8.3.2.1 dan NCDOT *Continuous Data Options*.
- **Equipment monitoring** (Exhibit 8-16, hal. 8-13): detector fail (fail-on → max recall; fail-off → tak terlayani)/ped button fail; count irregularity (vs profil); controller status alarms (online/offline, failure mode); parameter inconsistency (vs database); timing irregularity; clock synchronization; **transition frequency**; flash/conflict frequency; power source; communication quality (poll sukses/gagal/bad; % connected); response time; repair frequency. Database aset & catatan kegagalan wajib.
- **Public service requests** (§8.3.2.4, Exhibit 8-17, hal. 8-14 – 8-18): prosedur 7 langkah (identitas, lokasi, waktu, berulang?, deskripsi, jaminan waktu investigasi, masukkan ke database), respons ≤1 minggu, situs web regional; diagnosis sebelum membuka kabinet; matriks keluhan → pertanyaan diagnostik (tidak dapat hijau, hijau pendek, delay kiri, berhenti berurutan, dilayani tanpa permintaan, red-light running, walk pendek, preemption, night flash).
- Pembaruan pemeliharaan (§8.3.3): investigasi via remote monitoring dulu; undersaturated: kualitatif → split → offset → jam plan → cycle; oversaturated: split dulu, cycle kedua; "congestion is the result of poor signal timing parameters, especially excessively long cycle lengths or bad offsets" (hal. 8-19).

### G.3 Evaluasi before-after (STM2 §8.3.1, hal. 8-7 – 8-9; NCDOT *Travel Time Runs*, *Cost Benefit Analysis*)
Data "before" harus dikumpulkan sebelum implementasi; simpan rencana lama. NCDOT protokol: Tru-Traffic + GPS, ≥6 run/arah/periode, floating car, hindari Senin/Jumat/cuaca buruk/event, sinkron ke awal merah fase koordinasi; laporan CTT, CD, CStopD, CAS, CStops, LOS. Target NCDOT: −40 % travel time (koridor baru), −20 % (retimed) — dengan kritik keterbatasan (tak cocok untuk event/insiden/ramp; sulit saat jenuh; sampel kecil; mudah dimanipulasi; tak memperhitungkan volume) (*Performance Goals*). **Manfaat tahunan**: Delay = Σ volume puncak × Δdelay (s/veh)/3600 × $15,91/jam × 250 hari; Stops = Σ volume × Δstops × $0,014 × 250 (contoh $266.293 + $14.544) (*Cost Benefit Analysis*, hal. 4-5). Emisi/BBM via SimTraffic.

### G.4 Sumber data kontinu (NCDOT *Data Needs*, *Continuous Data Options*)
Matriks: traffic counts (1 hari, snapshot), travel time runs (padat karya), controller/system detectors & **split monitor** (gap-out/max-out; 15 menit agregat), Bluetooth (~328 ft jangkauan), **HRCD** (arrival on green, gap-outs, cycle failures, volume & occupancy; "perlu mengubah ukuran kinerja ke arrival on green"), probe pihak ketiga (akurasi diterima NCDOT 2017), Wi-Fi (lebih banyak deteksi), DSRC (ID acak 5 menit).

---

## H. Rekayasa Sistem dan Tata Kelola Program

### H.1 Systems Engineering (STM2 §9.1, hal. 9-1 – 9-3)
Lima dokumen: **Concept of Operations** (non-teknis; kebutuhan & cara pakai; milik stakeholder — owner, operator, maintainer, user), **System Requirements** (fungsional, kinerja, non-fungsional, enabling, constraints, interface, data — Exhibit 9-1 dari FHWA-HOP-11-027), **Design & Implementation** (alternatif, evaluasi produk, antarmuka & standar, spesifikasi), **Verification Plan** (uji terhadap requirements; tanggung jawab vendor, diawasi agensi), **Validation Plan** (MOE, data, analisis vs kebutuhan ConOps; milik agensi). "The practitioner should tailor the level of application to the size and/or complexity of the project." Berlaku juga untuk evaluasi opsi preferential treatment (sidebar 9-1). TSTM hal. 8-11 menyarankan pendekatan SE saat pengadaan peralatan.

### H.2 Program signal timing (STM2 §2; TSTM §2; NCDOT)
- NTOC Report Card: retiming ≤3 tahun; kontroler ≤10 tahun; biaya retiming $2.500–3.100/sinyal; B/C 40:1 nasional (TSTM hal. 2-11 – 2-12). NCDOT: B/C konsisten 40:1; siklus 3 tahun (80 % koridor "typical"), 18 bulan kritis, 5–6 tahun non-kritis; seleksi koridor menuju ROI (*Corridor Selection*).
- NCDOT hierarki **Operational Objective → Strategy → Tactic** (Tabel 1-3): 13 tujuan (efisiensi free run, regulasi kecepatan/traffic calming, minimalkan cycle failure, travel time/delay, throughput, progresi, safety, keluhan, kemacetan, lingkungan, event terencana, insiden, queue management); 24 strategi (meter traffic entering storage areas, manage queues, traffic responsive, ICM, flush plan, left-turn progression, side-street progression, reduce emissions/fuel, reduce stops, increase AOG, balance queues, mainline/bi-directional/transit/ped/bike progression, maximize mainline capacity, reduce vehicle/transit/ped/bike delay, reduce max-outs, reduce cycle & split failures, reduce cut-through, fine-tune parameters); taktik (optimize/long/short/half-double/alternate (1,5×)/**resonant** cycle, lead-lead/lag-lag/lead-lag, phase reservice, optimize offsets, max green ≈ (V_fase/ΣV_kritis)×C×1,25–1,5, gap time, walk time 4/7/10/15 s, minimalkan jumlah & durasi transisi, permissive mode auto/open/manual).
- Konteks koridor (NCDOT *Context of a Corridor*): grid vs arteri, lajur, satu/dua arah, parkir, jarak simpang, tata guna lahan, wilayah, prioritas interstate & rel di atas koridor, derajat kejenuhan, directionality, ped/bike, transit, masukan Division, keluhan.
- Proses proyek retiming (NCDOT SOW FY2017, 10 tugas): estimasi biaya → kick-off → data lapangan (TMC 13 jam, verifikasi geometri/phasing/jarak/speed/peralatan vs Plan of Record) → evaluasi eksisting (database TransLink32, "before runs") → pengembangan plan (Synchro, TOD schedule, master graphics 1280×768, detektor sistem logging) → preliminary submittal (format 9 bagian; review 3 minggu) → implementasi & fine-tuning (master & lokal) → "after runs" → laporan akhir (rekomendasi diklasifikasi high/medium/low) → pertemuan; garansi 1 bulan.
- Field protocol: hubungi Division sebelum ke lapangan; catat di log book kabinet; jangan upload timing di luar jam teknisi (NCDOT *Field Visit Protocol*).

### H.3 Staffing & pelatihan (STM2 §8.4, hal. 8-20 – 8-22; TSTM §8.4, hal. 8-9 – 8-12)
Posisi: Traffic Signal Engineer, Signal Technician/Analyst, ITS Engineer, Maintenance Technician, Electronic/Communications Specialist (CCTV, fiber, telekom, TMC, kontroler; skill Ethernet/database/IT), **TMC Operator**, Public Relations Coordinator. Rule of thumb ITE: 20–25 jam/simpang retiming; 1 engineer per 75–100 sinyal; 1 teknisi per 40–50 (NCHRP Syn. 245: 38–43); TMC 24/7: 1 manajer, 2 supervisor, 5 operator; Tabel 8-2 TSTM per ukuran sistem (mis. 501–1.000 sinyal: 5–10 engineer, 17–33 analis/teknisi). FHWA-HOP-09-006 menyarankan kriteria berbasis kinerja. Pelatihan: vendor, kontraktor, perpustakaan dokumentasi, retensi staf; sesi terbuka untuk publik. ASCT butuh staf berpengalaman/konsultan/vendor (STM2 9-16).

### H.4 Peran kelembagaan (NCDOT *Roles and Responsibilities*)
Division = pemilik/operator/pemelihara harian & kontak publik; COST = inventaris sistem & rencana koordinasi, pengembangan, prioritisasi, notifikasi 24–48 jam sebelum ke lapangan, dokumentasi field diary, tujuan lintas yurisdiksi, minimalkan penyesuaian lapangan tak terdokumentasi; PEF = tenaga tambahan. Pengembang properti didorong mendanai retiming seluruh koridor (*Impacts on a Corridor*).

---

## I. Implikasi untuk Desain Aplikasi ITCS

Bagian ini menerjemahkan isi manual menjadi kebutuhan konkret perangkat lunak ITCS (Dishub DKI-like: APILL adaptif real-time, green wave, prioritas bus/darurat, monitoring TMC, KPI). Rujukan dalam kurung.

### I.1 Entitas data (data model)

| Entitas | Atribut kunci | Sumber |
|---|---|---|
| **Intersection** | id, nama, koordinat, yurisdiksi/pengelola, tipe lingkungan (rural/suburban/urban/CBD), klasifikasi jalan, lebar simpang W per pendekat, skew, grade, tipe kabinet & kontroler (NEMA TS-1/TS-2, 170/2070, ATC), status komunikasi, jarak ke simpang tetangga, rel ≤200 ft? | STM2 §3.2–3.3, Exhibit 3-11 (3-11); §4.2 (4-9 – 4-13); §10.5 (10-14) |
| **Approach / Lane / Movement** | pendekat, lajur (jumlah, lebar, assignment, panjang turn bay), movement number HCM (1–18), permitted/protected, kecepatan (posted, v85), grade, halte/parkir/driveway | STM2 §3.3.4 (3-16 – 3-17), §5.1.1 (5-1) |
| **Phase** (per intersection) | nomor NEMA 1–8(+), ring, barrier group, tipe (through/left/ped/overlap), movements yang dilayani, parameter dasar: min green, max green 1/2/3, yellow, red clearance, passage time, min gap, time before reduction, time to reduce, added initial, max initial, walk, FDW, dual entry, recall mode, memory mode, ped protect | STM2 Exhibit 8-2 (8-2 – 8-3), §6.1 (6-3 – 6-22); TSTM §5.3–5.6 |
| **Overlap** | huruf/nomor, parent phases, modifier phases, trailing time, load switch | STM2 §5.1.4 (5-11 – 5-16) |
| **Detector** | id/channel, tipe teknologi, mode pulse/presence, lokasi (stop bar/setback/mid-block/upstream/turn-bay entrance/system), jarak ke stop bar, panjang zona, lajur, fungsi (call/extend/count/queue/system), phase assignment, extend phase & switch phase, delay, extend, locking, status kesehatan, profil hitung harapan | STM2 §4.1 (4-2 – 4-9), §5.1.5, §6.2; §9.4.2.3 (9-14) |
| **Timing Plan / Pattern** (NTCIP) | id, cycle length, offset, offset reference point, coordinated phases, sequence (lead/lag per fase), split per fase (s/%), force-off mode fixed/floating, permissive mode, walk mode, actuated coordinated time, transition mode, inhibit max, phase omit/recall per TOD, max 2 | STM2 §7.3–7.5 (7-11 – 7-35); TSTM §5.7 (5-29) |
| **TOD/DOW Schedule** | hari/tanggal/musim/hari libur → pattern; jam mulai plan puncak "lebih awal"; free-run window malam | STM2 §6.3 (6-27), §3.3.2.1 (3-13); NCDOT SOW |
| **Coordination Group / Subsystem** | daftar simpang, master clock/sync reference, common cycle, arah koordinasi, cross-coordination flag, suitability factor (ASCT) | STM2 §7.2.2, §9.4.2.1 (9-12) |
| **Alternative Plan** (incident/event/weather/evacuation/flush) | nomor (mis. 51–59), segmen terdampak, sinyal & pengelola, tujuan, asumsi, perubahan timing, **kriteria implementasi & penghentian**, pemilik/akses aktivasi, hasil validasi | STM2 Exhibit 11-7 (11-7); NCDOT *Alternative Timing Plans* |
| **Preemption Plan** | preempt number, priority level, input/detector, preemption phases, dwell/limited service phases, exit phases, min/max duration, delay, memory, min green/walk/FDW saat preempt; rel: MWT, RTT, TCGI, track clearance time, advance/simultaneous/gate-down inputs | STM2 §10.4.1, §10.5.5 (10-12 – 10-23) |
| **Priority Request** (NTCIP 1211) | vehicle id, class (bus/EV/truk), route, level of priority, TSD, TED, lokasi/AVL, schedule deviation, door status, ridership, status (received/scheduled/served/denied), strategi yang dipakai, waktu layanan, recovery | STM2 §10.2–10.3, §10.7 (10-2 – 10-25); TSTM §9.2 |
| **High-resolution Event Log** | timestamp 0,1 s, event type (detector on/off, phase G/Y/R, walk/FDW, preempt/priority, transition, plan change, alarm), intersection, phase/detector | STM2 §8.3.2.1 (8-10) |
| **Performance Record** (agregat 15 menit/plan/hari) | AOG %, AOR, stops/mile, travel time, delay, split/phase failures (gap-out vs max-out/force-off), queue, red-light violations, transitions count/duration, cycle length aktual | STM2 Exhibit 3-17, Exhibit 8-16 |
| **Equipment Health** | detector fail on/off/chatter, count irregularity, controller online/offline & failure mode, alarm count, parameter mismatch vs DB, clock drift, flash/conflict events, power source, comm poll stats, MTTR, repair frequency | STM2 Exhibit 8-16 (8-13) |
| **Service Request** | pelapor, kontak, lokasi, TOD, berulang?, deskripsi, kategori (Exhibit 8-17), SLA (≤1 minggu), hasil investigasi, respons | STM2 §8.3.2.4 (8-14 – 8-15) |
| **Count/Volume Profile** | 24-jam mingguan per lokasi mid-block, TMC per periode, PHF, % truk, ped/bike, transit, antrean awal/akhir periode | STM2 §3.3.2 (3-12 – 3-15) |
| **Retiming Project / Before-After Study** | tujuan operasional, MOE, data before/after, cost-benefit, rekomendasi (high/med/low), riwayat retiming | STM2 §8.3.1; NCDOT SOW & CBA |

### I.2 Parameter konfigurasi kontroler yang harus didukung (dengan nilai default/rentang dari manual)
- Yellow 3–6 s (rumus ITE; +0,1 s/1 % turunan); red clearance 0–6 s ((W+Lv)/v, −1 s NCHRP 731) (STM2 6-3 – 6-5).
- Min green 2–15 s per tipe fase/fasilitas; Gq = 3 + 2n; variable initial 1,2–2,0 s/aktuasi (STM2 6-5 – 6-7; TSTM 5-25).
- Max green 15–70 s; Max 2/3 per TOD; Inhibit Max saat koordinasi (STM2 6-9, 7-26).
- Passage time 0–3 s tergantung panjang zona & kecepatan; PT = MAH − (Lv+Ld)/(1,47·va); MAH 3,0/4,0 s; min gap dari MAH 2,0 s; time before reduction ≥10 s; time to reduce ≈ ½(max−min) (STM2 6-13 – 6-14; TSTM 5-20 – 5-23).
- Walk 4/7/10–15 s; FDW = Dc/3,5 − (Y+R); LPI ≥3 s; steady DW ≥3 s (STM2 6-17 – 6-20).
- Detector delay 2–5 s / 8–12 s; extend ≤2 s; switching (STM2 6-25 – 6-27).
- Koordinasi: cycle 60–120(150) s; split Σ ≤ C; force-off fixed/floating; permissive simultaneous/sequential; offset reference (default: awal kuning fase koordinasi pertama); sync reference (03:00 disarankan); transition mode default *shortway*, *add-only* bila ada preemption; min dwell dalam pattern 30 menit (STM2 7-11 – 7-35).
- Preemption: ≥6 preempt; priority rel > EV; min green saat preempt ≥2 s; delay 0; memory on; TCGI; MWT = 20 + CT (STM2 10-12 – 10-16).
- Priority: level per kelas, min phase duration, max extension, no ped truncation (STM2 10-14).
- ASCT: batas pencarian per langkah (split ±5 s, cycle +10–20 s), batas min/max cycle/offset, parameter terkunci (sequence/skip), adaptive on/off schedule, failure mode (koordinasi/free), backup plans (STM2 9-13 – 9-16).

### I.3 Algoritma dan aturan yang harus diimplementasikan
1. **Mesin fase dual-ring dengan barrier** (aturan kompatibilitas, skip, pemberian sisa waktu, dual entry, simultaneous gap) — STM2 §5.1.2, §6.1.5, §6.1.7; TSTM §5.4.3.
2. **Logika aktuasi**: min green → passage timer (reset per aktuasi) → gap-out hanya bila 3 syarat → max-out saat ada conflicting call; gap reduction linier; variable initial; recall & memory modes; detector delay/extend/switch/queue/call — STM2 §6.1–6.2; TSTM §5.4–5.6.
3. **Kalkulator clearance & ped** (ITE yellow, red clearance, PCT, FDW, bicycle min phase) sebagai validator input (tolak nilai di bawah rumus/MUTCD) — STM2 §6.1.1–6.1.6.
4. **Critical movement analysis / QEM & Webster** untuk estimasi cycle & split awal, plus v/c per movement dan LOS HCM — STM2 §5.2; TSTM §3.3, Eq. 6-1, 6-2.
5. **Koordinator**: master clock (sync reference + DST), local zero via offset reference, yield point & permissive, force-off fixed/floating, inhibit max, walk modes, actuated coordinated phase, ped re-service, early-return handling — STM2 §7.3–7.6; TSTM §6.3.
6. **Transition engine**: dwell/max dwell/add/subtract/shortway dengan batas per siklus (≈20 %), selesai ≤3–5 siklus; log frekuensi & durasi transisi — STM2 §7.5.3; TSTM §6.5.2.
7. **Time-space diagram & bandwidth** (efficiency, attainability), progression speed, alternate/quarter-cycle offset generator, negative/simultaneous offset untuk jenuh — STM2 §7.2, §12.3.2.3; TSTM §3.5.1, §6.6.2.
8. **TRPS**: V+K·O, weights, smoothing 50 %, target/threshold dengan hysteresis, min dwell 30 menit, group-wide switch — STM2 §9.3; TSTM §9.3.
9. **ASCT loop**: collect → model/predict → evaluate alternatives (metrik terpilih: delay, stops, AOG, throughput, degree of saturation ≤90 % SCOOT) → implement (download parameter vs hold/force-off) → repeat; rolling horizon 60 s/5 s; adaptive groups; constraint set; fallback — STM2 §9.4.2; TSTM §9.4 (SCOOT/SCATS/RHODES/OPAC/ACS-Lite).
10. **Preferential treatment engine**: request server (PRS) dengan TSD/TED, level prioritas & scheduling; strategi green extension/red truncation/insertion/sequence change/skipping; dwell limited service; recovery strategies (incl. queue delay recovery, return to coordinated tanpa transisi); conditional TSP decision tree (lateness, in-service, ridership, route level); rail preemption state machine (advance→TCGI hold→gate-down→timed TCGI→dwell→exit); MUTCD constraints (tidak memotong Y/R) — STM2 §10; TSTM §9.1–9.2.
11. **Oversaturation toolkit**: deteksi gejala dari okupansi/antrean (overflow, spillback, starvation), split reallocation, cycle bound (Lieberman), phase truncation, re-service, green flush sequencer hilir→hulu (≤255 s), gating/metering, periode loading/oversaturated/recovery — STM2 §12.
12. **Special-condition plan manager**: trigger berbasis kecepatan/okupansi/konfirmasi insiden/cuaca, aktivasi per koridor, kriteria deaktivasi, MoU lintas yurisdiksi, debrief — STM2 §11; NCDOT *Alternative Timing Plans*.
13. **Health monitor & alarm rules**: detektor fail-on/off/chatter (bandingkan dengan profil), clock drift, comm poll stats, parameter-vs-DB mismatch, transition excess, flash/conflict — STM2 Exhibit 8-16.
14. **Data quality rules**: volume ≠ demand saat antrean; hitung demand dari upstream undersaturated atau queue observation; validasi sumber detektor sebelum dipakai — STM2 §3.3.2 (3-12 – 3-13).

### I.4 KPI yang harus dihitung (mengacu STM2 Exhibit 3-17, §8.3; TSTM §3.4–3.5; NCDOT)
- Per pendekat/fase: **% arrival on green**, arrival profile/PCD, **split failure rate** (max-out/force-off vs gap-out), phase failures, queue length (rata-rata/95 %), control delay estimate & LOS, red-light running count, max-out frequency (safety proxy), ped actuation ratio.
- Per koridor: travel time & average speed (probe/Bluetooth/HRCD), stops per mile, AOG:AOR ratio, bandwidth efficiency/attainability, arterial LOS, composite index (CSPI), throughput input/output (jenuh), emisi/BBM (model).
- Sistem/program: jumlah & durasi transisi, % waktu dalam koordinasi, preemption/priority counts & durasi pemulihan, TSP delay/reliability transit (mis. −40 % delay, −35–40 % variabilitas), kesehatan perangkat (detector uptime, comm availability, clock sync), SLA respons pengaduan (≤7 hari), retiming age (≤3 tahun), B/C & manfaat tahunan (formula NCDOT).

### I.5 Antarmuka operator (TMC) yang dibutuhkan
- Editor ring-barrier & timing sheet dengan validasi rumus; time-space diagram interaktif (band, offset drag, sequence) — STM2 §5.1, §7.2.
- Manajer pattern/TOD/DOW, alternate & incident plans dengan tombol aktivasi manual, tampilan kriteria masuk/keluar, log siapa-kapan — STM2 §7.5.3, §11; NCDOT.
- Dashboard kesehatan perangkat & alarm (Exhibit 8-16); status koordinasi/transition per simpang (Exhibit 7-29 cycle length plot).
- Dashboard kinerja: PCD, split monitor (gap/max/force), AOG per plan, travel time, before-after comparison (Exhibit 8-10 – 8-15).
- Konsol preferential treatment: permintaan aktif (TSD/TED), level prioritas, log layanan, konfigurasi decision tree TSP; monitor preempt rel (MWT/TCGI) — STM2 §10.
- Modul pengaduan publik (form 7 langkah, database, respons) — STM2 §8.3.2.4.
- Modul ASCT: parameter constraint, on/off schedule, tinjauan keputusan untuk rekalibrasi, backup plan, failure mode — STM2 §9.4.4.
- Peran & audit: Division/COST-like ownership, catatan lapangan (field diary), notifikasi sebelum kunjungan, larangan upload di luar jam teknisi — NCDOT.
- Master graphics simpang (minimal 1280×768, label simpang & detektor) — NCDOT SOW Task 5.

---

## J. Kutipan Kunci (verbatim, singkat)

1. "Adaptive systems should only be considered after the capabilities of traditional systems have been fully considered." — STM2 §3.1.2.2, hal. 3-5.
2. "It cannot be overemphasized that traffic counts are, at best, a snapshot in time, and need to be applied with judgment and understanding of the effects on signal operations." — STM2 §3.3.2, hal. 3-12.
3. "Users perceive stops first and their delay second. Minimizing stops on arterials has the most impact on reducing user complaints..." — STM2 §3.4.2, hal. 3-21.
4. "A phase failure (also called a 'split failure' when the intersection is coordinated) is defined as the occurrence of one or more stopped vehicles that cannot proceed through a signalized intersection on a green indication." — STM2 §3.4.2.6, hal. 3-24.
5. "The normal failure mode of a detector is to place a continuous call for service, so a failed detector on a phase will cause that phase's maximum green to time every cycle." — STM2 §6.1.4, hal. 6-8.
6. "The current phase will only gap out ... if all of the following conditions are met: 1. The minimum green timer has expired. 2. A call is waiting for service on a conflicting phase. 3. The passage timer has expired." — STM2 §6.1.5, hal. 6-10.
7. "The NTCIP term 'pattern' refers to a unique set of coordination parameters—cycle, split, offset, and sequence." — STM2 §7.3, hal. 7-11.
8. "It is generally recommended to remain in a coordinated pattern for at least 30 minutes. It is also best to avoid changing patterns during congested conditions... A peak-period pattern is best implemented early to ensure all offset transitioning is completed before the onset of peak traffic flows." — STM2 §7.5.3, hal. 7-33.
9. "'High-resolution' event data are an emerging source of data. Rather than storing the average values of data, individual time-stamped traffic events ... are logged in the controller, or in an external data collector, at a resolution of 0.1 seconds or faster." — STM2 §8.3.2.1.1, hal. 8-10.
10. "It is important to understand that ASCT systems are not 'set-and-forget' systems. They require ongoing fine-tuning and higher levels of maintenance than traditional systems..." — STM2 §9.4, hal. 9-11.
11. "For example, a rolling-horizon system might evaluate hundreds of different options for the duration and sequence of each phase over the next 60 seconds and then implement only the decision trajectory for the next 5 seconds. The process then repeats." — STM2 §9.4.2.2, hal. 9-13.
12. "Per NTCIP 1211, priority is the preferential treatment of one vehicle class ... over another vehicle class at a signalized intersection without causing the traffic signal controller to drop from coordinated operations." — STM2 Exhibit 10-1, hal. 10-1.
13. "Green extension facilitates significantly less intersection delay than red truncation, and it should be given priority when competing calls exist." — STM2 §10.7, hal. 10-23.
14. "Adaptive control systems should not be expected to eliminate oversaturation. Rather, these systems are one tool in a box of many other conventional strategies..." — STM2 §12.3.4 sidebar, hal. 12-21.
15. "...research and practical experience have shown that when green intervals are longer than 30 seconds, saturation flow rates and overall intersection efficiency decline." — STM2 §12.3.1.2, hal. 12-7.
16. "Movements or lane groups with volume-to-capacity ratios less than 0.85 are considered undersaturated and typically have sufficient capacity and stable operations." — TSTM §3.3.5, hal. 3-8.
17. "SCOOT controls the exact green time of every phase on a traffic controller by sending 'hold' and 'force-off' commands to the controller." — TSTM §9.4, hal. 9-12.
18. "TRPS merely selects a timing plan to operate, but does not make changes to the timings specified in the timing plan. That is the role of adaptive traffic signal control." — TSTM §9.3, hal. 9-8.
19. "The 2007 NTOC National Traffic Signal Report Card ... 'to keep pace with changing travel patterns, traffic signal timing should be actively monitored, reviewed, and updated at least every three years...'" — TSTM §2.3.1, hal. 2-12.
20. "Studies have shown that improving traffic signal coordination plans is one of the most cost effective uses of transportation funds, with a consistent benefit-cost ratio of 40:1." — NCDOT *Introduction*.
21. "Transitions can introduce the most ineffective period of signal timing on a corridor." — NCDOT *Establishing Operational Objectives*, Tabel 3, hal. 7.
22. "Do not upload signal timing plans after hours when technicians are not available." — NCDOT *Field Visit Protocol*.

---

## K. Ringkasan 10 Temuan Terpenting untuk Proyek ITCS

1. **Model data inti** ITCS harus mengikuti struktur NEMA/NTCIP 1202: intersection → ring/barrier → phase (1–8+, overlap) → detector channel, dengan *pattern* = cycle + split + offset + sequence, dan TOD/DOW schedule (STM2 Bab 5–7; Exhibit 8-2 adalah daftar lengkap parameter yang wajib dimodelkan).
2. **Logika aktuasi lokal** (min green, passage/gap-out dengan 3 syarat, max-out, gap reduction, variable initial, recall, memory, dual entry, detector delay/extend/switch) adalah fondasi yang harus dimiliki bahkan oleh sistem adaptif — ASCT tipe *download* mengandalkan gap-out & force-off kontroler lokal (STM2 §6, §9.4.2.2).
3. **Rumus wajib**: ITE yellow `t + v/(2(a+Gg))`, red clearance `(W+Lv)/v` (−1 s), `Gq = 3+2n`, `PCT = Dc/3,5 ft/s`, `c = s·g/C`, `X = vC/(sg)`, Webster `C = (1,5L+5)/(1−Y)`, `PT = MAH − (Lv+Ld)/v`, bandwidth efficiency `(B_A+B_B)/2C` — semua tersedia eksplisit di TSTM 2008 (badan rumus STM2 tidak terekstraksi).
4. **Koordinasi/green wave** dikendalikan oleh master clock + offset reference point (disarankan awal kuning fase koordinasi pertama karena teramati), force-off fixed/floating, permissive, yield point; **early return to green** dan pejalan kaki adalah dua sumber utama penyimpangan dari band ideal.
5. **Transisi** (dwell/max dwell/add/subtract/shortway) adalah periode paling tidak efisien; sistem harus membatasi frekuensi pergantian (≥30 menit per pattern, ≤3–5 siklus penyelesaian, mulai plan puncak lebih awal) dan **mencatat frekuensi transisi sebagai KPI kesehatan**.
6. **Hierarki teknologi**: fitur koordinasi lanjut (actuated coordinated phase, dynamic phase length, re-service) → traffic responsive (V+K·O, hysteresis, 30 pattern) → ASCT; ASCT tidak menyelesaikan masalah kapasitas dan belum terbukti mengatasi oversaturation — aplikasi harus menyediakan *toolkit* jenuh (split reallocation, negative/simultaneous offsets, green flush, gating) di samping mode adaptif.
7. **Arsitektur ASCT** yang dirujuk memiliki dua pola integrasi (download parameter vs override hold/force-off), rolling horizon 60 s/5 s, adaptive groups, deteksi wajib pada semua fase (lane-by-lane ideal), komunikasi IP, parameter constraint, failure mode & backup plans — ini menjadi spesifikasi minimum modul adaptif ITCS. SCOOT/SCATS/RHODES/OPAC/ACS-Lite dijelaskan singkat; InSync tidak dibahas.
8. **Prioritas bus & preemption darurat** harus dibangun sebagai state machine NTCIP 1211 (PRG/PRS, TSD/TED, level prioritas, scheduling) dengan strategi green extension (utama), red truncation, insertion, sequence change, skipping; pemulihan terdefinisi (termasuk *return to coordinated* tanpa transisi dan *queue delay recovery*); TSP kondisional berbasis AVL/lateness/ridership; batasan MUTCD (Y/R tak boleh dipotong).
9. **Monitoring berbasis high-resolution data 0,1 s** (PCD, AOG, split failure gap/max/force) plus daftar 14 item *equipment monitoring* (Exhibit 8-16) dan matriks pengaduan publik (Exhibit 8-17) adalah cetak biru modul TMC/KPI; NCDOT menunjukkan transisi dari travel-time runs ke HRCD/probe/Bluetooth dan formula manfaat tahunan untuk B/C.
10. **Tata kelola**: Systems Engineering (ConOps → requirements → design → verification → validation) wajib untuk pengadaan sistem lanjut; retiming ≤3 tahun; 1 engineer/75–100 sinyal, 1 teknisi/40–50; peran TMC operator, PR coordinator, dan spesialis komunikasi/IT; dokumentasi lapangan (field diary), notifikasi sebelum kunjungan, dan larangan upload di luar jam teknisi — semua perlu didukung fitur audit & workflow dalam aplikasi.
