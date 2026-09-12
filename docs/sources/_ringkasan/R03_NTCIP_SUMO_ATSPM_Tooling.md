# R03 — NTCIP 1202, SUMO, dan ATSPM: Catatan Studi dan Rancangan Referensi Tooling ITCS

Disusun: 2026-09-12 (studi bahan acuan untuk perancangan aplikasi Integrated/Intelligent Traffic Control System ala Dishub DKI Jakarta).
Bahasa: Indonesia, istilah teknis dipertahankan dalam bahasa Inggris.

## Sumber yang dipelajari dan kode rujukan

| Kode | Sumber | Catatan versi |
|---|---|---|
| [NTCIP] | `docs/sources/_teks_ekstraksi/NTCIP_1202_v02.19_Actuated_Signal_Controller_Objects.txt` — NTCIP 1202:2005 v02.19, *Object Definitions for Actuated Traffic Signal Controller (ASC) Units – version 02* (AASHTO/ITE/NEMA, Nov 2005) | Ini **versi 02 (2005)**, bukan v03 (2019). Konsekuensinya: tidak ada objek *signal priority* (TSP), tidak ada objek *high-resolution event log*, dan tidak ada objek ATC/SPaT. Lihat §A.16. |
| [ARC-IT] | `02_Panduan_Praktis_Standar/ARC-IT_NTCIP_1202_Standard_Page.md` | Halaman ringkas; hanya memuat daftar *communication solutions* yang memakai NTCIP 1202 (SNMPv1/v3 over TLS, Kafka/AMQP/MQTT/DDS untuk CVRSE). |
| [SUMO-TL] | `06_Simulasi_Tools_OpenSource/SUMO_Docs_Traffic_Lights.md` (+ blok kode dari `.html`) | Dokumentasi resmi SUMO “Traffic Lights”. File `.md` kehilangan nama atribut/param; nama diambil dari blok kode di `.html`. |
| [SUMO-NEMA] | `06_Simulasi_Tools_OpenSource/SUMO_Docs_NEMA_Phases.md` (+ `.html`) | “Traffic Lights with NEMA Phases”. |
| [SUMO-TraCI] | `06_Simulasi_Tools_OpenSource/SUMO_Docs_TraCI4Traffic_Lights.md` (+ `.html`) | Tutorial TraCI4Traffic Lights. |
| [Genders2019] | `docs/sources/_teks_ekstraksi/arXiv_1909.00395_Open_Source_Framework_Adaptive_TSC_sumolights.txt` — Genders & Razavi, *An Open-Source Framework for Adaptive Traffic Signal Control* (arXiv 1909.00395) | Framework `sumolights`. |
| [Pan2023] | `docs/sources/_teks_ekstraksi/arXiv_2308.14295_Traffic_Light_Control_RL_SUMO.txt` — Pan, *Traffic Light Control with Reinforcement Learning* (arXiv 2308.14295) | DQN dengan *phase gate* & *memory palace*. |
| [HOP-20-002] | `docs/sources/_teks_ekstraksi/FHWA_HOP-20-002_...ATSPM_2020.txt` — FHWA-HOP-20-002 (Mar 2020, 64 hlm.) | Laporan *outreach* EDC-4; berisi *use cases* dan definisi metrik tingkat praktisi. |
| [NCDOT] | `docs/sources/_teks_ekstraksi/NCDOT_Guide_on_ATSPM.txt` — Kittelson/ITRE untuk NCDOT (Mar 2019) | Panduan agensi; Appendix A = 13 metrik, Appendix B = kebutuhan detektor. |
| [EDC4-FS] | `docs/sources/_teks_ekstraksi/FHWA_EDC4_ATSPM_Factsheet.txt` — FHWA-16-CAI-014 | Lembar fakta 2 halaman. |

Catatan kejujuran sumber: hal-hal yang **tidak** ada di dokumen ditandai eksplisit dengan “[tidak ada di dokumen]”. Pengetahuan umum yang saya tambahkan untuk melengkapi (mis. angka kode enumerasi Indiana) ditandai “[di luar dokumen — verifikasi]”.

---

## 0. Ringkasan eksekutif

1. **NTCIP 1202 adalah kamus objek (MIB) untuk controller sinyal aktuasi**, diakses lewat SNMP GET/SET (atau STMP untuk objek dinamis dan *block objects* yang dikodekan OER). Objek dikelompokkan per node: `phase`, `detector`, `unit`, `coord`, `timebaseAsc`, `preempt`, `ring`, `channel`, `overlap`, `ts2port1`, `ascBlock` [NTCIP §2.1–2.12].
2. **Central system mengendalikan controller melalui sejumlah kecil objek kontrol tipe “C”**: `systemPatternControl` (pilih pattern/free/flash), `systemSyncControl` (sinkronisasi cycle), `phaseControlGroup{PhaseOmit,PedOmit,Hold,ForceOff,VehCall,PedCall}`, `ringControlGroup{StopTime,ForceOff,Max2,MaxInhibit,PedRecycle,RedRest,OmitRedClear}`, `preemptControlState`, `specialFunctionOutputControl`, `unitControl`. Semua tunduk pada *backup timer* (`unitBackupTime`): jika central berhenti menulis, controller kembali ke mode lokal [NTCIP §2.4.3, §2.5.14–15, §2.2.5, §2.8.5, §2.7.3].
3. **Status dibaca sebagai bitmask 8-fase per grup** (`phaseStatusGroup{Reds,Yellows,Greens,Walks,PedClears,DontWalks,VehCalls,PedCalls,PhaseOns,PhaseNexts}`) ditambah `ringStatus` (alasan terminasi: Gap Out/Max Out/Force Off dan *coded status* Min Green/Extension/Maximum/Green Rest/Yellow/Red…), `coordPatternStatus`, `coordCycleStatus`, `coordSyncStatus`, `localFreeStatus`, `unitControlStatus`, `unitFlashStatus`, `unitAlarmStatus1/2`, `shortAlarmStatus`, `vehicleDetectorStatusGroup{Active,Alarms}`, `preemptState` [NTCIP §2.2.4, §2.8.6, §2.5.10–13, §2.4.5–9, §2.3.4, §2.7.2].
4. **Parameter database controller (tipe “P2”) hanya boleh diubah dalam transaksi** `dbCreateTransaction` (NTCIP 1201) yang diakhiri *consistency check* Annex B; *block objects* (`ascBlockData`, OER) memungkinkan *upload/download* seluruh tabel sekaligus [NTCIP Annex C.4–C.5, §3].
5. **SUMO** mendefinisikan program lampu sebagai `tlLogic` dengan daftar `phase` (durasi + *state string* per *link index*); tersedia tipe `static`, `actuated` (gap-based, dengan *custom conditions*), `delay_based`, dan `NEMA` (dual-ring/barrier, coordinated, dengan `whetherOutputState` untuk keluaran ATSPM). TraCI memberi akses baca/tulis fase, state, program, dan detektor [SUMO-TL; SUMO-NEMA; SUMO-TraCI].
6. **sumolights** membuktikan bahwa *Max-pressure* (heuristik tanpa pembelajaran) mengungguli DQN dan DDPG pada jaringan uji dua simpang setelah *hyperparameter tuning*; SOTL terburuk; controller berbasis pembelajaran sangat sensitif terhadap hyperparameter [Genders2019 §IV–V].
7. **ATSPM** dibangun dari *high-resolution controller event log* (resolusi 0,1 s, kode enumerasi Indiana/Purdue) + detektor; lima komponen: hi-res controller, komunikasi, server, software, deteksi (opsional) [HOP-20-002 p.9; NCDOT §4].
8. **Metrik inti** dan aturan hitungnya: Purdue Phase Termination (gap/max/force-off/skip/ped), Split Monitor, Purdue Coordination Diagram (arrivals on green, platoon ratio), Purdue Split Failure (GOR & ROR5 ≥ 80 %), Approach Delay, Arrivals on Red, Turning Movement Counts, Approach Volume (PHF/K/D), Pedestrian Delay, Preemption Details, Approach Speed, Yellow & Red Actuations, Purdue Link Pivot (optimasi offset koridor), Watchdog (ambang alarm) [NCDOT App. A; HOP-20-002 p.20–27].
9. **Kebutuhan detektor menentukan metrik yang bisa dihasilkan**: tanpa detektor tambahan → phase termination, split monitor, ped delay, preemption; *advance detection* (350–400 ft sebelum antrian) → PCD, AoR, approach delay, link pivot; *stop-bar presence* → split failure; *lane-by-lane count* → TMC/approach volume; detektor kecepatan/past-stop-bar → speed, YRA [NCDOT App. B, Exhibit B-1].
10. **Rancangan ITCS**: model data yang selaras NTCIP (phase/ring/sequence/pattern/split/action/preempt/detector/channel/overlap), *adaptor protokol* berlapis (NTCIP-SNMP, vendor RS-232, TraCI), SUMO NEMA sebagai *digital twin* untuk SIL/HIL, dan *pipeline* ATSPM sebagai modul KPI (§D).

---

## A. NTCIP 1202 v02.19 — Object Definitions for ASC

### A.1 Kedudukan dan arsitektur akses

- **Tujuan**: “The messaging between Transportation Management and Actuated Signal Controllers is accomplished by using the NTCIP Application Layer services to convey requests to access or modify values stored in a given device; these values are referred to as objects.” [NTCIP §1.1].
- **Format definisi**: objek didefinisikan dengan makro `OBJECT-TYPE` RFC 1212 (SMI RFC 1155); teks Clause 2.1 sampai akhir Section 2 “constitutes the NTCIP Standard ASC MIB” [NTCIP §2 pembuka].
- **Protokol**: SNMP (RFC 1157) untuk GET/SET objek; STMP (NTCIP 1103) untuk objek dinamis; OER (NTCIP 1102) untuk *block objects*. Referensi normatif: NTCIP 1201 (Global Object Definitions), NTCIP 1102 (OER), NTCIP 1103 (TMP), NEMA TS 2-1998 [NTCIP §1.2].
- **Pohon OID**: `asc OBJECT IDENTIFIER ::= { devices 1 }` dengan `devices` diimpor dari TMIB-II (NTCIP 1201). Sub-node: `phase ::= {asc 1}`, `detector ::= {asc 2}`, `unit ::= {asc 3}`, `coord ::= {asc 4}`, `timebaseAsc ::= {asc 5}`, `preempt ::= {asc 6}`, `ring ::= {asc 7}`, `channel ::= {asc 8}`, `overlap ::= {asc 9}`, `ts2port1 ::= {asc 10}`, `ascBlock ::= {asc 11}` (urutan mengikuti clause 2.2–2.12). Blok proprietary vendor memakai *Private Node Number* NEMA `1.3.6.1.4.1.1206.3.PNN` [NTCIP §2.1, §3.1].
- **Pola tabel**: setiap tabel punya objek `max…` (jumlah baris, *read-only*), `…Table` (SEQUENCE OF), `…Entry`, dan kolom pertama `…Number` sebagai indeks; “All management applications shall reference the specific device MIB as provided by the device manufacturer for support and constraints (sub-ranges)” [NTCIP §2 pembuka].
- **Bitmask grup-8**: banyak status/kontrol dikemas per 8 fase/ring/detektor/kanal dalam satu oktet: Bit 7 = nomor `group*8`, Bit 6 = `group*8-1`, … Bit 0 = `group*8-7` [NTCIP §2.2.4]. `maxPhaseGroups = TRUNCATE[(maxPhases+7)/8]` [NTCIP §2.2.3].
- **Tipe objek (Annex A.1.1)**: **C** = *Control Object* — SET tidak boleh ditunda oleh `dbCreateTransaction`; **P** = *Parameter Object* — SET via transaksi opsional (device wajib mendukung SET normal dan via transaksi); **P2** = *Parameter Object* — SET **wajib** lewat `dbCreateTransaction`, SET SNMP normal tidak boleh diizinkan; **S** = *Status/Information* — *read-only* [NTCIP Annex A.1.1].

### A.2 Peta node MIB dan isi ringkas

| Node | Clause | Tabel/objek utama | Fungsi |
|---|---|---|---|
| phase | 2.2 | `maxPhases`, `phaseTable`, `phaseStatusGroupTable`, `phaseControlGroupTable` | Parameter waktu fase, status output/panggilan, kontrol jarak jauh per fase |
| detector | 2.3 | `vehicleDetectorTable`, `vehicleDetectorStatusGroupTable`, `volumeOccupancyReport`, `pedestrianDetectorTable` | Konfigurasi detektor, diagnostik, status aktif/alarm, laporan volume/okupansi |
| unit | 2.4 | `unitStartUpFlash`, `unitBackupTime`, `unitControlStatus`, `unitFlashStatus`, `unitAlarmStatus1/2`, `shortAlarmStatus`, `unitControl`, `alarmGroupTable`, `specialFunctionOutputTable` | Status unit, alarm, kontrol unit, output fungsi khusus |
| coord | 2.5 | `coordOperationalMode`, `coordCorrectionMode`, `coordMaximumMode`, `coordForceMode`, `patternTable`, `splitTable`, `coordPatternStatus`, `localFreeStatus`, `coordCycleStatus`, `coordSyncStatus`, `systemPatternControl`, `systemSyncControl` | Koordinasi: pattern (cycle/offset/split/sequence), status, perintah sistem |
| timebaseAsc | 2.6 | `timebaseAscPatternSync`, `timebaseAscActionTable`, `timebaseAscActionStatus` | Aksi berbasis waktu (TOD) yang dipetakan ke *day plan* NTCIP 1201 |
| preempt | 2.7 | `preemptTable`, `preemptControlTable` | Parameter preemption (kereta/darurat) dan aktivasi jarak jauh |
| ring | 2.8 | `maxRings`, `sequenceTable`, `ringControlGroupTable`, `ringStatusTable` | Urutan fase per ring, kontrol per ring, alasan terminasi |
| channel | 2.9 | `channelTable`, `channelStatusGroupTable` | Pemetaan output fisik (kanal) ke fase/overlap, status R/Y/G kanal |
| overlap | 2.10 | `overlapTable`, `overlapStatusGroupTable` | Overlap (included/modifier phases, trailing green/yellow/red) |
| ts2port1 | 2.11 | `port1Table` | Perangkat SDLC Port 1 (NEMA TS 2) |
| ascBlock | 2.12 | `ascBlockGetControl`, `ascBlockData`, `ascBlockErrorStatus` | Upload/download blok data OER (Section 3) |

### A.3 Phase Table (`phaseTable`, {phase 2}) — field kunci

Semua *read-write* kecuali `phaseNumber` (read-only, 1..255) [NTCIP §2.2.2]:

| Objek | Satuan / rentang | Arti (ringkasan definisi) |
|---|---|---|
| `phaseWalk` | s (0..255) | Lama indikasi Walk. |
| `phasePedestrianClear` | s | Durasi Pedestrian Clearance / flashing Don't Walk. |
| `phaseMinimumGreen` | s (TS2: 1..255) | Bagian hijau pertama yang ditimer; mempertimbangkan penyimpanan kendaraan antara zona deteksi dan stop line. |
| `phasePassage` | 0,1 s (0..25,5) | *Passage/Vehicle Extension*: bagian hijau yang dapat diperpanjang; fase tetap di *extensible portion* selama passage timer belum habis; timer di-reset setiap aktuasi. |
| `phaseMaximum1`, `phaseMaximum2` | s | Batas maksimum hijau saat ada *serviceable conflicting call*; Max2 dapat dipilih via ring control/ input eksternal. |
| `phaseYellowChange` | 0,1 s (TS2: 3..25,5) | Interval kuning setelah hijau. |
| `phaseRedClear` | 0,1 s | Interval *red clearance* setelah kuning. |
| `phaseRedRevert` | 0,1 s | Minimum merah setelah kuning sebelum hijau lagi pada grup output yang sama; `unitRedRevert` adalah batas bawah global. |
| `phaseAddedInitial`, `phaseMaximumInitial` | 0,1 s/aktuasi; s | *Volume-density variable initial*: initial = min(addedInitial × jumlah aktuasi saat kuning/merah, maxInitial), tidak kurang dari Minimum Green. |
| `phaseTimeBeforeReduction`, `phaseCarsBeforeReduction`, `phaseTimeToReduce`, `phaseReduceBy`, `phaseMinimumGap` | s; kendaraan; s; 0,1 s; 0,1 s | *Gap reduction*: setelah TBR atau CBR terpenuhi (mana lebih dulu), *allowable gap* diturunkan linier dari Passage ke Minimum Gap selama TimeToReduce (atau bertahap `phaseReduceBy`). |
| `phaseDynamicMaxLimit`, `phaseDynamicMaxStep` | s; 0,1 s | *Dynamic max*: setelah dua kali *max out* berturut, running max naik satu step; setelah dua kali *gap out* berturut turun satu step; dibatasi oleh normal max dan dynamicMaxLimit. |
| `phaseStartup` | enum {other, phaseNotOn, greenWalk, greenNoWalk, yellowChange, redClear…} | Keadaan fase saat *power-up/external start*. |
| `phaseOptions` | bitmask 16-bit | Bit 0 Enabled Phase; Bit 1 Automatic Flash Entry; Bit 2 Automatic Flash Exit; Bit 3 Non-Actuated 1; Bit 4 Non-Actuated 2; Bit 5 Non-Lock Detector Memory; Bit 6 Min Vehicle Recall; Bit 7 Max Vehicle Recall; Bit 8 Ped Recall; Bit 9 Soft Vehicle Recall; Bit 10 Dual Entry; Bit 11 Simultaneous Gap Disable; Bit 12 Guaranteed Passage; Bit 13 Actuated Rest In Walk; Bit 14 Conditional Service Enable; Bit 15 AddedInitialCalculation (max vs sum). |
| `phaseRing` | 1..maxRings (0 = disabled) | Ring tempat fase berada. |
| `phaseConcurrency` | OCTET STRING (daftar nomor fase) | Fase yang boleh berjalan bersamaan; fase dalam ring yang sama **tidak** boleh konkuren. |

### A.4 Phase Status Group dan Phase Control Group

- `phaseStatusGroupTable` ({phase 4}, read-only): `Reds`, `Yellows`, `Greens`, `DontWalks`, `PedClears`, `Walks`, `VehCalls`, `PedCalls`, `PhaseOns` (fase ON selama Green, Yellow, Red Clearance; boleh true saat Red Dwell), `PhaseNexts` (fase yang *committed* menjadi berikutnya; keputusan diambil pada akhir hijau fase yang berakhir) [NTCIP §2.2.4].
- `phaseControlGroupTable` ({phase 5}, read-write, tipe C): `PhaseOmit` (System Phase Omit), `PedOmit`, `Hold` (System Phase Hold), `ForceOff` (bit di-reset otomatis ke 0 saat hijau fase berakhir), `VehCall` (menempatkan panggilan kendaraan), `PedCall` [NTCIP §2.2.5].

### A.5 Detector node

- `vehicleDetectorTable` ({detector 2}) per detektor: `vehicleDetectorOptions` (Bit 7 Call, 6 Queue, 5 AddedInitial, 4 Passage, 3 Red Lock Call, 2 Yellow Lock Call, 1 Occupancy Detector, 0 Volume Detector), `CallPhase` (fase yang dipanggil; 0 = nonaktif), `SwitchPhase` (aktuasi dialihkan ke fase lain saat fase asal kuning/merah dan switch phase hijau), `Delay` (0,1 s; hanya saat fase tidak hijau), `Extend` (0,1 s; hanya saat hijau), `QueueLimit` (s), diagnostik `NoActivity` (menit), `MaxPresence` (menit), `ErraticCounts` (cpm), `FailTime` (s; saat *failed*, panggilan konstan pada fase saat non-hijau dan dipertahankan `FailTime` detik setelah hijau mulai), `Alarms` (Bit 7 Other, 4 Configuration, 3 Communications, …), `ReportedAlarms` (alarm dari kartu detektor loop: Excessive Change, dst.), `Reset` [NTCIP §2.3.2].
- `vehicleDetectorStatusGroupTable` ({detector 4}): `Active` (bitmask ON/OFF deteksi *real-time*), `Alarms` [NTCIP §2.3.4].
- `volumeOccupancyReport` ({detector 5}): `volumeOccupancySequence` (0..255, naik tiap periode; deteksi laporan hilang/ganda), `volumeOccupancyPeriod` (s, read-write), `activeVolumeOccupancyDetectors`, `volumeOccupancyTable` dengan `detectorVolume` (0..254; 255 = overflow) dan `detectorOccupancy` (0..200 = okupansi dalam 0,5 %; 210 Max Presence Fault, 211 No Activity, 212 Open loop, 213 Shorted loop, 214 Excessive Change, 216 Watchdog, 217 Erratic Output) [NTCIP §2.3.5].
- `pedestrianDetectorTable` ({detector 7}): `CallPhase`, `NoActivity`, `MaxPresence`, `ErraticCounts`, `Alarms` [NTCIP §2.3.7].
- Implikasi: volume/okupansi NTCIP adalah **agregat per periode** (bukan *event log* per aktuasi). Untuk ATSPM tetap dibutuhkan *hi-res logger* (lihat §C.2).

### A.6 Unit node

- `unitStartUpFlash` (s), `unitAutoPedestrianClear`, **`unitBackupTime`** (0..65535 s): “When any of the defined system control parameters is SET, the backup timer is reset… If the unitBackupTime interval expires without a SET operation to any of the system control parameters, then the CU shall revert to Backup Mode” [NTCIP §2.4.3]. `unitRedRevert` [§2.4.4].
- `unitControlStatus` enum {other, systemControl, systemStandby, backupMode, manual, timebase, interconnect…} [§2.4.5]; `unitFlashStatus` {notFlash, automatic, localManual, faultMonitor, mmu, startup, preempt…} [§2.4.6].
- `unitAlarmStatus2`: Bit 5 Offset Transitioning, Bit 4 Stop Time, Bit 3 External Start… [§2.4.7]. `unitAlarmStatus1`: Bit 7 CoordActive, 6 Local Free, 5 Local Flash, 4 MMU Flash, 3 Cycle Fail, 2 Coord Fail, 1 Coord Fault, 0 Cycle Fault [§2.4.8]. `shortAlarmStatus`: Bit 7 Critical Alarm (Stop Time), 6 Non-Critical Alarm, 5 Detector Fault, 4 Coordination Alarm (CU tidak menjalankan pattern yang dipanggil), … [§2.4.9].
- `unitControl` (tipe C): Bit 7 Dimming Enable, 6 Interconnect, 5 Walk Rest Modifier, 4 Call to Non-Actuated 2, 3 Call to Non-Actuated 1, 2 External Minimum Recall [§2.4.10].
- `alarmGroupTable` (status 8 input alarm fisik per baris) [§2.4.12]; `specialFunctionOutputTable`: `Control` (0/1; di-reset ke 0 saat Backup Mode; menulisnya me-reset backup timer) dan `Status` [§2.4.14]. Objek lama `specialFunctionOutputState` *deprecated* [Annex D].

### A.7 Coordination node

- `coordOperationalMode` (0 Automatic; 1–253 Manual Pattern; 254 Manual Free; 255 Manual Flash) [§2.5.1].
- `coordCorrectionMode` {dwell, shortway (smooth), addOnly} — cara mengejar offset baru [§2.5.2]; `coordMaximumMode` {maximum1, maximum2, maxInhibit} [§2.5.3]; `coordForceMode` {floating (fase non-koordinasi dibatasi split-nya, sisa waktu kembali ke fase koordinasi), fixed (force-off di posisi tetap dalam siklus, sisa waktu ke fase berikutnya)} [§2.5.4].
- `patternTableType` {patterns, offset3 (plan = 3 baris dengan offset berbeda), offset5} [§2.5.6].
- **`patternTable`** ({coord 7}, 1..253): `patternCycleTime` (s; TS2 30..255; jika tidak cukup untuk kebutuhan minimum semua fase → Free, set bit Local Free/Local Override), `patternOffsetTime` (s; local time zero tertinggal dari system time zero; ≥ cycle → Free), `patternSplitNumber` (indeks ke `splitTable`), `patternSequenceNumber` (indeks ke `sequenceTable`) [§2.5.7].
- **`splitTable`** ({coord 9}) diindeks (`splitNumber`, `splitPhase`): `splitTime` (s; waktu yang boleh diterima fase sebelum force-off, termasuk clearance), `splitMode` {none, minimumVehicleRecall, maximumVehicleRecall, pedestrianRecall, maximumVehicleAndPedestrianRecall, phaseOmitted}, `splitCoordPhase` (1 = fase koordinasi) [§2.5.9].
- Status: `coordPatternStatus` (1–253 pattern; 254 Free; 255 Flash), `localFreeStatus` {notFree, commandFree, transitionFree, inputFree, coordFree, badPlan, badCycleTime, splitOverrun, invalidOffset, failed}, `coordCycleStatus` (0..510 s; hitung mundur dari cycle ke 0), `coordSyncStatus` (0..510 s; waktu sejak *system reference point*) [§2.5.10–13].
- **Perintah sistem**: `systemPatternControl` (0 Standby = sistem melepas kendali; 1–253 pattern; 254 Free; 255 Flash; pattern tak valid → Free; di-reset ke 0 saat Backup Mode; menulisnya me-reset backup timer) dan `systemSyncControl` (0–254 = posisi saat ini dalam siklus sistem → menetapkan waktu ke *reference point* berikutnya; 255 = referensi ke Time Base lokal; akurasi 0,1 s) [§2.5.14–15].
- Definisi istilah [§1.3]: *offset* = hubungan waktu (detik) antara titik awal siklus lokal dan referensi sistem; *pattern* = himpunan unik parameter koordinasi (cycle, split, offset, sequence); *split* = porsi siklus yang dialokasikan ke suatu fase.

### A.8 Time base node

- `timebaseAscPatternSync` (menit lewat tengah malam; 65535 = gunakan waktu aksi sebagai referensi sinkron) [§2.6.1].
- `timebaseAscActionTable` ({timebaseAsc 3}): tiap baris = aksi yang dirujuk *day plan* NTCIP 1201: `timebaseAscPattern` (0 = tidak memilih pattern, melepas kendali ke entitas prioritas lebih rendah mis. interconnect), `timebaseAscAuxillaryFunction` (bit Aux 1–3, dimming), `timebaseAscSpecialFunction` (bit SF 1–8) [§2.6.3]. `timebaseAscActionStatus` = baris aksi yang sedang aktif [§2.6.4].
- Jadwal kalender (schedule/day plan) sendiri ada di NTCIP 1201 dan tersedia sebagai blok `AscScheduleBlock` (0x0B) dan `AscDayPlanBlock` (0x0C) [§3.13–3.14].

### A.9 Preempt node

- `preemptTable` ({preempt 2}) per preempt: `preemptControl` (bitmask; Bit 3 Flash Dwell, bit 2 mengubah prioritas relatif), `preemptLink` (rangkaikan ke preempt prioritas lebih tinggi), `preemptDelay` (s, 0–600; input harus aktif selama ini sebelum urutan dimulai), `preemptMinimumDuration`, `preemptMinimumGreen`, `preemptMinimumWalk`, `preemptEnterPedClear`, `preemptEnterYellowChange`, `preemptEnterRedClear` (batas minimum yang harus dihormati saat transisi masuk), `preemptTrackGreen` (+ `TrackYellowChange`, `TrackRedClear`; 0 = tanpa *track clearance*), `preemptDwellGreen` (min dwell), `preemptMaximumPresence` (s; setelah ini panggilan dianggap tidak valid), daftar fase/overlap sebagai OCTET STRING: `TrackPhase`, `DwellPhase`, `DwellPed`, `ExitPhase`, `TrackOverlap`, `DwellOverlap`, `CyclingPhase`, `CyclingPed`, `CyclingOverlap` [§2.7.2].
- `preemptState` (read-only) {other, notActive, notActiveWithCall, entryStarted, trackService, dwell, linkActive, exitStarted, maxPresence} [§2.7.2].
- `preemptControlTable` → `preemptControlState` (0/1, tipe C): 1 = aktifkan preempt dari jarak jauh, aktif selama objek atau input fisik ON [§2.7.3].
- Konsistensi (Annex B): fase dalam Track/Dwell/Exit harus bisa berjalan konkuren, tidak dalam ring yang sama, tidak duplikat, tidak *disabled*; overlap dwell harus punya *included phase* aktif.

### A.10 Ring node

- `maxRings`, `maxSequences`; **`sequenceTable`** diindeks (`sequenceNumber`, `sequenceRingNumber`) dengan `sequenceData` = OCTET STRING urutan nomor fase dalam ring [§2.8.3].
- **`ringControlGroupTable`** (tipe C, bitmask per ring): `StopTime`, `ForceOff` (mengakhiri fase aktif via force-off), `Max2`, `MaxInhibit`, `PedRecycle`, `RedRest`, `OmitRedClear` [§2.8.5].
- **`ringStatus`** (read-only per ring): Bit 5 Force Off, Bit 4 Max Out, Bit 3 Gap Out (alasan terminasi fase aktif); Bit 2..0 *coded status*: 0 Min Green, 1 Extension, 2 Maximum, 3 Green Rest, 4 Yellow Change, (5 Red Clearance, 6 Red Rest, 7 Undefined — kelanjutan tabel terpotong pada ekstraksi) [§2.8.6].
- Annex B: tiap fase muncul sekali per sequence; ring fase sesuai `sequenceRingNumber`; semua fase ring harus dimasukkan; urutan *concurrency group* harus sama di semua ring; contoh dual-ring standar `01-02-03-04` / `05-06-07-08` [Annex B.1].

### A.11 Channel, Overlap, TS2 Port 1

- `channelTable`: `channelControlSource` (nomor fase atau overlap A=1, B=2…), `channelControlType` {phaseVehicle, phasePedestrian, overlap}, `channelFlash` (Bit 3 alternate ½ Hz, Bit 2 flash red, Bit 1 flash yellow), `channelDim`; `channelStatusGroup{Reds,Yellows,Greens}` [§2.9].
- `overlapTable`: `overlapType` {normal, minusGreenYellow}, `overlapIncludedPhases`, `overlapModifierPhases`, `overlapTrailGreen/Yellow/Red`; `overlapStatusGroup{Reds,Yellows,Greens}` [§2.10]. Contoh urutan overlap ada di Annex C.6.
- `port1Table` (SDLC TS 2): `port1DevicePresent`, `port1Frame40Enable`, `port1Status` {online = ≥5 dari 10 respons terakhir benar, responseFault}, `port1FaultFrame` [§2.11].

### A.12 Block objects (Section 2.12 dan Section 3)

- `ascBlockGetControl` (OCTET STRING 2..12, OER): parameter referensi *upload* — `ascBlockDataType`, `ascBlockDataID`, `ascBlockIndex1`, `ascBlockQuantity1` (dan index/quantity ke-2 bila perlu) [§2.12.1].
- `ascBlockData` (OCTET STRING 2..484): “An OER encoded string used for uploading and downloading ASC parameters… A SET on this object shall require the use of 'dbCreateTransaction'” [§2.12.2]. `ascBlockErrorStatus` menunjuk elemen yang menyebabkan `badValue` [§2.12.3].
- Data ID standar (`dataType` 0x00): 0x00 AscPhaseBlock, 0x01 AscVehDetectorBlock, 0x02 AscPedDetectorBlock, 0x03 AscPatternBlock, 0x04 AscSplitBlock, 0x05 AscTimebaseBlock, 0x06 AscPreemptBlock, 0x07 AscSequenceBlock, 0x08 AscChannelBlock, 0x09 AscOverlapBlock, 0x0A AscPort1Block, 0x0B AscScheduleBlock, 0x0C AscDayPlanBlock, 0x0D AscEventConfigBlock, 0x0E AscEventClassBlock, 0x0F/0x10/0x11 DynObj Config/Owner/Status (GET/SET via STMP → genError), 0x12 AscMiscBlock; 0x13–0xFF reserved [§3.1]. (Catatan: pada ekstraksi teks kolom dataID untuk baris 0x00–0x0A bergeser; pemetaan di atas mengikuti urutan Section 3.2–3.12 yang konsisten dengan contoh Phase Block “00 00 02 02 …” = standard block, phase data, mulai phase 2, 2 fase [§3.2.1].)
- Struktur `AscPhaseBlock ::= SEQUENCE { dataType, dataID, index1, quantity1, data SEQUENCE OF AscPhaseBlockData }` dengan tiap elemen `phaseWalk.x … phaseConcurrency.x` [§3.2].

### A.13 Conformance groups (Annex A)

Status M/O per grup [Annex A.2]: **Mandatory** — Phase (2.2), Detector (2.3), Configuration (NTCIP 1201 2.2), Report (1201 2.3), Security (rfc1213). **Optional** — Volume Occupancy Report, Unit, Special Function, Coordination, Time Base, Preempt, Ring, Channel, Overlap, TS2 Port 1, Block Object, PMPP, IP/TCP/UDP/Ethernet, dsb. Di dalam grup, tiap objek diberi tipe (C/P/P2/S), status (M/O), rentang yang diizinkan, dan kolom *Supported Values* untuk diisi vendor (PICS/PRL) — contoh Phase Conformance Group: `maxPhases` S/M, `phaseWalk` P/M, `phasePassage` P/M, dst. [Annex A.3]. Konsekuensi praktis: **spesifikasi pengadaan controller harus menyebut grup mana yang wajib** (Coordination, Time Base, Preempt, Ring, Block Object) karena standar hanya mewajibkan Phase dan Detector.

### A.14 Consistency checks (Annex B)

Aturan normatif yang dijalankan controller saat `dbCreateTransaction = verify`; pesan ke `dbVerifyError`, mis. “PHASE xx CONCURRENCY FAULT”, “PHASE xx MUTUAL FAULT”, “SEQ xx SAME PHASE FAULT”, “SEQ xx RING # FAULT”, “SEQ xx RING # PHS OMITTED”, “SEQ xx RING SEQ FAULT”, “SEQ xx CG SEQ FAULT”, “SEQ xx SEQUENCING FAULT”, “START PHASE CG FAULT”, “PE DWELL PHASE RING FAULT”, “OVLP INC PHASE MULTI FAULT”, … dan “NO VERIFICATION ERROR” bila bersih [Annex B.1]. Vendor boleh menambah cek sendiri tapi harus memakai mekanisme pelaporan yang sama [Annex B.2]. Untuk ITCS, aturan-aturan ini sebaiknya **direplikasi sebagai validasi sisi server** sebelum mengunduh plan ke controller.

### A.15 Bagaimana central system membaca status dan mengirim perintah

Use case Annex C (informatif tetapi “Any ASC claiming conformance … shall support the exchanges as shown”):

| Use case | Urutan pesan |
|---|---|
| C.1 GET objek C/P/S | `get(objects)` → `response = data`; boleh banyak objek sekaligus. |
| C.2 GET block | `set(ascBlockGetControl)` → `get(ascBlockData)`; ulangi per blok. |
| C.3 SET objek C/P | `set(objects)` langsung diimplementasikan. |
| C.4 SET objek P2 | `get(dbCreateTransaction)` sampai ≠ verify → `set(dbCreateTransaction=transaction)` (mulai buffering) → `set(objek P/P2)` berulang → `set(dbCreateTransaction=verify)` (controller menjalankan Annex B) → `get(dbCreateTransaction)` sampai ≠ verify → `set(dbCreateTransaction=normal)` → implementasi bila `Done`. |
| C.5 SET block | Sama seperti C.4 dengan `set(ascBlockData)`. |

Pemetaan perintah operasional ITCS → objek NTCIP:

| Perintah TMC | Objek | Tipe | Keterangan |
|---|---|---|---|
| Pilih pattern / plan (mis. green wave sore) | `systemPatternControl` = 1..253 | C | 254 Free, 255 Flash, 0 Standby. Perlu `coordOperationalMode` = 0 (Automatic) agar sumber sistem dihormati. |
| Sinkronkan siklus koridor | `systemSyncControl` = posisi dalam siklus | C | 255 = kembali ke time base lokal. |
| Ubah cycle/offset/split | `patternCycleTime`, `patternOffsetTime`, `splitTime`, `splitMode`, `splitCoordPhase` | P/P2 | Lewat transaksi; verifikasi Annex B. |
| Hold fase (mis. perpanjang hijau bus) | `phaseControlGroupHold` bit fase | C | Selama hold, fase tidak diakhiri. |
| Force-off fase | `phaseControlGroupForceOff` atau `ringControlGroupForceOff` | C | Bit di-reset saat hijau berakhir. |
| Omit fase / ped | `phaseControlGroupPhaseOmit`, `PedOmit` | C | |
| Tempatkan panggilan (deteksi kamera/AI) | `phaseControlGroupVehCall`, `PedCall` | C | Cara “menyuntikkan” deteksi virtual dari central. |
| Stop time / Max2 / MaxInhibit / Red Rest / Ped Recycle / Omit Red Clear | `ringControlGroup…` | C | Per ring. |
| Preempt darurat dari central | `preemptControlState` = 1 | C | Setara input fisik. |
| Output fungsi khusus (mis. VMS/rambu) | `specialFunctionOutputControl` | C | Reset saat Backup Mode. |
| Heartbeat/keep-alive | SET apa pun pada objek kontrol sistem | — | Harus lebih sering dari `unitBackupTime`, kalau tidak controller *revert to Backup Mode* [§2.4.3]. |
| Baca status lampu real-time | `phaseStatusGroup*`, `channelStatusGroup*`, `overlapStatusGroup*` | S | Poll berkala (bitmask kompak). |
| Baca posisi siklus & mode | `coordPatternStatus`, `coordCycleStatus`, `coordSyncStatus`, `localFreeStatus`, `unitControlStatus`, `timebaseAscActionStatus` | S | |
| Baca kesehatan | `unitAlarmStatus1/2`, `shortAlarmStatus`, `alarmGroupState`, `vehicleDetectorAlarms`, `vehicleDetectorStatusGroupAlarms`, `port1Status` | S | |
| Baca volume/okupansi agregat | `volumeOccupancyTable` + `volumeOccupancySequence` | S | Periode diatur `volumeOccupancyPeriod`. |
| Unduh/unggah seluruh database | `ascBlockGetControl`/`ascBlockData` | C/P2 | OER; efisien untuk *backup/restore* dan *cloning*. |

### A.16 Yang tidak tercakup di NTCIP 1202 v02 (penting untuk keputusan)

- **Tidak ada objek Transit/Signal Priority.** Kata “priority” hanya muncul dalam konteks prioritas antar-preempt (`preemptNumber`, `preemptLink`). Prioritas bus di NTCIP berada di **NTCIP 1211 (SCP)** dan/atau NTCIP 1202 v03 — [tidak ada di dokumen]. [ARC-IT] menyebut solusi “CTI NTCIP Signal Priority – SNMPv3/TLS” yang mengindikasikan standar terkait, tanpa detail.
- **Tidak ada objek high-resolution event log / ATSPM** dan **tidak ada SPaT/CV**; [ARC-IT] hanya menyebut *NTCIP Traffic Signal to CVRSE* dengan transport Kafka/AMQP/MQTT/DDS.
- **Tidak ada model *adaptive control*** — standar ini hanya mendefinisikan parameter aktuasi klasik, koordinasi TOD, dan preempt. Adaptif harus diimplementasikan di central dengan perintah C.
- Hal-hal yang dirujuk ke NTCIP 1201 (schedule, day plan, event log config/class, `dbCreateTransaction`) tidak didefinisikan di sini.

---

## B. SUMO — Traffic light modelling, NEMA, TraCI, dan framework adaptif

### B.1 Konsep dasar TLS di SUMO

- Tiga tujuan pemodelan: membangun sinyal masuk akal untuk seluruh kota, mereplikasi sinyal nyata dengan fidelitas tinggi, dan mensimulasikan algoritme apa pun untuk riset [SUMO-TL pembuka].
- **Sinyal mengendalikan *link* (koneksi lane-ke-lane), bukan lane**; satu lane bisa punya beberapa sinyal (belok kiri dan lurus). Indeks *link* diberi searah jarum jam mulai dari utara (indeks 0 di jam 12), belok kanan sebelum lurus sebelum belok kiri; crossing pejalan kaki di akhir [SUMO-TL “Signal state definitions”].
- **Perbedaan dengan diagram rekayasa lalu lintas**: di SUMO waktu di sumbu vertikal dan **“a new phase is introduced whenever at least one signal changes its state”** — transisi hijau→hijau bisa terdiri dari beberapa fase antara (kuning, all-red) [SUMO-TL].
- Karakter *state string*: `r` merah; `y` kuning; `g` hijau tanpa prioritas (harus mengalah pada arus foe berprioritas, melambat saat mendekat); `G` hijau prioritas; `s` panah kanan hijau wajib berhenti; `u` merah+kuning; `o` off-blinking (harus mengalah); `O` off-no-signal (punya hak jalan) [SUMO-TL].
- Setiap simpang bersinyal “has the right-of-way rules of a priority intersection underneath”; hijau parsial (`g`) hanya benar jika aturan prioritas memaksa arus minor mengalah [SUMO-TL].
- Program *default* yang dibangkitkan netconvert: siklus 90 s, hijau dibagi rata antar arah utama, kuning dihitung dari kecepatan; belok kiri *permissive* (`g`) bila kecepatan < 70 km/j, kalau tidak *protected* dengan fase belok 6 s; layout 4 fase hijau standar; tidak membuat all-red kecuali diminta [SUMO-TL “Automatically generated”].

### B.2 `tlLogic` statis

```xml
<additional>
  <tlLogic id="0" programID="my_program" offset="0" type="static">
    <phase duration="31" state="GGggrrrrGGggrrrr"/>
    <phase duration="5"  state="yyggrrrryyggrrrr"/>
    <phase duration="6"  state="rrGGrrrrrrGGrrrr"/>
    <phase duration="5"  state="rryyrrrrrryyrrrr"/>
    ...
  </tlLogic>
</additional>
```
Atribut `tlLogic`: `id` (harus sama dengan id TLS di `.net.xml`, biasanya = id junction), `type` {`static`, `actuated`, `delay_based`, `NEMA`}, `programID` (“off” dicadangkan), `offset` (atau `"begin"`). Atribut `phase`: `duration`, `state`, `minDur`, `maxDur` (default 2147483 bila minDur diset), `name` (untuk memetakan indeks fase SUMO ke nama fase rekayasa), `next` (indeks fase berikutnya; daftar bila `actuated`), `earliestEnd`/`latestEnd` (koordinasi) [SUMO-TL “Defining New TLS-Programs”]. Dimuat dengan `sumo -a tls.add.xml …`; program terakhir yang dimuat dipakai kecuali WAUT/TraCI [SUMO-TL “Loading a new Program”].

### B.3 `actuated` (gap-based) dan *custom switching rules*

- Prinsip: “prolonging traffic phases whenever a continuous stream of traffic is detected… switches to the next phase after detecting a sufficient time gap”. `minDur`/`maxDur` menentukan rentang. Detektor *induction loop* dibuat otomatis pada jarak `detector-gap` (s) × kecepatan, dinamai `TLSID_PROGRAMID_EDGEINDEX.LANEINDEX`; detektor hanya dipakai bila semua koneksi dari lane itu mendapat `G` pada fase tsb (agar tidak memperpanjang fase percuma) [SUMO-TL “Type 'actuated'”].
- Param: `max-gap` (3.0), `detector-gap` (2.0), `passing-time` (2.0; batas jarak detektor `(minDur/passingTime+0.5)*7.5`), `vTypes`, `show-detectors`, `file`, `freq`, `jam-threshold` (-1; `jam-threshold:LANEID`), `detector-length` (0), `build-all-detectors`, `coordinated`, `cycleTime`, `inactive-threshold` (180 s; anti-starvation saat `next` berdaftar), `minDur:X`/`maxDur:X` per link index, `extra-detectors`, `max-gap:LANEID`, `detector-length:LANEID`, dan pemetaan detektor kustom `<param key="LANE_ID" value="customDetectorID"/>` (atau `NO_DETECTOR`) [SUMO-TL].
- **Koordinasi**: `coordinated="true"` + `cycleTime` + `earliestEnd`/`latestEnd` per fase (timeInCycle); `latestEnd < earliestEnd` berarti fase boleh melewati batas siklus [SUMO-TL “Coordination”].
- **Multi-next (acyclic)**: `next="1 8"`; prioritas = jumlah detektor aktif fase kandidat (+bonus pejalan kaki, +bonus fase saat ini bila < maxDur, +bonus anti-starvation), siklus default = nilai pertama `next` [SUMO-TL “Dynamic Phase Selection”].
- **Custom conditions**: atribut fase `earlyTarget` (dievaluasi saat fase aktuasi bisa berpindah) dan `finalTarget` (saat maxDur tercapai); ekspresi dengan elemen `z:DETID` (gap sejak deteksi terakhir), `a:DETID` (jumlah kendaraan), `w:DETID` (waktu tunggu terlama), `d:DETID` (delay kedatangan halte transit), `g:TLSINDEX`/`r:TLSINDEX` (durasi hijau/merah link), `p:TLSINDEX` (pejalan kaki menunggu), `c:` (waktu dalam siklus), `DEFAULT` (logika gap bawaan), `<condition id=… value=…/>` bernama, `<assignment id check value/>` (variabel persisten), `<function id nArgs/>`; `minDur:4`/`maxDur:4`/`earliestEnd:4`/`latestEnd:4` bisa di-*override* lewat condition [SUMO-TL “custom switching rules”].
- Contoh prioritas bus (langsung dari dokumen): `<inductionLoop id="dBus" lane="SC_0" pos="-90" vTypes="busType" file="NUL"/>` lalu `<condition id="NSbus" value="3 > z:dBus"/>` dan fase kuning `earlyTarget="EW or NSbus"` — pola yang sama bisa dipakai untuk TSP sederhana di simulator.

### B.4 `delay_based`

Perpanjangan fase dipicu **akumulasi *time loss*** kendaraan dalam `detectorRange` (m dari stop line; default menutupi lane pendekat) yang melebihi `minTimeLoss` (s); *time loss* sesaat = `1 − v/v_max`; param `extendMaxDur` (perilaku < 1.16.0). Referensi Oertel & Wagner, TRB 2011 [SUMO-TL “Type 'delay_based'”]. Detektor kustom = `laneAreaDetector` (E2).

### B.5 NEMA controller (`type="NEMA"`, sejak SUMO 1.11.0)

- Definisi fase NEMA: fase = *movement* (bukan *stage*); fase ganjil = belok kiri, genap = lurus/kanan; 2 & 6 biasanya jalan utama; ring-and-barrier: satu fase per ring pada satu waktu, fase antar-ring boleh bersama bila tidak beda sisi *barrier*; contoh kombinasi 1+5, 1+6, 2+6, 3+7, 3+8, 4+8 dan 2+5 bila fase 1 gap-out lebih dulu [SUMO-NEMA].
- Dikembangkan NREL (Tianxin Li dkk.), didanai US DOE VTO; validasi: Schrader, Wang, Bittle, *Extension and Validation of NEMA-Style Dual-Ring Controller in SUMO*, SUMO Conf Proc 2022 [SUMO-NEMA].
- Contoh lengkap (dari dokumen):
```xml
<tlLogic id="2881" offset="10" programID="NEMA" type="NEMA">
  <param key="detector-length" value="20"/>
  <param key="detector-length-leftTurnLane" value="10"/>
  <param key="total-cycle-length" value="130"/>
  <param key="ring1" value="1,2,3,4"/>
  <param key="ring2" value="5,6,7,8"/>
  <param key="barrierPhases" value="2,6"/>
  <param key="coordinate-mode" value="true"/>
  <param key="barrier2Phases" value="4,8"/>
  <param key="minRecall" value="2,6"/>
  <param key="maxRecall" value=""/>
  <param key="whetherOutputState" value="true"/>
  <param key="fixForceOff" value="false"/>
  <phase duration="99" minDur="5" maxDur="25" vehext="2" yellow="3" red="2" name="3" state="rrrrrrrrGrrr"/>
  ...
</tlLogic>
```
- Param: `ring1`/`ring2` (fase per ring; `0` untuk fase yang tidak ada; ulangi fase ring 1 bila sisi barrier di ring 2 kosong — contoh ramp `ring1="1,2,0,4"`, `ring2="0,6,0,4"`, `barrier2Phases="4,4"`), `barrierPhases` (fase yang harus berakhir bersama; dalam *coordinated mode* = fase koordinasi, biasanya 2,6), `barrier2Phases` (biasanya 4,8), `coordinate-mode`, `total-cycle-length`, `minRecall` (default semua fase), `maxRecall` (jika semua → fixed-time dengan maxDur), `fixForceOff` (true = *fixed force-off*: fase non-koordinasi boleh memakai sisa waktu fase sebelumnya; false = *floating*), **`whetherOutputState`** (“record the signal phase change events. This could be used for generating ATSPM”), `show-detectors`, `controllerType` (TS2 = offset ke awal fase koordinasi pertama, tervalidasi terhadap SIL Econolite; 170 = ke awal kuning fase koordinasi), `detector-length`, `detector-length-leftTurnLane`, `lockPhases` (detektor tetap ON sampai fase dilayani), `crossPhaseSwitching:X` (mis. `crossPhaseSwitching:2 = 5`: detektor fase 5 melapor ke fase 2 saat fase 2 aktif), `ignore-errors` [SUMO-NEMA].
- Atribut fase: `duration` (99, tidak berpengaruh), `minDur`, `maxDur` (dalam coordinated mode = split − yellow − red), `vehext` (vehicle extension), `yellow`, `red`, `name` (nomor fase NEMA), `state` [SUMO-NEMA]. Perhatikan padanan langsung dengan NTCIP: `minDur`≈`phaseMinimumGreen`, `maxDur`≈`phaseMaximum1`/`splitTime`, `vehext`≈`phasePassage`, `yellow`≈`phaseYellowChange`, `red`≈`phaseRedClear`, `minRecall/maxRecall`≈`phaseOptions` bit 6/7, `fixForceOff`≈`coordForceMode`, `total-cycle-length`≈`patternCycleTime`, `offset`≈`patternOffsetTime`.
- TraCI khusus NEMA: `setNemaOffset(tlsID, offset)` (transisi dengan memendekkan/memanjangkan hijau koordinasi; disarankan bertahap), `setNemaMaxGreens(tlsID, [8 angka])`, `setNemaSplits(tlsID, splits)` (mengurangi Y+R lalu set max green), `setNemaCycleLength(tlsID, cycleLength)`; semua berlaku **setelah siklus berjalan selesai** [SUMO-NEMA]. Ini setara semantik `patternOffsetTime`, `splitTime`, `patternCycleTime` NTCIP.
- Validasi konfigurasi: kesalahan bila fase sebelum barrier X dari kedua ring tidak berjumlah sama; bisa diabaikan dengan `ignore-errors` untuk mensimulasikan controller salah konfigurasi [SUMO-NEMA].

### B.6 Pergantian program: WAUT, “off”, “online”

- **WAUT** (*Wochenschaltautomatik*): `<WAUT refTime id startProg>` + `<wautSwitch time to/>` + `<wautJunction wautID junctionID [procedure="GSP"|"Stretch"] [synchron]/>`; `period` untuk pengulangan; program bernama harus sudah dimuat [SUMO-TL “Defining Program Switch Times”]. Ini analog `timebaseAscActionTable`/day plan NTCIP.
- Program `off` (`<tlLogic id="0" type="static" programID="off"/>` atau opsi sumo): lampu menjadi `O`/`o` dan simpang berperilaku sebagai prioritas; analog *flash* NTCIP [SUMO-TL].
- Program bernama **`online`** menginterupsi WAUT — dipakai untuk *override* via TraCI [SUMO-TL].
- Ubah offset saja: `<tlLogic id="0" programID="0" offset="42"/>` [SUMO-TL].

### B.7 Detektor E1/E2/E3 dan alat pembangkit

- E1 = `inductionLoop` (titik; dipakai `actuated` dan tutorial TraCI), E2 = `laneAreaDetector` (areal; dipakai `delay_based`), E3 = `multi-entry/multi-exit` (entry/exit points). Skrip di `tools/output`: `generateTLSE2Detectors.py` (semua lane masuk, offset default 0.1 m, panjang default 250 m, keluaran default `e2.add.xml` → `e2output.xml`, frekuensi 60 s) dan `generateTLSE3Detectors.py` (exit di simpang, entry ditelusuri ke hulu sampai 250 m/TLS lain, keluaran `e3.add.xml`) [SUMO-TL “Tools for Importing/Generating detectors”]. Detektor kustom bisa diberi `vTypes` (mis. hanya bus) dan `file="NUL"`.
- Aktivasi detektor `actuated`/`NEMA` bisa ditulis ke output (`file`, `freq`) dan divisualisasikan (hijau = dipakai fase ini, putih = tidak, merah = ada deteksi sejak merah) [SUMO-TL].

### B.8 TraCI untuk lampu lalu lintas

- Arsitektur: “TraCI uses a TCP-based client/server architecture where SUMO acts as a server and the external script (the 'controller') is the client” [SUMO-TraCI]. Alur tutorial: `traci.start(...)` → loop `traci.simulationStep()` → baca `traci.inductionloop.getLastStepVehicleNumber(id)` → `traci.trafficlight.setPhase(TLID, phase)` → `traci.close()`; jika fase yang diset sama dengan fase aktif, fase **di-restart dari awal** [SUMO-TraCI].
- Pola adaptif yang direkomendasikan dokumen: muat program dengan **fase hijau berdurasi sangat panjang (mis. 1000 s)** agar tidak berpindah sendiri, lalu skrip memanggil `setPhase` ke fase kuning saat hijau harus diakhiri — kuning/all-red tetap ditangani SUMO; untuk transisi bercabang, tambahkan fase transisi di akhir program dan gunakan `next` [SUMO-TL “Controlling via TraCI”]. `setPhaseDuration` mengubah sisa durasi fase saat ini saja (tidak permanen).
- Kendali penuh: `setRedYellowGreenState(tlsID, state)` — setelah ini SUMO tidak mengubah state lagi sampai `setProgram`; skrip harus mengurus semua fase/transisi [SUMO-TraCI; SUMO-TL]. Program lengkap: ambil struktur dengan `getCompleteRedYellowGreenDefinition` lalu ubah dan kirim balik dengan `setCompleteRedYellowGreenDefinition` (dokumen: “recommend to first obtain a data structure…”) [SUMO-TL].
- Perintah lain yang disebut: `setProgram`, `getControlledLinks` (“TLS Link indices can be access using…”), fungsi NEMA di §B.5. Daftar lengkap API TraCI [tidak ada di dokumen ini; rujuk halaman *TraCI/Change Traffic Lights State* SUMO].

### B.9 Membangun jaringan dan alur eksperimen

- `netconvert` membangkitkan program TLS; untuk menjadikan semua TLS aktuasi: `netconvert -s orig.net.xml --o new.net.xml --tls.rebuild --tls.default-type actuated`; opsi lain yang disebut: cycle time default, yellow time, all-red, `--tls.layout`, `--tls.default-type`, penggabungan sinyal (`--tls.join`, jarak default 20 m), *signal groups* (`--tls.group-signals`, `--tls.ungroup-signals`), `tlType="NEMA"` pada node, `rightOfWay="allwayStop"/"mixedPriority"` untuk perilaku saat off [SUMO-TL]. Alat konversi program nyata: `tls_csv2SUMO.py` (durasi per koneksi edge-ke-edge) dan `tls_csvSignalGroups.py` (waktu mulai/akhir hijau per *signal group*, transisi otomatis) — sangat relevan untuk memasukkan plan APILL eksisting [SUMO-TL “Defining Signal Groups… / Tools”].
- Import OSM: dokumen ini hanya menyebut netconvert secara umum; detail impor OSM [tidak ada di dokumen]. `netedit` disebut untuk mengedit TLS dan membuat/menghapus *signal groups*.
- LiSuM: *middleware* untuk *software-in-the-loop* LISA+ dengan SUMO — bukti konsep SIL untuk controller virtual [SUMO-TL akhir].
- Alur eksperimen tipikal (gabungan dokumen): (1) jaringan `.net.xml` (netconvert/netedit), (2) `tlLogic` NEMA/actuated di `.add.xml` + detektor E1/E2/E3, (3) demand `.rou.xml` (tutorial: Poisson diaproksimasi binomial, `p=1/30`), (4) `sumocfg`, (5) skrip TraCI sebagai controller, (6) keluaran detektor + `whetherOutputState` untuk ATSPM, (7) GUI *Show/Track Phases* untuk inspeksi (waktu dalam siklus, nama fase, detektor & condition) [SUMO-TL “Signal Plan Visualization”].

### B.10 sumolights (Genders & Razavi 2019)

- **Tujuan**: kerangka umum untuk mengembangkan dan **membandingkan** controller adaptif — pembelajaran dan non-pembelajaran — di SUMO; kode di `github.com/docwza/sumolights`; SUMO 1.2.0 + TensorFlow 1.13 [Genders2019 §I, App.].
- **Abstraksi bersama**: himpunan lane masuk `L_inc`, keluar `L_out`, himpunan fase hijau `P`; `L_p,inc` = lane masuk yang hijau di fase `p`. Keputusan kontrol didekomposisi jadi dua: *fase berikutnya apa* dan *berapa lama* [Genders2019 §III].
- **Controller non-pembelajaran**:
  - *Uniform*: siklus tetap, durasi hijau sama `u` (baseline).
  - *Webster's adaptif*: kumpulkan arus per fase selama interval `W`, hitung `Y = Σ max(F_l/s)`, `C = (1.5R+5)/(1−Y)` dibatasi `[c_min, c_max]`, `G = C − R` dialokasikan proporsional ke `y`; hyperparameter `W, c_min, c_max, s` (Algorithm 1).
  - *Max-pressure*: asiklik; setelah `g_min`, pilih fase dengan `Pressure(p) = Σ_{l∈L_p,inc}|V_l| − Σ_{l∈L_p,out}|V_l|` terbesar (Algorithm 2); hanya `g_min`.
  - *SOTL*: siklik dengan durasi dinamis; integral kendaraan-waktu pada fase merah `κ` melebihi ambang `θ` memicu pindah, dengan `g_min`, jaga platoon kecil (`n < μ`, jarak `< ω`) (Algorithm 3).
- **Controller pembelajaran** (distributed acting, centralized learning: banyak *actor* dengan instans SUMO sendiri, *learner* per subset simpang, *replay buffer*; parameter disebar ke semua actor):
  - *DQN*: asiklik, memilih fase hijau berikutnya, ditahan `a_repeat`; state = densitas & antrian tiap lane masuk (dinormalisasi `k_j`, jangkauan 150 m) + one-hot fase terakhir (+1 untuk all-red); reward `r_t = −Σ_v d_t^v` (delay = travel time aktual − free-flow) dinormalisasi `|r_min|`; MLP 2×3|s| ELU.
  - *DDPG*: siklik, aksi kontinu = durasi hijau berikutnya (dibulatkan, `[g_min, g_max]`), melewati fase kosong; aktor/kritik 2×3|s| batch-norm ELU, tanh output, L2 0.01.
  - Kuning 2 s dan all-red 3 s disisipkan di antara semua transisi hijau [App.].
- **Hasil** (jaringan 2 simpang, 3 jam demand dinamis, grid search hyperparameter, lalu 32 seed): controller kaya hyperparameter (SOTL, DDPG, DQN) memiliki varian kinerja jauh lebih besar; Max-pressure & Webster's robust. Travel time (mean, std, median) s: **Max-pressure (59, 21, 54)** terbaik; Webster's (71, 30, 66); DDPG (72, 34, 65); DQN (78, 46, 66) dengan banyak *outlier*; Uniform (79, 37, 74); **SOTL (158, 169, 85)** terburuk. DQN buruk saat demand rendah tetapi setara/lebih baik saat puncak (asiklik), DDPG sebaliknya; dugaan DQN *overfit* pada periode reward besar [Genders2019 §IV.B, Fig. 5–6, §V].
- **Pelajaran untuk ITCS**: (1) uji puluhan–ratusan konfigurasi hyperparameter sebelum menyimpulkan; (2) heuristik Max-pressure adalah *baseline* kuat dan murah untuk dijalankan *real-time* dari data antrian kamera; (3) arsitektur actor/learner paralel diperlukan bila melatih RL untuk banyak simpang.

### B.11 Pan (2023) — DQN dengan *phase gate* dan *memory palace*

- Masalah: satu simpang 4 kaki × 3 lajur (Xueyuan Rd × Wensan Rd, Hangzhou); dua fase NS/WE (kuning diabaikan, ditempel di akhir fase); aksi biner {ubah fase, pertahankan} setiap 5 s [Pan2023 §3.2–3.3].
- State: antrian per lane `q`, jumlah kendaraan `v`, total waktu tunggu `w` (sejak berhenti terakhir < 0,1 m/s), fase saat ini & berikutnya, plus citra grid posisi kendaraan yang dienkode CNN → `s_t = Concat(q, v, w, P_t, P_{t+1}, l_t)` [§3.3.1].
- Reward: `R_t = Σ(λ1 d + λ2 w + λ3 q) + λ4 C + λ5 V + λ6 T` dengan `d = 1 − avg speed/speed limit`, `C` = 1 bila ganti fase, `V` = kendaraan lewat, `T` = total travel time yang lewat; bobot (−0,25, −0,25, −0,25, −5, −1, −1) [§3.3.3, Tabel 2].
- Arsitektur *phase gate*: cabang FC terpisah per fase, dipilih oleh *phase selector* [§3.4]. Pelatihan dua tahap: *offline* dari jadwal tetap (2 jam pertama dari 20 jam), lalu *online* ε-greedy (ε = 0,05, γ = 0,8, update tiap 300 s, batch 300, memori 1000 per kombinasi fase-aksi) [§3.5, §4.3]. *Memory palace*: buffer terpisah per kombinasi fase-aksi, sampling seimbang [§3.5.2].
- Hasil vs Webster fixed-time (Tabel 4): waktu tunggu turun 57,1–100 %, antrian 40,9–100 %, travel time 16,8–68,0 % pada skenario Balanced/Imbalanced/Switch/Hangzhou [§4.5]. Catatan kritis: baseline hanya fixed-time; tidak dibandingkan dengan actuated/Max-pressure; satu simpang; “switch” 100 % karena arus satu arah saja — tidak representatif Jakarta. Kode: `github.com/OscarTaoyuPan/TrafficLightControl_QS`.

---

## C. ATSPM — Automated Traffic Signal Performance Measures

### C.1 Definisi, komponen, dan model implementasi

- “ATSPMs automatically collect and convert high-resolution traffic controller data into actionable performance measures. Data and performance measures are based on the Indiana DOT high-resolution data enumerations, allowing them to be implemented with any type of traffic signal system that supports high-resolution data logging.” [HOP-20-002 p.9].
- **Lima komponen** [HOP-20-002 p.9]: (1) *High-Resolution Controller* — setiap input (detektor) dan output (perubahan fase) dicatat dengan timestamp memakai kode “enumerations”; (2) *Communications* — persisten (fiber), periodik (dial-up), atau manual; (3) *Server*; (4) *Software*; (5) *Detection* (opsional — tanpa deteksi masih bisa analisis green time; dengan deteksi: phase utilization, offset optimization).
- Resolusi: “collected continuously at 1/10-second resolution” [NCDOT §1.2].
- Tiga model implementasi: *open-source* (UDOT, di-host FHWA OSADP/GitHub; agensi menyediakan storage/hosting), *integrated* (vendor controller: Econolite Centracs SPM, Trafficware SPM Cloud), *third-party* (Miovision TrafficLink; hardware SmartLink di kabinet, cloud, langganan) [HOP-20-002 p.10; NCDOT §5, Exhibit 5-1].
- Data logger: ATC controller Linux dengan fitur logger; 2070 dapat di-*upgrade* dengan modul CPU 1C; hardware eksternal dapat merekam input/output kabinet tetapi **tidak** merekam *termination type* tanpa koneksi ke controller; Raspberry Pi sebagai *interim logger* [NCDOT §5.1, §3.1].
- Skala data: Seminole County (387 sinyal) mengumpulkan ~9 GB/hari; SQL Server Express 10 GB ≈ 1.000 simpang-hari [HOP-20-002 p.54; NCDOT §5.3].
- Biaya indikatif NCDOT (25 simpang, 2018): implementasi open-source $183k, Econolite $166k, Trafficware $152k, Miovision $126k; langganan tahunan $0/$11k/$8k/$30k; komunikasi per simpang fiber $85k, radio $11k, Raspberry Pi $2k; deteksi radar $74k, loop $28k–82k, video $69k [NCDOT Exhibit 3-1, 3-2, 5-2, 5-3].

### C.2 High-resolution controller event log (enumerasi)

> **ERRATUM (2026-09-12, koordinator):** daftar kode di bawah semula ditandai "di luar dokumen — verifikasi". Tabel resmi *Indiana Traffic Signal Hi Resolution Data Logger Enumerations* (Purdue, 2012) kini ada di `02_Panduan_Praktis_Standar/` (+ `docs/sources/_teks_ekstraksi/Purdue_Indiana_HiRes_Data_Logger_Enumerations.txt`); kode yang tercantum di sini terverifikasi cocok, dan kode tambahan (mis. 150 coord cycle state, 151 coordinated phase yield, 89/90 ped detector) dirangkum di `docs/kb/06_Model_Data_dan_Antarmuka.md` §C.

- Semua dokumen merujuk **“Indiana Traffic Signal Hi Resolution Data Logger Enumerations”** (Purdue e-Pubs, `docs.lib.purdue.edu/jtrpdata/3/`) sebagai standar *de-facto* “used across traffic signal controller vendors, ensuring that all controllers are logging events using the same codes in the same structure” [NCDOT App. C.1; HOP-20-002 p.9 catatan kaki 2].
- Struktur rekaman (tersirat dari dokumen): `(signal_id, timestamp 0,1 s, event_code, event_parameter)` dengan parameter = nomor fase / kanal detektor / nomor preempt / nomor pattern. **Tabel angka kode enumerasi tidak dimuat dalam dokumen yang dipelajari** [tidak ada di dokumen].
- Jenis kejadian yang **disebut** di dokumen dan harus ada dalam log: awal/akhir hijau-kuning-merah tiap fase; jenis terminasi (gap out, max out, force off, skip) [NCDOT A.1]; interval pejalan kaki (walk, clearance) dan *ped call/actuation* [NCDOT A.3; HOP p.20 “Stuck ped”]; detektor ON/OFF per kanal [NCDOT A.7]; preempt *request*, *service*, *dwell*, *termination* [NCDOT A.4]; perubahan *coordination plan/pattern* (visualisasi menandai batas plan) [HOP p.21]; posisi siklus (untuk PCD) [NCDOT A.5]. `whetherOutputState` SUMO NEMA menghasilkan *signal phase change events* untuk tujuan sama [SUMO-NEMA].
- [di luar dokumen — verifikasi terhadap dokumen Purdue] Kode Indiana yang lazim dipakai implementasi open-source UDOT: 0 Phase On; 1 Phase Begin Green; 3 Phase Min Complete; 4 Phase Gap Out; 5 Phase Max Out; 6 Phase Force Off; 7 Phase Green Termination; 8 Phase Begin Yellow Clearance; 9 Phase End Yellow Clearance; 10 Phase Begin Red Clearance; 11 Phase End Red Clearance; 21 Ped Begin Walk; 22 Ped Begin Clearance; 23 Ped Begin Solid Don't Walk; 45 Ped Call Registered; 81 Detector Off; 82 Detector On; 89 Ped Detector Off; 90 Ped Detector On; 102 Preempt Call Input On; 104 Preempt Call Input Off; 105 Preempt Entry Started; 107 Preempt Begin Dwell; 111 Preempt Exit Started; 131 Coord Pattern Change; 132 Cycle Length Change; 133 Offset Length Change. Angka-angka ini **wajib diverifikasi** sebelum dijadikan spesifikasi.

### C.3 Definisi metrik dan algoritma perhitungan

Berikut tiap metrik, dengan definisi, cara hitung (yang dinyatakan dokumen), kebutuhan data, dan visualisasi. Sumber utama: [NCDOT App. A.1–A.13, p.19–36] dan [HOP-20-002 p.20–27].

1. **Purdue Phase Termination** [NCDOT A.1; HOP p.21–22] — Untuk tiap fase dan tiap siklus, klasifikasikan kejadian terminasi: *Gap out* (min time terpenuhi, ada conflicting call, vehicle extension timer habis → kapasitas tersedia atau perlu cek passage/truk), *Max out* (fase diperpanjang sampai maksimum → jenuh atau detektor rusak menahan panggilan), *Force off* (pada plan koordinasi; fase koordinasi biasanya force-off tiap siklus), *Skip* (tidak ada call), *Pedestrian activity*. Visualisasi: x = waktu hari, y = fase, titik berwarna (hijau gap, merah max, biru force-off, coklat ped), latar bergantian biru/abu-abu per plan. Data: hanya event log; tanpa detektor tambahan. Kegunaan: kapasitas tersedia, deteksi detektor rusak (max-out malam hari), verifikasi recall.
2. **Split Monitor** [NCDOT A.2; HOP p.29–30] — Sama dengan (1) plus durasi aktual fase (s) vs *programmed split* per siklus, satu grafik per fase. Perhitungan: durasi = t(begin green)→t(end red clearance) per fase per siklus; bandingkan ke split plan. Kegunaan: estimasi green time yang dibutuhkan vs tersedia; deteksi *double serving* berlebih pada sistem adaptif (kasus Lake County).
3. **Pedestrian Delay** [NCDOT A.3; HOP p.27] — Delay = waktu antara *ped call/button push* dan aktivasi Walk untuk fase itu; laporkan min/maks/rata-rata per hari dan per plan, jumlah aktuasi per waktu. Kegunaan: tombol rusak (ped timing tiap siklus malam hari), pertimbangan ped recall.
4. **Preemption Details** [NCDOT A.4] — Waktu *request*, *service*, *time to service*, *dwell time*, dan kapan request berakhir, untuk tiap preempt. Data: event log preempt. Kegunaan: frekuensi preempt & delay yang ditimbulkan ke pengguna lain.
5. **Purdue Coordination Diagram (PCD)** [NCDOT A.5; HOP p.23, 25] — Untuk fase koordinasi, tiap aktuasi detektor *advance* diplot sebagai titik pada (waktu hari, waktu-dalam-siklus); garis hijau = awal hijau, garis merah = awal merah (atas). Titik di atas garis hijau = *arrival on green*, di bawah = *arrival on red*. Metrik: **% Arrivals on Green (AoG)** = kedatangan saat hijau / total; **Platoon Ratio** = AoG dinormalisasi terhadap proporsi waktu hijau dalam siklus (“normalizes arrivals on green considering the percent of time the phase was green during the cycle”). Data: *advance detection* 350–400 ft sebelum antrian tipikal, zona kecil (bukan presence panjang); detektor seri antar-lajur boleh tapi *undercount*. Kegunaan: penyesuaian offset, verifikasi cycle length, evaluasi sebelum/sesudah (contoh US 17: AoG 59 % → 66 %, 70–74 % PM peak). Rujukan metode: Day et al., TRR 2192 (2010).
6. **Purdue Link Pivot** [NCDOT A.6] — Optimasi offset koridor: untuk tiap *link* (pasangan simpang berurutan) hitung *Link Delta* = perubahan offset yang memaksimalkan AoG prediksi (dari distribusi kedatangan hulu-hilir); *Offset (+ to Offset)* = akumulasi delta sepanjang rute; *New Offset* = existing + adjustment; bandingkan AoG eksisting vs prediksi. Input: rute terurut, periode analisis, cycle length, opsi bias arah. Data: advance detection di simpang berurutan.
7. **Turning Movement Counts (TMC)** [NCDOT A.7] — Volume per lajur dan per *lane group* (kiri/lurus/kanan) dalam *bin* (umumnya 15 menit); sepeda terpisah bila ada; tabel per interval. Data: deteksi *lane-by-lane*, zona kecil, ideal **melewati stop bar** agar antrian tidak menutupi. Kegunaan: kesehatan detektor per kanal (volume nol tiba-tiba, kasus NC 55), kapasitas per fase.
8. **Purdue Split Failure** [NCDOT A.8; HOP p.24] — Per fase per siklus hitung **GOR** (Green Occupancy Ratio) = proporsi waktu hijau saat detektor stop-bar terokupasi, dan **ROR5** (Red Occupancy Ratio 5 s pertama merah). **Split failure bila GOR ≥ 80 % dan ROR5 ≥ 80 %** (kendaraan tak terlayani di akhir fase). Visual: garis kuning vertikal per kegagalan, rata-rata GOR/ROR5 15 menit, total per hari dan per plan. Data: *stop-bar presence detection*; detektor yang digabung satu kanal melebihkan okupansi. Kegunaan: alokasi green vs demand; before/after (NC 50: naikkan split fase 4 → split failure turun).
9. **Approach Volume** [NCDOT A.9] — Volume per arah (pasangan N/S, E/W) per jenis detektor per bin 15 menit; tabel perencanaan: **PHF, K-factor, D-factor**. Data: count detection stop-bar atau advance.
10. **Approach Delay** [NCDOT A.10] — Delay per kendaraan = (waktu fase mendapat hijau) − (waktu aktuasi advance dikonversi ke waktu tiba stop bar); total & rata-rata per fase. **Tidak** memperhitungkan start-up lost time, deselerasi, antrian tetap — “simplified approach”. Data: advance detection.
11. **Arrivals on Red (AoR)** [NCDOT A.11] — Jumlah/persentase kedatangan saat merah per fase per waktu; kebalikan PCD tetapi tanpa informasi posisi dalam siklus. Data: advance detection. Kegunaan: tren per plan.
12. **Approach Speed** [NCDOT A.12] — Speed limit, rata-rata, persentil-85 per waktu; proxy travel time. Data: detektor radar berkemampuan kecepatan (open-source: Wavetronix Advance) atau probe Bluetooth/WiFi vendor.
13. **Yellow and Red Actuations (YRA)** [NCDOT A.13; HOP p.26] — Kendaraan yang memasuki simpang saat kuning, saat red clearance, atau saat fase konflik sudah aktif (*severe violation*); diplot terhadap overlay kuning/merah. Data: deteksi masuk simpang (zona *past stop bar*) atau stop-bar dengan filter kecepatan. Kegunaan: red-light running, evaluasi durasi kuning/all-red.
14. **ATSPM Watchdog** [HOP p.20] — *scheduled job* harian, email sekali sehari bila: *No data* (< 500 rekaman/24 jam per fase → komunikasi gagal); *Force offs* > 90 % dari ≥ 50 aktivasi pukul 01:00–05:00; *Max outs* > 90 % dari ≥ 50 aktivasi 01:00–05:00 (detektor rusak); *Low advance detector counts* (< 100 kendaraan 17:00–18:00 pada detektor PCD); *Stuck ped* (> 200 aktuasi ped 01:00–05:00). Ambang default dapat diubah.
15. **Corridor/program level** [HOP p.32–35]: GDOT MARK 1 dashboard mengagregasi AoG, *progression ratio*, split failures, volume koridor, *device & communication uptime*, peringkat simpang per AoG, laporan aktivitas pemeliharaan; PennDOT memakai probe data (INRIX/HERE/TomTom): *cumulative frequency diagram* travel time (geser kiri = membaik, lebih curam = lebih reliabel), plot median travel time (% speed limit) vs IQR (% speed limit) — arah kiri-bawah = membaik; *Travel Time Comparison Tool*, *Arterial Ranking Tool*, *Congestion Ticker* [HOP p.53].
16. **Queue length**: tidak ada metrik ATSPM bernama *queue length* dalam dokumen yang dipelajari [tidak ada di dokumen]; antrian di-*proxy* lewat split failure (ROR5), AoR, dan approach delay. (Di sisi simulasi/RL, *queue length* dihitung langsung dari kendaraan berhenti — [Pan2023 §3.3.1]: jumlah kendaraan berkecepatan nol per lane; [Genders2019]: antrian per lane dinormalisasi jam density.)
17. **Detector health**: gabungan Watchdog, TMC per kanal, Phase Termination (max-out malam), plus objek NTCIP `vehicleDetectorAlarms`/`detectorOccupancy` kode 210–217 [§A.5].

### C.4 Kebutuhan detektor per metrik (Exhibit B-1 NCDOT)

| Metrik | Tanpa detektor tambahan | Advance | Stop-bar presence | Stop-bar count | Speed |
|---|---|---|---|---|---|
| Phase Termination, Split Monitor, Ped Delay, Preemption Details | ✓ | | | | |
| PCD, Link Pivot, Approach Delay, Arrivals on Red | | ✓ | | | |
| Purdue Split Failure | | | ✓ | | |
| TMC, Approach Volume | | | | ✓ (lane-by-lane) | |
| Approach Speed | | | | | ✓ |
| Yellow & Red Actuations | | | past-stop-bar / stop-bar + filter kecepatan | | |

Konfigurasi A–F [NCDOT App. B]: A tanpa deteksi tambahan; B stop bar; C stop bar + advance; D semua; E (tipikal NCDOT) stop-bar presence di jalan minor & lajur belok kiri + advance lane-by-lane di jalan mayor; F sama dengan *lane groups*. Rekomendasi: tambah stop-bar presence di lajur lurus jalan mayor.

### C.5 Cara agensi menggunakan ATSPM (NCDOT dan use case FHWA)

- **Peran** [NCDOT §2]: engineer/teknisi → penyesuaian timing berbasis data (bukan model), *pinpoint* kerusakan, before/after berkelanjutan; manajer → proses rutin memeriksa alert (WatchDog), work order, prioritas proyek; pembuat kebijakan → *cost/benefit* dan tren investasi; IT → jaringan & data.
- **Prioritas lokasi** [NCDOT §6, Exhibit 6-1]: Tier I (permanen: fiber, stop-bar semua kaki, advance pada kaki koordinasi), Tier II (evaluasi sementara: Raspberry Pi + open source), Tier III (tidak direkomendasikan). Kriteria: peralatan ada, proyek konstruksi terencana, travel time tinggi, reliabilitas rendah, eksposur tinggi (v/c), keselamatan rendah, proyek retiming terencana; ≥ 5 kriteria → Tier I. ATSPM paling bermanfaat mendekati kapasitas; koridor sangat jenuh tidak cukup dengan retiming.
- **Use case FHWA** [HOP p.19–31]: (1) pemeliharaan — Watchdog + Phase Termination menemukan detektor gagal sebelum dikirim kru; (2) timing — PCD untuk offset, Split Failure untuk split, AoG dilacak bulanan; (3) keselamatan — YRA dan Ped Delay; (4) **evaluasi adaptive control** — ATSPM sebagai *observer* paralel yang objektif (InSync, Lake County): Split Monitor menemukan *double serving* berlebih; PCD menemukan hijau tak terpakai; validasi AoG tetap 90 % setelah meminjam hijau ke jalan minor; (5) koridor/program — dashboard dan probe data.
- **Kebijakan**: “ATSPMs by themselves will not improve traffic flow… like the tire pressure light” — perlu proses bisnis dan staf untuk bertindak [HOP p.16]. Kematangan diukur dengan *Traffic Signal Systems Capability Maturity* (business process, systems & technology, performance measurement, organization & workforce, culture, collaboration) [HOP p.47].
- **Kepemilikan data**: vendor terintegrasi mungkin tidak memberi akses raw hi-res data (harus diminta) [NCDOT Exhibit 5-5 catatan 15]; open source memberi fleksibilitas kustomisasi tetapi butuh IT.

---

## D. Rancangan referensi untuk aplikasi ITCS

Prinsip: (P1) model data internal **menyalin semantik NTCIP 1202** sehingga adaptor ke controller berstandar menjadi pemetaan 1:1 dan controller non-standar dipetakan ke model yang sama; (P2) **kontrol dari central hanya lewat “perintah C”** yang aman-gagal (backup timer), sedangkan perubahan plan lewat transaksi tervalidasi; (P3) **SUMO NEMA adalah *digital twin*** karena parameternya sudah sepadan NTCIP dan TraCI menyediakan API kontrol yang sama semantiknya; (P4) **event log hi-res adalah sumber kebenaran KPI**, baik dari controller lapangan maupun dari simulator (`whetherOutputState`); (P5) setiap algoritme adaptif (green wave, TSP, AI/kamera) harus dievaluasi dengan ATSPM sebagai *observer* independen [HOP p.29].

### D.1 Skema data (entitas dan atribut utama)

Notasi: `PK` kunci, `→` rujukan. Padanan sumber di kolom kanan.

| Entitas | Atribut utama | Padanan sumber |
|---|---|---|
| **Intersection** | `intersection_id` PK, nama, lat/lon, `region_id`, kaki simpang (approach: bearing, nama jalan, jumlah lajur), `corridor_id`(s) & urutan dalam koridor, tier ATSPM, status operasional | Link Pivot butuh rute terurut [NCDOT A.6]; tier [NCDOT §6] |
| **Controller** | `controller_id` PK → intersection, vendor, model, firmware, protokol {NTCIP-SNMP, NTCIP-STMP, vendor-RS232, TraCI-sim}, alamat IP/port/community atau serial, `unit_backup_time_s`, kapabilitas (conformance groups yang didukung: phase, detector, coord, timebase, preempt, ring, channel, overlap, block), `max_phases`, `max_rings`, `max_vehicle_detectors`, `max_patterns`, `max_splits`, `max_preempts`, `hi_res_logging` (bool), `sim_id` bila digital twin | `unitBackupTime`; `max*` objek; Annex A [NTCIP] |
| **Phase** | (`controller_id`, `phase_number`) PK, `ring`, `concurrency[]`, `enabled`, movement (arah/belokan), `walk`, `ped_clear`, `min_green`, `passage`, `max1`, `max2`, `yellow`, `red_clear`, `red_revert`, `added_initial`, `max_initial`, `tbr`, `cbr`, `time_to_reduce`, `reduce_by`, `min_gap`, `dyn_max_limit`, `dyn_max_step`, `startup`, `options` (16 bit: recall/flash entry/exit/dual entry/…) | `phaseTable` [NTCIP §2.2.2]; `<phase minDur maxDur vehext yellow red name>` [SUMO-NEMA] |
| **Ring / Sequence** | `sequence_number`, `ring_number`, `phase_order[]`; `barrier_groups[]` | `sequenceTable` [§2.8.3]; `ring1/ring2/barrierPhases` [SUMO-NEMA] |
| **Overlap** | `overlap_number`, `type`, `included_phases[]`, `modifier_phases[]`, `trail_green/yellow/red` | `overlapTable` [§2.10] |
| **Channel (SignalGroup)** | `channel_number`, `control_type` {vehicle, ped, overlap}, `control_source`, `flash_mode`, `dim_mode`; pemetaan ke *link index* SUMO | `channelTable` [§2.9]; link index [SUMO-TL] |
| **Detector** | `detector_number` PK, jenis {loop, radar, video/AI-camera, ped button, virtual}, lokasi (lane, jarak dari stop bar, panjang zona; klasifikasi *advance/stop-bar/past-stop-bar/count/presence/speed*), `call_phase`, `switch_phase`, `options` (call/queue/added-initial/passage/lock), `delay`, `extend`, `queue_limit`, diagnostik `no_activity`, `max_presence`, `erratic_counts`, `fail_time`; untuk ATSPM: `movement`, `lane_group`, `distance_to_stop_bar_ft`, `latency_correction_s`, `speed_mph` (untuk konversi waktu tiba) | `vehicleDetectorTable` [§2.3.2]; Approach Delay konversi waktu tiba [NCDOT A.10]; Exhibit B-1 |
| **PedDetector** | `ped_detector_number`, `call_phase`, diagnostik | `pedestrianDetectorTable` [§2.3.7] |
| **Pattern (TimingPlan)** | (`controller_id`, `pattern_number` 1..253) PK, `cycle_time`, `offset_time`, `split_number`, `sequence_number`, `force_mode` {floating, fixed}, `correction_mode` {dwell, shortway, addOnly}, `max_mode`; nama plan, koridor, tujuan (green wave arah) | `patternTable`, `coordForceMode`, `coordCorrectionMode` [§2.5]; `total-cycle-length/offset/fixForceOff` [SUMO-NEMA] |
| **Split** | (`split_number`, `phase_number`) PK, `split_time`, `mode` {none, minVehRecall, maxVehRecall, pedRecall, maxVehPedRecall, omitted}, `coord_phase` | `splitTable` [§2.5.9] |
| **TimebaseAction / DayPlan / Schedule** | `action_number`, `pattern`, `aux_functions`, `special_functions`; day plan (event time → action), schedule (hari/tanggal → day plan) | `timebaseAscActionTable` [§2.6.3]; blok 0x0B/0x0C; WAUT [SUMO-TL] |
| **Preempt** | `preempt_number`, semua parameter §A.9, `track_phases[]`, `dwell_phases[]`, `exit_phases[]`, `link`, prioritas; sumber (kereta, damkar/ambulans, manual TMC) | `preemptTable` [§2.7.2] |
| **PrioritySource (TSP)** | bus line/AVL, halte, *check-in/check-out* detektor, strategi {green extension, early green} — dipetakan ke aksi `Hold`/`ForceOff`/`VehCall` atau ke `earlyTarget` di simulasi | [tidak ada objek TSP di NTCIP v02]; contoh bus condition [SUMO-TL] |
| **SpecialFunction** | `sf_number`, deskripsi, status | `specialFunctionOutputTable` [§2.4.14] |
| **ControllerStatusSnapshot** (time-series) | `ts`, `pattern_status`, `local_free_status`, `cycle_status`, `sync_status`, `control_status`, `flash_status`, `alarm1`, `alarm2`, `short_alarm`, `active_action`, per-fase R/Y/G/Walk/PedClear/DontWalk/VehCall/PedCall/On/Next (bitmask), per-ring `ring_status`, per-detektor `active`/`alarms`, `preempt_state[]` | §A.4, §A.6, §A.7, §A.10 |
| **HiResEvent** (time-series, append-only) | `intersection_id`, `ts` (0,1 s), `event_code`, `event_param`, `source` {controller, external-logger, sumo}, `ingest_batch_id` | [HOP p.9; NCDOT C.1; SUMO-NEMA `whetherOutputState`] |
| **VolumeOccupancyReport** | `ts`, `period_s`, `sequence`, per-detektor `volume`, `occupancy_pct` / kode fault | `volumeOccupancyReport` [§2.3.5] |
| **CommandLog** | `ts`, operator/algoritme, `controller_id`, objek/OID atau perintah abstrak, nilai, hasil (SNMP error / `ascBlockErrorStatus` / `dbVerifyError`), `transaction_id` | Annex C; Annex B |
| **PlanChangeTransaction** | `transaction_id`, snapshot sebelum/sesudah (blok OER), status {buffering, verify, done, error}, pesan verifikasi | Annex C.4–C.5 |
| **KPI / Metric result** | `intersection_id`, `phase`/`approach`/`detector`, `metric_type`, `bin_start`, `bin_size`, nilai (mis. AoG, platoon ratio, GOR, ROR5, split_failures, term_gap/max/forceoff/skip counts, ped_delay avg/max, preempt count/time-to-service, volume, PHF, K, D, approach_delay_total/avg, aor_pct, speed_avg/p85, yra_yellow/red/severe) | §C.3 |
| **Alert** | `ts`, jenis Watchdog (no_data, force_offs, max_outs, low_adv_counts, stuck_ped) atau NTCIP alarm, ambang, nilai, status penanganan (work order) | [HOP p.20; NTCIP alarm objects] |
| **Corridor / Route** | `corridor_id`, urutan simpang, arah, cycle bersama, `bias_direction`, link jarak/kecepatan | Link Pivot [NCDOT A.6]; MARK 1 [HOP p.32] |
| **SimulationScenario** | `net.xml`, `add.xml` (tlLogic + detektor), `rou.xml`, seed, durasi, controller under test, hyperparameter set, hasil MoE (travel time mean/std/median, queue, delay) | [Genders2019 §IV] |

### D.2 Adaptor protokol dan digital twin

**Lapisan “Controller Abstraction Interface” (CAI)** — satu antarmuka internal dengan implementasi:

1. **NTCIP/SNMP adapter** (controller berstandar): 
   - *Poll status* berkala (mis. 1 s untuk `phaseStatusGroup*`/`ringStatus`/`coordCycleStatus`; 10–60 s untuk alarm & detektor; `volumeOccupancyPeriod` untuk V/O). Baca banyak OID dalam satu GET (Annex C.1).
   - *Command*: SET objek tipe C (§A.15). **Heartbeat**: pastikan ada SET ke objek kontrol sistem lebih sering dari `unitBackupTime`; bila TMC putus, controller sendiri kembali ke TOD lokal — perilaku *fail-safe* yang harus dipertahankan, bukan dihindari [NTCIP §2.4.3].
   - *Plan download*: implementasikan mesin status transaksi Annex C.4/C.5 (`dbCreateTransaction`), validasi Annex B di sisi server sebelum kirim, gunakan `ascBlockData` untuk unduh/unggah blok, simpan `dbVerifyError`.
   - *Conformance discovery*: baca `max*` dan uji GET per grup untuk mengisi kapabilitas controller (PRL).
   - Keamanan transport: ARC-IT mencantumkan profil SNMPv3/TLS [ARC-IT].
2. **Vendor RS-232/serial adapter** (controller lama non-NTCIP, umum di lapangan Indonesia): implementasikan protokol proprietary vendor di balik CAI yang sama; petakan hanya kapabilitas yang tersedia (mis. pilih plan, baca status lampu), tandai *unsupported* untuk perintah C yang tidak ada. Bila tidak ada hi-res log, pertimbangkan *external logger* di kabinet — dengan catatan “termination types” tidak akan terekam tanpa koneksi ke controller [NCDOT §5.1].
3. **TraCI/SUMO adapter** (digital twin): 
   - Bangun `tlLogic type="NEMA"` dari entitas Phase/Ring/Pattern/Split (pemetaan §B.5) + detektor E1/E2 sesuai entitas Detector; `whetherOutputState=true` untuk memancarkan event ke pipeline ATSPM.
   - Petakan perintah CAI: pilih pattern → `setProgram`/`setNemaSplits`+`setNemaCycleLength`+`setNemaOffset` (berlaku setelah siklus selesai [SUMO-NEMA]); hold/force-off → `setPhase` ke fase kuning atau `setPhaseDuration`; call → detektor virtual/`earlyTarget`; status → `getRedYellowGreenState`, `getPhase`, detektor `getLastStepVehicleNumber`/okupansi.
   - Untuk algoritme adaptif eksperimental gunakan pola “hijau panjang + `setPhase` ke kuning” [SUMO-TL] atau `setRedYellowGreenState` penuh; untuk RL gunakan arsitektur actor/learner paralel [Genders2019].
   - Alur SIL: plan eksisting (CSV) → `tls_csvSignalGroups.py` → SUMO; validasi bahwa ATSPM dari simulasi (PCD/AoG, split failure) konsisten dengan lapangan sebelum mengevaluasi algoritme baru; LiSuM menunjukkan pola *middleware* untuk controller virtual vendor [SUMO-TL].
4. **Deteksi kamera/AI** masuk ke CAI sebagai *virtual detector* (memicu `phaseControlGroupVehCall` di lapangan atau detektor E1/E2 di simulasi) dan sebagai sumber `HiResEvent` kode detector on/off, sehingga ATSPM tetap seragam.

### D.3 Pipeline ATSPM

1. **Ingest**: unduh log hi-res dari controller (FTP/HTTP vendor) atau terima dari external logger/SUMO; *batch* harian minimum, *near-real-time* untuk KPI TMC; deduplikasi dengan (`intersection_id`,`ts`,`code`,`param`).
2. **Normalize**: konversi format vendor ke skema `HiResEvent` (kode Indiana); *time sync* (GPS/NTP); simpan raw (agensi harus punya akses raw [NCDOT Exhibit 5-5 (15)]).
3. **Segmentasi siklus & fase**: rekonstruksi interval hijau/kuning/merah per fase dan batas siklus (dari coordination pattern change/cycle events atau dari awal hijau fase koordinasi), *termination reason* dari event gap/max/force-off, *skip* bila fase tidak muncul dalam siklus.
4. **Kalkulator metrik** (definisi §C.3): Phase Termination & Split Monitor (hanya event fase); Ped Delay (ped call → walk); Preemption Details; PCD/AoG/Platoon Ratio, AoR, Approach Delay, Link Pivot (advance detector + konversi jarak/kecepatan); Split Failure (GOR/ROR5 dari stop-bar presence; ambang 80 %); TMC/Approach Volume + PHF/K/D (count detector per lajur); Approach Speed; YRA. Konfigurasi detektor per simpang (jenis, jarak, movement) adalah *prasyarat* [NCDOT App. B].
5. **Agregasi**: bin 15 menit/jam/plan/hari; koridor (AoG rata-rata tertimbang, peringkat simpang, uptime perangkat & komunikasi ala MARK 1 [HOP p.32]); bulanan untuk tren (contoh AoG bulanan UDOT [HOP p.25]).
6. **Alert/Watchdog**: job harian dengan ambang default HOP p.20 (dapat diubah), ditambah alarm NTCIP real-time (`shortAlarmStatus` Detector Fault, Coordination Alarm; `vehicleDetectorAlarms`), dikirim ke work-order.
7. **Penyajian**: PCD, Phase Termination, Split Monitor, Split Failure, Ped Delay, Preempt, TMC, Volume, YRA per simpang (24 jam, latar per plan), dashboard koridor, before/after (dua rentang tanggal), *hot spots*. Fitur pembeda vendor yang patut ditiru: overlay multi-hari, filter hari-minggu, query multi-simpang, ekspor raw [NCDOT Exhibit 5-5].
8. **Evaluasi adaptif**: jalankan pipeline yang sama pada log dari lapangan dan dari SUMO; laporkan AoG, split failure, delay sebelum/sesudah aktivasi algoritme AI/green wave/TSP [HOP p.29–31].

### D.4 Daftar API internal yang disarankan

Semua *resource-oriented*; nama tentatif.

- **Inventory**: `GET/PUT /intersections/{id}`, `/controllers/{id}` (kapabilitas, protokol), `/controllers/{id}/phases`, `/rings`, `/overlaps`, `/channels`, `/detectors`, `/preempts`, `/patterns`, `/splits`, `/timebase/actions`, `/dayplans`, `/schedules`.
- **Live status**: `GET /controllers/{id}/status` (snapshot §D.1), `WS /controllers/{id}/status/stream` (push tiap poll), `GET /controllers/{id}/detectors/status`, `GET /controllers/{id}/vo-report`.
- **Command (tipe C)**: `POST /controllers/{id}/commands/pattern {pattern|free|flash|standby}`, `/commands/sync {cycle_position}`, `/commands/phase-control {group, omit, ped_omit, hold, force_off, veh_call, ped_call}`, `/commands/ring-control {…}`, `/commands/preempt {n, on|off}`, `/commands/special-function {n, on|off}`, `/commands/unit-control {bits}`; semua dicatat ke `CommandLog`, dengan `heartbeat` otomatis oleh adapter.
- **Plan management (P/P2)**: `POST /controllers/{id}/transactions` (buka), `PUT /transactions/{tid}/objects` atau `/blocks` (buffer), `POST /transactions/{tid}/verify` (jalankan Annex B server-side lalu di controller), `POST /transactions/{tid}/commit|abort`; `GET /controllers/{id}/blocks/{dataID}` (upload OER), `POST …/blocks` (download).
- **Corridor & strategi**: `POST /corridors/{id}/green-wave {pattern set, offsets}`, `POST /corridors/{id}/link-pivot/run {route, period, cycle, bias}` → rekomendasi offset; `POST /priority/requests` (bus/darurat: intersection, approach, ETA, strategi) → dipetakan ke command.
- **Simulation**: `POST /sim/scenarios` (net, add, rou, seed), `POST /sim/runs {scenario, controller_under_test, hyperparams}` → MoE + HiResEvent; `GET /sim/runs/{id}/atspm/...` (endpoint yang sama dengan lapangan).
- **ATSPM/KPI**: `POST /hires/ingest`, `GET /atspm/{intersection}/phase-termination?from&to`, `/split-monitor`, `/pcd?phase`, `/split-failure`, `/approach-delay`, `/arrivals-on-red`, `/tmc?bin=15`, `/approach-volume`, `/ped-delay`, `/preemption`, `/approach-speed`, `/yra`, `/corridors/{id}/summary`, `/compare?before&after`, `GET /alerts`, `POST /alerts/{id}/ack`.

### D.5 Keputusan desain dan rujukannya

| Keputusan | Alasan | Rujukan |
|---|---|---|
| Model data meniru node NTCIP 1202 | Pemetaan 1:1 ke controller standar; controller lain dipetakan ke model yang sama | [NTCIP §2] |
| Kontrol real-time hanya lewat objek C + heartbeat < `unitBackupTime` | Fail-safe bawaan controller | [NTCIP §2.4.3, §2.5.14] |
| Perubahan plan lewat transaksi + validasi Annex B | Standar mewajibkan untuk P2; mencegah database rusak | [NTCIP Annex A.1.1, B, C.4] |
| Spesifikasi pengadaan menyebut conformance groups wajib (Coord, Timebase, Preempt, Ring, Block) | Standar hanya mewajibkan Phase & Detector | [NTCIP Annex A.2] |
| TSP tidak dari NTCIP 1202 v02; gunakan Hold/ForceOff/VehCall + logika central, atau standar SCP/v03 | Tidak ada objek priority di v02 | [NTCIP; ARC-IT] |
| SUMO NEMA sebagai digital twin | Parameter dual-ring sepadan NTCIP; TraCI setNema*; output ATSPM; tervalidasi SIL Econolite | [SUMO-NEMA] |
| Max-pressure sebagai baseline adaptif pertama; RL setelah tuning masif | Hasil sumolights | [Genders2019 §IV–V] |
| RL: phase gate, memory palace, offline pretrain | Menangani ketidakseimbangan arus & warm start | [Pan2023 §3.4–3.5] |
| ATSPM sebagai observer independen untuk algoritme AI | Praktik FHWA/Lake County | [HOP p.29] |
| Deteksi: advance ~350–400 ft + stop-bar presence + lane-by-lane count untuk paket metrik penuh | Exhibit B-1 | [NCDOT App. B] |
| Watchdog dengan ambang default HOP | Praktik UDOT/GDOT | [HOP p.20] |
| Simpan raw hi-res & hitung sendiri (tidak bergantung vendor) | Akses raw data vendor terbatas | [NCDOT Exhibit 5-5] |
| Perencanaan kapasitas storage ~ puluhan MB/simpang/hari | 9 GB/hari untuk 387 sinyal | [HOP p.54] |

---

## E. Kutipan kunci (dengan bagian/halaman)

1. NTCIP §1.1 Scope: “The messaging between Transportation Management and Actuated Signal Controllers is accomplished by using the NTCIP Application Layer services to convey requests to access or modify values stored in a given device; these values are referred to as objects.”
2. NTCIP §2.1: “asc OBJECT IDENTIFIER ::= { devices 1 }” dan “All of the objects defined in this document reside under the 'asc' node of the global naming tree.”
3. NTCIP §2.4.3 `unitBackupTime`: “If the unitBackupTime interval expires without a SET operation to any of the system control parameters, then the CU shall revert to Backup Mode.”
4. NTCIP §2.5.14 `systemPatternControl`: “0 Standby – the system relinquishes control of the device. 1-253 Pattern … 254 Free … 255 Flash. If an unsupported / invalid pattern is called, Free shall be the operational mode.”
5. NTCIP §2.5.9 `splitTime`: “The time in seconds the splitPhase is allowed to receive (i.e. before a Force Off is applied) when constant demands exist on all phases… The splitTime includes all phase clearance times.”
6. NTCIP §2.2.5 `phaseControlGroupForceOff`: “When the phase green terminates, the associated bit shall be reset to 0.”
7. NTCIP §2.8.6 `ringStatus`: “Bit 5: Force Off… Bit 4: Max Out… Bit 3: Gap Out… Coded Status: 0 Min Green, 1 Extension, 2 Maximum, 3 Green Rest, 4 Yellow Change …”
8. NTCIP §2.12.2 `ascBlockData`: “An OER encoded string used for uploading and downloading ASC parameters… A SET on this object shall require the use of 'dbCreateTransaction' defined in NTCIP 1201 Clause 2.3.1.”
9. NTCIP Annex A.1.1: tipe P2 — “use of 'dbCreateTransaction' … to SET this object is mandatory. NOTE—The device must NOT allow a normal SNMP SET.”
10. NTCIP Annex B.1: “When no consistency faults are detected in the data when leaving 'transaction' mode, the following shall be written to the dbVerifyError object: 'NO VERIFICATION ERROR'.”
11. SUMO-TL: “in SUMO a new phase is introduced whenever at least one signal changes its state. This means that transitions between green phases can be made up of multiple intermediate phases.”
12. SUMO-TL: “a signal does not control lanes, but links – each connecting a lane which is incoming into a junction and one which is outgoing from this junction.”
13. SUMO-TL (TraCI): “A common pattern for implementing adaptive control via TraCI is to load [a program where] green phases have a long duration (i.e. 1000s) to avoid switching… and … setPhase … (typically a yellow phase) whenever the green phase should end.”
14. SUMO-NEMA: `whetherOutputState` — “Whether record the signal phase change events. This could be used for generating Automated Traffic Signal Performance Measures (ATSPM).”
15. SUMO-NEMA: “TS2 offset has been validated against software-in-the-loop Econolite controllers”; “All the updates in the signal timing parameters in the NEMA-phase controller will happen after the current cycle ended.”
16. SUMO-TraCI: “TraCI uses a TCP-based client/server architecture where SUMO acts as a server and the external script (the 'controller') is the client.”
17. Genders2019 §V: “the Max-pressure controller was found to achieve the best performance, yielding the lowest travel times, queues and delay. This manuscript's research provides evidence that heuristics can offer powerful solutions even compared to complex deep-learning methods.”
18. Genders2019 §IV.A: “methods with larger numbers of hyperparameters (e.g., SOTL, DDPG, DQN) exhibit greater performance variance than methods with fewer hyperparameters (e.g., Max-pressure).”
19. Pan2023 Abstract: “reducing vehicle waiting time (57.1% to 100%), queue lengths (40.9% to 100%), and total travel time (16.8% to 68.0%) compared to traditional fixed signal plans.”
20. HOP-20-002 p.9: “each time the traffic signal controller receives an input (e.g. from a detector) or generates an output (e.g. changes the phase of a signal), the controller logs the event and its timestamp in a high-resolution data log. Events are logged using standardized codes called 'enumerations.'”
21. HOP-20-002 p.24: “When GOR and ROR5 are both high (typically 80 percent or higher), this suggests the occurrence of a split failure.”
22. HOP-20-002 p.20 (Watchdog): “Max outs: This condition reports phases with more than 90 percent max outs in at least 50 activations between 1:00 AM and 5:00 AM.”
23. HOP-20-002 p.29: “Because ATSPM methodologies operate as an observer in parallel with the traffic signal control system, they can be used to monitor a wide variety of traffic control schemes, including adaptive systems.”
24. HOP-20-002 p.16: “ATSPMs can serve as a warning light for traffic signal system issues. However, there should be a process in place for traffic engineers and technicians to take action.”
25. NCDOT §1.2: “ATSPMs are collected continuously at 1/10-second resolution.”
26. NCDOT A.5 (p.24): PCD “provides the percent of vehicles arriving on green as well as a platoon ratio, which normalizes arrivals on green considering the percent of time the phase was green during the cycle”; deteksi “advance detection that is located in advance of typical queues (e.g., 350 to 400 feet from the stop bar).”
27. NCDOT A.10 (p.33): Approach Delay “calculated as the amount of time between vehicle actuations (converted to arrival time at the stop bar) and when that phase receives a green indication. This delay metric does not consider start-up lost time, deceleration, or standing queues.”
28. NCDOT §5.1: hardware eksternal “Without a connection to the traffic signal controller, there are some events that will not be logged (e.g., termination types).”
29. NCDOT App. C.1: Indiana enumerations “is used across traffic signal controller vendors, ensuring that all controllers are logging events using the same codes in the same structure.”
30. EDC4-FS: “ATSPMs consist of a high-resolution data-logging capability added to existing traffic signal infrastructure and data analysis techniques.”

---

## F. Keterbatasan bahan dan hal yang tidak ditemukan

- NTCIP yang tersedia adalah **v02 (2005)**; objek *priority* (TSP), *event log* hi-res, ATC/SPaT, dan pembaruan v03 (2019) **tidak ada di dokumen**.
- **Tabel kode enumerasi hi-res** (Indiana/Purdue) tidak dimuat di HOP-20-002, NCDOT, maupun factsheet; hanya dirujuk tautannya. Daftar kode di §C.2 adalah pengetahuan umum yang harus diverifikasi.
- **Rumus platoon ratio dan algoritme Link Pivot** hanya dijelaskan naratif; rumus eksplisit tidak ada di dokumen (rujuk Day et al. 2010 dan laporan Purdue TPF-5(258)).
- Halaman SUMO `.md` kehilangan nama atribut; nama diambil dari blok kode `.html`. Daftar lengkap fungsi TraCI dan alur impor OSM tidak ada di dokumen.
- HOP-20-002 adalah laporan *outreach* (workshop, webinar, case study); definisi metriknya tingkat praktisi, bukan spesifikasi komputasi.
- Tidak ada dokumen yang membahas *queue length* sebagai metrik ATSPM standar.

---

## G. Sepuluh temuan terpenting

1. NTCIP 1202 memisahkan tegas **objek kontrol (C)** yang boleh di-SET langsung dari **parameter (P/P2)** yang harus lewat transaksi `dbCreateTransaction` + *consistency check* Annex B — arsitektur ITCS harus meniru pemisahan ini.
2. Seluruh kendali real-time dari pusat bermuara pada sedikit objek: `systemPatternControl`, `systemSyncControl`, `phaseControlGroup{Hold,ForceOff,Omit,Call}`, `ringControlGroup*`, `preemptControlState`, `specialFunctionOutputControl`; dan **backup timer** memaksa central menulis berkala.
3. Status lampu, panggilan, alasan terminasi (gap/max/force-off), posisi siklus, mode free/coord, dan alarm tersedia sebagai bitmask/enum yang ringan untuk di-poll — cukup untuk tampilan TMC, tetapi **bukan** pengganti *hi-res event log*.
4. NTCIP 1202 v02 **tidak memuat** transit priority, event log hi-res, maupun adaptif — fitur unggulan ITCS Jakarta (bus priority, AI adaptif) harus dibangun di central di atas primitif C atau memakai standar lain (NTCIP 1211/1202 v03).
5. Standar hanya mewajibkan grup Phase dan Detector; **pengadaan controller harus mensyaratkan** Coordination, Time Base, Preempt, Ring, Block Object, dan sebaiknya logger hi-res.
6. SUMO `type="NEMA"` memiliki parameter yang sepadan langsung dengan NTCIP (min/max green, passage, yellow, red, ring/barrier, cycle, offset, split, recall, fixed/floating force-off) dan API TraCI `setNema*` — kandidat terbaik untuk *digital twin* dan pengujian SIL.
7. Untuk algoritme adaptif di SUMO, pola yang disarankan adalah program hijau-panjang + `setPhase` ke fase kuning (SUMO mengurus kuning/all-red), atau `setRedYellowGreenState` untuk kendali penuh; *custom conditions* (`earlyTarget`, `z:`, `d:`) sudah cukup untuk TSP sederhana tanpa TraCI.
8. Hasil sumolights: **Max-pressure mengalahkan DQN/DDPG** setelah tuning; controller kaya hyperparameter sangat sensitif — ITCS sebaiknya memulai dari heuristik (Max-pressure/Webster adaptif) dan memakai RL hanya dengan infrastruktur tuning/pelatihan paralel; klaim 57–100 % dari Pan (2023) hanya dibandingkan fixed-time satu simpang.
9. ATSPM berdiri di atas log 0,1 s dengan kode enumerasi Indiana; metrik kunci: Phase Termination, Split Monitor, PCD/AoG/platoon ratio, Split Failure (GOR & ROR5 ≥ 80 %), Approach Delay, AoR, TMC/Volume (PHF/K/D), Ped Delay, Preemption Details, Speed, YRA, Link Pivot, Watchdog — dan jenis detektor menentukan metrik mana yang bisa dihitung.
10. Praktik agensi: ATSPM adalah *observer* independen untuk mengevaluasi sistem adaptif (termasuk AI), memerlukan proses bisnis (alert → work order → retiming), akses raw data, dan perencanaan storage (~9 GB/hari untuk ~390 sinyal); pipeline ATSPM yang sama harus dipakai untuk log lapangan dan log simulasi agar pengembangan algoritme bisa divalidasi sebelum ke lapangan.
