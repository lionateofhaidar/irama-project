# 10 — Checklist Pra-GitHub & Fondasi Repo
Dipakai tepat sebelum/saat user membuat repositori. Centang berurutan.

## A. Keputusan yang harus final sebelum repo dibuat
- [x] Nama produk & nama repo: IRAMA (sementara), repo `lionateofhaidar/irama-project` — cek merek PDKI, domain, handle medsos **masih harus dilakukan**.
- [x] Lisensi: open-core (inti Apache-2.0 + modul komersial) — diputuskan (U-04); tulis ADR-01.
- [ ] Organisasi GitHub (bukan akun pribadi), 2FA wajib, kebijakan branch protection.
- [ ] Visibilitas: privat dulu; publikasi komponen open-source setelah audit lisensi dependensi.
- [x] Kota pilot: Bandung (U-02); sumber data uji: lihat `13_Kebutuhan_Data_per_Tahap.md` (user menyediakan 3–5 klip CCTV).
- [x] Stack awal diputuskan (U-05): Python/FastAPI + Go edge, React + MapLibre, PostgreSQL/PostGIS + TimescaleDB, MQTT, SUMO — tulis ADR-02…ADR-06, ADR-10.

## B. Struktur repo yang disarankan (monorepo)
```
<nama>/
  docs/                      ← SUDAH DITERAPKAN 2026-09-13: kb/ (basis pengetahuan), planning/, sources/ (bahan acuan), adr/, LOG_SESI.md
    adr/  conops/  srs/  kb/  planning/  LOG_SESI (arsip)
  apps/
    tmc-web/                 ← console operator, dashboard publik (React/Next + MapLibre) [usulan]
    api/                     ← backend (FastAPI/Go) [usulan]
  services/
    cai/                     ← Controller Abstraction Interface + adaptor (ntcip-snmp, vendor-rs232, traci-sim)
    atspm/                   ← ingest hi-res log, kalkulator metrik, watchdog
    kpi-pkji/                ← kalkulator PKJI/MKJI/PM 96, plan generator TOD
    priority/                ← PRS (TSP/EVP) [T4]
    adaptive/                ← cyclic max-pressure, perimeter control [T4]
  edge/                      ← agen edge (RPi/IPC): polling controller, hitung CCTV, buffer & heartbeat
  sim/                       ← jaringan SUMO koridor, skenario, skrip TraCI, uji SIL
  packages/                  ← skema data (OpenAPI/JSON Schema), enumerasi NTCIP/Indiana, util
  infra/                     ← docker-compose (T1–T2), k8s (T4+), observability
  tests/                     ← unit, integrasi (SUMO), kontrak API
  .github/                   ← workflows CI, issue/PR templates, CODEOWNERS, SECURITY.md
  LICENSE  README.md  CONTRIBUTING.md  CHANGELOG.md
```

## C. Fondasi rekayasa hari pertama
- [ ] README: visi 1 paragraf (dari `01`), status tahap, cara menjalankan demo SUMO.
- [ ] `docs/adr/` dengan template MADR; tulis ADR-01 (lisensi) s.d. ADR-18 sesuai `06` §7, minimal ADR-01…ADR-08 sebelum sprint 1.
- [ ] CI: lint + unit test + build docker; job "sim-smoke" menjalankan SUMO koridor kecil (headless) dan memverifikasi pipeline ATSPM menghasilkan AoG.
- [ ] Konvensi commit (Conventional Commits) & versi semantik; CHANGELOG.
- [ ] Issue templates: fitur (wajib mengisi "kebutuhan lapangan & bukti", "KPI", "fallback"), bug, riset.
- [ ] Project board dengan kolom per tahap T1–T5; impor backlog dari `05_Inventaris_Fitur_per_Tahap.md` (ID F-T#-##).
- [ ] SECURITY.md (pelaporan kerentanan), kebijakan rahasia (no secrets in repo; .env.example), dependabot.
- [ ] `docs/kb/` = salinan `_knowledge_base` (sumber kebenaran tetap di sini, sinkron manual).
- [ ] Skema data awal (OpenAPI + JSON Schema) untuk entitas inti (Intersection, Controller, Phase, Pattern, Detector, HiResEvent) — dari `docs/kb/06`.
- [ ] Enumerasi: mode kendali PM 49 (tetap/semi-adaptif/adaptif/terkoordinasi), LOS PM 96, kode event hi-res (tandai "verifikasi terhadap Purdue").

## D. Data & aset yang perlu disiapkan sebelum sprint 1
- [ ] Jaringan SUMO koridor contoh (3–5 simpang ≤1 km, sesuai syarat ATCS PM 96) dengan tlLogic NEMA & detektor E1/E2 → `sim/`.
- [ ] Contoh plan APILL eksisting (CSV signal group) untuk `tls_csvSignalGroups.py`.
- [ ] Contoh rekaman CCTV simpang (beberapa menit) untuk uji hitung kendaraan di edge.
- [ ] Salinan regulasi kunci (PM 49, PM 96, PM 76, PKJI Bab 5) ke `docs/kb/regulasi/` (hormati hak cipta: tautan resmi + ringkasan, bukan redistribusi bila ragu).

## E. Hal yang harus disepakati dengan mitra pilot (non-teknis, paralel)
- [ ] Surat minat/MoU Dishub pilot; akses ke ruang kendali & log controller; izin rekam CCTV (PDP).
- [ ] Peta yurisdiksi simpang pilot (provinsi/kota vs nasional → BPTJ/Dirjen).
- [ ] Kontak Ditlantas/Polres untuk prosedur override & (nanti) ETLE.
- [ ] Kriteria sukses pilot tertulis (KPI PM 96/PKJI + ATSPM; desain on/off).
