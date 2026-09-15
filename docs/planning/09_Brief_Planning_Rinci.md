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
| Konsep tahapan T1–T5, exit criteria | `docs/planning/04` | revisi 2026-09-14 |
| Inventaris fitur per tahap (backlog awal) | `docs/planning/05` | revisi 2026-09-14 (179 fitur) |
| Arsitektur konseptual & opsi teknologi, daftar ADR | `docs/planning/06` | revisi 2026-09-14 (ADR-01 sampai ADR-25, diagram F00–F12) |
| Persona & stakeholder | `docs/planning/07` | draf |
| Asumsi, risiko, pertanyaan terbuka + default | `docs/planning/08` | draf |
| Checklist pra-GitHub | `docs/planning/10` | final, direvisi 2026-09-14 |
| Pengadaan per tahap (nol sampai T3) | `docs/planning/11` | revisi 2026-09-14 |
| Kuesioner survei perangkat dan rekaman | `docs/planning/12` | siap pakai, direvisi 2026-09-14 |
| Kebutuhan data per tahap | `docs/planning/13` | revisi 2026-09-14 |
| Arsitektur per tahap dan diagram alur data A01 | `docs/planning/14` | revisi 2026-09-14 |
| Spesifikasi Vision Tracker dan Optimasi Simpang (inti T2) | `docs/planning/15` | draf 2026-09-14 |
| Panduan data latih Vision Tracker | `docs/planning/16` | draf 2026-09-14 |
| Definisi istilah | `docs/planning/01` bagian 8 | 2026-09-14 |

## 2. Keputusan yang harus diambil user di awal planning (lihat `08` untuk default)
1. Nama produk (rekomendasi: IRAMA; cadangan NADI).
2. Kota/koridor pilot pertama dan mitra Dishub (rekomendasi: kota Bodetabek yang sudah punya ATCS dasar & dekat, atau Bandung karena urgensi TomTom #12).
3. Bangun controller sendiri atau integrasi saja (rekomendasi: integrasi; pusat + edge; controller dari vendor NTCIP).
4. Model lisensi: open-core vs proprietary; hosting on-prem vs cloud (rekomendasi: inti open-source lisensi permisif untuk adaptor/standar, modul bernilai jual proprietary; on-prem default untuk pemda).
5. Stack teknologi (rekomendasi awal di `06`; putuskan lewat ADR-02 sampai ADR-05 dan ADR-19 sampai ADR-25 menurut `06` bagian 8).
6. Tim & peran minimum (rekomendasi: 1 traffic engineer, 2 backend, 1 frontend, 1 edge/IoT, 1 data/ML paruh waktu, 1 PM/QA) [asumsi].
7. Entitas hukum, TKDN, pendanaan (di luar lingkup teknis; lihat `03`).

Status 2026-09-14: semua butir di atas sudah diputuskan (`docs/kb/10` bagian B dan B2). Ringkasnya: nama IRAMA; pilot Bandung; integrasi tanpa edge sampai T3, edge dan kendali mulai T4; open-core dan on-prem; stack di `06`; tim dua orang sampai T2; badan usaha dan TKDN mengikuti urutan di `11`.

## 3. Keluaran yang harus dihasilkan planning rinci
1. **ConOps** (template FHWA HOP-11-027 + struktur RPP LAN untuk audiens pemda): skenario operasi normal, jenuh, insiden, cuaca, event, kegagalan detektor/komunikasi/server, preemption, TSP.
2. **System Requirements Specification** dari `docs/kb/04_Katalog_Kebutuhan.md` (KB-REQ) → requirement final bernomor, traceable ke need & verification case; non-fungsional; constraint.
3. **Arsitektur & ADR** (daftar ADR di `06`): stack, model data (NTCIP-aligned), CAI/adaptor, pipeline ATSPM, digital twin, keamanan, multi-tenant, retensi data.
4. **Peta jalan T1–T5** dengan epik/fitur dari `05`, estimasi, dependensi, tim, dan definisi selesai per tahap; rencana rilis pilot.
5. **Rencana verifikasi & validasi**: uji akurasi Vision Tracker per kondisi, uji regresi PKJI terhadap contoh resmi, validasi SUMO (T2), uji lapangan sebelum-sesudah (T3); untuk kendali di T4: SIL (SUMO) → HIL/shadow → live off-peak; desain evaluasi on/off & before–after; KPI dari `docs/kb/07`.
6. **Rencana kepatuhan & tata kelola data**: matriks dari `docs/kb/03`; PDP (DPIA/kajian dampak, retensi ANPR/CCTV); perjanjian data (Polri, Bapenda, DLH, operator bus); kewenangan simpang jalan nasional.
7. **Rencana go-to-market pilot**: proposal ke Dishub (bahasa RPP/LAN), MoU, kriteria sukses pilot, jalur e-katalog/TKDN.
8. **Repo GitHub & fondasi rekayasa** (lihat `10`): struktur monorepo, CI, lint/test, ADR folder, docs site, issue templates, kebijakan keamanan, lisensi.
9. **Register risiko & asumsi** hidup (dari `08` dan `docs/kb/08`).
10. **Spesifikasi rinci modul T2** berangkat dari `15`: skema tabel, rantai PKJI 2023, mode optimasi, wizard konfigurasi, tiga halaman dashboard, laporan kajian.
11. **Rencana data dan pelatihan** dari `13` dan `16`: register sumber, klip latih dan uji, hitungan manual, target akurasi per kondisi.

## 4. Urutan kerja yang disarankan untuk sesi planning
1. Baca `docs/kb/00_START_HERE.md` → `R00 §K` → `04_Konsep_Tahapan` → `08` (jawab pertanyaan terbuka).
2. Tetapkan nama, pilot, model lisensi, stack (ADR-01 sampai ADR-05; sudah diputuskan user, tinggal ditulis sebagai ADR).
3. Tulis ConOps T1–T2 dulu (T3–T5 sebagai outline), lalu SRS T1–T2 lengkap.
4. Rancang skema tabel Vision Tracker dan mesin PKJI (ADR-20, ADR-21) untuk T1–T2; model data NTCIP, CAI, dan adaptor menyusul untuk T3–T4.
5. Susun backlog T1 dalam sprint; demo T1 adalah satu simpang dari rekaman sampai hitungan, rekomendasi, dan dashboard dasar (`04` bagian 2, `13`).
6. Buat repo (checklist `10`), pindahkan `docs/kb` & `Pra-Perencanaan` ke `docs/` repo (sudah dilakukan 2026-09-13).

## 5. Batas lingkup pra-perencanaan (apa yang TIDAK dilakukan di sini)
- Tidak ada estimasi biaya/jadwal absolut (hanya relatif & asumsi) — butuh keputusan tim & pendanaan.
- Tidak ada pemilihan vendor controller/kamera; hanya kriteria (NTCIP, sertifikasi PM 49 Ps.25, TKDN).
- Tidak ada kode; hanya prototipe konsep (opsional) di planning.
- Tidak ada validasi lapangan; semua angka kinerja berasal dari literatur & berita.
