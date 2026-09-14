# -*- coding: utf-8 -*-
"""
Diagram alur fitur utama IRAMA (end-state) dengan pemetaan ke lapisan arsitektur dan tahap T1 sampai T5,
serta diagram arsitektur alur data dari CCTV sampai keputusan (A01).
Menghasilkan PNG dan mermaid di docs/planning/diagram/, serta potongan markdown:
_bagian_diagram.md dan _bagian_diagram_sederhana.md untuk dokumen 06,
_bagian_pipeline.md dan _bagian_pipeline_sederhana.md untuk dokumen 14.

Konvensi visual: baris (swimlane) = lapisan arsitektur; kotak = langkah; label warna di pojok kotak = tahap
saat langkah itu pertama kali tersedia (T1 hijau, T2 biru, T3 jingga, T4 ungu, T5 merah).
Panah dirutekan siku lewat celah antarkolom dan jalur di tepi lajur sehingga tidak menembus kotak.
Jalankan: python make_diagrams.py
"""
import io, os, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from matplotlib.path import Path

HERE = os.path.dirname(os.path.abspath(__file__))
STAGE_COLOR = {"T1": "#2E7D32", "T2": "#1565C0", "T3": "#EF6C00", "T4": "#6A1B9A", "T5": "#C62828"}
STAGE_NAME = {"T1": "T1 Purwarupa", "T2": "T2 Vision & Optimasi", "T3": "T3 Kejadian & Pemantauan", "T4": "T4 Kendali Adaptif", "T5": "T5 Platform Kota"}
LANES = [
    ("P", "Pengguna &\nmitra eksternal"),
    ("U", "Penyajian\n(layar &\naplikasi)"),
    ("S", "Pusat\n(laptop T1-T3,\nserver T4+)"),
    ("K", "Komunikasi &\nintegrasi"),
    ("L", "Lapangan\n(kamera, kabinet,\ncontroller)"),
]
LANE_IDX = {k: i for i, (k, _) in enumerate(LANES)}
LANE_FILL = ["#F7F7F7", "#FFFFFF", "#F2F6FA", "#FFFFFF", "#F7F7F7"]

# ------------------------------------------------------------------ data alur (revisi 2026-09-14)
# step: (id, lane, teks, tahap, komponen)  ; edge: (dari, ke, label)
FLOWS = []

def flow(fid, judul, tujuan, steps, edges, catatan="", hint=None):
    FLOWS.append(dict(id=fid, judul=judul, tujuan=tujuan, steps=steps, edges=edges, catatan=catatan, hint=hint or {}))

flow("F01", "Pemantauan kondisi simpang",
     "Kondisi setiap simpang (arus, LOS, nyala lampu, peringatan) terlihat di dashboard. T1 dan T2 memakai data dari rekaman melalui Vision Tracker; T3 menambah stream Dishub dan status controller baca-saja; T4 menambah edge dan kendali.",
     [("a", "L", "Rekaman atau stream CCTV simpang", "T1", "kamera eksisting, berkas rekaman"),
      ("b", "L", "Controller dibaca tanpa diubah, bila Dishub mengizinkan", "T3", "controller vendor/NTCIP"),
      ("c", "L", "Agen edge di kabinet menerjemahkan protokol vendor", "T4", "edge/"),
      ("d", "K", "Stream Dishub lewat VPN setelah MoU; MQTT dan mTLS di T4", "T3", "infra/ (MediaMTX, VPN)"),
      ("e", "S", "Vision Tracker menghitung arus (T1) dan membaca nyala lampu (T2)", "T1", "services/vision"),
      ("f", "S", "Aturan peringatan (lampu mati atau kedip, kamera bermasalah)", "T3", "services/health"),
      ("g", "U", "Peta simpang, LOS, dan kondisi terkini di dashboard", "T2", "apps/tmc-web (MapLibre)"),
      ("h", "P", "Engineer, operator, dan pimpinan memantau", "T2", "")],
     [("a", "e", ""), ("b", "d", ""), ("c", "d", "T4"), ("d", "e", ""), ("e", "f", ""), ("e", "g", ""), ("f", "g", "peringatan"), ("g", "h", "")])

flow("F02", "Rekomendasi dan penetapan waktu sinyal",
     "Engineer mengonfigurasi simpang, sistem mengubah hitungan Vision Tracker menjadi arus SMP, menghitung kinerja dengan PKJI 2023, menjalankan mode optimasi, memvalidasinya di SUMO, lalu menyusun laporan. Rekomendasi diterapkan manual di T2, lewat lembar jadwal di T3, dan dikirim ke controller di T4.",
     [("a", "P", "Engineer mengisi konfigurasi simpang (formulir T1, wizard T2)", "T1", "apps/tmc-web"),
      ("b", "S", "Konversi hitungan ke arus SMP per periode (EMP PKJI 2023)", "T1", "services/optimizer"),
      ("c", "S", "Kalkulator PKJI 2023: kapasitas, DJ, antrian, tundaan, LOS", "T1", "services/optimizer (NumPy)"),
      ("d", "S", "Mode optimasi: Webster (T1); empat mode lain (T2); multi-kriteria (T3)", "T1", "services/optimizer (SciPy)"),
      ("e", "S", "Validator keselamatan dan validasi SUMO eksisting vs rekomendasi", "T2", "sim/ (SUMO)"),
      ("f", "U", "Dashboard rekomendasi, manfaat rupiah, laporan Word/PDF", "T2", "apps/tmc-web, services/reports"),
      ("g", "P", "Persetujuan Kepala Dinas; Dirjen/BPTJ bila jalan nasional", "T2", "alur persetujuan"),
      ("h", "L", "Petugas menerapkan waktu baru di controller", "T2", "manual (T2), lembar jadwal (T3), NTCIP/adaptor (T4)"),
      ("i", "S", "Uji lapangan sebelum-sesudah diukur Vision Tracker", "T3", "services/vision")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", ""), ("f", "g", ""), ("g", "h", ""), ("h", "i", "T3")])

flow("F03", "Kendali terpusat, mode manual petugas, dan cadangan saat putus",
     "Mulai T4 operator atau petugas Polri memilih program atau mode manual dari ruang kendali. Pusat mengirim perintah terbatas beserta detak jantung. Bila jaringan putus, controller kembali ke jadwal lokal dan semua kejadian tetap tercatat.",
     [("a", "P", "Operator atau petugas Polri memilih program, kedip, atau mode manual", "T4", "konsol kendali"),
      ("b", "U", "Konsol kendali meminta konfirmasi dan alasan", "T4", "apps/tmc-web"),
      ("c", "S", "Layanan perintah memeriksa hak akses, mengirim perintah dan detak jantung", "T4", "services/cai"),
      ("d", "K", "SNMP/MQTT lewat VPN", "T4", "infra/"),
      ("e", "L", "Controller menjalankan program; edge meneruskan detak jantung", "T4", "controller, edge/"),
      ("f", "L", "Jaringan putus: controller kembali ke jadwal lokal; edge menyimpan catatan", "T4", "controller, edge/"),
      ("g", "S", "Jejak audit perintah; alarm bila cadangan aktif", "T4", "audit log, services/health")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", "bila putus"), ("e", "g", ""), ("f", "g", "alarm")])

flow("F04", "Kesehatan kamera dan perangkat, alarm, tiket kerja, dan pemeliharaan",
     "Kamera bermasalah terdeteksi dari gambar mulai T3; alarm controller dan detektor mulai T4. Peringatan menjadi tiket kerja untuk teknisi. Jadwal pemeliharaan berkala dan umur teknis aset dijaga sesuai PM 49/2014.",
     [("a", "L", "Kamera tertutup, gelap, buram, atau bergeser", "T3", "kamera; dideteksi services/vision"),
      ("b", "L", "Alarm controller, detektor, pintu kabinet, catu daya", "T4", "controller, edge/"),
      ("c", "S", "Mesin peringatan: prioritas, eskalasi, notifikasi APILL mati", "T3", "services/health"),
      ("d", "K", "Email/WhatsApp; API aduan kota", "T3", "integrasi"),
      ("e", "S", "Tiket kerja otomatis dengan target waktu penyelesaian", "T3", "services/ticket"),
      ("f", "U", "Aplikasi ponsel teknisi: tiket, checklist, foto", "T4", "apps/tmc-web (PWA)"),
      ("g", "S", "Jadwal pemeliharaan enam bulanan dan umur teknis lima tahun", "T3", "apps/api (aset)"),
      ("h", "P", "Kepala Dinas melihat KPI kesehatan kamera dan perangkat", "T3", "dashboard pimpinan")],
     [("a", "c", ""), ("b", "c", "T4"), ("c", "d", ""), ("c", "e", ""), ("e", "f", ""), ("f", "e", "selesai"), ("g", "e", "jatuh tempo"), ("e", "h", "KPI")])

flow("F05", "Pengukuran kinerja dan laporan",
     "Hitungan dan status lampu dari Vision Tracker (kemudian juga log controller) diolah menjadi KPI resmi PKJI dan LOS PM 96/2015, perbandingan eksisting dan rekomendasi, laporan kajian (T2), dan laporan wajib ke Forum LLAJ, Dirjen/BPTJ, dan Gubernur (T3).",
     [("a", "L", "Hitungan (T1), status lampu dan antrian (T2) dari Vision Tracker", "T1", "services/vision"),
      ("b", "K", "Log kejadian controller lewat MQTT", "T4", "infra/"),
      ("c", "S", "Simpan tabel 15 menit (T1), status lampu dan antrian (T2); retensi bertingkat", "T1", "PostgreSQL"),
      ("d", "S", "Metrik kinerja sinyal (split failure, arrivals on green)", "T3", "services/metrics"),
      ("e", "S", "KPI PKJI dan LOS PM 96; eksisting vs rekomendasi", "T1", "services/optimizer"),
      ("f", "S", "Laporan kajian simpang (T2); laporan wajib (T3)", "T2", "services/reports"),
      ("g", "U", "Dashboard pimpinan dan engineer; dashboard publik (T3)", "T2", "apps/tmc-web"),
      ("h", "P", "Pejabat, DPRD, Forum LLAJ, warga", "T2", "")],
     [("a", "c", ""), ("b", "c", "T4"), ("c", "d", ""), ("c", "e", ""), ("e", "f", ""), ("e", "g", ""), ("f", "h", ""), ("g", "h", "")])

flow("F06", "Pipeline Vision Tracker dan keluaran tabel hitungan",
     "Vision Tracker mengubah rekaman atau stream CCTV menjadi tabel hitungan per kelas, per arah, dan per 15 menit, ditambah hambatan samping, nyala lampu, dan antrian. Penyamaran wajah dan pelat berlaku mulai T2. Mulai T3 ditambah deteksi kejadian dan kesehatan kamera. Di T4 Vision Tracker berjalan di perangkat edge dan pembacaan pelat memakai kamera ANPR khusus.",
     [("a", "L", "Rekaman CCTV atau video publik (T1); stream RTSP/HLS (uji T2, Dishub T3)", "T1", "berkas, MediaMTX"),
      ("b", "S", "Ambil bingkai sekitar 10 per detik", "T1", "FFmpeg, OpenCV"),
      ("c", "S", "Deteksi enam kelas dan pelacakan", "T1", "RF-DETR/YOLOX, ONNX Runtime, ByteTrack"),
      ("d", "S", "Hitung per pendekat (T1) dan per arah dari lintasan (T2)", "T1", "supervision, services/vision"),
      ("e", "S", "Hambatan samping berbobot PKJI, nyala lampu, antrian dasar", "T2", "services/vision"),
      ("f", "S", "Tabel hitungan 15 menit dan mutu data; penyamaran video mulai T2", "T1", "PostgreSQL, services/vision"),
      ("g", "S", "Kendaraan prioritas, kejadian, pelanggaran, kesehatan kamera", "T3", "services/vision"),
      ("h", "L", "Vision Tracker di edge 24 jam; ANPR kamera khusus", "T4", "edge/ (Jetson/IPC)"),
      ("i", "U", "Tabel dan dashboard dasar (T1); halaman kualitas data (T2)", "T1", "apps/tmc-web"),
      ("j", "P", "Engineer memeriksa dan mengoreksi", "T1", "")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", "T2"), ("d", "f", ""), ("e", "f", ""), ("c", "g", "T3"), ("h", "f", "T4"), ("f", "i", ""), ("i", "j", "")])

flow("F07", "Kendali responsif dan adaptif",
     "Mulai T4 detektor virtual dari kamera dipakai untuk actuated, pemilihan program menurut kondisi, dan offset dasar antar simpang berdekatan. Di T5 ditambah max-pressure jaringan dan pengendalian perimeter. Mode bayangan memastikan algoritma terbukti sebelum mengendalikan lampu.",
     [("a", "L", "Detektor virtual kamera, loop, atau radar", "T4", "edge/, controller"),
      ("b", "S", "Gerbang kesehatan: adaptif hanya bila detektor sehat", "T4", "services/adaptive"),
      ("c", "S", "Actuated dan pemilihan program per simpang (TRPS)", "T4", "services/adaptive"),
      ("d", "S", "Offset dasar dan green wave sederhana simpang berdekatan", "T4", "services/adaptive"),
      ("e", "S", "Max-pressure jaringan dan pengendalian perimeter", "T5", "services/network"),
      ("f", "S", "Mode bayangan dan metrik kinerja sebagai pengamat", "T4", "shadow harness"),
      ("g", "K", "Perintah lewat antarmuka controller", "T4", "services/cai"),
      ("h", "L", "Controller menjalankan; jadwal lokal tetap cadangan", "T4", "controller"),
      ("i", "U", "Konsol adaptif: parameter, keputusan, nilai antara", "T4", "apps/tmc-web")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", "T5"), ("c", "g", ""), ("d", "g", ""), ("e", "g", ""), ("g", "h", ""), ("a", "f", ""), ("f", "i", ""), ("c", "i", "")])

flow("F08", "Prioritas bus dan kendaraan darurat",
     "Vision Tracker mengenali kendaraan prioritas sejak T3. Mulai T4 permintaan prioritas dari pelacakan bus dan pusat komando pemadam atau ambulans dinilai, dijaga batas keselamatannya, lalu dilayani lewat controller. Prioritas bus bersyarat berbasis muatan di T5.",
     [("a", "P", "AVL/APC operator bus; CAD pemadam dan ambulans", "T4", "operator bus, 112/119"),
      ("j", "S", "Vision Tracker mengenali ambulans, damkar, dan pengawalan dari kamera", "T3", "services/vision"),
      ("b", "K", "API mitra sesuai dokumen antarmuka", "T4", "integrasi (ICD)"),
      ("c", "S", "Layanan permintaan prioritas: kelayakan dan antrean", "T4", "services/priority"),
      ("d", "S", "Prioritas bersyarat berbasis muatan dan keterlambatan", "T5", "services/priority"),
      ("e", "S", "Batas: pejalan kaki tidak dipotong, satu aktivasi per siklus, pemulihan", "T4", "services/priority"),
      ("f", "K", "Perintah perpanjangan hijau atau preemption", "T4", "services/cai"),
      ("g", "L", "Controller memberi hijau tambahan atau preempt", "T4", "controller, edge/"),
      ("h", "U", "Konsol prioritas: permintaan, dilayani, dampak jalan samping", "T4", "apps/tmc-web"),
      ("i", "S", "Log dan KPI waktu tempuh bus dan waktu tanggap darurat", "T4", "services/metrics")],
     [("a", "b", ""), ("j", "c", "T4"), ("b", "c", ""), ("c", "d", "T5"), ("c", "e", ""), ("d", "e", ""), ("e", "f", ""), ("f", "g", ""), ("g", "i", ""), ("c", "h", ""), ("i", "h", "")])

flow("F09", "Bukti pelanggaran untuk ETLE Polri",
     "Sistem hanya menyediakan bukti. Di T3 Vision Tracker mendeteksi pelanggaran tanpa membaca pelat. Di T4 kamera ANPR khusus dan API ke Back Office ETLE Polri ditambahkan; verifikasi dan penindakan tetap oleh petugas Polri.",
     [("a", "S", "Vision Tracker mendeteksi terobos merah dan pelanggaran lain, tanpa pelat", "T3", "services/vision"),
      ("b", "S", "Paket bukti: klip tersamarkan, waktu, lokasi", "T3", "services/evidence"),
      ("c", "S", "Kontrol perlindungan data dan DPIA", "T3", "keamanan & kepatuhan"),
      ("d", "L", "Pembacaan pelat dengan kamera ANPR khusus", "T4", "kamera ANPR, edge/"),
      ("e", "K", "API ke Back Office ETLE sesuai Perpol 8/2023", "T4", "integrasi (ICD Polri)"),
      ("f", "P", "Petugas Polri memverifikasi dan menindak", "T4", "Polri"),
      ("g", "S", "Status tindak lanjut hanya-baca; laporan integrasi tahunan", "T4", "services/evidence"),
      ("h", "U", "Dashboard keselamatan per simpang", "T3", "apps/tmc-web")],
     [("a", "b", ""), ("b", "c", ""), ("d", "b", "T4"), ("c", "e", "T4"), ("e", "f", ""), ("f", "g", "status"), ("b", "h", ""), ("g", "h", "")])

flow("F10", "Keluhan publik dan jaminan layanan",
     "Mulai T3 laporan warga masuk lewat aplikasi kota atau CRM, menjadi tiket dengan target waktu penyelesaian, dan didiagnosis dengan data Vision Tracker termasuk pemutaran ulang kondisi saat keluhan.",
     [("a", "P", "Warga melapor lewat aplikasi kota, CRM, atau telepon", "T3", "CRM kota"),
      ("b", "K", "API CRM dua arah", "T3", "integrasi CRM"),
      ("c", "S", "Tiket, klasifikasi, target penyelesaian", "T3", "services/ticket"),
      ("d", "S", "Diagnosis: jenis keluhan dipetakan ke data hitungan dan nyala lampu", "T3", "services/metrics"),
      ("e", "S", "Pemutaran ulang kondisi saat keluhan", "T3", "PostgreSQL"),
      ("f", "U", "Operator menindaklanjuti; tiket kerja bila perlu", "T3", "apps/tmc-web"),
      ("g", "P", "Jawaban ke pelapor; status dapat dilihat publik", "T3", "CRM kota, dashboard publik")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("d", "f", ""), ("e", "f", ""), ("f", "g", "")])

flow("F11", "Simulasi SUMO, digital twin, dan mode bayangan",
     "Sejak T2 setiap rekomendasi diuji di SUMO dengan jaringan yang dibangun dari konfigurasi simpang. T3 mengkalibrasi twin per simpang dengan hitungan Vision Tracker. T4 menambah mode bayangan untuk algoritma adaptif. T5 membuka pasar algoritma.",
     [("a", "S", "Jaringan simulasi dibangun dari konfigurasi simpang atau OSM", "T2", "sim/"),
      ("b", "S", "Kalibrasi twin per simpang dengan hitungan Vision Tracker", "T3", "sim/"),
      ("c", "S", "Skenario: jadwal baru (T2), insiden dan acara (T4), kebijakan TDM (T5)", "T2", "sim/"),
      ("d", "S", "Pekerja simulasi menjalankan beberapa bilangan acak", "T2", "sim/ worker"),
      ("e", "S", "Mode bayangan: algoritma menerima data hidup tanpa mengendalikan lampu", "T4", "shadow harness"),
      ("f", "S", "Veto statistik dan uji konflik prioritas", "T4", "services/adaptive"),
      ("g", "P", "Universitas atau vendor mengajukan algoritma", "T5", "portal mitra"),
      ("h", "S", "Promosi bertahap: jam sepi, jam sibuk, hidup-mati", "T4", "services/adaptive"),
      ("i", "U", "Hasil validasi di dashboard dan laporan", "T2", "apps/tmc-web")],
     [("a", "b", "T3"), ("a", "c", ""), ("b", "c", ""), ("c", "d", ""), ("d", "i", ""), ("d", "e", "T4"), ("e", "f", ""), ("f", "h", ""), ("g", "d", "T5"), ("h", "i", "")])

flow("F12", "Platform banyak kota, data terbuka, dan pengelolaan permintaan perjalanan",
     "Di T5 satu platform melayani banyak kota dengan data terpisah, membandingkan kinerja antar kota, mengoptimasi koridor dan jaringan, menghitung ambang legal kebijakan pembatasan, dan membuka data lewat API publik.",
     [("a", "P", "Kota-kota sebagai tenant; Kemenhub/BPTJ; provinsi", "T5", "tenant"),
      ("b", "S", "Isolasi data per tenant dan yurisdiksi", "T4", "apps/api"),
      ("c", "S", "Optimasi koridor dan jaringan (bandwidth, Link Pivot, perimeter)", "T5", "services/network"),
      ("d", "S", "Benchmark antar kota; kalkulator ambang kebijakan pembatasan", "T5", "services/tdm"),
      ("e", "S", "Penasihat pembelajaran mesin yang hanya mengusulkan parameter", "T5", "services/advisor"),
      ("f", "K", "API publik dan data terbuka; integrasi ERP dan ganjil-genap", "T5", "API gateway"),
      ("g", "U", "Portal data terbuka dan dashboard benchmark", "T5", "apps/tmc-web"),
      ("h", "P", "Aplikasi navigasi, peneliti, warga", "T5", "")],
     [("a", "b", ""), ("b", "c", ""), ("b", "d", ""), ("b", "e", ""), ("c", "f", ""), ("d", "f", ""), ("d", "g", ""), ("f", "h", ""), ("g", "h", "")])

OVERVIEW = dict(id="F00", judul="Gambaran keseluruhan komponen IRAMA per lapisan dan tahap",
    lanes={
        "P": [("Engineer Dishub", "T1"), ("Kepala Dinas & pimpinan", "T2"), ("Operator ruang kendali", "T3"), ("Warga (aduan, publik)", "T3"), ("Operator bus, 112/119", "T4"), ("Polri & Back Office ETLE", "T4"), ("Kota lain, BPTJ, navigasi", "T5")],
        "U": [("Formulir & dashboard dasar", "T1"), ("Wizard konfigurasi", "T2"), ("Dashboard 3 halaman", "T2"), ("Laporan Word/PDF", "T2"), ("Konsol pemantauan & tiket", "T3"), ("Dashboard publik", "T3"), ("Konsol kendali & video wall", "T4"), ("Portal data & benchmark", "T5")],
        "S": [("Vision Tracker: hitung kelas", "T1"), ("Kalkulator PKJI & optimasi", "T1"), ("Periode, manfaat, SUMO", "T2"), ("Hambatan samping & nyala lampu", "T2"), ("Kejadian & kesehatan kamera", "T3"), ("Tiket & laporan wajib", "T3"), ("Controller baca-saja & jadwal", "T3"), ("Kendali terpusat & adaptif", "T4"), ("Prioritas bus & darurat", "T4"), ("Integrasi instansi", "T4"), ("Optimasi koridor & jaringan", "T5"), ("Multi-tenant, TDM, penasihat", "T5")],
        "K": [("Berkas rekaman", "T1"), ("Stream lokal (MediaMTX)", "T2"), ("Stream Dishub via VPN", "T3"), ("MQTT + mTLS", "T4"), ("API mitra (ICD)", "T4"), ("API publik", "T5")],
        "L": [("CCTV & rekamannya", "T1"), ("Controller (baca-saja)", "T3"), ("Edge Jetson/IPC", "T4"), ("Kamera ANPR khusus", "T4"), ("Controller NTCIP/vendor", "T4"), ("Fusi radar & GLOSA", "T5")],
    })

# ------------------------------------------------------------------ diagram arsitektur alur data (dokumen 14)
# kolom: (judul kolom, [(id, judul blok, teknologi, tahap)])
PIPE_COLS = [
    ("Sumber video", [
        ("V1", "Rekaman CCTV dan video publik", "MP4/MKV, register sumber rekaman", "T1"),
        ("V2", "Stream CCTV", "RTSP/HLS/ONVIF; uji lewat MediaMTX (T2), stream Dishub setelah MoU (T3)", "T2"),
    ]),
    ("Vision Tracker", [
        ("A1", "Ambil bingkai", "FFmpeg, OpenCV", "T1"),
        ("A2", "Deteksi enam kelas kendaraan", "RF-DETR/YOLOX lewat ONNX Runtime (CPU/iGPU)", "T1"),
        ("A3", "Pelacakan dan hitung per pendekat", "ByteTrack, supervision; arah dari lintasan (T2)", "T1"),
        ("A4", "Hambatan samping, nyala lampu, antrian", "logika IRAMA, OpenCV; penyamaran wajah dan pelat", "T2"),
        ("A5", "Kejadian dan kesehatan kamera", "model tambahan, aturan peringatan", "T3"),
    ]),
    ("Data terstruktur", [
        ("D1", "Tabel hitungan 15 menit dan mutu data", "PostgreSQL", "T1"),
        ("D2", "Hambatan samping, status lampu, antrian", "PostgreSQL (TimescaleDB opsional)", "T2"),
        ("D3", "Konfigurasi simpang dan parameter", "formulir (T1), wizard React + MapLibre (T2); PostgreSQL + PostGIS", "T1"),
        ("D4", "Peristiwa kejadian dan kesehatan kamera", "PostgreSQL, klip bukti tersamarkan", "T3"),
    ]),
    ("Optimasi waktu simpang", [
        ("O1", "Konversi SMP dan periode", "Python, EMP PKJI 2023; periode otomatis (T2)", "T1"),
        ("O2", "Kalkulator PKJI 2023", "NumPy, modul PKJI IRAMA; mode MKJI 1997 (T2)", "T1"),
        ("O3", "Mode optimasi", "SciPy; Webster (T1), empat mode (T2), multi-kriteria (T3)", "T1"),
        ("O4", "Validasi simulasi", "SUMO, TraCI", "T2"),
        ("O5", "Manfaat rupiah", "parameter UMK, BBM, emisi", "T2"),
    ]),
    ("Penyajian dan keputusan", [
        ("P1", "Dashboard simpang", "React, ECharts; versi dasar (T1), tiga halaman (T2)", "T1"),
        ("P2", "Laporan kajian Word/PDF", "python-docx, LibreOffice", "T2"),
        ("P3", "Keputusan engineer dan Kepala Dinas", "persetujuan dan jejak audit", "T2"),
        ("P4", "Konsol pemantauan kejadian", "React; notifikasi email/WhatsApp", "T3"),
    ]),
    ("Tindak lanjut", [
        ("R1", "Penerapan manual oleh petugas", "lembar jadwal dari dashboard atau laporan", "T2"),
        ("R2", "Ekspor jadwal dan uji sebelum-sesudah", "format tabel, NTCIP baca-saja", "T3"),
        ("R3", "Kendali controller dan adaptif", "adaptor NTCIP/vendor, edge, MQTT", "T4"),
        ("R4", "Koordinasi koridor dan jaringan", "offset, bandwidth, Link Pivot; twin kota", "T5"),
        ("R5", "Tiket kerja dan tindak lanjut kejadian", "tiket, email/WhatsApp, laporan wajib", "T3"),
    ]),
]
# panah antarblok: (dari, ke, label)
PIPE_EDGES = [("V1", "A1", ""), ("V2", "A1", ""),
              ("A1", "A2", ""), ("A2", "A3", ""), ("A3", "A4", ""), ("A4", "A5", ""),
              ("A3", "D1", ""), ("A4", "D2", ""), ("A5", "D4", ""),
              ("D1", "O1", ""), ("D2", "O2", ""), ("D3", "O2", ""),
              ("O1", "O2", ""), ("O2", "O3", ""), ("O3", "O4", ""), ("O4", "O5", ""),
              ("O3", "P1", ""), ("O4", "P1", ""), ("O5", "P1", ""),
              ("P1", "P2", ""), ("P2", "P3", ""),
              ("P3", "R1", ""), ("P3", "R2", ""), ("P3", "R3", ""), ("R3", "R4", ""), ("P4", "R5", "")]
# jalur khusus yang dilewatkan di bawah kolom: (dari, ke, label, gaya garis)
PIPE_SPECIAL = [("D4", "P4", "T3: peristiwa kejadian langsung ke konsol pemantauan, tanpa melalui optimasi", "-"),
                ("R2", "V2", "T3: uji sebelum-sesudah; rekaman sesudah penerapan diukur ulang oleh Vision Tracker", "--")]

# ------------------------------------------------------------------ render
# Kanvas memakai sumbu penuh sehingga 1 satuan data = 1 inci; ukuran huruf dalam poin.
LINE = "#455A64"
FS_BOX, FS_LAB, FS_LANE, FS_LEG = 5.4, 5.2, 7.0, 5.8
LANE_H, BW, BH, PITCH, X0, HEAD = 1.14, 1.22, 0.74, 1.60, 1.45, 0.72

def wrap(t, w=22):
    return "\n".join(textwrap.wrap(t, w))

def canvas(w, h):
    fig = plt.figure(figsize=(w, h), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax

def extent(fig, t):
    """Batas teks dalam inci: (x0, y0, x1, y1), tanpa bantalan latar."""
    bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
    return (bb.x0 / fig.dpi, bb.y0 / fig.dpi, bb.x1 / fig.dpi, bb.y1 / fig.dpi)

def legend(fig, ax, x_right, y, fs=FS_LEG):
    """Legenda tahap rata kanan. Jarak antarlabel dihitung dari lebar teks sebenarnya."""
    pad = 0.35
    pad_in = pad * fs / 72.0
    x = x_right - pad_in
    for st in reversed(list(STAGE_COLOR)):
        t = ax.text(x, y, STAGE_NAME[st], fontsize=fs, ha="right", va="center", color="white",
                    bbox=dict(boxstyle="round,pad=%.2f" % pad, fc=STAGE_COLOR[st], ec="none"))
        x = extent(fig, t)[0] - 2 * pad_in - 0.09
    return x + pad_in

def fit_text(fig, ax, x, y, text, maxw, fs, **kw):
    """Bungkus teks dengan lebar baris terbesar yang masih muat dalam maxw inci."""
    for n in range(48, 7, -1):
        t = ax.text(x, y, wrap(text, n), fontsize=fs, **kw)
        e = extent(fig, t)
        if e[2] - e[0] <= maxw:
            return t
        t.remove()
    return ax.text(x, y, wrap(text, 8), fontsize=fs, **kw)

def draw_box(fig, ax, x0, y0, w, h, text, st, sid=None, fs=FS_BOX):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.05",
                                fc="white", ec=STAGE_COLOR[st], lw=1.2, zorder=2))
    fit_text(fig, ax, x0 + 0.06, y0 + h / 2 - 0.04, text, w - 0.12, fs, va="center", ha="left",
             color="#212121", linespacing=1.15, zorder=4)
    ax.text(x0 + w - 0.03, y0 + h - 0.03, st, fontsize=5.6, ha="right", va="top", color="white", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.15", fc=STAGE_COLOR[st], ec="none"), zorder=4)
    if sid:
        ax.text(x0 + 0.045, y0 + h - 0.035, sid, fontsize=5.2, ha="left", va="top", color="#616161", zorder=4)

def draw_path(ax, pts, color=LINE, ls="-", lw=0.8, rad=0.05):
    """Garis siku dengan sudut membulat dan kepala panah di ujung."""
    verts, codes = [pts[0]], [Path.MOVETO]
    for i in range(1, len(pts) - 1):
        (xa, ya), (xb, yb), (xc, yc) = pts[i - 1], pts[i], pts[i + 1]
        l1 = abs(xb - xa) + abs(yb - ya); l2 = abs(xc - xb) + abs(yc - yb)
        r = min(rad, l1 / 2, l2 / 2)
        verts += [(xb - (xb - xa) / l1 * r, yb - (yb - ya) / l1 * r), (xb, yb), (xb + (xc - xb) / l2 * r, yb + (yc - yb) / l2 * r)]
        codes += [Path.LINETO, Path.CURVE3, Path.CURVE3]
    verts.append(pts[-1]); codes.append(Path.LINETO)
    ax.add_patch(FancyArrowPatch(path=Path(verts, codes), arrowstyle="-|>", mutation_scale=8, lw=lw,
                                 color=color, linestyle=ls, zorder=3))

# ---- perutean panah ortogonal: garis hanya lewat celah antarkolom dan jalur di tepi lajur
def _segs(pts):
    return [(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]) for i in range(len(pts) - 1)]

def _is_v(g):
    return abs(g[0] - g[2]) < 1e-9

def _hits(g, box, m):
    x0, y0, x1, y1 = box[0] - m, box[1] - m, box[2] + m, box[3] + m
    if _is_v(g):
        ya, yb = sorted((g[1], g[3]))
        return x0 < g[0] < x1 and ya < y1 and yb > y0
    xa, xb = sorted((g[0], g[2]))
    return y0 < g[1] < y1 and xa < x1 and xb > x0

def _close(a, b, tol=0.045):
    if _is_v(a) and _is_v(b) and abs(a[0] - b[0]) < tol:
        lo = max(min(a[1], a[3]), min(b[1], b[3])); hi = min(max(a[1], a[3]), max(b[1], b[3]))
        return hi - lo > 0.02
    if not _is_v(a) and not _is_v(b) and abs(a[1] - b[1]) < tol:
        lo = max(min(a[0], a[2]), min(b[0], b[2])); hi = min(max(a[0], a[2]), max(b[0], b[2]))
        return hi - lo > 0.02
    return False

def _cross(a, b):
    if _is_v(a) == _is_v(b):
        return False
    v, h = (a, b) if _is_v(a) else (b, a)
    return min(h[0], h[2]) < v[0] < max(h[0], h[2]) and min(v[1], v[3]) < h[1] < max(v[1], v[3])

def _touch(pt, g, tol=0.03):
    x, y = pt
    if _is_v(g):
        return abs(x - g[0]) < tol and min(g[1], g[3]) - tol <= y <= max(g[1], g[3]) + tol
    return abs(y - g[1]) < tol and min(g[0], g[2]) - tol <= x <= max(g[0], g[2]) + tol

def _rect_ov(a, b, m=0.0):
    return a[0] < b[2] + m and a[2] > b[0] - m and a[1] < b[3] + m and a[3] > b[1] - m

def _seg_rect(g, r):
    return _hits(g, r, 0.0)

TDIR = {"L": (1, 0), "R": (-1, 0), "T": (0, -1), "B": (0, 1)}   # arah gerak saat tiba di port

class Router:
    def __init__(self, boxes, xtracks, ytracks, margin=0.04):
        self.boxes = boxes
        self.xt = sorted(set(round(x, 4) for x in xtracks))
        self.yt = sorted(set(round(y, 4) for y in ytracks))
        self.m = margin
        self.done = []          # (dari, ke, titik)

    def ports(self, b):
        x0, y0, x1, y1 = self.boxes[b]
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        return {"R": ((x1, cy), (1, 0)), "L": ((x0, cy), (-1, 0)), "T": ((cx, y1), (0, 1)), "B": ((cx, y0), (0, -1))}

    def _near_x(self, x, d, k=6):
        xs = [t for t in self.xt if (t - x) * d > 1e-6]
        return sorted(xs, key=lambda t: abs(t - x))[:k]

    def _shapes(self, sp, sd, tp, td):
        out = []
        (sx, sy), (tx, ty) = sp, tp
        sh, th = sd[1] == 0, td[1] == 0
        if sh and th:
            if abs(sy - ty) < 1e-9 and sd == td and (tx - sx) * sd[0] > 0:
                out.append([sp, tp])
            for x in self.xt:
                if (x - sx) * sd[0] > 1e-6 and (tx - x) * td[0] > 1e-6:
                    out.append([sp, (x, sy), (x, ty), tp])
            for x1 in self._near_x(sx, sd[0]):
                for x2 in self._near_x(tx, -td[0]):
                    for y in self.yt:
                        out.append([sp, (x1, sy), (x1, y), (x2, y), (x2, ty), tp])
        elif not sh and not th:
            if abs(sx - tx) < 1e-9 and sd == td and (ty - sy) * sd[1] > 0:
                out.append([sp, tp])
            for y in self.yt:
                if (y - sy) * sd[1] > 1e-6 and (ty - y) * td[1] > 1e-6:
                    out.append([sp, (sx, y), (tx, y), tp])
        elif sh:
            if (tx - sx) * sd[0] > 1e-6 and (ty - sy) * td[1] > 1e-6:
                out.append([sp, (tx, sy), tp])
            for x1 in self._near_x(sx, sd[0]):
                for y in self.yt:
                    if (ty - y) * td[1] > 1e-6:
                        out.append([sp, (x1, sy), (x1, y), (tx, y), tp])
        else:
            if (ty - sy) * sd[1] > 1e-6 and (tx - sx) * td[0] > 1e-6:
                out.append([sp, (sx, ty), tp])
            for y in self.yt:
                if (y - sy) * sd[1] > 1e-6:
                    for x2 in self._near_x(tx, -td[0]):
                        out.append([sp, (sx, y), (x2, y), (x2, ty), tp])
        return out

    @staticmethod
    def _base(pts):
        segs = _segs(pts)
        return 0.5 * (len(segs) - 1) + 0.3 * sum(abs(g[2] - g[0]) + abs(g[3] - g[1]) for g in segs)

    def _valid(self, pts, s, t):
        segs = _segs(pts); n = len(segs)
        for i, g in enumerate(segs):
            if abs(g[0] - g[2]) < 1e-9 and abs(g[1] - g[3]) < 1e-9:
                return False
            for b, box in self.boxes.items():
                if (b == s and i == 0) or (b == t and i == n - 1):
                    continue
                if _hits(g, box, self.m):
                    return False
        return True

    def _penalty(self, pts, s, t, lab=None):
        p = 0.0
        segs = _segs(pts)
        for s2, t2, pts2 in self.done:
            share = (s2 == s) or (t2 == t)
            segs2 = _segs(pts2)
            for b in segs2:
                for a in segs:
                    if _close(a, b):
                        p += 0.0 if share else 40.0
                    elif _cross(a, b):
                        p += 1.0
            if not share:   # titik belok yang menempel garis lain
                p += 8.0 * sum(1 for v in pts[1:-1] for b in segs2 if _touch(v, b))
                p += 8.0 * sum(1 for v in pts2[1:-1] for a in segs if _touch(v, a))
        if lab:             # sediakan ruang untuk label: segmen datar cukup panjang atau segmen tegak cukup tinggi
            lw, lh = lab
            ok = any((not _is_v(g) and abs(g[2] - g[0]) >= lw + 0.12) or (_is_v(g) and abs(g[3] - g[1]) >= lh + 0.3) for g in segs)
            if not ok:
                p += 3.0
        return p

    def route(self, s, t, lab=None):
        cands = []
        for sn, (sp, sd) in self.ports(s).items():
            for tn, (tp, _) in self.ports(t).items():
                for pts in self._shapes(sp, sd, tp, TDIR[tn]):
                    cands.append((self._base(pts), len(cands), pts))
        cands.sort()
        best, best_sc = None, 1e18
        for base, _, pts in cands:
            if base >= best_sc:
                break
            if not self._valid(pts, s, t):
                continue
            sc = base + self._penalty(pts, s, t, lab)
            if sc < best_sc:
                best, best_sc = pts, sc
        if best is None:
            raise RuntimeError("tidak ada rute untuk %s -> %s" % (s, t))
        self.done.append((s, t, best))
        self.last_score = best_sc
        return best

    def improve(self, items, passes=4):
        """Rute ulang: tiap panah dilepas lalu dirutekan lagi terhadap panah lain; dipakai bila skornya lebih baik.
        items: daftar [kunci, asal, tujuan, ukuran_label, titik]; titik diperbarui di tempat."""
        for _ in range(passes):
            changed = False
            for it in items:
                key, s, t, lab, pts = it
                i = next(j for j, d in enumerate(self.done) if d[2] is pts)
                cur = self.done.pop(i)
                cur_sc = self._base(pts) + self._penalty(pts, s, t, lab)
                new = self.route(s, t, lab)
                if self.last_score < cur_sc - 1e-6:
                    it[4] = new
                    changed = True
                else:
                    self.done.pop()
                    self.done.insert(i, cur)
            if not changed:
                break

    def add(self, s, t, pts):
        self.done.append((s, t, pts))

    def label(self, fig, ax, pts, text, placed, fs=FS_LAB, color=LINE, bold=False):
        """Letakkan label di atas garis pada posisi yang tidak menabrak kotak atau label lain."""
        tmp = ax.text(0, 0, text, fontsize=fs, fontweight="bold" if bold else "normal")
        e = extent(fig, tmp); tmp.remove()
        w, h = (e[2] - e[0]) + 0.07, (e[3] - e[1]) + 0.05
        best, bsc = None, 1e18
        cands = []
        for g in _segs(pts):
            L = abs(g[2] - g[0]) + abs(g[3] - g[1]); hz = not _is_v(g)
            for f in (0.5, 0.38, 0.62, 0.25, 0.75, 0.12, 0.88):
                px, py = g[0] + (g[2] - g[0]) * f, g[1] + (g[3] - g[1]) * f
                cands.append((px, py, 0.0, g, L, hz, f))
                # cadangan: label di samping garis, bukan menutupi garis
                if hz:
                    cands += [(px, py + h / 2 + 0.012, 1.2, g, L, hz, f), (px, py - h / 2 - 0.012, 1.2, g, L, hz, f)]
                else:
                    cands += [(px + w / 2 + 0.02, py, 1.2, g, L, hz, f), (px - w / 2 - 0.02, py, 1.2, g, L, hz, f)]
        for cx, cy, side, g, L, hz, f in cands:
                r = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
                if any(_rect_ov(r, b, 0.015) for b in self.boxes.values()):
                    continue
                if any(_rect_ov(r, q, 0.01) for q in placed):
                    continue
                sc = side + abs(f - 0.5) + (0.0 if (hz and L > w + 0.08) else (0.7 if (not hz and L > h + 0.1) else 2.5))
                sc += 1.5 * sum(1 for (_, _, p2) in self.done if p2 is not pts for g2 in _segs(p2) if _seg_rect(g2, r))
                if sc < bsc:
                    best, bsc = (cx, cy, r), sc
        if best is None:
            g = max(_segs(pts), key=lambda g: abs(g[2] - g[0]) + abs(g[3] - g[1]))
            cx, cy = (g[0] + g[2]) / 2, (g[1] + g[3]) / 2
            best = (cx, cy, (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2))
            print("  peringatan: label '%s' tidak mendapat posisi bebas" % text)
        cx, cy, r = best
        placed.append(r)
        ax.text(cx, cy, text, fontsize=fs, fontweight="bold" if bold else "normal", ha="center", va="center", color=color,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"), zorder=5)

def edge_style(lab):
    if lab[:2] in STAGE_COLOR:
        return STAGE_COLOR[lab[:2]], True
    return LINE, False

# ---- tata letak kolom: langkah ditempatkan sedekat mungkin setelah pendahulunya, satu kotak per sel
def layout(steps, edges, hint):
    order = [s[0] for s in steps]
    idx = {s: i for i, s in enumerate(order)}
    lane = {s[0]: LANE_IDX[s[1]] for s in steps}
    col, occ = {}, set()
    for sid in order:
        c = max([col[a] + 1 for a, b, _ in edges if b == sid and idx[a] < idx[sid]], default=0)
        c = hint.get(sid, c)
        while (c, lane[sid]) in occ:
            c += 1
        col[sid] = c; occ.add((c, lane[sid]))
    for sid in order:   # langkah awal tanpa panah masuk ditarik ke dekat penerusnya
        if sid in hint or any(b == sid for a, b, _ in edges):
            continue
        succ = [col[b] for a, b, _ in edges if a == sid]
        if succ:
            want = min(succ) - 1
            if want > col[sid] and (want, lane[sid]) not in occ:
                occ.discard((col[sid], lane[sid])); col[sid] = want; occ.add((want, lane[sid]))
    return col, lane

def draw_flow(f, out_png):
    steps, edges = f["steps"], f["edges"]
    col, lane = layout(steps, edges, f.get("hint") or {})
    ncols = max(col.values()) + 1
    nl = len(LANES)
    fig_w = X0 + ncols * PITCH + 0.06
    fig_h = HEAD + nl * LANE_H + 0.04
    fig, ax = canvas(fig_w, fig_h)
    top = fig_h - HEAD
    ltop = lambda i: top - i * LANE_H
    obst = {}
    for i, (k, name) in enumerate(LANES):
        y0 = ltop(i + 1)
        ax.add_patch(Rectangle((0, y0), fig_w, LANE_H, facecolor=LANE_FILL[i], edgecolor="#BDBDBD", lw=0.6, zorder=1))
        t = ax.text(0.1, y0 + LANE_H / 2, name, va="center", ha="left", fontsize=FS_LANE, color="#37474F", fontweight="bold", zorder=4)
        obst["_lajur%d" % i] = extent(fig, t)
    ax.text(0.1, fig_h - 0.22, "%s  %s" % (f["id"], f["judul"]), fontsize=9.5, fontweight="bold", va="center")
    legend(fig, ax, fig_w - 0.1, fig_h - 0.52)
    boxes = {}
    for sid, ln, text, st, comp in steps:
        x0 = X0 + col[sid] * PITCH
        yc = ltop(lane[sid]) - LANE_H / 2
        boxes[sid] = (x0, yc - BH / 2, x0 + BW, yc + BH / 2)
        draw_box(fig, ax, x0, yc - BH / 2, BW, BH, text, st, sid)
    xt = []
    for c in range(-1, ncols):
        g = X0 + c * PITCH + BW + (PITCH - BW) / 2
        xt += [g + o for o in (0.0, -0.07, 0.07, -0.14, 0.14)]
    yt = []
    for k in range(nl + 1):
        if k > 0:
            yt += [ltop(k) + 0.05, ltop(k) + 0.10]
        if k < nl:
            yt += [ltop(k) - 0.05, ltop(k) - 0.10]
    r = Router(dict(boxes, **obst), xt, yt)
    def dist(e):
        a, b = boxes[e[0]], boxes[e[1]]
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    def lab_size(lab):
        if not lab:
            return None
        c, bold = edge_style(lab)
        tmp = ax.text(0, 0, lab, fontsize=FS_LAB, fontweight="bold" if bold else "normal")
        e = extent(fig, tmp); tmp.remove()
        return ((e[2] - e[0]) + 0.07, (e[3] - e[1]) + 0.05)
    paths = {}
    items = []
    for i in sorted(range(len(edges)), key=lambda i: (dist(edges[i]), i)):
        a, b, lab = edges[i]
        ls = lab_size(lab)
        paths[i] = r.route(a, b, ls)
        items.append([i, a, b, ls, paths[i]])
    r.improve(items)
    for it in items:
        paths[it[0]] = it[4]
    for i, (a, b, lab) in enumerate(edges):
        draw_path(ax, paths[i])
    placed = []
    for i, (a, b, lab) in enumerate(edges):
        if lab:
            c, bold = edge_style(lab)
            r.label(fig, ax, paths[i], lab, placed, color=c, bold=bold)
    fig.savefig(out_png, bbox_inches="tight", pad_inches=0.04); plt.close(fig)

def draw_overview(o, out_png):
    ncol = max(len(v) for v in o["lanes"].values())
    obw, opitch, olh, obh = 1.10, 1.22, 0.86, 0.56
    fig_w = X0 + ncol * opitch + 0.05
    fig_h = HEAD + len(LANES) * olh + 0.04
    fig, ax = canvas(fig_w, fig_h)
    top = fig_h - HEAD
    for i, (k, name) in enumerate(LANES):
        y0 = top - (i + 1) * olh
        ax.add_patch(Rectangle((0, y0), fig_w, olh, facecolor=LANE_FILL[i], edgecolor="#BDBDBD", lw=0.6, zorder=1))
        ax.text(0.1, y0 + olh / 2, name, va="center", ha="left", fontsize=FS_LANE, color="#37474F", fontweight="bold")
        for j, (text, st) in enumerate(o["lanes"][k]):
            draw_box(fig, ax, X0 + j * opitch, y0 + (olh - obh) / 2, obw, obh, text, st, fs=5.4)
    ax.text(0.1, fig_h - 0.22, "%s  %s" % (o["id"], o["judul"]), fontsize=9.5, fontweight="bold", va="center")
    legend(fig, ax, fig_w - 0.1, fig_h - 0.52)
    fig.savefig(out_png, bbox_inches="tight", pad_inches=0.04); plt.close(fig)

# ------------------------------------------------------------------ mermaid & markdown
def mermaid(f):
    lines = ["flowchart LR"]
    for k, name in LANES:
        ss = [s for s in f["steps"] if s[1] == k]
        if not ss:
            continue
        lines.append('  subgraph %s["%s"]' % (k, name.replace("\n", " ")))
        for sid, lane, text, st, comp in ss:
            lines.append('    %s%s["%s. %s (%s)"]' % (f["id"], sid, sid, text.replace('"', "'"), st))
        lines.append("  end")
    for a, b, lab in f["edges"]:
        lines.append("  %s%s -->%s %s%s" % (f["id"], a, ("|%s|" % lab) if lab else "", f["id"], b))
    for st, c in STAGE_COLOR.items():
        ids = [f["id"] + s[0] for s in f["steps"] if s[3] == st]
        if ids:
            lines.append("  classDef %s stroke:%s,stroke-width:2px" % (st.lower(), c))
            lines.append("  class %s %s" % (",".join(ids), st.lower()))
    return "\n".join(lines)

def rel_png(fid):
    name = sorted(x for x in os.listdir(HERE) if x.startswith(fid) and x.endswith(".png"))
    return "diagram/" + (name[0] if name else fid + ".png")

def md_section(sederhana):
    out = []
    out.append("## %sDiagram alur fitur utama dan pemetaannya ke arsitektur dan tahap\n" % ("" if sederhana else "9. "))
    out.append("Diagram berikut menggambarkan cara IRAMA bekerja pada kondisi end-state, satu diagram per fitur utama. Cara membacanya sama untuk semua diagram.\n")
    out.append("- Baris (lajur mendatar) adalah lapisan arsitektur: pengguna dan mitra eksternal, penyajian, pusat, komunikasi dan integrasi, lapangan. Posisi kotak menunjukkan komponen mana yang menjalankan langkah itu.")
    out.append("- Kotak adalah langkah, diberi huruf urut dan warna bingkai. Label kecil di pojok kanan atas (T1 sampai T5) menandai tahap saat langkah itu pertama tersedia. Warna: T1 hijau, T2 biru, T3 jingga, T4 ungu, T5 merah.")
    out.append("- Panah adalah aliran data atau perintah. Label abu-abu pada panah menjelaskan kondisi, misalnya \"bila putus\". Label berwarna, misalnya T3, berarti hubungan itu baru ada mulai tahap tersebut.")
    out.append("- Untuk membaca diagram pada tahap tertentu, abaikan kotak yang labelnya lebih tinggi dari tahap itu. Contoh: pada T2, kotak berlabel T3 sampai T5 belum ada, dan alur berhenti pada kotak terakhir yang tersedia.\n")
    out.append("Tabel di bawah tiap diagram memetakan langkah ke komponen dalam struktur repositori (apps, services, edge, sim, infra) dan tahapnya. Diagram direvisi 2026-09-14 mengikuti tahapan baru: T1 purwarupa, T2 Vision Tracker dan optimasi, T3 deteksi kejadian dan pemantauan, T4 kendali adaptif, T5 platform kota. Diagram arsitektur alur data per komponen dan teknologi (A01) ada di dokumen 14.\n")
    out.append("### F00 Gambaran keseluruhan komponen per lapisan dan tahap\n")
    out.append("![F00](%s)\n" % rel_png("F00"))
    out.append("Diagram ini memperlihatkan semua komponen yang ada pada end-state, dikelompokkan per lapisan, dengan label tahap pemunculannya. Diagram F01 sampai F12 memperlihatkan bagaimana komponen tersebut bekerja sama untuk tiap fitur.\n")
    for f in FLOWS:
        if sederhana:
            out.append("<<<PAGEBREAK>>>\n")
        out.append("### %s %s\n" % (f["id"], f["judul"]))
        out.append(f["tujuan"] + "\n")
        out.append("![%s](%s)\n" % (f["id"], rel_png(f["id"])))
        stages = sorted({s[3] for s in f["steps"]})
        out.append("Tahap yang terlibat: %s. Langkah dan komponennya:\n" % ", ".join(stages))
        out.append("| Langkah | Lapisan | Komponen | Tahap |")
        out.append("|---|---|---|---|")
        for sid, lane, text, st, comp in f["steps"]:
            out.append("| %s. %s | %s | %s | %s |" % (sid, text, dict(LANES)[lane].split("\n")[0].replace(" &", ""), comp or "(pihak luar)", st))
        out.append("")
        if not sederhana:
            out.append("Versi teks (mermaid):\n")
            out.append("```mermaid\n%s\n```\n" % mermaid(f))
    return "\n".join(out)

# ------------------------------------------------------------------ gambar diagram arsitektur alur data (A01)
def draw_pipeline(out_png):
    ncol = len(PIPE_COLS)
    colw, cgap, left = 2.2, 0.52, 0.15
    bw, bh, bgap, th = colw - 0.24, 0.74, 0.30, 0.44
    head = 1.0
    col_h = lambda n: th + n * bh + (n - 1) * bgap + 0.16
    maxb = max(len(b) for _, b in PIPE_COLS)
    fig_w = left + ncol * colw + (ncol - 1) * cgap + 0.45
    fig_h = head + col_h(maxb) + 0.95
    fig, ax = canvas(fig_w, fig_h)
    ax.text(left, fig_h - 0.3, "A01  Arsitektur alur data IRAMA per komponen, teknologi, dan tahap",
            fontsize=12, fontweight="bold", va="center")
    ax.text(left, fig_h - 0.68, "Label warna di pojok kotak menunjukkan tahap saat komponen pertama tersedia. Garis putus-putus menunjukkan umpan balik.",
            fontsize=7, va="center", color="#455A64")
    legend(fig, ax, fig_w - 0.1, fig_h - 0.68, fs=6.6)
    top = fig_h - head
    boxes, colbox = {}, []
    for ci, (ctitle, blocks) in enumerate(PIPE_COLS):
        x0 = left + ci * (colw + cgap)
        h = col_h(len(blocks))
        ax.add_patch(FancyBboxPatch((x0, top - h), colw, h, boxstyle="round,pad=0,rounding_size=0.08",
                                    fc="#EEF3F8" if ci % 2 else "#F5F5F5", ec="#B0BEC5", lw=0.8, zorder=1))
        colbox.append((x0, top - h, x0 + colw, top))
        ax.text(x0 + colw / 2, top - th / 2, ctitle, ha="center", va="center", fontsize=8.5, fontweight="bold", color="#263238")
        for bi, (bid, title, tech, st) in enumerate(blocks):
            bx0 = x0 + (colw - bw) / 2
            by1 = top - th - bi * (bh + bgap)
            boxes[bid] = (bx0, by1 - bh, bx0 + bw, by1)
            ax.add_patch(FancyBboxPatch((bx0, by1 - bh), bw, bh, boxstyle="round,pad=0,rounding_size=0.05",
                                        fc="white", ec=STAGE_COLOR[st], lw=1.3, zorder=2))
            t1 = fit_text(fig, ax, bx0 + 0.08, by1 - 0.16, title, bw - 0.16, 6.6, fontweight="bold", va="top", ha="left",
                          color="#212121", zorder=4)
            fit_text(fig, ax, bx0 + 0.08, extent(fig, t1)[1] - 0.05, tech, bw - 0.16, 5.6, style="italic", va="top", ha="left",
                     color="#455A64", zorder=4)
            ax.text(bx0 + bw - 0.03, by1 - 0.03, st, fontsize=6, ha="right", va="top", color="white", fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.15", fc=STAGE_COLOR[st], ec="none"), zorder=4)
    xt = []
    for ci in range(ncol - 1):
        g = left + ci * (colw + cgap) + colw + cgap / 2
        xt += [g + o for o in (0.0, -0.08, 0.08, -0.16, 0.16)]
    r = Router(boxes, xt, [])
    # jalur khusus di bawah kolom dicadangkan lebih dulu
    low = min(c[1] for c in colbox)
    ybands = [low - 0.30, low - 0.64]
    special = []
    for k, (a, b, lab, ls) in enumerate(PIPE_SPECIAL):
        A, B = boxes[a], boxes[b]
        y = ybands[k]
        if ls == "-":   # dari bawah blok asal ke bawah blok tujuan
            pts = [((A[0] + A[2]) / 2, A[1]), ((A[0] + A[2]) / 2, y), ((B[0] + B[2]) / 2, y), ((B[0] + B[2]) / 2, B[1])]
            color = STAGE_COLOR[lab[:2]]
        else:           # umpan balik: keluar sisi kanan, turun di luar kolom, kembali ke sumber video
            xr = colbox[-1][2] + 0.16
            pts = [(A[2], (A[1] + A[3]) / 2), (xr, (A[1] + A[3]) / 2), (xr, y), ((B[0] + B[2]) / 2, y), ((B[0] + B[2]) / 2, B[1])]
            color = LINE
        r.add("_khusus%d" % k, "_khusus%d" % k, pts)
        special.append((pts, lab, ls, color))
    def dist(e):
        a, b = boxes[e[0]], boxes[e[1]]
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    paths = {}
    items = []
    for i in sorted(range(len(PIPE_EDGES)), key=lambda i: (dist(PIPE_EDGES[i]), i)):
        a, b, lab = PIPE_EDGES[i]
        paths[i] = r.route(a, b)
        items.append([i, a, b, None, paths[i]])
    r.improve(items)
    for it in items:
        paths[it[0]] = it[4]
    for i in paths:
        draw_path(ax, paths[i], lw=0.9)
    placed = []
    for pts, lab, ls, color in special:
        draw_path(ax, pts, color=color, ls=ls, lw=1.0)
        r.label(fig, ax, pts, lab, placed, fs=6.2, color=STAGE_COLOR[lab[:2]], bold=False)
    fig.savefig(out_png, bbox_inches="tight", pad_inches=0.08); plt.close(fig)

def mermaid_pipeline():
    lines = ["flowchart LR"]
    for ci, (ctitle, blocks) in enumerate(PIPE_COLS):
        lines.append('  subgraph C%d["%s"]' % (ci, ctitle))
        for bid, title, tech, st in blocks:
            lines.append('    %s["%s (%s)<br/><i>%s</i>"]' % (bid, title, st, tech.replace('"', "'")))
        lines.append("  end")
    for a, b, lab in PIPE_EDGES:
        lines.append("  %s -->%s %s" % (a, ("|%s|" % lab) if lab else "", b))
    for a, b, lab, ls in PIPE_SPECIAL:
        lines.append("  %s %s|%s| %s" % (a, "-->" if ls == "-" else "-.->", lab, b))
    return "\n".join(lines)

def md_pipeline(sederhana):
    out = []
    out.append("## %sArsitektur alur data, komponen, dan teknologi (A01)\n" % ("" if sederhana else "1. "))
    out.append("Diagram A01 merangkum alur kerja IRAMA dari kamera sampai keputusan. Video dari CCTV diolah Vision Tracker menjadi tabel hitungan per kelas kendaraan, per arah, dan per 15 menit. Tabel itu disimpan bersama konfigurasi simpang, lalu diolah modul Optimasi Waktu Simpang menjadi rekomendasi waktu siklus dan waktu hijau. Hasilnya tampil di dashboard dan laporan kajian sebagai bahan keputusan engineer dan Kepala Dinas. Setiap kotak mencantumkan teknologi yang dipakai dalam huruf miring.\n")
    out.append("Cara membaca diagram:\n")
    out.append("- Label warna di pojok kanan atas kotak menunjukkan tahap saat komponen itu pertama tersedia. T1 hijau, T2 biru, T3 jingga, T4 ungu, T5 merah.")
    out.append("- Untuk melihat kondisi sistem pada tahap tertentu, abaikan kotak dengan tahap lebih tinggi. Pada T2, misalnya, alur berjalan dari rekaman atau stream uji, melalui Vision Tracker dan optimasi, sampai dashboard, laporan, keputusan, dan penerapan manual oleh petugas.")
    out.append("- Panah tegak di dalam kolom menunjukkan urutan proses. Panah antarkolom menunjukkan data yang berpindah ke bagian berikutnya.")
    out.append("- Garis jingga di bawah kolom adalah jalur kejadian mulai T3. Peristiwa seperti ambulans lewat atau kamera tertutup langsung dikirim ke konsol pemantauan tanpa melalui optimasi.")
    out.append("- Garis putus-putus adalah umpan balik mulai T3. Setelah jadwal baru diterapkan, rekaman sesudahnya diukur ulang untuk membuktikan perubahan kinerja simpang.\n")
    if sederhana:
        out.append("<<<LANDSCAPE>>>\n")
    out.append("![A01](%s)\n" % rel_png("A01"))
    out.append("Rincian komponen, teknologi, dan tahap:\n")
    out.append("| Kolom | Komponen | Teknologi | Tahap |")
    out.append("|---|---|---|---|")
    for ctitle, blocks in PIPE_COLS:
        for bid, title, tech, st in blocks:
            out.append("| %s | %s | %s | %s |" % (ctitle, title, tech, st))
    out.append("")
    if sederhana:
        out.append("<<<PORTRAIT>>>\n")
    if not sederhana:
        out.append("Versi teks (mermaid):\n")
        out.append("```mermaid\n%s\n```\n" % mermaid_pipeline())
    return "\n".join(out)

def main():
    for fn in os.listdir(HERE):
        if fn.endswith(".png") and (fn.startswith("F") or fn.startswith("A0")):
            os.remove(os.path.join(HERE, fn))
    draw_overview(OVERVIEW, os.path.join(HERE, "F00_Gambaran_Keseluruhan.png"))
    for f in FLOWS:
        slug = ""
        for w in f["judul"].split(",")[0].split():   # potong di batas kata, maksimal 40 karakter
            if len(slug) + len(w) + (1 if slug else 0) > 40:
                break
            slug = (slug + "_" + w) if slug else w
        png = os.path.join(HERE, "%s_%s.png" % (f["id"], slug))
        draw_flow(f, png)
        io.open(os.path.join(HERE, "%s.mmd" % f["id"]), "w", encoding="utf-8", newline=chr(10)).write(mermaid(f))
        print("ok", os.path.basename(png))
    draw_pipeline(os.path.join(HERE, "A01_Arsitektur_Alur_Data.png"))
    io.open(os.path.join(HERE, "A01.mmd"), "w", encoding="utf-8", newline=chr(10)).write(mermaid_pipeline())
    io.open(os.path.join(HERE, "_bagian_diagram.md"), "w", encoding="utf-8", newline=chr(10)).write(md_section(False))
    io.open(os.path.join(HERE, "_bagian_diagram_sederhana.md"), "w", encoding="utf-8", newline=chr(10)).write(md_section(True))
    io.open(os.path.join(HERE, "_bagian_pipeline.md"), "w", encoding="utf-8", newline=chr(10)).write(md_pipeline(False))
    io.open(os.path.join(HERE, "_bagian_pipeline_sederhana.md"), "w", encoding="utf-8", newline=chr(10)).write(md_pipeline(True))
    print("markdown ok")

if __name__ == "__main__":
    main()
