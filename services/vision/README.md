# services/vision

Vision Tracker: ambil bingkai (FFmpeg/OpenCV), deteksi enam kelas (RF-DETR atau YOLOX lewat ONNX Runtime, CPU atau iGPU), pelacakan (ByteTrack lewat supervision), hitung per pendekat [T1] dan per arah dari lintasan [T2], hambatan samping berbobot PKJI 2023, pembacaan nyala lampu, antrian dasar, penyamaran wajah dan pelat [T2]; kendaraan prioritas, kejadian, pelanggaran tanpa pelat, dan kesehatan kamera [T3]; berjalan di edge 24 jam [T4].

Spesifikasi di `docs/planning/15` bagian 3; panduan data latih di `docs/planning/16`. Ultralytics YOLO (AGPL) tidak dipakai.

Belum ada kode. Lihat `docs/planning/10_Checklist_Pra-GitHub.md` §B.
