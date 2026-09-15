# 10 — Checklist Pra-GitHub & Fondasi Repo
Dipakai tepat sebelum/saat user membuat repositori. Centang berurutan.

## A. Keputusan yang harus final sebelum repo dibuat
- [x] Nama produk & nama repo: IRAMA (sementara), repo `lionateofhaidar/irama-project` — cek merek PDKI, domain, handle medsos **masih harus dilakukan**.
- [x] Lisensi: open-core (inti Apache-2.0 + modul komersial) — diputuskan (U-04); tulis ADR-01.
- [ ] Organisasi GitHub (bukan akun pribadi), 2FA wajib, kebijakan branch protection.
- [ ] Visibilitas: privat dulu; publikasi komponen open-source setelah audit lisensi dependensi.
- [x] Kota pilot: Bandung (U-02); sumber data uji: lihat `13_Kebutuhan_Data_per_Tahap.md` (rekaman terbatas satu simpang; video publik boleh untuk uji dan pelatihan; stream Dishub setelah MoU).
- [x] Stack awal diputuskan (U-05, dilengkapi 2026-09-14): Python/FastAPI, React + MapLibre + ECharts, PostgreSQL/PostGIS (TimescaleDB opsional), SUMO; Vision Tracker dengan FFmpeg/OpenCV, RF-DETR atau YOLOX lewat ONNX Runtime, ByteTrack/supervision, MediaMTX; MQTT dan agen edge Go mulai T4. Tulis ADR-02…ADR-06, ADR-10, ADR-19…ADR-25.

## B. Struktur repo yang disarankan (monorepo)
```
<nama>/
  docs/                      ← SUDAH DITERAPKAN 2026-09-13: kb/ (basis pengetahuan), planning/, sources/ (bahan acuan), adr/, LOG_SESI.md
    adr/  conops/  srs/  kb/  planning/  LOG_SESI (arsip)
  apps/
    tmc-web/                 ← formulir dan dashboard dasar (T1), wizard dan dashboard tiga halaman (T2), konsol pemantauan (T3), konsol kendali (T4)
    api/                     ← backend FastAPI: konfigurasi, rekaman, hitungan, rekomendasi, laporan, akun dan peran [T1]
  services/
    vision/                  ← Vision Tracker: bingkai, deteksi, pelacakan, hitung, hambatan samping, nyala lampu, antrian [T1–T2]; kejadian [T3]
    optimizer/               ← konversi SMP, kalkulator PKJI 2023/MKJI 1997, mode optimasi, periode, manfaat rupiah [T1–T2]
    reports/                 ← laporan kajian Word/PDF [T2]; laporan wajib [T3]
    metrics/                 ← metrik kinerja sinyal (ATSPM) [T3]
    cai/                     ← Controller Abstraction Interface + adaptor: baca-saja [T3], kendali [T4]
    priority/                ← PRS (TSP/EVP) [T4]
    adaptive/                ← actuated, TRPS, offset dasar, mode bayangan [T4]
    (health/, ticket/, evidence/ [T3]; network/, tdm/, advisor/ [T5] dibuat saat tahapnya dimulai)
  edge/                      ← agen edge (Jetson/IPC): Vision Tracker 24 jam, polling controller, buffer & heartbeat [T4]
  sim/                       ← jaringan SUMO satu simpang dari konfigurasi [T2], twin per simpang [T3], mode bayangan [T4]
  packages/                  ← skema data (OpenAPI/JSON Schema), templat CSV data, enumerasi PKJI/NTCIP/Indiana, util
  infra/                     ← docker-compose di laptop (T1–T3), MediaMTX untuk uji stream (T2), k3s (T4+), observability
  tests/                     ← unit, uji regresi PKJI, uji akurasi Vision Tracker, integrasi (SUMO), kontrak API
  .github/                   ← workflows CI, issue/PR templates, CODEOWNERS, SECURITY.md
  LICENSE  README.md  CONTRIBUTING.md  CHANGELOG.md
```
Catatan 2026-09-14: folder `services/kpi-pkji` diganti nama menjadi `services/optimizer` dan `services/atspm` menjadi `services/metrics` agar sama dengan dokumen 06 dan diagram alur; `services/vision` dan `services/reports` ditambahkan.

## C. Fondasi rekayasa hari pertama
- [ ] README: visi 1 paragraf (dari `01`), status tahap, cara menjalankan demo T1 (rekaman → hitungan → rekomendasi).
- [ ] `docs/adr/` dengan template MADR; tulis ADR-01 (lisensi) s.d. ADR-25 sesuai `06` §8; sebelum sprint 1 minimal ADR-01, ADR-02, ADR-03, ADR-15, ADR-19, ADR-20, ADR-21, ADR-22, ADR-25.
- [ ] CI: lint + unit test + build docker; pemeriksaan lisensi dependensi (ADR-25); uji regresi kalkulator PKJI terhadap contoh resmi; job "vision-smoke" menjalankan Vision Tracker pada klip pendek dan membandingkan hitungan dengan nilai acuan; job "sim-smoke" menjalankan SUMO satu simpang (mulai T2).
- [ ] Konvensi commit (Conventional Commits) & versi semantik; CHANGELOG.
- [ ] Issue templates: fitur (wajib mengisi "kebutuhan lapangan & bukti", "KPI", "fallback"), bug, riset.
- [ ] Project board dengan kolom per tahap T1–T5; impor backlog dari `05_Inventaris_Fitur_per_Tahap.md` (ID F-T#-##).
- [ ] SECURITY.md (pelaporan kerentanan), kebijakan rahasia (no secrets in repo; .env.example), dependabot.
- [x] `docs/kb/` adalah sumber kebenaran basis pengetahuan (folder lama `Bahan Acuan/_knowledge_base` dipindahkan ke sini saat restrukturisasi 2026-09-13; tidak ada salinan lain yang perlu disinkronkan).
- [ ] Skema data awal (OpenAPI + JSON Schema) untuk entitas T1–T2 (Simpang, Pendekat, Fase, Kamera, Rekaman, Hitung15m, HambatanSamping15m, StatusLampu, Periode, Rekomendasi) sesuai `06` §5 dan `15`; entitas NTCIP (Controller, Pattern, Detector, HiResEvent) dari `docs/kb/06` menyusul untuk T3–T4.
- [ ] Enumerasi: kelas kendaraan IRAMA dan pemetaannya ke PKJI/MKJI, mode kendali PM 49 (tetap/semi-adaptif/adaptif/terkoordinasi), LOS PM 96, kode event hi-res (tabel resmi Purdue 2012 di `docs/kb/06` bagian C, sudah terverifikasi sejak T-11).

## D. Data & aset yang perlu disiapkan sebelum sprint 1
- [ ] Rekaman satu simpang, klip latih, dan klip uji sesuai `13` dan `16`, dicatat di register sumber (video tidak masuk repo).
- [ ] Waktu lampu eksisting dan geometri simpang target (`13` D1.7, D1.8); contoh perhitungan resmi untuk uji regresi (`13` D1.9).
- [ ] Hitungan manual referensi untuk klip uji (`13` D1.5); jaringan SUMO satu simpang menyusul di T2.
- [x] Regulasi dan pedoman kunci (PM 49, PM 96, PM 76, PKJI 2023) sudah ada di `docs/sources/01_Regulasi_Indonesia/` beserta teksnya di `docs/sources/_teks_ekstraksi/`, di repositori privat dan hanya untuk studi internal; folder terpisah `docs/kb/regulasi/` tidak diperlukan.

## E. Hal yang harus disepakati dengan mitra pilot (non-teknis, paralel)
- [ ] Surat minat dan MoU Dishub menjelang T3: akses rekaman dan stream kamera, izin baca controller, uji lapangan sebelum-sesudah; DPIA (PDP).
- [ ] Peta yurisdiksi simpang pilot (provinsi/kota vs nasional → BPTJ/Dirjen).
- [ ] Kontak Ditlantas/Polres untuk prosedur override & (nanti) ETLE.
- [ ] Kriteria sukses pilot tertulis (tundaan dan LOS PM 96/PKJI, akurasi Vision Tracker, uji sebelum-sesudah; desain on/off saat kendali aktif di T4).
