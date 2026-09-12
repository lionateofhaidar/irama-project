# R06 — Transit Signal Priority, Emergency Vehicle Preemption, HCM 6th Edition, dan Konteks ITCS Jakarta

Tanggal: 2026-09-12. Catatan studi terstruktur untuk perancangan aplikasi Intelligent/Integrated Traffic Control System (ITCS) Jakarta (#LANCAR-Jakarta). Bahasa Indonesia dengan istilah teknis Inggris dipertahankan. Semua angka dikutip dari teks sumber yang ada di folder `Bahan Acuan`; bila sumber tidak memuat angka, dinyatakan secara eksplisit.

Sumber yang dibaca (path relatif terhadap `Bahan Acuan\`):
- `_teks_ekstraksi\USDOT_Transit_Signal_Priority_Planning_Implementation_Handbook_2005.txt` (Smith, Hemily, Ivanovic — Gannett Fleming; US DOT/ITS America, Mei 2005; ~10.240 baris teks). Nomor halaman merujuk penanda "Transit Signal Priority Handbook 4 N" dalam teks.
- `_teks_ekstraksi\FHWA_HOP-24-019_Emergency_Vehicle_Preemption.txt` (factsheet EDC-7 NextGen TIM, 2 halaman).
- `_teks_ekstraksi\CED_HCM_6th_Edition_Overview.txt` (Washburn & Washburn, CED course C03-065, 43 halaman).
- `04_Konteks_Jakarta_ITCS\Artikel_*.md` dan `Teks_*.md` (19 file: Antara, Beritajakarta, CNN, Kompas, Metro TV, Transportasi Media, TomTom, Expat Indonesia, Jakarta Globe, Medcom, Tempo, TKDN).
- `_teks_ekstraksi\UMSIDA_Evaluasi_ATCS_Makassar_EN.txt` dan `_ID.txt`; `Papatung_2019_Kebijakan_Transportasi_Jakarta.txt`; `Pubmedia_Sistem_Transportasi_Publik_Smart_City_Jakarta.txt`; `03_Jurnal_Akademis\Teks_jmia_3068.md`; `Teks_itg_konstruksi_2851.md`.
- `05_Website_Acuan_Majalah_RPP\ANALISIS_MAJALAH_RPP_LANCAR-JAKARTA.md` (acuan kebutuhan bisnis; tidak diringkas ulang, dipakai untuk memetakan relevansi).
- Pelengkap yang dipakai secara terbatas untuk mengisi celah: `Permenhub_PM_76_2021_...txt` (Ps. 7, 11, 13, 19–21), `Permenhub_PM_96_2015_...txt` (ambang LOS simpang), `MKJI_1997.txt` (rumus tundaan Langkah E-4), `NTCIP_1202_v02.19_...txt` (objek preempt), `FHWA_HOP-08-024_Traffic_Signal_Timing_Manual_2008.txt` (Bab 9.1 preemption).

---

## 0. Sepuluh Temuan Terpenting (ringkasan eksekutif)

1. **Priority ≠ preemption.** NTCIP 1211/1202 membedakan *priority* (memodifikasi awal/akhir hijau, urutan fase, fase khusus **tanpa** melepas koordinasi) dari *preemption* (mengambil alih kendali normal untuk kereta/kendaraan darurat). Aplikasi ITCS Jakarta harus memodelkan keduanya sebagai dua state machine yang berbeda dengan hierarki override: preempt > priority (Handbook h.4, h.75; STM 2008 §9.1).
2. **Empat komponen TSP** yang harus ada di arsitektur: detection → Priority Request Generator (PRG) → Priority Request Server (PRS)/priority control strategies di controller → TSP system management (konfigurasi, log, laporan) (Handbook h.6, h.59–61).
3. **Strategi aktif yang paling umum dan paling aman untuk koordinasi adalah green extension + early green (red truncation)**; dipakai >40% agensi yang disurvei. Phase insertion/rotation/queue jump hanya untuk kasus geometri khusus (Handbook h.7–8, h.53, Tabel 8).
4. **Parameter operasional dari praktik**: extension/truncation 7–10 s (umum), hingga 20 s (Calgary); satu aktivasi per siklus; lockout pada siklus berikutnya; recovery 1–2 siklus; check-in 100–150 m atau ~15 s upstream; check-out di near-side/stop line (Handbook h.5, h.22, Lampiran A3).
5. **Conditional priority** (hanya bus yang terlambat ≥2 menit — TransLink; atau semua bus yang tidak lebih awal berbasis headway — LADOT, dihitung tiap 6 s) mensyaratkan AVL dan tautan pusat; unconditional cukup dengan controller lokal. Untuk TransJakarta yang berbasis headway, kriteria "headway management" lebih relevan daripada "schedule adherence" (Handbook h.22, h.61, Lampiran A3).
6. **Dampak terukur TSP**: waktu tempuh bus −10% hingga −25%, variabilitas −19% hingga −50%, signal delay bus −40% (dengan retiming); dampak ke jalan minor "tipikal 1 detik per kendaraan per siklus" dan "negligible". Klaim ini selalu dari before–after study yang dirancang (Handbook h.5, h.56–57).
7. **EVP**: rata-rata durasi preempt 25 s; efek ke jalan samping pulih dalam 1 siklus; response time −14 s/d −23% (~70 s); kecelakaan EV −71% (St. Paul); delay per simpang 7 s → 1 s; sistem berbasis AVL/CAD/ATMS (system-based, geofence GPS) lebih murah ~US$8 juta (San Jose) dan bisa memilih rute bebas (FHWA-HOP-24-019 h.1–2).
8. **HCM 6th overview tidak memuat rumus control delay maupun tabel LOS simpang bersinyal**; yang ada: service measure urban street = average travel speed dengan tabel ambang per FFS, aturan LOS F bila d/c > 1, faktor penyesuaian baru (work zone, midsegment blockage, downstream spillback), dan konsep reliability/ATDM. Rumus tundaan Indonesia (MKJI 1997, basis Akçelik 1988) dan ambang LOS PM 96/2015 (A <5 s … F >60 s) tersedia dan berbeda dari HCM.
9. **Konteks Jakarta**: 321 simpang prioritas; ITCS ±65 (2025) → 25 dikontrak 2025 (Rp120 M) → 321 pada 2030; klaim kinerja +20–30%, TomTom 53%→43% (peringkat 30/31 → 90). Angka klaim tidak disertai definisi MOE dan metode; ini celah yang harus diisi modul evaluasi aplikasi. Kritik Instran/MTI/DPRD: akar masalah = 24,35 juta kendaraan; realisasi angkutan umum 22,19% vs target 60% (Perda 5/2014).
10. **Pengalaman ATCS Indonesia** (Makassar, Garut, tinjauan multi-kota): evaluasi memakai MKJI 1997/PKJI 2023 dan PTV Vissim; ATCS menurunkan tundaan tetapi LOS tetap F bila DS ≈ 1,1; kendala tipikal: detektor/peralatan rusak, dana, SDM, disiplin pengguna jalan, hambatan samping. Implikasi: ITCS bukan pengganti TDM; aplikasi harus memiliki modul kesehatan perangkat, pemeliharaan, dan monev berbasis PKJI.

---

## A. TSP Handbook (US DOT, 2005)

### A.1 Identitas dan peta isi

Dokumen: *Transit Signal Priority (TSP): A Planning and Implementation Handbook*, Mei 2005, disusun Harriet R. Smith, Brendon Hemily, Miomir Ivanovic (Gannett Fleming) untuk US DOT (FTA + ITS JPO), dengan kontributor praktisi dari King County, TriMet, LADOT, TransLink, Pace, 3M, PTV, Kittelson, dsb. Merupakan pendamping *An Overview of Transit Signal Priority* (ITS America, 2004). Bertumpu pada 8 studi kasus mendalam (AC Transit Oakland, LADOT/LA Metro, Pace Chicago, Pierce Transit Tacoma, TransLink Vancouver, TriMet Portland, Virginia Route 1, dan satu lagi) dan survei 24–31 agensi.

Struktur (dari Table of Contents):

| Bagian | Bab | Isi |
|---|---|---|
| Executive Summary | vii–xi | Ringkasan, manfaat terukur, 4 komponen, lessons learned |
| **Part I — TSP Planning & Implementation** | 1 Introduction; 2 Background (definisi, benefit/cost, komponen, strategi pasif/aktif/adaptif); 3 Systems Engineering Approach; 4 Project Planning (needs assessment, stakeholders, ConOps & requirements, corridors, technology alternatives, architecture); 5 Project Design; 6 Implementation (procurement, installation, V&V); 7 Operations & Maintenance; 8 Evaluation & building on TSP; 9 Keys to Success | h.3–42 |
| **Part II — State of the Practice** | 10 Survey (39 agensi teridentifikasi, 31 dihubungi, 24 wawancara penuh); 11 Case Studies Summary; 12 Future Directions | h.45–57 |
| **Part III — Technical Support** | 13 System Architecture, Equipment, Software, Communications; 14 Traffic Engineering Terminology & TSP Examples; 15 Simulation & Optimization Tools; 16 Transit Terminology; 17 References | h.59–93 |
| Appendices | A1 Resources; A2 Glossary; A3 Case Study Details (h.100–172); A4 Survey Forms (h.173+) | |

### A.2 Definisi kunci: priority vs preemption

Handbook mengutip NTCIP (h.4):
- **Preemption** (NTCIP 1202 v2): "the transfer of the normal control (operation) of traffic signals to a special signal control mode for the purpose of servicing railroad crossings, emergency vehicle passage, mass transit vehicle passage, and other special tasks, the control of which requires terminating normal traffic control."
- **Priority** (NTCIP 1211): "the preferential treatment of one vehicle class … over another vehicle class at a signalized intersection **without causing the traffic signal controllers to drop from coordinated operations**. Priority may be accomplished by … the beginning and end times of greens on identified phases, the phase sequence, inclusion of special phases, without interrupting the general timing relationship between specific green indications at adjacent intersections."

Terminologi h.75 menyebut preemption sebagai "High" priority (pejalan kaki "don't walk" dituntaskan dulu) dan priority sebagai "Low" priority. Survei menemukan tiga agensi memakai *preemption* (bukan priority) untuk LRT/busway pada ROW eksklusif (Charlotte, Houston Metro, LYNX Orlando) (h.53). Ini penting untuk TransJakarta: koridor busway berjalur khusus secara teknis bisa diperlakukan mendekati preemption, tetapi handbook dan STM 2008 memperingatkan dampak besar preemption terhadap koordinasi dan pejalan kaki.

### A.3 Empat komponen sistem TSP (h.6)

1. **Detection** — menyampaikan data kendaraan (lokasi, ETA, pendekat) ke PRG.
2. **Priority Request Generator/Server** — meminta prioritas ke sistem kendali dan mentriase permintaan ganda.
3. **Priority Control Strategies** — peningkatan perangkat lunak controller yang menyediakan strategi (idealnya lebih fleksibel daripada preemption).
4. **TSP System Management** — konfigurasi, event logging, pelaporan di sisi transit maupun traffic.

Urutan kejadian generik (Figure 1, h.6): bus terdeteksi di titik Pd upstream → PRG memberi tahu sistem kendali → sistem memutuskan berdasarkan kondisi terdefinisi → controller C mengeksekusi (extend green bila sedang hijau; truncate red bila sedang merah) → bus melewati simpang, terdeteksi di Pc (check-out) → controller memulihkan timing normal dengan logika yang ditetapkan.

### A.4 Strategi prioritas dan logikanya

**Passive priority** (h.7): tanpa deteksi; timing plan disusun memperhitungkan dwell time rata-rata, siklus sependek mungkin, progression untuk bus (contoh Denver Transit Mall: cycle length dipilih dari kecepatan bus). Risiko: lalu lintas lain menerima tundaan yang tidak perlu. Termasuk pula "timing to minimize person delay" (bukan vehicle delay).

**Active priority** (h.7–8, h.74–75, h.77–79) — tabel logika, parameter, dan recovery:

| Strategi | Kondisi pemicu | Mekanisme | Parameter waktu (dari sumber) | Recovery / catatan |
|---|---|---|---|---|
| **Green extension** | Bus terdeteksi saat fase bus **hijau**, mendekati akhir hijau | Hijau diperpanjang hingga maksimum yang diizinkan, mengambil "variable green" dari fase berikutnya; fase berikutnya dipendekkan ke "acceptable TSP minimum green" | Contoh Figure 14: penghematan 90 s tundaan (bus tidak menunggu side street + left turn). Praktik: 7–10 s (berubah per simpang), hingga 20 s (Calgary) | Paling efektif karena tidak butuh clearance interval tambahan; tidak merusak koordinasi bila controller "TSP-capable" per NTCIP 1211 |
| **Early green / red truncation** | Bus terdeteksi saat fase bus **merah** | Fase-fase sebelum fase bus dipendekkan (ke minimum green + clearance) agar hijau bus datang lebih awal | Contoh Figure 13 (siklus 120 s): bus mendapat hijau 45 s lebih awal; hijau tetap jatuh di local zero point sehingga koordinasi terjaga. Praktik: hingga 20 s (Calgary) | Dibatasi pedestrian minimum (Walk + FDW; Walk ≥4 s per MUTCD di satu studi kasus); tidak boleh memotong yellow/all-red |
| **Actuated transit phase** | Bus terdeteksi di lajur/lokasi khusus | Fase hanya tampil bila ada bus (mis. lajur belok kiri bus; **queue jump** dengan indikasi khusus/white bar agar bus masuk link hilir mendahului arus) | Tidak diberi angka | Berguna untuk near-side bus bay |
| **Phase insertion** | Bus meminta fase khusus | Fase khusus disisipkan ke urutan normal (mis. leading left-turn-only untuk bus masuk terminal) | Tidak diberi angka | Ottawa: left-turn phase insertion, queue jump di T-intersection |
| **Phase rotation** | Bus belok tiba sebelum hijau through | Urutan fase diputar (lagging left menjadi leading) | Tidak diberi angka | Tetap melayani semua fase |
| **Phase suppression/skipping** | Fase non-kritis tanpa permintaan | Fase dilewati, dengan logika penilaian kemacetan pendekat yang dilewati | — | Beberapa agensi lanjutan memakainya |
| **Window stretching** | — | Fase non-prioritas punya "core time" wajib + "variable time" yang bisa diambil; varian *flexible* bila posisi core tidak tetap | — | Alternatif pengelolaan split |
| **Red interrupt / special phase** | Near-side stop dari bahu | Fase hijau pendek khusus bus disisipkan | — | Untuk queue jump |
| **Compensation/Recovery** | Setelah prioritas diberikan | Fase non-prioritas diberi waktu tambahan; membatasi jumlah siklus berturut-turut yang mendapat prioritas (**lockout** siklus berikutnya) | "Recovery generally takes one or two cycles" (h.22); kebijakan umum: tidak memberi prioritas di simpang yang sama sampai kembali sinkron (h.5) | Beberapa agensi: sinkronisasi tidak pernah putus karena TSP hanya "mencuri" beberapa detik dari hijau jalan minor |

**Adaptive** (h.8–9): dua konsep — *TSP with Adaptive Signal Control Systems* (prioritas diberikan sambil mengoptimalkan kriteria kinerja: person delay, transit delay, vehicle delay; membutuhkan deteksi dini bus dan pembaruan ETA berulang) dan *Adaptive Signal Priority* (menimbang trade-off transit vs traffic secara gradual; komponen: prediksi time-to-arrival akurat, deteksi lalu lintas, algoritme yang mempertimbangkan dampak dan keselamatan pejalan kaki, tautan V2I, PRG/PRS). NCHRP 3-66 menunjukkan adaptive priority bisa dibangun di atas closed-loop system. Handbook menyebut ini "possibly the wave of the future" dan berfokus pada active priority untuk bus mixed traffic.

**Batas yang harus dijaga (contoh requirements h.25):** TSP tidak boleh memendekkan minimum/clearance interval, tidak boleh melewati fase (dalam profil konservatif), tidak boleh memutus koordinasi; harus ada *transition back to coordination*, *override by emergency vehicle call*, *reservice-inhibit timer*, *delay timer* pada input TPR, *locking detection* dengan pelepasan setelah fase prioritas dilayani, ≥4 alternate split plans per input, semuanya dapat diprogram time-of-day.

**Faktor pembatas besarnya prioritas (h.23):** cycle length, kompleksitas fase, arus jalan minor, perlindungan waktu pejalan kaki, akurasi check-out. Handbook menekankan agar jumlah detik prioritas yang disepakati **ditulis dalam MoU/Interagency Agreement** karena "in some jurisdictions, the seconds of priority granted (mysteriously) diminish over time."

### A.5 Teknologi deteksi dan komunikasi (h.66–69)

| Teknologi | Cara kerja | Kelebihan | Keterbatasan |
|---|---|---|---|
| **Hard-wired loop + transponder** | Transponder di bawah kendaraan dibaca loop di perkerasan; ID unik (AVI) | Kompatibel loop standar; tidak butuh line-of-sight; check-out mudah (tambah loop hilir) | Loop rentan rusak (pavement flexing, resurfacing) |
| **Light-based (infrared/optical strobe)** | Emitter IR di atap depan bus → detektor di mast arm → *phase selector* di cabinet; ID kendaraan bisa disandikan | Paling luas dipakai di AS karena sudah ada untuk EVP (satu sistem untuk EVP+TSP); teruji | Butuh line-of-sight; terganggu geometri, cuaca, dedaunan; pantulan bisa memicu deteksi palsu di simpang tetangga |
| **Sound-based (siren detector / digital sound wave)** | Mikrofon direksional mendeteksi sirene (yelp/wail/hi-lo); versi digital memakai generator suara non-audible di bus | EV tidak perlu alat tambahan; lintas yurisdiksi; tanpa line-of-sight | Tidak praktis untuk TSP (butuh sirene); alarm palsu; tanpa ID/log |
| **Radio-based (RF tag / spread spectrum)** | RF transponder di kendaraan + tag reader upstream (RS-232 ke controller); varian antena+receiver dengan log ID, priority level, arah, waktu, durasi | Tanpa line-of-sight; log lengkap | Butuh lokasi curbside, daya, komunikasi; lisensi FCC; non-directional (harus kirim arah) |
| **GPS/AVL-based** | Unit on-board (GPS AVL) mengirim pesan prioritas berisi schedule deviation, passenger load, dll. ke field unit di controller; atau transceiver mengirim lokasi/kecepatan/heading saat masuk jangkauan | Tanpa line-of-sight; bisa memberi tahu saat bus sudah lewat (check-out); mendukung conditional | **Polling rate AVL** mungkin tidak cukup untuk simpang rapat atau check-in/out dekat halte; urban canyon |

Prinsip desain (h.66): pemilihan detektor harus **paralel dengan pemilihan perangkat lunak TSP**; "inappropriate application of a detection system can be a fatal flaw"; harus bisa menentukan **kapan bus telah melewati simpang** agar extension dihentikan sedini mungkin. Survei (h.50–51): optical dominan karena warisan EVP; NEMA controller >40%. Validasi jarak deteksi dan akurasi optical/RF "required careful attention and/or attenuation" (h.36).

Komunikasi (h.69): dua jenis — (1) kendaraan↔controller lokal (bagian dari sistem deteksi), (2) simpang↔pusat (fiber/tembaga/nirkabel) yang dibutuhkan untuk TSP terpusat, conditional priority, dan pengarsipan data.

### A.6 Arsitektur bus–roadside–central (h.59–62)

Tiga sistem utama: **PRG**, **sistem komunikasi**, **PRS** (biasanya di dalam sistem kendali sinyal). NTCIP 1211 mendefinisikan skenario berdasarkan lokasi PRG (Figure 6):
- PRG-4: di kendaraan, langsung ke PRS controller (paling umum);
- PRG-5: wayside detection oleh sistem sinyal lokal;
- PRG-1/2/3: di transit management center dan/atau traffic management center berbasis pengetahuan lokasi kendaraan (AVL), diteruskan center-to-center lalu center-to-intersection.

Sistem kendali sinyal bertanggung jawab mengeksekusi, membatasi (mis. **satu aktivasi per siklus**: permintaan kedua diabaikan), dan memastikan **permintaan berprioritas lebih tinggi (emergency/railroad preemption) meng-override** yang lain. Standar: NTCIP 1211 (object definitions for signal control and prioritization) dan APTA TCIP di sisi transit. Handbook mencatat banyak komponen masih proprietary.

Perangkat keras/lunak (h.62–66): electromechanical, NEMA, Type 170, ATC/2070; perangkat lunak NEMA vendor (Eagle/Siemens, Econolite, Peek, dll.) menyediakan green extension/early green; perangkat lunak 170/2070 (BI Tran 233, NextPhase, VS-Plus, Wapiti W4iks) menyediakan fitur lebih kaya termasuk phase insertion/rotation, queue jump, dan **conditional priority**. LADOT memakai sistem terpusat yang memantau bus dan menghitung headway.

### A.7 Kebijakan conditional priority (late bus, headway)

- **Definisi (h.61):** conditional = prioritas hanya bagi kendaraan yang memenuhi kriteria (terlambat, on route, dsb.). "No system is strictly unconditional" karena selalu ada batasan (mis. tiga bus di tiga siklus berturut-turut tidak semuanya dilayani).
- **Kapan memilih (h.22, h.61):** bila tujuan = **reliability** (variabilitas termasuk bus "hot"/lebih awal) → conditional berbasis schedule adherence **atau headway interval**; membutuhkan AVL (Portland, Vancouver) atau sistem kendali pusat canggih (Los Angeles) dan menaikkan kebutuhan komunikasi. Bila tujuan = **travel time** (layanan sangat sering/express) → unconditional dengan kriteria sisi lalu lintas saja (recovery), lebih agresif, tanpa AVL, lebih murah.
- **Ambang praktik (Lampiran A3):** TransLink 98 B-Line — prioritas untuk bus **≥2 menit terlambat**; master unit membedakan **4 tingkat keterlambatan** dan meneruskan permintaan bus paling terlambat saat konflik. LADOT — prioritas untuk **semua bus yang tidak lebih awal** berbasis perbandingan headway, resolusi menit, dihitung **setiap 6 detik**; bus non-revenue tidak diberi prioritas. Calgary/LRT: GPS + peta rute + jadwal; hanya menghubungi sinyal bila terlambat "several minutes"; LRT memakai predictive priority (green band). Definisi on-time (h.89): tidak lebih awal dari **x = 0 menit** dan tidak lebih lambat dari **y = 3 (atau 5) menit** — nilai yang "very common".
- **Headway management (h.89):** untuk layanan berbasis headway, tindakan korektif termasuk menahan unit di belakang *bunch* meski mengorbankan ketepatan jadwal — relevan langsung bagi TransJakarta.
- **Elemen ConOps terkait (h.23):** centralized vs distributed; integrasi EMS; conditionality (yes/no) dan basisnya (jenis layanan, schedule adherence, headway); pilihan strategi; parameter per simpang (extension time, truncation time, insertion points, aturan koridor bersilangan, level "low priority" bertingkat); detection distance; check-in/check-out; handling of coordination; windows in cycles (frekuensi dan durasi); recovery (lockout); jurisdictional rules; data to be collected.

### A.8 Dampak terukur

| Lokasi | Dampak pada bus | Dampak pada lalu lintas umum | Sumber |
|---|---|---|---|
| Tacoma (Pierce Transit), 6 koridor, 110–245 simpang | TSP + optimasi sinyal: transit signal delay −40%; total signal delay S.19th −5–30% (transit) | GP −18–70% (S.19th), −30–65% (Pacific Ave) berkat koordinasi ulang; manfaat ekonomi US$14,2 juta/tahun untuk 6 koridor | h.viii, h.57 |
| Portland (TriMet), 8 koridor, 250–650 simpang | Travel time −10%, variabilitas hingga −19%; menghindari penambahan 1 bus (Line 4, Nov 2000); scheduled recovery time dikurangi | "Very little" | h.viii, h.57 |
| Chicago (Pace) | Running time −15% (3 menit), rentang 7–20% menurut waktu; hemat 1 bus weekday | Studi dampak: kecil, tanpa keluhan ke IDOT | h.viii, h.56 |
| Los Angeles (LADOT/Metro Rapid) | Travel time −19–25% (1/3 dari TSP, 2/3 dari headway-based service, halte lebih jarang, dwell lebih pendek); ridership +4–40%, 1/3 penumpang baru | "Typically one second delay per vehicle per cycle" | h.viii, h.56 |
| Vancouver (TransLink 98 B-Line, 59+4 simpang) | Travel time koridor 100 → 84 menit; variabilitas −40–50%; modal shift 23% auto → transit; net benefit CD$2,9 juta | "No noticeable impact" | h.57 |
| Oakland (AC Transit, 8 simpang Caltrans) | ~9% time savings (ekstrapolasi) | "Infinitesimal" | h.56 |
| Umum | Penghematan waktu tempuh bus "on the order of 15%" tergantung signal delay awal | "Extremely small or imperceptible"; "all stated that the non-priority street impact was negligible" | h.5, h.x |

Biaya (h.56–57): AC Transit US$25 ribu (transmitter) + ~US$300 ribu (komponen TSP); LA US$10 juta; Pace US$732 ribu; Tacoma US$2,7 juta; TransLink CD$1,3 juta; TriMet US$5,8 juta; Virginia Route 1 US$220 ribu untuk 25 simpang + 12 bus. Pemeliharaan umumnya "insignificant" (US$1 ribu/simpang/tahun di LA; 0,2 FTE untuk 650 bus di TriMet).

### A.9 Langkah perencanaan dan evaluasi (systems engineering)

Lima langkah (h.9): **Planning → Design → Implementation → Operations & Maintenance → Evaluation, Verification, Validation and Building on TSP** (wajib untuk proyek ITS berdana federal AS).

**Planning (Bab 4):** needs assessment (mengapa TSP: signal delay bus, data transit & lalu lintas, biaya awal, business case); stakeholder (identifikasi, pengelolaan, project management); ConOps + requirements (goals → MOE → ConOps → requirements); pemilihan koridor/simpang; alternatif teknologi & arsitektur. Pertanyaan kunci sejak awal: apakah **EMS preemption** sudah/akan ada, karena memengaruhi tujuan, stakeholder, teknologi, dan desain (h.12); kesesuaian dengan **regional ITS architecture** dan standar NTCIP/TCIP.

**MOE yang dipakai agensi (h.22, h.38):** reduced bus travel time; reduced stop & signal delay; reduced variability/schedule adherence; reduced recovery time at end of run; fuel savings; air quality; reduced operating resources; number of signal cycles to clear a queue before/after TSP; reduced mainline queue; minimal delay to other vehicles; reduced accidents dan decreased EV travel time (preemption); public response.

**Design (Bab 5):** inventaris sistem kendali (turn movements & volumes, LOS, delays/queues) dan data bus ("before" dwell/travel time, variabilitas per waktu, layover/recovery, ons/offs, transfer, pejalan kaki); desain pusat & komunikasi; desain per simpang (labor-intensive); on-board; **optimasi dan penyiapan timing plan setelah instalasi TSP**; mikrosimulasi untuk kasus khusus; **kebijakan far-side stop** (menyederhanakan perhitungan extension, check-out lebih akurat, mengurangi lockout bus berikutnya) (h.29); integrasi dengan EMS preemption: legacy system, EMS mana yang diberi prioritas, resolusi konflik antar level, upgrade kendaraan EMS (h.31).

**Implementation (Bab 6):** procurement (bid vs RFP, libatkan bagian pengadaan sejak awal); instalasi bus & lapangan; pelatihan; komunikasi internal (termasuk **scheduling department** agar penghematan tidak hilang sebagai layover); publikasi; **verification & validation** (uji alat, uji sistem, validasi jarak/akurasi deteksi).

**O&M (Bab 7):** pemantauan kinerja berkelanjutan (saat ini "haphazard": pengemudi melapor bila sinyal tidak merespons — perlu mekanisme lebih baik); perjanjian tertulis siapa memelihara apa (transit: on-board; traffic: lapangan) dan spare parts.

**Evaluation (Bab 8):** before–after study (bisa "simulasi before" dengan mematikan TSP sebentar; satu situs mengumpulkan data setengah waktu TSP on dan setengah TSP off untuk mengendalikan variabilitas cuaca/pengemudi/musim); evaluasi bertahap: sebelum → setelah optimasi umum pra-TSP → setelah TSP + optimasi pasca-TSP; **ongoing data collection dari AVL** (travel time & variabilitas per waktu/hari/musim, schedule adherence, layover/recovery) untuk menilai efektivitas strategi, pengaruh kondisi, dwell time, perilaku pengemudi; **fine-tuning** iteratif antara penyesuaian jadwal kecil dan setelan TSP; log LADOT mencatat setiap permintaan: diminta/diberikan, kapan mulai, berapa lama, jenis, lama lockout, waktu recovery, serta kegagalan detektor (Lampiran A3).

**Simulasi (Bab 15):** model harus mampu mensimulasikan green extension/red truncation (dan idealnya phase rotation/insertion/skipping), dwell time per halte, headway; multiple runs dengan random seed (satu run "almost always misleading"); warm-up ≈ waktu tempuh rute terpanjang; MOE: queue, delay, travel time, volume, speed variation; pilih jumlah run dari varians dan confidence interval.

### A.10 Checklist implementasi (disarikan dari Keys to Success h.41–42, lessons learned h.x, dan Bab 4–8)

1. Libatkan stakeholder sejak hari pertama (traffic + transit + EMS + pengadaan + scheduling).
2. Tunjuk *champion* di tiap instansi; jaga momentum.
3. Mulai dengan **demonstrasi/pilot** untuk menguji teknis, mengukur manfaat, dan membangun kepercayaan traffic engineer.
4. Tetapkan tujuan sederhana (travel time atau reliability) → MOE → ConOps → requirements.
5. Putuskan conditional vs unconditional dan basisnya (schedule vs headway) sesuai ketersediaan AVL.
6. Tetapkan strategi (mulai dari green extension + early green) dan parameter per simpang; **tuliskan detik prioritas dalam MoU**.
7. Pilih deteksi bersamaan dengan perangkat lunak; pastikan check-out; validasi jarak deteksi di lapangan.
8. Pertimbangkan far-side stop; optimalkan timing plan sebelum dan sesudah TSP.
9. Integrasikan/harmonisasikan dengan EMS preemption (hierarki override).
10. Standarkan peralatan controller lintas yurisdiksi.
11. Lakukan before–after study yang kredibel dalam bahasa traffic engineering setempat.
12. Bangun pengumpulan data berkelanjutan (log permintaan, AVL) dan proses fine-tuning + revisi jadwal bertahap.
13. Perjanjian pemeliharaan tertulis dan pelatihan teknisi/pengemudi.
14. "Keep it simple, build incrementally."

---

## B. Emergency Vehicle Preemption (EVP)

### B.1 Cara kerja dan teknologi (FHWA-HOP-24-019)

EVP mengubah indikasi sinyal menjadi hijau bagi kendaraan darurat yang mendekat "while promptly displaying a red signal to drivers who may cross the emergency vehicle's path." Dua pendekatan:
- **Vehicle-based**: transmitter di kendaraan ↔ receiver di tiap simpang (visual/optical, audible/siren, wireless); controller lokal mem-preempt timing plan. Masih luas dipakai.
- **System-based**: memanfaatkan **AVL + CAD (computer-aided dispatch) + ATMS terpusat**; tanpa perangkat khusus di lapangan. CAD memberi tahu ATMS saat unit ditugaskan ke panggilan prioritas tinggi dan rute yang disarankan; AVL memberi lokasi real-time; permintaan dikirim ke sinyal via pusat. **Geofence GPS** di sekitar simpang mendeteksi kedatangan; kecepatan dan jarak real-time menentukan pemicu dan durasi preempt. Keunggulan: kendaraan bebas memilih rute, mudah diskalakan ke seluruh jaringan, lebih murah, lebih andal, lebih mudah dikelola; koordinasi lintas yurisdiksi dimungkinkan pada keduanya.

Teknologi deteksi yang dirinci Handbook TSP (h.67–69): optical/IR strobe (3M Opticom — juga dipasang Calgary Fire), siren detector, RF, loop transponder, GPS. STM 2008 §9.1.1 menambahkan **push button** dan mencatat banyak kota membatasi preemption hanya untuk pemadam kebakaran karena polisi/ambulans dianggap cukup lincah dengan sirene (mengurangi gangguan koordinasi).

### B.2 Urutan preempt dan recovery ke koordinasi

Factsheet FHWA tidak merinci urutan; detail berikut dari NTCIP 1202 v02.19 (objek `preemptEntry`) dan STM 2008 §9.1.2:
- **Entry/delay**: `preemptDelay` (waktu tunda sebelum preempt aktif; *non-locking memory* bila input hilang sebelum delay habis, preempt tidak terjadi), `preemptMinDuration`, `preemptMinGreen`, `preemptMinWalk`, `preemptEnterPedClear` — fase aktif harus menuntaskan minimum green/walk/ped clear sebelum dilepas; **yellow dan all-red tidak boleh dipendekkan** (MUTCD via STM 2008), sedangkan walk/ped clearance **boleh** dipendekkan/dihilangkan untuk preemption (tidak untuk priority).
- **Track clearance**: `preemptTrackPhase` + `preemptTrackGreen` — fase hijau untuk mengosongkan area konflik (asal untuk rel; pada EVP jalan dapat dipakai untuk mengosongkan antrean di pendekat EV).
- **Dwell**: `preemptDwellPhase` + `preemptDwellGreen` — fase hijau yang ditahan selama kendaraan darurat hadir; opsi *flash dwell* (fase dwell kedip kuning, lainnya merah); `preemptMaxPresence`.
- **Exit**: `preemptExitPhase` — fase yang dilayani saat keluar; transisi keluar tidak boleh memendekkan yellow/all-red pendekat yang dipreempt dan tidak boleh langsung kuning → hijau.
- **Prioritas antar preempt**: nomor lebih kecil meng-override nomor lebih besar (`preemptControl` bit 2); `preemptLink` untuk merangkai preempt.
- **Recovery/transition**: STM 2008 mencatat pada sistem terkoordinasi di Washington DC, pemulihan ke koordinasi dasar memakan **30 detik hingga 7 menit**; sinyal biasanya bersiklus beberapa kali sebelum kembali ke split/offset normal, yang menambah tundaan terutama pada jam puncak. Perlu metode transisi (dibahas di STM Bab 6) untuk meminimalkan dampak. Handbook TSP h.31 dan h.25: TSP harus menyediakan override oleh EV call dan transisi kembali yang mempertahankan koordinasi.

### B.3 Dampak dan isu keselamatan

- St. Paul, MN: **−71% kecelakaan kendaraan darurat** setelah EVP (studi 1977).
- Virginia Tech: **durasi preempt rata-rata 25 detik**; efek pada jalan samping umumnya pulih **dalam satu siklus**.
- Denver: response time **−14% s/d −23% (rata-rata 70 detik)** di 6 simpang.
- Plano, TX: 7 kecelakaan di simpang bersinyal (1981–83) → hanya 4 dalam >20 tahun setelah EVP.
- Delay rata-rata per simpang sebelum EVP 7 detik → 1 detik (Central EVP, 2023).
- San Jose: sistem terpusat ~**US$8 juta lebih murah** daripada alternatif hardware-based untuk simpang lebih sedikit.
- Kunci program: perencanaan terkoordinasi traffic + public safety, kebijakan, pelatihan pengguna, **performance management & reporting** (memantau aktivasi, mengkuantifikasi manfaat, menjustifikasi program).
- Isu keselamatan (STM 2008 §9.1.3): pemendekan walk/FDW harus seminimal mungkin; *preempt confirmatory lights* yang tidak jelas dapat membuat EV salah mengira sudah mendapat kendali; konflik preempt rel vs EV; interoperabilitas multi-vendor; *preempt trap* bila track clearance kurang.
- Handbook TSP (h.57, Virginia Route 1): "Additional delay caused by EMS pre-emption is small"; manfaat tambahan "emergency responder confidence".

---

## C. HCM 6th Edition Overview (CED C03-065)

### C.1 Isi overview

HCM 6th (TRB, 2016) berjudul *A Guide for Multimodal Mobility Analysis*; 4 volume (Concepts; Uninterrupted Flow; Interrupted Flow; Volume 4 online Applications Guide, gratis di hcmvolume4.org). Empat dimensi: quantity of travel, quality of travel, accessibility, capacity. Tambahan besar: travel time reliability (freeway Ch.11, urban street Ch.17), managed lanes, work zones, alternative intersections (DDI, RCUT, MUT, DLT) dengan service measure baru **experienced travel time (ETT)** = jumlah control delay + waktu tempuh jarak ekstra, dan ATDM (Ch.37). Setiap bab metodologi kini memuat tabel kebutuhan data, sumber data, nilai default, sensitivitas; example results; versi bab bernomor (mulai 6.0).

### C.2 Ukuran kinerja yang relevan untuk simpang bersinyal dan jalan perkotaan

- **Signalized Intersections (Ch.19/31):** overview hanya menyebut perubahan: faktor penyesuaian arus jenuh untuk heavy vehicle dan grade digabung; tundaan gerakan tak bersinyal di simpang bersinyal kini dimasukkan ke approach/intersection delay (input pengguna); faktor arus jenuh baru untuk **work zone**, **midsegment lane blockage**, **downstream spillback**; Ch.31 memuat metode perencanaan yang disederhanakan. **Overview tidak memuat rumus control delay (komponen d1 uniform delay, d2 incremental delay, d3 initial-queue delay) maupun tabel ambang LOS simpang bersinyal (10/20/35/55/80 s/veh).** Nilai-nilai tersebut adalah pengetahuan umum HCM yang harus diverifikasi ke teks HCM Ch.19 sebelum dipakai di aplikasi; tidak dikutip di sini sebagai angka sumber.
- **Urban Street Facilities/Segments (Ch.16/18):** service measure diubah menjadi **average travel speed** (bukan % FFS). **LOS F juga berlaku bila d/c > 1,0.** Tabel 1 (ambang kecepatan, mi/h, menurut base FFS 55/50/45/40/35/30/25): LOS A >44/40/36/32/28/24/20; B >37/34/30/27/23/20/17; C >28/25/23/20/18/15/13; D >22/20/18/16/14/12/10; E >17/15/14/12/11/9/8; F ≤ nilai E. Ambang A/B segmen ≈ 80% FFS. Tambahan: prediksi **queue spillback time**, faktor parkir, segmen dengan roundabout, RTOR dalam volume balancing, pedestrian/bicycle LOS dibobot travel time, default akselerasi/deselerasi bus.
- **Reliability & ATDM (Ch.17/37):** metode urban street reliability menjalankan metode Ch.16 berulang untuk skenario permintaan, cuaca, insiden, work zone, special event selama hingga setahun → distribusi travel time; praktis hanya lewat perangkat lunak. Konsep ini adalah dasar KPI keandalan (mis. planning time index) untuk dashboard.
- **Multimodal:** HCM mencakup auto, truck, pedestrian, bicycle, bus; pedestrian & bicycle LOS score; transit dibahas sebagai bagian urban street (default nilai bus).

### C.3 Perbedaan dengan MKJI 1997 / PKJI 2023 / PM 96/2015 (dari sumber di folder)

| Aspek | HCM 6th (overview) | MKJI 1997 / PKJI 2023 / PM 96/2015 |
|---|---|---|
| Ukuran kinerja simpang bersinyal | Control delay (rumus tidak di overview) | MKJI Langkah E-4: **D_j = DT_j + DG_j**; DT = c × 0,5(1−GR)² / (1−GR×DS) + NQ1 × 3600 / C (basis Akçelik 1988); tundaan geometrik default 6 det/smp; ditambah NQ (antrian N1+N2), panjang antrian QL, rasio kendaraan terhenti NS |
| Ambang LOS simpang | Tidak ada di overview (perlu HCM Ch.19) | PM 96/2015 Lampiran: **A <5 s; B 5–15 s; C 15–25 s; D 25–40 s; E 40–60 s; F >60 s per kendaraan**; arteri/kolektor primer minimal LOS B |
| Ukuran kinerja ruas | Average travel speed vs FFS; d/c>1 → F | PKJI 2023: derajat kejenuhan **DJ** (batas desain **0,85**), kecepatan tempuh vT, waktu tempuh wT; tundaan T, panjang antrian PA, rasio kendaraan henti RKH |
| Satuan kendaraan | pc (passenger car), PCE truk SUT/TT | smp (satuan mobil penumpang), ekr; komposisi sepeda motor tinggi diperhitungkan |
| Reliability | Ada (Ch.11, 17) | Tidak ada |
| Multimodal | Ya | Terbatas |

Catatan: studi Indonesia yang ditinjau (Makassar, Garut) memakai MKJI 1997/PKJI 2023 dan ambang LOS yang konsisten dengan PM 96/2015; aplikasi ITCS Jakarta sebaiknya menghitung KPI dalam kerangka PKJI/PM 96 (untuk kepatuhan regulasi dan komparabilitas dengan studi lokal) **dan** dapat menampilkan padanan HCM untuk benchmark internasional.

---

## D. Konteks Jakarta (sintesis kronologis)

### D.1 Kronologi

| Waktu | Peristiwa / data | Sumber |
|---|---|---|
| 2004 | TransJakarta (BRT) mulai beroperasi | Papatung 2019 |
| 2007–2014 | Pergub 103/2007 Pola Transportasi Makro; **Perda DKI 5/2014 tentang Transportasi**: target **60% perjalanan dengan angkutan umum**, kecepatan rata-rata jaringan **35 km/jam** | Papatung 2019 |
| 2013–2015 | 16,07 juta kendaraan (2013); 25,7 juta perjalanan/hari (2015: 18,8 juta DKI + 6,9 juta Bodetabek), diperkirakan 98% kendaraan pribadi | Papatung 2019 (mengutip Dishub) |
| 2017–2021 | TomTom: 2017 61% (#4 dunia); 2018 53% (#7); 2019 53%; 2020 36% (#31); 2021 34% (#46). 2021: Sustainable Transport Award pertama di Asia Tenggara | Pubmedia 2025 |
| 2023 | Uji coba ITCS di **20 simpang**; klaim melancarkan **15–20%** per titik; dipantau dari NOC ITS Traffic Light | Kompas 4/7/2025 (mengutip Kompas 4/7/2023) |
| 2023 (tanggal tidak tercantum) | PT TKDN uji coba ITCS 3 bulan di Solo (Simpang Tugu Wisnu Manahan, Simpang Sumber Girimulyo); VV&E oleh ITS Indonesia; fitur VIP Green Wave, Bus Priority, Actuated (Full Reaction), Self Adaptive, Coordinated Green Wave; AI Digital Twin 3D Gen-5, AI Predictive Modelling; kamera IR | Antara 3635259; Tempo |
| 2024 | IMD Smart City Index 2024: Jakarta #103/142 | Pubmedia |
| 9 Des 2024 | Janji Pramono Anung–Rano Karno atasi kemacetan (detikOto) | RPP h.7 |
| Jan 2025 | TomTom Traffic Index 2024 rilis: Jakarta **#90, tingkat kemacetan 43%** (turun dari 53%, #30/31 pada 2023); 10 km = 25 menit 31 detik; 108 jam hilang/tahun; Bandung 32 menit 37 detik (terburuk di Indonesia) | Antara 5050989; Beritajakarta 145079; Jakarta Globe |
| 11 Jun 2025 | Gubernur meninjau ITCS 65 simpang di UP SPLL (Gedung Dinas Teknis Abdul Muis): "sistemnya sudah cukup baik, hanya masih kurang"; **25 petugas/shift**; **call center terkoneksi CRM, SLA maks 3 jam** | Beritajakarta 145079 |
| 12 Jun 2025 | Dishub: Recognition System (jenis kendaraan, pelat, pelanggaran) dan Predictive System (prediksi volume, hitung waktu hijau maksimum optimal); dasar **PM 76/2021** | Transportasi Media |
| 2–3 Jul 2025 | Seminar RPP PKN II: Rp **120 M** APBD 2025 untuk **25 simpang**; 3 tahap (0–2 bln MoU + 5 simpang; 6–12 bln ETLE/pajak/emisi; >12 bln 321 simpang + KRE + PL2SE); perimeter dalam/luar; target top-50 kota global 2029 | Beritajakarta 145625; CNN; Metro; Kompas |
| Jul 2025 | Podcast "Rabu Belajar": prioritas hijau untuk pemadam/ambulans lalu kembali ke pengaturan berdasarkan panjang antrean; distribusi hijau proporsional volume; ANPR → DLH; ETLE bersama Ditlantas PMJ; target semua simpang ITCS **2030** | Antara 5050989, 5051249, 5051493 |
| 10 Des 2025 | Forum Beritasatu: Pramono mengaitkan perbaikan dengan subsidi TJ (Rp3.500), ASN wajib angkutan umum tiap Rabu, ridership TJ >1 juta/hari | Jakarta Globe |

Catatan konsistensi: peringkat 2023 disebut "30" (Beritajakarta, Transportasi Media) dan "31" (Antara mengutip Syafrin). Pubmedia menyebut 2020 = 36% #31 sedangkan Syafrin menyebut 2023 = 53% #31; keduanya dikutip apa adanya, tidak direkonsiliasi di sini. Halaman TomTom yang diarsipkan hanya berisi teks umum tanpa angka Jakarta. Judul Antara "Rano sebut ITCS turunkan waktu tunggu kendaraan 15 persen" hanya tersedia sebagai tautan, isinya tidak dibaca.

### D.2 Fitur ITCS Dishub yang diklaim (gabungan pemberitaan dan RPP)

- Kendali: **Actuated (Full Reaction)** — memberi info ke controller bila simpang padat/perlu hijau lebih panjang; **Self Adaptive** — info real-time agar simpang lebih padat dapat hijau lebih lama atau mempercepat merah di simpang lain; **Coordinated Green Wave** antar simpang; **VIP Green Wave** — kendaraan tertentu (darurat, VVIP) mendapat hijau berurutan di simpang yang dilewati; **Bus Priority** — deteksi bus via pelat nomor/jenis kendaraan, dapat menangani lebih dari satu bus bersamaan (Tempo).
- AI: **Recognition** (jenis kendaraan, pelat, pelanggaran seperti belok terlarang/lajur terlarang) dan **Predictive** (prediksi volume, waktu hijau maksimum optimal; AI Predictive Modelling dari data historis: waktu, cuaca, hari libur, acara; digital twin 3D).
- Logika yang dijelaskan Kadishub: sistem memprediksi dan menghitung total kebutuhan hijau secara real time, lalu mendistribusikan "secara normal" — kaki bervolume tinggi mendapat hijau lebih panjang; setelah kendaraan prioritas lewat, pengaturan kembali berdasarkan panjang antrean.
- Arsitektur per simpang (RPP h.9): 4 kamera Viero + 1 fisheye + 4 ANPR; junction box dengan PoE/industrial switch, Viero AI Processor, antarmuka RS232 ke traffic light controller; Metro-E/fiber ke pusat (server traffic, analytic, VMS, storage, video wall).
- Halaman produk TKDN "APILL Generation 5" dan "ITCS in the Era of EV" dalam arsip hanya berisi teks navigasi (konten tidak terambil).

### D.3 Organisasi TMC dan layanan

UP Sistem Pengendalian Lalu Lintas (UP SPLL) Dishub DKI, Jl. Abdul Muis; ±25 operator per shift (Expat Indonesia menyebut "50-person monitoring team"); call center terhubung CRM (platform layanan pelanggan Jakarta) dengan SOP penyelesaian keluhan maksimum 3 jam. Menurut PM 76/2021 Ps.21, penyelenggaraan ITS harus didukung **unit kerja pengelola** dan **SDM berkompetensi** yang ditetapkan Menteri; Ps.7(3) mensyaratkan seluruh peralatan terhubung ke ruang kendali dan dapat diubah setelannya dari ruang kendali; Ps.7(4) menyebut layanan prioritas untuk angkutan umum massal, ambulans, pemadam, pejabat negara/tamu negara, penindakan pelanggaran, deteksi kerusakan peralatan dari ruang kendali, rekaman data operasional dan historis.

### D.4 Integrasi ETLE / DLH / Bapenda / Tol

- **Ditlantas Polda Metro Jaya**: kamera ANPR ITCS diintegrasikan ke ETLE; MoU untuk data pelanggaran.
- **Bapenda + Ditlantas PMJ**: data penindakan kendaraan belum bayar pajak (klaim: mendorong PAD).
- **DLH**: ANPR menangkap pelat → dicocokkan dengan data uji emisi → menentukan ruas target operasi (ruas dengan pelanggaran tertinggi); klaim perbaikan udara karena stop-and-go berkurang.
- **PT Jasa Marga, PT Hutama Karya**: sosialisasi pemanfaatan data ITCS.
- Jangka panjang: **KRE** (Kawasan Rendah Emisi) dan **PL2SE/ERP**.

### D.5 Vendor dan teknologi

PT Teknologi Karya Digital Nusa Tbk (TKDN): ITCS dengan "AI Digital Twin 3D Generasi ke-5" dan "AI Predictive Modelling"; sertifikasi VV&E ITS Indonesia; kamera deteksi per kaki simpang dengan IR light; kamera "Viero" muncul di diagram RPP. Tidak ada dokumen teknis vendor (spesifikasi, protokol) dalam arsip; TKDN adalah perusahaan publik dan berita bersumber rilis pers, sehingga klaim kinerja Solo ("hasil positif") tidak terkuantifikasi.

### D.6 Kritik dan risiko pemangku kepentingan

- **Instran** (Budi Susandi): kendaraan bermotor naik 5× dalam 22 tahun — 4,51 juta (2002) → **24,35 juta (2024)**: 4,35 juta mobil, 19,01 juta motor, 44.352 bus, 876.637 angkutan barang, 64.611 kendaraan khusus; solusi = kendalikan kendaraan pribadi (TDM: parkir mahal, hapus subsidi BBM pribadi, kepemilikan bersyarat garasi, ganjil-genap, jalan berbayar, insentif/disinsentif).
- **MTI Jakarta** (Yusa C. Permana): modal share angkutan umum masih ~20% meski investasi besar; perlu **Single Data / data bank transportasi** untuk perencanaan-monev dan kepercayaan investor.
- **KPBB, FDTJ**: turut menyampaikan ke Gubernur–Wagub.
- **DPRD**: Fraksi PAN (Syahroni) — realisasi penanganan kemacetan 89,98% dari Rp7,15 triliun: apakah menurunkan waktu tempuh dan biaya logistik UMKM? Fraksi Demokrat–Perindo (Nur Afni Sajim) — realisasi pengguna angkutan umum **22,19% vs target 20,97% (2024)**, jauh dari **60%** Perda 5/2014; minta konsistensi disinsentif (pajak progresif, ERP, pajak parkir, pembatasan usia kendaraan, ganjil-genap), MRT fase 3, LRT Jabodebek, revitalisasi halte, informasi perjalanan terintegrasi.
- **Gubernur sendiri** mengakui penyebab lain: galian kabel/proyek SDA/PU yang tidak tertata, tamu negara, pascabanjir, kecelakaan.
- **Papatung 2019** (BRT): implementasi cenderung *predict and provide*, keterbatasan perencanaan, tarif/pembayaran, operasional, pengawasan; komunikasi Dishub–Organda–operator belum optimal; sterilisasi jalur busway memerlukan satgas gabungan; SDM TJ ~9.000 orang.
- **Pubmedia 2025**: tantangan smart mobility — ketergantungan teknologi, biaya tinggi, jangkauan rute, privasi data.
- Risiko yang disebut RPP: MoU tidak tercapai (mitigasi: koordinasi intens).

### D.7 Regulasi yang dirujuk

- **PM 76/2021** Sistem Manajemen Transportasi Cerdas LLAJ: Ps.4 (sistem terbuka, berkesinambungan, sesuai standar; data kecepatan, pola aliran, kepadatan, waktu perjalanan); Ps.6–7 (ATMS: pengaturan lalu lintas kawasan, pemantauan real time, rambu elektronik, kecelakaan, ETLE, deteksi waktu tempuh, **deteksi prioritas bus otomatis**); Ps.11 (APTS: **sinyal prioritas bus untuk perubahan fase/sinyal khusus di simpang bersinyal**, mengurangi tundaan angkutan umum prioritas); Ps.13 (manajemen darurat: info ambulans, pemadam, RS terdekat, derek); Ps.19 (gubernur untuk jalan provinsi; **Kepala BPTJ untuk jalan nasional di Jabodetabek**; kerja sama badan usaha untuk perencanaan–pembangunan–pengoperasian–pemeliharaan); Ps.20 (integrasi dengan sistem K/L dan pemda); Ps.21 (unit pengelola + SDM kompeten); Ps.22–24 (pembinaan/pengawasan: pemantauan dan analisis efektivitas, tindakan korektif).
- **Perda DKI 5/2014 tentang Transportasi**: target 60% angkutan umum, 35 km/jam; tujuan (a)–(e) termasuk transportasi terpadu, tertib, aman, lancar, efisien, dan daya saing dengan kota dunia.
- Disebut tidak langsung: PP 32/2011 (MRLL, Andalalin, MKLL), PM 96/2015 (LOS), PM 49/2014 (APILL) — lihat R00.

---

## E. Pengalaman ATCS di Indonesia

### E.1 Makassar — Simpang empat Jl. Padjonga Dg Ngalle (UMSIDA, Pradana & Wahyuni, Agustus 2025)

- **Metode:** before–after study; data sekunder Dishub Makassar dan PT Adi Joyo Kusumo (geometri, arus, waktu sinyal per fase); 2 hari pengamatan (1 weekday, 1 weekend) × 3 periode puncak (07–10, 12–15, 17–20 WITA); analisis **MKJI 1997**: kapasitas, DS, tundaan, panjang antrean, LOS.
- **Hasil:** volume puncak weekday 7.416 / 7.682 / 7.825 smp/jam (pagi/siang/sore); weekend 6.755 / 8.022 / 7.109 smp/jam. Sebelum ATCS (2023) LOS F, tundaan sangat tinggi, DS mendekati/melebihi 1,0. Setelah ATCS (2024): tundaan rata-rata turun pada sebagian besar periode puncak, antrean berkurang terutama pada lengan dominan, LOS naik 1–2 kategori pada periode tertentu — **tetapi DS rata-rata tetap ≈1,1 dan LOS keseluruhan tetap F**; DS sore weekday masih tinggi.
- **Interpretasi penulis:** perbaikan berasal dari efisiensi sistem (bukan penurunan volume); efektivitas bergantung pada disiplin pengguna jalan dan kapasitas fisik; hambatan samping (parkir liar, PKL) dan geometri membatasi.
- **Rekomendasi:** optimalisasi waktu sinyal, evaluasi berkala, penyesuaian geometrik, rekayasa tambahan, sosialisasi disiplin; dukungan non-teknis (pengawasan, penertiban hambatan samping).
- **Keterbatasan studi:** hanya 2 hari, data sekunder, tabel 1–2 tidak terbaca dalam ekstraksi (angka tundaan per pendekat tidak tersedia di teks).

### E.2 Garut — Simpang Maktal (Farida, Mulyana, Al Fadhilah; Jurnal Konstruksi ITG, Mei 2026)

- Survei lapangan jam puncak sore (volume, rasio belok); analisis manual **PKJI 2023** (arus jenuh, kapasitas, DS, tundaan, antrian, LOS) dibandingkan **PTV Vissim Student 25**.
- Hasil: pendekat B DS >0,9 (hampir jenuh); tundaan rata-rata manual ≈60 det/smp, LOS D–F; simulasi memberi tundaan lebih tinggi di semua pendekat hingga LOS F. Kesimpulan: ATCS berpotensi mengoptimalkan distribusi hijau — ini studi **pra-implementasi** berbasis evaluasi kinerja + mikrosimulasi, pola yang dapat dipakai untuk memprioritaskan 256 simpang Jakarta.

### E.3 Tinjauan multi-kota (JMIA 2024, literature review)

Kota: Medan, Batam, Bandung, Balikpapan (Simpang Dome — Maulidya 2022 "Optimisasi Kinerja ATCS"), Ambon, Serang, Kabupaten Bogor, Bandar Lampung, Kendari (Simpang Taman Kota), Kubu Raya (konsep), Mataram (Dasan Cermen — evaluasi sebelum/sesudah ITCS, Hasyim 2024). Temuan umum: ATCS memberi manfaat kelancaran di lokasi tertentu, tetapi **kendala**: keterbatasan dana, **peralatan rusak/malfungsi**, rendahnya kesadaran/kepatuhan publik, hambatan pemeliharaan dan pengembangan. Rekomendasi: kualitas SDM, pendanaan dan fasilitas, evaluasi dan pengawasan lebih ketat. (Detail kuantitatif per kota tidak tersedia dalam teks yang diarsipkan — hanya abstrak dan daftar pustaka.)

### E.4 Kendala tipikal yang konsisten muncul

1. **Detektor/kamera** rusak atau tidak akurat (loop putus, kamera terhalang), tanpa deteksi kerusakan otomatis.
2. **Komunikasi** simpang–pusat tidak stabil sehingga koordinasi/adaptif jatuh ke mode lokal.
3. **SDM**: operator dan teknisi terbatas; pengetahuan timing plan lemah sehingga sistem adaptif "dibiarkan" atau dikembalikan ke fixed time.
4. **Pemeliharaan** dan anggaran operasional tidak berkelanjutan setelah proyek.
5. **Hambatan samping dan disiplin** (parkir liar, PKL, pelanggaran sinyal, sepeda motor) yang tidak dapat diperbaiki oleh algoritme sinyal.
6. **Kapasitas jenuh (DS ≥ 1)**: sinyal adaptif hanya mengefisienkan pembagian hijau; tanpa TDM/kapasitas, LOS tetap F.
7. **Evaluasi** jarang dilakukan sistematis (before–after singkat, tanpa kontrol), sejalan dengan kritik MTI soal single data.

---

## F. Implikasi untuk Desain Aplikasi ITCS Jakarta

### F.1 Daftar fitur wajib

| ID | Fitur | Sumber / justifikasi |
|---|---|---|
| F-01 | **Mesin kendali sinyal multi-mode**: fixed-time TOD (≥8 rencana), actuated, semi-adaptif, adaptif, terkoordinasi (green wave), dengan fallback otomatis ke plan TOD bila deteksi/komunikasi gagal | PM 49/2014 (R00); klaim fitur Dishub; kendala E.4 |
| F-02 | **Modul TSP (bus priority)** dengan strategi green extension dan early green sebagai default; opsi phase insertion/queue jump/rotation per simpang; parameter per simpang dan time-of-day | Handbook h.7–8, h.23, h.53 |
| F-03 | **Conditional priority berbasis headway dan/atau keterlambatan** dari AVL TransJakarta; tingkat keterlambatan bertingkat; bus non-revenue dikecualikan; prioritas antar bus (paling terlambat menang) | Handbook h.22, h.61, Lampiran A3 (TransLink, LADOT); PM 76 Ps.11 |
| F-04 | **Priority Request Server terpusat** dengan aturan: 1 aktivasi/siklus, lockout siklus berikutnya, reservice-inhibit timer, delay timer, recovery/compensation, pencatatan setiap permintaan (diminta/diberikan/ditolak, durasi, jenis, lockout, waktu recovery) | Handbook h.25, h.61–62, Lampiran A3 (LADOT log) |
| F-05 | **Modul EVP** dengan hierarki preempt (kebakaran > ambulans > VVIP, dapat dikonfigurasi), urutan entry–track clearance–dwell–exit, larangan memotong yellow/all-red, pemendekan walk/FDW terkontrol, transisi kembali ke koordinasi | FHWA-HOP-24-019; NTCIP 1202 preempt objects; STM 2008 §9.1 |
| F-06 | **System-based EVP**: integrasi AVL/CAD Damkar dan ambulans (112/119) + geofence GPS per simpang; route-agnostic; pemicu berdasarkan kecepatan/jarak; VIP green wave berurutan di koridor | FHWA-HOP-24-019 h.1; fitur VIP Green Wave TKDN |
| F-07 | **Check-in/check-out** untuk bus dan EV (geofence + ANPR/kamera sebagai konfirmasi) agar extension dihentikan segera setelah kendaraan lewat | Handbook h.66, h.29 (far-side) |
| F-08 | **Kalkulator kinerja simpang PKJI/MKJI** (DS, tundaan DT+DG, NQ, QL, NS, LOS PM 96/2015) real-time dari data deteksi, plus padanan HCM (control delay, travel speed LOS) untuk benchmark | MKJI Langkah E-4; PM 96/2015; HCM overview Tabel 1 |
| F-09 | **Modul evaluasi before–after** dengan desain on/off bergantian, evaluasi bertahap (pra-optimasi, pasca-optimasi, pasca-TSP), statistik multi-hari; laporan MOE standar | Handbook Bab 8; celah klaim Jakarta (D.1) |
| F-10 | **Kesehatan perangkat & pemeliharaan**: deteksi kerusakan detektor/kamera/komunikasi dari ruang kendali, tiket ke CRM, jadwal pemeliharaan 6-bulanan, umur teknis | PM 76 Ps.7(4)e–f; PM 49/2014 (R00); kendala E.4 |
| F-11 | **Integrasi eksternal via API**: Ditlantas PMJ (ETLE: event pelanggaran + bukti), Bapenda (status pajak per pelat), DLH (status uji emisi per pelat, agregat per ruas), TransJakarta (AVL/APC, jadwal, headway), Damkar/AGD (CAD), pengelola tol | RPP h.9, h.11; Antara 5051249; Handbook PRG-1/2/3 |
| F-12 | **Dashboard publik #LANCAR-Jakarta** dan **dashboard internal TMC** (lihat F.3) | RPP h.4, h.17; MTI (single data) |
| F-13 | **Manajemen konfigurasi & MoU digital**: parameter prioritas (detik extension/truncation, ambang keterlambatan) tersimpan dengan riwayat perubahan dan persetujuan lintas instansi | Handbook h.23 ("seconds of priority diminish over time") |
| F-14 | **Data historis & prediksi**: arsip volume/antrian per menit, model prediksi kejenuhan (waktu, cuaca, libur, acara) untuk pra-penyesuaian siklus; digital twin/simulasi (SUMO/Vissim) untuk uji strategi sebelum diterapkan | Antara 3635259; Handbook Bab 15; ITG Garut |
| F-15 | **Manajemen kejadian**: galian/proyek, banjir, kunjungan tamu negara, kecelakaan sebagai event yang memicu plan khusus dan tercatat untuk analisis reliability | Beritajakarta 145079; HCM Ch.17 |
| F-16 | **Keselamatan pejalan kaki**: minimum walk/ped clearance sebagai batas keras pada semua strategi prioritas; pejalan kaki dalam MOE | Handbook h.25, h.77; STM 2008 |
| F-17 | **Kewenangan & yurisdiksi**: pemetaan simpang per status jalan (provinsi vs nasional/BPTJ vs tol) dan hak akses konfigurasi | PM 76 Ps.19; PM 49 (R00) |
| F-18 | **Pelatihan & SOP**: modul e-learning operator, checklist verifikasi harian, SLA keluhan 3 jam terukur | RPP h.19–20; Beritajakarta 145079; Handbook 6.2.2 |

### F.2 Parameter default TSP/EVP yang disarankan (titik awal untuk pilot, dikalibrasi per simpang)

| Parameter | Nilai awal | Dasar |
|---|---|---|
| Green extension maksimum | 10 s (rentang 7–20 s) | Studi kasus 7–10 s; Calgary hingga 20 s |
| Red truncation maksimum | 10 s (hingga 20 s), tidak melampaui minimum green + Walk + FDW fase lain | Calgary; batas pejalan kaki h.77 |
| Aktivasi | 1 per siklus per pendekat; lockout siklus berikutnya | Handbook h.61, Lampiran A3 |
| Recovery | target ≤2 siklus; koordinasi tidak dilepas | Handbook h.5, h.22 |
| Check-in | 100–150 m atau ~15 s upstream (menurut kecepatan bus); check-out di stop line/near-side | Lampiran A3 (TransLink) |
| Kriteria conditional | headway ≥ headway rencana + X (X awal 2 menit) atau keterlambatan ≥2 menit; tidak untuk bus lebih awal; evaluasi tiap ≤6 s | TransLink (≥2 menit), LADOT (tiap 6 s); definisi on-time x=0, y=3–5 menit |
| Tingkat keterlambatan | 4 level; level tertinggi menang saat konflik | TransLink |
| Ambang tidak diberi prioritas | kaki lawan DS > nilai ambang (mis. 0,85) atau antrian melebihi panjang link | PKJI DJ 0,85 (kriteria desain), Handbook h.23 (batas arus jalan minor) |
| Preempt EV: durasi | dwell hingga check-out, tipikal ~25 s; `preemptMaxPresence` sebagai pengaman | FHWA (25 s rata-rata) |
| Preempt EV: entry | yellow + all-red penuh; walk boleh dipotong hingga minimum yang ditetapkan (angka minimum tidak ada di sumber; MUTCD 4 s dikutip satu studi kasus untuk TSP) | STM 2008; Lampiran A3 |
| Preempt EV: cakupan | pemadam kebakaran wajib; ambulans opsional per kebijakan; VVIP terkonfigurasi | STM 2008 §9.1.3; PM 76 Ps.7(4)a |
| Preempt EV: pemulihan | transisi terkontrol; target < 1–2 siklus (benchmark VT: efek jalan samping pulih dalam 1 siklus; DC: 30 s–7 menit sebagai peringatan) | FHWA; STM 2008 |

Semua nilai di atas adalah nilai awal dari praktik luar negeri; **belum ada angka kalibrasi Jakarta dalam sumber**, sehingga aplikasi harus menyimpan nilai per simpang dan mencatat hasil kalibrasi pilot.

### F.3 KPI dashboard

**Publik (#LANCAR-Jakarta):** kecepatan rata-rata jaringan vs target 35 km/jam (Perda 5/2014); waktu tempuh koridor utama dan indeks keandalan (planning time index); tundaan rata-rata simpang dan LOS (PM 96/2015) per simpang ITCS; jumlah simpang ITCS aktif vs 321; jumlah aktivasi bus priority dan EVP per hari serta rata-rata penghematan waktu; ketepatan headway TransJakarta di koridor ber-TSP; status keluhan (SLA 3 jam); indikator lingkungan (stop-and-go, estimasi emisi) dengan metode yang dipublikasikan; peringkat TomTom sebagai konteks (bukan KPI internal).

**Internal TMC:** per simpang: DS, tundaan DT/DG, NQ/QL, NS, siklus/split aktual vs rencana, uptime detektor/kamera/komunikasi, mode kendali aktif; TSP: permintaan/diberikan/ditolak, detik yang diberikan, lockout, recovery, dampak ke kaki minor (delay/veh/cycle); EVP: aktivasi, durasi, response time (dari CAD), konflik antar preempt; ETLE/ANPR: event terkirim/diterima, laju kecocokan pelat; kejadian (galian, banjir, VVIP); tiket pemeliharaan dan MTTR; before–after per proyek.

### F.4 Integrasi eksternal (API)

| Mitra | Data masuk ke ITCS | Data keluar dari ITCS | Catatan |
|---|---|---|---|
| TransJakarta (AVL/APC/jadwal) | posisi, ETA, headway, keterlambatan, status revenue | log prioritas, waktu tempuh koridor | PRG dapat di TJ center (PRG-1/2) atau di bus (PRG-4); polling rate AVL harus cukup untuk simpang rapat |
| Damkar / AGD 119 / 112 (CAD) | unit ditugaskan, rute, posisi | konfirmasi preempt, response time | system-based EVP; geofence |
| Ditlantas PMJ (ETLE) | daftar target (opsional) | event pelanggaran + foto/video + pelat + waktu | format sesuai standar ETLE; retensi & privasi |
| Bapenda | status pajak per pelat (query) | agregat pelat terdeteksi per ruas | perlu dasar hukum pertukaran data |
| DLH | status uji emisi per pelat | agregat kepatuhan per ruas untuk target operasi | Antara 5051249 |
| Jasa Marga / Hutama Karya | kondisi gerbang/ramp | arus menuju gerbang | sosialisasi data |
| BPTJ/Kemenhub | — | laporan efektivitas (PM 76 Ps.22–24) | jalan nasional di Jabodetabek |

### F.5 Risiko dan mitigasi

| Risiko | Mitigasi (sumber) |
|---|---|
| Klaim manfaat tidak dapat dibuktikan (tanpa MOE/metode) | Modul evaluasi before–after dengan desain on/off dan MOE tertulis (Handbook Bab 8); publikasi metode di dashboard |
| Detik prioritas "menyusut" atau parameter diubah sepihak | MoU digital dengan riwayat dan persetujuan (Handbook h.23) |
| Konflik TSP vs EVP vs VVIP | Hierarki override tegas; uji konflik di simulasi (Handbook h.31, h.62) |
| Detektor/kamera rusak, komunikasi putus | Deteksi kerusakan otomatis, fallback TOD, tiket CRM (PM 76 Ps.7; JMIA) |
| Sistem adaptif "dikembalikan" ke fixed-time oleh operator | Pelatihan bertingkat (matriks Mampu/Mau RPP), audit mode kendali |
| DS ≥ 1: sinyal tidak mampu memperbaiki LOS | Komunikasikan batas (Makassar); dukung TDM/ERP/KRE dengan data (Instran, MTI, DPRD) |
| Keselamatan pejalan kaki tergerus prioritas | Batas keras minimum walk/FDW; pejalan kaki dalam MOE (Handbook h.77; STM 2008) |
| Vendor lock-in / proprietary | Standar terbuka (NTCIP 1202/1211, TCIP), PM 76 Ps.4 "sistem terbuka … sesuai standar" |
| Privasi data ANPR lintas instansi | Tata kelola data, retensi, dasar hukum MoU; kritik Pubmedia soal privasi |
| MoU lintas instansi tidak tercapai | Koordinasi intens (RPP); pilot yang menunjukkan bukti untuk membangun kepercayaan (Handbook h.41) |
| Kewenangan simpang di jalan nasional (BPTJ) | Pemetaan yurisdiksi dan hak akses (PM 76 Ps.19) |

---

## G. Kutipan Kunci (dengan halaman/sumber)

1. "Priority: The preferential treatment of one vehicle class … at a signalized intersection without causing the traffic signal controllers to drop from coordinated operations." — TSP Handbook h.4 (mengutip NTCIP 1211).
2. "Green extension is one of the most effective forms of TSP since a green extension does not require additional clearance intervals." — TSP Handbook h.7.
3. "Most agencies will not grant TSP at the same intersection in which TSP has just been granted until the signals are back in synchronization. That usually takes one or two cycles." — TSP Handbook h.5.
4. "Experiences from prior deployments generally indicate bus travel time savings on the order of 15% … with very minor impacts on the overall intersection operations." — TSP Handbook h.5.
5. "If you have some kind of vehicle location technology and your goal is to increase reliability, it makes sense to grant conditional priority. Granting priority to a bus running ahead of schedule would decrease reliability." — TSP Handbook h.61.
6. "In some jurisdictions, the seconds of priority granted (mysteriously) diminish over time … This can be avoided by having a written agreement … combined with an ongoing data collection/monitoring system." — TSP Handbook h.23.
7. "Inappropriate application of a detection system can be a fatal flaw in the TSP system's design." — TSP Handbook h.66.
8. "On the 98 B-Line, priority is granted to buses that are two or more minutes late. The TSP Master Unit has the ability to distinguish four levels of 'lateness'." — TSP Handbook Lampiran A3 (TransLink).
9. "Typically 1 sec delay per vehicle per cycle." — TSP Handbook Lampiran A3 (LADOT), h.56.
10. "The Virginia Tech Transportation Institute determined that the average duration of a preemption was 25 seconds and that effects on side streets were usually cleared within one cycle." — FHWA-HOP-24-019 h.2.
11. "System-based EVP allows the response vehicle to select any route to the emergency scene … The Global Positioning System-based technology uses geofences around the signalized intersection." — FHWA-HOP-24-019 h.1.
12. "Once a signal was preempted, the coordinated systems took anywhere between 30 seconds to 7 minutes to recover to base time coordination." — FHWA Signal Timing Manual 2008 §9.1.2 (h.9-2).
13. "LOS F, in addition to the average speed thresholds, also applies anytime the d/c ratio exceeds 1.0." — CED HCM 6th Overview h.29.
14. "DT = c × A + NQ1 × 3600 / C … A = 0,5 × (1 − GR)² / (1 − GR × DS)" — MKJI 1997, Simpang Bersinyal, Langkah E-4 (h.2-67).
15. "Tingkat pelayanan A, dengan kondisi tundaan kurang dari 5 detik per kendaraan … F, dengan kondisi tundaan lebih dari 60 detik per kendaraan." — PM 96/2015 Lampiran, Tingkat Pelayanan pada Persimpangan.
16. "Dari total 321 simpang prioritas … teknologi ITCS baru ada di sekitar 65 simpang … selebihnya masih menggunakan ATCS sehingga pengaturannya masih bersifat statis." — Syafrin Liputo, Antara 5050989.
17. "Setelah kendaraan prioritas seperti mobil pemadam kebakaran atau ambulans lewat, maka pengaturan lalu lintas kembali disesuaikan dengan panjang antrean yang ada di kaki persimpangan." — Antara 5050989.
18. "Kami call center-nya ada dan juga terkoneksi langsung dengan CRM. Sehingga SOP untuk penanganan setiap ada keluhan itu kami maksimum tiga jam itu sudah diselesaikan." — Syafrin Liputo, Beritajakarta 145079 (11/6/2025).
19. "Has the allocation of Rp 7.15 trillion for traffic congestion management reduced commuting time and logistics costs for small business operators?" — Syahroni (Fraksi PAN), Kompas 4/7/2025.
20. "Setelah pemasangan ATCS pada tahun 2024, terjadi penurunan tundaan rata-rata pada sebagian besar waktu puncak, namun LOS secara keseluruhan tetap berada di kategori F." — UMSIDA Makassar h.3.
21. "Sistem transportasi umum tingkat lanjut … harus memenuhi prinsip kerja: … d. menggunakan sistem sinyal prioritas bus untuk pengaturan perubahan fase dan sinyal khusus pada simpang bersinyal; dan e. mengurangi waktu tundaan angkutan umum prioritas pada simpang bersinyal." — PM 76/2021 Ps.11(3).
22. "The findings show that while ATCS has provided benefits … there are still several barriers in the maintenance and development of this system … limited financial resources, equipment malfunctions, and low public awareness." — JMIA 2024 (abstrak).

---

## Lampiran: Celah data yang harus dilengkapi pada tahap berikutnya

- Angka tundaan per pendekat Makassar (tabel tidak terekstraksi) dan hasil kuantitatif Balikpapan/Mataram (hanya judul).
- Rumus dan ambang LOS HCM Ch.19 (verifikasi langsung ke HCM, bukan overview).
- Spesifikasi teknis vendor (TKDN/Viero): protokol controller (NTCIP?), polling rate, format log.
- Metode di balik klaim "20–30%", "15–20%", dan "15% waktu tunggu" Dishub DKI.
- Kebijakan Dishub soal ambang keterlambatan TransJakarta dan cakupan EVP (belum pernah dipublikasikan dalam sumber yang tersedia).
