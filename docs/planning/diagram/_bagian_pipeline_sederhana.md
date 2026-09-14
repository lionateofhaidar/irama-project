## Arsitektur alur data, komponen, dan teknologi (A01)

Diagram A01 merangkum alur kerja IRAMA dari kamera sampai keputusan. Video dari CCTV diolah Vision Tracker menjadi tabel hitungan per kelas kendaraan, per arah, dan per 15 menit. Tabel itu disimpan bersama konfigurasi simpang, lalu diolah modul Optimasi Waktu Simpang menjadi rekomendasi waktu siklus dan waktu hijau. Hasilnya tampil di dashboard dan laporan kajian sebagai bahan keputusan engineer dan Kepala Dinas. Setiap kotak mencantumkan teknologi yang dipakai dalam huruf miring.

Cara membaca diagram:

- Label warna di pojok kanan atas kotak menunjukkan tahap saat komponen itu pertama tersedia. T1 hijau, T2 biru, T3 jingga, T4 ungu, T5 merah.
- Untuk melihat kondisi sistem pada tahap tertentu, abaikan kotak dengan tahap lebih tinggi. Pada T2, misalnya, alur berjalan dari rekaman atau stream uji, melalui Vision Tracker dan optimasi, sampai dashboard, laporan, keputusan, dan penerapan manual oleh petugas.
- Panah tegak di dalam kolom menunjukkan urutan proses. Panah antarkolom menunjukkan data yang berpindah ke bagian berikutnya.
- Garis jingga di bawah kolom adalah jalur kejadian mulai T3. Peristiwa seperti ambulans lewat atau kamera tertutup langsung dikirim ke konsol pemantauan tanpa melalui optimasi.
- Garis putus-putus adalah umpan balik mulai T3. Setelah jadwal baru diterapkan, rekaman sesudahnya diukur ulang untuk membuktikan perubahan kinerja simpang.

<<<LANDSCAPE>>>

![A01](diagram/A01_Arsitektur_Alur_Data.png)

Rincian komponen, teknologi, dan tahap:

| Kolom | Komponen | Teknologi | Tahap |
|---|---|---|---|
| Sumber video | Rekaman CCTV dan video publik | MP4/MKV, register sumber rekaman | T1 |
| Sumber video | Stream CCTV | RTSP/HLS/ONVIF; uji lewat MediaMTX (T2), stream Dishub setelah MoU (T3) | T2 |
| Vision Tracker | Ambil bingkai | FFmpeg, OpenCV | T1 |
| Vision Tracker | Deteksi enam kelas kendaraan | RF-DETR/YOLOX lewat ONNX Runtime (CPU/iGPU) | T1 |
| Vision Tracker | Pelacakan dan hitung per pendekat | ByteTrack, supervision; arah dari lintasan (T2) | T1 |
| Vision Tracker | Hambatan samping, nyala lampu, antrian | logika IRAMA, OpenCV; penyamaran wajah dan pelat | T2 |
| Vision Tracker | Kejadian dan kesehatan kamera | model tambahan, aturan peringatan | T3 |
| Data terstruktur | Tabel hitungan 15 menit dan mutu data | PostgreSQL | T1 |
| Data terstruktur | Hambatan samping, status lampu, antrian | PostgreSQL (TimescaleDB opsional) | T2 |
| Data terstruktur | Konfigurasi simpang dan parameter | formulir (T1), wizard React + MapLibre (T2); PostgreSQL + PostGIS | T1 |
| Data terstruktur | Peristiwa kejadian dan kesehatan kamera | PostgreSQL, klip bukti tersamarkan | T3 |
| Optimasi waktu simpang | Konversi SMP dan periode | Python, EMP PKJI 2023; periode otomatis (T2) | T1 |
| Optimasi waktu simpang | Kalkulator PKJI 2023 | NumPy, modul PKJI IRAMA; mode MKJI 1997 (T2) | T1 |
| Optimasi waktu simpang | Mode optimasi | SciPy; Webster (T1), empat mode (T2), multi-kriteria (T3) | T1 |
| Optimasi waktu simpang | Validasi simulasi | SUMO, TraCI | T2 |
| Optimasi waktu simpang | Manfaat rupiah | parameter UMK, BBM, emisi | T2 |
| Penyajian dan keputusan | Dashboard simpang | React, ECharts; versi dasar (T1), tiga halaman (T2) | T1 |
| Penyajian dan keputusan | Laporan kajian Word/PDF | python-docx, LibreOffice | T2 |
| Penyajian dan keputusan | Keputusan engineer dan Kepala Dinas | persetujuan dan jejak audit | T2 |
| Penyajian dan keputusan | Konsol pemantauan kejadian | React; notifikasi email/WhatsApp | T3 |
| Tindak lanjut | Penerapan manual oleh petugas | lembar jadwal dari dashboard atau laporan | T2 |
| Tindak lanjut | Ekspor jadwal dan uji sebelum-sesudah | format tabel, NTCIP baca-saja | T3 |
| Tindak lanjut | Kendali controller dan adaptif | adaptor NTCIP/vendor, edge, MQTT | T4 |
| Tindak lanjut | Koordinasi koridor dan jaringan | offset, bandwidth, Link Pivot; twin kota | T5 |
| Tindak lanjut | Tiket kerja dan tindak lanjut kejadian | tiket, email/WhatsApp, laporan wajib | T3 |

<<<PORTRAIT>>>
