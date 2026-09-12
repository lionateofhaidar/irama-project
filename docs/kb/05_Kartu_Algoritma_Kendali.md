# 05 — Kartu Algoritma & Mode Kendali

**Cara pakai.** Satu kartu per algoritma/mode kendali sinyal. Bidang: Tujuan · Input/detektor · Parameter & default · Pseudocode · Constraint/guard-rail · Bukti kinerja · Kesiapan deploy · Tahap saran · Cara uji. Angka hanya dari sumber (tag dalam kurung). Nilai default adalah **titik awal** dari praktik luar negeri/pedoman Indonesia; belum ada angka kalibrasi Jakarta dalam korpus. Lihat pohon keputusan dan hierarki fallback di akhir.

Tag: STM2 = NCHRP 812 (R01); TSTM = FHWA 2008 (R01); MSE = FHWA HOP-11-027 (R02); T414 = NCHRP 20-07/414 (R02); Dirjen273 = Kep. Dirjen 273/1996 (R00 G); PKJI = PKJI 2023 (R05 D); PM49/PM96 = Permenhub (R00); NTCIP = R03 A; SUMO = R03 B; ATSPM = R03 C; paper = R04 A.x.

---

## K-01 Fixed-time / Time-of-Day (TOD) plans — Webster/Dirjen 273/PKJI 2023
- **Tujuan:** baseline & fallback wajib; rencana siklus tetap per periode hari (PM49 Ps.14: ≥8 rencana siklus).
- **Input:** volume per gerakan per periode (LHRT × K, K 7–12 %), geometri (LE/We), komposisi (EMP), kelandaian, parkir, hambatan samping. Tanpa detektor.
- **Parameter & default:** kuning 3,0 s (PKJI hlm.112); all-red = waktu pengosongan (rumus Dirjen273/PKJI 5-9; V 10 m/s, 3 m/s KTB, 1,2 m/s ped); wAH normal 4/5/6 s (lebar 6–<10 / 10–<15 / ≥15 m); siklus 2 fase 40–80 s, 3 fase 50–100 s, 4 fase 80–130 s, >130 s dihindari; hijau ≥10 s; cadangan hijau 10 %; DJ target ≤0,85; FUK Jakarta 1,05.
- **Pseudocode:** hitung S/J per pendekat → FR=q/J → FR_crit per fase → IFR=ΣFR_crit → LT=Σ(kuning+all-red) → c=(1,5·LT+5)/(1−IFR) → g_i=(c−LT)·PR_i → C=S·g/c → DJ; jika DJ>0,85 ubah fase/lebar/larangan belok → ulangi. Simpan sebagai pattern (cycle, split, offset, sequence) per TOD.
- **Guard-rail:** tinjau ulang timing ≥1×/3 bulan (Dirjen273 I.H); retiming ≤3 tahun (NTOC); jangan siklus panjang untuk "menambah kapasitas" (120→180 s hanya +2 % kapasitas, TSTM Gb.6-16; hijau >30 s menurunkan arus jenuh, STM2 12-7).
- **Bukti:** retiming saja −10 % delay (TSTM); B/C 40:1 (NCDOT); fixed-time bisa lebih baik dari adaptif pada volume rendah (TSTM §9.4).
- **Kesiapan:** sangat tinggi. **Tahap:** T1 (kalkulator & plan mgmt), T2 (TOD via central).
- **Uji:** hitung ulang contoh Yogyakarta Dirjen273 Bab X (c=70 s, g1=28, g2=30, DS=0,44) sebagai test case; SUMO static tlLogic + ATSPM split monitor.

## K-02 Actuated ring-barrier (fully/semi-actuated) + volume-density
- **Tujuan:** merespons kehadiran kendaraan; near-optimal delay untuk kedatangan acak di simpang terisolasi (STM2 §3.1.2; taxonomy §II.2).
- **Input:** detektor presence stop-bar (zona 6–80 ft) dan/atau setback (decision zone 5,5–2,5 s travel time); ped button.
- **Parameter & default (STM2 §6):** min green 2–15 s per tipe (Gq=3+2n tanpa stop-bar); max green 15–70 s (Gmax=(V·C)/(1200·n)+1, min 15 s); passage time 0–3 s (PT=MAH−(Lv+Ld)/v, MAH 3,0/4,0 s); gap reduction: time before reduction ≥10 s, time to reduce ≈½(max−min), min gap 2,0 s; variable initial 1,2–2,0 s/aktuasi; walk 4/7/10–15 s; FDW=Dc/3,5−(Y+R); recall: soft recall fase 2&6; memory non-locking default; detector delay 2–5 s (kiri), 8–12 s (RTOR); extend ≤2 s.
- **Pseudocode (per fase aktif):** `if minGreen expired AND conflictingCall AND passageTimer expired → gap-out; elif greenTime ≥ max (dengan conflicting call) → max-out; passageTimer reset tiap aktuasi; setelah TBR/CBR, allowableGap turun linier ke minGap`. Dual entry & simultaneous gap sesuai flag NTCIP phaseOptions.
- **Guard-rail:** detektor gagal → continuous call → max recall (STM2 6-8); ped clearance tidak dipotong max green (6-17); LPI ≥3 s.
- **Bukti:** state of practice; ASCT unggul vs semi-actuated −34,9 % delay, vs fully-actuated −24,1 % (T414 hlm.69–70) — artinya actuated yang ditala baik sudah dekat.
- **Kesiapan:** sangat tinggi (fungsi controller). **Tahap:** T3 di digital twin & controller NTCIP; T4 lapangan luas.
- **Uji:** SUMO `type="actuated"`/`NEMA` (minDur/maxDur/vehext) + ATSPM phase termination (gap/max ratio).

## K-03 Actuated-coordinated (COS + force-off/permissive) & transisi
- **Tujuan:** koordinasi arteri/green wave sambil mengaktuasi fase minor (STM2 §7).
- **Input:** pattern (cycle, split, offset, sequence), master clock (GPS/NTP), detektor fase minor, arrival-on-green untuk fine-tuning.
- **Parameter & default:** cycle 60–120 (150) s; Σsplit ≤ C; force-off floating (default) / fixed (mengurangi early return); permissive simultaneous/sequential otomatis; offset reference = awal kuning fase koordinasi pertama (teramati); sync reference 03:00; transition mode shortway (add-only bila ada preemption); batas penyesuaian per siklus ±20 %; ≥30 menit per pattern; selesai ≤3–5 siklus; mulai plan puncak lebih awal.
- **Pseudocode:** `localZero = masterClock − offset; tiap fase non-koord: terminasi maks di forceOff_i; fase koord dijamin hijau minimum = split − yield; saat pattern berubah: pilih dwell/add/subtract/shortway → geser ≤20 %/siklus hingga |Δoffset|<ε`.
- **Guard-rail:** jangan koordinasi terlalu malam (keluhan minor street); early return to green → geser offset/fixed force-off; ped tak cukup split → transisi lebih baik daripada layani ped tiap siklus (§7.5.1).
- **Bukti:** NCDOT target −40 % travel time koridor baru, −20 % retimed; transisi = periode paling tidak efisien (NCDOT Tab.3).
- **Kesiapan:** sangat tinggi. **Tahap:** T3 (koridor pilot), T4.
- **Uji:** SUMO NEMA `coordinate-mode` + `setNemaOffset`; ATSPM PCD/AoG, Link Pivot; KPI jumlah & durasi transisi.

## K-04 Traffic Responsive Plan Selection (TRPS) — 1-GC
- **Tujuan:** memilih pattern dari pustaka berdasarkan detektor sistem, bukan jam (STM2 §9.3; TSTM §9.3).
- **Input:** detektor sistem setback/exit-side, zona kecil (6×6 ft), per lajur; volume V & occupancy O per detektor.
- **Parameter:** K (skala occupancy→volume; K=17 di exit side, 5–7 dekat stop bar); bobot w_i; smoothing 50 %; ambang masuk/keluar dengan hysteresis (contoh offset 2→3 masuk 52 keluar 49); min waktu dalam plan; perubahan ≥30 menit persisten; matriks 6 cycle/split × 5 offset = 30 pattern.
- **Pseudocode:** target-based: `err_j = Σ_i w_i·|(V_i+K·O_i) − T_ij|; pilih j dengan err terkecil jika < x % dari plan berjalan`; threshold-based: `CC = Σ w_i(V_i+K·O_i); indeks cycle ∝ volume arteri, split ∝ rasio arteri/minor, offset ∝ inbound/outbound; ganti bila CC melewati ambang masuk & tetap di atas ambang keluar`.
- **Guard-rail:** terlalu banyak detektor gagal → TRPS nonaktif; lambat merespons insiden mendadak.
- **Bukti:** kualitatif (manual); efektif untuk perubahan besar & persisten.
- **Kesiapan:** tinggi (fitur central/master). **Tahap:** T3.
- **Uji:** SUMO WAUT/`setProgram` dipicu skrip; validasi frekuensi pergantian.

## K-05 Adaptif generasi-2 ala SCOOT/SCATS (split/offset/cycle optimizer, hierarkis)
- **Tujuan:** menyesuaikan COS online berdasarkan deteksi; standar industri deployed global (paper A.1; TSTM §9.4).
- **Input:** SCOOT: stop-line + advance 150–1.000 ft (cyclic flow profile); SCATS: hitung stop-line + gap (degree of saturation).
- **Parameter:** SCOOT: split optimizer geser beberapa detik untuk minimalkan DS; offset optimizer per siklus; cycle optimizer per region (target node terpadat 90 % saturasi); SCATS: pilih split plan dari pustaka & skala pada rentang cycle. Batas pencarian ASCT: split ±5 s, cycle +10–20 s per langkah (STM2 9-13).
- **Pseudocode (generik "download parameter"):** `tiap siklus: ukur DS/queue per pendekat → split_baru = argmin ΣDS dalam ±5 s → offset_baru = argmin stops dari CFP → cycle_region = f(DS maks, 90 %) → download pattern; controller tetap gap-out/force-off`. Alternatif "override": kirim hold/force-off tiap detik (rolling horizon 60 s/5 s).
- **Guard-rail:** parameter terkunci (sequence/skip), min/max, kembali ke TOD bila detektor/komunikasi gagal (MSE Req 2.1.1.0-x).
- **Bukti:** manfaat rata-rata ≥10 %, hingga ≥50 % pada timing usang/jenuh (EDC-1); SCOOT Toronto delay −17 %, stops −22 %; SCATS Oakland County travel time −6,7 %, stops −26,5 %; T414: stops −7,8 % … split failure −85 %, side-street delay +3,4 %, crashes −35 %. Lebih baik pada AADT 35–55 ribu daripada >55 ribu.
- **Kesiapan:** produk komersial (proprietary). **Tahap:** T4 (bila membeli/menyamai), atau diganti K-06 sebagai versi terbuka.
- **Uji:** SIL di SUMO + ATSPM sebagai observer independen (HOP-20-002 p.29); on/off bergantian hari.

## K-06 Cyclic Max-Pressure terkoordinasi (Tsitsokas 2022) + node selection + perimeter control
- **Tujuan:** adaptif real-time terbuka & deployable: cycle & offset tetap per koridor (green wave terjaga), MP hanya mengalokasikan split; stabil (maximum stability, Varaiya 2013 via paper A.4–A.5).
- **Input:** antrian/occupancy per link masuk & keluar (kamera AI/loop/probe), kapasitas link c_z, turning ratio β (diestimasi online tiap 15 menit), saturation flow S_z.
- **Parameter & default (A.5):** pressure link `p_z = (x_z/c_z − Σ_w β_zw x_w/c_w)·S_z`; `P_j = max(0, Σ_{z∈v_j} p_z)`; green mentah `g̃_j = P_j/ΣP_i · G_n`; proyeksi QP integer: min green ≥7 s (sesuaikan ped), Σg + L = C, |Δg| ≤5 s/siklus. Node selection skor `R_n = α·mean_occ + β·var_occ + γ·N_c` (fraksi waktu ≥80 % kapasitas); MP di 10–25 % node kritis. Perimeter control: PI `u(k)=u(k−1) − K_P[n(k)−n(k−1)] − K_I[n(k)−n̂]` aktif dekat setpoint (hysteresis), green gerbang ≥15 % saturation flow.
- **Pseudocode:** `tiap siklus C_n: hitung p_z semua link; P_j per fase; g̃; g = QP_project(g̃, gmin, gmax, Δ≤5, integer, Σ=C−L); download split; (opsional) region CBD: n(k) akumulasi → u(k) → bagi ke gerbang berbobot antrian`.
- **Guard-rail:** urutan fase tetap; cycle/offset tidak diubah oleh MP; rate-limit; fallback ke split TOD bila data hilang; hindari MP 100 % node pada high demand (gain ≈0).
- **Bukti (Barcelona 565 simpang, mesoscopic):** medium demand VHT −14,5 % (10 % node), −18,8 % (25 %), −10,6 % (100 %); high demand MP 100 % −0,2 %, PC −7,6 %, PC+MP25 % −15,6 %. sumolights: MP travel time 59 s vs DQN 78, DDPG 72, Webster 71, SOTL 158 (R03 B.10). CityLight: MP mengalahkan semua baseline RL lain (A.13).
- **Kesiapan:** tinggi (heuristik sederhana; uji lapangan TT-MP dilaporkan A.4/A.7; Barcelona = simulasi).
- **Tahap:** T3 (1–2 koridor pilot, shadow → live off-peak), T4 (jaringan + PC).
- **Uji:** SUMO NEMA + `setNemaSplits` per siklus; ATSPM split failure/AoG; bandingkan vs K-03 on/off.

## K-07 D-MP / probe-based Max-Pressure (Liu & Gayah 2022)
- **Tujuan:** MP dengan metrik delay (dari probe/GPS) alih-alih hitungan antrian.
- **Input:** delay per link pada interval sebelumnya T (5 s optimal), probe penetrasi ≥50–70 % untuk unggul (A.4).
- **Parameter:** T=5 s; lost time 3 s; acyclic (urutan fase acak) → tidak disarankan lapangan tanpa cyclic wrapper.
- **Bukti:** total delay D-MP 184,8 s vs Original-MP 290,8 s (−13 % s.d. −36 %) di grid 4×4 SUMO; penetrasi 10 % dibuang (varian besar).
- **Kesiapan:** rendah–sedang (acyclic; butuh probe tinggi). **Tahap:** T5 (riset) atau sebagai sumber pressure tambahan di K-06.
- **Uji:** SUMO CV penetrasi variabel.

## K-08 OCC-MP / Transit-MP / mTransit-MP — TSP kondisional berbasis occupancy (A.6, A.7)
- **Tujuan:** prioritas bus berdasarkan muatan tanpa merusak stabilitas jaringan; menangani CV jarang & halte.
- **Input:** occupancy bus (APC) atau asumsi (mobil 1,5 pnp), posisi GPS bus & status halte (δ_v=0 bila belum lewat halte terdekat), normalized link travel time τ_v; fallback historis (λ̂, ρ̂, IQA) untuk link tanpa observasi.
- **Parameter:** update 10 s; yellow 3 s; segmentasi link ≈420 m; ambang tidak memberi prioritas bila kaki lawan DJ >0,85 / antrian melebihi link (R06 F.2); robust error APC σ≤40 %.
- **Pseudocode:** `w(l,m) = occ_upstream · [x(l,m) − Σ r·x(m,n)]⁺; P_φ = Σ w·C·S; pilih φ*=argmax P (acyclic) atau alokasikan split (cyclic)`. Transit-MP: `state_up = Σ δ_v·p_v·τ_v; state_down = Σ δ_v·τ_v`; tanpa CV → estimasi historis.
- **Guard-rail:** jangan konstanta prioritas absolut (RB-MP: mobil +3,5–25,8 %); bus di halte tidak memicu; batasi frekuensi per siklus; ped minimum.
- **Bukti:** OCC-MP: bus −14,5 %/−7,5 %, mobil +0,36–2,64 %, PTT −0,1…−3,6 %; Transit-MP: passenger delay −31,6 % (efek halte) lalu −17,9 %; spillover −94 %; bekerja hingga penetrasi 0,1 (mTransit-MP).
- **Kesiapan:** sedang–tinggi (butuh AVL/APC — TransJakarta punya). **Tahap:** T3 rule-based (green ext/early green + AVL headway), T4 OCC/Transit-MP di atas K-06.
- **Uji:** SUMO custom condition bus (`d:`/`z:` detektor busType) → lalu TraCI; KPI bus delay, passenger delay, side-street delay.

## K-09 TSP rule-based (green extension / early green) — TSP Handbook
- **Tujuan:** prioritas bus sederhana kompatibel controller NEMA/NTCIP 1211.
- **Input:** check-in 100–150 m/~15 s hulu (GPS/optical/RF), check-out stop line; AVL keterlambatan/headway.
- **Parameter & default (R06 F.2):** extension maks 10 s (7–20); truncation maks 10 s (≤20), tidak melampaui min green + Walk + FDW fase lain; 1 aktivasi/siklus/pendekat; lockout siklus berikutnya; recovery ≤2 siklus tanpa lepas koordinasi; kondisional: terlambat ≥2 menit atau headway ≥ rencana + 2 menit; evaluasi tiap ≤6 s; 4 level keterlambatan; bus non-revenue dikecualikan.
- **Pseudocode:** `on check-in(bus): if !eligible(bus) return; if phase_bus == GREEN and remaining < ext_max → extend ≤ ext_max until check-out; elif RED → truncate non-priority phases to min (respect ped) → early green; set lockout(next cycle); log request`.
- **Guard-rail:** Y/R & ped tak dipotong; detik prioritas tertulis di MoU; EV preempt meng-override.
- **Bukti:** bus travel time −10…−25 %, variabilitas −19…−50 %, signal delay −40 % (dengan retiming); dampak mobil "1 s/kendaraan/siklus".
- **Kesiapan:** sangat tinggi. **Tahap:** T3.
- **Uji:** SUMO condition `earlyTarget="NSbus"`; ATSPM preemption/priority details; before–after bus travel time dari AVL.

## K-10 EVP bertingkat (Humagain & Sinha 2020) + urutan NTCIP preempt
- **Tujuan:** preemption darurat hanya bila target respons terancam; resolusi konflik multi-EV.
- **Input:** posisi/kecepatan EV (AVL/CAD, geofence GPS per simpang), level kritikalitas (purple/red/orange), rute.
- **Parameter:** target waktu t_target = d/v_limit·a_level (level 1/1,5/2); preempt bila Δ = t_cur − t_target > 0; green reserve dari posisi/kecepatan; urutan NTCIP: preemptDelay (0), min green ≥2 s, walk/FDW boleh dipotong (bukan untuk priority), Y/R tidak; track clearance → dwell (limited service disukai) → exit phase; preemptMaxPresence; prioritas rel > EV; recovery: return to coordinated/queue delay recovery.
- **Pseudocode:** `on EV_update: Δ = d/v_now − t_target; if Δ>0: reserve green at next intersections along route; if conflict with other EV at node → conflict graph → serve higher level/earlier; if current phase green → extend, else → transition (respect Y/R) → dwell until check-out → exit → recovery`.
- **Guard-rail:** durasi preempt tipikal ~25 s; pemulihan koordinasi bisa 30 s–7 menit (peringatan); preempt confirmatory light; cakupan: pemadam wajib, ambulans per kebijakan, VVIP terkonfigurasi (PM 76 Ps.7(4)a).
- **Bukti:** EV 96 % tepat target; antrian −36 % vs absolute preemption; non-EV wait ≈ tanpa preemption (A.18); EVP menurunkan response time −14…−23 %, kecelakaan EV −71 % (FHWA HOP-24-019).
- **Kesiapan:** tinggi (system-based EVP lebih murah). **Tahap:** T3 (preempt dasar via NTCIP/central), T4 (bertingkat + CAD).
- **Uji:** SUMO + skenario EV; KPI response time dari CAD, side-street recovery ≤1 siklus.

## K-11 RL sebagai advisor (PPO ring-barrier, veto statistik, shadow mode)
- **Tujuan:** menala parameter (bobot MP, setpoint PC, split TOD) atau merekomendasikan, bukan mengendalikan langsung.
- **Input:** state per lajur (count, queue, occupancy, elapsed green), SPaT; training di digital twin dengan OD beragam.
- **Parameter (A.16/A.15):** PPO clip 0,2, lr 3e-4/1e-3, γ 0,99; aksi = pasangan fase kompatibel dual-ring 8 fase dengan invalid action masking; durasi aksi min 30 s (A.15) atau 5 s (A.12); max green ≤60 s; reward −Σ delay/300 s; veto: SARIMA + credible interval 95 % → tolak aksi anomali.
- **Pseudocode:** `train(sim, ODs∈{A,B,C,…}) → policy; deploy shadow: tiap langkah log(action_rl, action_live); evaluasi ATSPM; jika superior stabil ≥N minggu → advisor: usulkan parameter ke operator/K-06`.
- **Guard-rail:** belum ada RL-TSC yang deployed (A.2); distribution shift (A.1, A.16); LLM di luar control loop (A.17); SIL→HIL→shadow→phased live (A.3).
- **Bukti (simulasi):** RL −11…−32 % vs actuated tuned (A.16, A.10); CityLight +11,7 % throughput vs baseline terbaik; BCT-APLight vs MP ATT −7,8 %; tetapi MP mengalahkan DQN/DDPG di sumolights.
- **Kesiapan:** rendah. **Tahap:** T4 shadow, T5 advisor.
- **Uji:** sumolights-style actor/learner paralel; multi-OD; ATSPM sebagai observer.

## K-12 Oversaturation toolkit (STM2 §12; TSTM §8.3)
- **Tujuan:** throughput/queue management saat DS ≥1; ASCT tidak menyelesaikan jenuh.
- **Teknik & parameter:** split reallocation (dari fase v/c rendah, jaga v/c<1, prioritaskan storage hulu terbesar); batas cycle Lieberman-Chang-Prassas (split 0,5 & link 700 ft → ≤150 s); phase truncation (akhiri hijau saat arus di detektor minimal); re-service (double cycling minor); lead-lag (kiri meluap → lead; through melewati bay → lag); green flush hilir→hulu (preemption berurutan ≤255 s; efektif bila minor ≤20 % volume; operator via CCTV); offset simultan (store-and-forward) / negatif (hijau hilir lebih awal; queue ratio 0,5 & link 800 ft → −30…+10 s); gating/metering di link eksterior dengan storage; periode loading/oversaturated/recovery.
- **Pseudocode (deteksi gejala):** `if occupancy_stopbar ≥ x selama y siklus ∧ ROR5 tinggi → overflow; if downstream link occupancy ≥ z → spillback (de facto red) → aktifkan offset anti-spillback/gating; recovery: flush plan hingga antrian < ambang`.
- **Guard-rail:** minimalkan delay tidak realistis saat jenuh; throughput input vs output; ped tetap dilayani.
- **Bukti:** kualitatif (manual); Makassar: ATCS menurunkan tundaan tapi LOS tetap F pada DS ≈1,1 (R06 E.1).
- **Kesiapan:** tinggi (rule-based + operator). **Tahap:** T4.
- **Uji:** SUMO skenario high demand; KPI throughput, spillback count, queue ratio.

## K-13 Special-condition plans (cuaca, insiden, event, evakuasi)
- **Tujuan:** plan khusus dengan trigger & deaktivasi jelas (STM2 §11; NCDOT plan 51–59).
- **Parameter:** cuaca: +1–2 s red clearance, +min green tanjakan, recall bila deteksi rusak, weather plan (UDOT −30 % FFS; event >20 menit); insiden: alternate route, flush/contingency plan, aktivasi berdasarkan durasi/lajur tertutup/kecepatan rata-rata/konfirmasi; deaktivasi bila bersih/rute alternatif memburuk; event: +larangan parkir, contraflow, debrief.
- **Pseudocode:** `if trigger(speed<thr ∧ confirmed_incident) → activate plan_k (koridor) → monitor → if deactivation criteria → return to TOD/adaptive (transition)`.
- **Guard-rail:** MoU lintas yurisdiksi; validasi plan off-peak; ≥1 teknisi sinyal di tim event.
- **Kesiapan:** tinggi. **Tahap:** T3.
- **Uji:** simulasi insiden di SUMO; drill.

## K-14 Green wave / koordinasi arteri (MAXBAND konsep, Link Pivot, probe-based tuning)
- **Tujuan:** memaksimalkan bandwidth/AoG sepanjang koridor.
- **Input:** jarak antar simpang, kecepatan progresi, cycle bersama (resonant cycle = kelipatan travel time), profil kedatangan (advance detector) atau probe multi-hari.
- **Metode:** offset satu arah t_ij = L_ij/v; dua arah MAXBAND (MILP) [konsep]; alternate/quarter-cycle offset (Portland 60 s/13 mph); **Link Pivot ATSPM**: Link Delta per pasangan simpang → akumulasi → new offset (butuh advance detection & rute terurut); **probe-based** (Mahmud & Day): cyclic TSD (τ=t mod C), PPD, SOFT, heat map dari data 3–6 % penetrasi diagregasi 4 minggu — cycle length harus persis.
- **Guard-rail:** actuated murni merusak green wave → pakai actuated-coordinated/cyclic MP; koridor panjang dipecah dengan programmed stop; bandwidth idealisasi (abaikan dispersi/antrean hilir).
- **Bukti:** PCD offset AoG 53,2 % → 86,6 % (STM2 Exh.8-14/15); US-17 AoG 59 % → 66 % (NCDOT); teori: greenwave serentak dengan offset unik optimal pada arteri fluid (A.11); GLOSA hemat BBM hingga 15–20 % (A.8, sekunder).
- **Kesiapan:** tinggi. **Tahap:** T2 (evaluasi probe & PCD), T3 (Link Pivot & offset update).
- **Uji:** SUMO NEMA `setNemaOffset`; ATSPM PCD/AoG sebelum–sesudah.

---

## Pohon keputusan pemilihan mode per simpang (usulan)
1. **Ada detektor sehat?** Tidak → K-01 TOD (≥8 plan) + K-13; jadwalkan retrofit deteksi. Ya → lanjut.
2. **Simpang terisolasi (jarak ke tetangga >1 km / bukan bagian grup ≥3 simpang)?** Ya → K-02 fully-actuated (+K-09 bila ada bus). Tidak → lanjut (kandidat ATCS per PM 96 Lamp. II.F.e).
3. **Koridor terkoordinasi:** default K-03 actuated-coordinated dengan pattern TOD; tambahkan K-04 TRPS bila variasi besar & persisten; K-14 untuk penalaan offset (probe/PCD).
4. **Simpang kritis** (skor R_n tinggi: occupancy tinggi/variabel, ≥80 % kapasitas): aktifkan K-06 cyclic MP (split adaptif) dalam pattern koridor; pilot 10–25 % node.
5. **Kawasan CBD jenuh (DS ≥1, spillback):** K-06 + perimeter control; K-12 toolkit; ekspektasi realistis (LOS mungkin tetap F).
6. **Ada bus/BRT:** K-09 rule-based dulu → K-08 OCC/Transit-MP bila AVL/APC tersedia.
7. **Rute darurat (Damkar/ambulans):** K-10; hierarki preempt > priority > adaptif.
8. **Semua mode:** K-11 RL hanya shadow/advisor; K-13 plans khusus; guard-rail K-01…K-03 tetap aktif di controller.

## Hierarki fallback (wajib diimplementasikan di semua tahap)
`Adaptif (K-05/K-06) → Central TOD/TRPS (K-01/K-04) → Signal System Master / lokal TOD (≥8 plan, PM49) → Free actuated (K-02) → Flash (conflict/fault, SK 7234) → Manual petugas (UU Ps.104)`. Pemicu turun: detektor gagal > ambang, komunikasi putus (backup timer), adaptive processor gagal, occupancy ekstrem, perintah operator/jadwal/eksternal (MSE Req 2.1.1.0-1..6). Setiap transisi otomatis, ter-log, ter-alarm, dan dilaporkan sebagai KPI.

---

**Pointer ke detail:** R01 §B–F (parameter & rumus manual), R04 A.4–A.7, A.15–A.18 (formulasi MP/TSP/EVP/RL), R04 F (rekomendasi bertingkat & 10 guard-rail), R03 B (implementasi SUMO), R00 G (Dirjen 273), R05 D (PKJI). Lembar rumus: `02_Lembar_Rumus.md`.
