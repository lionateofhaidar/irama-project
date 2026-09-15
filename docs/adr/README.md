# Architecture Decision Records

Format: MADR (`0000-template.md`). Penomoran dan isi pokok mengikuti daftar ADR-01 sampai ADR-25 di `docs/planning/06_Arsitektur_Konseptual_dan_Opsi_Teknologi.md` bagian 8 (kanonis). Nama file: `NN-judul-singkat.md`, misalnya `19-model-deteksi-onnx.md`.

Belum ada ADR yang ditulis. ADR yang harus selesai sebelum sprint 1 (`docs/planning/10` bagian C): ADR-01, ADR-02, ADR-03, ADR-15, ADR-19, ADR-20, ADR-21, ADR-22, dan ADR-25.

Keputusan yang sudah diambil user tetapi belum ditulis sebagai ADR (sumber: `docs/kb/10` bagian B dan B2, revisi 2026-09-14):
- ADR-01 Model lisensi: open-core, inti Apache-2.0, modul komersial terpisah (U-04).
- ADR-02 Bahasa dan framework: Python + FastAPI di pusat; frontend React + MapLibre + ECharts; agen edge Go atau Python ringan mulai T4 (U-05).
- ADR-04 Penyimpanan deret waktu dan retensi: PostgreSQL biasa dulu, TimescaleDB hanya bila perlu; aturan retensi di `06` bagian 6 (U-05, dilengkapi 2026-09-14).
- ADR-05 Antrean tugas dan message bus: tabel antrean PostgreSQL di T1–T3; MQTT (Mosquitto atau NanoMQ) atau NATS mulai T4 (U-05; U-22).
- ADR-06 Strategi adaptor controller: tanpa edge sampai T3; controller dibaca tanpa diubah di T3; adaptor kendali NTCIP dan vendor lewat edge mulai T4 (U-03 direvisi, U-21, U-22).
- ADR-15 Deployment: laptop tim dan Docker Compose di T1–T3; k3s mulai T4; on-prem default, cloud opsional (U-04, U-22).
- ADR-19 Model deteksi: model berlisensi permisif (RF-DETR atau YOLOX) dalam format ONNX; Ultralytics YOLO (AGPL) tidak dipakai; pilihan akhir lewat uji kecepatan dan akurasi T1, lisensi bobot tiap varian diperiksa (U-25, Q-12).
- ADR-22 Kebijakan data rekaman: rekaman saja sampai ada MoU; video publik boleh untuk uji dan pelatihan dengan register sumber (U-23).
- ADR-23 Lokasi pelatihan: Kaggle (utama) dan Colab (cadangan) untuk data publik; data Dishub dilatih di laptop (U-24).
- ADR-25 Pemeriksaan lisensi dependensi: otomatis di CI dengan daftar larangan (U-25).

Catatan: daftar lama di berkas ini (edisi 2026-09-13) merujuk `06` bagian 7 dengan ADR-01 sampai ADR-18, edge ringan di T2, TimescaleDB wajib, dan MQTT sejak awal. Semua itu sudah digantikan keputusan 2026-09-14 di atas.
