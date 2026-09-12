# 00 — START HERE (panduan melanjutkan pekerjaan di sesi lain)
Terakhir diperbarui: 2026-09-13 (keputusan user U-01…U-08 & Q-01…Q-11 diputuskan; repo GitHub `lionateofhaidar/irama-project`).

## 1. Dalam 5 menit: apa proyek ini
- Membangun **platform manajemen & kendali lalu lintas kota** (ATMS/ITCS) untuk pemda Indonesia, terinspirasi ITCS Dishub DKI (Majalah RPP "LANCAR-Jakarta", Syafrin Liputo, PKN II 2025) tetapi **tidak identik**: berbasis standar terbuka, bertahap (T1 MVP → T5 end-state), terukur, patuh regulasi, hemat server.
- Nama kerja: **IRAMA** (diputuskan sementara 2026-09-13; cek merek PDKI/domain masih wajib) — lihat `docs/planning/02`.
- Kota pilot: **Bandung** (basis personel); target ke-2 Surabaya; pasar: Medan, Palembang, Bodetabek (bukan DKI). Tim: 2 orang sampai T2 → pola simulation-first + mitra lapangan (KB-10 §B).
- Fase yang sudah selesai: (1) studi website acuan; (2) pengumpulan & studi bahan (±110 sumber); (3) basis pengetahuan ringkas; (4) dokumen pra-perencanaan. **Fase berikutnya: user membuat GitHub + planning rinci end-to-end** (brief di `docs/planning/09`).

## 2. Urutan baca untuk resume (murah → mahal)
| Langkah | File | Waktu | Isi |
|---|---|---|---|
| 1 | `docs/LOG_SESI.md` §2 & §3 akhir | 3 mnt | status terakhir, tindak lanjut |
| 2 | `docs/kb/10_Keputusan_dan_Pertanyaan_Terbuka.md` | 5 mnt | 20 keputusan tersirat (D-), 8 keputusan user (U-), 10 pertanyaan riset (Q-) — **kanonis** (file `docs/planning/08` punya penomoran D-/Q- sendiri untuk konteks pasar; bila bertentangan, ikuti file ini) |
| 3 | `docs/sources/_ringkasan/R00_Catatan_Studi_Utama.md` §K | 10 mnt | sintesis 7 pilar |
| 4 | `docs/planning/01` → `04` (termasuk §7b revisi) → `05` → `06` → `11`–`13` | 40 mnt | visi, tahapan, backlog fitur, arsitektur, pengadaan, kuesioner survei, kebutuhan data |
| 5 | `docs/kb/01–09, 11` sesuai kebutuhan | per topik | glosarium, rumus, regulasi, kebutuhan, algoritma, data, KPI, risiko, kota, sumber |
| 6 | `docs/sources/_ringkasan/R01–R06` | hanya bila perlu detail | catatan studi ±62.000 kata dengan rujukan halaman |
| 7 | `docs/sources/_teks_ekstraksi/*.txt` | grep saja | teks asli semua PDF |

## 3. Peta folder (struktur monorepo sejak 2026-09-13)
```
<repo>/
  README.md  LICENSE  .gitattributes (Git LFS: pdf/png/webp/jpg)  .gitignore
  docs/
    LOG_SESI.md                     ← log kronologis wajib (satu file, terus ditambah)
    kb/00–11                        ← basis pengetahuan ringkas (file ini ada di sini)
    planning/01–13                  ← visi, nama, pasar, tahapan, fitur, arsitektur, persona, asumsi, brief, checklist, pengadaan, kuesioner, kebutuhan data
    sources/                        ← Bahan Acuan (dulu `Bahan Acuan/`)
      README_INDEX.md               ← katalog semua sumber + workaround unduhan
      01_Regulasi_Indonesia/  02_Panduan_Praktis_Standar/  03_Jurnal_Akademis/
      04_Konteks_Jakarta_ITCS/  05_Website_Acuan_Majalah_RPP/  06_Simulasi_Tools_OpenSource/
      07_Konteks_Kota_Target/       ← riset kota target (Bandung, Medan, dst.)
      _teks_ekstraksi/              ← pdftotext semua PDF
      _ringkasan/R00–R06            ← catatan studi (R00 = bacaan langsung + verifikasi + sintesis)
    adr/  conops/  srs/             ← diisi saat planning rinci (template ADR sudah ada)
  apps/ services/ edge/ sim/ packages/ infra/ tests/ .github/   ← kerangka kode (kosong, ber-README)
```

## 4. Konvensi yang dipakai (ikuti agar konsisten)
- Bahasa Indonesia; istilah teknis Inggris dipertahankan.
- Tag sumber ringkas: `[R05 D.2]`, `[PM 49 Ps.14]`, `[PKJI 5-11]`, `[KB-03]`; asumsi ditandai `[A]`/[asumsi].
- ID: kepatuhan `C-##` (kanonis = R05 §G.1 = KB-03 §B; C-36…C-43 tambahan di KB-03); kebutuhan `KB-REQ-###` & constraint `KB-CON-##` (KB-04); kartu algoritma `K-##` (KB-05); fitur `F-T#-##` dalam epik `E##` (docs/planning/05); ADR `ADR-01…ADR-18` (docs/planning/06 §7, kanonis); keputusan `D-##`, `U-##`, `Q-##` (KB-10); risiko `R-##` (docs/planning/08) & register operasional (KB-08).
- Tahap (nama kerja kanonis = `docs/planning/04`): T1 MVP "Lihat & Kelola"; T2 siap jual "Kendali Terkoordinasi"; T3 transisi "Responsif"; T4 setara ITCS "Adaptif Terpadu"; T5 end-state "Platform Mobilitas Kota".
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
- Cyclic max-pressure: cycle/offset tetap, split adaptif, min green 7 s, perubahan ≤5 s/siklus; MP di 20–25% simpang kritis ≥ MP di semua; +perimeter control saat jenuh.
- TSP: green extension/early green 7–10 s (≤20), 1 aktivasi/siklus, lockout, recovery 1–2 siklus; kondisional berbasis headway/keterlambatan ≥2 mnt.
- EVP: preempt rata-rata 25 s; efek pulih 1 siklus; bertingkat hanya bila target respons terancam.
- ATSPM: log 0,1 s (kode Purdue/Indiana), split failure GOR & ROR5 ≥80%, watchdog (>90% max-out 01–05, <500 rekaman/hari, dsb.); ≈23 MB/simpang/hari.
- Hukum: pusat kendali SIK LLAJ dikelola Polri (UU Ps.247); override petugas (Ps.104); ETLE bukti (Ps.272; Perpol 2/2025: bukti dari perangkat lain wajib diverifikasi Polri; Back Office ETLE Polri); simpang jalan nasional → Dirjen/BPTJ; data milik Pemprov (Pergub 68); UU PDP untuk ANPR/CCTV.
- Belum ada RL-TSC yang pernah deployed; umur ASCT rata-rata 6–7 tahun karena isu institusional; penyebab decommissioning: deteksi, komunikasi, maintenance.

## 6. Workaround teknis yang terbukti di sesi ini
- FlipHTML5: buka viewer dengan Playwright (Python) → `window.fliphtml5_pages` berisi URL webp ter-hash; unduh dengan cookie + Referer.
- Situs 403 untuk curl: coba `page.request.get` Playwright (berhasil untuk ntcip.org); PDF regulasi Indonesia paling andal dari `peraturan.bpk.go.id/Download/<id>/...pdf` (id dari halaman Details).
- Perintah Bash sangat panjang (>~5 KB) gagal "unexpected EOF" → pakai Write tool / file daftar URL.
- `pdftotext -layout` untuk ekstraksi; grafik/tabel gambar tidak terekstraksi (catat sebagai "perlu digitalisasi").

## 7. Yang belum selesai / tindak lanjut (lihat KB-10 §C & LOG §2)
- Data lokasi ATCS Jakarta (portal timeout); NTCIP 1202 v03 & 1211; PM 67/2021; Pergub DKI turunan MRLL/ERP; Perdirjen tata cara waktu siklus; NCHRP Synthesis 403 (NAP login); metode klaim kinerja ITCS DKI; digitalisasi grafik PKJI (tipe O, FG, NqMAX) & Q-11 notasi Nq1.
- Erratum yang sudah dicatat di R0x (jangan bingung saat membaca): R05 §C "PM 76 tidak dapat dikaji" → usang, lihat R00 §C; R03 §C.2 kode hi-res kini terverifikasi tabel resmi Purdue (lihat KB-06 §C).
