# 00 — START HERE (panduan melanjutkan pekerjaan di sesi lain)
Terakhir diperbarui: 2026-09-14 (perubahan kritikal: T2 = Vision Tracker + Optimasi Simpang; nol pengadaan sampai T3; keputusan user U-09…U-29; dokumen planning 14 ditulis ulang, 15 dan 16 baru, Definisi Istilah di 01 bagian 8; repo GitHub `lionateofhaidar/irama-project`).

## 1. Dalam 5 menit: apa proyek ini
- Membangun **platform manajemen & kendali lalu lintas kota** (ATMS/ITCS) untuk pemda Indonesia, terinspirasi ITCS Dishub DKI (Majalah RPP "LANCAR-Jakarta", Syafrin Liputo, PKN II 2025) tetapi **tidak identik**: berbasis standar terbuka, bertahap (T1 Purwarupa sampai T5 Platform Mobilitas Kota), terukur, patuh regulasi, tanpa pengadaan sampai T3.
- Inti produk T1–T2: **Vision Tracker** (menghitung kendaraan per kelas dan per arah dari CCTV) + **modul Optimasi Waktu Simpang** (rekomendasi siklus dan hijau menurut PKJI 2023). Spesifikasi `docs/planning/15`, panduan data latih `16`, diagram alur data A01 di `14` bagian 1.
- Nama kerja: **IRAMA** (diputuskan sementara 2026-09-13; cek merek PDKI/domain masih wajib) — lihat `docs/planning/02`.
- Kota pilot: **Bandung** (basis personel); target ke-2 Surabaya; pasar: Medan, Palembang, Bodetabek (bukan DKI). Tim: 2 orang sampai T2 → pola recording-first: rekaman CCTV dan video publik diolah di laptop; stream Dishub setelah MoU (KB-10 §B dan §B2).
- Fase yang sudah selesai: (1) studi website acuan; (2) pengumpulan & studi bahan (±110 sumber); (3) basis pengetahuan ringkas; (4) dokumen pra-perencanaan. (5) revisi 2026-09-14 untuk fokus T2. **Fase berikutnya: planning rinci T1 dan pengumpulan rekaman sesuai `docs/planning/13`** (brief di `docs/planning/09`).

## 2. Urutan baca untuk resume (murah → mahal)
| Langkah | File | Waktu | Isi |
|---|---|---|---|
| 1 | `docs/LOG_SESI.md` bagian status terakhir (saat ini §9) | 3 mnt | status terakhir, tindak lanjut |
| 2 | `docs/kb/10_Keputusan_dan_Pertanyaan_Terbuka.md` | 5 mnt | 20 keputusan tersirat (D-), keputusan user U-01…U-29 (§B dan §B2), pertanyaan riset Q-01…Q-15 — **kanonis** (file `docs/planning/08` punya penomoran D-/Q- sendiri untuk konteks pasar; bila bertentangan, ikuti file ini) |
| 3 | `docs/sources/_ringkasan/R00_Catatan_Studi_Utama.md` §K | 10 mnt | sintesis 7 pilar |
| 4 | `docs/planning/01` (termasuk Definisi Istilah §8) → `04` → `15` → `16` → `14` → `05` → `06` → `11`–`13` | 60 mnt | visi, istilah, tahapan, spesifikasi T2, data latih, arsitektur per tahap, backlog fitur, arsitektur dan lisensi, pengadaan, kuesioner survei, kebutuhan data |
| 5 | `docs/kb/01–09, 11` sesuai kebutuhan | per topik | glosarium, rumus, regulasi, kebutuhan, algoritma, data, KPI, risiko, kota, sumber |
| 6 | `docs/sources/_ringkasan/R01–R07` | hanya bila perlu detail | catatan studi ±62.000 kata dengan rujukan halaman; **R07** = regulasi Bandung/Jabar/ERP DKI, rumus Purdue (POG, platoon ratio, Link Pivot), data & kandidat koridor pilot Bandung |
| 7 | `docs/sources/_teks_ekstraksi/*.txt` | grep saja | teks asli semua PDF |

## 3. Peta folder (struktur monorepo sejak 2026-09-13)
```
<repo>/
  README.md  LICENSE  .gitattributes (Git LFS: pdf/png/webp/jpg)  .gitignore
  docs/
    LOG_SESI.md                     ← log kronologis wajib (satu file, terus ditambah)
    kb/00–11                        ← basis pengetahuan ringkas (file ini ada di sini)
    planning/01–16                  ← visi (+ Definisi Istilah), nama, pasar, tahapan, fitur, arsitektur, persona, asumsi, brief, checklist, pengadaan, kuesioner, kebutuhan data, arsitektur per tahap, spesifikasi T2, panduan data latih
    planning/diagram/               ← make_diagrams.py + gambar F00–F12 (alur fitur) dan A01 (alur data CCTV → keputusan)
    planning/docx/                  ← versi docx/PDF lokal (di .gitignore, tidak dipush)
    sources/                        ← Bahan Acuan (dulu `Bahan Acuan/`)
      README_INDEX.md               ← katalog semua sumber + workaround unduhan
      01_Regulasi_Indonesia/  02_Panduan_Praktis_Standar/  03_Jurnal_Akademis/
      04_Konteks_Jakarta_ITCS/  05_Website_Acuan_Majalah_RPP/  06_Simulasi_Tools_OpenSource/
      07_Konteks_Kota_Target/       ← riset kota target (Bandung, Medan, dst.)
      _teks_ekstraksi/              ← pdftotext semua PDF
      _ringkasan/R00–R07            ← catatan studi (R00 = bacaan langsung + verifikasi + sintesis); R08 catatan lokal naskah tugas akhir (tidak dipush)
    adr/  conops/  srs/             ← diisi saat planning rinci (template ADR sudah ada)
  apps/ services/ edge/ sim/ packages/ infra/ tests/ .github/   ← kerangka kode (kosong, ber-README)
```

## 4. Konvensi yang dipakai (ikuti agar konsisten)
- Bahasa Indonesia; istilah teknis Inggris dipertahankan.
- Tag sumber ringkas: `[R05 D.2]`, `[PM 49 Ps.14]`, `[PKJI 5-11]`, `[KB-03]`; asumsi ditandai `[A]`/[asumsi].
- ID: kepatuhan `C-##` (kanonis = R05 §G.1 = KB-03 §B; C-36…C-43 tambahan di KB-03); kebutuhan `KB-REQ-###` & constraint `KB-CON-##` (KB-04); kartu algoritma `K-##` (KB-05); fitur `F-T#-##` dalam epik `E##` (docs/planning/05); ADR `ADR-01…ADR-25` (docs/planning/06 §8, kanonis); keputusan `D-##`, `U-##`, `Q-##` (KB-10); risiko `R-##` (docs/planning/08) & register operasional (KB-08).
- Tahap (nama kerja kanonis = `docs/planning/04`, revisi 2026-09-14): T1 Purwarupa Hitung dan Rekomendasi; T2 Vision Tracker dan Optimasi Simpang; T3 Deteksi Kejadian dan Pemantauan Operasional; T4 Kendali Adaptif Terpadu; T5 Platform Mobilitas Kota. Nama lama ("Lihat & Kelola", "Kendali Terkoordinasi", "Responsif") tidak berlaku lagi.
- Istilah sulit dijelaskan dengan bahasa sehari-hari di `docs/planning/01` §8.
- LOS memakai PM 96/2015; rumus PKJI 2023; antarmuka NTCIP 1202/1211; fallback ≥8 plan TOD.
- Setiap task baru → tambah entri `[T-xx]` di `LOG_SESI.md`.

## 5. Fakta kunci yang sering dibutuhkan (cheat-sheet)
- Jakarta: 321 simpang prioritas, 65 ber-ITCS (2025), 25 dikontrak Rp120 M; klaim +20–30%; TomTom 2023 #30 → 2024 #90 (53%→43%).
- TomTom 2024 Indonesia: Bandung #12 dunia, Medan #15, lalu Surabaya, Palembang, Jakarta.
- LOS simpang PM 96: A<5, B5–15, C15–25, D25–40, E40–60, F>60 s/kend. Target Perda DKI: 35 km/jam & 60% angkutan umum; Perpres 55/2018: 30 km/jam (2029).
- ATCS syarat PM 96: ≥3 simpang, jarak ≤1 km, detektor + komunikasi + control centre room.
- PM 49/2014: ≥8 rencana siklus; pemeliharaan ≥6 bulan; umur teknis ≤5 tahun; perangkat TI bersertifikat.
- SK.7234/2013 controller: ≥8+8 signal group (hingga 32), ≥4–16 program, 10 plan/hari, conflict → flashing, manual override, detektor ≥4 zona gap/occupancy, DIS RS-485.
- Webster/PKJI: s = (1,5·wHH + 5)/(1 − RAS); siklus 40–130 s; kuning 3 s; DJ ≤ 0,85.
- Cyclic max-pressure (T5): cycle/offset tetap, split adaptif, min green 7 s, perubahan ≤5 s/siklus; MP di 20–25% simpang kritis ≥ MP di semua; +perimeter control saat jenuh.
- TSP: green extension/early green 7–10 s (≤20), 1 aktivasi/siklus, lockout, recovery 1–2 siklus; kondisional berbasis headway/keterlambatan ≥2 mnt.
- EVP: preempt rata-rata 25 s; efek pulih 1 siklus; bertingkat hanya bila target respons terancam.
- ATSPM: log 0,1 s (kode Purdue/Indiana), split failure GOR & ROR5 ≥80%, watchdog (>90% max-out 01–05, <500 rekaman/hari, dsb.); ≈23 MB/simpang/hari.
- Hukum: pusat kendali SIK LLAJ dikelola Polri (UU Ps.247); override petugas (Ps.104); ETLE bukti (Ps.272; Perpol 2/2025: bukti dari perangkat lain wajib diverifikasi Polri; Back Office ETLE Polri); simpang jalan nasional → Dirjen/BPTJ; data milik Pemprov (Pergub 68); UU PDP untuk ANPR/CCTV.
- Belum ada RL-TSC yang pernah deployed; umur ASCT rata-rata 6–7 tahun karena isu institusional; penyebab decommissioning: deteksi, komunikasi, maintenance.
- EMP PKJI 2023 simpang APILL: MP 1,00; KS 1,30; SM 0,15 terlindung / 0,40 terlawan; KTB tidak dikonversi (masuk RKTB untuk FHS).
- Hambatan samping PKJI 2023: pejalan kaki 0,5; berhenti/parkir 1,0; keluar-masuk 0,7; kendaraan lambat 0,4, per 200 m per jam → KHS SR <100, R 100–299, S 300–499, T 500–899, ST ≥900.
- Akurasi Vision Tracker: sekitar 90% siang dan 85% malam/hujan di T1–T2; 95% dan 90% mulai T3; rumus 1 − Σ selisih mutlak / Σ hitungan manual.
- Laptop tim: Ryzen 7 7730U 8 inti, RAM 32 GB, grafis terintegrasi (tanpa NVIDIA), ruang kosong ±249 GB; rekaman 1080p ≈ 1,5–2 GB per jam per kamera.
- Lisensi dilarang: Ultralytics YOLO (AGPL), Redis versi baru (RSAL/SSPL/AGPL), EMQX (BSL); Grafana/Loki hanya sebagai alat terpisah tanpa modifikasi.

## 6. Workaround teknis yang terbukti di sesi ini
- FlipHTML5: buka viewer dengan Playwright (Python) → `window.fliphtml5_pages` berisi URL webp ter-hash; unduh dengan cookie + Referer.
- Situs 403 untuk curl: coba `page.request.get` Playwright (berhasil untuk ntcip.org); PDF regulasi Indonesia paling andal dari `peraturan.bpk.go.id/Download/<id>/...pdf` (id dari halaman Details).
- Perintah Bash sangat panjang (>~5 KB) gagal "unexpected EOF" → pakai Write tool / file daftar URL.
- Diagram alur: ubah data di `docs/planning/diagram/make_diagrams.py` lalu jalankan ulang; panah dirutekan siku otomatis dan skrip juga menghasilkan potongan markdown untuk 06 dan 14.
- Versi docx/PDF: `docs/planning/docx/build_docx.py` (lokal, tidak dipush); sumber sederhana di `docs/planning/docx/src/`.
- Jam di log sesi harus diambil dari jam sistem (`date`), bukan diperkirakan (koreksi di LOG T-43).
- `pdftotext -layout` untuk ekstraksi; grafik/tabel gambar tidak terekstraksi (catat sebagai "perlu digitalisasi").

## 7. Yang belum selesai / tindak lanjut (lihat KB-10 §C & LOG §2)
- Terbaru (2026-09-14): user menyiapkan rekaman sesuai `docs/planning/13` (register sumber, rekaman satu simpang, klip latih dan uji, hitungan manual, geometri, waktu lampu eksisting); planning rinci T1; ADR-19…ADR-25; Q-12…Q-15 di KB-10.
- Data lokasi ATCS Jakarta (portal timeout); NTCIP 1202 v03 & 1211; PM 67/2021; Pergub DKI turunan MRLL/ERP; Perdirjen tata cara waktu siklus; NCHRP Synthesis 403 (NAP login); metode klaim kinerja ITCS DKI; digitalisasi grafik PKJI (tipe O, FG, NqMAX) & Q-11 notasi Nq1.
- Erratum yang sudah dicatat di R0x (jangan bingung saat membaca): R05 §C "PM 76 tidak dapat dikaji" → usang, lihat R00 §C; R03 §C.2 kode hi-res kini terverifikasi tabel resmi Purdue (lihat KB-06 §C).
