# 02 — Lembar Rumus Implementasi

**Cara pakai file ini**
- Tiap rumus: nama → rumus eksplisit → variabel & satuan → default/tabel → sumber → kapan dipakai. Notasi PKJI 2023 dipakai sebagai utama; padanan MKJI 1997 / Kep. Dirjen 273/1996 di kolom "Padanan".
- Tanda ⚠ = nilai berasal dari grafik di sumber dan harus didigitalisasi (tabel/lookup) sebelum implementasi.
- Semua rumus Indonesia memodelkan simpang terisolir fixed-time; untuk kendali adaptif rumus ini = baseline, validator, dan KPI, bukan pengendali real-time [PKJI 5.3.1; R05 D.4].
- Verifikasi angka ke `docs/sources/_teks_ekstraksi/PKJI_2023_*.txt` (Bab 5, hlm. 102–128) bila ragu.

## A. PKJI 2023 — Simpang APILL (padanan MKJI 1997 / Dirjen 273)

| # | Nama | Rumus | Variabel / satuan | Default / tabel | Sumber | Padanan |
|---|---|---|---|---|---|---|
| A1 | Arus jam perencanaan | qJP = LHRT × K | LHRT kend/hari; K perkotaan 7–12% | K ≈ 9% jalan kota [PM 96 Lamp.I] | [PKJI 5-13] | VJP = K×LHR [Dirjen 273 Tabel 2-1] |
| A2 | Konversi SMP | q = Σ (kend/jam × EMP) | EMP: MP 1,00; KS 1,30; SM 0,15 (P) / 0,40 (O); KTB dikeluarkan/lihat RKTB | — | [PKJI Tabel 5-2] | MKJI/Dirjen: MC 0,2/0,4; UM 0,5/1,0 |
| A3 | Rasio belok | RBKi = qBKi/qTotal; RBKa = qBKa/qTotal; RKTB = qKTB/qKB | — | default belok 15% bila tak ada data [Dirjen 273 Bab II.B] | [PKJI 5-24…5-26] | PLT, PRT |
| A4 | Lebar efektif | Jika LBKiJT ≥ 2 m (atau lajur eksklusif): LE = min{L − LBKiJT; LM}, qBKiJT dikeluarkan; cek tipe P: bila LK < LM×(1−RBKa) → LE = LK (hanya arus lurus). Jika LBKiJT < 2 m: LE = min{L; LM + LBKiJT; L×(1+RBKiJT) − LBKiJT}; cek LK < LM×(1−RBKa−RBKiJT) → LE = LK | L lebar pendekat hulu, LM lebar masuk, LK lebar keluar, LBKiJT lebar lajur belok kiri jalan terus (m) | — | [PKJI 5-2, 5-3] | We; W_A, W_ENTRY, W_EXIT, W_LTOR [Dirjen 273 Bab V.B] |
| A5 | Arus jenuh dasar tipe P | J0 = 600 × LE | SMP/jam hijau; LE m | — | [PKJI 5-6] | S0 = 600·We |
| A6 | Arus jenuh dasar tipe O | ⚠ J0 = f(LE, qBKa, qBKa,O) dari Gambar 12-2…12-9; koreksi bila arus >250: tanpa lajur BKa terpisah — jika qBKa,O >250 & qBKa <250: J = J(250) − (qBKa,O − 250)×8; jika keduanya >250: J = J(250,250) − (qBKa,O + qBKa − 500)×2 | SMP/jam | belok kanan >250 SMP/jam → pertimbangkan fase terlindung | [PKJI 5.3.3; Lamp.12] | Gambar 5-4/5-5 [Dirjen 273] |
| A7 | Arus jenuh terkoreksi | J = J0 × FHS × FUK × FG × FP × FBKi × FBKa | — | lihat A8–A13 | [PKJI 5-4] | S = S0·FCS·FSF·FG·FP·FRT·FLT |
| A8 | Faktor ukuran kota FUK | tabel: >3,0 jt jiwa 1,05; 1,0–3,0 1,00; 0,5–1,0 0,94; 0,1–0,5 0,83; <0,1 0,82 | — | Jakarta = 1,05 | [PKJI Tabel 12-1] | FCS (Dirjen: 0,25–0,5 jt 0,83… sedikit beda batas) |
| A9 | Faktor hambatan samping FHS | tabel f(lingkungan KOM/KIM/AT, hambatan tinggi/sedang/rendah, fase terlawan/terlindung, RKTB 0,00–0,25); contoh KOM-tinggi-terlindung: 0,93/0,91/0,88/0,87/0,85/0,81; KOM-tinggi-terlawan: 0,93/0,88/0,84/0,79/0,74/0,70; AT-terlindung 1,00/0,98/0,95/0,93/0,90/0,88 | — | tak diketahui → anggap **tinggi** | [PKJI Tabel 12-3] | FSF |
| A10 | Faktor kelandaian FG | ⚠ Gambar 12-10 f(kelandaian %, + naik / − turun) | — | datar = 1,0 | [PKJI 5.3.3] | FG Gambar 5-6 |
| A11 | Faktor parkir FP | FP = [Lp/3 − (L − 2)×(Lp/3 − wH)/L] / wH | Lp jarak garis henti–kendaraan parkir pertama (m); L lebar pendekat (m); wH waktu hijau (s) | wH normal 27 s (MKJI 26 s); tidak dipakai bila LE = LK | [PKJI 5-5] | Fp [Dirjen 273 Bab V.D] |
| A12 | Faktor belok kanan FBKa | FBKa = 1,0 + RBKa × 0,26 | hanya tipe P, tanpa median, dua arah, LE oleh LM | — | [PKJI 5-27] | FRT |
| A13 | Faktor belok kiri FBKi | FBKi = 1,0 − RBKi × 0,16 | hanya tipe P tanpa BKiJT, LE oleh LM | — | [PKJI 5-28] | FLT |
| A14 | Arus jenuh gabungan 2 fase | J1+2 = (J1×wH1 + J2×wH2)/(wH1 + wH2) | — | hijau awal/akhir 1/4–1/3 total, **≥10 s** | [PKJI 5-7] | — |
| A15 | Rasio arus | Rq/J = q / J | — | — | [PKJI 5-8] | FR = Q/S |
| A16 | Rasio arus simpang | RAS = Σ_i (Rq/J)kritis,i (nilai tertinggi tiap fase) | — | RAS ≥1 → jenuh, rumus siklus tak realistik | [PKJI 5-29] | IFR = ΣFRcrit |
| A17 | Rasio fase | RF_i = (Rq/J)kritis,i / RAS | — | — | [PKJI 5-30] | PR |
| A18 | Waktu merah semua (all-red) | wMS = max{ (LKBR + PKBR)/vKBR − LKDT/vKDT ; LPK/vPK } | L jarak garis henti→titik konflik kendaraan berangkat (KBR)/datang (KDT) (m); P panjang kendaraan; v m/s | vKBR = vKDT = 10 m/s bermotor; 3 m/s KTB; 1,2 m/s pejalan kaki; PKBR 5 m (MP/KS), 2 m (SM/KTB); all-red ≥ CT | [PKJI 5-9] | CT_i [Dirjen 273 Bab IV.B] |
| A19 | Waktu antar hijau normal | wAH = wK + wMS | tabel: simpang kecil (lebar 6–<10 m) 4 s; sedang (10–<15) 5 s; besar (≥15) 6 s per fase | kuning wK = **3,0 s** (Indonesia) | [PKJI Tabel 5-1; hlm.112] | IG 5/6/7 s [Dirjen 273 Tabel 4-1] |
| A20 | Waktu hijau hilang | wHH = Σ_i (wMS + wK)_i | s/siklus | — | [PKJI 5-10] | LT = ΣIG |
| A21 | Waktu siklus Webster | s = (1,5 × wHH + 5) / (1 − RAS) | s | layak: 2 fase 40–80; 3 fase 50–100; 4 fase 80–130 s; **>130 s dihindari** | [PKJI 5-11; Tabel 12-2] | c = (1,5LT+5)/(1−IFR) |
| A22 | Waktu hijau per fase | wH_i = (s − wHH) × RF_i | s | hindari hijau <10 s; kinerja lebih peka salah bagi hijau daripada siklus panjang | [PKJI 5-12] | g_i = (c−LT)·PR_i |
| A23 | Kapasitas | C = J × wH / s | SMP/jam | — | [PKJI 5-1] | C = S·g/c |
| A24 | Derajat kejenuhan | DJ = q / C | — | desain **≤0,85**; ≥1 jenuh | [PKJI 5-14] | DS |
| A25 | Antrian sisa | Nq1 = 0 bila DJ ≤ 0,5; bila DJ > 0,5: Nq1 = 0,25 × C × [ (DJ−1) + √((DJ−1)² + 8×(DJ−0,5)/C) ] | SMP; C kapasitas SMP/jam (teks PKJI tercetak "s", dimensi menunjukkan C) | — | [PKJI 5-15, 5-16] | NQ1 ⚠ Gambar 7-1 [Dirjen 273] |
| A26 | Antrian datang saat merah | Nq2 = s × [(1 − RH)/(1 − RH×DJ)] × q/3600 | RH = wH/s; q SMP/jam | — | [PKJI 5-17] | NQ2 = Q·(c−g) (Q skr/detik) |
| A27 | Antrian total & maksimum | Nq = Nq1 + Nq2; ⚠ NqMAX = f(Nq, POL) Gambar 5-9 | — | POL ≤5% desain; 5–10% operasi | [PKJI 5.3.4] | NQmax Gambar 7-2 |
| A28 | Panjang antrian | PA = NqMAX × 20 / LM | m; 20 m² per SMP; LM lebar masuk (m) | — | [PKJI 5-18] | QL = NQmax·20/W_ENTRY |
| A29 | Rasio & jumlah kendaraan terhenti | RKH = 0,9 × Nq × 3600 / (q × s); NKH = q × RKH; RKH_Total = ΣNKH / qTotal | — | MKJI: PSV = min(NS,1) (cap tidak dinyatakan PKJI) | [PKJI 5-19, 5-20, 5-31] | NS, PSV = 1 + NQ/c − g/c [Dirjen 273 Bab VII.C] |
| A30 | Tundaan lalu lintas (Akcelik) | TLL = s × 0,5 × (1 − RH)² / (1 − RH × DJ) + Nq1 × 3600 / C | det/SMP | — | [PKJI 5-22] | DT; Dirjen: D_j = (A_j·c + B_j/Q_j)·0,90, A_j = (1−GR)²/[2(1−GR·DS)], B_j = DS²/[2(1−DS)] |
| A31 | Tundaan geometrik | TG = (1 − RKH) × PB × 6 + RKH × 4 | PB porsi kendaraan membelok; 6 s belok tanpa henti, 4 s berhenti | asumsi 40 km/jam, belok 10 km/jam, 1,5 m/s² | [PKJI 5-23] | DG |
| A32 | Tundaan rata-rata pendekat & simpang | T_i = TLL_i + TG_i; TI = Σ(q_i × T_i) / qTotal | det/SMP | → kelas LOS PM 96 (bagian F) | [PKJI 5-21, 5-32] | D, D_I |
| A33 | Efisiensi alternatif fase | pilih skema dengan (RAS + wHH/s) terendah | — | — | [PKJI 5.3.4; Dirjen 273 Bab V.F] | — |
| A34 | Perbaikan bila DJ > 0,85 | pelebaran pendekat (pada RF kritis) → fase belok kanan terpisah (tipe O, RBKa tinggi, RF >0,8) → larangan belok kanan → ulangi | — | — | [PKJI Langkah E; Dirjen 273 Bab VI] | — |

## B. Manual FHWA / NCHRP (satuan AS kecuali disebut)

| # | Nama | Rumus | Variabel | Default | Sumber | Kapan |
|---|---|---|---|---|---|---|
| B1 | Kuning ITE | Y = t + 1,47·v / (2(a + 32,2·g)) [US]; Y = t + v/(2(a + 9,81·g)) [SI] | t 1,0 s; v mph (m/s); a 10 ft/s² (3,0 m/s²); g gradien desimal | tabel: 25 mph 3,0; 30 3,2; 35 3,6; 40 3,9; 45 4,3; 50 4,7; 55 5,0; 60 5,4 s; ±0,1 s per 1% gradien; MUTCD 3–6 s | [NCHRP 812 §6.1.1; FHWA 2008 Eq.5-2] | validator input kuning |
| B2 | Red clearance | R = (W + Lv) / (1,47·v) (−1 s NCHRP 731) | W lebar simpang ft; Lv 20 ft | ≤6 s MUTCD; praktik 0,5–2 s | [NCHRP 812 §6.1.2] | validator all-red (bandingkan A18) |
| B3 | Min green queue clearance | Gq = 3 + 2·n; n = d / Lv | d jarak detektor setback; Lv 25 ft | driver expectancy: arteri >40 mph 10–15 s; minor 4–10; kiri 2–10 s | [NCHRP 812 §6.1.3] | min green |
| B4 | Variable initial | initial = min(addedInitial × aktuasi, maxInitial), ≥ min green | 2,0 s/aktuasi (1 lajur), 1,5 (2), 1,2 (≥3) | — | [NCHRP 812 Exhibit 6-5; NTCIP phase] | volume-density |
| B5 | Max green estimasi | Gmax = (V·C)/(1200·n) + 1 (min 15 s) atau 1,25–1,5 × green minimum-delay pretimed | V vph, C s, n lajur | 15–70 s per tipe fase | [FHWA 2008 Tabel 5-6; NCHRP 812 Exhibit 6-9] | max green |
| B6 | Passage time | PT = MAH − (Lv + Ld)/(1,47·va) | MAH 3,0 s (4,0 dengan gap reduction); Lv panjang kendaraan; Ld panjang detektor; va = 0,88·v85 | zona 6 ft 2,3–2,7 s … 80 ft 0,3–1,8 s; setback 2–3 s | [FHWA 2008 Eq.5-5; NCHRP 812 Exhibit 6-12] | gap timer |
| B7 | Gap reduction | allowable gap turun linier dari passage ke min gap selama time-to-reduce setelah time-before-reduction | TBR ≥10 s (≈min green); TTR ≈ ½(max−min); min gap MAH 2,0 s | — | [FHWA 2008 §5.5.1] | volume-density |
| B8 | Pedestrian clearance | PCT = Dc / vp; FDW = PCT − (Y + R) atau = PCT (konservatif) | Dc jarak seberang ft; vp 3,5 ft/s (1,07 m/s) | walk ≥7 s (4 s rendah; 10–15 CBD); LPI ≥3 s; steady DW ≥3 s | [NCHRP 812 §6.1.6] | validator ped |
| B9 | Effective green & capacity | g = G + Y + R − (l1 + l2); c = s·g/C; X = v/c = v·C/(s·g) | s = 3600/h (h ≈ 2,2 s → 1636 vphpl; ideal 1900); lost time 4–5 s/fase | X <0,85 stabil; 0,85–1 tak stabil; >1 jenuh | [FHWA 2008 Eq.3-1…3-3] | v/c per movement |
| B10 | Webster (AS) | C = (1,5·L + 5)/(1 − Y); Y = Σ(v_crit/s) | — | umumnya ≤120 s; 120→180 s hanya +2% kapasitas | [FHWA 2008 Eq.6-1] | = A21 |
| B11 | HCM QEM cycle | C = L / (1 − min(CS, RS)/RS); RS = 1710·PHF·fa; Xcm = CS/(RS·(1 − L/C)) | CS critical sum vph; fa 0,90 CBD | min 60 s, maks yurisdiksi (150 s) | [FHWA 2008 Eq.6-2; Contoh 3-1] | cycle awal |
| B12 | Antrian praktis | Q_avg = v·C/3600 (atau v·(C−g)/3600); Q95 ≈ 2·Q_avg; panjang 25 ft/kend; green ≈ 2 + 2·Q | — | — | [FHWA 2008 §3.4.3] | cek turn bay |
| B13 | Bandwidth efficiency & attainability | E = (B_A + B_B)/(2C); attainability = bandwidth / g_crit | — | E: <0,12 buruk; 0,13–0,24 cukup; 0,25–0,36 baik; ≥0,37 sangat baik | [FHWA 2008 Eq.3-7/3-8] | KPI koridor |
| B14 | Performance Index Synchro | PI = D·1 + St·10 + QP·100 (per 3600) | D delay, St stops, QP queue penalty | — | [FHWA 2008 Eq.6-3] | optimasi plan |
| B15 | Offset satu arah | t_offset = L_ij / v_progression | jarak antar simpang, kecepatan progresi | referensi: awal kuning fase koordinasi | [arXiv 2507.22511; NCHRP 812 §7.3] | green wave |
| B16 | Resonant/alternate cycle | kecepatan progresi = jarak blok / (½, ¼, ⅙ siklus) untuk single/double/triple alternate | — | contoh quarter-cycle grid 60 s / 13 mph | [NCHRP 812 Exhibit 7-18] | grid |
| B17 | Batas siklus jenuh (Lieberman) | ⚠ batas atas siklus f(split ratio, panjang link); contoh split 0,5 & link 700 ft → maks 150 s | — | hijau >30 s menurunkan saturation flow | [NCHRP 812 §12.3.1.2] | oversaturation |
| B18 | Cuaca | saturation flow: hujan −4,7%; hujan seharian −8,5–12,3%; kabut −11,4%; kecepatan arteri −6–20% | — | tambah red clearance 1–2 s; min green tanjakan; weather plan −30% FFS | [NCHRP 812 Exhibit 11-4/11-5] | weather plan |

## C. Traffic Responsive (TRPS)

| # | Nama | Rumus | Catatan | Sumber |
|---|---|---|---|---|
| C1 | Volume ekuivalen | VE_i = V_i + K·O_i | K skala okupansi→volume; K=17 → 100% okupansi ≈ 1700 vplph (sisi keluar); K 5–7 dekat stop bar | [NCHRP 812 §9.3] |
| C2 | Target-based (UTCS) | err_j = Σ_i w_i·\|(V_i + K·O_i) − T_ij\|; pilih pattern err terendah bila lebih rendah X% dari pattern berjalan [rekonstruksi] | signature target per pattern | [NCHRP 812 Eq.9-1] |
| C3 | Threshold-based | CC = Σ_i w_i·(V_i + K·O_i) vs ambang masuk/keluar (hysteresis; contoh offset 2→3 masuk 52, keluar 49) | cycle ∝ VE arteri; split ∝ rasio arteri/minor; offset ∝ rasio inbound/outbound; smoothing 50%; min dwell 30 menit | [NCHRP 812 Eq.9-2, Exhibit 9-2, 9-6] |

## D. Max-pressure & kendali adaptif

| # | Nama | Rumus | Variabel / constraint | Sumber |
|---|---|---|---|---|
| D1 | Max-pressure asli | w_(l,m) = η_(l,m) − Σ_{n∈D(m)} r_(m,n)·η_(m,n); P_φ = Σ_{(l,m)∈φ} c_(l,m)·w_(l,m); φ* = argmax P_φ | η antrian (kendaraan) atau delay (D-MP); r turning ratio; c saturation flow; time step 5–10 s; min green g_min | [arXiv 2202.03290 §2; 1909.00395 Alg.2] |
| D2 | Cyclic MP (deployable) | p_z = (x_z/c_z − Σ_w β_{z,w}·x_w/c_w)·S_z; P_j = max{0, Σ_{z∈v_j} p_z}; g̃_j = (P_j/ΣP_i)·G_n; proyeksi QP: min Σ_j (g̃_j − G_j)² s.t. Σ_j G_j + L_n = C_n; G_j ≥ g_min; \|G_j − G_j^prev\| ≤ Δg^R; integer | x antrian, c kapasitas link, β turn ratio, S sat flow; **g_min 7 s; Δg^R 5 s/siklus**; cycle & offset tetap | [arXiv 2210.10453 §3.1.1] |
| D3 | Node selection MP parsial | R_n = α·m¹_n + β·m²_n + γ·N^c_n (mean occupancy, varians occupancy, fraksi waktu ≥80% kapasitas); grid-search α,β,γ | 10–25% node kritis ≥ manfaat 100% | [arXiv 2210.10453 §5] |
| D4 | Perimeter control PI | u(k) = u(k−1) − K_P[n(k) − n(k−1)] − K_I[n(k) − n̂] | n akumulasi region (MFD), n̂ setpoint; hysteresis start/stop; min 15% sat flow gerbang | [arXiv 2210.10453 §3.2] |
| D5 | OCC-MP weight | w(l,m) = o(l,m)·[x(l,m) − Σ_{n∈D(m)} x(m,n)·r(m,n)]⁺; P_φ = Σ w·C·S | o = occupancy penumpang rata-rata hulu (bus dari APC; mobil 1,5); update 10 s | [arXiv 2406.19269 §3] |
| D6 | Transit-MP state | hulu: Σ_v δ_v·p_v·τ_v; hilir: Σ_v δ_v·τ_v; τ_v = LTT_v/ETT; δ_v = 0 bila transit belum lewat halte terdekat; fallback historis E[Q(t)] = max{0, E[Q(t−T0)] + λ̂T0 − s·μ^dep·T0}, delay ≈ E[Q]²/(2λ̂) | T0 10 s; segmen link ≈420 m | [arXiv 2511.00309 §3–4] |
| D7 | EVP bersyarat (mixed-criticality) | preempt bila Δ = t^cur − t^target > 0; t^target = d/v_limit·a_level; t^cur = d/v_now | level faktor 1 / 1,5 / 2; target 8/12/20 menit; conflict graph multi-EV | [arXiv 2109.03210 §3] |
| D8 | Webster adaptif (sumolights) | interval W kumpulkan arus per fase; Y = Σ max(F_l/s); C = (1,5R+5)/(1−Y) dibatasi [c_min, c_max]; G = C − R ∝ y | — | [arXiv 1909.00395 Alg.1] |
| D9 | Reward RL tipikal | r = −Σ_v d_v/d_max (d_max 300 s) atau −\|queue\|²; aksi ring-barrier 8 fase dengan masking; min green 10 s; max green 60 s; keputusan 5–15 s | hanya untuk simulasi/advisor | [arXiv 2603.15283; 2007.03433] |
| D10 | Delay probe | d_i = t_i − t_f (t_f = jarak/speed limit); travel rate r = t/D; TTI = t/t_f; SOFT dari Fourier profil kecepatan | penetrasi 3–6% → agregasi multi-hari; cycle harus tepat | [arXiv 2212.02315 §3] |

## E. ATSPM (dari hi-res log 0,1 s)

| # | Metrik | Cara hitung | Detektor | Sumber |
|---|---|---|---|---|
| E1 | Phase termination | per fase per siklus: gap-out / max-out / force-off / skip / ped | tidak perlu | [NCDOT A.1] |
| E2 | Split monitor | durasi aktual (begin green → end red clear) vs programmed split | tidak perlu | [NCDOT A.2] |
| E3 | Ped delay | t(walk mulai) − t(ped call) | tombol | [NCDOT A.3] |
| E4 | Preemption details | request → service (time to service), dwell, end | tidak perlu | [NCDOT A.4] |
| E5 | AoG (arrivals on green) | AoG% = kedatangan (advance) saat hijau / total kedatangan | advance 350–400 ft | [NCDOT A.5] |
| E6 | Platoon ratio | AoG dinormalisasi terhadap proporsi hijau dalam siklus (naratif; rumus eksplisit tidak ada di sumber; TSPH Tabel 49: ≤0,5 very poor … >2,0 exceptional) | advance | [NCDOT A.5; TSPH Tabel 49] |
| E7 | Split failure | GOR = waktu hijau terokupasi / hijau; ROR5 = okupansi 5 s pertama merah; **failure bila GOR ≥80% dan ROR5 ≥80%** | stop-bar presence | [NCDOT A.8; HOP-20-002 hlm.24] |
| E8 | Approach delay | Σ [t(hijau) − t(aktuasi advance dikonversi ke stop bar)] per kendaraan; rata-rata per fase (abaikan start-up lost time) | advance | [NCDOT A.10] |
| E9 | Arrivals on red | kedatangan saat merah / total | advance | [NCDOT A.11] |
| E10 | TMC / approach volume | count per lajur per 15 menit; PHF, K, D | lane-by-lane count | [NCDOT A.7, A.9] |
| E11 | YRA | kendaraan masuk saat kuning / red clearance / fase konflik aktif | past-stop-bar / speed filter | [NCDOT A.13] |
| E12 | Watchdog | no data <500 rekaman/24 jam; force-off >90% (≥50 aktivasi 01–05); max-out >90% (≥50, 01–05); advance <100 kend 17–18; stuck ped >200 (01–05) | — | [HOP-20-002 hlm.20] |
| E13 | Link Pivot | ⚠ Link delta = perubahan offset yang memaksimalkan AoG prediksi; offset baru = existing + akumulasi delta (algoritme rinci tidak ada di sumber) | advance berurutan | [NCDOT A.6] |
| E14 | Storage | ≈9 GB/hari untuk 387 sinyal (≈23 MB/simpang/hari) | — | [HOP-20-002 hlm.54] |

## F. Tingkat pelayanan & ambang kebijakan

| Klasifikasi | Nilai | Sumber |
|---|---|---|
| LOS simpang (tundaan det/kend) | A <5; B 5–15; C 15–25; D 25–40; E 40–60; F >60 | [PM 96/2015 Lamp.I Bab II.D] |
| LOS simpang HCM (control delay s/veh) | A ≤10; B 10–20; C 20–35; D 35–55; E 55–80; F >80 | [FHWA 2008 §3.4.1] |
| LOS ruas (kecepatan km/jam) | A ≥80; B ≥70; C ≥60; D ≥50; E ≥30 (perkotaan ≥10, volume mendekati kapasitas); F <30 | [PM 96 Lamp.I] |
| Target LOS minimal | arteri primer B; kolektor primer B; lokal primer C; tol B; arteri sekunder C; kolektor sekunder C; lokal sekunder D; lingkungan D | [PM 96 Lamp.I] |
| Warrant APILL | >750 kend/jam selama 8 jam; delay >30 s; >175 pejalan kaki/jam ×8 jam; >5 laka/tahun | [PM 96 Lamp.II.F.b] |
| ATCS | ≥3 simpang; jarak ≤1 km | [PM 96 Lamp.II.F.e] |
| Kotak kuning | simpang adaptif/ATCS & LOS ≥C | [PM 96 Lamp.II.F.h] |
| Pembatasan perseorangan / motor / ERP | V/C ≥0,7 & <30 km/jam; V/C ≥0,5; V/C ≥0,9 & ≤10 km/jam, 2×2 lajur, bukan jalan nasional | [PP 32/2011 Ps.65, 70, 79] |
| Tidal flow / SSA / parkir / u-turn | V/C >0,9 (70:30); V/C >0,85; V/C >0,7 & <30 km/jam; V/C <0,65 | [PM 96 Lamp.II.G] |
| KPI strategis | 60% angkutan umum & 35 km/jam (Perda 5/2014 Ps.8); ≥30 km/jam & 60% (Perpres 55/2018, 2029) | [Perda; Perpres] |
| Guard-rail kendali (dari riset) | min green ≥7–10 s; max green ≤60 s; Δsplit ≤5 s/siklus; kuning 3 s; ≥30 menit per pattern; transisi ≤3–5 siklus; TSP ext ≤10 s, 1×/siklus; EVP ~25 s | [R04 F; R01 C.6; R06 F.2] |

## G. Evaluasi manfaat

| # | Rumus | Sumber |
|---|---|---|
| G1 | Manfaat delay tahunan = Σ volume puncak × Δdelay (s/veh)/3600 × $15,91/jam × 250 hari; manfaat stops = Σ volume × Δstops × $0,014 × 250 (contoh $266.293 + $14.544) | [NCDOT Cost Benefit Analysis hlm.4–5] |
| G2 | Desain evaluasi: before–after (rentan musim) vs on–off bergantian (lebih adil); ≥6 run floating car/arah; hindari Senin/Jumat/cuaca buruk | [T414 hlm.58; NCDOT Travel Time Runs] |
| G3 | Manfaat ASCT rata-rata: stops −7,8% … split failure −85%; side-street delay +3,4%; crashes −35%; lebih besar pada AADT 35–55 ribu | [T414 hlm.10, 66] |

## H. Rel (bila ada perlintasan ≤200 ft)
- MWT = MT (≥20 s) + CT (1 s per 10 ft jarak bersih >35 ft); RTT + waktu bersihkan antrian < MWT; TCGI wajib; risiko preempt trap [NCHRP 812 §10.5, Eq.10-1].

**Pointer ke detail**
- PKJI prosedur A–F & formulir: R05 D.4; perbedaan MKJI: R05 D.5; Dirjen 273 lengkap: R00 G.
- Rumus FHWA/NCHRP: R01 B.4–B.5, C.3, D.3; NTCIP parameter: R03 A.3.
- Max-pressure/PC/RL: R04 A.4–A.7, A.16, F; ATSPM: R03 C.3–C.4; TSP/EVP parameter: R06 F.2.
