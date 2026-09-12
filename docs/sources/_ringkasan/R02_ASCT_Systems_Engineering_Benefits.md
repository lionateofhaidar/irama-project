# R02 — Catatan Studi: Systems Engineering ASCT, Bukti Manfaat, dan Manajemen Program Sinyal

**Sumber yang dipelajari (teks hasil pdftotext, folder `_teks_ekstraksi`):**

| Kode | Dokumen | Ukuran | Konvensi rujukan halaman dalam catatan ini |
|---|---|---|---|
| **MSE-ASCT** | FHWA-HOP-11-027, *Model Systems Engineering Documents for Adaptive Signal Control Technology (ASCT) Systems*, Agustus 2012 (DKS Associates/FHWA) | 276 hlm | `hlm. N` = nomor halaman cetak (halaman PDF = N + 12). Lampiran B/C/D dirujuk dengan nomor pernyataan/requirement (mis. `Req 13.1.0-2`, `Need 4.14.0-1`). |
| **T414** | NCHRP 20-07 Task 414, *Benefits of Adaptive Traffic Control Deployments — A Review of Evaluation Studies*, Stevanovic dkk., FAU, Nov 2019 | ~80 hlm + lampiran | `hlm. N` = nomor halaman cetak = halaman PDF. |
| **NYSERDA** | NYSERDA Report 16-12 / NYSDOT C-13-04, *Decision-Making Tool for Applying Adaptive Traffic Control Systems*, Ban dkk. (RPI), Maret 2016 | 72 hlm | `hlm. N` = nomor cetak (halaman PDF = N + 9). |
| **EDC-1** | FHWA Every Day Counts, brosur *Adaptive Signal Control Technologies* | 2 hlm | `hlm. 1/2`. |
| **TSPH** | FHWA-HOP-23-041, *Traffic Signal Program Handbook*, April 2023 (TTI/VHB) | 276 hlm | `hlm. N` = nomor cetak (halaman PDF = N + 19). |

Catatan ini disusun untuk mendukung penyusunan **Concept of Operations (ConOps)**, **System Requirements**, **arsitektur**, dan **rencana verifikasi/validasi** aplikasi Intelligent/Integrated Traffic Control System (ITCS) Dishub DKI Jakarta (321 simpang, APILL adaptif real-time berbasis AI/kamera, green wave, prioritas bus & kendaraan darurat, integrasi ETLE/pajak/uji emisi, TMC dengan video wall, KPI).

---

## A. Peta Isi Tiap Dokumen

### A.1 MSE-ASCT (FHWA-HOP-11-027) — dokumen utama

Dokumen ini adalah **panduan + template** untuk agensi yang ingin menilai, memilih, dan mengadakan ASCT dengan proses systems engineering (SE) yang "commensurate with the scale of the project" (sesuai 23 CFR 940.11). Strukturnya:

| Bagian | Isi | Hlm |
|---|---|---|
| Executive Summary | Visi EDC ASCT; peringatan bahwa banyak ASCT dinonaktifkan sebelum umur pakai habis karena kurang sumber daya/kapabilitas atau misalignment tujuan; empat dokumen keluaran (ConOps, System Requirements, Verification Plan, Validation Plan); rekomendasi kuat **jangan gunakan low-bid** untuk ASCT. | 1–2 |
| A. Preamble | Mengapa SE; kapan mempertimbangkan ASCT; ASCT bukan "set and forget"; ASCT tidak bisa mengatasi basic timing settings yang buruk; perlu backup plan; cara memakai dokumen. | 3–7 |
| B. Overview of the Process | Figure 2 "Should you consider ASCT?"; peringatan bahwa ASCT **tidak** menghilangkan kebutuhan staf traffic engineering; Figure 3 alur (Build Requirements → Evaluate Alternatives → Continue Tailoring); 10 langkah "Assembling your documents". | 8–10 |
| C. The Systems Engineering Documents | Tanggung jawab (vendor **tidak boleh** menyusun dokumen SE); deskripsi ConOps, Requirements (Tabel 1 kategori requirement), Verification Plan, Validation Plan; **Procurement Plan** (RFI, industry review, RFQ, RFP best-value, low-bid, market-research approach yang sering gagal, sole source/PIF). | 11–20 |
| D. Concept of Operations Guidance | Alur logis penyusunan ConOps; checklist ConOps; panduan per bab (1 Scope; 2 Referenced Docs; 3 User-Oriented Operational Description; 4 Operational Needs — 4.1 s.d. 4.16; 5 Envisioned System; 6 Operational Environment; 7 Support Environment; 8 Scenarios). | 21–55 |
| E. System Requirements Guidance | Struktur dokumen requirements, checklist, kategori requirement, metode verifikasi (Demonstration/Test/Analyze/Inspection), traceability matrix (Tabel 2). | 56–59 |
| F. Verification Plan Guidance | Tiga level dokumen verifikasi; checklist; isi verification case. | 60–62 |
| G. Validation Plan Guidance | Sama untuk validasi (terhadap needs/scenarios). | 63–65 |
| App. A Templates | Template ConOps, Requirements, Verification, Validation. | 67–82 |
| App. B ConOps Sample Statements | Tabel pernyataan contoh bernomor (1.x s.d. 8.x) yang setiap need-nya ditautkan ke requirement. | 83–166 |
| App. C Example Scenarios | Skenario nyata (disamarkan) "Broadway Avenue corridor": peak unsaturated/oversaturated, business hours, off-peak, LRT preemption, bus priority, EV preemption, major events, major incidents, detector/communication/adaptive-system failure, ultimate deployment. | 167–174 |
| App. D Sample Requirements | Tabel requirement bernomor 1–18 dengan trace ke need. | 175–262 |

### A.2 NCHRP 20-07 Task 414 (T414)

Studi sintesis 85 evaluation studies dari 140 deployment ATCS di AS/Kanada, membangun **Assessment Tool for Adaptive Traffic Control ((AT)²C)** berbasis Excel. Bab: 1 Background & literature review (hlm. 12–16); 2 Research approach (17–18); 3 Framework for data categorization — Section A agency, B deployed ATCS, C evaluation, D benefits (19–24); 4 Data collection/survey (25–26); 5 (AT)²C tool (27–34); 6 Applications & findings — survey results, agency info, operational conditions, infrastructure & costs, evaluation details, data filtering per brand/AADT/retiming frequency/pre-ATCS control/area/network/procurement (35–74); 7 Conclusions (75–76); Appendix A–E.

### A.3 NYSERDA 16-12

Decision tool dua tahap: **kualitatif** (decision tree Figure 8: Layer 1 traffic analysis — volume, delay, travel time reliability, road type, signal spacing; Layer 2 infrastructure analysis — cost, detector, communications) dan **kuantitatif** (regresi & SVM atas data Wolf Road, Albany). Bab: 1 Intro (hlm. 1–4); 2 Review sistem ASCT & MOE (5–18); 3 Guideline/decision tree (19–21); 4 Database (22–35); 5 Quantitative tool (36–54); 6 Case study Western Ave (55–58); 7 Conclusions (59–60).

### A.4 EDC-1 Brochure

Dua halaman: definisi ASCT; manfaat utama; FAQ (di mana paling efektif, seberapa besar perbaikan, seberapa luas dipakai, bagaimana merencanakan); ACS Lite vs sistem besar (SCOOT, SCATS, RHODES).

### A.5 TSPH (FHWA-HOP-23-041)

Bagian I (program): Bab 2 Good Basic Service — GcOST, program objectives, empat elemen program, TSMP (hlm. 9–26); Bab 3 Capability Maturity Framework per area: systems & technology, infrastructure, business processes (planning/design, operations, maintenance, management), workforce, management & administration (culture, staffing, performance measurement & outreach, collaboration) (27–68). Bagian II (systems & technology): Bab 4 Systems Engineering (69–81); Bab 5 Intersection Control (83–124); Bab 6 Detection — termasuk *Detection for ASC* (129–163); Bab 7 Communications — arsitektur, NTCIP, **security** (165–195); Bab 8 System Control — TBC/interconnected/traffic-responsive/adaptive, Tabel 42 spesifikasi ASC, arsitektur referensi CTSS, Tabel 43 sensor density (197–215); Bab 9 Advanced Control — preemption/priority, **ATSPM**, interchange, special event/incident, regional program, connected vehicle (217–249); Appendix Scope of Work Template SE analysis (251–255).

---

## B. Proses Systems Engineering (V-model) untuk ASCT

### B.1 Fase dan logika proses (MSE-ASCT hlm. 7–10; TSPH hlm. 70–71)

MSE-ASCT membagi proses menjadi empat fase (hlm. 7):
1. **Fase 1 — definisikan *what*, bukan *how***: needs, objectives, operational description. Hati-hati membedakan **constraint** dari **requirement**; contoh klasik kesalahan: menetapkan tipe controller eksisting sebagai requirement padahal itu constraint yang menyembunyikan trade-off (hlm. 7).
2. **Fase 2 — identifikasi constraints** dan putuskan mana yang diterima (menjadi non-functional requirement) atau dihilangkan (dengan biaya finansial/politik).
3. **Fase 3 — desain** (*how*).
4. **Fase 4 — verifikasi & validasi**: memastikan "you get what you paid for".

Proses bersifat **iteratif**: jawaban pertanyaan → statement ConOps → requirement → cek kompatibilitas dengan constraint → revisi (hlm. 9). Karena ASCT hampir selalu dipasang di atas sistem eksisting, ConOps disusun berulang, satu elemen per iterasi (hlm. 10).

TSPH (hlm. 70–71) merangkum V-model sekuensial: purpose (dari planning docs) → user needs (ConOps) → requirements (validasi terhadap needs) → design (verify vs requirements, validate vs needs) → implement per bagian (test/verify/validate) → integrate (test/verify/validate) → operate → dokumentasi defisiensi untuk revisi/retirement. Proses **iteratif** (prototype–evaluate–refine) dianjurkan untuk elemen inovatif seperti integrasi CV, transit control, smart pedestrian — relevan bagi komponen AI/kamera ITCS Jakarta yang belum punya needs terdokumentasi matang.

### B.2 Sepuluh langkah "Assembling your documents" (MSE-ASCT hlm. 10)

1. Baca seluruh panduan. 2. Siapkan ConOps sesuai template (outline ANSI G-043-1992). 3. Salin & edit statement dari Tabel Sample Statements. 4. Tulis teks sendiri untuk bagian yang diminta. 5. Setiap statement ConOps punya ID unik; setiap need (Bab 4) merujuk ≥1 requirement. 6. Siapkan System Requirements sesuai template. 7. Untuk tiap need, salin requirement yang terkait; jika memilih *child* requirement, *parent*-nya wajib ikut. 8. Need yang tidak tercakup sampel → buat requirement baru. 9. Verification Plan: **setiap requirement butuh verification test**. 10. Validation Plan: **setiap need butuh validation test**.

### B.3 Deliverables dan kepemilikan

| Deliverable | Audiens | Siapa menyusun | Sumber |
|---|---|---|---|
| Concept of Operations | Operator, manajer, maintenance, pengambil keputusan, pejabat terpilih | Agensi (boleh dibantu konsultan independen) | hlm. 11–13 |
| System Requirements | Staf teknis, pengguna, desainer, vendor | Agensi | hlm. 13–14 |
| Verification Plan (+ procedures + report) | Sama dengan Requirements | Plan: agensi; *procedures* boleh vendor jika manual belum ada, tetapi harus diaudit agensi; tes disaksikan & diaudit agensi | hlm. 11, 14 |
| Validation Plan (+ report) | Sama dengan ConOps | **Agensi, tidak boleh didelegasikan ke vendor** | hlm. 15 |
| Procurement Plan | — | Agensi | hlm. 15–20 |

Kutipan: "a vendor should never be tasked with the responsibility of preparing the systems engineering documents. This would be a clear conflict of interest" (hlm. 11).

### B.4 Checklist ConOps (MSE-ASCT hlm. 21)

- Alasan pengadaan sistem dinyatakan jelas?
- Semua stakeholder (yang mengoperasikan, memelihara, membangun, mengelola, memakai, terdampak) teridentifikasi beserta perannya?
- Alternatif operasional non-adaptif (traffic responsive, TOD) dijelaskan dan pilihan dijustifikasi?
- Lingkungan eksternal dan **interface ke sistem eksisting** dijelaskan?
- Support environment (termasuk maintenance) dijelaskan?
- Operational environment dijelaskan?
- Skenario operasi normal lengkap? Skenario **maintenance dan failure** lengkap?
- Skenario memuat sudut pandang semua stakeholder (siapa melakukan apa)?
- Semua constraint teridentifikasi?

### B.5 Checklist Requirements (hlm. 57)

Definisi semua fungsi utama; tiap fungsi punya requirement "what + under what conditions" (environmental, reliability, availability); istilah/akronim didefinisikan; dokumen pendukung dirujuk; tiap requirement **traceable** ke need/scenario; tiap requirement **concise, verifiable, clear, feasible, necessary, unambiguous, technology (vendor) independent**; requirement yang bergantung teknologi ditandai sebagai constraint; tiap requirement punya metode verifikasi dan trace ke verification case. Aturan penulisan: satu pernyataan per requirement, hindari "and/but/except" (hlm. 57).

### B.6 Checklist Verification Plan & Validation Plan (hlm. 60, 63–64)

Menjawab who/what/where/when; jelas apa yang terjadi bila ada kegagalan (stop/restart/skip, fix software/reset/ubah requirement, re-verify); mendokumentasikan konfigurasi hardware/software; semua requirement (atau needs/scenarios) ter-trace ke verification (validation) case. Aturan praktis: "if it was important enough to write down as a requirement, then it should be verified, at least once" (hlm. 60).

### B.7 Scope of Work SE analysis (TSPH Appendix hlm. 251–255)

Task 1 ConOps (1a existing docs → Bab 1–2; 1b user needs existing activities → Bab 3–4; 1c needs new activities; 1d system concept/architecture → Bab 5; 1e environment → Bab 6–7; 1f scenarios → Bab 8). Task 2 Validation Plan. Task 3 Requirements (traceability table, **requirements walk-through** di mana systems engineer mendemonstrasikan setiap requirement tertaut ke need). Task 4 Verification Plan. Task 5 SE analysis (23 CFR 940.11: arsitektur, peran agensi, requirements, alternatif, procurement, standar & testing, sumber daya O&M). Task 6 Procurement options (qualifications vs cost vs sole-source; RFP vs DBB vs DB; peran agency/systems engineer/designer/contractor/vendor/tester). Task 7 Resource requirements (staffing gap analysis, equipment, facilities).

---

## C. Concept of Operations — Model

### C.1 Struktur ConOps (ANSI G-043-1992; MSE-ASCT hlm. 21)

1 Scope (1.1 document purpose; 1.2 project purpose & scope; **1.3 procurement** — metode harus diputuskan dini karena memengaruhi format requirements) · 2 Referenced documents (kebijakan, regional ITS architecture, standar ANSI/IEEE/NTCIP/NEC, MOU, ICD sistem eksternal) · 3 User-oriented operational description · 4 Operational needs · 5 System overview · 6 Operational environment · 7 Support environment · 8 Operational scenarios.

Bab 3 harus memuat: network characteristics, traffic characteristics, signal grouping, land use, operating agencies, **existing architecture & infrastructure** (TMC/server/workstation/LAN-WAN, hub/on-street master, komunikasi: media/bandwidth/protokol, lokasi & teknologi detektor, fungsi sistem yang dipakai, kapan retiming terakhir) (hlm. 23–24); limitations sistem eksisting; proposed improvements; **statement of objectives**; strategies; alternatif non-adaptif yang dipertimbangkan (hlm. 24–30).

### C.2 Operational objectives (hlm. 25–26; App. B 3.4.4)

Enam pilihan objective, boleh kombinasi dan berubah menurut waktu ("Variable objectives"):
1. **Smooth flow** — green band satu/dua arah, platoon jarang berhenti; fase non-koordinasi dijalankan pada saturasi tinggi (green sependek mungkin) dengan batasan mencegah phase failure & overflow turn bay.
2. **Maximize throughput** — green band lebar di rute koordinasi tanpa kongesti tak wajar di gerakan lain.
3. **Access equity** — melayani semua gerakan secara adil (kawasan retail/aktivitas).
4. **Manage queues** — antrian tidak memblokir simpang hulu; kontrol cycle/phase length, *gating*, multiple phase service.
5. **Variable** — mis. pipeline/throughput saat peak, equity saat jam kerja, minimize stops off-peak.
6. **Maximize isolated intersection efficiency** — delay/stops/fungsi objektif komposit.

Strategi (hlm. 26–27): provide a pipeline (cycle-based dengan "resonant cycle length" = kelipatan travel time antar simpang; atau non-cycle-based mengikuti critical intersection), distribute phase splits (occupancy/gap-out–max-out), manage queues (offset untuk mengosongkan blok, batasi cycle, tentukan lokasi penyimpanan antrian), variable strategies.

Goals & user objectives dari App. B 3.4.2–3.4.3: mendukung mobilitas kendaraan/pejalan kaki/transit; perbaikan terukur mobilitas personal (adjust to changing conditions, reduce delays, reduce travel times, **same level of safety**); interoperabilitas antar agensi (data exchange & control, remote monitoring, standar); sistem regional (regional ITS architecture, C2C, lapor kondisi lalu lintas); lingkungan (kurangi emisi via stops & delays); jadwal (sistem matang, risiko rendah).

### C.3 Daftar lengkap kategori operational needs (MSE-ASCT Bab 4, hlm. 30–50; App. B 4.x)

| No. | Kategori need (App. B) | Pertanyaan kunci panduan | Contoh statement need |
|---|---|---|---|
| 4.1 | **Adaptive strategies** | Operasi terbaik tanpa adaptif: fixed-cycle coordination / actuated isolated / actuated linked? Teknik adaptif: sequence-based (common cycle; hitung cycle-split-offset), non-sequence-based (tanpa cycle; critical intersection + progression), phase-based (1–2 simpang minor di-slave ke simpang kritis) (hlm. 30–32). | 4.1.0-1 "The system operator needs the ability to implement different strategies individually or in combination…: maximize throughput; smooth flow; distribute phase times equitably; manage length of queues; manage locations of queues; at isolated intersection optimize with minimum phase failures". 4.1.0-3 ubah strategi berdasarkan kondisi. 4.1.0-4 deteksi repeated phase failures. 4.1.0-6/7 modifikasi/fix phase sequence. 4.1.0-8 tentukan coordinated route. 4.1.0-9 set timing parameter sesuai kebijakan agensi. |
| 4.2 | **Network characteristics** | Jumlah sinyal total & per grup; grup fleksibel (Figure 8: 150s peak, 80/120/70s lunch, 90/120s school exit, 80/55s evening, 120/75s Saturday) (hlm. 33–36). | 4.2.0-1 kendalikan hingga XXX sinyal hingga XXX mil dari TMC; 4.2.0-2 hingga XX grup independen; 4.2.0-3 ubah komposisi grup menurut kondisi. |
| 4.3 | **Institutional & system boundaries / crossing arterials** | Batas dengan sistem lain: part of operation (kirim cycle/sync/offset), part of system, constrained adaptive (terima cycle dari tetangga atau deteksi platoon masuk) (hlm. 36–38). | 4.3.0-1 kendalikan sinyal yurisdiksi lain; 4.3.0-2 kirim data ke sistem lain; 4.3.0-3 koordinasi dua rute bersilangan; 4.3.0-4 terima data sistem lain; 4.3.0-5 batasi cycle agar kompatibel; 4.3.0-6 deteksi lalu lintas dari sistem tetangga. |
| 4.4 | **Security** | Level akses & jurisdiction rights yang dapat ditetapkan administrator (hlm. 38). | 4.4.0-1 "security management and administrative system that allows access and operational privileges to be assigned, monitored and controlled by an administrator, and conform to the agency's access and network infrastructure security policies". |
| 4.5 | **Queuing interactions** | Antrian masuk dari hilir (freeway/ramp meter)? dari generator (parkir)? antrian keluar sistem tidak dapat diterima? kontrol lokasi penyimpanan antrian? flush? (hlm. 38–39). | 4.5.0-1…5: deteksi antrian dari luar/dalam sistem, yang merambat keluar, simpan antrian di lokasi aman, cegah antrian di lokasi tertentu. |
| 4.6 | **Pedestrians** | Abaikan (dilayani lokal), akomodasi sesekali, selalu beri waktu penuh, fitur khusus (early walk, exclusive phase, recall) (hlm. 39–40). | 4.6.0-1…5. |
| 4.7 | **Non-adaptive situations** | Tangani adaptif otomatis; deteksi kondisi → non-adaptif; jadwal TOD; special events/diversion; operator override (hlm. 40–41). | 4.7.0-1 deteksi kondisi saat adaptif bukan pilihan & jalankan operasi pre-defined; 4.7.0-2 jadwalkan TOD; 4.7.0-3 override. |
| 4.8 | **System responsiveness** | Respons terhadap perubahan kecil vs besar; response time berbeda untuk solusi adaptif vs non-adaptif; hindari osilasi (hlm. 41–42). | 4.8.0-1 ikuti perubahan kondisi secara dekat; 4.8.0-2 batasi pilihan cycle (resonant). |
| 4.9 | **Complex coordination & controller features** | 16 pertanyaan: multiple phase service, overlaps, variable sequence, phase omit, detector switching, non-standard features, coordinate different approaches/turning movements, early release of hold, hold uncoordinated phase position, late phase introduction, protected/permissive, FYA, movement restriction TOD, per-lane, transit queue jump, post-preemption sequences (hlm. 42–44). | 4.9.0-1 "implement the following advanced controller features while maintaining adaptive operation: …" |
| 4.10 | **Monitoring and control** | Dari TMC, on-site, multi-TMC, remote, maintenance vehicle, sistem eksternal (ICM) (hlm. 44). | 4.10.0-1 lokasi akses; 4.10.0-2 akses database/monitoring controller & signal management system. |
| 4.11 | **Performance reporting** | Ukur terhadap objective function sistem **dan** terhadap mobility objectives agensi; real-time logging; retensi; data warehouse; external interfaces; **use historical data to recreate events** (jawab komplain "saya menunggu 30 menit") (hlm. 44–46). | 4.11.0-1 sistem eksternal memonitor ASCT otomatis; 4.11.0-2 simpan & laporkan data perhitungan timing; 4.11.0-3 data ukur kinerja; 4.11.0-4 simpan semua data & ekspor; 4.11.0-5 lapor real-time ke sistem eksternal; 4.11.0-6 status timing & input eksak untuk analisis historis; 4.11.0-7 laporan historis & real-time. |
| 4.12 | **Failure notification** | Laporkan langsung ke staf atau lewat sistem lain (maintenance management) (hlm. 46). | 4.12.0-1 notifikasi segera; 4.12.0-2 teruskan otomatis ke sistem eksternal; 4.12.0-3 log lengkap alarm. |
| 4.13 | **Preemption and priority** | Railroad, EV, LRT, bus; proses recovery; frekuensi call; aturan (fase saat/pasca preemption) (hlm. 47). | 4.13.0-1…4. |
| 4.14 | **Failure and fallback modes** | Kembali ke TOD (central/on-street master/local) atau free; toleransi kegagalan detektor sesuai kemampuan maintenance (hlm. 48). | 4.14.0-1 "fall back to TOD or isolated free operation, as specified by the operator, without causing disruption to traffic flow, in the event of equipment, communications and software failure". |
| 4.15 | **Constraints** | Infrastructure (controller, detector, signal system, comms, cabinet); management & HR (ketakutan staf, hiring/training policy); financial; complexity (setara TOD / TOD+TRPS / lebih kompleks); people (kapabilitas, struktur O&M, pendanaan); hardware/software; schedule (hlm. 48–50). | 4.15.0-1 peralatan yang wajib dipakai; 4.15.0-2 IT policy. |
| 4.16 | **Training and support** | — | Semua staf O&M dilatih; sistem dipelihara agar requirement tetap terpenuhi; update software; warranty. |
| 4.17 | **External interfaces** | Aktifkan rambu/DMS berdasar kondisi; reaksi terhadap perintah ICM/sistem lain. | 4.17.0-1, 4.17.0-2. |
| 4.18 | **Maintenance** | Peralatan mudah diakses. | 4.18.0-1. |

Ringkasnya, kategori kebutuhan yang wajib ada dalam ConOps ITCS: **detection, communication, adaptive algorithm behaviour (strategies & responsiveness), coordination & grouping, transitions/non-adaptive situations, priority/preemption, monitoring & control, performance reporting, data logging/storage, failure notification, fail-safe/fallback, security, pedestrians, queue management, boundaries/interfaces, constraints, training, maintenance/support/warranty**.

### C.4 Envisioned system, environment, support (Bab 5–7, hlm. 50–54)

Bab 5: block diagram konseptual & high-level data flow; Figure 9 contoh diagram aktivitas stakeholder yang menandai proses mana yang akan diotomatisasi (monitoring, implement flush/queue-mgmt strategy, update timing plans, investigate complaint) (hlm. 52). App. B 5.x memberi statement untuk size & grouping, operational objectives per grup, **fallback operation** (common cycle; isolated actuated; slaved to critical intersection), crossing routes & adjacent systems, operator access, complex controller features, organisasi. Bab 6: stakeholders, aktivitas (siapkan parameter, fine tuning, monitoring, interaksi antar agensi), struktur organisasi, fasilitas (TMC/server room, AC, UPS/battery backup, operator 24/7?), pelatihan. Bab 7: test equipment, **simulator** dan **development server** untuk menguji firmware/upgrade sebelum live, dukungan vendor/konsultan (audit berkala), MOU antar agensi, disposal.

### C.5 Skenario operasional (Bab 8, hlm. 54–55; App. B 8.x; App. C)

Tiap skenario = satu lokasi + satu kondisi lalu lintas + aktivitas stakeholder + respons ASCT, dengan elemen: network, traffic conditions, operational objectives, coordination & timing strategies, summary of operation. Skenario tidak menghasilkan requirement — hanya *needs* yang menghasilkan requirement; jika skenario memuat perilaku yang tidak tercakup need, tambahkan need (hlm. 54). Kelompok skenario yang direkomendasikan App. B 8.1: heavy congested; heavy uncongested; moderate balanced; light balanced; demand-affecting event; capacity-affecting event (cuaca, insiden); fault conditions (communications, detection, adaptive processor); priority & preemption; pedestrians; installation/calibration.

Poin penting dari App. C (proyek nyata):
- **Peak oversaturated**: cycle = maksimum yang diizinkan operator atau ditentukan "maximum duration between successively servicing a phase with demand"; bandwidth maksimum di arah dominan; lead-lag dan double service left turn ditentukan sistem (hlm. 168–169).
- **Off-peak**: cycle rendah dengan omit protected left turn dan max green di bawah walk+clearance tetapi tetap melayani pejalan kaki tanpa keluar koordinasi (hlm. 169).
- **Bus priority**: logika keputusan (extend green, early green, exclusive phase) di local controller dengan aturan operator (waktu/cycle sejak priority terakhir, priority level); logika kelayakan bus (schedule adherence, route, in/out of service, load) **berada di sistem transit, bukan ASCT** (hlm. 170).
- **EV preemption**: rute preemption dari fire house; preemption ditunda sampai diperlukan berdasarkan travel time (hlm. 171).
- **Major incidents**: arsitektur memungkinkan bagian utara/tengah/selatan koridor merespons independen namun konsisten (hlm. 171–172).
- **Detector failure**: local recall + alarm; system detector → data alternatif (lajur sebelah/hulu/hilir); jika jumlah gagal > ambang → fallback TOD/free sesuai lokasi & waktu; alarm otomatis ke O&M (hlm. 172).
- **Adaptive system failure**: dua jenis — kegagalan server/peralatan; dan ketidakmampuan algoritma menangani kondisi (kongesti merambat masuk dari luar; occupancy ekstrem) → fallback (hlm. 172–173).
- **Installation**: hasil perhitungan antara harus dapat diperiksa untuk kalibrasi per detektor dan identifikasi detektor rusak (App. B 8.12, hlm. 165).

---

## D. System Requirements — Kutipan/Parafrase per Kategori (MSE-ASCT App. D)

Nomor di bawah adalah ID sample requirement App. D (hlm. 175–262). Sistem disebut "ASCT". Nilai "XX" harus ditetapkan agensi.

### D.1 Network characteristics (Sec. 1)
- 1.0-1 "The ASCT shall control a minimum of XX signals concurrently."
- 1.0-2 dukung grup sinyal; 1.0-2.0-1 batas grup ditetapkan user; 1.0-2.0-2 minimum XX grup; 1.0-2.0-3 ukuran grup 1–XX; 1.0-2.0-4 tiap grup beroperasi independen; 1.0-2.0-5.x batas grup diubah oleh sistem menurut **TOD schedule**, **kondisi lalu lintas**, atau **perintah user**.

### D.2 Type of operation — mode & fallback ke TOD (Sec. 2.1.1)
- 2.1.1.0-1 beroperasi non-adaptif saat kondisi terdefinisi hadir; 2.1.1.0-2 saat peralatan adaptif gagal; 2.1.1.0-2.0-1 saat detektor tertentu gagal; **2.1.1.0-2.0-2 saat jumlah detektor gagal pada satu controller melebihi nilai user**; 2.1.1.0-2.0-3 saat jumlah detektor gagal dalam grup melebihi nilai user; 2.1.1.0-2.0-4 saat link komunikasi tertentu gagal; 2.1.1.0-3/4 saat user memerintahkan berhenti adaptif (grup/seluruh); 2.1.1.0-5 sesuai TOD schedule user; 2.1.1.0-6 saat diperintahkan proses sistem eksternal.
- 2.1.1.0-7 "The ASCT shall alter the adaptive operation to achieve required objectives in user-specified conditions" (objective shift); sub-req 7.0-1…4: saat kondisi memenuhi kriteria user, ubah state controller untuk **maximize throughput**, **prevent queues exceeding storage at user-specified locations**, **equitable green distribution**, **two-way progression**.
- 2.1.1.0-8 min/max phase time per fase per controller; tidak melampaui/di bawah nilai.
- 2.1.1.0-9 "detect repeated phases that do not serve all waiting vehicles (may be inferred by repeated max-out)"; 9.0-1 ubah operasi untuk meminimalkan repeated phase failures.
- 2.1.1.0-10 tentukan urutan fase di simpang tertentu berdasarkan fungsi optimasi.
- 2.1.1.0-11 koordinasi sepanjang rute; 11.0-1 rute user-defined; 11.0-2 tentukan rute dari kondisi lalu lintas; 11.0-3 dari jadwal; 11.0-4 simpan XX rute; implementasi rute tersimpan via perintah operator/kondisi/jadwal.
- 2.1.1.0-12 tidak menghalangi phase timings di local controller yang ditetapkan kebijakan agensi.

### D.3 Allowable phases (Sec. 2.1.2)
- 2.1.2.0-1/2 tidak mencegah protected/permissive dan lead/lag left turn; 0-3/4/5 cegah skipping fase tertentu (saat sequence tertentu / external input / TOD); 0-6/7/8/9 omit fase (cycle < nilai / kondisi lalu lintas / external input / TOD); 0-10/11 alokasi unused time dari fase yang terminate early/skipped ke next phase, next coordinated phase, user-specified (previous) phase; 0-12 jangan ubah urutan fase di simpang tertentu.

### D.4 Oversaturation & queue (Sec. 2.1.3)
- 2.1.3.0-1 "detect the presence of queues at pre-configured locations"; 0-2 saat antrian terdeteksi jalankan timing plan/mode operasi user; 0-3 jalankan strategi adaptif user; 0-4 omit fase di controller tertentu; **0-5 "meter traffic into user-specified bottlenecks by storing queues at user-specified locations"**; 0-6 simpan antrian di lokasi tertentu; 0-7 pertahankan capacity flow melalui bottleneck; 0-8 batasi cycle grup ke nilai user saat antrian terdeteksi.

### D.5 Sequence-based coordination (Sec. 2.2) / non-sequence (2.3) / single intersection (2.4) / phase-based (2.5)
- 2.2.0-2 pilih cycle dari TOD; 2.2.0-3 hitung phase length semua fase sesuai strategi; 2.2.0-4 hitung offset untuk reference point tiap controller sepanjang rute dalam grup; 2.2.0-4.0-1 terapkan offset; 2.2.0-5 hitung cycle tiap siklus berdasarkan objective; 5.0-1/2 batasi cycle ke nilai/rentang user; 5.0-3 hitung cycle optimum sesuai strategi; **5.0-4 batasi perubahan cycle ≤ nilai user**; 5.0-4.0-1 naikkan limit untuk XX siklus berikut bila kondisi berubah (didefinisikan XX kenaikan berturut-turut pada laju maksimum); 5.0-5 sesuaikan offset untuk meminimalkan stop platoon dari fase hulu tertentu.
- 2.3.0-2 (non-sequence) hitung state sinyal di critical controller; 0-3 di simpang non-kritis hitung waktu fase hijau relatif terhadap reference point simpang kritis; **0-4 "when demand is present, implement a user-specified maximum time between successive displays of each phase"**; 0-5 hindari stop kendaraan dari fase hulu.
- 2.4.0-2/3/4 (isolated) hitung cycle, phase length, phase order dari kondisi terukur; 0-3.0-1 batasi perbedaan panjang fase antar layanan berturut-turut.
- 2.5.0-2…7 (phase-based).

### D.6 Responsiveness (Sec. 2.6)
- 2.6.0-1 batasi perubahan cycle berturut-turut < nilai user; 0-2 batasi perubahan phase time antar siklus (tidak berlaku untuk gap-out/skip aktuasi); 0-3 batasi frekuensi perubahan arah koordinasi utama; **0-4 "when a large change in traffic demand is detected, respond more quickly than normal operation, subject to user-specified limits (DEFINE 'MORE QUICKLY')"**; 0-5 pilih cycle dari daftar user-defined.

### D.7 External/internal interfaces (Sec. 3) — integrasi dengan central system
- 3.0-1 "support external interfaces according to the referenced interface control documents"; interface requirements harus memuat: information layer protocol, application layer protocol, lower layer protocol, data aggregation, frequency of storage, frequency of reporting, duration of storage.
- 3.0-1.0-1…5 kirim operational / control / monitoring / coordination / performance data ke sistem eksternal XX; 3.0-1.0-6 terima perintah dari sistem eksternal; 3.0-1.0-7 laksanakan perintah: specified cycle length, direction of progression, adaptive strategy.

### D.8 Crossing arterials & boundaries (Sec. 4)
- 4.0-1 conform ke operasi sistem eksternal; 0-1.0-1 minimalkan interupsi lalu lintas masuk (bisa via deteksi tanpa koneksi); 0-1.0-2 jalankan fixed cycle sama dengan sistem tetangga; 0-1.0-3 ubah operasi berdasarkan data sistem lain; 0-1.0-4 koordinasi adaptif di rute bersilangan.

### D.9 Access & security (Sec. 5)
- 5.0-1 security policy mencakup 21 elemen: local access, remote access, system monitoring, manual override, development, operations, user login, password, administration, signal controller group access, access to classes of equipment, **access by jurisdiction**, output activation, system parameters, report generation, configuration, security alerts, security logging, security reporting, database, signal controller.
- 5.0-2 akses monitoring & kontrol dari: agency TMC, maintenance facility, LAN/WAN, TMC agensi lain, local cabinet, maintenance vehicle, remote via internet; 5.0-3 comply agency security policy; 5.0-4 tidak menghalangi akses ke database/monitoring/reporting controller lokal oleh signal management system yang terpasang.

### D.10 Data log (Sec. 6) — logging & performance data
- 6.0-1 log **time-stamped**: vehicle phase calls, pedestrian calls, EV preemption calls, transit priority calls, railroad preemption calls, start/end tiap fase, controller interval changes, start/end transisi ke plan baru.
- 6.0-2 ekspor log: Excel, text, CSV, open-source SQL; 6.0-3 simpan event log ≥ XX hari; 6.0-4 simpan hasil semua perhitungan parameter timing ≥ XX hari; 6.0-5 simpan data input algoritma ≥ XX hari: volume, occupancy, queue length, phase utilization, arrivals in green, green band efficiency; 6.0-6 arsip otomatis; 6.0-7 kapasitas storage untuk XX controller (controller state, reports, log, security data, ASCT parameters, detector status); **6.0-8 "calculate and report relative data quality including the extent data is affected by detector faults"**; 6.0-9 laporan perbandingan day-to-day, hour-to-hour, hour-of-week, day-of-year; 6.0-10 database standar; **6.0-11 "report stored data in a form suitable to provide explanations of system behavior to public and politicians and to troubleshoot the system"**; 6.0-12 simpan volume/occupancy/queue per XX menit.

### D.11 Advanced controller operation (Sec. 7) — interface controller
- 7.0-1 layani fase lebih dari sekali per cycle bila ditentukan; 7.0-2…5 minimum XX overlap, XX fase, XX ring, XX fase per ring; 7.0-6 minimum XX phase sequence user-defined, dapat ditugaskan ke plan, dieksekusi via TOD atau kondisi; 7.0-7/8 tidak mencegah output fase/overlap via TOD/external input; 7.0-9 fase apa pun dapat menjadi coordinated phase; 7.0-10 early release coordinated phase; 7.0-11 tidak mencegah FYA; 7.0-12 tidak mencegah actuated control lokal dengan XX extension/passage timer per detector channel; 7.0-12.0-1 adaptif dengan detector channel tertentu; 7.0-13 controller boleh menjalankan cycle berbeda dari tetangga; 7.0-14/15 fitur & detector logic custom.
- Catatan ConOps 6.0-6.0-1/2: "The central server will be a standard platform (maintained by the agency IT Department) and able to be replaced independently from the software"; "The agency selection of controller will not be constrained by the adaptive software" (hlm. 149).

### D.12 Pedestrians (Sec. 8), Special functions (Sec. 9), Detection (Sec. 10)
- 8.0-1 walk hingga XX detik sebelum vehicle green; 8.0-2/3 akomodasi crossing time selama adaptif / lalu lanjut adaptif; 8.0-4 exclusive pedestrian phase; 8.0-5 pedestrian recall via TOD; 8.0-6 late start non-coordinated phase (4 kondisi); 8.0-7 recall di fase bersebelahan dengan coordinated; 8.0-9 tidak menghambat negative ped timing.
- 9.0-1/2/3 set special function output berdasarkan occupancy detektor / cycle length / TOD (untuk rambu/DMS).
- 10.0-1 kompatibel dengan teknologi detektor A/B/C yang ditetapkan agensi.

### D.13 Preemption & priority (Sec. 11–12)
- 11.0-1/2/3 pertahankan operasi adaptif di simpang non-preempted selama railroad/EV/LRT preemption; **11.0-4 "resume adaptive control of signal controllers when preemptions are released"**; 11.0-5 aksi user di simpang non-preempted (inhibit phase, aktifkan sign/DMS); 11.0-6 operasi normal saat special function (phase omit, max recall, fire route); 11.0-7 lepaskan controller tertentu ke kontrol lokal saat satu sinyal dalam grup di-preempt; 11.0-8 tidak mencegah limited-service actuated mode lokal.
- 12.0-1 lanjutkan adaptif grup saat satu controller ada transit priority call; 12.0-2 majukan awal green (user-defined, adaptif berlanjut); 12.0-3 tunda akhir green; 12.0-4 ≥ XX exclusive transit phases; 12.0-5 kontrol fase kendaraan independen dari LRT-only/bus-only phases; 12.0-6/7 interface ke sistem bus/LRT priority eksternal; **12.0-8 "accept a transit priority call from: a signal controller/transit vehicle detector; an external system"**.

### D.14 Failure events & fallback (Sec. 13) — detector health, comms, processor
- 13.1.0-1 aksi user saat data valid dari XX detektor dalam grup hilang: 1.0-1 lepaskan ke central system control; 1.0-2 lepaskan ke operasi lokal TOD; 13.1.0-2 sumber data alternatif: detektor alternatif user-specified, **data historis tersimpan dari detektor yang gagal**; 13.1.0-2.0-3 "switch to the alternate source in real time without operator intervention"; 13.1.0-3 alarm ke penerima user (boleh via maintenance management system); 13.1.0-4/5 log permanen yang searchable, archivable, exportable.
- 13.2-1 aksi saat komunikasi ke ≥1 controller dalam grup gagal; 13.2-1.0-1 lepaskan seluruh grup ke kontrol lokal; 13.2-1.0-2 switch real-time tanpa operator; 13.2-2 alarm; **13.2-3 "issue an alarm within XX minutes of detection of a failure"**; 13.2-4/5 log.
- 13.3-1 aksi saat adaptive control gagal (ke central / ke lokal TOD); 13.3-2 alarm; 13.3-3 log; **13.3-4 "during adaptive processor failure, provide all local detector inputs to the local controller"**.

### D.15 Software, training, maintenance/warranty, schedule (Sec. 14–17)
- 14.0-1 platform OS; 14.0-2/3 penuhi semua requirement dengan detektor/controller tipe tertentu.
- 15.0-1.x pelatihan operasi, troubleshooting, preventive maintenance & repair, konfigurasi, administrasi, **kalibrasi**; materi cetak & elektronik; lokasi; min XX jam untuk XX staf; XX sesi.
- 16.0-1 kontrak maintenance terpisah (repairs to preserve requirements fulfillment, responsiveness); 16.0-2 update software rutin XX tahun agar requirement tetap terpenuhi (termasuk IT management requirements); 16.0-3 warranty XX tahun.
- 17.0-1/2 set state I/O eksternal via TOD.

### D.16 Performance measurement, monitoring & reporting (Sec. 18)
- **18.0-1 "report measures of current traffic conditions on which it bases signal state alterations"**; **18.0-2 "report all intermediate calculated values that are affected by calibration parameters"**; 18.0-3 log semua perubahan state sinyal yang diperintahkan ASCT; 3.0-1/2/3 log event dari external inputs, perubahan external output, nilai parameter aktual; 3.0-4 retensi XX; 3.0-5 arsip.

### D.17 Kategori requirement lain & metode verifikasi (hlm. 13, 58)
Tabel 1: functional (what), performance (how well), non-functional (under what conditions: reliability, safety, environmental), enabling (production, testing, training, support, deployment, disposal), constraints (technology, design, standards), interface, data. Metode verifikasi per requirement: **Demonstration** (tanpa alat uji eksternal), **Test** (dengan alat uji), **Analyze** (kesimpulan logis/matematis, mis. algoritma kongesti dari count & occupancy), **Inspection** (visual).

TSPH hlm. 78 melengkapi dengan struktur requirements Model SE Documents for CTSS (FHWA-HOP-19-019): 3.1.1 Access Control, 3.1.2 Security, 3.1.3 System Configuration, 3.1.4 Database Development, 3.1.5 Database Management, 3.1.6 Failure Events & Fallback, 3.1.7 Monitoring, 3.1.8 Control (termasuk TRPS), 3.1.9 Adaptive Operations, 3.1.10 Adaptive Advanced Controller Operation, 3.1.11 Adaptive Pedestrians, 3.1.12 Adaptive Special Functions, 3.1.13 Adaptive Detection, 3.1.14 Adaptive Railroad & EVP, 3.1.15 Adaptive Transit Priority, 3.1.16 Performance Measurement/Monitoring/Reporting, 3.1.17 External Interfaces, 3.1.18 Software, 3.1.19 Training, 3.1.20 Maintenance/Support/Warranty. Format kalimat: need = "The User needs to do something, somehow"; requirement = "The System shall do something, somehow" (hlm. 77–78).

---

## E. Verification & Validation

### E.1 Perbedaan dan penanggung jawab (MSE-ASCT hlm. 5, 14–15)
- **Verification** = sistem memenuhi semua requirement ("works as you intended"); umumnya dilakukan vendor, disaksikan & diaudit agensi; dijadwalkan bertahap (factory, submittal, pre-selection demo, installation), bukan hanya di akhir (hlm. 18).
- **Validation** = sejauh mana sistem mencapai *needs*/objectives ConOps ("extent to which transportation is improved"); tanggung jawab agensi, tidak dapat didelegasikan.
- Verification Plan **harus disiapkan sebelum RFP terbit dan sebelum kontrak ditandatangani**, dilampirkan ke RFP; test procedures disusun setelah sistem dipilih (hlm. 18). Untuk requirement mandatory yang belum pernah didemonstrasikan di agensi lain (mis. FYA), minta demonstrasi **sebelum** pemilihan (hlm. 18).

### E.2 Isi verification/validation case (hlm. 62, 65)
Nama & nomor; objective; daftar requirement (atau needs/scenarios) yang dicakup; data yang dicatat (expected results, rekaman pesan digital ke sistem eksternal); **pass/fail criteria**; konfigurasi HW/SW; asumsi & constraint. Validation case dapat mengelompokkan mis. "semua kontrol lalu lintas selama AM peak" (hlm. 65).

### E.3 Desain evaluasi before-after vs on-off (T414 hlm. 58, 60; NYSERDA hlm. 2, 17)
- **Before-after**: "before" saat TOD masih beroperasi, "after" setelah ASCT; jeda beberapa bulan; rentan variasi musiman dan perubahan volume → hasil bisa "unfair".
- **On-off**: keduanya setelah ASCT terpasang, adaptif ON vs background TOD OFF dalam musim sama; risiko bila background TOD tidak identik dengan plan asli. Kergaye dkk. (2010) di Park City: hasil lebih menguntungkan ASCT dengan on-off (NYSERDA hlm. 2).
- Distribusi metode (T414 hlm. 60–62): before-after sedikit lebih banyak daripada on-off; 25% evaluasi via simulasi (VISSIM 55%, CORSIM 18%, Paramics 9%); 2% "retroactive" (rata-rata timing adaptif dibandingkan satu plan TOD di Synchro). Perangkat pengumpulan: GPS probe (dominan), Jamar count boards/observasi manual untuk side-street delay, Bluetooth, wireless detectors, video; software PC-Travel, GPS Kit Pro, Tru-Traffic.
- Empirical Bayes before-after disarankan HSM untuk dampak keselamatan (NYSERDA hlm. 17).

### E.4 Ukuran kinerja (MOE)
- NYSERDA hlm. 16–18: route travel time (GPS probe atau vehicle re-identification; sample 2–14 run per NCHRP 398), travel time reliability (variabilitas TOD/DOW), delay (floating car, high-resolution phase/detector data 24 jam), traffic volume/throughput, derived MOE (fuel, emissions, B/C ratio, NPV). Tabel 7 (Gettman dkk. 2013): objectives smooth flow / access equity / throughput / reliability ↔ MOE: route travel time & delay, average speed, link travel time, stops per mile, **percent arrivals on green**, **platoon ratio**, green-occupancy ratio (min/max/SD), served v/c per movement, total volume, time to process equivalent volume, buffer time, planning time.
- T414 hlm. 63: MOE efisiensi (delay, travel time, stops, queue, split failure, side-street delay, transit travel time), lingkungan (fuel, HC/CO/NOx), keselamatan (crashes, conflicts); dilaporkan per periode (AM, midday, PM, Friday PM peak/special event, Saturday, weekday) dan per level (route, network).
- TSPH Tabel 46–48 (hlm. 226–229): health (comms uptime, % detektor berfungsi per mode, % sinyal offline, durasi offline, flash status, power failure, false preemption/priority); intersection (preemption/priority counts & durations, % cycles with unserved vehicles, split failures, phase termination gap-out/max-out, ped delay, queue exceeding storage, RLR); system (percent arrivals on green, platoon ratio, arrival type, **Purdue Coordination Diagram**, cyclic flow profile, time-space diagram, offset adjustment diagram, oversaturation severity index, travel time/speed/stopped delay, reliability: 95th percentile, buffer time/index, planning time/index). Detektor PCD ±400 ft di hulu stop bar (hlm. 230). Tabel 49 arrival type ↔ platoon ratio (≤0.5 very poor … >2.0 exceptional).

### E.5 Peringatan evaluasi
- "The classic example is the defense of traffic signal systems based on performance measures wholly related to improved timings without the recognition that improved timings can be implemented without a system" (TSPH hlm. 56) → validasi ITCS harus memisahkan manfaat retiming dari manfaat sistem.
- Hasil (AT)²C adalah rata-rata yang bisa menyembunyikan efek deployment tertentu; gunakan untuk tren, bukan vonis (T414 hlm. 63).

---

## F. Bukti Manfaat (T414, NYSERDA, EDC-1)

### F.1 Klaim umum (EDC-1 hlm. 1–2)
- ASCT memperbaiki travel time, control delay, emisi, fuel **≥10%**; pada timing yang sangat usang/kondisi jenuh **≥50%**; perbaikan kecil bila demand stabil, kinerja dipantau, timing terpelihara.
- Studi: crash dapat turun hingga 15% lewat perbaikan timing.
- Dipakai <1% simpang bersinyal AS; hambatan: biaya hardware, **keahlian konfigurasi & maintenance**, kurangnya performance measurement, mitos.
- ACS Lite: ≤30 sinyal, update tiap beberapa menit; sistem besar ratusan sinyal, second-by-second, terintegrasi central. SCOOT paling luas; SCATS mencocokkan pola ke pustaka plan & menskalakan split; RHODES peer-to-peer.

### F.2 Angka manfaat agregat (T414 hlm. 9–10, 63–64, 75–76)
- 85 studi evaluasi; manfaat efisiensi rata-rata (semua periode) **7,8% (number of stops) s.d. 85% (split failure)**; **side-street delay naik 3,4%**; transit travel time turun 2,8%; fuel 0,3–7%; emisi 0,1–9,8%; **crashes −35,1%**, conflicts −7,6%.
- Per AADT: manfaat lebih tinggi pada **AADT moderat 35.000–55.000** daripada >55.000 ("ATCSs work better in moderate traffic conditions than if traffic approaches saturation", hlm. 66).
- Per retiming pre-ATCS: manfaat lebih tinggi pada sinyal yang **moderately retimed (1–2 tahun)** daripada frequently retimed (≤1 tahun); 69% deployment sebelumnya tidak di-retime setiap tahun (hlm. 53, 67).
- Per kontrol pre-ATCS: semi-actuated → route delay −34,9%, stops −35,3%; fully actuated → −24,1%, −24,7%; fixed-time TOD → −16,6% s.d. −20% (mengejutkan, lebih rendah; hlm. 69–70). 67% deployment menggantikan TOD fully actuated (hlm. 52).
- Per area: suburban semua MOE membaik (travel time −8,8% s.d. stops −20%; emisi −3 s.d. −5,5%; fuel −3,7%; crashes −22,3%); urban: travel time/delay/stops −7,6% s.d. −19,9% tetapi **side-street delay +6%**; crashes −34% (hlm. 71).
- Per bentuk jaringan: single corridor (63% deployment) efisiensi +2,8% s.d. +85,5%, side-street delay +6,3%, fuel −1,2 s.d. −11,2%, emisi −2,4 s.d. −21,5%, crashes −14%; **two intersecting corridors: delay +7,1%, stops +24,6%** (dipengaruhi outlier +112%), network travel time −5,4%; mixed networks +5,1% s.d. +40,9% (hlm. 72–73).
- Per metode pengadaan: competitive bidding lebih baik untuk delay; sole-source lebih baik untuk travel time & stops (sistem sole-source cenderung memaksimalkan progression arus utama, mungkin mengorbankan kinerja jaringan) (hlm. 74).

### F.3 Angka per sistem (NYSERDA hlm. 5–15; Tabel 1 goal per sistem)
| Sistem | Tujuan operasional | Hasil lapangan yang dikutip |
|---|---|---|
| **SCOOT** | Minimize delay, dengan bobot stop | Toronto: delay −17%, stops −22%, fuel −5,7%, HC −5%; Roswell GA: 38 kamera + >60 sinyal, dipilih karena kongesti non-rekuren |
| **SCATS** | Minimize stops, delay, travel time; mengelola grup simpang | Oakland County MI (28 simpang): travel time −6,7%, stops −26,5%, queue −17,5%, delay −19%, fuel −5,1%, speed +7%; White Plains NY (50–60 ribu kend/hari): travel time −15%, stops −25% AM, stops −30% midday/PM; US-280 Alabama: travel time −6 s.d. −8 menit; Park City UT (14 simpang) membaik; cenderung cycle lebih panjang & memihak mainline (hlm. 8–9) |
| **QuicTrac** | Minimize delay/congestion, detektor sedikit | San Marcos Blvd CA: delay −46%, stops −39%, fuel −8% |
| **InSync** | Minimize queues & delay (AI + video) | Pinellas County FL: stops −37%, travel time −12%, delay −24%, emisi −16%, speed +12%, fuel −9%; Upper Merion PA: travel time −26%, stops −21%, delay −34%, speed +35%; CDOT: InSync menghemat $9,2 juta/20 tahun vs QuicTrac $5,7 juta |
| **ACS Lite** | Closed-loop, adjust split di atas plan TOD, stop-line detector per lajur, hemat biaya | Gahanna OH (deployment pertama); **Wolf Road Albany NY: delay simpang batas naik drastis, dalam koridor turun sedikit — efek "metering" + isu software** (hlm. 13–14) |
| **ACDSS** | Online simulation (AIMSUN), plug-in algoritma, data 30 detik | Midtown Manhattan 110 blok: speed +10%; Victory Blvd Staten Island (4 simpang): fuel −8%, stops −42%, delay −30%, speed +20%, throughput +7% |
| Brilon & Wietholt (Muenster, Jerman) | — | PI +30%; transit travel time −>20% dengan TSP |
| Slavin dkk. (SCATS+TSP, Portland) | — | SCATS tidak merugikan transit |

Distribusi merek di AS (T414 Tabel 3, hlm. 36): InSync 44 deployment (34 di database), SCATS 10, P2P 9, Centracs Adaptive 8, ACS Lite 6, SynchroGreen 5, SCOOT 4, D4 4, Intelight 4, OPAC 3, SURTRAC 2, LADOT ATCS 2, Transparity 17 (hanya 1 di database). Dari 33 ASCT, 31 menyesuaikan offset & split; cycle lebih jarang; **phase sequence paling jarang** (hlm. 50).

### F.4 Biaya
- T414 (hlm. 55–56, Tabel 12): instalasi rata-rata **$55.534/simpang** (min $2.000, maks $283.000); lisensi rata-rata **$10.252/simpang** (0–$56.000); maintenance rata-rata **$3.814/simpang/tahun** (300–21.660). 19/35 agensi: biaya maintenance ASCT ≈ sebelum; 11 lebih tinggi; 4 lebih rendah. Tidak ada korelasi merek–biaya maintenance.
- NYSERDA (hlm. 6, 19–20): $20.000–$80.000/simpang; centrally controlled $40.000–80.000; biaya mencakup licensing, warranty, training, support, hardware, maintenance; biaya SCOOT tinggi karena banyak detektor; **"most systems require at least one detector per lane per signal phase"**; 93% agensi memakai loop, 43% video, 18% radar; ~80% memakai twisted pair/telepon/fiber.
- T414 (hlm. 55): fiber paling umum, lalu twisted pair dan wireless; video detection paling sering, lalu loop dan radar; 37/55 memakai ≥2 teknologi deteksi; layout stop-line 34/36, mid-block sering, far-side paling jarang.

### F.5 Faktor keberhasilan/kegagalan
- **Decommissioning** (T414 hlm. 42–43): 78% fully operational, 10% partial (dipakai terbatas/bersama TOD), 10% partially decommissioned, 2% fully decommissioned. Penyebab utama: **masalah deteksi & komunikasi, ketidaksesuaian dengan ekspektasi agensi, masalah maintenance**.
- **Umur pakai** (hlm. 56–57): 42% ≤5 tahun, 42% 5–10 tahun, 12% 10–15; rata-rata ~6–7 tahun; 78% agensi mengharapkan 5–15 tahun → ekspektasi terlalu optimis; "institutional issues, more than outdated hardware and/or software, are the major barrier".
- **Workforce** (hlm. 36–37): 10/28 agensi butuh staf tambahan; kota kekurangan manajer/engineer/teknisi; ~30% agensi mengaku kurang memahami prinsip kerja ASCT-nya (hlm. 49). 48% agensi mengoperasikan >1 ASCT; bila merek berbeda, selalu dimonitor terpisah (hlm. 48–49).
- **Instalasi** (hlm. 41): 50% <3 bulan, 33% 3–12 bulan, 18% >1 tahun; keterlambatan (7/51) terutama masalah teknis (deteksi/komunikasi/peralatan) dan koordinasi vendor–agensi buruk.
- **Alasan implementasi** (hlm. 43): perbaikan arus urban (26), variabilitas lalu lintas (17), B/C tinggi (13), oversaturation & variabilitas harian (12); lainnya special events, funding, early adopter.
- **SE process** hanya 36% deployment (hlm. 59); 64% dipilih sole-source, 15% competitive bidding (hlm. 51).
- 65% agensi mengoperasikan 5–15 sinyal adaptif; hanya ~15% ≥30 sinyal → manfaat ASCT belum "terjual" ke agensi besar (hlm. 46). 64% deployment 2015–2019 terintegrasi high-resolution data; 15% V2I; 6% V2V (hlm. 48).
- Multimodal: fitur pejalan kaki paling dimanfaatkan; railroad & bicycle ~3% penuh; tidak dipakai 17% (ped) s.d. 31% (bike) (hlm. 47). Manfaat side-street, multimodal, dan keselamatan dinilai agensi kurang meyakinkan (hlm. 51).
- Peringatan MSE-ASCT (hlm. 4, 8): ASCT tidak mengatasi basic timing yang buruk; wajib backup plan berkualitas; bila agensi tidak sanggup memelihara sistem tradisional, jangan ASCT dulu.

### F.6 Kriteria decision tool (NYSERDA hlm. 19–21, 55–58)
- **Layer 1 Traffic analysis**: volume koridor, delay, travel time (reliability), road type (arterial through corridor), **signal spacing (ambang 0,5 mil ≈ 800 m)**, LOS. Adaptif direkomendasikan bila delay serius, travel time tidak reliabel, demand tinggi/variatif/tak terduga, insiden & special events sering; 80% agensi memasang di jaringan 30–45 mph; 42% arterial murni, 10% grid. Kasus Western Ave: LOS C, travel time reliabel ~12 menit → adaptif **bukan** pilihan terbaik.
- **Layer 2 Infrastructure analysis**: biaya; kebutuhan controller upgrade + pelatihan teknisi; deteksi (Western Ave perlu 200–300 detektor wireless); komunikasi (fiber/Wi-Fi belum ada) → "resources needed … are quite substantial".
- **Kuantitatif** (hlm. 53–54): kumpulkan volume, v/c, occupancy, event, weather beberapa bulan; petakan tiap titik data ke SVM (5 fitur, error <10%); tiap titik "vote" actuated vs adaptive; mayoritas menentukan. Batasan: korelasi bukan kausalitas; model dilatih hanya di Wolf Road; jangan jadi satu-satunya kriteria (hlm. 59–60).

---

## G. Manajemen Program (TSPH) — Relevan untuk Dishub

### G.1 Kerangka program & GcOST (hlm. 9–17)
Program sinyal = **program objectives** di pusat + empat elemen: management & administration; workforce/facilities/equipment; business processes; infrastructure/systems/technology (Figure 5). Proses **GcOST** (Goals → context → Objectives → Strategies → Tactics) + performance measures. Konteks (operasional: TOD, mode, event; fisik: land use, jaringan, cuaca; organisasi: kapabilitas) adalah "arguably the most important capability" (hlm. 11). Dua belas program objectives (hlm. 14–17): assign ROW safely; appropriate distribution of green; pedestrian & bicycle comfort; preferential service; smooth flow; maximize throughput; manage queues; respond to stakeholder needs; comply with policies/standards; minimize life-cycle costs; state of good repair; sustain systems & technology reliability. Agensi efektif: "avoid constructing infrastructure elements that they cannot maintain and operate" dan "measure and report results" (hlm. 1); agensi lemah memakai **komplain sebagai ukuran kinerja utama** (hlm. 9).

**Traffic Signal Management Plan (TSMP)** (hlm. 22–25): preliminary TSMP (baseline) → assessment (risk matrix) → action plan → implementation plans; template: executive summary, intro, program objectives, maintenance, operations, design, management & administration, action plan.

### G.2 Capability Maturity Framework (hlm. 27–29)
Empat level: 1 Developing (ad hoc, champion-driven) → 2 Established (proses terdokumentasi; risiko "fokus proses bukan outcome") → 3 Measured (efektivitas proses diukur; continuous improvement) → 4 Managed (optimasi, prioritas inti, kemitraan formal). Tiap kenaikan level mengurangi risiko tetapi menambah biaya kontrol proses.

### G.3 Staffing & workforce (hlm. 19–20, 47–56)
- Tabel 3: workforce — traffic engineer/manager, signal operations engineer, traffic analyst/technician, signal/electrical technicians, construction inspectors; equipment — MMU tester, controller test unit, test controller, simulation/timing software, **trouble ticket/recordkeeping system**, bucket trucks, spare controller, comms testers (TDR/OTDR); facilities — operations/comms center, **TMC**, maintenance shop, dispatch/radio room, secured storage.
- Workforce CMF: definisikan **core competencies** (definition, key behaviors, learning opportunities, proficiency level); job description selaras objectives; training & sertifikasi didanai; tracking training needs; succession planning (cross-training, leadership academy, mentorship); klarifikasi roles & responsibilities (procure comms/field upgrades, fine-tune timing, evaluate, O&M field equipment/timing plans, dokumentasi, data collection, batasan kapan timing boleh diubah); outsourcing yang lazim: desain/konstruksi, deteksi, preventive & emergency maintenance, komunikasi, timing plans, performance monitoring (hlm. 55–56).
- T414: ASCT butuh staf ahli; TSPH hlm. 208: "ASC systems require highly trained staff to monitor and sustain operations at peak performance"; kalibrasi ekstensif dan penyesuaian lapangan wajib.

### G.4 Maintenance & asset management (hlm. 40–47)
- Jenis: response/emergency maintenance; **preventive maintenance** (inspeksi, kalibrasi, pembersihan, pengujian) tahunan/semesteran per simpang; checklist (seal kabinet, wiring, breaker/load switch/relay, detection amplifiers & pushbutton, re-lamping, kerusakan struktur, filter, vegetasi, grafiti).
- Maintenance performance measures: emergency calls/simpang/tahun, lampu mati diganti, **average response time**, time to complete repair, % fixed with inventory parts, **% functioning detection sensors**, catatan per sinyal (teknisi, tanggal), jumlah perbaikan operasional.
- Kontrak maintenance: term, aktivitas (infrastruktur, penyesuaian timing, penggantian), **response time & performance expectations**, kompensasi, pelaporan, spare, peralatan, kualifikasi personel, asuransi.
- Asset management (NCHRP 632): operasi harian, identifikasi defisiensi, evaluasi opsi preservasi/peningkatan, alokasi anggaran; CMF Level 3 mensyaratkan **asset management system yang melacak life cycle** (hlm. 46); Level 4 memakai asset management, core competencies, life-cycle planning untuk keputusan investasi.
- Infrastruktur: resilience (quick-release bracket, LED, BBU/generator, **cyberlock kabinet** Utah DOT); **reduce design complexity** — jangan memasang sistem tercanggih bila sumber daya tidak cukup; gunakan capital funds untuk desain robust karena dana maintenance lebih langka (hlm. 33–35).

### G.5 Performance-based management & outreach (hlm. 56–59)
Laporan disesuaikan audiens: pengambil keputusan (ringkasan dampak & anggaran), engineer (teknis: offset/split, troubleshooting), teknisi junior (sistem otomatis yang mengidentifikasi masalah & solusi). Strategi: **ATSPM** (high-resolution logging 10 Hz; manfaat: safety, targeted maintenance, improved operations "address problems before they become complaints"), **real-time performance dashboards** (peta live, speed/congestion, kamera, tren reliabilitas per koridor/arah/bulan/jam/hari, alokasi sumber daya), **project benefit summaries** tahunan. CMF Level 4: performance measures menginformasikan anggaran, asset management, investasi teknologi.

### G.6 Procurement (MSE-ASCT hlm. 15–20; TSPH hlm. 254)
- Kompetitif ≠ low-bid; gunakan **RFP best-value**; vendor wajib menjelaskan *bagaimana* tiap requirement dipenuhi (bukan Yes/No); evaluasi akurasi jawaban, tingkat pemenuhan, dan keberterimaan metode; dua cara memperhitungkan biaya: cut-off anggaran atau utility-per-cost.
- RFI untuk requirement yang diragukan ketersediaannya; industry review of draft requirements (respons dirahasiakan); RFQ untuk kualifikasi vendor (stabilitas finansial, track record support/training, bukti sistem beroperasi) — bukan untuk memangkas beban evaluasi.
- Pisahkan bagian "intelligent" (central software, server, controller software → RFP) dari komponen fisik & konstruksi (→ low-bid) setelah sistem dipilih; bila terpaksa low-bid: masukkan requirements ke special provisions, wajibkan submittal kepatuhan dini dan acceptance test plan sebelum konstruksi.
- Market-research/low-bid approach "has been used for many of the adaptive installations whose final operation has not been satisfactory" (hlm. 18).
- Requirements diklasifikasikan **mandatory / desirable / optional**; optional menjaga jalur ekspansi masa depan.
- Sole source hanya bila unik memenuhi requirement atau harus sinkron dengan sistem eksisting; pilot proprietary tidak otomatis membenarkan perluasan.

### G.7 Komunikasi, standar & cybersecurity (TSPH Bab 7–8)
- Pertimbangan: throughput/bandwidth (video streaming mahal), **latency**, **reliability** (adaptif berbasis central & tampilan status real-time butuh komunikasi reliabilitas tinggi; database management boleh rendah), fixed path vs broadcast, leased line (hlm. 169–171). Uptime metric; demand ≤50% kapasitas throughput (hlm. 194–195).
- Arsitektur ARC-IT: P2P, C2F, C2C (hlm. 171–178). NTCIP: interoperability & interchangeability; daftar standar relevan — **NTCIP 1202 v03A (ASC)**, 1201 (global objects), 1210 (Signal System Masters), **1211 (Signal Control & Prioritization)**, 1205 (CCTV), 1206 (data collection), 2104/2202 (Ethernet/IP), 2301 (STMF), 9012 (testing C2F) (hlm. 190–192). Open protocol menurunkan life-cycle cost; proprietary mengunci vendor (hlm. 189).
- Security: **NEMA TS 8** (cyber & physical security ITS) untuk pengadaan; physical (kunci kabinet, alarm pintu terbuka, vandal resistant), personnel (permissions, akses TMC terbatas), network (berlapis), disaster preparedness (akses data bila TMC lumpuh), NCHRP 03-127 cybersecurity (hlm. 192–194). MSE-ASCT: ConOps 7.3 "adaptive processor/server will be protected within the agency's firewalls" (hlm. 151).
- System control (hlm. 197–213): fungsi central system per ARC-IT (remote manage, collect status & faults, manage/implement plans, boundaries, clock sync, adjust for priority/preemption, adapt real-time, sensor database); Tabel 41 tingkat kontrol & karakteristik implementasi (adaptif: ≥1–2 system detector per approach, komunikasi lebih cepat, deteksi per approach, maintenance deteksi lebih tinggi, controller mungkin perlu prosesor tambahan); Tabel 43 sensor web density level 3.0 untuk adaptif (downstream detection untuk release rate & flow profile, stop-bar demand, per-lane); empat lokasi detektor ASC (stop line ≤10 m — SCATS; 10–15 m hulu — BALANCE/MOTION; midblock — ACS Lite; far-side hulu — SCOOT/UTOPIA/RHODES) (hlm. 161, 208); Figure 61 arsitektur referensi CTSS (TMC: CTSS management system, ASCT adaptive processor, ATSPM; field: SSM opsional, controller, cabinet devices; external: CV back office, RSU, external devices) (hlm. 210).
- Advanced control (Bab 9): preemption (transfer kontrol; loss-of-life situations) vs priority (tanpa keluar koordinasi; NTCIP 1211); strategi TSP: green extension, red truncation/early green, phase insertion (queue jump), sequence change, phase skipping (Tabel 45); special event/incident timing butuh komunikasi ke pusat, central software, deteksi volume, video surveillance (hlm. 242); regional program (RTSOP) mencakup consistency, cross-jurisdictional timing, region-wide TSP, incident & severe weather plans, adaptive control (hlm. 243–244); CV: SAE J2735 BSM/SPaT/MAP, SPaT = konversi NTCIP 1202 (hlm. 245–247).

---

## H. Implikasi untuk Desain Aplikasi ITCS Jakarta

### H.1 Requirement kandidat

| ID | Requirement kandidat (draf, "shall") | Sumber |
|---|---|---|
| ITCS-NET-01 | Sistem shall mengendalikan minimum 321 simpang secara bersamaan dan mendukung ekspansi hingga ≥500 simpang tanpa perubahan arsitektur. | MSE-ASCT Req 1.0-1; T414 hlm. 46 (hanya 15% agensi ≥30 sinyal → skala Jakarta luar biasa besar) |
| ITCS-NET-02 | Sistem shall mendukung grup koordinasi (1–N simpang) yang batasnya dapat diubah oleh operator, jadwal TOD, dan kondisi lalu lintas terukur. | Req 1.0-2.x |
| ITCS-OBJ-01 | Sistem shall memungkinkan operator menetapkan objective per grup dan per periode (smooth flow / throughput / equity / queue management / isolated efficiency) dan mengubah objective otomatis saat kriteria kondisi terpenuhi. | Req 2.1.1.0-7.x; ConOps 3.4.4 |
| ITCS-ALG-01 | Sistem shall menerapkan batas min/max phase time, batas cycle (nilai/rentang), batas perubahan cycle & split antar siklus, dan batas frekuensi perubahan arah koordinasi yang ditetapkan operator. | Req 2.1.1.0-8, 2.2.0-5.0-x, 2.6.0-1..3 |
| ITCS-ALG-02 | Sistem shall mendeteksi repeated phase failure (repeated max-out / occupancy tinggi) dan menyesuaikan operasi. | Req 2.1.1.0-9 |
| ITCS-ALG-03 | Saat perubahan demand besar terdeteksi (insiden, event), sistem shall merespons lebih cepat dari operasi normal dalam batas operator (nilai "lebih cepat" harus didefinisikan kuantitatif). | Req 2.6.0-4 |
| ITCS-ALG-04 | Sistem shall menyediakan mode non-sequence-based dengan "maximum time between successive displays of each phase" untuk kondisi jenuh. | Req 2.3.0-4; App. C hlm. 168 |
| ITCS-QUE-01 | Sistem shall mendeteksi antrian pada lokasi terkonfigurasi (termasuk dari kamera AI) dan mampu metering/menyimpan antrian di lokasi yang ditentukan serta membatasi cycle grup. | Req 2.1.3.0-1..8; Need 4.5.x |
| ITCS-GW-01 | (Green wave) Sistem shall menghitung dan menerapkan offset untuk reference point setiap controller di rute koordinasi, memilih arah progression berdasar volume dominan, dan mempertahankan resonant cycle bila tersedia. | Req 2.2.0-4, 2.2.0-5.0-5; App. C hlm. 168 |
| ITCS-PRI-01 | Sistem shall menerima transit priority call dari detektor/OBU bus dan dari sistem eksternal (mis. TransJakarta), melayani via green extension / early green / exclusive phase dengan aturan user (waktu sejak priority terakhir, priority level), sambil operasi adaptif grup berlanjut. | Req 12.0-1..8; App. C hlm. 170; TSPH Tabel 45 |
| ITCS-PRI-02 | Logika kelayakan bus (schedule adherence, occupancy) shall berada di sistem transit; ITCS hanya menerima request terverifikasi. | App. C hlm. 170 |
| ITCS-PRE-01 | Sistem shall mempertahankan operasi adaptif di simpang non-preempted selama EV preemption dan resume adaptif otomatis setelah preemption dilepas; mendukung rute preemption terjadwal dari pos/markas dengan penundaan berbasis travel time. | Req 11.0-1..8; App. C hlm. 171 |
| ITCS-FB-01 | Sistem shall beralih ke operasi non-adaptif (TOD di central/lokal atau free) ketika: detektor tertentu gagal; jumlah detektor gagal per controller/grup melebihi ambang; link komunikasi gagal; adaptive processor gagal; kondisi terdefinisi (occupancy ekstrem) hadir; perintah operator; jadwal; perintah sistem eksternal — tanpa mengganggu arus. | Req 2.1.1.0-1..6; Need 4.14.0-1 |
| ITCS-FB-02 | Sistem shall menggunakan sumber data alternatif (detektor tetangga, data historis) secara real-time tanpa intervensi operator saat data detektor tidak valid. | Req 13.1.0-2.x |
| ITCS-FB-03 | Saat adaptive processor gagal, semua input detektor lokal shall tetap tersedia bagi controller lokal. | Req 13.3-4 |
| ITCS-FB-04 | Setiap controller shall menyimpan backup TOD plans berkualitas yang dipelihara berkala. | MSE-ASCT hlm. 4 |
| ITCS-ALM-01 | Sistem shall menerbitkan alarm ke penerima yang ditentukan dalam ≤ X menit sejak deteksi kegagalan (detektor, komunikasi, processor, pintu kabinet), dan meneruskannya ke sistem maintenance management. | Req 13.x-2/3; TSPH hlm. 193 |
| ITCS-LOG-01 | Sistem shall mencatat event ber-timestamp (calls kendaraan/pejalan kaki/EV/transit, awal-akhir fase, interval, transisi plan) dan semua perubahan state yang diperintahkan, dengan resolusi mendukung ATSPM (≥10 Hz). | Req 6.0-1, 18.0-3; TSPH hlm. 225 |
| ITCS-LOG-02 | Sistem shall menyimpan input algoritma (volume, occupancy, queue, phase utilization, arrivals on green, band efficiency) dan hasil perhitungan antara yang dipengaruhi parameter kalibrasi selama ≥ X hari, dan mengekspor ke CSV/SQL. | Req 6.0-4/5, 18.0-1/2 |
| ITCS-LOG-03 | Sistem shall menghitung dan melaporkan kualitas data relatif (sejauh mana data terpengaruh detector fault). | Req 6.0-8 |
| ITCS-RPT-01 | Sistem shall menyediakan laporan perbandingan (day-to-day, hour-of-week, day-of-year) dan laporan yang dapat dipahami publik/pejabat untuk menjelaskan perilaku sistem dan menjawab komplain (rekreasi kejadian historis). | Req 6.0-9/11; Need 4.11 |
| ITCS-KPI-01 | Sistem shall menghitung KPI operasional: percent arrivals on green, platoon ratio, split failures, gap-out/max-out, travel time & reliability (95th, buffer/planning index), queue length, stops, delay; KPI kesehatan: comms uptime, % detektor berfungsi, % sinyal offline, false preemption/priority. | TSPH Tabel 46–48; NYSERDA Tabel 7 |
| ITCS-SEC-01 | Sistem shall menerapkan security policy dengan role-based & jurisdiction-based access, logging & alerting keamanan, sesuai NEMA TS 8 dan kebijakan IT Dishub; server di balik firewall. | Req 5.0-1.x; TSPH hlm. 192–193 |
| ITCS-ACC-01 | Sistem shall dapat dimonitor/dikendalikan dari TMC, fasilitas maintenance, workstation LAN/WAN, TMC agensi lain (Polda/Korlantas, Kementerian), kabinet lokal, kendaraan maintenance, dan remote via internet dengan hak sesuai peran. | Req 5.0-2.x |
| ITCS-IF-01 | Sistem shall mendukung interface eksternal menurut Interface Control Document yang mendefinisikan information/application/lower layer protocol, agregasi, frekuensi simpan/lapor, durasi simpan — untuk ETLE, pajak kendaraan, uji emisi, transit, TMC lain. | Req 3.0-1 |
| ITCS-IF-02 | Sistem shall menerima dan menjalankan perintah dari sistem eksternal (cycle length, arah progression, strategi adaptif) dan beroperasi non-adaptif bila diperintahkan. | Req 3.0-1.0-6/7, 2.1.1.0-6 |
| ITCS-IF-03 | Interface controller shall memakai NTCIP 1202 (ASC), 1211 (SCP untuk priority), 1201, dengan protokol transport IP (NTCIP 2104/2202); pilihan controller tidak boleh dibatasi oleh perangkat lunak adaptif. | TSPH hlm. 190–191; ConOps 6.0-6.0-2 |
| ITCS-CTL-01 | Sistem shall tidak menghalangi fitur controller lokal (phase re-service, overlaps, variable sequence, omit, FYA, detector switching, timing sesuai kebijakan) dan mengakomodasi per-lane detection. | Req 7.0-x, 2.1.1.0-12 |
| ITCS-PED-01 | Sistem shall mengakomodasi waktu penyeberangan pejalan kaki selama adaptif, exclusive pedestrian phase, recall via TOD, dan early walk hingga X detik. | Req 8.0-x |
| ITCS-DET-01 | Sistem shall kompatibel dengan teknologi deteksi yang ditetapkan (kamera AI, radar, loop) dengan layout stop-line per lajur + advance/far-side untuk arrival profile; sensor density level 3.0. | Req 10.0-1; TSPH Tabel 43, hlm. 161 |
| ITCS-DET-02 | Sistem shall memantau kesehatan detektor (constant call, no actuation, anomali count) dan melaporkan % detektor berfungsi. | TSPH hlm. 224–226 |
| ITCS-SUP-01 | Vendor shall menyediakan pelatihan operasi, troubleshooting, PM, konfigurasi, administrasi, kalibrasi; update software X tahun; warranty X tahun; kontrak maintenance dengan response time. | Req 15–16 |
| ITCS-ENV-01 | Sistem shall menyediakan development/test server dan simulator untuk menguji timing/firmware/upgrade sebelum live. | ConOps Bab 7 hlm. 53–54 |
| ITCS-VER-01 | Setiap requirement shall memiliki metode verifikasi (Demonstration/Test/Analyze/Inspection) dan verification case; setiap need shall memiliki validation case; Verification Plan disertakan dalam RFP. | MSE-ASCT hlm. 18, 58–62 |

### H.2 Arsitektur referensi (sintesis)

Mengikuti Figure 61 TSPH (hlm. 210) dan Bab 5 MSE-ASCT:
- **Lapisan TMC**: (a) Central Traffic Signal System Management (database timing, monitoring, control, TOD/TRPS, clock sync, boundaries, alarm); (b) **Adaptive Processor/ASCT** (modul AI/optimasi, dapat per-wilayah/grup agar bagian jaringan merespons independen namun konsisten — App. C hlm. 172); (c) **ATSPM/performance engine** (high-resolution logs → KPI, PCD, dashboard, benefit summaries); (d) **Data warehouse/archive** (retensi, ekspor, rekreasi kejadian); (e) **Video wall/dashboard** (real-time map, CCTV, KPI audiens: pimpinan/engineer/teknisi); (f) **Security & access management** (RBAC per yurisdiksi, logging).
- **Lapisan lapangan**: controller NTCIP 1202 dengan backup TOD lokal & limited-service actuated mode; kabinet dengan sensor pintu; deteksi (kamera AI per lajur stop-line + advance/far-side; radar; loop) dengan diagnostik kesehatan; unit priority (NTCIP 1211) untuk bus/EV; opsional Signal System Master per grup untuk mengurangi beban komunikasi dan menjaga koordinasi saat link ke TMC putus.
- **Lapisan komunikasi**: fiber sebagai tulang punggung (paling umum, T414 hlm. 55), wireless/seluler sebagai redundansi; klasifikasi fungsi berdasarkan kebutuhan reliabilitas/latensi (adaptif central & status real-time = high reliability; database transfer = boleh rendah; video = bandwidth tinggi); uptime dipantau; NEMA TS 8.
- **Lapisan eksternal (C2C)**: sistem transit (priority request & AVL), dispatch EV/pos pemadam, ETLE/pajak/uji emisi (data kendaraan; hanya lewat ICD, bukan bagian logika adaptif), TMC lain/Polda, sistem informasi pengguna jalan, CV/RSU (SPaT/MAP) masa depan.
- **Fallback hierarchy**: adaptif → central TOD/TRPS → SSM/lokal TOD → free actuated → flash; transisi tanpa gangguan, otomatis, ter-log dan ter-alarm.

### H.3 Risiko utama & mitigasi

| Risiko | Bukti | Mitigasi |
|---|---|---|
| **Deteksi & komunikasi tidak andal** → penyebab utama decommissioning; kamera AI rentan cuaca/glare/occlusion. | T414 hlm. 42, 53; TSPH Tabel 29 hlm. 156 | Requirement kesehatan detektor & data-quality (Req 6.0-8), fallback berbasis ambang detektor gagal, redundansi sensor (kamera+radar), PM terjadwal, KPI % detektor berfungsi, kontrak maintenance dengan response time. |
| **Kapasitas SDM Dishub** (ASCT butuh staf ahli; 30% agensi tidak paham prinsip sistemnya; umur ASCT rata-rata 6–7 tahun karena isu institusional). | T414 hlm. 37, 49, 57; MSE-ASCT hlm. 8 | Core competencies & job descriptions, pelatihan kalibrasi, TSMP, succession planning, dukungan vendor multi-tahun, requirement 18.0-2 (nilai antara transparan) agar sistem bukan "black box". |
| **Skala 321 simpang jauh melampaui praktik umum** (65% agensi hanya 5–15 sinyal adaptif). | T414 hlm. 46 | Deployment bertahap per koridor/grup dengan validasi tiap tahap; arsitektur grup independen; pilot dengan experimental plan yang eksplisit (MSE-ASCT hlm. 20). |
| **Metering effect**: delay simpang batas meningkat (Wolf Road ACS Lite) dan side-street delay naik 3–6%. | NYSERDA hlm. 13–14; T414 hlm. 10, 71 | Objective equity di kawasan akses, KPI side-street delay & split failures, deteksi antrian di batas sistem, requirement crossing arterials/boundaries (Sec. 4). |
| **Manfaat lebih kecil pada kondisi mendekati jenuh** (AADT >55.000) dan pada sinyal yang sudah sering di-retime. | T414 hlm. 66–67 | Ekspektasi realistis dalam ConOps; strategi queue management/oversaturation (Sec. 2.1.3); ukur baseline dulu (on-off design). |
| **Procurement low-bid / market-research** menghasilkan requirement yang baru ditemukan saat acceptance. | MSE-ASCT hlm. 17–18 | RFP best-value dengan Verification Plan dalam RFP, demo pra-seleksi untuk requirement kritis (AI-camera adaptive, TSP), pemisahan software vs konstruksi. |
| **Vendor lock-in & protokol proprietary**. | TSPH hlm. 189 | NTCIP 1202/1211 wajib; server platform standar terpisah dari software; requirement technology-independent. |
| **Cybersecurity** (kabinet IP-addressable = pintu ke seluruh jaringan). | TSPH hlm. 192–193 | NEMA TS 8, kunci elektronik & alarm pintu kabinet, jaringan berlapis, disaster preparedness (akses data bila TMC lumpuh). |
| **Validasi tercampur dengan manfaat retiming**. | TSPH hlm. 56 | Desain evaluasi on-off + before-after, MOE per periode & per level, EB untuk keselamatan. |
| **Elemen AI yang belum matang** (needs belum lengkap). | TSPH hlm. 71 | Proses SE iteratif (prototype–evaluate–refine) khusus modul AI, sekuensial untuk komponen konvensional. |

---

## I. Kutipan Kunci (dengan halaman)

1. "Over the last two decades a significant number of adaptive systems have been deactivated well before the end of their useful life due either to a lack of adequate resources or agency capability to support system operation and maintenance, or in some cases a failure to properly align agency and system operations objectives." — MSE-ASCT, Executive Summary, hlm. 1.
2. "It is strongly recommended that ASCT systems not be procured using traditional low-bid process, because experience has shown that ASCT systems are complex and require sufficient integration and customization that they cannot be successfully treated as COTS purchases." — MSE-ASCT hlm. 2.
3. "Most adaptive control systems operate on top of or in conjunction with many of the most basic low level foundational traffic control settings. Therefore these systems cannot overcome the impact of poorly selected basic timing settings and parameters." — MSE-ASCT hlm. 4.
4. "Adaptive control is often marketed as eliminating the need for signal timing activities, but this is misleading… if an agency lacks the resources to operate and maintain a traditional system, then ASCT probably should not be considered until those resources can be provided in a sustainable way." — MSE-ASCT hlm. 8.
5. "A prime example of a constraint that is often initially (and incorrectly) identified as a requirement is the type of controller that will be used." — MSE-ASCT hlm. 7.
6. "Every element of all the other documents must be able to be traced to statements of need in the Concept of Operation." — MSE-ASCT hlm. 12.
7. "Validation is the responsibility of the agency, and cannot be delegated to the system supplier or vendor." — MSE-ASCT hlm. 15.
8. "[The verification plan] must be prepared before a formal RFP is issued and, regardless of procurement approach you have selected, before a contract is signed." — MSE-ASCT hlm. 18.
9. "The system operator needs to fall back to TOD or isolated free operation, as specified by the operator, without causing disruption to traffic flow, in the event of equipment, communications and software failure." — MSE-ASCT App. B Need 4.14.0-1 (hlm. 139).
10. "If the number of detector failures within a specified group exceeds a user-specified threshold, the system will cease adaptive operation and go to a fallback mode of time-of-day operation or free operation." — MSE-ASCT App. C, hlm. 172.
11. "The ASCT shall report all intermediate calculated values that are affected by calibration parameters." — MSE-ASCT App. D Req 18.0-2 (hlm. 261).
12. "The ASCT shall report stored data in a form suitable to provide explanations of system behavior to public and politicians and to troubleshoot the system." — Req 6.0-11 (hlm. 246).
13. "Reported average costs of ATCS installations are around $55,000 per intersection. Average costs of ATCS software licensing are around $10,000 (per intersection) and finally the average ATCS maintenance costs, per intersection per year, are approximately $4,000. In 36% of the deployments, system engineering analysis was conducted prior to an ATCS installation." — T414 hlm. 9–10.
14. "average benefits of ATCSs can be estimated (for efficiency-based performance measures) in a range from 7.8% (number of stops) to 85% (split failure)… they also report an increase in side-street delays for 3.4%… a number of crashes was decreased by 35.1%." — T414 hlm. 10.
15. "The main reasons for decommissioning the ATCS are: detection and communication problems, incompatibility of deployed ATCS with agency's expectations, and maintenance issues." — T414 hlm. 42.
16. "majority of the ATCS have been functional for less than 10 years with an average ATCS lifespan somewhere around 6-7 years… institutional issues, more than outdated hardware and/or software, are the major barrier to achieve a longer lifespan." — T414 hlm. 57.
17. "higher benefits were achieved on networks with moderate traffic (i.e., AADT is between 35,000 and 55,000) than on those with high traffic (AADT higher than 55,000)." — T414 hlm. 76.
18. "for a heavily congested corridor (such as the Wolf Road Corridor), ACS Lite can potentially improve traffic flow within its own system. However, this may be achieved by 'metering' (i.e., restricting) flow into the system, thereby generating large delays/problems at the boundary intersections." — NYSERDA hlm. 13–14.
19. "Adaptive traffic signal control may not be suitable for any given transportation corridor or intersections. Therefore, careful data collection and analysis should be conducted before deploying." — NYSERDA hlm. 59.
20. "Many studies have shown that adaptive signal control improves average performance metrics (travel time, control delay, emissions, and fuel consumption) by 10 percent or more. In systems with extremely outdated signal timing, and under saturated conditions, the improvement can be 50 percent or more." — EDC-1 hlm. 1.
21. "agencies that struggled to provide good basic service typically exhibited… Using complaints as the primary measure of performance." — TSPH hlm. 9.
22. "The classic example is the defense of traffic signal systems based on performance measures wholly related to improved timings without the recognition that improved timings can be implemented without a system." — TSPH hlm. 56.
23. "well-maintained, highly-reliable detection and communications systems are essential requirements of ASCs… ASC systems require highly trained staff to monitor and sustain operations at peak performance." — TSPH hlm. 208.
24. "Systems engineering succeeds when the requirements document is complete and correct. It is complete when it describes everything expected of the system…, and it is correct when the agency has confidence that a system exactly fulfilling the requirements (no more and no less) will meet their needs." — TSPH hlm. 79.
25. "If an unauthorized person gains access to the traffic control cabinet, they can access the IP network and therefore have access to the entire network." — TSPH hlm. 193.

---

*Catatan metodologis:* nomor halaman diturunkan dari penanda form-feed pdftotext; offset halaman cetak vs PDF dicantumkan di tabel sumber. Tabel-tabel numerik T414 (Tabel 15–35) berupa gambar dalam PDF sehingga tidak terekstraksi; angka yang dikutip diambil dari teks naratif Bab 6–7 dan Summary.
