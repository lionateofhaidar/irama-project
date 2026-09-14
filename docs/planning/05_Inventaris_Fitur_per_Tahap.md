# 05 — Inventaris Fitur per Tahap (Backlog Pra-Perencanaan)

Status: revisi 2026-09-14 (keputusan user T-34 s.d. T-42). ID fitur `F-T#-##` dipertahankan agar rujukan lintas dokumen tidak putus; **kolom Tahap adalah tahap yang berlaku**, dan fitur yang pindah tahap ditandai "(dulu T#)". Fitur baru untuk dua modul inti T2 ada di epik E20 sampai E23 (ID 141 sampai 178). Prioritas MoSCoW relatif terhadap tahapnya. Kolom "Bukti" merujuk sumber: [R00]–[R07], [Majalah], regulasi (C-xx = kebutuhan kepatuhan KB-03 §B), dan keputusan user (T-xx di `docs/LOG_SESI.md`). Kolom singkat: **Dep** = dependensi, **Data** = data atau detektor, **Patuh** = kepatuhan, **Sukses** = ukuran sukses. Semua estimasi dan ambang adalah asumsi awal.

Ringkas perubahan 2026-09-14: kalkulator, registri simpang, dan dashboard dasar di T1; Vision Tracker, optimasi, konfigurasi, dashboard lengkap, laporan, validasi SUMO, dan manfaat rupiah di T2; pemantauan operasional, anomali, laporan wajib, controller baca-saja, dan uji lapangan di T3; kendali, edge, ANPR, prioritas, integrasi instansi, dan koordinasi dasar di T4; optimasi koridor dan jaringan penuh di T5.

## E01 — Inventaris & Aset APILL
| ID | Fitur | Deskripsi | Bukti/kebutuhan | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-01 | Registri simpang | Simpang, kaki, pendekat, lajur, geometri (L, LM, LK, LBKiJT), status jalan (nasional/provinsi/kota), koordinat | PKJI Form SA-I; C-01 | T1 | Must | — | survei | C-01 | 100% simpang pilot terdaftar |
| F-T1-02 | Registri aset APILL | Controller, luminer, tiang, detektor, DIS; serial, tahun, sertifikat, logo stiker; umur teknis ≤5 th | PM 49 Ps.19–25, 42; C-05, C-07 | **T3** (dulu T1) | Must | F-T1-01 | manual | C-05/07 | atribut wajib terisi |
| F-T1-03 | Jadwal pemeliharaan berkala ≤6 bulan + checklist | Reminder, checklist (optik, korosi, cat, penghalang), riwayat | PM 49 Ps.41; TSPH G.4 | **T3** (dulu T1) | Must | F-T1-02 | — | C-06 | alarm jatuh tempo |
| F-T1-04 | Pemeliharaan insidentil & penyesuaian siklus | Log penggantian komponen & re-timing aktual | PM 49 Ps.41(5) | **T3** (dulu T1) | Should | F-T1-03 | — | C-06 | log lengkap |
| F-T1-05 | Referensi SK/izin per aset | Simpan SK Gubernur/izin Kadis & tanggal pemasangan (kekuatan hukum +30 hari) | UU Ps.102; Perda Ps.74 | **T3** (dulu T2) | Should | F-T1-02 | — | C-02/03/04 | 100% aset bereferensi |
| F-T2-06 | Penilaian kinerja aset & usulan penghapusan | Skor kinerja per aset dari alarm/uptime | PM 49 Ps.42 | **T4** (dulu T2) | Could | F-T2-30 | health | C-07 | laporan tahunan |
| F-T2-07 | Master graphics simpang | Diagram simpang dengan label fase & detektor (≥1280×768) | NCDOT SOW [R01 I.5] | T2 | Should | F-T1-01 | — | — | tiap simpang punya diagram |
| F-T5-08 | Perencanaan kebutuhan 5 tahun | Proyeksi kebutuhan APILL/ATCS dari pertumbuhan & warrant | SK 7234/2013 [R00 H] | T5 | Could | F-T1-16 | historis | — | laporan rencana |

## E02 — Peta & Status Real-time
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-09 | Peta simpang & status warna | Peta (MapLibre) dengan status: mode kendali, plan aktif, alarm, komunikasi. Status controller mulai T3 (baca-saja); peta simpang dan LOS ada di E23. | PM 76 Ps.7(4)b | **T3** (dulu T1) | Must | F-T1-01 | status controller | — | latensi ≤5 s |
| F-T1-10 | Tampilan fase live per simpang | R/Y/G per kelompok sinyal dan posisi siklus dari nyala lampu kamera (F-T2-148) atau status controller baca-saja; alasan terminasi menyusul di T4 | NTCIP status [R03 A.4] | **T3** (dulu T1) | Must | F-T2-148 | status | — | akurat vs lapangan |
| F-T1-11 | Timeline plan aktual vs rencana | Cycle length plot & transisi | STM2 Exhibit 7-29 [R01 I.5] | **T3** (dulu T1) | Should | F-T1-10 | hi-res | — | — |
| F-T2-12 | Grup koridor & tampilan sinkron | Status koordinasi per koridor (≥3 simpang ≤1 km). Offset dasar T4; optimasi koridor penuh T5. | PM 96 II.F.e | **T4** (dulu T2) | Must | F-T1-09 | — | C-11 | — |
| F-T2-13 | Layer kejadian (insiden, galian, banjir, event) | Event kota sebagai layer & pemicu plan | STM2 §11; Beritajakarta [R06 D.1] | **T3** (dulu T2) | Should | F-T2-52 | manual/API | — | — |
| F-T3-14 | Layer probe kecepatan/waktu tempuh | Heat map kecepatan per ruas dari GPS | R04 A.19 | **T5** (dulu T3) | Should | F-T3-58 | probe | — | — |
| F-T4-15 | Video wall / mode TMC | Tata letak multi-layar, peta + CCTV + KPI | Majalah h.16 | T4 | Should | F-T2-95 | — | — | — |

## E03 — Plan Manager & Kalkulator
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-16 | Kalkulator PKJI 2023 / MKJI | Input geometri & arus → J, C, DJ, siklus Webster, hijau, Nq, PA, RKH, tundaan, LOS PM 96 | PKJI Bab 5 [R05 D]; Dirjen 273 [R00 G] | T1 | Must | F-T1-01 | survei | C-30 | lulus uji contoh resmi |
| F-T1-17 | Digitalisasi grafik PKJI (tipe O, F_G, Nq_MAX) | Tabel/fungsi interpolasi dari grafik | [R00 G] | T1 | Must | F-T1-16 | — | — | galat ≤2% |
| F-T1-18 | Editor plan TOD (≥8 plan) stage-based & ring-barrier | Fase/tahap, split, offset, sequence; dukung stage (Indonesia) & NEMA | PM 49 Ps.14; STM2 §5; [R00 I] | **T2** (dulu T1) | Must | F-T1-01 | — | C-09 | ≥8 plan/simpang |
| F-T1-19 | Validator keselamatan waktu | ITE yellow, red clearance, min green, walk/FDW, ≤130 s, hijau ≥10 s | STM2 §6.1; PKJI 5.3 | T1 | Must | F-T1-160 | — | keselamatan | tolak nilai di bawah rumus |
| F-T1-20 | Validator konsistensi Annex B | Concurrency, ring, sequence, preempt phases | NTCIP Annex B [R03 A.14] | **T4** (dulu T1) | Must | F-T1-18 | — | — | 0 fault saat download |
| F-T1-21 | Jadwal TOD/DOW/libur | Day plan & schedule, plan puncak mulai lebih awal | STM2 §6.3, 7.5.3 | **T2** (dulu T1) | Must | F-T1-18 | — | — | — |
| F-T2-22 | Time-space diagram & bandwidth | Diagram berskala, efisiensi/attainability, drag offset | TSTM §3.5, STM2 §7.2 | **T4** (dulu T2) | Should | F-T2-12 | — | — | — |
| F-T2-23 | Versi & riwayat plan + persetujuan | Perubahan plan tercatat, disetujui, rollback | UU Ps.98; Dirjen (jalan nasional) | T2 | Must | F-T1-18 | — | C-01/C-20 | audit lengkap |
| F-T2-24 | Warrant & kelayakan simpang | Cek warrant APILL/adaptif/ATCS/ITS/kotak kuning | PM 96 II.F | **T3** (dulu T2) | Could | F-T1-16 | survei | — | — |
| F-T3-25 | Simulasi wajib sebelum penetapan | Kirim plan ke twin, laporkan MoE, simpan bukti. Validasi SUMO sejak T2 (keputusan 2026-09-14). | PM 96 I.II.E.b | **T2** (dulu T3) | Must | F-T3-70 | twin | C-19 | tiap plan baru ada bukti simulasi |
| F-T3-26 | Generator plan alternate/quarter-cycle & resonant cycle | Cycle dari jarak & kecepatan progresi | STM2 §7.4 | **T5** (dulu T3) | Could | F-T2-22 | — | — | — |

## E04 — Controller Adapter (Controller Abstraction Interface)
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-27 | Adaptor simulasi TraCI/SUMO NEMA | Bangun tlLogic dari model; status & perintah via TraCI. Dipakai validasi SUMO di T2. | [R03 B.5, D.2] | **T2** (dulu T1) | Must | F-T1-18 | — | — | round-trip plan |
| F-T1-28 | Adaptor NTCIP 1202 read-only | GET status/alarm/VO report via SNMP | [R03 A.15] | **T3** (dulu T1) | Should | F-T1-02 | controller | — | poll 1 s |
| F-T2-29 | Adaptor NTCIP 1202 read-write | Perintah tipe C, heartbeat < backup time, transaksi P2, block upload/download | [R03 A.15, D.2] | **T4** (dulu T2) | Must | F-T1-28 | — | C-09 | fallback teruji |
| F-T2-30 | Adaptor RS-232 vendor lokal (≥1) | Protokol vendor e-katalog (mis. TKDN/lokal) di edge gateway | Majalah (RS232); e-katalog | **T4** (dulu T2) | Must | F-T2-29 | — | — | 1 vendor lulus HIL |
| F-T2-31 | Edge logger I/O kabinet (fallback) | Rekam input/output kabinet bila controller tanpa logger | NCDOT §5.1 [R03 C.1] | **T4** (dulu T2) | Should | — | I/O | — | event 0,1 s |
| F-T2-32 | Discovery kapabilitas (conformance) | Baca max* & uji grup objek; PRL (hanya membaca, dimulai saat controller dibaca di T3) | NTCIP Annex A | **T3** (dulu T2) | Should | F-T1-28 | — | — | — |
| F-T2-33 | Edge agent: buffer & batch bila offline | Store-and-forward event, sinkron jam (GPS/NTP) | P4 hemat server | **T4** (dulu T2) | Must | F-T2-29 | — | — | 0 kehilangan data 24 jam offline |
| F-T3-34 | Detektor virtual dari kamera AI | Count/occupancy/queue per lajur → VehCall/E1. Untuk kendali (T4). Hitungan vision di laptop ada di E20. | [R03 D.2]; TKDN Viero | **T4** (dulu T3) | Must | F-T3-123 | kamera | C-12 | akurasi count ≥90% siang (ASUMSI) |
| F-T4-35 | Adaptor NTCIP 1211 (SCP) & 1202 v03 | Priority request/status objek | [R03 A.16] | T4 | Should | F-T2-29 | — | — | — |
| F-T4-36 | SPaT/MAP publish (CV-ready) | Keluaran SAE J2735 dari status | TSPH Bab 9 | **T5** (dulu T4) | Could | F-T2-29 | — | — | — |

## E05 — TMC Console, Override & Mode Manual
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T2-37 | Pilih plan/free/flash dari TMC | systemPatternControl per simpang/grup + log | [R03 A.15] | **T4** (dulu T2) | Must | F-T2-29 | — | C-15 | — |
| F-T2-38 | Mode manual petugas (perpanjang/perpendek hijau) | Override terbatas waktu, alasan, identitas (Polri/Dishub) | UU Ps.104; SK 7234 | **T4** (dulu T2) | Must | F-T2-37 | — | C-15 | semua override ter-log |
| F-T2-39 | Hold/force-off/omit/call manual | Perintah tipe C dengan konfirmasi | NTCIP C objects | **T4** (dulu T2) | Should | F-T2-29 | — | — | — |
| F-T2-40 | Sinkronisasi jam & offset | systemSyncControl; deteksi drift | STM2 §7.3 | **T4** (dulu T2) | Must | F-T2-29 | — | — | drift ≤1 s |
| F-T2-41 | Audit trail perintah (siapa-kapan-mengapa) | CommandLog + PlanChangeTransaction | HOP-11-027 Req 18.0-3 | **T4** (dulu T2) | Must | — | — | C-26 | 100% perintah |
| F-T2-42 | Notifikasi APILL tidak berfungsi ke Polri/TMC | Insiden otomatis saat flash/fault. Deteksi APILL mati atau kedip dari kamera (T3) atau controller (T4). | PP 32 Ps.34–35 | **T3** (dulu T2) | Must | F-T2-148 | alarm | C-18 | ≤1 menit |
| F-T4-43 | Integrasi pusat kendali Polri (NTMC/RTMC) | Pertukaran status & perintah C2C | UU Ps.246–247 | T4 | Must | F-T4-96 | — | C-22 | — |

## E06 — Kesehatan Perangkat, Alarm, Watchdog
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T2-44 | Health detektor (no activity, max presence, erratic, count vs profil) | Dari alarm NTCIP & analitik event | STM2 Exhibit 8-16; NTCIP §2.3 | **T4** (dulu T2) | Must | F-T2-29 | — | C-08 | % detektor berfungsi |
| F-T2-45 | Alarm controller (flash, conflict, coord fail, stop time, pintu kabinet) | Real-time + eskalasi | NTCIP unitAlarm; TSPH | **T4** (dulu T2) | Must | F-T2-29 | — | C-18 | alarm ≤X menit |
| F-T2-46 | Uptime komunikasi & poll stats | Persentase connected, latency | STM2 8-16 | **T4** (dulu T2) | Must | F-T2-33 | — | — | — |
| F-T2-47 | Watchdog harian ATSPM | No data, force-off/max-out >90% dini hari, low counts, stuck ped | HOP-20-002 p.20 | **T4** (dulu T2) | Must | F-T1-54 | hi-res | — | email harian |
| F-T2-48 | Alarm → tiket kerja otomatis | Work order ke teknisi, MTTR | TSPH G.4 | **T3** (dulu T2) | Must | F-T2-50 | — | — | MTTR tercatat |
| F-T2-49 | KPI kesehatan perangkat | % kamera sehat dan % simpang terpantau (T3); % detektor OK, % sinyal offline, transisi berlebih, false preempt (T4) | TSPH Tabel 46 | **T3** (dulu T2) | Should | F-T3-154 | — | — | — |

## E07 — Keluhan Publik & SLA
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T2-50 | Tiket keluhan (form 7 langkah) | Pelapor, lokasi, waktu, berulang, deskripsi, jaminan waktu | STM2 Exhibit 8-17 | **T3** (dulu T2) | Must | — | — | — | SLA (3 jam DKI) |
| F-T2-51 | Matriks diagnosis keluhan | Keluhan → pertanyaan diagnostik → data terkait (hitungan dan nyala lampu dari Vision Tracker di T3; metrik sinyal controller di T4) | STM2 §8.3.2.4 | **T3** (dulu T2) | Should | F-T2-50 | — | — | — |
| F-T2-52 | Integrasi CRM/aduan kota | API dua arah (mis. JAKI/CRM) | Beritajakarta 145079 | **T3** (dulu T2) | Could | F-T2-50 | — | — | — |
| F-T3-53 | Rekreasi kejadian historis | Putar ulang hitungan, nyala lampu, dan peristiwa saat komplain (log controller mulai T4) | HOP-11-027 Need 4.11 | T3 | Should | F-T2-148 | hi-res | — | — |

## E08 — Hi-res Log & ATSPM
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-54 | Ingest event 0,1 s (kode Indiana) | Skema HiResEvent; dedup; dari SUMO/controller/edge | [R03 C.2] | **T3** (dulu T1) | Must | F-T1-27 | — | — | — |
| F-T1-55 | Phase termination & split monitor | Gap/max/force-off/skip; durasi vs split | NCDOT A.1–A.2 | **T4** (dulu T1) | Must | F-T1-54 | event | — | — |
| F-T1-56 | PCD / AoG / platoon ratio | Advance detector vs siklus | NCDOT A.5 | **T4** (dulu T1) | Must | F-T1-54 | advance | — | — |
| F-T1-57 | Purdue split failure (GOR/ROR5 ≥80%) | Per fase per siklus | NCDOT A.8 | **T3** (dulu T1) | Must | F-T1-54 | stop-bar | — | — |
| F-T2-58 | Ped delay, preemption details, AoR, approach delay | Metrik tambahan | NCDOT A.3/4/10/11 | **T3** (dulu T2) | Should | F-T1-54 | — | — | — |
| F-T2-59 | TMC/approach volume, PHF/K/D | Volume per pendekat dan per arah dari hitungan Vision Tracker; PHF, K, D | NCDOT A.7/9 | T2 | Should | F-T1-144 | count | — | — |
| F-T3-60 | YRA (yellow/red actuations) & bukti RLR | Deteksi kendaraan masuk simpang saat kuning/merah dari nyala lampu kamera dan lintasan Vision Tracker | NCDOT A.13 | T3 | Should | F-T2-148 | past-stop-bar | C-24 | — |
| F-T3-61 | Link Pivot (rekomendasi offset koridor) | Optimasi offset dari AoG | NCDOT A.6 | **T5** (dulu T3) | Must | F-T1-56 | advance | — | AoG naik |
| F-T2-62 | Agregasi & retensi bertingkat | Data rinci disimpan singkat, ringkasan 15 menit disimpan 5 tahun; mulai T4 juga log 0,1 s controller (30–90 hari) | P4 | T2 | Must | F-T1-144 | — | — | storage terprediksi |

## E09 — KPI, LOS, Dashboard & Laporan Wajib
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-63 | LOS simpang PM 96 (A–F) real-time & historis | Tundaan estimasi (PKJI dari count/occupancy) | PM 96 [R00 E] | T1 | Must | F-T1-16 | count | C-30 | — |
| F-T1-64 | Before–after / on-off evaluator | Dua rentang atau dua skenario; MoE tundaan, LOS, antrian, kendaraan terhenti (T2: eksisting vs rekomendasi dari PKJI dan SUMO; T3: uji lapangan); AoG dan split failure menyusul saat metrik sinyal tersedia | STM2 §8.3.1; T414 | **T2** (dulu T1) | Must | F-T1-160 | — | C-20 | laporan otomatis |
| F-T2-65 | Laporan MRLL ke Forum LLAJ | Template berbasis data & kinerja | UU Ps.98 | **T3** (dulu T2) | Must | F-T1-64 | — | C-20 | — |
| F-T2-66 | Kajian kecepatan rata-rata & V/C (Dirjen/BPTJ) | Template PM 96 Lampiran III; memakai hitungan Vision Tracker dan survei; data probe menyusul di T5 (F-T3-58) | PM 96 | **T3** (dulu T2) | Must | F-T2-59 | hitungan, survei (probe di T5) | C-21 | — |
| F-T2-67 | Laporan triwulan Gubernur & tahunan | Pergub 68 Ps.15; Perda Ps.237 | [R05] | **T3** (dulu T2) | Should | — | — | C-35 | — |
| F-T2-68 | Dashboard publik "kota" | Peta status, LOS, waktu tempuh, SLA keluhan (anonim) | UU Ps.250; Perda Ps.233 | **T3** (dulu T2) | Should | F-T1-63 | — | C-23 | — |
| F-T3-69 | Travel time & reliability (95th, buffer, planning index) dari probe | Per koridor/jam | NYSERDA Tabel 7 | **T5** (dulu T3) | Should | F-T3-58 | probe | — | target 35/30 km/j |
| F-T3-70 | Estimasi emisi/BBM per koridor | Model stops & delay → CO2. Versi sederhana di T2 (F-T2-164), lengkap di T3. | PKJI catatan; NCDOT CBA | **T2** (dulu T3) | Could | F-T1-64 | — | C-31 | — |
| F-T4-71 | Laporan efektivitas ke Dirjen/BPTJ (PM 76 Ps.22–24) | Otomatis tahunan | PM 76 | T4 | Should | F-T2-65 | — | — | — |
| F-T5-72 | Benchmark antar kota | Peringkat AoG/LOS/uptime multi-tenant | T5 konsep | T5 | Could | F-T5-114 | — | — | — |

## E10 — Koordinasi, Green Wave & Traffic-Responsive
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T2-73 | Koordinator pusat (pattern, offset reference, force-off, permissive) | Parameter koordinasi per grup | STM2 §7.3 | **T4** (dulu T2) | Must | F-T2-29 | — | C-11 | — |
| F-T2-74 | Transition engine & KPI transisi | dwell/add/subtract/shortway; ≥30 menit/pattern | STM2 §7.5.3 | **T4** (dulu T2) | Must | F-T2-73 | — | — | transisi ≤3–5 siklus |
| F-T3-75 | Traffic-responsive plan selection | V+K·O, hysteresis, signature/threshold | STM2 §9.3 | **T4** (dulu T3) | Must | F-T3-34 | detektor sistem | — | — |
| F-T3-76 | Penalaan offset berbasis probe (cyclic TSD, PPD, SOFT) | Agregasi multi-hari, cycle length diketahui | R04 A.19 | **T5** (dulu T3) | Must | F-T3-58 | probe | — | AoG +10 poin (ASUMSI) |
| F-T3-77 | Dynamic phase length / re-service | Fitur koordinasi lanjut sebelum adaptif | STM2 §9.2 | **T4** (dulu T3) | Could | F-T2-73 | detektor | — | — |
| F-T4-78 | Toolkit oversaturation (split reallocation, negative/simultaneous offset, green flush, gating) | Strategi jenuh manual/semi-otomatis | STM2 §12 | **T5** (dulu T4) | Should | F-T2-73 | — | — | — |

## E11 — Actuated, Adaptif & Perimeter Control
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T3-79 | Actuated/semi-actuated dari detektor virtual | Min/max green, passage, gap reduction, recall di controller/edge | STM2 §6 | **T4** (dulu T3) | Must | F-T3-34 | detektor | C-12 | — |
| F-T3-80 | Health gate untuk mode adaptif | Adaptif hanya bila detektor sehat ≥N hari; auto-degrade | C-12; R04 F guard-rail 4 | **T4** (dulu T3) | Must | F-T2-44 | — | C-12 | — |
| F-T4-81 | Cyclic max-pressure terkoordinasi | Split by pressure ternormalisasi; min green; ≤5 s/siklus; integer QP | R04 A.5 | **T5** (dulu T4) | Must | F-T3-79 | antrian/okupansi | — | VHT −10% (ASUMSI) |
| F-T4-82 | Pemilihan simpang kritis (skor R_n) | Okupansi rata-rata, varians, durasi ≥80% | R04 A.5 | **T5** (dulu T4) | Must | F-T2-62 | historis | — | — |
| F-T4-83 | Perimeter control (PI, hysteresis) | Gating CBD berbasis akumulasi MFD | R04 A.5 | **T5** (dulu T4) | Should | F-T4-81 | akumulasi | — | — |
| F-T4-84 | Delay-based MP dari probe (D-MP) | Opsi metrik pressure = delay | R04 A.4 | **T5** (dulu T4) | Could | F-T3-58 | probe | — | — |
| F-T4-85 | Predictive volume 15–60 menit | Prakiraan dari historis (hari, cuaca, event) | Antara 3635259; R06 D.2 | T4 | Should | F-T2-62 | historis | — | MAPE ≤20% (ASUMSI) |
| F-T5-86 | RL advisor (shadow) untuk parameter MP/PC | Multi-OD training; veto statistik | R04 A.15–A.16 | T5 | Could | F-T3-108 | twin | — | — |

## E12 — Prioritas Transit & Darurat
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T3-87 | Priority Request Server terpusat | Antrian permintaan, level, TSD/TED, 1 aktivasi/siklus, lockout, log | STM2 §10; TSP Handbook | **T4** (dulu T3) | Must | F-T2-29 | AVL | C-14 | — |
| F-T3-88 | TSP green extension / early green (≤10 s) | Strategi dasar per simpang/TOD | R06 F.2 | **T4** (dulu T3) | Must | F-T3-87 | AVL/check-in | C-14 | bus TT −10% |
| F-T3-89 | Check-in/check-out geofence + konfirmasi kamera | Hentikan extension setelah bus lewat | TSP h.66 | **T4** (dulu T3) | Must | F-T3-88 | GPS | — | — |
| F-T4-90 | TSP kondisional headway/keterlambatan (OCC/Transit-MP) | Bobot occupancy; bus di halte tak dihitung; fallback historis | R04 A.6–A.7 | **T5** (dulu T4) | Must | F-T3-88 | APC/AVL | C-14 | PTT turun |
| F-T4-91 | EVP bertingkat (mixed-criticality) | Preempt hanya bila target respons terancam; conflict graph; recovery | R04 A.18; UU Ps.135 | T4 | Must | F-T4-97 | CAD/GPS | C-16 | EV target ≥90% |
| F-T4-92 | VIP/konvoi green wave terjadwal | Rute & waktu; kembali ke koordinasi. Memakai offset dasar T4. | PM 76 Ps.7(4)a | T4 | Should | F-T4-91 | — | — | — |
| F-T3-93 | MoU digital detik prioritas | Parameter prioritas dengan riwayat & persetujuan lintas instansi | TSP h.23 | **T4** (dulu T3) | Should | F-T3-87 | — | — | 0 perubahan tak tercatat |
| F-T4-94 | Batas prioritas terhadap pejalan kaki & side street | Walk/FDW tak dipotong; ambang DS kaki lawan | TSP h.77; PKJI 0,85 | T4 | Must | F-T3-88 | — | keselamatan | — |

## E13 — Integrasi Eksternal
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T2-95 | CCTV live view (RTSP→WebRTC), tanpa rekam di pusat | Kamera eksisting | P4 | **T3** (dulu T2) | Must | — | RTSP | — | ≤60 stream |
| F-T4-96 | C2C ke pusat kendali Polri & JSC | Status, insiden, perintah | UU Ps.246 | T4 | Must | F-T2-29 | — | C-22 | — |
| F-T4-97 | AVL/CAD pemadam & ambulans (112/119) | Unit ditugaskan, rute, posisi | FHWA EVP | T4 | Must | — | API | — | — |
| F-T3-98 | AVL/APC operator bus (TransJakarta/BRT kota) | Posisi, headway, keterlambatan, muatan | Pergub 68 Ps.10(6) | **T4** (dulu T3) | Must | — | API | — | — |
| F-T3-99 | Bukti ETLE-ready ke Polri | Paket bukti (foto/video/pelat/waktu) & status | UU Ps.272; C-24 | **T4** (dulu T3) | Should | F-T3-60 | ANPR | C-24, PDP | — |
| F-T4-100 | Bapenda: query status pajak per pelat (agregat per ruas) | Perjanjian & PDP | Antara 5051249 | T4 | Could | F-T3-99 | ANPR | C-25 | — |
| F-T4-101 | DLH: uji emisi per pelat → target ruas | Agregat kepatuhan | Antara 5051249 | T4 | Could | F-T3-99 | ANPR | C-25/31 | — |
| F-T4-102 | Pengelola tol: arus menuju gerbang | Data ramp/gerbang | Majalah | T4 | Could | — | API | — | — |
| F-T4-103 | Cuaca & kualitas udara | Trigger weather plan; info baku mutu udara | STM2 §11.1; UU Ps.249 | T4 | Should | F-T2-13 | API | C-31 | — |
| F-T5-104 | API publik & data terbuka | Status, LOS, waktu tempuh, log prioritas anonim | UU Ps.250 | T5 | Should | F-T2-68 | — | C-23 | — |
| F-T5-105 | GLOSA/SPaT ke aplikasi navigasi | Layanan ATIS | PM 76 Ps.8 | T5 | Could | F-T4-36 | — | — | — |

## E14 — Digital Twin & Shadow Mode
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-106 | Generator jaringan SUMO dari registri (+OSM) | net/add/rou otomatis. Dipakai validasi SUMO di T2. | [R03 B.9] | **T2** (dulu T1) | Must | F-T1-01 | — | — | — |
| F-T3-107 | Kalibrasi twin per simpang (koridor menyusul) | Demand dari hitungan Vision Tracker; galat ≤15% (ASUMSI). Kalibrasi per koridor menyusul bersama offset dasar di T4 dan optimasi koridor di T5 (keputusan 2026-09-14). | [R04 A.3] | T3 | Must | F-T1-106 | count | — | — |
| F-T3-108 | Shadow mode engine | Algoritma menerima data live, keputusan dicatat tanpa aktuasi, dibandingkan | [R04 A.3 §8.4] | **T4** (dulu T3) | Must | F-T2-29 | — | — | laporan divergensi |
| F-T3-109 | Uji konflik prioritas di twin | TSP vs EVP vs VVIP | TSP h.31 | **T4** (dulu T3) | Should | F-T3-107 | — | — | — |
| F-T4-110 | Uji plan otomatis (batch what-if) | Skenario demand/cuaca/insiden | STM2 §11 | T4 | Should | F-T3-107 | — | — | — |
| F-T5-111 | Twin kota mesoscopic + what-if kebijakan TDM | Ganjil-genap/ERP/penutupan | PP 32 | T5 | Should | F-T3-107 | — | — | — |
| F-T5-112 | Marketplace algoritma (SIL→shadow→live) | Plugin pihak ketiga dengan sandbox & veto | R04 A.15 | T5 | Could | F-T3-108 | — | — | — |

## E15 — Multi-tenant, Keamanan, Tata Kelola
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-113 | RBAC dasar & audit log | Peran operator/engineer/admin/viewer | Req 5.0-1 | **T2** (dulu T1) | Must | — | — | C-26 | — |
| F-T5-114 | Multi-tenant per kota/yurisdiksi | Isolasi data, akses per status jalan (BPTJ/Polri) | PM 76 Ps.19 | T5 | Must | F-T1-113 | — | C-17 | — |
| F-T2-115 | Kebijakan keamanan NEMA TS 8 (mTLS edge, segmentasi, kunci kabinet) | Checklist & monitoring | TSPH G.7 | **T4** (dulu T2) | Must | F-T2-33 | — | — | audit lulus |
| F-T3-116 | Tata kelola data PDP (klasifikasi, retensi video dan klip, persetujuan akses) | Data kamera Dishub mulai T3 (MoU, DPIA); aturan pelat, pajak, dan emisi ditambahkan saat ANPR di T4 | UU 27/2022; Pergub 68 | T3 | Must | F-T2-151 | — | C-26 | — |
| F-T2-117 | Workflow persetujuan jalan nasional (Dirjen/BPTJ) | Status jalan → alur persetujuan | PM 96 Ps.5 | **T3** (dulu T2) | Should | F-T1-05 | — | C-01 | — |
| F-T2-118 | Field diary & notifikasi kunjungan | Catatan lapangan, larangan upload di luar jam teknisi | NCDOT protocol | **T4** (dulu T2) | Should | F-T2-48 | — | — | — |
| F-T2-119 | Mobile teknisi (Android/PWA) | Tiket, checklist PM, foto, offline | TSPH G.4 | **T4** (dulu T2) | Must | F-T2-48 | — | — | — |
| F-T3-120 | E-learning operator & sertifikasi internal | Modul kalibrasi, ATSPM, SOP | RPP h.19; TSPH G.3 | **T4** (dulu T3) | Should | — | — | C-33 | — |
| F-T4-121 | Core competency & jadwal retiming ≤3 tahun | Tracking retiming per simpang | TSTM §2.3 | T4 | Could | F-T2-23 | — | — | — |
| F-T2-122 | Backup/restore database controller (block OER) | Cloning konfigurasi | NTCIP §2.12 | **T4** (dulu T2) | Should | F-T2-29 | — | — | — |

## E16 — AI Recognition & Predictive (layanan)
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T3-123 | Klasifikasi kendaraan & count per lajur di edge | Model ringan (YOLO-class). Versi di perangkat edge (T4). Versi laptop ada di E20. | R06 D.2 | **T4** (dulu T3) | Must | — | kamera | — | — |
| F-T3-124 | Estimasi panjang antrian dari kamera | Untuk MP & LOS. Dasar di T2 (F-T2-149), lengkap di T3. | R04 A.2 | T3 | Must | F-T2-149 | kamera | — | — |
| F-T4-125 | ANPR & deteksi kendaraan prioritas (pelat khusus) | Bus/ambulans/pemadam via pelat sebagai fallback AVL. Memakai kamera ANPR khusus; dipindah kembali ke T4 (keputusan 2026-09-14, menggantikan keputusan 2026-09-13); prasyarat F-T3-116 dan DPIA. | Majalah; Antara | **T4** (dulu T3) | Should | F-T3-123, F-T3-116 | ANPR | PDP | — |
| F-T4-126 | Deteksi pelanggaran (RLR, lajur terlarang) sebagai bukti | Bukan penindakan | C-24 | **T3** (dulu T4) | Should | F-T3-60 | kamera | C-24 | — |
| F-T4-127 | Deteksi insiden otomatis (berhenti, kepadatan anomali) | Trigger plan insiden | STM2 §11.2 | **T3** (dulu T4) | Should | F-T3-124 | kamera/probe | — | — |
| F-T5-128 | Keselamatan VRU (fusi kamera+radar, LPI adaptif) | Konflik pejalan kaki | R04 A.3 | T5 | Could | F-T3-123 | radar | — | — |
| F-T4-129 | Nilai antara transparan untuk semua model AI | Simpan input/skor/keputusan. Berlaku untuk Vision Tracker dan modul optimasi sejak T2. | Req 18.0-2 | **T2** (dulu T4) | Must | — | — | anti black-box | — |

## E17 — Special Conditions & Operasi
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T2-130 | Plan insiden/event/banjir manual (nomor 51–59) | Trigger, kriteria masuk/keluar, pemilik | STM2 Exhibit 11-7; NCDOT | **T4** (dulu T2) | Should | F-T1-21 | — | — | — |
| F-T3-131 | Trigger otomatis (kecepatan probe, konfirmasi insiden) | Aktivasi plan dari kecepatan antarkamera (F-T3-157) dan konfirmasi insiden; kecepatan probe menyusul di T5 | STM2 §11.2 | **T4** (dulu T3) | Should | F-T3-157 | kamera (probe di T5) | — | — |
| F-T3-132 | Weather-responsive plan | +red clearance, min green; deteksi kecepatan turun | STM2 §11.1 | **T4** (dulu T3) | Could | F-T4-103 | cuaca | — | — |
| F-T2-133 | Flush/contingency plan manual | Green flush hilir→hulu | STM2 §12 | **T5** (dulu T2) | Could | F-T2-37 | — | — | — |
| F-T4-134 | Post-event debrief otomatis | Laporan kinerja selama event | STM2 §11.3 | T4 | Could | F-T1-64 | — | — | — |

## E18 — Probe & Data Eksternal Lalu Lintas
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T3-58 | Ingest probe GPS (bus/ojol/navigasi) & map-matching | Waypoint → segmen; agregasi multi-hari | R04 A.19 | **T5** (dulu T3) | Must | — | probe | PDP | — |
| F-T3-135 | Estimasi turning ratio & OD dari probe | Untuk MP & twin | R04 A.5 | **T5** (dulu T3) | Should | F-T3-58 | probe | — | — |
| F-T4-136 | Deteksi waktu tempuh koridor (PM 76 Ps.7(2)g) | Bluetooth/WiFi/probe | PM 76 | **T5** (dulu T4) | Should | F-T3-58 | — | — | — |
| F-T5-137 | Analitik "tanpa detektor" untuk kota baru | Paket evaluasi koridor dari probe saja | R04 A.19 | T5 | Should | F-T3-76 | probe | — | — |

## E19 — TDM & Kebijakan (T5)
| ID | Fitur | Deskripsi | Bukti | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T5-138 | Kalkulator ambang MKLL per ruas (V/C, kecepatan) | Ganjil-genap ≥0,7 & <30 km/j; ERP ≥0,9 & ≤10 km/j | PP 32 Ps.65–79 | T5 | Should | F-T3-69 | probe/count | C-28/29 | — |
| F-T5-139 | Evaluasi tahunan MKLL otomatis | Laporan efektivitas (kecepatan rata-rata) | PP 32 Ps.63; Perda Ps.81 | T5 | Should | F-T5-138 | — | C-29 | — |
| F-T5-140 | Integrasi ERP/ganjil-genap (data pembatasan ke sistem Pemprov) | Pertukaran data | Pergub 68 Ps.13(4) | T5 | Could | F-T5-138 | — | — | — |

## E20 — Vision Tracker (baru 2026-09-14)
| ID | Fitur | Deskripsi | Bukti/kebutuhan | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-141 | Pengolahan rekaman video per kamera | Unggah dan antrean file rekaman dengan metadata (simpang, pendekat, tanggal, jam mulai, kondisi, sumber dan izin); pembacaan bingkai sekitar 10 per detik | keputusan user T-34, T-41 | T1 | Must | F-T1-01 | rekaman | PDP | klip 30 menit terolah tanpa galat |
| F-T1-142 | Deteksi dan pelacakan enam kelas | Motor, mobil (termasuk angkot dan pikap), bus, truk, kendaraan tak bermotor, pejalan kaki; model berlisensi Apache-2.0 lewat ONNX Runtime; pelacakan ByteTrack | T-40, T-42 | T1 | Must | F-T1-141 | rekaman | — | akurasi sekitar 90% siang pada klip uji |
| F-T1-143 | Garis hitung per pendekat | Menggambar garis masuk per pendekat di cuplikan kamera | `15` §3 | T1 | Must | F-T1-142 | — | — | — |
| F-T1-144 | Tabel hitungan 15 menit | Tabel hitung_15m (simpang, pendekat, gerakan, kelas rinci dan PKJI, jumlah, sumber, mutu); ekspor CSV | `15` §3.4 | T1 | Must | F-T1-143 | — | — | tabel lengkap untuk semua pendekat |
| F-T2-145 | Arah gerakan dari lintasan | Lurus, belok kiri, belok kiri langsung, belok kanan dari lintasan masuk-keluar; cadangan proporsi belok manual; sumber ditandai | T-36 | T2 | Must | F-T1-144 | rekaman | — | arah benar sekitar 90% pada klip uji (ASUMSI) |
| F-T2-146 | Hambatan samping empat jenis berbobot | Pejalan kaki (0,5), kendaraan berhenti atau parkir (1,0), keluar-masuk (0,7), kendaraan lambat (0,4) per 200 m per jam; kelas KHS; pemetaan ke kelas simpang; rasio KTB | PKJI 2023 Tabel 4-8, 4-9; T-36 | T2 | Must | F-T1-142 | rekaman | C-08 dasar | kelas konsisten dengan penilaian engineer |
| F-T2-147 | Mode stream langsung | RTSP/HLS; diuji dengan rekaman yang diputar ulang lewat server stream lokal; 2 sampai 4 stream di laptop | T-34, T-39 | T2 | Must | F-T1-142 | stream | — | berjalan 8 jam tanpa henti |
| F-T2-148 | Pembacaan nyala lampu dari kamera | Area kepala lampu dibaca per bingkai; awal hijau, kuning, merah; siklus dan hijau eksisting terukur otomatis | T-38 | T2 | Should | F-T1-141 | rekaman | — | selisih ≤1 detik terhadap stopwatch (ASUMSI) |
| F-T2-149 | Antrian dan okupansi dasar | Kendaraan diam per lajur saat akhir merah; okupansi garis henti | T-38 | T2 | Should | F-T1-142 | rekaman | — | — |
| F-T2-150 | Uji akurasi hitungan | Alat hitung manual cepat; perbandingan per kelas per 15 menit; laporan akurasi per kondisi | T-34, T-39 | T2 | Must | F-T1-144 | hitungan manual | — | 90% siang, 85% malam atau hujan |
| F-T2-151 | Penyamaran dan retensi video | Wajah dan pelat pada cuplikan tersimpan diburamkan; video mentah dihapus setelah diolah kecuali sampel validasi | UU 27/2022 | T2 | Must | F-T1-141 | — | C-37, C-38 dasar | tidak ada video mentah tersimpan di luar sampel |
| F-T2-152 | Register sumber rekaman | Asal, tautan, izin atau lisensi, tanggal, kegunaan setiap rekaman | T-42 | T2 | Must | F-T1-141 | — | — | semua rekaman tercatat |
| F-T3-153 | Kendaraan prioritas dan iring-iringan | Ambulans, damkar, mobil polisi dengan lampu menyala, pengawalan | T-38 | T3 | Must | F-T1-142 | rekaman/stream | C-16 dasar | recall sekitar 90% pada set uji (ASUMSI) |
| F-T3-154 | Kesehatan kamera dasar | Kamera tertutup, gelap, buram, atau bergeser memicu peringatan | T-38 | T3 | Must | F-T1-141 | stream | C-08 | peringatan ≤5 menit |
| F-T4-155 | Kesehatan kamera lanjutan | Hujan lebat, genangan atau banjir, silau | T-38 | T4 | Should | F-T3-154 | stream | — | — |
| F-T3-156 | Kelas angkot dan pikap serta penalaan akurasi | Memisahkan angkot dan pikap dari mobil; penalaan hingga 95% siang dan 90% malam atau hujan | T-42 | T3 | Must | F-T2-150 | rekaman | — | 95%/90% |
| F-T3-157 | Kecepatan dan waktu tempuh antar kamera | Mencocokkan kendaraan antar kamera tanpa membaca pelat | T-38 | T3 | Should | F-T2-145 | stream | PDP | — |
| F-T3-158 | Waktu tunggu dan volume penyeberang | Jumlah penyeberang dan lama menunggu per fase | T-38 | T3 | Should | F-T2-146 | rekaman/stream | C-32 | — |

## E21 — Optimasi Waktu Simpang (baru 2026-09-14)
| ID | Fitur | Deskripsi | Bukti/kebutuhan | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-159 | Konversi hitungan ke arus SMP | EMP PKJI 2023 terlindung dan terlawan; arus satu jam tertinggi per periode; faktor jam puncak; rasio belok; rasio KTB | PKJI 2023 Tabel 5-2 | T1 | Must | F-T1-144 | hitungan | C-30 | — |
| F-T1-160 | Rekomendasi mode Webster/PKJI baku | Siklus Webster dan hijau sebanding rasio arus kritis, dengan validator keselamatan | PKJI 5-11, 5-12 | T1 | Must | F-T1-16 | — | C-30 | lolos contoh Dirjen 273/1996 |
| F-T2-161 | Mode optimasi pilihan | Tundaan terendah dengan batasan; minimalkan DJ tertinggi; siklus praktis minimum; pertahankan siklus eksisting; semua mode dihitung bersamaan | T-35 | T2 | Must | F-T1-160 | — | keselamatan | — |
| F-T2-162 | Mode pembanding MKJI 1997 | Rantai MKJI untuk studi lama dan uji regresi | T-35 | T2 | Should | F-T1-16 | — | — | cocok per baris formulir studi lama |
| F-T2-163 | Penentuan periode otomatis dan manual | Profil 15 menit menjadi paling banyak delapan jadwal per jenis hari; periode manual di konfigurasi | PM 49/2014; T-36 | T2 | Must | F-T1-144 | hitungan | C-09 | — |
| F-T2-164 | Manfaat rupiah sederhana | Nilai waktu (UMK), BBM saat diam, emisi; nilai tahunan; parameter dapat diubah | T-37 | T2 | Must | F-T1-64 | parameter ekonomi | — | — |
| F-T2-165 | Laporan kajian otomatis | Word dan PDF; formulir PKJI SA-I sampai SA-V; narasi; validasi SUMO; manfaat rupiah | T-37 | T2 | Must | F-T2-161 | — | C-19, C-20 dasar | laporan dalam satu klik |
| F-T3-166 | Mode multi-kriteria berbobot | Tundaan, antrian terhadap ruang tersedia, kendaraan terhenti, waktu tunggu pejalan kaki, prioritas angkutan umum | T-35 | T3 | Should | F-T2-161 | — | — | — |
| F-T3-167 | Skema fase alternatif | Evaluasi fase belok kanan terlindung dan penggabungan fase | `15` §4.6 | T3 | Should | F-T2-161 | — | keselamatan | — |
| F-T3-168 | Uji lapangan sebelum-sesudah | Dishub menerapkan jadwal rekomendasi; Vision Tracker mengukur perubahan | T-37 | T3 | Must | F-T2-161 | rekaman/stream | C-20 | penurunan tundaan terukur |
| F-T3-169 | Ekspor lembar jadwal | Tabel untuk petugas dan format vendor/NTCIP | T-38 | T3 | Must | F-T2-161 | — | C-09 | — |

## E22 — Konfigurasi Simpang dan Data Statis (baru 2026-09-14)
| ID | Fitur | Deskripsi | Bukti/kebutuhan | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-170 | Formulir konfigurasi sederhana | Geometri per pendekat, fase, waktu lampu eksisting | T-34 | T1 | Must | F-T1-01 | survei, citra | C-01 | — |
| F-T2-171 | Wizard konfigurasi intuitif | Peta satelit untuk menggambar dan mengukur lebar; templat simpang tiga dan empat lengan; nilai default PKJI; validasi dengan petunjuk | permintaan user 2026-09-14 | T2 | Must | F-T1-170 | citra | — | engineer baru selesai ≤30 menit (ASUMSI) |
| F-T2-172 | Pemetaan kamera dan penandaan zona | Tautan kamera ke pendekat; garis hitung, zona keluar, zona hambatan samping dan panjangnya, area kepala lampu | `15` §5 | T2 | Must | F-T2-171 | rekaman | — | — |
| F-T2-173 | Parameter kebijakan dan ekonomi | Hijau minimum, siklus maksimum, DJ target, UMK, harga BBM, okupansi kendaraan | `15` §4.6, §4.9 | T2 | Must | F-T2-171 | — | — | — |
| F-T2-174 | Versi serta ekspor dan impor konfigurasi | Riwayat perubahan konfigurasi; berkas konfigurasi dapat dipindahkan | — | T2 | Should | F-T2-171 | — | audit | — |

## E23 — Dashboard Simpang (baru 2026-09-14)
| ID | Fitur | Deskripsi | Bukti/kebutuhan | Tahap | MoSCoW | Dep | Data | Patuh | Sukses |
|---|---|---|---|---|---|---|---|---|---|
| F-T1-175 | Dashboard dasar satu simpang | Volume, kapasitas, DJ, tundaan, LOS, rekomendasi | T-34 | T1 | Must | F-T1-160 | — | C-30 | — |
| F-T2-176 | Halaman Ringkasan Simpang dan Rekomendasi | Peta dan diagram simpang; LOS keseluruhan dan per pendekat; lembar jadwal rekomendasi; eksisting vs rekomendasi; manfaat rupiah; unduh laporan | T-37 | T2 | Must | F-T2-161 | — | C-30 | — |
| F-T2-177 | Halaman Arus Lalu Lintas dan Kapasitas | Profil 15 menit; komposisi kelas; volume per pendekat dan per arah; kapasitas per pendekat dan per arah; jam puncak; hambatan samping; jadwal hasil pengelompokan | T-37 | T2 | Must | F-T2-163 | — | — | — |
| F-T2-178 | Halaman Kinerja Pendekat dan Kualitas Data | DJ, antrian, kendaraan terhenti, tundaan per pendekat; peringatan; antrian kamera vs PKJI; akurasi, cakupan rekaman, jam hilang, kondisi | T-37 | T2 | Must | F-T2-150 | — | — | — |

## Ringkasan
| Tahap | Jumlah fitur | Must | Should | Could |
|---|---|---|---|---|
| T1 | 13 | 13 | 0 | 0 |
| T2 | 33 | 26 | 6 | 1 |
| T3 | 42 | 20 | 20 | 2 |
| T4 | 62 | 34 | 20 | 8 |
| T5 | 29 | 7 | 11 | 11 |
| **Total** | **179** | 100 | 57 | 22 |

Catatan: fitur tahap lebih awal dibawa ke tahap berikutnya (kumulatif). Jumlah dihitung otomatis dari tabel di atas pada revisi 2026-09-14. Sesuai keputusan tim dua orang, hanya fitur Must yang dikerjakan sebelum ada pembeli; fitur Should dan Could menunggu permintaan pembeli atau sisa kapasitas.
