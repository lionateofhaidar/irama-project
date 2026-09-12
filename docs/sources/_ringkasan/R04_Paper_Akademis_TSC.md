# R04 — Catatan Studi Paper Akademis: Traffic Signal Control (TSC), Prioritas Transit/Darurat, Green Wave, dan Digital Twin

**Konteks proyek:** perancangan aplikasi Intelligent/Integrated Traffic Control System (ITCS) ala Dishub DKI Jakarta — APILL adaptif real-time berbasis AI/kamera untuk ±321 simpang, dengan fitur actuated, self-adaptive, coordinated green wave, bus priority (TransJakarta), emergency preemption, predictive modelling, dan digital twin 3D. Tujuan catatan ini: memilih **algoritma kendali yang realistis untuk dideploy** (bukan sekadar riset) beserta **fallback aman**.

**Sumber:** 19 paper arXiv (folder `docs/sources/_teks_ekstraksi/`) + 1 review PMC (`03_Jurnal_Akademis/Teks_PMC11435829_...md`). Semua angka di bawah diambil langsung dari teks paper; jika suatu paper tidak memuat angka kuantitatif, dinyatakan eksplisit.

**Konvensi:** istilah teknis Inggris dipertahankan (max-pressure, reward, spillback, dsb.). Skor relevansi ITCS Jakarta: 1 (rendah) – 5 (sangat tinggi).

---

## A. Catatan per Paper

### A.1 Wang, Abdulhai & Sanner (2022) — *A Critical Review of Traffic Signal Control and a Novel Unified View of RL and MPC Approaches for ATSC*
- **Sitasi:** Xiaoyu Wang, Baher Abdulhai, Scott Sanner (Univ. of Toronto). arXiv:2211.14426 (book chapter, 2022).
- **Masalah:** literatur ATSC (Adaptive TSC) berkembang pesat, khususnya RL dan MPC, tetapi tanpa analisis lintas-domain; metode baru "claim better performance than older approaches, but lack cross-evaluation and in-field tests". Perbedaan bahasa antara komunitas MPC dan RL menyulitkan perbandingan.
- **Metode (kerangka konseptual, bukan eksperimen):**
  - Taksonomi historis: fixed-time (Webster 1958; MAXBAND/MULTIBAND/PASSER progression-based; TRANSYT/SYNCHRO delay-based) → actuated (gap-out/max-out; "relatively myopic") → ATSC 1G (TR2, UTCS-1: pemilihan plan per TOD) → 2G (SCATS, SCOOT: optimasi online cycle/split/offset, hierarkis) → 3G rolling-horizon DP (OPAC, PRODYN, UTOPIA, RHODES) → 4G/MPC (SURTRAC: scheduling MILP, deployed di Pittsburgh) → MF-RL (MARLIN: Q-learning tabular, "one of the few RL-based ATSC methods ever tested in the field") → DRL (DQN+CNN, CTDE, GAT).
  - Dua jenis aksi: **second-based** (extend/change; FPS vs VPS) dan **cycle-based** (order, split, cycle). Paper menegaskan cycle-based "less flexible ... but more popular in the industry since drivers know exactly the length of each phase" dan "more pedestrian-friendly".
  - Tiga paradigma arsitektur: centralized, decentralized, hierarchical (SCATS/SCOOT = hierarkis).
  - Rule-based heuristic: **max-pressure** (Varaiya 2013) — decentralized, throughput-maximizing, stabil dalam *stability region*, tetapi "not optimized based on a given traffic model".
  - **Unified view**: memodelkan TSC sebagai Mixed-Observability MDP (MOMDP) dengan state $s=[s_c, s_o]$ (inner system terkontrol + outer system/demand yang hanya diamati). Bellman: $V^\pi(s)=\mathbb E[r]+\gamma\sum_{s'}P(s'|s,a)V^\pi(s')$; Q-learning: $Q\leftarrow Q+\alpha(r+\gamma\max_{a'}Q(s',a')-Q)$. RHO/MPC: $\max_{a_{t:t+H}}\sum r$ s.t. $s_{t+1}\sim P(\cdot|s_t,a_t,e_t)$ dengan $e_t$ prediksi exogenous event; hanya aksi pertama dieksekusi.
  - Kritik pada MF-RL: state hanya lokal → transisi non-Markov/non-stasioner → "convergence, generalization, and distribution shifting issues at the same time". Solusi ideal: belief-state policy $s=[s_c, s_d, b_d]$ (belief atas demand via HMM/Kalman/RNN).
  - Dec-POMDP NEXP-complete → dekomposisi ke MOMDP independen; CTDE (VDN/QMIX/COMA) berguna tapi "assumptions CTDE relies on could not be always fulfilled in-field" karena policy dibekukan saat deploy.
- **Data/simulator:** tidak ada eksperimen; review.
- **Hasil kuantitatif:** tidak ada; klaim kualitatif: MPC "none of them has been tested in the field"; RHO dengan model bagus > MF-RL tanpa model > RHO dengan model buruk.
- **Arah riset:** (1) modelkan exogenous disturbance dengan belief state; (2) atasi distribution shift dengan model-based online planning (MB-RL/MCTS, merujuk Jaggi et al. 2021 yang menunjukkan MF-RL gagal generalisasi saat pola demand berubah); (3) hierarchical control untuk jaringan besar.
- **Keterbatasan:** tidak ada validasi numerik; fokus Toronto.
- **Relevansi ITCS Jakarta: 5.** Ini peta jalan konseptual paling penting: menegaskan bahwa **2G ATSC (SCATS/SCOOT-like, hierarkis, cycle-based) tetap standar industri yang deployed**, MP adalah heuristik stabil yang cepat, dan RL belum siap deploy tanpa mekanisme belief/online-planning. Untuk Jakarta, mendukung desain hierarkis (regional master → local controller) dengan aksi cycle-based yang dapat diprediksi pengemudi/pejalan kaki.

### A.2 Chen, Fang & Sadeh (2022) — *The Real Deal: A Review of Challenges and Opportunities in Moving RL-Based TSC Towards Reality*
- **Sitasi:** Rex Chen, Fei Fang, Norman Sadeh (CMU). arXiv:2206.11996v3; ATT'22 Workshop (CEUR-WS), 2022.
- **Masalah:** "RL-based signal controllers have never been deployed" meski banyak paper menyebut deployment sebagai future work; fokus pada engineering challenges dari perspektif *data-to-deployment pipeline*.
- **Metode:** review terstruktur (Google Scholar + snowballing). Formulasi MDP standar: $Q(s,a)=\sum_{s'}P(s'|s,a)[R+\gamma\max_{a'}Q(s',a')]$; ekstensi POMDP, Markov game, Dec-POMDP. Statistik dari review [10] atas 160 paper: state paling umum **queue length (38%)**, current phase (11%); aksi memilih next phase/durasi (62%) vs cycle-based (32%); reward queue length (30%), delay (13%), waiting time (9%), throughput (4%). **67% paper tidak menyebut sumber data spesifik.**
- **Empat tantangan & pelajaran lapangan:**
  1. *Uncertainty in detection*: loop murah/akurat tapi rentan aus; video/radar degradasi saat cuaca buruk/malam. SURTRAC menangani error estimasi antrean secara eksplisit; overestimasi antrean moderat justru membantu. State sederhana (count+phase) bisa mengalahkan representasi citra kompleks.
  2. *Reliability of communications*: 90% sistem TSC AS adalah closed-loop 3-tingkat (TMC → field master → local controller); RL harus masuk ke ekosistem NTCIP 1202; masalah nyata adalah *signal strength/latency*, bukan bandwidth.
  3. *Compliance & interpretability*: min green, yellow/red clearance, aturan pejalan kaki (LePI) harus dipaksakan lewat action space; belum ada RL yang memakai Accident Modification Factors; interpretabilitas via surrogate decision tree, SHAP, rule post-processing.
  4. *Heterogeneous road users*: dari 160 paper hanya 3 mempertimbangkan kendaraan non-pribadi dan 1 pejalan kaki. SCATS mengimplementasikan priority & preemption secara native dan terbukti robust; controller butuh beberapa cycle untuk recover dari preemption.
- **Hasil kuantitatif:** hanya statistik literatur (di atas).
- **Keterbatasan:** tidak ada eksperimen; berbasis AS.
- **Relevansi: 5.** Daftar periksa deployment: desain state sesuai detektor yang benar-benar ada (kamera Jakarta: hitung antrean/occupancy, bukan citra mentah), constraint keselamatan di action space, kompatibilitas protokol, dan perlakuan eksplisit untuk bus/EV/pejalan kaki.

### A.3 Bagabaldo & Hackl (2025) — *Digital Twins for Intelligent Intersections: A Literature Review*
- **Sitasi:** Alben Rome Bagabaldo, Jürgen Hackl (Princeton). arXiv:2510.05374, Okt 2025.
- **Masalah:** sintesis literatur DT untuk simpang cerdas; 544 kandidat → **85 paper** (2019–Mei 2025), lima tema: arsitektur (18), data & simulasi (19), AI/ML kontrol (23), VRU safety (15), scaling citywide (35). Screening dibantu LLM (Gemini) lalu review manual.
- **Temuan arsitektur:** arsitektur **5 lapis**: (i) data acquisition (video, LiDAR, radar, loop, cuaca); (ii) communication (DSRC/WAVE, C-V2X, 5G NR, MQTT, edge microservices); (iii) processing (SUMO via TraCI, HIL, GMM/EM, GNN/STGAT, GAN/VAE, RL agents); (iv) modeling (physics solver, foundation model, IFC/mesh); (v) visualization (web dashboard, BIM, mixed reality). Contoh: Redis + Kalman untuk forecasting ringan tanpa engine simulasi; co-simulation SUMO–CARLA; SUMO+Veins+OMNeT++ untuk validasi SPaT/MAP.
- **Data & simulasi:** fusi heterogen (JDL model), imputasi data hilang (k-means + temporal-neighbor interpolation), downscaling mesoscopic mempercepat komputasi "up to 500%", Mixture Density Networks menutup sim-to-real gap ">30%" (Bamminger et al.).
- **AI/ML:** RL/MARL untuk sinyal, "democratizing traffic control" (agen multi-objektif voting), cooperative adaptable lanes memangkas waiting time "almost 50%" (Dubey et al.); XAI dan human-in-the-loop.
- **VRU:** camera-only mendeteksi "<30% potential pedestrian collisions", fused camera+LiDAR+radar mencegah ">90%" (Tengilimoglu et al.); model GWPR+NB memperbaiki hot spot ">10%".
- **Kritik penting (Discussion):** banyak "digital twin" sebenarnya **"digital shadow"** (aliran satu arah, tanpa aktuasi). Usulan **validasi bertahap**: Simulation-in-the-Loop → Hardware-in-the-Loop → **Shadow Mode Deployment** (twin menerima data live, keputusannya dicatat tapi tidak diaktuasi) → Phased Live Deployment (off-peak, human oversight, override). Bias vehicular-centric; isu privasi, bias, akuntabilitas; data historis jarang untuk kejadian langka → generative synthetic scenarios & transfer learning.
- **Hasil kuantitatif:** hanya angka yang dikutip dari paper lain (di atas).
- **Keterbatasan:** open-access ScienceDirect saja; screening LLM.
- **Relevansi: 5.** Memberi arsitektur referensi DT dan **protokol shadow mode** yang harus diadopsi ITCS Jakarta sebelum algoritma apa pun mengendalikan lampu nyata.

### A.4 Liu & Gayah (2022) — *A Novel Max Pressure Algorithm Based on Traffic Delay* (D-MP)
- **Sitasi:** Hao Liu, Vikash V. Gayah (Penn State). arXiv:2202.03290v3; Transportation Research Part C 143:103803 (2022).
- **Masalah:** Original-MP (Varaiya 2013) memakai jumlah kendaraan (point queue) — sulit diukur, tidak membedakan kendaraan berhenti/bergerak, dan "intersection approaches with low travel demand can incur arbitrarily large delays".
- **Metode/formulasi:**
  - Bentuk umum MP: $w_{(l,m)}(t)=\eta_{(l,m)}(t)-\sum_{n\in D(m)} r_{(m,n)}\eta_{(m,n)}(t)$; $P_\phi(t)=\sum_{(l,m)\in\phi} c_{(l,m)} w_{(l,m)}(t)$; $\phi^*=\arg\max_\phi P_\phi$.
  - D-MP: metrik $\eta$ = **total delay pada interval sebelumnya** $[(i-1)T, iT]$. Proposisi 3: total delay per step ≡ jumlah kendaraan berhenti (dengan asumsi kendaraan bergerak pada free-flow). Di simulasi, delay = $t\cdot n - d/v_f$ (Persamaan 38).
  - Teorema 4: D-MP mewarisi **maximum stability** (bukti Lyapunov mengikuti Varaiya; kunci: jumlah kendaraan bergerak terbatas, Proposisi 2).
  - Store-and-forward dengan lost time 3 s: saturation flow efektif $(T-3)/T\cdot s$ saat ganti phase → time step terlalu pendek membuat MP jarang berpindah phase.
- **Data/simulator:** SUMO, grid 4×4, 2 lajur/link, turning 0.2/0.5/0.3, demand N–S = 2× E–W, sat flow terkalibrasi 1.800 veh/h/lane, 10 seed. Pola 4 jam: low → naik ke high → konstan → turun.
- **Hasil:** time step optimal D-MP 5 s (Original-MP 9 s, TT-MP 9 s, H-MP 5 s). Total delay (internal + waiting): D-MP 184,84 s; H-MP 225,65 s; Original-MP 290,84 s; TT-MP 212,73 s → **reduksi 13,11%–36,44%**. D-MP punya stable region terbesar dan blocked vehicles paling sedikit. Di lingkungan connected vehicle (CV): D-MP unggul di low demand pada semua penetrasi; "when the penetration rate exceeds 50%, D-MP prevails over Original-MP and H-MP in a fully connected environment"; medium demand ambang >60% (dan >80% untuk mengalahkan H-MP full), high demand ambang 70%. Penetrasi 10% dibuang karena varians terlalu besar.
- **Keterbatasan:** phase order acak dan durasi kelipatan time step ("confusing to drivers and thus unacceptable for some city engineers"); tidak ada koordinasi; asumsi kapasitas antrean tak hingga.
- **Relevansi: 4.** Menunjukkan bahwa metrik **delay dari probe/GPS** (bukan antrean dari detektor) dapat menjadi masukan MP — cocok untuk data GPS TransJakarta/ojol. Namun untuk deploy perlu varian cyclic (lihat A.5).

### A.5 Tsitsokas, Kouvelas & Geroliminis (2022) — *Two-layer adaptive signal control ... Combining efficient Max-Pressure with Perimeter Control*
- **Sitasi:** D. Tsitsokas, A. Kouvelas, N. Geroliminis (EPFL/ETH). arXiv:2210.10453; Transportation Research Part C 152:104128 (2023).
- **Masalah:** MP efektif lokal tapi "effectiveness is questionable under over-saturated conditions and queue spill-backs", dan biaya instrumentasi naik dengan jumlah simpang; Perimeter Control (PC) berbasis MFD efektif regional tapi asumsi homogenitas lemah. Belum ada studi MP parsial (subset node).
- **Metode/formulasi (versi MP yang paling siap deploy):**
  - **Cycle-based MP** (mirip Kouvelas et al. 2014): cycle $C_n$, offset, dan urutan phase **tetap** (dari plan pre-timed), MP hanya mengubah split. Pressure link: $p_z(k_c)=\big(\tfrac{x_z}{c_z}-\sum_{w\in O_n}\beta_{z,w}\tfrac{x_w}{c_w}\big)S_z$ (antrean dinormalisasi kapasitas link → memperhitungkan risiko spillback), $P_{n,j}=\max\{0,\sum_{z\in v_j}p_z\}$, green mentah $\tilde g_{n,j}=\tfrac{P_j}{\sum_i P_i}G_n$.
  - **Proyeksi ke green feasible** (QP integer): $\min\sum_j(\tilde g_{n,j}-G_{n,j})^2$ s.t. $\sum_j G_{n,j}+L_n=C_n$; $G_{n,j}\ge g_{n,j,\min}$; $|G_{n,j}-G^p_{n,j}|\le \Delta g^R_{n,j}$; integer. Nilai: **min green 7 s, perubahan maksimum antar-cycle 5 s** ("to avoid instabilities").
  - **PC** via PI regulator: $u(k_c)=u(k_c-1)-K_P[n(k_c)-n(k_c-1)]-K_I[n(k_c)-\hat n]$, aktif hanya saat akumulasi mendekati setpoint (hysteresis start/stop); green rata-rata per boundary lalu dibagi ke simpang gerbang dengan bobot antrean (QP kedua).
  - **Node selection** untuk MP parsial: skor $R_n=\alpha m^1_n+\beta m^2_n+\gamma N^c_n$ (mean occupancy, varians occupancy, fraksi waktu ≥80% kapasitas); grid-search $\alpha,\beta,\gamma$.
- **Data/simulator:** Store-and-Forward termodifikasi (dengan spillback, S-Model), MATLAB+Gurobi; **Barcelona center: 1.570 link, 933 node, 565 simpang bersinyal, cycle 90–100 s**; medium 251k trip, high 316k trip; 3 region MFD; turn ratio diperbarui tiap 15 menit via shortest path.
- **Hasil (VHT vs fixed-time):** medium demand — MP 10% node kritis **−14,5%**, 25% **−18,8%**, **MP 100% hanya −10,6%**; PC saja −0,5%; PC+MP20% −17,7%. High demand — **MP 100% ≈ 0 (−0,2%)**, MP parsial −2,5…−7,6%; PC saja −7,6%; **PC+MP25% −15,6%**, PC+MP100% −16,3%. Skema tetap unggul saat demand berfluktuasi hingga 20% dari mean.
- **Keterbatasan:** pengetahuan sempurna antrean & turn ratio; mesoscopic; PI gain ditala trial-and-error; tanpa prioritas transit (disebut future work).
- **Relevansi: 5.** Ini **cetak biru operasional** untuk Jakarta: MP cyclic dengan cycle/offset tetap (koordinasi terjaga), constraint min-green & rate-limit, MP hanya di simpang kritis (hemat instrumentasi), plus gating perimeter untuk kawasan CBD saat jenuh. Temuan "MP di semua node bisa lebih buruk dari parsial" adalah peringatan penting.

### A.6 Ahmed, Liu & Gayah (2024) — *OCC-MP: A Max-Pressure framework to prioritize transit and high occupancy vehicles*
- **Sitasi:** Tanveer Ahmed, Hao Liu, Vikash V. Gayah. arXiv:2406.19269v2; Transportation Research Part C 166:104795 (2024).
- **Masalah:** MP tidak membedakan bus/HOV; TSP rule-based (Xu et al. 2022, RB-MP) memberi prioritas tanpa syarat → memperkecil stable region dan butuh lajur khusus.
- **Formulasi:** $w(l,m)=o(l,m)\cdot\big[x(l,m)-\sum_{n\in D(m)}x(m,n)r(m,n)\big]^+$, dengan $o$ = **rata-rata occupancy penumpang di upstream** (downstream tidak diberi bobot occupancy karena merepresentasikan supply). $P_\phi=\sum w\cdot C\cdot S$; acyclic (pilih phase max pressure tiap 10 s). Bukti maximum stability untuk simpang terisolasi (asumsi ekspektasi occupancy independen dari antrean). Baseline RB-MP: tambah konstanta besar $M$ pada weight jika ada bus.
- **Data/simulator:** AIMSUN, grid 8×8 (64 simpang, 4 phase), link 200 m, sat flow 1.800, 10 rute bus (7 high-occ 50 pnp/bus atau 12; 3 low-occ 25 atau 3), headway 2 atau 5 menit, demand high 32.256 / low 23.040 kendaraan; occupancy mobil pribadi diasumsikan 1,5 (skenario 1) atau diketahui (skenario 2, CV).
- **Hasil:** kenaikan travel time mobil pribadi: OCC-MP **0,36%–2,64%**, RB-MP **3,50%–25,75%** ("the best performance of RB-MP is still worse than the worst performance of OCC-MP"). Reduksi bus travel time: OCC-MP **14,5%** (bus penuh) / **7,5%** (bus sepi); RB-MP ≈30% konstan. Passenger travel time OCC-MP lebih rendah di 6/8 sub-skenario (0,1–3,6%); RB-MP naik hingga 21,2%. Robust terhadap error APC hingga σ=40%. Stable region OCC-MP ≈ Q-MP > RB-MP. Dalam CV parsial (20–100%), OCC-MP selalu PTT terendah.
- **Keterbatasan:** grid sintetis; acyclic (urutan phase acak); belum memodelkan dwell di halte.
- **Relevansi: 5.** Prioritas bus **kondisional** (bergantung muatan) tanpa mengorbankan stabilitas jaringan — sangat cocok untuk TransJakarta yang punya APC/GPS; parameter yang dibutuhkan: occupancy bus real-time, occupancy mobil asumsi 1,5, update 10 s.

### A.7 Tan, Liu, Sun, Rinaldi & van Lint (2025) — *Transit-MP: Transit-Prioritized Max-Pressure Control in Sparse Connected Vehicle Environments*
- **Sitasi:** Chaopeng Tan (TU Delft/TU Dresden), Hao Liu (Univ. of Maine), Dingshan Sun, Marco Rinaldi, Hans van Lint. arXiv:2511.00309, Okt 2025.
- **Masalah:** MP berbasis CV gagal saat penetrasi CV rendah (link tanpa observasi → pressure nol → **queue starvation**); OCC-MP mengasumsikan occupancy konstan dan mengabaikan dwell transit di halte.
- **Formulasi:** state upstream $\sum_{v\in V^{cv}_{i,o}}\delta_v p_v \tau_v$ (occupancy $p_v$ × normalized link travel time $\tau_v=LTT_v/ETT_{i,o}$; $\delta_v=0$ untuk transit yang belum melewati halte terdekat), downstream $\sum \delta_v\tau_v$ (tanpa occupancy). $c_{i,o}$ dipaksa 0 bila weight tanpa occupancy negatif. Teorema 2: **stabil jaringan di lingkungan CV parsial** (bukti Lyapunov dengan bobot upstream/downstream berbeda — kontribusi teoritis utama). **mTransit-MP**: bila tidak ada CV pada movement, gunakan estimasi historis (arrival rate $\hat\lambda$, penetrasi $\hat\rho$, model IQA: $E[Q(t)]=\max\{0,E[Q(t-T_0)]+\hat\lambda T_0-s\,\mu^{dep}T_0\}$, delay $\approx E[Q]^2/(2\hat\lambda)$); Teorema 3: bebas queue starvation.
- **Data/simulator:** SUMO, **koridor nyata Amsterdam 3 simpang, 7 tram + 8 bus, 31 halte**, lajur dedicated/mixed/umum, decision step 10 s, yellow 3 s, 3 seed.
- **Hasil:** memperhitungkan halte (eOCC-MP vs OCC-MP): transit delay −23–30%, passenger delay −31,6%, car delay −16,9%. Transit-MP vs eOCC-MP: transit delay −5–43% lebih lanjut, passenger delay −17,9%, car delay −21,8%, max spillover 5,3 kendaraan (**−94,2%**). Pada penetrasi 0,2: multimodal delay −21,9%, spillover −94,3%. mTransit-MP pada penetrasi 0,1: spillover −61,8%, delay −14,2%, passenger delay −11,7%; tidak sensitif terhadap error estimasi ±50%. Segmentasi link 420 m terbaik untuk Transit-MP (link >900 m tanpa segmentasi memberi green terlalu dini).
- **Keterbatasan:** koridor kecil; asumsi rute CV diketahui; privasi.
- **Relevansi: 5.** Langsung relevan: Jakarta punya GPS bus (penetrasi transit 100%) tetapi probe mobil pribadi jarang; mekanisme fallback historis (mTransit-MP) dan pengecualian bus yang masih di halte adalah detail implementasi yang wajib.

### A.8 Talluri, Stang & Weidl (2025) — *Green Wave as an Integral Part for the Optimization of Traffic Efficiency and Safety: A Survey*
- **Sitasi:** K. K. Talluri, C. Stang, G. Weidl (Aschaffenburg UAS / ZF). arXiv:2507.22511; IEEE Intelligent Vehicles Symposium 2025.
- **Masalah:** survei metode green wave dan dampaknya pada efisiensi, lingkungan, keselamatan; integrasi V2X.
- **Metode:** review (IEEE Xplore/Scopus/GS, 2011–2024). Taksonomi: fixed-time (Webster; offset $t_{i,j}=L_{i,j}/v$ satu arah; MAXBAND MILP dua arah), actuated (MOVA; "Green Wave corridors infeasible" karena cycle bervariasi), adaptif industri (SCOOT common cycle + split/offset; SCATS hierarkis supervisor–regional–local; UTOPIA dua level; RHODES/OPAC "less field penetration"), akademik (fuzzy, GA/PSO/ACO, RL/MDP dengan tabel state/action/reward). Bagian V2X: MICA-V, C-V2X platooning, GLOSA, DDPG-BAND/ES-BAND (reward bandwidth).
- **Hasil kuantitatif (dikutip dari sumber lain):** GLOSA hemat bahan bakar "up to 15%"; eco-speed planning 16,65% energi & 26,33% travel time [1]; eco-speed V2I 20% bahan bakar [17]; platoon stability +45% [11]; green wave menurunkan CO2/NOx/PM10 10–40% [15]; simpang bersinyal menaikkan CO2 11,52% akibat stop [70]; RL adaptif +41% kecepatan rata-rata [71]; countdown timer mengurangi red-light running tetapi berpotensi mengganggu koordinasi pejalan kaki.
- **Keterbatasan:** survei pendek (konferensi); tidak ada eksperimen sendiri; banyak klaim kuantitatif berasal dari studi simulasi kecil.
- **Relevansi: 3.** Berguna untuk kerangka green wave (common cycle + offset) dan justifikasi manfaat lingkungan, serta ide GLOSA lewat aplikasi navigasi; tetapi tidak memberi algoritma yang langsung deployable.

### A.9 Kwesiga, Vishnoi, Guin & Hunter (2024) — *Integrating Transit Signal Priority into MARL-based TSC*
- **Sitasi:** D. K. Kwesiga, S. C. Vishnoi, A. Guin, M. Hunter (Georgia Tech). arXiv:2411.19359 (TRB submission, Agustus 2024).
- **Masalah:** kedatangan bus jarang → melatih satu agen RL untuk lalu lintas umum sekaligus TSP tidak efisien; usulan **agen TSP event-based** terpisah yang aktif hanya saat bus masuk zona komunikasi.
- **Metode:** Vissim, 2 simpang berjarak 1.600 ft, v/c 0,95, halte far-side, dwell dari data APC MARTA. Background: MARL DDQN dengan **VDN** ($Q_{tot}=\sum_i Q_i$), state = jumlah kendaraan per lajur + signal state kedua simpang, aksi = phase berikutnya (4 phase) dengan **invalid action masking** (min/max green, clearance, sequence), reward $r=-\bar d - N - M + P$ (penalti antrean samping, penalti ganti phase prematur, bonus offset koordinasi EB). TSP agent: state tambahan vektor posisi/kecepatan bus dalam sel 25 ft (zona 800 ft, DSRC), reward gabungan bus delay, bus speed, penalti antrean samping; dua varian: independen (DTDE) dan terkoordinasi (CTDE/VDN). Hyperparameter: 3 layer (128/256/256), lr 0,01, γ 0,99, buffer 20.000.
- **Hasil:** VDN MARL sedikit lebih baik dari coordinated actuated (ASC) pada v/c 0,95 (konvergen ~900 episode). TSP independen: bus travel time **−22%**; terkoordinasi **−27%**; kedua varian konvergen ke bus delay ≈25 s, tetapi DTDE tidak stabil selama training. Dampak side-street kecil kecuali satu gerakan (B_SB_LT +18%).
- **Keterbatasan:** 2 simpang sintetis; tanpa pejalan kaki; training ratusan–ribuan episode.
- **Relevansi: 3.** Konsep **agen prioritas event-based di atas pengendali latar** (bukan satu agen monolitik) dan invalid action masking layak ditiru; namun RL-TSP tidak lebih praktis daripada OCC/Transit-MP untuk 321 simpang.

### A.10 Muresan, Fu & Pan (2019) — *Adaptive TSC with Deep RL: An Exploratory Investigation*
- **Sitasi:** M. Muresan, L. Fu, G. Pan (Univ. of Waterloo). arXiv:1901.00960; TRB 97th Annual Meeting.
- **Masalah:** eksplorasi DRL untuk satu simpang dengan state yang menyertakan time-of-day/day-of-week.
- **Metode:** VISSIM + TensorFlow; state matriks bit 80×80 (antrean, signal state, TOD, DOW; 4 frame terakhir), CNN 3 layer; aksi biner (lanjut/ganti phase, ring-barrier, **min green 10 s** dipaksakan); reward +20 per kendaraan discharged, −1 per kendaraan menunggu, −5 per kendaraan tersisa di antrean saat green berakhir; kendaraan <15 km/jam dianggap antre; ε-greedy 1→0,005; 61 hari simulasi training, 2 hari uji.
- **Hasil:** delay rata-rata **−32% vs semi-actuated** (Synchro, 4 plan TOD) dan **−37% vs fixed-time**; manfaat terbesar saat under-saturated; skenario tak terduga (side street 600 vph vs 175 saat training) tetap ditangani. Kelemahan: pada 30 hari pertama "occasionally make a suboptimal set of actions resulting in a major delay".
- **Keterbatasan:** satu simpang, 2 phase, tanpa belok; tidak ada koordinasi.
- **Relevansi: 2.** Nilai historis; menunjukkan reward berbasis discharge/antrean dan constraint min-green, tetapi skala dan formulasi jauh dari kebutuhan Jakarta.

### A.11 Zhu, Liu, Borst & Walid (2025) — *Deep RL for Traffic Light Control in ITS*
- **Sitasi:** Ming Zhu, Xiao-Yang Liu, Sem Borst, Anwar Walid. arXiv:2302.03669v4; IEEE Trans. Network Science & Engineering (2025).
- **Masalah:** skalabilitas DRL dan apakah perilaku "greenwave" muncul secara alami.
- **Metode:** model stylized discrete-time: state $(X_1,X_2;L)$ (antrean dua arus + konfigurasi lampu 0–3), aksi lanjut/ganti, satu kendaraan lewat per slot, reward $-|X|^2$ (kuadrat antrean). DQN (satu simpang) vs kebijakan optimal via policy iteration; DDPG diskretisasi (sigmoid curam) untuk grid 5×10. Bukti analitik (fluid model, arteri N simpang): kebijakan **greenwave** (semua lampu berganti serentak saat selisih antrean arteri–jalan silang mencapai ambang) **unik optimal** dengan panjang green/red $G=\lambda_0(Y+O)/(1-\lambda_0-\lambda_{max})$.
- **Hasil:** DQN mereplikasi thresholding policy optimal; DDPG memunculkan pola greenwave di 5×10 tanpa diprogram. Tidak ada angka delay absolut yang dapat dibandingkan dengan praktik.
- **Keterbatasan:** model sangat disederhanakan (tanpa belok, 1 kendaraan/slot); bukan simulator mikro.
- **Relevansi: 2.** Wawasan teoretis: koordinasi arteri optimal = pergantian serentak dengan offset (green wave), mendukung pendekatan common-cycle/offset klasik; tidak untuk implementasi.

### A.12 Guo (2019) — *Decentralized Deep RL for Network Level TSC* (tesis MS, UC Davis)
- **Sitasi:** Jin Guo (advisor M. Zhang). arXiv:2007.03433.
- **Masalah:** MARL terdesentralisasi penuh tanpa unit pusat; tiga tingkat komunikasi: IDQL (tanpa), S2RL (share state), **S2R2L** (share state & reward).
- **Metode:** SUMO, grid Manhattan 4×4 satu arah, link 150 m; observasi lokal (occupancy & queue ratio per lajur, one-hot stage, rasio waktu berjalan) dalam radius 150 m; aksi pilih stage tiap **5 s**, yellow+all-red 3 s, **min green 10 s, max green 60 s**; reward selisih total waiting time; S2R2L reward berbobot $\frac{1}{n+|N(i)|}(n r_i+\sum_j r_j)$, $n=2$ terbaik. n-step Double DQN + prioritized replay, dropout 0,4. Benchmark **Max Pressure** (dalam jaringan ini tereduksi ke Longest-Queue-First).
- **Hasil:** S2R2L **−34,55% delay, −10,91% queue** vs MP (jaringan); tetapi **MP terbaik saat demand rendah** dan di beberapa simpang MP tetap lebih baik. Sensitivitas max green: S2R2L bagus di 50–60 s, buruk di 30 s; MP terbaik di 40 s. Bab 6 mengusulkan policy-gradient + importance sampling untuk menutup reality gap (konseptual).
- **Keterbatasan:** grid satu arah sintetis; MP disederhanakan; tesis.
- **Relevansi: 2.** Menunjukkan perlunya **max green ≤60 s sebagai guard-rail** dan bahwa MP sederhana bisa kalah saat jenuh — tetapi bukti dari jaringan mainan.

### A.13 Zeng et al. (2024/2025) — *CityLight: A Neighborhood-inclusive Universal Model for Coordinated City-scale TSC*
- **Sitasi:** Jinwei Zeng, Chao Yu, Xinyi Yang, Wenxuan Ao, Qianyue Hao, Jian Yuan, Yong Li, Yu Wang, Huazhong Yang (Tsinghua). arXiv:2406.02126v4 (2025).
- **Masalah:** kontrol ribuan simpang heterogen (3/4 lengan) dengan **satu universal policy** (parameter sharing) yang juga merepresentasikan pengaruh tetangga.
- **Metode:** Dec-POMDP; **MAPPO** parameter-sharing; observasi per phase (antrean, last-passing flag, jumlah lajur; 3 lengan di-pad −1) dengan phase reindexing; Neighbor Influence Encoder (cross-attention relasi arus + konektivitas jarak/lajur) dan Aggregator (competing group); reward $r_i=q_i+\alpha\cdot\text{mean}_{j\in N(i)}q_j$ (mean-field). Keputusan tiap 15 s, episode 60 menit. Simulator **MOSS** (GPU, ~100× SUMO).
- **Data:** Manhattan 196, Chaoyang 97, Central Beijing 885, Jinan 4.064 (dari kamera), **Beijing 13.952 simpang** (OD dari LBS).
- **Hasil:** rata-rata **+11,68% throughput** vs baseline terbaik; transfer lintas skala/kota **+22,59%** (30,57% lintas skala, 14,62% lintas kota). Contoh Beijing: Max Pressure TP 60.615/ATT 1.134 → CityLight 70.451/1.030. Training ~9 jam, 1×RTX 4090, ~20 GB; metode individual-policy (CoLight) butuh >2 hari dan tak dapat dijalankan di Jinan/Beijing. Ablasi: tiap modul menyumbang 1,3–2,2%.
- **Keterbatasan:** simulator mesoscopic tanpa pejalan kaki/bus; aksi phase-selection acyclic; belum ada uji lapangan.
- **Relevansi: 3.** Bukti bahwa RL city-scale **secara komputasi** feasible dan bahwa **Max Pressure adalah baseline kuat** (di Beijing MP mengalahkan semua baseline lain kecuali CityLight). Cocok sebagai riset offline/advisor untuk Jakarta, bukan kontrol langsung.

### A.14 Guo, Li, Zhang, Zhang, Li & Li (2024) — *Scalable Multi-Objective Optimization for Robust TSC in Uncertain Environments* (AHMOA)
- **Sitasi:** Weian Guo et al. (Tongji). arXiv:2409.13388.
- **Masalah:** optimasi sinyal jaringan ribuan simpang dengan objektif konflik dan ketidakpastian (cuaca, libur, insiden).
- **Metode:** variabel keputusan **red-light ratio $\rho_i$** per simpang (level makroskopik, bukan phase); tiga objektif: $f_1$ delay rata-rata (Webster termodifikasi $D=\tfrac{C(1-g/C)^2}{2(1-\rho x)}+\tfrac{x^2}{2s(1-x)}$), $f_2$ stabilitas jaringan (selisih volume antar simpang/waktu × $|\rho_i-\rho_{i+1}|$ × adjacency), $R$ robustness (std objektif antar jam). AHMOA: GA/DE/PSO/Local Search dengan probabilitas adaptif dari success rate, memori historis, non-dominated sorting; cuaca $\omega(t)=0,8+0,4\sin(2\pi t/T)$; tiap solusi dievaluasi 5×.
- **Data:** generator sintetis 24 jam; Manhattan 2.640 simpang (22 arteri, 120 kolektor), Paris 1.200, Istanbul & São Paulo 30 arteri/50 kolektor. Pop 120, 50 generasi. Pembanding MOEA/D, NSGA-III, NSDE3.
- **Hasil:** Manhattan: seluruh 17 solusi Pareto global dari AHMOA; Istanbul/Paris: MOEA/D lebih baik pada delay, AHMOA unggul pada stabilitas/robustness. **Tidak ada angka reduksi delay absolut** (hanya log-objective dan peta warna).
- **Keterbatasan:** model makro tanpa mikrosimulasi; variabel hanya rasio merah; tidak real-time.
- **Relevansi: 2.** Ide "robustness sebagai objektif" dan evaluasi multi-jam relevan untuk **penyusunan TOD plan offline** yang tahan variasi, tapi bukan pengendali online.

### A.15 Duan, Gao, He & Xian (2024) — *Bayesian Critique-Tune-Based RL with Adaptive Pressure for Multi-Intersection TSC* (BCT-APLight)
- **Sitasi:** Wenchang Duan, Zhenguo Gao, Jiwan He, Jinguo Xian (SJTU). arXiv:2412.16225v2.
- **Masalah:** RL "excessive trust" pada policy yang tidak masuk akal; pressure konvensional mengabaikan bobot berbeda tiap lajur upstream ke downstream.
- **Metode:** (1) **Adaptive Pressure** $p(X_y,X'_{y'})=x(l_k)-\sum_j \omega_{jk}x(m_j)$ dengan $\omega$ dari multi-head attention atas matriks 3×3×4 (waiting/running/total per lajur/arah); (2) **Critique layer**: SARIMA + prior Bayesian (truncated normal/Laplace/inverse-gamma) atas reward historis → credible interval 95%; jika predicted reward keluar interval, (3) **Tune layer**: KDE prior atas Q historis + likelihood Gaussian Q saat ini → pilih phase yang meminimumkan posterior risk (square loss). Backbone DQN; reward = insentif throughput − penalti ganti phase. CityFlow; **durasi aksi minimum 30 s, yellow 3 s, all-red 2 s**.
- **Data:** 7 dataset nyata: Jinan 3×4 (3), Hangzhou 4×4 (2), New York 28×7 (2).
- **Hasil:** vs Advanced-CoLight: **ATT −3,01%, AQL −9,60%, AWT −15,28%**; vs MaxPressure: ATT −7,83%, AQL −21,74%, AWT −20,69%; vs LightGPT (LLM) ATT −8,08% dan LightGPT kalah dari MaxPressure. Ablasi: AP-DQN vs DQN ATT −26,62%, AQL −52,36%, AWT −58,21%; CT di atas Advanced-CoLight +1,74/4,83/7,01%. New York-1 ATT 755,06 s vs 800,96 (Advanced-CoLight).
- **Keterbatasan:** kompleksitas tinggi; tanpa transit/pejalan kaki; tidak ada uji lapangan.
- **Relevansi: 3.** Dua ide berguna: (a) **lapisan "critique" statistik yang memveto keputusan RL anomali** — pola guard-rail yang bisa diadopsi; (b) LLM-agent (LightGPT) belum kompetitif dengan Max Pressure.

### A.16 Kwesiga, Guin, Abdelghany & Hunter (2026) — *Evaluating the Robustness of RL-based Adaptive TSC*
- **Sitasi:** D. Kwesiga, A. Guin (Georgia Tech), K. Abdelghany (SMU), M. Hunter. arXiv:2603.15283.
- **Masalah:** kebanyakan studi RL memakai struktur phase sederhana, diuji pada demand yang sama dengan training, dan dibandingkan hanya dengan fixed-time.
- **Metode:** **PPO** (clip 0,2, lr aktor 3e-4/kritik 1e-3, γ 0,99, entropy 0,01); state = jumlah kendaraan per lajur + elapsed green per phase (asumsi CV/video + SPaT); aksi = pasangan phase kompatibel dalam **dual-ring barrier 8 phase** ({1,5},{1,6},{2,5},{2,6},{3,7},{3,8},{4,7},{4,8}) dengan invalid action masking; time step dinamis = min ring-step; reward $r=-\sum_v d_v/d_{max}$, $d_{max}=300$ s. **Distributed asynchronous training** (learner + worker PCs, banyak instance SUMO). Robustness diukur dengan SSIM antar matriks OD (dissimilarity hingga 0,603); v/c 0,5–1,05; baseline **fully-actuated ASC yang dioptimasi Synchro** per pola OD.
- **Hasil:** pada OD training, RL mengurangi delay **11,1%–31,7% per gerakan vs ASC**. Model I (satu OD) gagal pada OD D (delay EBL/EBT melebihi ASC); Model II (OD A+B+C) tetap mengalahkan ASC pada OD tak terlihat (D, E, F) kecuali gerakan volume sangat rendah (60 veh/h). Konvergensi: Model I ~500 episode, Model II ~1.250 (training hingga 5.000 episode).
- **Keterbatasan:** satu simpang hipotetis; tanpa noise sensor; tanpa transit.
- **Relevansi: 4.** Memberi pola RL yang **kompatibel dengan controller lapangan** (ring-barrier NEMA-like) dan bukti bahwa **diversitas demand saat training** wajib; juga menegaskan ASC yang dioptimasi sebagai baseline yang benar.

### A.17 Jan, Syed, Kamal, Wali & Akarma (2026) — *Autonomous Traffic Signal Optimization Using Digital Twin and Agentic AI*
- **Sitasi:** Salman Jan (MMU/Arab Open Univ.), T. A. Syed, S. Kamal, Q. Wali, A. Akarma. arXiv:2604.27753.
- **Masalah:** kerangka DT + agentic AI untuk optimasi sinyal real-time.
- **Metode (arsitektur):** Physical layer (loop/IR/kamera/IoT + edge preprocessing) → Data & Modeling layer (Feature Store; DT model simpang/phase/antrean; operations interface) → Agentic block (LangChain/GraphChain): **Perception Agent**, **Risk Agent** (probabilitas kongesti/propagasi), **Simulation Agent** (what-if di DT, daftar kandidat), **LLM Explanation Agent** ("not involved in the control loop, thus preventing non-deterministic actions") → Action layer: **Governance Agent** (cek kepatuhan pra-eksekusi) + **MCP Gateway** (schema-validated) ke traffic management API; Secure Message Bus (mTLS, RBAC) + Decision & Event Log.
- **Data:** jaringan sintetis 12 simpang, 3 skenario (ringan, berat, insiden); baseline fixed 60 s dan "RL controller trained on six months of data".
- **Hasil (rata-rata 3 skenario):** flow efficiency 85% (RL 80%, fixed 75%); rata-rata wait **49 s vs 54 s (RL) vs 60 s (fixed)** → −18% vs fixed, −9% vs RL; unggul terbesar di skenario insiden. Metrik "flow efficiency" tidak didefinisikan; simulator tidak disebut.
- **Keterbatasan:** evaluasi sangat tipis; tidak ada detail algoritma keputusan deterministik.
- **Relevansi: 3 (arsitektur) / 1 (bukti kinerja).** Pola arsitektur governance — LLM hanya untuk penjelasan, validasi skema perintah, audit log, gateway aman — sangat relevan untuk ITCS; klaim kinerja tidak dapat diandalkan.

### A.18 Humagain & Sinha (2020) — *Routing Emergency Vehicles in Arterial Road Networks using Real-time Mixed Criticality Systems*
- **Sitasi:** S. Humagain, R. Sinha (AUT, Auckland). arXiv:2109.03210; IEEE ITSC 2020, pp. 1–6.
- **Masalah:** preemption absolut untuk semua EV merugikan lalu lintas umum dan tidak menyelesaikan konflik multi-EV; EMS tetap sulit memenuhi target respons.
- **Metode:** memetakan tingkat darurat (NZ: **purple/red/orange** = high/medium/low) ke tingkat kritikalitas RTMCS dengan target waktu tempuh berbeda; EVP hanya dipicu bila $\Delta=t^{cur}-t^{target}>0$ ($t^{target}=d/v_{limit}\cdot a_{level}$, $t^{cur}=d/v_{now}$); konflik antar-EV di satu simpang diselesaikan dengan **conflict graph** (approach = node, konflik = edge); green reserve dihitung dari posisi/kecepatan yang dikirim via VANET (DSRC 5,9 GHz, IEEE 802.11p); jika lampu sedang hijau → extend, jika tidak → ganti phase.
- **Data:** SUMO + OMNeT++ + Veins; potongan arteri Auckland terkalibrasi; sat flow 1.800 pcu/jam/lajur; demand 450/850/1.800 pcu/jam/lajur; EV 1% kendaraan, proporsi kritikalitas 63,6/23,2/13,3% (data St John); target 8/12/20 menit (bagian awal menyebut 8/12/16 — inkonsisten dalam teks).
- **Hasil:** success rate EV memenuhi target **96%** pada densitas tinggi (95% untuk EV kritikalitas tinggi); waiting time non-EV "almost comparable to the system without pre-emption"; antrean rata-rata turun **hingga 36%** vs absolute preemption; throughput ≈ tanpa preemption (absolute preemption terendah). Angka waktu tunggu absolut hanya dalam grafik.
- **Keterbatasan:** butuh V2I/GPS di EV; tidak membahas recovery koordinasi pasca-preemption; simulasi tunggal.
- **Relevansi: 4.** Model **preemption bersyarat & bertingkat** (hanya bila EV terlambat dari target) plus resolusi konflik multi-EV adalah fitur konkret untuk modul emergency ITCS (ambulans/pemadam dengan GPS/AVL).

### A.19 Mahmud & Day (2023) — *Evaluation of Arterial Signal Coordination with Commercial Connected Vehicle Data*
- **Sitasi:** Shoaib Mahmud, Christopher M. Day (Iowa State). Journal of Transportation Technologies 13:327–352, 2023 (file arXiv_2212.02315).
- **Masalah:** mengevaluasi kualitas progression koridor **tanpa infrastruktur detektor**, memakai data trajektori CV komersial (Wejo).
- **Metode:** data waypoint tiap ~3 s (journey ID, posisi, kecepatan); 90.000 journey/10,3 juta waypoint → geofence & filter → **53.656 journey, 3,9 juta waypoint, 4 minggu**; map-matching; **penetrasi 3–6% AADT**, diatasi dengan agregasi multi-hari (TOD plan sama tiap weekday). Metrik: travel rate $r_i=t_i/D$, travel time index $T_i=t_i/t_f$, delay $d_i=t_i-t_f$ (free-flow = speed limit), **SOFT** (Fourier atas profil kecepatan, 0–100), agregasi berbobot per OD path. Visualisasi: **cyclic time-space diagram** ($\tau=t \bmod C$), **empirical Platoon Progression Diagram** (bin 1 s × 100 ft), **speed heat map** per jam (ambang antrean 35 mph dari limit 45 mph).
- **Data:** US-20 Dubuque, Iowa, **8 simpang, 2,6 mil**, cycle TOD 103–130 s.
- **Hasil:** metrik memberi gambaran berbeda tergantung OD path yang disertakan (end-to-end vs semua); PPD dengan semua journey mengungkap platoon sekunder/tersier yang tak terlihat; heat map menunjukkan antrean terluas EB 11:00–14:00 dan WB 14:00–17:00; indikasi green terlalu pendek di segmen tertentu. Tidak ada klaim persentase perbaikan (paper evaluasi, bukan kontrol).
- **Keterbatasan:** offline; penetrasi rendah; cycle length harus diketahui persis (salah sedikit → pola hilang).
- **Relevansi: 5.** Metodologi langsung dapat diterapkan pada **GPS TransJakarta/ojol/aplikasi navigasi** untuk menilai dan menala offset/green wave di Jakarta tanpa memasang detektor di semua simpang.

### A.20 Werbińska-Wojciechowska, Giel & Winiarska (2024) — *Digital Twin Approach for Operation and Maintenance of Transportation System — Systematic Review*
- **Sitasi:** Wroclaw University of Science and Technology; Sensors 24(18):6069, MDPI, 2024; PMC11435829.
- **Masalah:** review sistematis (PRISMA, Primo multi-search) DT untuk operasi & pemeliharaan sistem transportasi; 2.509 → **201 paper** (2012–2024), 7 kelompok: air (37), rel (38), **jalan (44)**, in-house logistics (34), air/intermodal (19), supply chain (14), lainnya (15). Bibliometrik VOSviewer.
- **Konsep kunci:** DT = physical object + virtual model + koneksi **dua arah otomatis**; dibedakan dari **Digital Model** (manual) dan **Digital Shadow** (fisik→digital otomatis, umpan balik manual). Siklus hidup DT: prototype (DTP) → instance (DTI). Kualitas sensor menentukan kegunaan DT ("sensor failures ... can even lead to the failure of the physical object as it is operated based on feedback from the DT").
- **Transportasi jalan:** DT dipakai untuk "optimizing traffic conditions, planning urban transportation, calculating recommended vehicle speeds, controlling traffic signals, visualizing possible scenarios, and enhancing road safety"; disebut arsitektur referensi Transportation DT (Irfan et al.), DT untuk ATSC (Dasgupta et al.), 3D DT berbasis road-side sensing, Mobility Digital Twin (Wang et al.), Kušić et al. (sinergi stream data & simulasi motorway).
- **Kerangka (RQ4, berbasis ISO 23247):** Level I *Observable Elements* (aset fisik + sensor); Level II *Communication unit* (data collection + device control) → dua mode: **fully automated** (closed loop) dan **semi-automated** (instruksi dari user); Level III *Digital twin unit* (model virtual + cache data historis); Level IV *User unit* (tujuan, simulasi, forecasting, reporting, integrasi); *Cross-system entity* (translasi protokol, integrasi, keamanan). Komponen: data acquisition & integration, analytics & visualization, simulation & modeling, collaboration tools, feedback loop. Enam fungsi: condition monitoring, failure prediction, maintenance scheduling, resource management, reporting & compliance, feedback loop.
- **Gap:** integrasi dengan sistem eksisting, real-time data integrity/security, standardisasi, skalabilitas, interaksi & pelatihan pengguna, interoperabilitas, kepatuhan regulasi, keamanan siber, biaya investasi.
- **Hasil kuantitatif:** hanya bibliometrik (misal China 25% paper; 173 dari 201 terbit 2021–2024).
- **Keterbatasan:** fokus O&M/in-house logistics, bukan kontrol lalu lintas; tidak ada evaluasi kinerja.
- **Relevansi: 3.** Berguna untuk **struktur organisasi DT dan pemeliharaan aset ITCS** (kamera, controller, komunikasi) — DT bukan hanya untuk lalu lintas tetapi juga untuk kesehatan perangkat 321 simpang; kerangka ISO 23247 dan mode semi/fully automated dapat menjadi standar dokumen desain.

---

## B. Sintesis Lintas Paper: Taksonomi Metode, Kelebihan/Kekurangan, Kesiapan Deployment, Kebutuhan Detektor

### B.1 Taksonomi dan penilaian

| Kelas metode | Contoh dari paper | Kelebihan (menurut paper) | Kekurangan | Kesiapan deploy | Kebutuhan data/detektor |
|---|---|---|---|---|---|
| **Fixed-time / Webster / TOD plans** | A.1, A.8, A.14 | Tanpa sensor; stabil under-saturated; offset mudah dikoordinasikan (A.12: "fixed timing provides enough resilience for offset"); dasar green wave (MAXBAND) | Tidak merespons fluktuasi; plan usang jika tak di-retime (A.10: retiming saja bisa −10% delay) | **Sangat tinggi** (baseline & fallback wajib) | Hanya hitungan historis |
| **Actuated (semi/fully), MOVA** | A.1, A.8, A.12, A.16 | Merespons kehadiran kendaraan; state of practice (A.16) | "Relatively myopic" (A.1); cycle bervariasi sehingga green wave sulit (A.8); semi-actuated ≈ fixed pada praktiknya (A.10) | Sangat tinggi | Detektor presence/gap per approach (loop/kamera) |
| **SCATS/SCOOT-like 2G adaptive (hierarkis, cycle/split/offset online)** | A.1, A.2, A.8 | Deployed global; koordinasi regional; priority/preemption native (SCATS, A.2); pedestrian-friendly (cycle-based) | Kurang tanggap pada high-density/highly dynamic (A.1); butuh detektor stop-line/upstream tiap simpang | Sangat tinggi (produk komersial) | Loop/kamera per approach; komunikasi ke regional master |
| **Max-Pressure & varian** (Original, D-MP, cyclic MP, OCC-MP, Transit-MP, mTransit-MP, PC+MP) | A.4–A.7, A.5 | Terdesentralisasi, tanpa prediksi demand, **maximum stability** terbukti; bisa dipasang bertahap (A.5: "gradual installation to network is theoretically possible"); varian cyclic menjaga cycle/offset tetap; OCC/Transit-MP memberi TSP kondisional dengan stabilitas terjaga | Acyclic MP membingungkan pengemudi (A.4); tidak optimal secara delay; lemah saat semua antrean jenuh (A.5: MP 100% ≈ 0 pada high demand) dan pada demand rendah kalah dari RL (A.12); butuh antrean/occupancy up- dan downstream + turning ratio | **Tinggi** (heuristik sederhana; ada uji lapangan TT-MP menurut A.4/A.7) | Antrean atau delay per link (kamera/probe), turning ratio (dapat diestimasi, A.5), occupancy bus (APC) |
| **MPC / rolling-horizon (OPAC, RHODES, SURTRAC)** | A.1, A.2 | Model eksplisit, bukti stabilitas, menangani disturbance via feedforward; SURTRAC deployed | Butuh model terkalibrasi & komputasi online; "none of them [MPC] has been tested in the field" (A.1) | Sedang (SURTRAC tinggi) | Detektor advance + stop-bar, turn ratio |
| **RL single-agent** | A.10, A.11, A.16 | −11…−37% delay vs actuated dalam simulasi; adaptif pada kejadian tak terduga | Belum pernah deployed (A.2); distribution shift (A.1, A.16); training ribuan episode | Rendah–sedang | Hitungan per lajur + SPaT; simulator terkalibrasi |
| **MARL / universal policy** | A.9, A.12, A.13, A.15 | Skalabel (CityLight 13.952 simpang); koordinasi implisit; mengalahkan MP di simulasi | Non-stasioner (DTDE tidak stabil, A.9/A.12); CTDE policy beku (A.1); tanpa bus/pejalan kaki; black box (A.12: "mistrained MARL controller ... even cause fatal accidents") | Rendah | Data jaringan luas; GPU untuk training |
| **Multi-objective evolutionary (offline)** | A.14 | Robust terhadap variasi jam/cuaca; Pareto trade-off | Bukan real-time; model makro | Sedang untuk desain plan | Volume historis per simpang |
| **Hybrid: RL + statistical veto; MP + PC; agen event-based** | A.15, A.5, A.9, A.17 | Guard-rail eksplisit; memadukan keunggulan | Kompleksitas | Sedang–tinggi (untuk bagian rule-based) | Gabungan |
| **LLM/agentic** | A.15 (LightGPT), A.17 | Penjelasan/explainability; orkestrasi | LightGPT kalah dari MaxPressure (A.15); biaya API; non-deterministik → harus di luar control loop (A.17) | Rendah (kontrol), sedang (explanation/ops) | — |

### B.2 Sim-to-real gap, robustness, safety constraints
- **Belum ada RL yang deployed** (A.2); penyebab: detektor tidak ideal, komunikasi, kepatuhan, road users heterogen. A.1 menambahkan alasan teoretis: non-stasioneritas dan **distribution shift** — policy beku hanya baik pada state yang sering dikunjungi saat training.
- Bukti empiris robustness: A.16 — model satu-OD gagal pada OD tidak mirip (1−SSIM 0,603), model multi-OD robust; A.10 — RL tetap merespons lonjakan 4× volume side street. A.3 dan A.12 menyebut domain randomization / noise injection sebagai mitigasi.
- **Safety constraints** yang muncul konsisten: min green (7 s di A.5; 10 s di A.10/A.12), max green (60 s, A.12), yellow 3 s + all-red 2 s (A.15), perubahan split ≤5 s/cycle (A.5), phase sequence tetap / ring-barrier (A.5, A.16), invalid action masking (A.9, A.16), durasi aksi minimum 30 s (A.15), penalti ganti phase (A.15, A.9). A.2 menambah LePI/pedestrian minimum green dan review AMF.
- **Kualitas data** menentukan: A.4/A.6/A.7 menunjukkan MP berbasis probe menurun tajam di bawah ~20–30% penetrasi; A.7 memberi fallback historis; A.19 memakai agregasi multi-hari untuk penetrasi 3–6%.

### B.3 Kebutuhan detektor untuk Jakarta (321 simpang, kamera AI)
- **Minimum untuk actuated/cyclic-MP:** per approach: antrean/occupancy (kamera CV; A.2 memperingatkan degradasi malam/hujan → butuh fallback), hitungan per phase; turning ratio dapat diestimasi online (A.5) atau dari OD probe (A.19).
- **Untuk prioritas bus:** posisi GPS bus + APC (A.6/A.7); flag halte agar bus di halte tidak memicu prioritas (A.7).
- **Untuk emergency:** GPS/AVL EV + rute (A.18).
- **Untuk koordinasi/green wave:** data trajektori probe multi-hari (A.19) + cycle length yang tepat.
- **Untuk perimeter control:** akumulasi kendaraan per region (MFD) dari kamera/probe (A.5).

---

## C. Prioritas Transit dan Preemption Darurat: Integrasi ke Max-Pressure/RL dan Parameter

| Pendekatan | Mekanisme | Parameter yang dipakai di paper | Dampak yang dilaporkan |
|---|---|---|---|
| **RB-MP** (rule-based dalam MP; Xu et al. 2022 direplikasi di A.6) | Tambah konstanta besar $M$ ke weight movement jika ada bus di antrean → prioritas tanpa syarat | Update 10 s; lajur bus khusus (asli) | Bus −≈30% VTT tetapi mobil +3,5–25,8%; PTT bisa +21,2%; stable region mengecil |
| **OCC-MP** (A.6) | Weight = occupancy rata-rata upstream × (queue diff)$^+$; downstream tanpa occupancy | Occupancy bus dari APC; mobil 1,5 pnp (atau dari CV); update 10 s; robust error APC σ≤40% | Bus −14,5%/−7,5%; mobil +0,36–2,64%; PTT −0,1…−3,6%; stabilitas ≈ Q-MP |
| **Transit-MP / mTransit-MP** (A.7) | Occupancy × normalized link travel time (CV); bus dihitung hanya setelah lewat halte terdekat ($\delta_v$); fallback historis (arrival rate, penetrasi, IQA) jika tak ada CV | $T_0=10$ s, yellow 3 s, lost time 1 s; segmentasi link ≈420 m; ETT free-flow per link; opsional prediksi expected arrival time dengan dwell (Lampiran A) | Passenger delay −31,6% (efek halte) lalu −17,9% lagi; spillover −94% ; bekerja hingga penetrasi 0,1 |
| **MARL TSP event-based** (A.9) | Agen TSP terpisah aktif saat bus masuk zona 800 ft; state posisi/kecepatan bus sel 25 ft; reward bus delay+speed−penalti antrean samping; koordinasi via VDN | Headway bus 15 min; v/c 0,95; dwell dari APC | Bus delay −22% (independen) / −27% (terkoordinasi); side street +≈ kecil, satu gerakan +18% |
| **EVP mixed-criticality** (A.18) | Preempt hanya jika $\Delta=t^{cur}-t^{target}>0$; level purple/red/orange dengan faktor target 1/1,5/2; conflict graph untuk multi-EV; extend jika hijau, ganti jika merah; green reserve dari posisi/kecepatan | Target 8/12/20 menit; VANET DSRC; EV 1% arus | EV 96% memenuhi target; non-EV wait ≈ tanpa preemption; antrean −36% vs absolute preemption |
| **Praktik SCATS** (A.2) | Prioritization (request V2I) vs preemption (mengganti plan); recovery beberapa cycle | — | Gain SCATS robust terhadap prioritization; recovery time membaik |

**Kesimpulan untuk ITCS Jakarta:** gunakan **prioritas kondisional berbasis occupancy** (OCC/Transit-MP) untuk TransJakarta dan bus reguler, bukan preemption absolut; gunakan **preemption bertingkat dengan target waktu** (A.18) untuk ambulans/pemadam; keduanya berjalan di atas pengendali latar (cyclic MP/actuated) dengan constraint keselamatan tetap aktif dan strategi recovery pasca-preemption (A.2).

---

## D. Green Wave / Koordinasi Arteri dan Pemanfaatan Data Connected Vehicle

- **Prinsip klasik (A.8, A.1, A.12):** koordinasi memerlukan **common cycle length** (atau half/double), split, dan **offset** $t_{i,j}=L_{i,j}/v$; MAXBAND/MULTIBAND memaksimalkan bandwidth dua arah via MILP; metrik arterial: platoon ratio/arrival type, green band width (A.1 Lampiran II). Actuated murni merusak green wave (A.8); karena itu A.5 memilih **MP cyclic yang tidak mengubah cycle/offset**.
- **Bukti teoretis (A.11):** pada arteri fluid symmetric, kebijakan greenwave (pergantian serentak dengan offset) adalah unik optimal, dan DDPG menemukannya sendiri — memperkuat bahwa koordinasi arteri layak dijadikan constraint struktural, bukan sesuatu yang harus "dipelajari" ulang tiap hari.
- **Koordinasi + prioritas (A.9):** reward berisi bonus offset arah bus, sehingga TSP tetap konsisten dengan progression.
- **Smoothing-MP / C-MP** (disebut di A.7 sebagai Xu et al. 2024a dan Ahmed et al. 2024a) memperluas MP untuk koordinasi arteri — tidak dibaca langsung, hanya rujukan.
- **Pemanfaatan data probe/CV (A.19):** dengan penetrasi 3–6% dan agregasi 4 minggu, koridor 8 simpang dapat dievaluasi tanpa detektor: delay/travel rate/TTI/SOFT per OD path; cyclic TSD dan empirical PPD mengungkap platoon sekunder dan segmen dengan green kurang; speed heat map memetakan antrean per jam. Prasyarat: cycle length tiap plan diketahui persis. Rujukan A.19 juga menyebut "detector-free optimization of traffic signal offsets with connected vehicle data" (Day et al. 2017) sebagai langkah berikutnya.
- **CV untuk kontrol (A.4, A.6, A.7):** delay/travel time dari probe dapat langsung menjadi pressure; kinerja turun di bawah 20–30% penetrasi, sehingga untuk Jakarta data probe lebih tepat dipakai untuk (a) evaluasi/penalaan offset & TOD plan mingguan, (b) estimasi turning ratio/OD, (c) prioritas transit (bus 100% ter-GPS), sementara kontrol detik-ke-detik tetap dari kamera.
- **GLOSA/eco-driving (A.8):** penghematan bahan bakar hingga 15–20% dilaporkan; dapat disalurkan lewat aplikasi navigasi bila SPaT dipublikasikan — fitur lanjutan, bukan prioritas.

---

## E. Digital Twin: Arsitektur Referensi, Komponen, Data Pipeline, Use-case, Tantangan

**Arsitektur referensi (gabungan A.3, A.17, A.20):**
1. **Data acquisition / Observable Elements:** kamera AI, radar/LiDAR opsional, loop, cuaca, GPS bus/EV, probe komersial; status perangkat (untuk DT pemeliharaan, A.20).
2. **Communication:** MQTT/edge microservices, C-V2X/5G bila ada; NTCIP-kompatibel ke controller (A.2); Secure Message Bus dengan mTLS/RBAC (A.17); intermediary protocol translation (A.20 cross-system entity).
3. **Processing:** fusi & imputasi (JDL, k-means/temporal interpolation, Kalman; A.3), estimasi state (antrean, turn ratio, akumulasi regional), engine simulasi (SUMO via TraCI, co-simulation; atau forecasting ringan Redis+Kalman), AI modules.
4. **Modeling / Digital Twin unit:** model jaringan + phase + antrean, cache historis (A.20), what-if Simulation Agent dan Risk Agent (A.17).
5. **Visualization / User unit:** dashboard web 3D/BIM, mixed reality; fungsi define goals, simulasi, forecasting, reporting (A.20); LLM Explanation Agent di luar loop (A.17).
6. **Action / Governance:** Governance Agent pra-eksekusi, MCP gateway schema-validated, Decision & Event Log (A.17); mode **semi-automated** (operator konfirmasi) vs **fully automated** (closed loop) (A.20).

**Data pipeline:** ingest → cleaning/normalisasi → fusi/imputasi → state estimation → sinkronisasi twin (kontinu) → what-if/forecast → rekomendasi/aksi → log & feedback untuk kalibrasi ulang (feedback loop, A.20).

**Use-case yang disebut:** prediksi antrean/spillover dan penyesuaian preventif; uji timing plan sebelum deploy; deteksi insiden (PCA+DBSCAN dari GPS); VRU safety (fusi sensor mencegah >90% konflik pejalan kaki); training RL di twin (A.3); resiliensi saat lane closure; pemeliharaan prediktif perangkat, condition monitoring, scheduling, compliance reporting (A.20); rerouting saat insiden (A.17).

**Tantangan:** "digital shadow" vs true twin (A.3, A.20); interoperabilitas & standardisasi (ISO 23247, A.20); skalabilitas citywide & komputasi (A.3: lightweight models, mesoscopic downscaling); integritas & keamanan data real-time, cybersecurity; privasi/bias/akuntabilitas (A.3); validasi tanpa data historis untuk kejadian langka (synthetic scenarios); biaya investasi dan pelatihan operator (A.20); latensi komunikasi (A.2).

**Protokol validasi yang direkomendasikan (A.3):** SIL → HIL (algoritma di controller nyata terhubung twin) → **Shadow Mode** (keputusan dicatat, tidak diaktuasi, dibandingkan dengan hasil nyata) → phased live (off-peak, override manusia).

---

## F. Rekomendasi Algoritma Bertingkat untuk ITCS Jakarta + Guard-rail

**Tingkat 0 — Fallback keras (selalu tersedia di controller lokal):** fixed-time TOD plans (Webster/MAXBAND-style, cycle bersama per koridor) yang disusun dari data historis dan diperbarui berkala (A.1, A.10, A.14); aktif otomatis saat komunikasi/kamera gagal (A.2: koneksi/latency adalah kegagalan nyata, sebagaimana dilaporkan agensi). Robustness plan dapat dinilai dengan objektif stabilitas/robustness gaya A.14.

**Tingkat 1 — Actuated/semi-actuated dengan constraint NEMA ring-barrier:** min/max green, gap-out, pedestrian minimum, yellow/all-red; dijalankan di controller (A.16, A.2). Ini state of practice dan baseline yang benar untuk mengukur manfaat tingkat di atasnya.

**Tingkat 2 — Cyclic Max-Pressure terkoordinasi (inti adaptif real-time):** ikuti A.5: cycle & offset tetap per koridor (green wave terjaga), MP hanya mengalokasikan split dengan pressure ternormalisasi kapasitas link, proyeksi QP dengan **min green (≥7 s; sesuaikan aturan pejalan kaki), max green, perubahan ≤5 s/cycle**, integer. Input: antrean/occupancy dari kamera (dan delay dari probe bila tersedia, A.4). Terapkan **hanya di simpang kritis** yang dipilih dengan skor $R_n$ (occupancy, varians, durasi ≥80% kapasitas) — A.5 menunjukkan 20–25% node dapat memberi manfaat setara/lebih dari 100%. Tambahkan **perimeter/gating control** (PI regulator berbasis akumulasi MFD) untuk kawasan CBD saat jenuh — PC+MP menggandakan manfaat pada high demand (7,6% → 15,6%).

**Tingkat 2b — Prioritas transit & darurat di atas Tingkat 2:** OCC-MP/Transit-MP: bobot occupancy bus dari APC/GPS, mobil 1,5, bus di halte tidak dihitung, fallback historis untuk link tanpa observasi (A.6, A.7). EVP bersyarat bertingkat dengan conflict graph dan green reserve dari posisi/kecepatan EV (A.18); recovery ke plan koordinasi setelah preemption (A.2).

**Tingkat 3 — Analitik & penalaan berbasis probe (mingguan/harian):** evaluasi progression dengan cyclic TSD/PPD/SOFT/heat map dari GPS TransJakarta/ojol/aplikasi (A.19); estimasi turn ratio & OD; deteksi insiden; penyesuaian offset/TOD plan.

**Tingkat 4 — Digital twin + RL sebagai advisor/offline:** twin (SUMO/mesoscopic) terkalibrasi untuk what-if, uji plan, dan training RL dengan **demand beragam** (A.16), ring-barrier action space + invalid action masking (A.16), lapisan **critique statistik yang memveto keputusan anomali** (A.15). Deploy RL hanya lewat **shadow mode** (A.3) sebagai rekomendasi ke operator atau sebagai penala parameter Tingkat 2 (misal bobot, setpoint PC), bukan pengendali langsung — konsisten dengan A.1/A.2 (belum ada RL deployed) dan A.13 (MP sudah baseline kuat; gain RL 8–14% throughput di simulasi).

**Guard-rail keselamatan (daftar):**
1. Min green, max green, yellow, all-red, pedestrian walk/clearance dipaksakan di controller, bukan hanya di algoritma (A.2, A.5, A.15).
2. Phase sequence tetap/ring-barrier; larang lompatan phase yang membingungkan pengemudi (A.4, A.5, A.16).
3. Rate-limit perubahan split ≤5 s per cycle dan cycle bersama per koridor (A.5).
4. Watchdog: bila data kamera hilang/stale, degradasi ke actuated → fixed-time; overestimasi antrean lebih aman daripada underestimasi (A.2).
5. Batas prioritas transit: gunakan bobot occupancy, bukan konstanta besar; batasi frekuensi prioritas per cycle agar side street tidak starvation (A.6, A.7 queue-starvation immunity).
6. EVP hanya bila target respons terancam; resolusi konflik multi-EV; recovery terjadwal (A.18, A.2).
7. Perimeter control dengan hysteresis start/stop dan batas minimum 15% saturation flow gerbang (A.5).
8. Setiap perintah ke controller divalidasi skema (MCP-like), dicatat di audit log, dan dapat di-override operator; LLM tidak berada di control loop (A.17).
9. Veto statistik untuk keputusan RL di luar credible interval (A.15); shadow-mode sebelum live (A.3).
10. Metrik keselamatan (AMF/crash review) dan fairness per gerakan (A.16 menunjukkan gerakan volume rendah bisa dikorbankan) dipantau, bukan hanya delay.

---

## G. Kutipan Kunci (singkat)

1. A.1 §II.B.2: "The newer methods that lean on emerging techniques claim better performance than older approaches, but lack cross-evaluation and in-field tests."
2. A.1 §II.A.1: cycle-based controllers "less flexible than the second-based controller but more popular in the industry since drivers know exactly the length of each phase ... more pedestrian-friendly."
3. A.1 §IV.A.4: "the presence of a good prediction model in RHO maybe advantageous to no model as in MFRL approaches, but no-model can be better than an inaccurate model."
4. A.2 Abstract: "However, RL-based signal controllers have never been deployed."
5. A.2 §4.2: "[68] found that moderate queue length overestimation significantly improves the performance of adaptive control."
6. A.2 §7.1: "[10] found in 160 papers on RL-based TSC that only three accounted for non-private vehicle types, and only one accounted for pedestrians."
7. A.3 §8.1: banyak DT "may just fall into what is called a 'digital shadow'"; §8.4: "Shadow Mode Deployment: This is the crucial, and often missing, step."
8. A.4 §6: "One shortcoming of the proposed model is that it activates phases in arbitrary orders with arbitrary durations ... unacceptable for some city engineers."
9. A.5 §5.1: "with only 10% of critical nodes the system travel time improves by 14.5% ... while in the case of controlling all nodes, it improves only by 10.6%."; §6: "single MP shows zero improvement for full network implementation in high demand scenario, while combined MP with PC achieves twice the gain of single PC."
10. A.5 §3.1.1: "we impose a threshold to maximum absolute change of every phase duration between consecutive cycles" (5 s), min green 7 s.
11. A.6 §4.1.1: "the best performance of RB-MP is still worse than the worst performance of OCC-MP."
12. A.7 Abstract: "queue starvation phenomenon: a movement no longer receives the green phase despite the queue spillover" — diatasi mTransit-MP dengan data historis.
13. A.8 §II.B: "Actuated signal control systems are primarily used for isolated intersection control, making Green Wave corridors infeasible."
14. A.9 §5: independent TSP agents "show high instability throughout the training process"; koordinasi memberi −27% vs −22%.
15. A.12 §5.6.5: "a mistrained MARL controller tends to make the traffic network unstable, even cause fatal accidents."
16. A.13 §5.3: "the performance of baseline universal policy methods deteriorates, even falling below that of rule-based approaches" saat skala membesar.
17. A.15 §V.B: "LightGPT fails to outperform traditional and RL-based methods such as MaxPressure, CoLight ..."
18. A.16 Abstract: "A model trained on a single O–D pattern generalizes well to similar unseen demand patterns but degrades under substantially different demand conditions."
19. A.17 §Agentic AI Block: LLM Explanation Agent "is not involved in the control loop, thus preventing non-deterministic actions in safety-critical systems."
20. A.18 §4: "Absolute pre-emption incurs a very high waiting time for non-EVs ... average queue length is reduced up to 36% using EVP algorithm as compared to absolute pre-emption."
21. A.19 §3.1: penetrasi "approximately 3% - 6% of the annual average daily traffic ... mitigated by the aggregation of data across multiple days."
22. A.20 §2.1: "This factor [automatic bidirectional data sharing] distinguishes a digital twin from a digital model (DM) or digital shadow (DS)."

---

## Lampiran: Ringkasan Skor Relevansi

| # | Paper | Skor | Peran dalam ITCS Jakarta |
|---|---|---|---|
| A.1 | Wang/Abdulhai/Sanner 2022 | 5 | Kerangka pemilihan arsitektur & kritik RL |
| A.2 | Chen/Fang/Sadeh 2022 | 5 | Checklist deployment & safety |
| A.3 | Bagabaldo/Hackl 2025 | 5 | Arsitektur DT & shadow-mode |
| A.4 | Liu/Gayah 2022 (D-MP) | 4 | MP berbasis delay/probe |
| A.5 | Tsitsokas et al. 2022 | 5 | Cyclic MP + PC, node selection, constraint |
| A.6 | Ahmed et al. 2024 (OCC-MP) | 5 | TSP kondisional |
| A.7 | Tan et al. 2025 (Transit-MP) | 5 | TSP dengan halte & sparse CV, fallback |
| A.8 | Talluri et al. 2025 | 3 | Kerangka green wave/V2X |
| A.9 | Kwesiga et al. 2024 | 3 | Agen prioritas event-based |
| A.10 | Muresan et al. 2019 | 2 | Historis DRL |
| A.11 | Zhu et al. 2025 | 2 | Teori greenwave optimal |
| A.12 | Guo 2019 | 2 | MARL vs MP, max green guard-rail |
| A.13 | CityLight 2025 | 3 | RL city-scale offline; MP baseline kuat |
| A.14 | AHMOA 2024 | 2 | TOD plan robust offline |
| A.15 | BCT-APLight 2024 | 3 | Veto statistik; LLM tidak kompetitif |
| A.16 | Kwesiga et al. 2026 | 4 | RL ring-barrier, robustness multi-OD |
| A.17 | Jan et al. 2026 | 3/1 | Pola governance agentic; bukti lemah |
| A.18 | Humagain/Sinha 2020 | 4 | EVP bertingkat |
| A.19 | Mahmud/Day 2023 | 5 | Evaluasi koridor dari data probe |
| A.20 | Werbińska-Wojciechowska et al. 2024 | 3 | Kerangka DT O&M ISO 23247 |
