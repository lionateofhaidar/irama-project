# 01 — Visi Produk & Positioning
Status: draf pra-perencanaan (2026-09-12). Dasar: seluruh bahan di `docs/sources/` (ringkasan di `docs/kb/` dan `docs/sources/_ringkasan/R00` bagian K). Angka bertanda [asumsi] belum diverifikasi.

## 1. Masalah yang nyata di lapangan (bukan yang dibayangkan)
| Masalah | Bukti | Sumber |
|---|---|---|
| Pengaturan simpang statis: kaki simpang padat dapat hijau pendek, kaki sepi dapat hijau panjang | Pernyataan Kadishub DKI; 256 dari 321 simpang Jakarta masih ATCS statis | [R06 D.2], majalah h.4 |
| Kota-kota besar lebih macet dari Jakarta tetapi ATCS-nya masih tahap CCTV + koordinasi dasar | TomTom 2024: Bandung #12 dunia, Medan #15, Surabaya, Palembang di atas Jakarta (#90); Palembang 15 simpang terkoneksi; Bekasi ruang ATCS baru 2023 | riset [T-09], [KB-09] |
| Sistem adaptif sering "mati" karena detektor rusak, komunikasi putus, SDM & pemeliharaan, bukan karena algoritma | Umur ASCT rata-rata 6–7 tahun; alasan decommissioning = deteksi, komunikasi, maintenance; ATCS Makassar/Garut/multi-kota: peralatan rusak, dana, SDM | [R02 F.5], [R06 E.4] |
| Klaim manfaat tanpa ukuran kinerja yang terdefinisi → sulit dipertanggungjawabkan ke DPRD/publik | Klaim "+20–30%" tanpa MOE; DPRD DKI menanyakan dampak Rp7,15 T | [R06 D.1, D.6] |
| Waktu sinyal jarang ditinjau ulang padahal aturan mewajibkan (≥ tiap 3 bulan) dan retiming saja bernilai B/C 40:1 | Kep. Dirjen 273/1996; NCDOT; 69% deployment ASCT AS tidak di-retime tahunan | [R00 G], [R01 H.2], [R02 F.2] |
| Prioritas bus/darurat belum sistematis; detik prioritas "menyusut" tanpa perjanjian & log | TSP Handbook; PM 76/2021 Ps.7 & 11 mewajibkan prioritas bus/darurat | [R06 A.4, A.7], [R00 C] |
| Controller lapangan beragam & proprietary (RS-232), vendor lock-in | Diagram majalah (RS232 ke controller); TSPH: proprietary mengunci vendor; e-katalog LKPP penuh controller merek lokal | [R00 A], [R02 G.7], [T-09] |
| Data terpencar; single data transportasi belum ada; kewajiban data terbuka (UU 22/2009 Ps.250) belum terpenuhi | MTI Jakarta; Perda/Pergub soal integrasi data | [R06 D.6], [R05 A.6–A.7] |

## 2. Pernyataan visi
**Platform pengendalian lalu lintas kota yang terbuka, bertahap, dan dapat dipertanggungjawabkan: mulai dari "membuat sinyal yang ada bekerja dengan benar dan terukur", lalu bertahap menjadi kendali adaptif terkoordinasi setara ITCS, tanpa mengganti seluruh perangkat lapangan dan tanpa bergantung pada satu vendor.**

Nilai inti (urut prioritas):
1. **Berjalan di atas yang sudah ada** — integrasi ke controller/CCTV eksisting via adaptor (NTCIP untuk yang standar, RS-232 vendor untuk yang lama); pemda tidak harus membeli ulang.
2. **Fail-safe & sesuai aturan** — fallback ke rencana waktu lokal (≥8 plan, PM 49/2014), override petugas (UU 22/2009 Ps.104), preemption hak utama, kewenangan Polri dihormati, LOS PM 96/2015, PDP.
3. **Terukur, bukan diklaim** — ATSPM & KPI PKJI built-in; before–after on/off; laporan wajib (Forum LLAJ, Dirjen, Gubernur) otomatis.
4. **Hemat sumber daya** — edge-first, agregasi di tepi, retensi bertingkat; T2 dapat berjalan di satu server menengah [asumsi, lihat 06].
5. **Bertahap & bisa dibeli per tahap** — tiap tahap punya nilai sendiri dan definisi selesai yang terukur.
6. **Anti black-box** — setiap keputusan sistem menampilkan nilai antara dan alasannya (Req 18.0-2 HOP-11-027); AI/RL hanya sebagai penasihat lewat shadow mode sampai terbukti.
7. **Manusia di dalam loop** — operator, engineer, teknisi, dan petugas lapangan adalah pengguna utama, bukan objek otomatisasi.

## 3. Positioning
- **Untuk** Dinas Perhubungan kota/kabupaten/provinsi (dan UPT pengendali lalu lintas) yang sudah punya APILL/ATCS dasar dan CCTV tetapi belum punya kendali adaptif terukur,
- **produk ini adalah** sistem manajemen & kendali lalu lintas kota (ATMS/ITCS) berbasis standar terbuka,
- **yang** membuat sinyal eksisting bekerja lebih baik dalam hitungan minggu (T1–T2) dan bertumbuh menjadi kendali adaptif terkoordinasi dengan prioritas bus/darurat (T3–T5),
- **berbeda dari** ATCS vendor perangkat (terkunci pada controller mereka, KPI minim) dan dari sistem "AI" turnkey (mahal, black-box, bergantung deteksi kamera sempurna),
- **karena** dibangun di atas NTCIP/PKJI/PM 96, dengan mesin KPI dan fallback sebagai fitur utama, dan dijual bertahap.

## 4. Apa yang sengaja berbeda dari ITCS DKI (bukan tiruan)
| ITCS DKI (end-state) | Produk ini |
|---|---|
| Kamera AI vendor per kaki simpang sebagai satu-satunya deteksi | Deteksi berlapis: hitung dari CCTV eksisting, radar/loop bila ada, probe GPS, laporan manual; degradasi anggun bila satu sumber hilang |
| Nilai jual = "AI, digital twin 3D" | Nilai jual = sinyal yang benar, terukur, dan patuh aturan; AI menyusul sebagai penasihat |
| Satu vendor menyediakan lapangan + pusat | Pusat terbuka; lapangan dari vendor mana pun yang memenuhi spesifikasi (NTCIP wajib di pengadaan baru) |
| Fokus Jakarta (321 simpang, Rp120 M) | Multi-kota; mulai koridor 3–5 simpang; skala ke ratusan |
| Klaim kinerja tanpa MOE publik | Dashboard publik dengan metode yang dipublikasikan (UU Ps.250) |

## 5. Ringkasan tahapan (detail & exit criteria di `04_Konsep_Tahapan_1-5.md`)
| Tahap | Nama kerja | Inti nilai |
|---|---|---|
| T1 MVP | "Lihat & Kelola" | Inventaris simpang/APILL, peta status, plan manager TOD dengan kalkulator PKJI, integrasi CCTV eksisting, KPI dasar, log & tiket; bisa diuji di 1 koridor |
| T2 Siap jual | "Kendali Terkoordinasi" | Adaptor controller (NTCIP + 1–2 vendor RS-232), TMC console & override, health/watchdog, ATSPM dasar, laporan wajib, dashboard publik; server terbatas |
| T3 Transisi | "Responsif" | Green wave/offset tuning berbasis probe & Link Pivot, traffic-responsive plan selection, actuated, special-condition plans, digital twin SUMO per koridor |
| T4 Setara ITCS | "Adaptif Terpadu" | Cyclic max-pressure terkoordinasi di simpang kritis, perimeter control, TSP kondisional (AVL), EVP bertingkat, integrasi ETLE/pajak/emisi sebagai penyedia bukti, multi-tenant |
| T5 End-state | "Platform Mobilitas Kota" | Marketplace algoritma via shadow mode, RL advisor, integrasi TDM (ganjil-genap/ERP) berbasis data, data terbuka, analitik regional lintas-yurisdiksi (BPTJ) |

## 6. Prinsip "kreatif tapi berpijak"
Setiap ide baru harus lolos tiga uji: (1) ada bukti kebutuhan lapangan (keluhan, kendala terdokumentasi, kewajiban regulasi); (2) bisa diukur dampaknya dengan KPI yang sudah didefinisikan; (3) punya fallback bila gagal. Ide yang lolos masuk backlog `05_Inventaris_Fitur_per_Tahap.md`; yang belum lolos dicatat di `docs/kb/10_Keputusan_dan_Pertanyaan_Terbuka.md`.

## 7. Ukuran sukses produk (level program)
- Pemda pilot menaikkan LOS/menurunkan tundaan terukur (PM 96) dengan desain on/off — target awal ≥10% delay pada koridor pilot [asumsi dari EDC-1 "≥10%"].
- ≥95% ketersediaan komunikasi & ≥90% detektor sehat di simpang yang dikelola [asumsi; KPI kesehatan TSPH].
- Setiap perubahan waktu sinyal ter-log, ter-review ≤3 bulan (Kep. Dirjen 273/1996).
- Laporan wajib (Forum LLAJ/Dirjen/Gubernur) dihasilkan otomatis.
- Dapat dijual ke ≥1 kota di luar pilot pada T2 [asumsi].
