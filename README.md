# IRAMA: Platform Manajemen & Kendali Lalu Lintas Kota (nama kerja)

Platform ATMS/ITCS untuk pemerintah daerah Indonesia yang dibangun bertahap dari CCTV yang sudah ada. Tahap awal mengubah rekaman CCTV menjadi hitungan lalu lintas per kelas kendaraan dan per arah (Vision Tracker), lalu menghasilkan rekomendasi waktu siklus dan waktu hijau menurut PKJI 2023 dengan LOS PM 96/2015 (Optimasi Waktu Simpang). Tahap berikutnya menambah deteksi kejadian dan pemantauan, kendali adaptif setara ITCS DKI dengan standar terbuka (RTSP/ONVIF, NTCIP 1202/1211, ONNX), dan akhirnya platform banyak kota. Patuh regulasi (UU 22/2009, PM 49/2014, PM 76/2021, UU PDP).

**Status (2026-09-14):** pra-perencanaan selesai dan direvisi. Fokus T2 adalah Vision Tracker dan Optimasi Simpang. Tidak ada pengadaan sampai T3 selesai: pekerjaan berjalan di laptop tim dengan perangkat lunak berlisensi bebas dan GPU gratis untuk pelatihan. Kota pilot Bandung (target ke-2 Surabaya). Lisensi open-core (inti Apache-2.0, modul komersial terpisah). Kode belum ada; planning rinci T1 menyusul.

## Tahapan
| Tahap | Nama kerja | Inti |
|---|---|---|
| T1 | Purwarupa Hitung dan Rekomendasi | satu simpang dari rekaman sampai rekomendasi dan dashboard dasar |
| T2 | Vision Tracker dan Optimasi Simpang | satu simpang lengkap; lima mode optimasi; wizard, dashboard tiga halaman, laporan, validasi SUMO, manfaat rupiah |
| T3 | Deteksi Kejadian dan Pemantauan Operasional | kejadian, kesehatan kamera, laporan wajib, controller baca-saja, uji lapangan |
| T4 | Kendali Adaptif Terpadu | pengadaan dimulai; kendali dan adaptif per simpang, koordinasi dasar, prioritas, integrasi instansi |
| T5 | Platform Mobilitas Kota | optimasi koridor dan jaringan, banyak kota, data terbuka |

## Mulai dari mana
1. `docs/kb/00_START_HERE.md`: panduan singkat dan urutan baca.
2. `docs/LOG_SESI.md`: log kronologis seluruh pekerjaan (wajib diperbarui setiap task).
3. `docs/planning/04` (tahapan), `15` (spesifikasi T2), `14` (arsitektur per tahap dan diagram alur data A01), `13` (data yang perlu disiapkan).
4. `docs/planning/01` bagian 8: Definisi Istilah dengan bahasa sehari-hari.

## Struktur
| Folder | Isi |
|---|---|
| `docs/kb/` | basis pengetahuan ringkas (glosarium, rumus, regulasi, kebutuhan, algoritma, model data, KPI, risiko, kota, keputusan) |
| `docs/planning/` | dokumen pra-perencanaan 01–16; `diagram/` berisi gambar alur F00–F12 dan A01 beserta skrip pembuatnya |
| `docs/sources/` | bahan acuan: regulasi, manual, jurnal, konteks kota, teks ekstraksi, catatan studi R00–R07 (PDF/gambar via Git LFS) |
| `docs/adr/` | Architecture Decision Records (template MADR; ADR-01…ADR-25 direncanakan di `docs/planning/06` §8) |
| `apps/ services/ edge/ sim/ packages/ infra/ tests/` | kerangka kode (kosong, ber-README) sesuai `docs/planning/10` §B |

## Catatan lisensi & hak cipta
Kode inti akan dilisensikan Apache-2.0 (lihat `LICENSE`); modul komersial akan berada di paket terpisah. Dependensi dipilih berlisensi permisif, dan lisensinya diperiksa otomatis di CI (ADR-25). Folder `docs/sources/` memuat salinan dokumen pihak ketiga (regulasi, manual, paper, arsip berita) **hanya untuk keperluan studi internal**. Repositori ini privat; jangan mendistribusikan ulang materi tersebut. Beberapa berkas kerja (versi docx/PDF dokumen planning dan catatan pribadi) sengaja hanya disimpan lokal melalui `.gitignore`.

## Cara kerja tim
- Setiap task dicatat sebagai entri `[T-xx]` di `docs/LOG_SESI.md`.
- Keputusan arsitektur lewat ADR (`docs/adr/`); keputusan produk & pertanyaan terbuka di `docs/kb/10_Keputusan_dan_Pertanyaan_Terbuka.md`.
- Konvensi ID: C-## (kepatuhan), KB-REQ-### (kebutuhan), K-## (algoritma), F-T#-## (fitur), ADR-##, D-/U-/Q-## (keputusan/pertanyaan).
