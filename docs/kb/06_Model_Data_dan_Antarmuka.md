# 06 — Model Data & Antarmuka

**Cara pakai.** Referensi cepat untuk merancang skema data, adaptor controller, dan integrasi eksternal ITCS. Entitas disusun agar **semantik NTCIP 1202** dapat dipetakan 1:1 (controller standar), sementara controller RS-232 vendor dan simulator SUMO dipetakan ke model yang sama (prinsip P1–P5 R03 D). Kolom "Padanan" memberi nama objek NTCIP / atribut SUMO / notasi PKJI agar tidak menerjemahkan ulang. Kode enumerasi hi-res mengacu pada tabel resmi Purdue/Indiana yang kini ada di korpus ([Purdue 2012]).

Tag: NTCIP §x = R03 A / NTCIP 1202 v02 clause; SUMO = R03 B; STM2 = R01; PKJI = R05 D; PM49/PM76/PM96/SK7234 = R00; R06 = TSP/EVP/Jakarta.

---

## A. Entitas inti (inventaris & konfigurasi)

| Entitas | Atribut kunci | Padanan / sumber |
|---|---|---|
| **Region / Corridor / Group** | id, nama, daftar simpang terurut, arah koordinasi, cycle bersama, sync reference, cross-coordination flag, suitability factor (ASCT), region MFD (untuk perimeter control), bias arah (Link Pivot) | STM2 §7.2.2, §9.4.2.1; R03 D.1 Corridor; R04 A.5 |
| **Intersection** | id, nama, lat/lon, kaki simpang (bearing, nama jalan, lajur), **status jalan** (nasional/provinsi/kota/tol) & yurisdiksi, tipe lingkungan (KOM/KIM/AT), kelas jalan, lebar W per pendekat, skew, grade, jarak ke tetangga, rel ≤200 ft?, tier ATSPM, status operasional, referensi SK/izin (KB-REQ-002), tanggal pemasangan & berlaku hukum | STM2 §3.2–3.3, §4.2, §10.5; PKJI Formulir SA-I; PM 96 Lamp. III; Perda Ps.74 |
| **Approach / Lane / Movement** | pendekat (U/S/T/B, sub-pendekat), lajur (jumlah, lebar, assignment, panjang turn bay, LBKiJT), movement number (NEMA 1–8 / HCM 1–18 / PKJI LRS-BKa-BKi), permitted/protected (tipe P/O), kecepatan (posted, v85), grade, halte/parkir/driveway, hambatan samping, LE/LM/LK | STM2 §3.3.4, §5.1.1; PKJI Langkah A |
| **Controller** | id → intersection, vendor, model, firmware, **protokol** {NTCIP-SNMP, NTCIP-STMP, vendor-RS232, TraCI-sim}, alamat IP/port/community atau serial, `unit_backup_time_s`, conformance groups didukung (phase, detector, coord, timebase, preempt, ring, channel, overlap, block), `max_phases`, `max_rings`, `max_vehicle_detectors`, `max_patterns`, `max_splits`, `max_preempts`, hi_res_logging (bool), jumlah signal group (≥8+8 hingga 32), jumlah program (≥4–16), plan/hari (≥10), kondisi kerja 5–70 °C/RH 95 %, sertifikasi, serial/tahun (penandaan), umur teknis (≤5 th), sim_id (twin) | NTCIP `unit`, `max*`, Annex A; SK 7234 Bab II; PM 49 Ps.24, 25, 42 |
| **Phase** | (controller, phase_number) , ring, concurrency[], enabled, movement, walk, ped_clear, min_green, passage, max1, max2, yellow, red_clear, red_revert, added_initial, max_initial, TBR, CBR, time_to_reduce, reduce_by, min_gap, dyn_max_limit/step, startup, options (16 bit: recall/flash/dual entry/…), **stage** (untuk model stage-based MKJI) | NTCIP `phaseTable` §2.2.2; SUMO NEMA `<phase minDur maxDur vehext yellow red name>`; PKJI wH/wK/wMS |
| **Ring / Sequence / Barrier** | sequence_number, ring_number, phase_order[], barrier groups | NTCIP `sequenceTable` §2.8.3; SUMO `ring1/ring2/barrierPhases/barrier2Phases` |
| **Overlap** | number, type {normal, minusGreenYellow}, included_phases[], modifier_phases[], trail green/yellow/red, load switch | NTCIP `overlapTable` §2.10; STM2 §5.1.4 |
| **Channel (SignalGroup)** | number, control_type {vehicle, ped, overlap}, control_source, flash_mode, dim; pemetaan ke *link index* SUMO | NTCIP `channelTable` §2.9; SUMO link index (searah jarum jam dari utara) |
| **Detector (Vehicle/Ped/Virtual)** | number, jenis {loop, magnetik, radar, video/AI-camera, ANPR, fisheye, ped button, virtual/probe}, lokasi (lane, jarak ke stop bar, panjang zona; kelas advance/stop-bar/past-stop-bar/count/presence/speed; ≥4 zona per pendekat), call_phase, switch_phase, options (call/queue/added-initial/passage/lock), delay, extend, queue_limit, diagnostik (no_activity, max_presence, erratic_counts, fail_time), alarms, output gap & occupancy, movement/lane_group (ATSPM), latency_correction, speed untuk konversi waktu tiba, sertifikasi | NTCIP `vehicleDetectorTable` §2.3.2, `pedestrianDetectorTable`; SK 7234 (h); NCDOT App. B; R03 D.2-4 |
| **Pattern (TimingPlan)** | (controller, pattern_number 1..253), cycle_time, offset_time, offset_reference_point, coordinated_phases, split_number, sequence_number, force_mode {floating, fixed}, correction_mode {dwell, shortway, addOnly}, max_mode, permissive mode, walk mode, actuated coordinated time, inhibit max, nama, koridor, tujuan (arah green wave), sumber (TOD/TRPS/adaptif/manual) | NTCIP `patternTable`, `coordForceMode`, `coordCorrectionMode` §2.5; SUMO `total-cycle-length/offset/fixForceOff`; STM2 §7.3 |
| **Split** | (split_number, phase), split_time, mode {none, minVehRecall, maxVehRecall, pedRecall, maxVehPedRecall, omitted}, coord_phase | NTCIP `splitTable` §2.5.9 |
| **TimebaseAction / DayPlan / Schedule** | action_number, pattern, aux/special functions; day plan (event time → action), schedule (hari/tanggal/libur/musim → day plan); ≥8 plan (PM 49), ≥10 perubahan/hari (SK 7234) | NTCIP `timebaseAscActionTable` §2.6, blok 0x0B/0x0C; SUMO WAUT; STM2 §6.3 |
| **AlternativePlan** (incident/event/weather/evacuation/flush) | nomor (51–59 gaya NCDOT), segmen, sinyal & pengelola, tujuan, asumsi, perubahan timing, **kriteria implementasi & penghentian**, pemilik/akses aktivasi, hasil validasi, MoU | STM2 Exh.11-7; NCDOT Alternative Timing Plans |
| **Preempt** | number, semua parameter NTCIP (delay, min duration/green/walk, enter ped clear/yellow/red, track green/yellow/red, dwell green, max presence, track/dwell/exit/cycling phases & overlaps, link, control bits), sumber (rel/EV/manual), prioritas relatif, rel: MWT, RTT, TCGI, gate-down inputs | NTCIP `preemptTable` §2.7.2; STM2 §10.4–10.5 |
| **PrioritySource / PriorityRequest (TSP)** | vehicle_id, class (bus/EV/truk/VVIP), route/line, level, TSD, TED, posisi/AVL, schedule deviation, headway, door status/halte flag, ridership/occupancy, status {received, scheduled, served, denied}, strategi (ext/early/insert/rotate), waktu layanan, lockout, recovery | NTCIP 1211 PRG/PRS (tidak di korpus, R06 A.6); STM2 §10.2–10.3; R04 A.6–A.7 |
| **SpecialFunction / VMS / DIS** | number, deskripsi, status, konten, protokol (DIS RS-485 1200–9600 bps), countdown 5–7 s | NTCIP `specialFunctionOutputTable` §2.4.14; SK 7234 (i); PM 76 Ps.7(2)c |
| **Asset & Maintenance** | komponen (luminer, tiang, pondasi, controller, kabel, detektor, DIS, kamera), serial/pabrik/tahun/tegangan, tanggal pasang, umur teknis, jadwal PM ≤6 bulan + checklist, log insidentil, tiket CRM, MTTR, penilaian kinerja aset, horizon 5 tahun | PM 49 Ps.19–25, 41–42; SK 7234 Bab II; TSPH G.4 |
| **User / Role / Jurisdiction** | pengguna, peran (operator TMC, engineer, teknisi, admin, pimpinan, mitra eksternal), yurisdiksi (Dishub/Sudinhub wilayah/BPTJ/Polri), kompetensi/sertifikasi, hak per kelas perangkat & fungsi (21 elemen security policy) | MSE Req 5.0-1; PM 76 Ps.21; PM 96 Ps.1(4) |

## B. Entitas runtime & time-series

| Entitas | Atribut kunci | Padanan |
|---|---|---|
| **ControllerStatusSnapshot** | ts, pattern_status (1–253/254 Free/255 Flash), local_free_status, cycle_status (0..510 s countdown), sync_status, control_status {systemControl, standby, backupMode, manual, timebase, interconnect}, flash_status, alarm1/alarm2/short_alarm, active_action, per-fase bitmask R/Y/G/Walk/PedClear/DontWalk/VehCall/PedCall/On/Next, per-ring ring_status (gap/max/force-off + coded status), per-detektor active/alarms, preempt_state[] | NTCIP §2.2.4, §2.4.5–9, §2.5.10–13, §2.7.2, §2.8.6 |
| **HiResEvent** (append-only) | intersection_id, ts (0,1 s), event_code (Indiana/Purdue), event_param (Phase # 1–16 / DET Channel # / Preempt # 1–10 / Pattern # 0–255 / detik), source {controller, external-logger, sumo, camera-virtual}, ingest_batch_id | [Purdue 2012] enumerations (ATSPM); SUMO `whetherOutputState` |
| **VolumeOccupancyReport** | ts, period_s, sequence, per-detektor volume (0..254; 255 overflow), occupancy (0..200 = 0,5 %; kode fault 210–217) | NTCIP §2.3.5 |
| **DetectionEvent (AI/ANPR)** | ts, kamera, zona/lajur, jenis kendaraan, pelat (terenkripsi/hash, retensi PDP), arah, kecepatan, event pelanggaran (kode), bukti (ref file) | RPP h.9; Antara 5051249; UU PDP |
| **ProbeTrajectory** | journey_id, ts, lat/lon, speed, sumber (TJ AVL, ojol, navigasi), map-matched link | R04 A.19 |
| **CommandLog** (audit) | ts, aktor (operator/algoritme), controller, objek/OID atau perintah abstrak, nilai, hasil (SNMP error/ascBlockErrorStatus/dbVerifyError), transaction_id, alasan | NTCIP Annex B/C; R04 GR8 |
| **PlanChangeTransaction** | transaction_id, snapshot sebelum/sesudah (blok OER), status {buffering, verify, done, error}, pesan verifikasi, persetujuan (bila jalan nasional) | NTCIP Annex C.4–C.5; PM 96 Ps.5(2) |
| **KPI / MetricResult** | intersection/phase/approach/detector/corridor, metric_type, bin_start, bin_size, nilai | lihat `07_KPI_dan_Monev.md` |
| **Alert / WorkOrder** | ts, jenis (watchdog no_data/force_offs/max_outs/low_adv_counts/stuck_ped; alarm NTCIP; APILL tidak berfungsi), ambang, nilai, status penanganan, tiket CRM, SLA | HOP-20-002 p.20; PP 32 Ps.34 |
| **ServiceRequest (keluhan publik)** | pelapor, kontak, lokasi, waktu, berulang?, deskripsi, kategori diagnostik, SLA (3 jam Dishub / ≤1 minggu STM2), hasil, respons | STM2 Exh.8-17; Beritajakarta 145079 |
| **SimulationScenario / Run** | net.xml, add.xml (tlLogic + detektor), rou.xml, seed, durasi, controller under test, hyperparameter, MoE (travel time mean/std/median, queue, delay), HiResEvent keluaran | R03 B.9, D.1 |
| **EvaluationStudy (before–after)** | tujuan, MOE, periode before/after atau on/off, data, hasil, cost-benefit, rekomendasi (high/med/low), riwayat retiming | STM2 §8.3.1; NCDOT CBA |
| **CountProfile / SurveyData** | LHRT (≥4×/tahun; 7 hari), VJP, TMC per periode, PHF, % truk, ped/bike, komposisi | PM 96 Lamp. I II.B; PKJI Formulir SA-II |
| **ExternalDataRecord** | jenis (pajak, uji emisi, pelanggaran ETLE, AVL, CAD), pelat/ID (hash), ts, sumber, dasar hukum perjanjian, retensi | Pergub 68 Ps.10(6); R06 F.4 |

## C. Enumerasi penting

| Enumerasi | Nilai | Sumber |
|---|---|---|
| Mode kendali (regulasi) | terkoordinasi terpusat; tidak terkoordinasi: siklus tetap (≥8 plan), semi-adaptif, adaptif | PM 49 Ps.11–16 |
| Mode operasi controller (NTCIP) | `coordOperationalMode` 0 Automatic / 1–253 Manual Pattern / 254 Free / 255 Flash; `unitControlStatus` {systemControl, systemStandby, backupMode, manual, timebase, interconnect}; `unitFlashStatus` {notFlash, automatic, localManual, faultMonitor, mmu, startup, preempt} | NTCIP §2.5.1, §2.4.5–6 |
| Local free reason | {notFree, commandFree, transitionFree, inputFree, coordFree, badPlan, badCycleTime, splitOverrun, invalidOffset, failed} | NTCIP §2.5.11 |
| Alasan terminasi fase | Gap Out / Max Out / Force Off (+ skip, ped) ; coded status Min Green, Extension, Maximum, Green Rest, Yellow, Red Clearance, Red Rest | NTCIP `ringStatus` §2.8.6; ATSPM Phase Termination |
| Force mode / correction mode | floating / fixed ; dwell / shortway / addOnly | NTCIP §2.5.2, §2.5.4 |
| Split mode | none, minVehRecall, maxVehRecall, pedRecall, maxVehPedRecall, omitted | NTCIP §2.5.9 |
| Preempt state | other, notActive, notActiveWithCall, entryStarted, trackService, dwell, linkActive, exitStarted, maxPresence | NTCIP §2.7.2 |
| Detector occupancy fault codes | 210 Max Presence, 211 No Activity, 212 Open loop, 213 Shorted, 214 Excessive Change, 216 Watchdog, 217 Erratic | NTCIP §2.3.5 |
| Tipe objek NTCIP | C (control, SET langsung), P (parameter), P2 (parameter, wajib transaksi), S (status) | NTCIP Annex A.1.1 |
| Hi-res event codes (Indiana/Purdue, resmi) | Fase: 0 Phase On; 1 Phase Begin Green; 2 Phase Check; 3 Phase Min Complete; 4 Phase Gap Out; 5 Phase Max Out; 6 Phase Force Off; 7 Phase Green Termination; 8 Phase Begin Yellow; 9 Phase End Yellow; 10 Phase Begin Red; 11 Phase End Red (parameter = Phase # 1–16). Pejalan kaki: 21 Ped Begin Walk; 22 Ped Begin Clearance; 23 Ped Begin Solid Don't Walk; 43 Phase Call Registered; 44 Phase Call Dropped; 45 Pedestrian Call. Detektor: 81 Detector Off; 82 Detector On (DET Channel #); 89 PedDetector Off; 90 PedDetector On. Preempt: 102 Preempt Call Input On; 104 Preempt Call Input Off; 105 Preempt Entry Started; 107 Preemption Begin Dwell; 111 Preemption Begin Exit (Preempt # 1–10). Koordinasi: 131 Coord Pattern Change (Pattern # 0–255); 132 Cycle Length Change (s); 133 Offset Length Change (s); 150 Coord cycle state change dengan parameter 0 Free / 1 In Step / 2 Transition-Add / 3 Transition-Subtract / 4 Transition-Dwell / 5 Local Zero / 6 Begin Pickup; 151 Coordinated phase yield (Phase #). | [Purdue 2012] `docs/sources/_teks_ekstraksi/Purdue_Indiana_HiRes_Data_Logger_Enumerations.txt`; R03 C.2 |
| SUMO state chars | r, y, g (permissive), G (protected), s, u (red+yellow), o, O | R03 B.1 |
| Tipe pendekat PKJI | P (terlindung) / O (terlawan) | PKJI Bab 5 |
| LOS simpang | A <5; B 5–15; C 15–25; D 25–40; E 40–60; F >60 det/kend | PM 96 Lamp. I |
| Kelas kendaraan prioritas | angkutan umum massal jalan, ambulans, pemadam, pimpinan lembaga negara, tamu negara | PM 76 Ps.7(4)a; UU Ps.134 |
| Level EVP | purple/red/orange (target 8/12/20 menit; faktor 1/1,5/2) | R04 A.18 |
| Tingkat keterlambatan bus | 4 level (TransLink); on-time x=0, y=3–5 menit | R06 A.7 |

## D. Antarmuka controller — Controller Abstraction Interface (CAI)

**Prinsip:** satu antarmuka internal; adaptor per protokol; kontrol real-time hanya lewat objek C; parameter lewat transaksi tervalidasi; heartbeat < `unitBackupTime`; fallback lokal adalah fitur, bukan bug (NTCIP §2.4.3).

| Operasi CAI | NTCIP-SNMP adapter | RS-232 vendor adapter | TraCI/SUMO adapter |
|---|---|---|---|
| readStatus (≤1 s) | GET `phaseStatusGroup*`, `ringStatus`, `coordCycleStatus`, `coordPatternStatus`, `unitControlStatus` (banyak OID per GET, Annex C.1) | polling protokol vendor; petakan ke bitmask yang sama; tandai unsupported | `getRedYellowGreenState`, `getPhase`, `getProgram`, detektor `getLastStepVehicleNumber`/occupancy |
| readHealth (10–60 s) | `unitAlarmStatus1/2`, `shortAlarmStatus`, `alarmGroupState`, `vehicleDetectorAlarms`, `port1Status` | status vendor (fault/flash/door) | status simulasi |
| readVolumeOccupancy | `volumeOccupancyTable` + `volumeOccupancySequence` (period `volumeOccupancyPeriod`) | jika ada | detektor E1/E2 output |
| selectPattern / free / flash / standby | SET `systemPatternControl` (1–253/254/255/0); `coordOperationalMode`=0 | perintah pilih program vendor | `setProgram`; NEMA `setNemaSplits`/`setNemaCycleLength`/`setNemaOffset` (berlaku setelah siklus selesai) |
| syncCycle | SET `systemSyncControl` | jika ada | `setNemaOffset` |
| hold / forceOff / omit / call (per fase, per ring) | SET `phaseControlGroup{Hold,ForceOff,PhaseOmit,PedOmit,VehCall,PedCall}`, `ringControlGroup*` | umumnya tidak ada → unsupported | `setPhase` ke fase kuning / `setPhaseDuration` / detektor virtual / `earlyTarget` |
| preempt on/off | SET `preemptControlState` | input fisik/relay | skenario EV |
| specialFunction | SET `specialFunctionOutputControl` | relay vendor | — |
| heartbeat | SET apa pun objek kontrol sistem lebih sering dari `unitBackupTime` | keep-alive vendor | — |
| beginTransaction / setParams / verify / commit | `dbCreateTransaction` (get→set transaction→set P/P2→set verify→poll→set normal), simpan `dbVerifyError`; validasi Annex B server-side dulu | download plan vendor (biasanya seluruh tabel) | `setCompleteRedYellowGreenDefinition` / tulis `.add.xml` |
| uploadBlock / downloadBlock | `ascBlockGetControl` + `ascBlockData` (OER, data ID 0x00–0x12) | backup file vendor | — |
| discoverCapabilities | baca `max*`, uji GET per grup → PRL | tabel kapabilitas manual | — |
| hiResLog pull | FTP/HTTP vendor logger (di luar NTCIP v02) | external logger (tanpa termination type) | `whetherOutputState=true` |

**Keamanan transport:** SNMPv3/TLS bila tersedia (ARC-IT); NEMA TS 8.

## E. Integrasi eksternal

| Mitra | Data masuk ke ITCS | Data keluar dari ITCS | Dasar hukum / catatan |
|---|---|---|---|
| **Ditlantas Polda Metro Jaya / NTMC (SIK LLAJ)** | daftar target/permintaan (opsional), instruksi operasional | event pelanggaran + bukti + pelat + waktu (ETLE); status/data lalu lintas real time; akses monitoring | UU Ps.246–247, 251, 272; PP 32 Ps.46; ITCS = penyedia bukti, bukan penindak |
| **Bapenda DKI** | status pajak per pelat (query) | agregat pelat terdeteksi per ruas | PP 32 Ps.16; Perda Ps.239; UU PDP; perjanjian kerja sama |
| **Dinas Lingkungan Hidup** | status uji emisi per pelat | agregat kepatuhan per ruas (target operasi) | Antara 5051249; PM 96 Lamp. II.H |
| **TransJakarta / Jak Lingko** | AVL posisi, ETA, headway, keterlambatan, status revenue, APC | log prioritas, waktu tempuh koridor | Pergub 68 Ps.10(6); PM 76 Ps.11; PRG-1/2/4 |
| **Damkar / AGD 119 / 112 (CAD)** | unit ditugaskan, rute, posisi, level | konfirmasi preempt, response time | PM 76 Ps.7(4)a, Ps.13; UU Ps.134 |
| **Jasa Marga / Hutama Karya** | kondisi gerbang/ramp | arus menuju gerbang | RPP h.11 (MoU sosialisasi) |
| **Jakarta Smart City / JAKI** | — | data & KPI publik, CCTV, status keluhan | UU Ps.250; Perda Ps.233; Pergub 68 Ps.11 |
| **BPTJ / Ditjen Hubdat** | persetujuan MRLL jalan nasional | laporan tahunan/efektivitas, kajian | PM 96 Ps.5(2), Lamp. III; PM 76 Ps.19, 22–24 |
| **CRM Pemprov** | tiket keluhan | status penanganan (SLA 3 jam) | Beritajakarta 145079 |
| **Forum LLAJ / Gubernur** | — | laporan MRLL, triwulanan | UU Ps.98; Pergub 68 Ps.15 |
| **Sumber probe (navigasi/ojol)** | trajektori agregat | — | perjanjian data; PDP |
| **CV/RSU (masa depan)** | BSM | SPaT/MAP (konversi dari NTCIP 1202) | TSPH hlm.245–247 |

## F. API internal (dari R03 D.4) dikelompokkan per tahap

Diselaraskan pada 2026-09-15 dengan tahapan kanonis `docs/planning/04` dan daftar API T1–T3 di `docs/planning/06` bagian 5. Pengelompokan lama (T1 MVP monitoring, T2 siap jual, T3 transisi adaptif, T4 setara ITCS) tidak berlaku lagi; perpindahan utamanya dicatat dalam kurung.

- **T1–T2 (satu simpang di laptop; API berbahasa Indonesia sesuai `06` §5):** `/simpang`, `/simpang/{id}/konfigurasi`, `/kamera`, `/rekaman`, `/vision/jobs`, `/hitungan`, `/hambatan-samping`, `/status-lampu`, `/antrian`, `/periode`, `/optimasi/run`, `/rekomendasi`, `/validasi-sumo`, `/manfaat`, `/laporan`, `/mutu-data`; volume per pendekat dan per arah (TMC, PHF) lewat `/hitungan` (T2); KPI PKJI per simpang `GET /kpi/{intersection}/pkji` (T1); audit perubahan konfigurasi dan rekomendasi `GET /audit` (T2).
- **T3 (pemantauan, controller baca-saja):** `/peristiwa`, `/kesehatan-kamera`, `/tiket`, `/laporan-wajib`, `/lembar-jadwal`; status controller baca-saja `GET /controllers/{id}/status`, `WS …/status/stream`, `/detectors/status` (bila Dishub mengizinkan; dulu T1); inventaris baca `GET /intersections, /controllers, /phases, /rings, /overlaps, /channels, /detectors, /patterns, /splits, /timebase/actions, /dayplans, /schedules` (dulu T1); Assets/Maintenance `/assets, /maintenance/schedules, /workorders` (dulu T1); Alerts `GET /alerts`, `POST /alerts/{id}/ack` untuk kamera dan lampu (dulu T1); Service requests `/service-requests` dan Public `GET /public/kpi`, `/public/intersections` (dulu T2); `POST /hires/ingest` dari SUMO dan status lampu kamera; ATSPM dari data kamera `/split-failure|approach-delay|arrivals-on-red|ped-delay|yra`; Sim `POST /sim/scenarios`, `POST /sim/runs`, `GET /sim/runs/{id}/atspm/...` untuk kalibrasi twin per simpang.
- **T4 (kendali adaptif terpadu):** Command `POST /controllers/{id}/commands/pattern|sync|special-function|unit-control|phase-control|ring-control|preempt` dengan heartbeat otomatis (dulu T2–T3); Plan `POST /controllers/{id}/transactions`, `PUT /transactions/{tid}/objects|blocks`, `POST …/verify|commit|abort`, `GET/POST /controllers/{id}/blocks/{dataID}` (dulu T2); inventaris tulis `PUT` untuk objek controller (dulu T1); ATSPM dari log controller `/phase-termination|split-monitor|pcd|preemption` (dulu T2–T3); `POST /priority/requests` (dulu T3); adaptif per simpang `/adaptive/groups`, `/adaptive/params`, `/adaptive/decisions` transparan; offset dasar `POST /corridors/{id}/green-wave`, `GET /corridors/{id}/summary`, `/compare?before&after` (dulu T2–T3); External ICD (ETLE evidence push, AVL ingest, CAD ingest; dulu T3) dan external command intake (ICM).
- **T5 (platform mobilitas kota):** `POST /corridors/{id}/link-pivot/run` (dulu T3); optimasi jaringan (max-pressure, perimeter control), oversaturation plans, objective per grup (dulu T4); RL advisor (`/advisor/recommendations`, shadow logs), digital twin kota dan prediksi, SPaT/MAP, ERP/KRE data feeds, API publik data terbuka, multi-tenant.

---

**Pointer ke detail:** R03 A (objek NTCIP per node, tabel pemetaan perintah), R03 B (SUMO tlLogic/NEMA/TraCI), R03 D (skema 20 entitas, adaptor, pipeline, API), R01 I.1–I.2 (entitas & parameter default), R00 H (SK 7234 spesifikasi controller/detektor/DIS), R06 F.4 (matriks integrasi), R05 G (dasar hukum data).
