# 06 — Arsitektur Konseptual & Opsi Teknologi

Status: draf pra-perencanaan 2026-09-12. Semua "rekomendasi default" adalah **rekomendasi awal** untuk diputuskan lewat ADR saat planning rinci; angka kapasitas/server adalah **ASUMSI**. Sumber: [R01]–[R06], [R00], [KB].

## 1. Arsitektur lapisan (lintas tahap)

```
┌──────────────────────────────── PENYAJIAN ────────────────────────────────┐
│ TMC Web (peta, fase live, CCTV, ATSPM, plan editor)  │ Mobile teknisi (PWA) │
│ Dashboard publik / API terbuka (T2+/T5)             │ Video wall (T4)      │
└───────────────────────────────────┬───────────────────────────────────────┘
┌──────────────────────────────── PUSAT ────────────────────────────────────┐
│ API Gateway + AuthN/AuthZ (RBAC, tenant)                                  │
│ Core services: Inventory | Plan Manager (PKJI calc, validators) |        │
│   Coordinator/TRPS | Priority Request Server | Health & Alarm | Ticket   │
│ Data services: HiRes ingest → ATSPM engine → KPI/LOS → Reports          │
│ Algorithm runtime: Adaptive (cyclic MP, PC) | Shadow-mode harness        │
│ Digital twin: SUMO/TraCI workers | Scenario store                         │
│ Storage: PostgreSQL(+PostGIS) | TimescaleDB (events, KPI) | Object store  │
│ Message bus: MQTT broker (edge) ⇄ NATS/Kafka (T4+) | Cache Redis         │
└───────────────────────────────────┬───────────────────────────────────────┘
┌──────────────────────────────── INTEGRASI (C2C) ──────────────────────────┐
│ Polri NTMC/RTMC | JSC/portal kota | AVL/APC bus | CAD 112/119 | ETLE     │
│ Bapenda | DLH | Tol | Cuaca/AQI | Probe GPS | CRM aduan                   │
└───────────────────────────────────┬───────────────────────────────────────┘
┌──────────────────────────────── KOMUNIKASI ───────────────────────────────┐
│ Fiber/Metro-E (utama) | 4G/5G (cadangan) | mTLS, VPN, segmentasi NEMA TS 8│
└───────────────────────────────────┬───────────────────────────────────────┘
┌──────────────────────────────── LAPANGAN / EDGE ──────────────────────────┐
│ Edge Gateway per kabinet: Controller Abstraction Interface               │
│   ├ Adaptor NTCIP 1202/1211 (SNMP/STMP)   ├ Adaptor RS-232 vendor          │
│   ├ Edge logger I/O (fallback hi-res)     ├ Buffer store-and-forward      │
│   └ Heartbeat < unitBackupTime            └ Sinkron waktu GPS/NTP          │
│ Edge AI box (T3+): count/occupancy/queue/ANPR → detektor virtual           │
│ Controller APILL (≥8 plan TOD lokal, actuated lokal, conflict monitor)     │
│ Detektor (kamera/loop/radar), DIS/countdown, CCTV RTSP                    │
└───────────────────────────────────────────────────────────────────────────┘
```

Prinsip: kecerdasan **turun ke edge** (deteksi, buffer, fallback), **kendali** di pusat hanya lewat perintah tipe C + heartbeat, **kebenaran KPI** dari hi-res event log yang sama untuk lapangan & simulasi [R03 D].

## 2. Komponen per tahap

| Komponen | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| Inventory/Registry + PKJI calc + validators | ✓ | ✓ | ✓ | ✓ | ✓ |
| Adaptor: TraCI sim | ✓ | ✓ | ✓ | ✓ | ✓ |
| Adaptor: NTCIP read-only / read-write | RO | RW | RW | RW + 1211/v03 | RW |
| Adaptor: RS-232 vendor | — | ≥1 | ≥2 | ≥3 | plugin SDK |
| Edge gateway (buffer, heartbeat, logger) | — | ✓ | ✓ | ✓ | ✓ |
| Edge AI (detektor virtual, ANPR) | — | — | ✓ (simpang terpilih) | ✓ | ✓ + fusi radar |
| Coordinator/transition/TRPS | — | Coordinator | +TRPS | +MP/PC | +marketplace |
| Priority Request Server | — | — | TSP dasar | TSP kondisional + EVP | + VIP/konvoi, GLOSA |
| ATSPM engine | 4 metrik | 8 metrik + watchdog | + YRA, Link Pivot | penuh | penuh + benchmark |
| Digital twin | SUMO lokal | — (opsional) | per koridor + shadow | batch what-if | twin kota |
| Integrasi C2C | — | CCTV, CRM | AVL, probe, ETLE-bukti | Polri, CAD, Bapenda, DLH, tol, cuaca | API publik, TDM |
| Multi-tenant | — | — | — | per yurisdiksi | multi-kota |
| Deployment | Compose laptop | Compose 1 VM | Compose 2 VM / 1 server | k8s kecil (3 node) | k8s multi-region |

## 3. Opsi teknologi & rekomendasi awal

| Area | Opsi | Trade-off | Rekomendasi awal (ADR) |
|---|---|---|---|
| Backend | **Python/FastAPI**; Go; TypeScript/NestJS | Python: ekosistem traffic (SUMO/TraCI, pysnmp, numpy, ML) & kecepatan iterasi; Go: performa & binari edge; TS: satu bahasa dengan frontend | **Python/FastAPI** untuk core & algoritma; **Go** (atau Python ringan) untuk edge agent bila butuh binari kecil |
| Frontend | **React + Next.js/Vite**, MapLibre GL (peta vektor), ECharts/Plotly untuk PCD/TSD | Vue alternatif; Leaflet lebih ringan tapi raster | **React + MapLibre + ECharts**; PWA untuk mobile teknisi |
| Database relasional | **PostgreSQL 16 + PostGIS** | Standar, spasial, JSONB | Ya |
| Time-series | **TimescaleDB** (hypertable, compression, continuous aggregates); ClickHouse; InfluxDB | Timescale = satu engine dengan Postgres, kompresi 10–20×, retensi per policy; ClickHouse lebih cepat untuk analitik besar (T5) | **TimescaleDB** T1–T4; evaluasi ClickHouse di T5 |
| Object store | MinIO / S3 | Bukti foto/video singkat, blok OER, laporan | MinIO on-prem |
| Message bus | **MQTT (Mosquitto/EMQX)** edge↔pusat; NATS JetStream / Kafka intra-pusat | MQTT hemat bandwidth & QoS untuk 4G; Kafka berat untuk T2 | MQTT + Redis streams (T2); NATS JetStream (T3); Kafka hanya bila >500 simpang |
| Video | RTSP → **go2rtc/mediamtx** → WebRTC/HLS; VMS eksisting via ONVIF | Tidak merekam di pusat T1–T3 (hemat storage); rekaman event pendek di edge | Gateway ringan, rekam klip 30 s hanya untuk bukti |
| Edge hardware | Raspberry Pi 4/5 industrial; Jetson Orin Nano (AI); industrial PC | Pi murah untuk gateway; Jetson untuk 4 kamera/simpang | Gateway Pi/IPC per kabinet; Jetson di simpang kritis |
| Protokol controller | pysnmp/gosnmp (NTCIP 1202), STMP opsional; RS-232 via pyserial; OER encoder untuk block | v02 tanpa TSP → 1211/v03 di T4 | Library adaptor sendiri + conformance test suite |
| Simulasi | **SUMO + TraCI/libsumo**, netconvert/OSM, NEMA type | Vissim komersial | SUMO (lisensi EPL, dipakai jurnal Indonesia juga) |
| ML/AI | Ultralytics YOLO (edge count/klasifikasi), OpenALPR/PaddleOCR (ANPR), scikit-learn/LightGBM (prediksi), RL offline (SB3) | Akurasi hujan/malam; biaya GPU | Model ringan di edge; pusat hanya skor & nilai antara |
| Observability | Prometheus + Grafana + Loki; OpenTelemetry | — | Ya sejak T1 |
| Deployment | Docker Compose (T1–T3); k3s/k8s (T4+); Ansible untuk edge | Compose cukup untuk ≤100 simpang (ASUMSI) | Compose → k3s |
| Keamanan | mTLS edge (step-ca/Vault), OAuth2/OIDC (Keycloak), RBAC per tenant/yurisdiksi, audit log immutable, NEMA TS 8 checklist, VPN/segmentasi | — | Keycloak + step-ca; audit append-only |
| Lisensi produk | Core open-source (Apache-2.0) + modul komersial; atau proprietary penuh | Open core menaikkan kepercayaan pemda & kepatuhan "sistem terbuka" PM 76 | Diputuskan di ADR-01 (rekomendasi: open core) |

## 4. Model data & antarmuka (ringkas; detail [R03 D.1], [R01 I.1])
Entitas: Intersection, Approach/Lane/Movement, Controller (protokol, kapabilitas, backup time), Phase/Stage, Ring/Sequence, Overlap, Channel, Detector, Pattern, Split, TimebaseAction/DayPlan, Preempt, PriorityRequest, SpecialFunction, ControllerStatusSnapshot, HiResEvent, VolumeOccupancyReport, CommandLog, PlanChangeTransaction, KPI result, Alert, Corridor, SimulationScenario, Asset (PM 49), Ticket, FieldDiary, Tenant/Jurisdiction.
API: `/intersections`, `/controllers/{id}/status|commands|transactions|blocks`, `/plans`, `/corridors/{id}/green-wave|link-pivot`, `/priority/requests`, `/hires/ingest`, `/atspm/*`, `/kpi/*`, `/reports/*`, `/sim/*`, `/alerts`, `/tickets`.

## 5. Retensi & volume data (hemat server)

| Data | Resolusi | Retensi (ASUMSI) | Volume |
|---|---|---|---|
| Hi-res event | 0,1 s | 90 hari mentah (terkompresi Timescale ~10×) | ±23 MB/simpang/hari mentah (HOP-20-002: 9 GB/hari/387 sinyal) → 40 simpang ≈ 0,9 GB/hari; terkompresi ≈ 0,1 GB/hari |
| Status snapshot | 1 s | 7 hari | kecil (bitmask) |
| Agregat ATSPM/KPI | 15 menit/plan/hari | 5 tahun | ≈ 1 MB/simpang/bulan |
| Volume/occupancy | 1–5 menit | 2 tahun | kecil |
| Command/audit log | event | permanen | kecil |
| Video | tidak disimpan di pusat (T1–T3); klip bukti 30 s | 30 hari | ≈ 5 MB/klip |
| Probe GPS | waypoint | 90 hari mentah → agregat segmen | tergantung penyedia |

Edge: buffer 24–72 jam event; agregasi menit di edge bila link lemah.

## 6. Estimasi server per tahap (ASUMSI, untuk validasi di planning)

| Tahap | Cakupan | Pusat | Edge | Catatan |
|---|---|---|---|---|
| T1 | ≤5 simpang (sim) | laptop/VM 4 vCPU/16 GB/200 GB | — | SUMO lokal |
| T2 | ≤40 simpang, ≤60 kamera view | 1 VM 8 vCPU/32 GB/1 TB SSD (atau mini-server on-prem) | Pi/IPC per kabinet | Compose; 30 hari stabil |
| T3 | ≤100 simpang, 5–10 koridor adaptif | 2 VM (app 8/32; data 8/64/2 TB) + 1 worker simulasi | + Jetson di 10–30 simpang | NATS |
| T4 | 100–350 simpang | k3s 3 node (16/64 tiap) + storage 10 TB + GPU node opsional | Jetson di simpang kritis | HA, backup |
| T5 | multi-kota | cloud/DC pemerintah, autoscale | — | data lake + ClickHouse |

## 7. Daftar ADR yang harus dibuat saat planning
1. ADR-01 Model lisensi & open-core vs proprietary.
2. ADR-02 Bahasa/framework backend & edge agent.
3. ADR-03 Skema data inti: mengikuti NTCIP 1202 v03 + ekstensi stage-based Indonesia.
4. ADR-04 Time-series store & kebijakan retensi.
5. ADR-05 Message bus edge↔pusat (MQTT QoS, topik, keamanan).
6. ADR-06 Strategi adaptor controller (NTCIP native, RS-232 plugin SDK, edge logger fallback).
7. ADR-07 Kebijakan kendali: perintah C saja untuk real-time; plan via transaksi; heartbeat.
8. ADR-08 Standar hi-res event (kode Indiana) & pipeline ATSPM tunggal lapangan/simulasi.
9. ADR-09 Algoritma adaptif tingkat pertama (cyclic MP) & guard-rail wajib.
10. ADR-10 Digital twin (SUMO NEMA) & protokol validasi SIL→HIL→shadow→live.
11. ADR-11 Video: tidak disimpan di pusat; gateway & klip bukti.
12. ADR-12 Keamanan: mTLS, IdP, RBAC yurisdiksi, NEMA TS 8, PDP (retensi pelat, anonimisasi).
13. ADR-13 Multi-tenant (sejak skema data) & isolasi.
14. ADR-14 Observability & SLO (latensi status ≤5 s, alarm ≤1 menit, uptime ≥99,5%).
15. ADR-15 Strategi deployment (Compose → k3s) & on-prem vs cloud pemda.
16. ADR-16 Integrasi eksternal via ICD (format, frekuensi, kepemilikan data) dan MoU digital.
17. ADR-17 Peta dasar (OSM/MapLibre) & sumber geometri simpang.
18. ADR-18 Bahasa UI & i18n (ID utama), aksesibilitas TMC.
