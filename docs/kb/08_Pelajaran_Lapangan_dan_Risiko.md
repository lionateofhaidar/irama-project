# 08 — Pelajaran Lapangan (Lessons) dan Register Risiko

**Cara pakai:** baca Bagian A sebelum menulis requirement/roadmap apa pun — tiap kartu = satu pelajaran yang terbukti di lapangan, buktinya, dan konsekuensi desain yang harus masuk ke tahap tertentu (T1 sampai T5 menurut `docs/planning/04`; kolom tahap diselaraskan pada 2026-09-15, nilai yang berubah ditandai "(dulu …)" menurut skema lama 2026-09-12). Bagian B = register risiko hidup; salin ke dokumen planning dan perbarui kolom Pemilik/Status. Tag sumber: `[R0x §..]` = catatan studi di `docs/sources/_ringkasan/`, `[07/...]` = arsip `07_Konteks_Kota_Target/`, `[04/...]` = arsip berita Jakarta. Angka hanya dikutip bila ada di sumber.

---

## A. Kartu Pelajaran

### A.1 Institusional & SDM
| # | Pelajaran | Bukti | Konsekuensi desain | Tahap |
|---|---|---|---|---|
| L-01 | Sistem adaptif mati bukan karena algoritmanya, tetapi karena institusi tidak sanggup mengoperasikan/memeliharanya | Umur ASCT rata-rata 6–7 tahun; 42% ≤5 th; "institutional issues … are the major barrier" [R02 F.5, T414 hlm.57]; 10% partial + 2% fully decommissioned [T414 hlm.42] | Produk harus **murah dioperasikan**: UI operator sederhana, runbook, pelatihan bawaan, kontrak dukungan; ukur "health" institusi sebagai KPI | T1–T5 |
| L-02 | ~30% agensi tidak paham prinsip sistem adaptifnya; 36% butuh staf tambahan | [R02 F.5, T414 hlm.37, 49] | Transparansi keputusan (nilai antara ditampilkan, Req 18.0-2), mode "jelaskan keputusan", pelatihan bertingkat (matriks Mampu/Mau RPP) | T2+ |
| L-03 | Wali kota menagih Dishub soal antrean; sensor adaptif tak kunjung dianggarkan | Surabaya: 136 simpang, baru **8 ATCS adaptif**, ideal ~400 unit; Eri Cahyadi minta sensor durasi dianggarkan 2025 [07/surabaya_sits_136…] | Nilai jual = **kemampuan adaptif yang terjangkau per simpang** + laporan yang bisa dibawa Kadishub ke wali kota | T2 (laporan kajian), **T4** (kemampuan adaptif) (dulu T2) |
| L-04 | Staf pelaksana bisa "mengembalikan" sistem ke fixed-time bila tidak paham/percaya | Kendala tipikal ATCS Indonesia [R06 E.4]; JMIA: peralatan rusak, SDM, dana [R06 E.3] | Audit trail mode kendali; alasan override wajib diisi; dashboard "berapa lama simpang berjalan adaptif" | **T4** (dulu T2+) |
| L-05 | Anggaran pemeliharaan APILL kota besar kecil dan diprotes DPRD bila lampu tetap rusak | Medan: pemeliharaan traffic light ±Rp3 M/tahun "dicukup-cukupkan" [07/medan_its_2020] | Modul pemeliharaan & bukti kinerja perangkat (uptime) = alat pertanggungjawaban Dishub ke DPRD | **T3** (dulu T1–T2) |
| L-06 | Hibah ATCS Kemenhub baru "diserahterimakan" bertahun-tahun setelah dipasang → celah pemeliharaan/operasional | Batam (BMN dipasang 2014–2019, BAST 2024); Bukittinggi (2019–2020, BAST 2022) [07/batam_antara…, 07/bukittinggi…] | Rancang integrasi/pengambilalihan aset eksisting (controller & CCTV hibah) sebagai jalur masuk; jangan asumsikan greenfield | T1 (CCTV eksisting), **T3–T4** (aset dan controller) (dulu T2–T3) |

### A.2 Deteksi, komunikasi, perangkat
| # | Pelajaran | Bukti | Konsekuensi desain | Tahap |
|---|---|---|---|---|
| L-07 | Deteksi & komunikasi tidak andal = penyebab #1 decommissioning | [R02 F.5, T414 hlm.42]; TSPH: "well-maintained, highly-reliable detection and communications … essential" [R02 kutipan 23] | Mutu rekaman dicatat sejak T1; health monitor kamera di T3, detektor dan komunikasi di T4; fallback otomatis ke TOD bila data stale (Req 2.1.1.0-2.x) sejak kendali tersambung di T4 | T1–T2 (mutu rekaman), **T3** (kesehatan kamera), **T4** (detektor, komunikasi, fallback) (dulu T1) |
| L-08 | Kamera terputus massal karena satu node/penghubung rusak (vandalisme, gangguan) | Bandung: ±20 kamera CCTV ATCS mati karena node controller dirusak (Pasteur–Tamansari, Mei 2026) [07/bandung_20_cctv…]; Cianjur: situs ATCS down karena gangguan jaringan/server; dari 77 kamera "ada beberapa yang mati" [07/cianjur…] | Topologi tanpa single point of failure per koridor; watchdog "no data"; alarm ke tiket; SLA perbaikan | **T3** (kamera dan tiket), **T4** (jaringan dan edge) (dulu T1–T2) |
| L-09 | Overestimasi antrean moderat lebih aman daripada underestimasi; state sederhana (count+phase) bisa mengalahkan citra mentah | [R04 A.2, Chen 2022 §4.2] | Kamera AI → keluaran terstruktur (count/occupancy/queue) bukan citra; bias konservatif | **T1–T3** (tabel hitungan dan antrian), T4 (detektor virtual) (dulu T2–T3) |
| L-10 | "Most systems require at least one detector per lane per signal phase"; biaya terbesar ASCT adalah detektor/komunikasi, bukan software | NYSERDA hlm.20; instalasi ≈US$55.500/simpang, lisensi ≈US$10.250, maintenance ≈US$3.800/th [R02 F.4] | Tahap MVP harus bekerja dengan **sensor minimal** (1 kamera/pendekat atau data eksisting); adaptif penuh di simpang kritis saja | T1–T3 |
| L-11 | Probe/GPS penetrasi 3–6% cukup untuk evaluasi & penalaan offset bila diagregasi multi-hari; tidak cukup untuk kendali detik-ke-detik (<20–30%) | [R04 A.19 Mahmud & Day; A.4/A.7] | Modul analitik koridor dari GPS bus/ojol/navigasi sebagai fitur murah (T5; GPS logger untuk offset dasar di T4); kendali real-time tetap dari sensor lokal | T4 (GPS logger untuk offset dasar), **T5** (analitik koridor) (dulu T2) |

### A.3 Algoritma & operasi
| # | Pelajaran | Bukti | Konsekuensi desain | Tahap |
|---|---|---|---|---|
| L-12 | Belum ada RL-TSC yang dideploy; distribution shift & non-stasioneritas | [R04 A.1, A.2] | RL hanya advisor/shadow mode; inti adaptif = heuristik (max-pressure siklik, Webster adaptif) | **T4** (mode bayangan), T5 (penasihat RL) (dulu T3–T5) |
| L-13 | MP di 10–25% simpang kritis memberi manfaat ≥ MP di 100% simpang; pada demand tinggi MP 100% ≈ 0 tanpa perimeter control | Tsitsokas: −14,5% (10%), −18,8% (25%), −10,6% (100%); PC+MP25% −15,6% [R04 A.5] | Pilih simpang kritis dengan skor (occupancy, varians, waktu ≥80% kapasitas); perimeter/gating untuk CBD | **T5** (dulu T3) |
| L-14 | Cycle & offset tetap + MP mengatur split, min green ≥7 s, perubahan ≤5 s/siklus | [R04 A.5] | Guard-rail bawaan mesin kendali | **T4** (batas perubahan per siklus), **T5** (max-pressure) (dulu T3) |
| L-15 | Prioritas bus tanpa syarat merusak lalu lintas umum; prioritas kondisional (occupancy/headway) aman | OCC-MP: mobil +0,36–2,64% vs RB-MP +3,5–25,8% [R04 A.6]; TSP Handbook: green extension/early green 7–10 s, 1 aktivasi/siklus, lockout [R06 A.4] | TSP kondisional dari AVL; detik prioritas tertulis di MoU | **T4** (berbasis aturan), **T5** (bersyarat) (dulu T3) |
| L-16 | ATCS tidak mengatasi DS ≥ 1: LOS tetap F | Makassar: setelah ATCS tundaan turun tetapi DS ≈1,1, LOS F [R06 E.1]; STM2: ASCT "cannot solve underlying capacity issues" [R01 D.1] | Komunikasikan batas; sediakan data untuk TDM/ERP; modul warrant kapasitas | T2+ |
| L-17 | Transisi plan adalah periode paling tidak efisien; retiming ≤3 tahun; hijau >30 s menurunkan arus jenuh | [R01 C.6, G, K] | Batasi frekuensi ganti plan; jadwal re-timing 3-bulanan (Dirjen 273/1996) / ≤3 th; peringatan hijau panjang | T2 (jadwal dan peringatan hijau panjang), **T4** (batas transisi) (dulu T2) |
| L-18 | Side-street delay bisa naik 3–6%; efek "metering" di simpang batas | [R02 F.2, NYSERDA Wolf Road] | KPI equity per pendekat; deteksi antrean di batas sistem | **T2** (kinerja per pendekat), **T4** (dampak adaptif pada jalan minor) (dulu T3) |
| L-19 | ATSPM adalah observer independen; "warning light" tanpa proses bisnis tidak berguna | [R03 C.5, HOP-20-002 p.16, p.29] | Alert → tiket kerja → verifikasi; pipeline ATSPM dipakai untuk lapangan & simulasi | **T3** (tiket dan metrik dari kamera), **T4** (ATSPM dari controller) (dulu T2–T3) |
| L-20 | Klaim manfaat harus dari before–after/on–off yang dirancang; jangan campur manfaat retiming dengan sistem | [R02 E.3, E.5]; klaim Jakarta +20–30% tanpa MOE [R06 D] | Modul evaluasi wajib sebelum publikasi angka | T2 |

### A.4 Hukum, tata kelola, komersial
| # | Pelajaran | Bukti | Konsekuensi desain | Tahap |
|---|---|---|---|---|
| L-21 | Pusat kendali SIK LLAJ dikelola Polri; operasional MRLL & penegakan hukum = Polri; Dishub = perlengkapan jalan & MRLL | UU 22/2009 Ps.7(2), 12, 247(3), 272 [R05 A.1] | Interkoneksi ke Polri wajib; ETLE hanya bukti; override petugas; jangan jual "tilang otomatis" | **T3** (bukti tanpa pelat), **T4** (interkoneksi Polri dan override) (dulu T2+) |
| L-22 | Simpang jalan nasional (BPTJ/Dirjen) butuh persetujuan | PM 96/2015 Ps.5(2); PM 76/2021 Ps.19 [R05, R00 C] | Atribut status jalan + workflow persetujuan | T1 (atribut), **T3** (alur persetujuan) (dulu T2) |
| L-23 | Data terintegrasi milik Pemprov; akses pihak ketiga perlu persetujuan; UU PDP untuk ANPR/pajak | Pergub 68/2021 Ps.10–11 [R00 D]; UU 27/2022 | Klasifikasi data, retensi, RBAC, DPIA | T2 (penyamaran, retensi, akun dan peran), **T3** (DPIA data Dishub) (dulu T2) |
| L-24 | Low-bid & "market research" menghasilkan ASCT yang tidak memuaskan; RFP best-value + verification plan dalam RFP | [R02 B, G.6] | Siapkan dokumen ConOps/requirements agar pemda bisa mengadakan dengan benar (bagian dari penawaran) | **T4** (dulu T2) |
| L-25 | TKDN menentukan keterjangkauan pasar pemerintah: prioritas TKDN+BMP >40% & TKDN >25% (Perpres 46/2025 Ps.66) | [07/tkdn_perpres46_cnbc] | Rencanakan sertifikasi TKDN software & perangkat; produk masuk e-katalog/INAPROC | **T3** (dulu T2) |
| L-26 | Kota memakai ATCS terutama untuk **pemantauan CCTV + teguran pengeras suara**, bukan kendali adaptif | Palembang 15 titik + speaker; Tangerang TPA; Bekasi 120 CCTV; KBB 129 kamera/50 titik Rp19 M; Kab. Bogor ITS 16 simpang [07/*] | Produk harus menyerap alur kerja ini (CCTV, tegur, pos petugas) sebelum menjual "AI adaptif"; di IRAMA alur ini masuk T3 (konsol pemantauan kejadian), sedangkan T1–T2 memakai CCTV yang sama untuk hitungan dan kajian waktu sinyal | **T3** (dulu T1) |
| L-27 | Pola pengadaan kota: bertahap (3 → 23 → 33 simpang), FS→DED dulu, hibah Kemenhub ±Rp2–4 M/simpang (Makassar 4 simpang Rp4,3 M) | [07/tangerangkab_23…, tangerang_33…, makassar…] | Harga per simpang harus jauh di bawah hibah; paket "FS/DED digital" sebagai layanan | T2 |

---

## B. Register Risiko

Skala: Kemungkinan (K) 1–5, Dampak (D) 1–5. Pemilik: PO = product owner, TL = tech lead, BD = bisnis/pemasaran, LG = legal.

| ID | Risiko | K | D | Mitigasi | Sumber | Pemilik |
|---|---|---|---|---|---|---|
| R-01 | Pemda tidak sanggup mengoperasikan/memelihara → sistem ditinggalkan dalam 2–5 tahun | 4 | 5 | Desain "operasi murah", pelatihan bawaan, kontrak dukungan/SaaS, KPI institusi, transisi bertahap | L-01, L-02, L-04 | PO |
| R-02 | Detektor/kamera/komunikasi tidak andal (cuaca, vandalisme, listrik) | 5 | 5 | Health monitor + fallback TOD otomatis + watchdog + redundansi jalur; SLA; desain tanpa SPOF | L-07, L-08 | TL |
| R-03 | Server/bandwidth terbatas di pemda (saat sistem dipasang di pemda mulai T4) | 4 | 3 | T1–T3 berjalan di laptop tim; mulai T4 edge memproses di simpang dan hanya mengirim agregat ke pusat; video on-demand bukan streaming terus; storage retensi terukur (~puluhan MB/simpang/hari hi-res) | R03 C.1; U-22 | TL |
| R-04 | Kewenangan Polri (pusat kendali, penindakan) memicu konflik/penolakan | 3 | 5 | Posisikan sebagai subsistem Dishub yang terinterkoneksi; fitur bukti, bukan tilang; MoU tiga pihak | L-21 | LG/BD |
| R-05 | Pelanggaran UU PDP (ANPR, pajak, emisi) | 3 | 5 | DPIA, minimisasi data, retensi, enkripsi, akses berbasis persetujuan Gubernur/Walikota | L-23 | LG |
| R-06 | Simpang jalan nasional tidak boleh diubah tanpa Dirjen/BPTJ | 4 | 3 | Atribut yurisdiksi; workflow persetujuan; mulai pilot di jalan kota/provinsi | L-22 | PO |
| R-07 | Vendor lock-in controller eksisting (protokol proprietary) menghambat integrasi | 4 | 4 | Controller Abstraction Interface; adaptor RS-232 vendor; syarat NTCIP di pengadaan baru; mode "pemantauan saja" bila kendali tidak tersedia | R03 D.2 | TL |
| R-08 | Produk kalah di e-katalog karena TKDN rendah / tidak terdaftar | 4 | 4 | Sertifikasi TKDN (software & perangkat), BMP, pendaftaran INAPROC, kemitraan pabrikan lokal (Javis/Qumicon) | L-25 | BD |
| R-09 | Low-bid memenangkan vendor murah tanpa kualitas; produk kita dibandingkan per unit kamera | 4 | 3 | Bantu pemda menyusun requirements/verification (best-value); jual outcome & layanan | L-24, L-27 | BD |
| R-10 | Klaim kinerja tidak terbukti → reputasi | 3 | 4 | Modul before–after/on–off bawaan; publikasi metode | L-20 | PO |
| R-11 | Algoritma adaptif memperburuk jalan minor/pejalan kaki | 3 | 4 | Guard-rail (min green, ped, max green ≤60 s, rate-limit), KPI equity, shadow mode | L-14, L-18 | TL |
| R-12 | RL/AI dijual berlebihan, gagal generalisasi | 3 | 4 | RL = advisor; heuristik sebagai inti; dokumentasi jujur | L-12 | PO |
| R-13 | Kapasitas jenuh (DS ≥1) → hasil kecil, pemda kecewa | 4 | 3 | Ekspektasi tertulis; warrant kapasitas; dukung TDM | L-16 | BD/PO |
| R-14 | Ketergantungan hibah/BMN yang belum diserahterimakan (aset abu-abu) | 3 | 3 | Inventaris aset & status BMN di onboarding | L-06 | BD |
| R-15 | Perubahan regulasi (Perpres PBJ, PM 76 turunan, Perpol ETLE) | 2 | 3 | Pantau JDIH; arsitektur modular untuk kepatuhan | R05 | LG |
| R-16 | Skala 321 simpang jauh melampaui praktik (65% agensi 5–15 sinyal) | 3 | 4 | Deployment per koridor/grup; arsitektur grup independen | R02 H.3 | TL |
| R-17 | Keamanan siber kabinet IP → akses jaringan pemda | 3 | 5 | NEMA TS 8, segmentasi, kunci kabinet, audit | R02 G.7 | TL |
| R-18 | Data probe/GPS bus tidak tersedia atau polling terlalu jarang untuk TSP | 3 | 3 | Fallback historis (mTransit-MP); polling ≤6 s di simpang rapat; MoU operator bus | R04 A.7, R06 F.2 | TL |

---

**Pointer ke detail:** R02 F–H (bukti manfaat/biaya/risiko ASCT), R06 D–F (konteks Jakarta, ATCS Indonesia, risiko), R04 B–F (kesiapan algoritma, guard-rail), R05 G.3 (larangan hukum), R03 C–D (ATSPM/health), `07_Konteks_Kota_Target/Teks_*.md` (bukti kota), KB 09 (profil kota), KB 10 (keputusan & pertanyaan terbuka).
