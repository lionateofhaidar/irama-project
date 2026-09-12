# IRAMA — Platform Manajemen & Kendali Lalu Lintas Kota (nama kerja)

Platform ATMS/ITCS untuk pemerintah daerah Indonesia: standar terbuka (NTCIP 1202/1211), bertahap (T1 MVP → T5 Platform Mobilitas Kota), terukur (ATSPM, PKJI 2023, LOS PM 96/2015), patuh regulasi (UU 22/2009, PM 49/2014, PM 76/2021, UU PDP), dan hemat server (edge-first, on-prem).

**Status:** pra-perencanaan selesai (2026-09-12); kota pilot: Bandung (target ke-2: Surabaya); lisensi: open-core (inti Apache-2.0, modul komersial terpisah). Kode belum ada — planning rinci menyusul.

## Mulai dari mana
1. `docs/kb/00_START_HERE.md` — panduan 5 menit + urutan baca.
2. `docs/LOG_SESI.md` — log kronologis seluruh pekerjaan (wajib diperbarui setiap task).
3. `docs/planning/09_Brief_Planning_Rinci.md` dan `10_Checklist_Pra-GitHub.md` — langkah berikutnya.

## Struktur
| Folder | Isi |
|---|---|
| `docs/kb/` | basis pengetahuan ringkas (glosarium, rumus, regulasi, kebutuhan, algoritma, model data, KPI, risiko, kota, keputusan) |
| `docs/planning/` | dokumen pra-perencanaan 01–13 |
| `docs/sources/` | bahan acuan: regulasi, manual, jurnal, konteks kota, teks ekstraksi, catatan studi R00–R06 (PDF/gambar via Git LFS) |
| `docs/adr/` | Architecture Decision Records (template MADR; ADR-01…ADR-18 direncanakan di `docs/planning/06` §7) |
| `apps/ services/ edge/ sim/ packages/ infra/ tests/` | kerangka kode (kosong) sesuai `docs/planning/10` §B |

## Catatan lisensi & hak cipta
Kode inti akan dilisensikan Apache-2.0 (lihat `LICENSE`); modul komersial akan berada di paket terpisah. Folder `docs/sources/` memuat salinan dokumen pihak ketiga (regulasi, manual, paper, arsip berita) **hanya untuk keperluan studi internal** — repositori ini privat; jangan mendistribusikan ulang materi tersebut.

## Cara kerja tim
- Setiap task dicatat sebagai entri `[T-xx]` di `docs/LOG_SESI.md`.
- Keputusan arsitektur lewat ADR (`docs/adr/`); keputusan produk & pertanyaan terbuka di `docs/kb/10_Keputusan_dan_Pertanyaan_Terbuka.md`.
- Konvensi ID: C-## (kepatuhan), KB-REQ-### (kebutuhan), K-## (algoritma), F-T#-## (fitur), ADR-##, D-/U-/Q-## (keputusan/pertanyaan).
