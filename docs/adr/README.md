# Architecture Decision Records

Format: MADR (`0000-template.md`). Penomoran mengikuti `docs/planning/06_Arsitektur_Konseptual_dan_Opsi_Teknologi.md` §7 (ADR-01…ADR-18). Nama file: `NN-judul-singkat.md`.

Status keputusan awal (dari sesi 2026-09-13, belum ditulis sebagai ADR):
- ADR-01 Lisensi: open-core, inti Apache-2.0 (U-04).
- ADR-02 Stack: Python/FastAPI + agen edge Go; React + MapLibre + ECharts (U-05).
- ADR-04 Time-series: PostgreSQL + PostGIS + TimescaleDB (U-05).
- ADR-05 Message bus: MQTT (U-05).
- ADR-06 Adaptor: edge-light di T2 (U-03).
- ADR-15 Deployment: on-prem default, Docker Compose → k3s (U-04).
