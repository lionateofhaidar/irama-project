# 09 — Brief untuk Planning Rinci End-to-End
Tujuan file ini: menjadi "kontrak" antara fase pra-perencanaan (selesai) dan fase planning rinci (berikutnya). Semua masukan yang dibutuhkan planning sudah tersedia di folder yang dirujuk.

## 1. Masukan yang sudah tersedia (dan di mana)
| Masukan | Lokasi | Status |
|---|---|---|
| Kebutuhan bisnis & acuan (ITCS DKI) | `docs/sources/05_.../ANALISIS_MAJALAH_RPP_LANCAR-JAKARTA.md` | final |
| Sintesis pengetahuan 7 pilar | `docs/sources/_ringkasan/R00_Catatan_Studi_Utama.md` §K | final |
| Basis pengetahuan ringkas (glosarium, rumus, regulasi, kebutuhan, algoritma, data, KPI, risiko, kota, sumber, keputusan) | `docs/kb/00–11` | final (versi 1) |
| Detail per tema | `docs/sources/_ringkasan/R01–R06` | final |
| Visi & positioning, nama | `docs/planning/01`, `02` | draf untuk diputuskan |
| Pasar, kota target, pengadaan | `docs/planning/03` | draf |
| Konsep tahapan T1–T5, exit criteria | `docs/planning/04` | draf |
| Inventaris fitur per tahap (backlog awal) | `docs/planning/05` | draf |
| Arsitektur konseptual & opsi teknologi, daftar ADR | `docs/planning/06` | draf |
| Persona & stakeholder | `docs/planning/07` | draf |
| Asumsi, risiko, pertanyaan terbuka + default | `docs/planning/08` | draf |
| Checklist pra-GitHub | `docs/planning/10` | final |

## 2. Keputusan yang harus diambil user di awal planning (lihat `08` untuk default)
1. Nama produk (rekomendasi: IRAMA; cadangan NADI).
2. Kota/koridor pilot pertama dan mitra Dishub (rekomendasi: kota Bodetabek yang sudah punya ATCS dasar & dekat, atau Bandung karena urgensi TomTom #12).
3. Bangun controller sendiri atau integrasi saja (rekomendasi: integrasi; pusat + edge; controller dari vendor NTCIP).
4. Model lisensi: open-core vs proprietary; hosting on-prem vs cloud (rekomendasi: inti open-source lisensi permisif untuk adaptor/standar, modul bernilai jual proprietary; on-prem default untuk pemda).
5. Stack teknologi (rekomendasi awal di `06`; putuskan lewat ADR-001…).
6. Tim & peran minimum (rekomendasi: 1 traffic engineer, 2 backend, 1 frontend, 1 edge/IoT, 1 data/ML paruh waktu, 1 PM/QA) [asumsi].
7. Entitas hukum, TKDN, pendanaan (di luar lingkup teknis; lihat `03`).

## 3. Keluaran yang harus dihasilkan planning rinci
1. **ConOps** (template FHWA HOP-11-027 + struktur RPP LAN untuk audiens pemda): skenario operasi normal, jenuh, insiden, cuaca, event, kegagalan detektor/komunikasi/server, preemption, TSP.
2. **System Requirements Specification** dari `docs/kb/04_Katalog_Kebutuhan.md` (KB-REQ) → requirement final bernomor, traceable ke need & verification case; non-fungsional; constraint.
3. **Arsitektur & ADR** (daftar ADR di `06`): stack, model data (NTCIP-aligned), CAI/adaptor, pipeline ATSPM, digital twin, keamanan, multi-tenant, retensi data.
4. **Peta jalan T1–T5** dengan epik/fitur dari `05`, estimasi, dependensi, tim, dan definisi selesai per tahap; rencana rilis pilot.
5. **Rencana verifikasi & validasi**: SIL (SUMO) → HIL/shadow → live off-peak; desain evaluasi on/off & before–after; KPI dari `docs/kb/07`.
6. **Rencana kepatuhan & tata kelola data**: matriks dari `docs/kb/03`; PDP (DPIA/kajian dampak, retensi ANPR/CCTV); perjanjian data (Polri, Bapenda, DLH, operator bus); kewenangan simpang jalan nasional.
7. **Rencana go-to-market pilot**: proposal ke Dishub (bahasa RPP/LAN), MoU, kriteria sukses pilot, jalur e-katalog/TKDN.
8. **Repo GitHub & fondasi rekayasa** (lihat `10`): struktur monorepo, CI, lint/test, ADR folder, docs site, issue templates, kebijakan keamanan, lisensi.
9. **Register risiko & asumsi** hidup (dari `08` dan `docs/kb/08`).

## 4. Urutan kerja yang disarankan untuk sesi planning
1. Baca `docs/kb/00_START_HERE.md` → `R00 §K` → `04_Konsep_Tahapan` → `08` (jawab pertanyaan terbuka).
2. Tetapkan nama, pilot, model lisensi, stack (ADR-001–005).
3. Tulis ConOps T1–T2 dulu (T3–T5 sebagai outline), lalu SRS T1–T2 lengkap.
4. Rancang model data & CAI; buat prototipe adaptor SUMO (digital twin) sebagai target uji sebelum controller nyata.
5. Susun backlog T1 (MVP) dalam sprint; definisikan demo MVP (koridor 3–5 simpang di SUMO + data CCTV contoh).
6. Buat repo (checklist `10`), pindahkan `docs/kb` & `Pra-Perencanaan` ke `docs/` repo.

## 5. Batas lingkup pra-perencanaan (apa yang TIDAK dilakukan di sini)
- Tidak ada estimasi biaya/jadwal absolut (hanya relatif & asumsi) — butuh keputusan tim & pendanaan.
- Tidak ada pemilihan vendor controller/kamera; hanya kriteria (NTCIP, sertifikasi PM 49 Ps.25, TKDN).
- Tidak ada kode; hanya prototipe konsep (opsional) di planning.
- Tidak ada validasi lapangan; semua angka kinerja berasal dari literatur & berita.
