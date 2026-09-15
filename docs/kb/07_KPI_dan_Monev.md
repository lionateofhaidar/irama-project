# 07 — Katalog KPI & Monitoring-Evaluasi

**Cara pakai.** Daftar KPI yang harus dihitung ITCS, dikelompokkan per domain. Kolom: definisi/rumus · sumber data · agregasi · ambang/target · audiens (Pub = publik, Pim = pimpinan, Eng = engineer, Tek = teknisi) · tahap saran. Ambang hanya dari sumber; yang belum ada di korpus ditandai "tetapkan". Bagian akhir: desain evaluasi dan skema pelaporan wajib. Kolom tahap mengikuti tahapan kanonis `docs/planning/04` dan diselaraskan pada 2026-09-15 dengan `docs/planning/05`; nilai yang berubah ditandai "(dulu …)" menurut skema lama 2026-09-12.

Tag: PKJI = PKJI 2023 (R05 D); PM96 = Permenhub 96/2015 (R00 E); STM2/TSTM/NCDOT = R01; TSPH = R02 G; HOP = FHWA HOP-20-002 & NCDOT ATSPM (R03 C); MSE = R02; R06 = TSP/EVP/Jakarta; Perda = Perda DKI 5/2014; Perpres = Perpres 55/2018.

---

## A. Kinerja lalu lintas simpang (PKJI 2023 / MKJI 1997 / PM 96) — kepatuhan regulasi

| KPI | Definisi / rumus | Sumber data | Agregasi | Ambang / target | Audiens | Tahap |
|---|---|---|---|---|---|---|
| Arus jenuh J | J = J0·FHS·FUK·FG·FP·FBKi·FBKa; J0 = 600·LE (tipe P) / diagram (tipe O); FUK Jakarta 1,05 | geometri + survei | per pendekat | — | Eng | T1 |
| Kapasitas pendekat C | C = J·wH/s | plan aktif + J | per pendekat/periode | — | Eng | T1 |
| Derajat kejenuhan DJ | DJ = q/C | volume (detektor/kamera/survei) | 15 menit / jam / periode plan | **DJ ≤0,85** desain (PKJI); ≥1,0 jenuh | Eng, Pim | T1 |
| Rasio arus simpang RAS & siklus Webster | RAS = Σ(q/J)kritis; s = (1,5·wHH+5)/(1−RAS) | — | per plan | siklus 40–130 s; hijau ≥10 s; kuning 3 s | Eng | T1 |
| Antrian Nq, panjang antrian PA | Nq = Nq1+Nq2 (PKJI 5-15…5-17); PA = Nq·20/LM (m) | volume + plan (atau kamera) | per pendekat/siklus | PA ≤ panjang link/storage (spillback) | Eng, Tek | T1 (hitung), T2 (ukur) |
| Rasio kendaraan terhenti RKH, NKH | RKH = 0,9·Nq·3600/(q·s); NKH = q·RKH | — | per pendekat/jam | — | Eng | T1 |
| Tundaan TLL, TG, T, TI | TLL = s·0,5(1−RH)²/(1−RH·DJ) + Nq1·3600/C; TG = (1−RKH)·PB·6 + RKH·4; T = TLL+TG; TI = Σ(q·T)/qTotal | — | per pendekat & simpang | → LOS | Eng, Pim, Pub | T1 |
| **LOS simpang (PM 96/2015)** | kelas dari tundaan/kend: A <5; B 5–15; C 15–25; D 25–40; E 40–60; F >60 s | TI | per simpang/periode | target min: arteri primer ≥B, arteri/kolektor sekunder ≥C, lokal ≥D | Pub, Pim | T1 |
| LOS ruas (PM 96) | berdasarkan kecepatan: A ≥80 … F <30 km/jam (perkotaan E ≥10) | probe/travel time | per ruas | target per fungsi jalan | Pim | **T3** (kecepatan antarkamera), **T5** (probe) (dulu T2) |
| V/C ruas | volume/kapasitas ruas | detektor/probe + PKJI ruas | per ruas/jam | ambang kebijakan: 0,5 (motor), 0,65 (u-turn), 0,7 (pembatasan), 0,85 (SSA), 0,9 (ERP/tidal) | Eng, Pim | **T3** (dulu T2) |
| Padanan HCM (benchmark) | control delay & LOS HCM (A ≤10 … F >80 s) — rumus perlu HCM Ch.19 (tidak di korpus) | — | — | hanya benchmark | Eng | T3 |

## B. ATSPM (high-resolution 0,1 s) — operasi harian

| KPI | Definisi / rumus | Data/detektor | Agregasi | Ambang | Audiens | Tahap |
|---|---|---|---|---|---|---|
| Phase termination | klasifikasi per fase/siklus: gap-out / max-out / force-off / skip / ped | event log saja | per siklus → per jam/plan | max-out malam hari → detektor rusak (Watchdog >90 % dari ≥50 aktivasi 01–05) | Eng, Tek | **T4** (dulu T2) |
| Split monitor | durasi aktual fase (begin green → end red clear) vs programmed split | event log | per siklus/fase | split failure / double serving berlebih | Eng | **T3** (durasi aktual dari status lampu kamera), **T4** (terhadap split terprogram) (dulu T2) |
| Ped delay | waktu ped call → Walk | event log ped | min/max/avg per plan/hari | stuck ped >200 aktuasi 01–05 | Eng, Tek | **T3** (dulu T2) |
| Preemption/priority details | request, service, time-to-service, dwell, end; jumlah & durasi | event log preempt/priority | per hari | false preemption = KPI kesehatan (TSPH Tab.46) | Eng | **T4** (dulu T2 preempt, T3 priority) |
| Purdue Coordination Diagram, **% Arrivals on Green (AoG)**, platoon ratio | titik kedatangan advance detector pada waktu-dalam-siklus; AoG = kedatangan saat hijau/total; platoon ratio = AoG dinormalisasi porsi hijau | advance detection 350–400 ft (≈110–120 m) sebelum antrian | per fase koordinasi/plan/hari; tren bulanan | contoh: AoG 53 % → 87 % setelah offset (STM2); arrival type ≤0,5 very poor … >2,0 exceptional (TSPH Tab.49) | Eng, Pim | **T4** (dulu T2 bila detektor, T3) |
| Arrivals on Red (AoR) | jumlah/% kedatangan saat merah | advance | per fase/jam | tren | Eng | T3 |
| Approach delay | Σ(t hijau − t tiba stop bar) per kendaraan (tanpa start-up lost time) | advance | per fase/jam | — | Eng | T3 |
| **Purdue split failure** | GOR = occupancy stop-bar selama hijau; ROR5 = occupancy 5 s pertama merah; failure bila **GOR ≥80 % & ROR5 ≥80 %** | stop-bar presence | per fase/siklus → per plan/hari | 0 target; naik → split/adaptif perlu | Eng | T3 |
| TMC / approach volume, PHF, K, D | hitungan per lajur/lane group 15 menit; PHF; K-factor; D-factor | lane-by-lane count | 15 menit | volume nol tiba-tiba → detektor rusak | Eng, Tek | **T2** (dulu T2/T3) |
| Approach speed | rata-rata & persentil-85 | radar/probe | per jam | vs speed limit | Eng | T3 |
| Yellow & red actuations (YRA) | kendaraan masuk saat kuning / red clearance / fase konflik aktif (severe) | past-stop-bar/stop-bar + kecepatan | per fase/hari | red-light running → keselamatan | Eng, Pim | T3 |
| Link Pivot | Link Delta (offset yang memaksimalkan AoG prediksi) per pasangan simpang → new offset | advance di simpang berurutan | per koridor/periode | — | Eng | **T5** (dulu T3) |
| Watchdog | no data <500 rekaman/24 jam; force-off/max-out >90 % (≥50 aktivasi 01–05); advance counts <100 kend 17–18; stuck ped >200 (01–05) | event log | harian | default HOP p.20 (dapat diubah) | Tek | **T4** (dulu T2) |

## C. Koridor / jaringan (probe, Bluetooth, HRCD)

| KPI | Definisi | Data | Agregasi | Ambang / target | Audiens | Tahap |
|---|---|---|---|---|---|---|
| Travel time & average speed koridor | waktu tempuh end-to-end / kecepatan rata-rata (space mean speed) | probe GPS (TJ/ojol/navigasi, penetrasi 3–6 % diagregasi ≥4 minggu), Bluetooth, floating car ≥6 run/arah | per koridor/arah/periode/hari-minggu | **35 km/jam** rata-rata jaringan (Perda Ps.8); **≥30 km/jam** jam puncak 2029 (Perpres 55); NCDOT target −40 %/−20 % travel time | Pub, Pim | **T3** (waktu tempuh antarkamera), **T5** (koridor dari probe) (dulu T2) |
| Reliability: 95th percentile, buffer time/index, planning time/index | TT95 − TTmean; (TT95 − TTmean)/TTmean; TT95/TTfree | probe | per koridor/periode | tetapkan | Pim, Eng | **T5** (dulu T2) |
| Stops per km, stop delay | dari trajektori (kecepatan <ambang) | probe | per koridor | pengguna merasakan stop dulu (STM2) | Eng, Pub | **T5** (dulu T2) |
| Travel time index, delay per kendaraan | t/t_free ; t − t_free | probe | per OD path | — | Eng | **T5** (dulu T2) |
| Cyclic time-space diagram, PPD, SOFT, speed heat map | visual progression (τ = t mod C) | probe + cycle length persis | per koridor/plan | — | Eng | **T5** (dulu T2) |
| Bandwidth efficiency / attainability | (B_A+B_B)/(2C); bandwidth/g_crit | plan | per koridor | PASSER: 0,25–0,36 baik; ≥0,37 sangat baik | Eng | **T4** (dulu T2) |
| Throughput input/output (jenuh) | kendaraan masuk vs keluar sistem per periode | detektor perimeter | per kawasan | loading/oversaturated/recovery | Eng | **T5** (dulu T4) |
| Akumulasi regional (MFD) | n(k) kendaraan dalam region | kamera/probe | per region/menit | setpoint n̂ perimeter control | Eng | **T5** (dulu T4) |
| Emisi/BBM (model) | dari stops & delay (mis. SimTraffic/model) | KPI di atas | per koridor | green wave: CO2/NOx/PM −10…−40 % (survei, sekunder) | Pub, Pim | **T2** (sederhana per simpang), T3 (lengkap) (dulu T3) |
| TomTom index (konteks) | congestion level %, waktu per 10 km | eksternal | tahunan | konteks, bukan KPI internal | Pub | T2 |

## D. Transit (TSP) & darurat (EVP)

| KPI | Definisi | Data | Ambang / benchmark | Audiens | Tahap |
|---|---|---|---|---|---|
| Bus travel time & variabilitas koridor | rata-rata & CV per periode | AVL | benchmark −10…−25 % TT, −19…−50 % variabilitas (TSP Handbook) | Pim, Eng | **T4** (dulu T3) |
| Bus signal delay | delay di simpang ber-TSP | AVL + event | −40 % (dengan retiming) | Eng | **T4** (dulu T3) |
| Headway adherence / schedule adherence | deviasi headway; on-time (x=0, y=3–5 menit) | AVL | tetapkan (TJ berbasis headway) | Pim | **T4** (dulu T3) |
| Permintaan prioritas: diminta/diberikan/ditolak, detik diberikan, lockout, recovery | dari PRS log | ITCS | 1 aktivasi/siklus; recovery ≤2 siklus | Eng | **T4** (dulu T3) |
| Dampak side-street (delay/kendaraan/siklus) | dari split monitor/approach delay | ATSPM | tipikal "1 s/kend/siklus"; T414: side-street delay +3,4–6 % | Eng | **T4** (dulu T3) |
| Passenger delay / person delay | Σ occupancy × delay | APC + delay | OCC-MP: PTT −0,1…−3,6 % | Eng | **T5** (dulu T4) |
| EVP: aktivasi, durasi, time-to-service, response time (dari CAD), pencapaian target respons | log preempt + CAD | ITCS + CAD | durasi tipikal ~25 s; target 96 % tepat (Humagain); response time −14…−23 % | Pim, Eng | **T4** (dulu T3) |
| Side-street recovery pasca-preempt | siklus sampai normal | event log | ≤1–2 siklus (VT); peringatan 30 s–7 menit (DC) | Eng | **T4** (dulu T3) |
| False preemption/priority | aktivasi tanpa kendaraan | log | KPI kesehatan | Tek | **T4** (dulu T3) |

## E. Kesehatan perangkat & komunikasi

| KPI | Definisi | Ambang / sumber | Audiens | Tahap |
|---|---|---|---|---|
| Uptime komunikasi per simpang (% poll sukses) | poll sukses/gagal/bad | tetapkan (demand ≤50 % kapasitas throughput, TSPH) | Tek, Pim | **T4** (dulu T1) |
| % detektor berfungsi per mode/simpang | detektor tanpa fault (NTCIP alarms, Watchdog, count profile) | KPI PM utama (TSPH Tab.46) | Tek, Pim | **T3** (% kamera sehat), **T4** (% detektor) (dulu T1) |
| % sinyal offline / durasi offline / flash status / power failure | status controller | — | Tek | **T3** (lampu mati atau kedip dari kamera), **T4** (status controller) (dulu T1) |
| Frekuensi & durasi transisi | dari event pattern change/offset | ≥30 menit per pattern; selesai ≤3–5 siklus | Eng | **T4** (dulu T2) |
| Clock drift, parameter mismatch vs DB, timing irregularity | status & upload blok | 0 | Tek | **T4** (dulu T2) |
| Conflict/flash events, kabinet door alarm | status/alarm | 0 | Tek | **T4** (dulu T1) |
| MTTR, response time, emergency calls/simpang/tahun, % fixed with inventory | work order | TSPH G.4 | Pim, Tek | **T3** (dulu T2) |
| Kepatuhan pemeliharaan berkala (≤6 bulan) & umur teknis (≤5 th) | asset | 100 % | Pim | **T3** (dulu T1) |
| Kualitas data relatif (dampak detector fault) | MSE Req 6.0-8 | dilaporkan per KPI | Eng | T2 |

## F. Layanan & program

| KPI | Definisi | Ambang | Audiens | Tahap |
|---|---|---|---|---|
| SLA keluhan | waktu tiket → selesai | **≤3 jam** (Dishub DKI, CRM); STM2 respons ≤1 minggu | Pub, Pim | **T3** (dulu T2) |
| Retiming age | waktu sejak retiming terakhir per simpang | ≤3 tahun (NTOC); ≤3 bulan tinjau timing (Dirjen 273) | Eng | T2 (tanggal kajian terakhir), **T4** (pelacakan retiming per simpang) (dulu T2) |
| Jumlah simpang ITCS aktif vs target | 65 → 321 (2030) | milestone RPP | Pub, Pim | **T4** (dulu T1) |
| Cakupan mode kendali | % simpang adaptif/terkoordinasi/TOD/flash | — | Pim | **T4** (dulu T1) |
| Manfaat tahunan (NCDOT CBA) | Delay = Σ vol puncak × Δdelay/3600 × nilai waktu × 250 hari; Stops = Σ vol × Δstops × biaya stop × 250 | B/C 40:1 rujukan | Pim | T2 |
| Modal share angkutan umum, waktu perjalanan angkutan umum jam puncak | data Jak Lingko | 60 % (Perda/Perpres); ≤90 menit (Perpres) | Pim | T4 |
| Keselamatan | kecelakaan/konflik per simpang, RLR (YRA), max-out/force-off frequency | crashes −35 % (T414) benchmark; EB before–after | Pim, Eng | T3 |
| Pelatihan & kompetensi | % operator tersertifikasi/bimtek | PM 76 Ps.21 | Pim | **T4** (dulu T2) |

## G. Desain evaluasi

1. **Before–after** (PM 96 Lamp. I VI wajib): "before" saat plan lama, "after" setelah perubahan; rentan musim → lengkapi dengan **on/off bergantian hari** (adaptif ON vs TOD OFF pada musim sama; Park City hasil lebih adil) (T414 hlm.58–60; NYSERDA hlm.2).
2. **Bertahap:** sebelum → setelah retiming/optimasi konvensional → setelah adaptif/TSP; **pisahkan manfaat retiming dari manfaat sistem** (TSPH hlm.56).
3. **Statistik:** multi-hari, hindari Senin/Jumat/cuaca buruk/event; ≥6 run floating car/arah/periode; simulasi ≥N seed dengan confidence interval (TSP Handbook Bab 15; NCDOT).
4. **Keselamatan:** Empirical Bayes before–after (HSM via NYSERDA hlm.17).
5. **MOE per periode** (AM, midday, PM, akhir pekan, event) & per level (simpang, koridor, jaringan); KPI side-street & multimodal wajib (T414: dinilai kurang meyakinkan agensi).
6. **ATSPM sebagai observer independen** untuk sistem adaptif/AI (HOP p.29); shadow mode untuk RL (R04 A.3).
7. **Definisikan MOE & metode sebelum klaim** — klaim Jakarta "+20–30 %", "15–20 %" tidak disertai metode (R06 D).

## H. Skema pelaporan wajib

| Laporan | Isi minimum | Penerima | Frekuensi | Dasar |
|---|---|---|---|---|
| Laporan pelaksanaan MRLL | analisis, evaluasi, LOS before–after per kebijakan | Forum LLAJ | tiap kebijakan / berkala | UU 22/2009 Ps.98; PM 96 Lamp. I VI |
| Laporan MRLL jalan nasional DKI | kecepatan rata-rata, V/C, dampak jaringan | Dirjen Hubdat / BPTJ | ≥1×/tahun (+evaluasi Dirjen tahunan) | PM 96 Ps.5(2), Lamp. III |
| Laporan monev Jak Lingko | 18 jenis data, SPM | Gubernur | tiap 3 bulan (BUMD bulanan) | Pergub 68 Ps.15 |
| Evaluasi MKLL (ganjil-genap/ERP) | V/C, kecepatan, efektivitas (kenaikan kecepatan rata-rata) | Gubernur/DPRD | tahunan | PP 32 Ps.63(2); Perda Ps.81(2) |
| Penilaian kinerja transportasi | KPI jaringan (35 km/jam, 60 %) | Kepala Dinas → Gubernur | tahunan | Perda Ps.237 |
| Laporan efektivitas SMTC | pemantauan & analisis efektivitas, tindakan korektif | Menteri/BPTJ | sesuai pembinaan | PM 76 Ps.22–24 |
| Penilaian kinerja aset APILL | dasar penghapusan (umur ≤5 th) | Pejabat berwenang | per aset | PM 49 Ps.42 |
| Dashboard publik | KPI terdefinisi + metode | masyarakat | real-time/harian | UU Ps.250; Perda Ps.233 |
| Project benefit summary | manfaat tahunan, B/C | pimpinan | tahunan | TSPH G.5; NCDOT CBA |

---

**Pointer ke detail:** R05 D (rumus PKJI lengkap & prosedur), R00 G (Dirjen 273 formulir & LOS), R03 C.3 (algoritma tiap metrik ATSPM), R01 G (ukuran kinerja, monitoring, equipment monitoring Exh.8-16, keluhan Exh.8-17), R02 E–F (V&V, MOE, benefit evidence), R06 F.3 (KPI publik/internal Jakarta), R04 A.19 (metode probe).
