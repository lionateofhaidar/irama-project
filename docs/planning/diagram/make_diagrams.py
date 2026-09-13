# -*- coding: utf-8 -*-
"""
Diagram alur fitur utama IRAMA (end-state) dengan pemetaan ke lapisan arsitektur dan tahap T1–T5.
Menghasilkan: PNG (docs/planning/diagram/F##_*.png), mermaid (docs/planning/diagram/F##_*.mmd),
dan potongan markdown (docs/planning/diagram/_bagian_diagram.md dan _bagian_diagram_sederhana.md)
untuk disisipkan ke dokumen 06 (kanonis dan versi docx).

Konvensi visual: baris (swimlane) = lapisan arsitektur; kotak = langkah; label warna di pojok kotak = tahap
saat langkah itu pertama kali tersedia (T1 hijau, T2 biru, T3 jingga, T4 ungu, T5 merah).
"""
import io, os, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
STAGE_COLOR = {"T1": "#2E7D32", "T2": "#1565C0", "T3": "#EF6C00", "T4": "#6A1B9A", "T5": "#C62828"}
STAGE_NAME = {"T1": "T1 MVP", "T2": "T2 Siap jual", "T3": "T3 Responsif", "T4": "T4 Adaptif terpadu", "T5": "T5 Platform kota"}
LANES = [
    ("P", "Pengguna &\nmitra eksternal"),
    ("U", "Penyajian\n(layar &\naplikasi)"),
    ("S", "Pusat\n(server aplikasi)"),
    ("K", "Komunikasi &\nintegrasi"),
    ("L", "Lapangan\n(kabinet, edge,\nkamera)"),
]
LANE_IDX = {k: i for i, (k, _) in enumerate(LANES)}
LANE_FILL = ["#F7F7F7", "#FFFFFF", "#F2F6FA", "#FFFFFF", "#F7F7F7"]

# ------------------------------------------------------------------ data alur
# step: (id, lane, teks, tahap, komponen)  ; edge: (dari, ke, label)  ; sub = baris kedua dalam lane (opsional)
FLOWS = []

def flow(fid, judul, tujuan, steps, edges, catatan=""):
    FLOWS.append(dict(id=fid, judul=judul, tujuan=tujuan, steps=steps, edges=edges, catatan=catatan))

flow("F01", "Pemantauan status simpang secara langsung",
     "Operator ruang kendali melihat kondisi setiap simpang (mode kendali, lampu yang menyala, detektor, alarm) dengan jeda paling lama lima detik. Pada T1 lampu sungguhan digantikan simulator; mulai T2 data datang dari controller di kabinet.",
     [("a", "L", "Simulator SUMO berperan sebagai controller", "T1", "sim/, services/cai (adaptor TraCI)"),
      ("b", "L", "Controller melaporkan status lampu dan detektor tiap detik", "T2", "controller vendor/NTCIP"),
      ("c", "L", "Agen edge menerjemahkan protokol vendor, menyimpan data bila jaringan putus", "T2", "edge/ (edge-light)"),
      ("d", "K", "Jaringan Dishub (fiber/4G) lewat VPN, pesan MQTT", "T2", "infra/ (MQTT, WireGuard)"),
      ("e", "S", "Layanan status menerima dan menyimpan potret status", "T1", "apps/api, TimescaleDB"),
      ("f", "S", "Mesin aturan menandai anomali (offline, kedip, konflik, jam melenceng)", "T2", "services/health"),
      ("g", "U", "Peta simpang dan tampilan fase langsung di konsol", "T1", "apps/tmc-web (MapLibre)"),
      ("h", "P", "Operator memantau; pimpinan dan publik melihat ringkasan", "T2", "dashboard publik")],
     [("a", "e", "T1"), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", ""), ("e", "g", ""), ("f", "g", "alarm"), ("g", "h", "")])

flow("F02", "Perencanaan dan penetapan jadwal lampu",
     "Perencana menyusun jadwal lampu (fase, lama hijau, offset) berdasarkan data survei, memeriksanya dengan kalkulator dan validator, mengujinya di simulator, lalu mengirimkannya ke controller setelah disetujui pejabat yang berwenang.",
     [("a", "P", "Perencana memasukkan data survei, geometri, dan arus", "T1", "apps/tmc-web"),
      ("b", "S", "Kalkulator PKJI 2023: kapasitas, antrian, tundaan, kelas LOS", "T1", "services/kpi-pkji"),
      ("c", "U", "Editor jadwal (fase, hijau, offset); minimal delapan jadwal per simpang", "T1", "apps/tmc-web"),
      ("d", "S", "Validator keselamatan (kuning, merah semua, hijau minimum) dan konsistensi urutan fase", "T1", "services/kpi-pkji"),
      ("e", "S", "Uji di digital twin SUMO; laporan hasil (wajib sebelum penetapan mulai T3)", "T1", "sim/, services/twin"),
      ("f", "P", "Persetujuan Kepala Dinas; Dirjen/BPTJ bila simpang di jalan nasional", "T2", "alur persetujuan"),
      ("g", "S", "Transaksi unduh jadwal tervalidasi; versi dan jejak audit", "T2", "services/cai"),
      ("h", "L", "Controller menerima jadwal baru; jadwal lokal ikut diperbarui", "T2", "controller, edge/")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", ""), ("f", "g", ""), ("g", "h", "")])

flow("F03", "Kendali terpusat, mode manual petugas, dan cadangan saat putus",
     "Operator atau petugas Polri memilih program atau mode manual dari ruang kendali. Pusat mengirim perintah terbatas beserta detak jantung. Bila jaringan putus, controller kembali ke jadwal lokal dan semua kejadian tetap tercatat.",
     [("a", "P", "Operator atau petugas Polri memilih program, kedip, atau mode manual", "T2", "konsol operator"),
      ("b", "U", "Konsol kendali meminta konfirmasi dan alasan", "T2", "apps/tmc-web"),
      ("c", "S", "Layanan perintah memeriksa hak akses, mengirim perintah tipe C dan detak jantung", "T2", "services/cai"),
      ("d", "K", "SNMP/MQTT lewat VPN", "T2", "infra/"),
      ("e", "L", "Controller menjalankan program; edge meneruskan detak jantung", "T2", "controller, edge/"),
      ("f", "L", "Jaringan putus: controller kembali ke jadwal lokal; edge menyimpan catatan", "T2", "controller (backup timer), edge/"),
      ("g", "S", "Jejak audit perintah dan KPI transisi; alarm bila cadangan aktif", "T2", "audit log, services/health")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", "bila putus"), ("e", "g", ""), ("f", "g", "alarm")])

flow("F04", "Kesehatan perangkat, alarm, tiket kerja, dan pemeliharaan",
     "Kerusakan detektor, kamera, controller, atau jaringan terdeteksi otomatis, diprioritaskan, lalu menjadi tiket kerja untuk teknisi. Jadwal pemeliharaan berkala dan umur teknis aset dijaga sesuai PM 49/2014.",
     [("a", "L", "Alarm controller dan detektor; pintu kabinet; catu daya", "T2", "controller, edge/"),
      ("b", "S", "Watchdog harian dari catatan kejadian (detektor diam, max-out dini hari)", "T2", "services/atspm"),
      ("c", "S", "Mesin alarm: prioritas, eskalasi, notifikasi ke Polri bila APILL mati", "T2", "services/health"),
      ("d", "K", "Email/WhatsApp; API CRM kota", "T2", "infra/, integrasi CRM"),
      ("e", "S", "Tiket kerja otomatis dengan SLA dan pencatatan waktu perbaikan", "T2", "services/ticket"),
      ("f", "U", "Aplikasi ponsel teknisi: tiket, checklist, foto, bisa offline", "T2", "apps/tmc-web (PWA)"),
      ("g", "S", "Jadwal pemeliharaan enam bulanan, umur teknis lima tahun, penilaian aset", "T1", "apps/api (inventory)"),
      ("h", "P", "Kepala Dinas melihat KPI kesehatan perangkat dan biaya", "T2", "dashboard pimpinan")],
     [("a", "c", ""), ("b", "c", ""), ("c", "d", ""), ("c", "e", ""), ("e", "f", ""), ("f", "e", "selesai"), ("g", "e", "jatuh tempo"), ("e", "h", "KPI")])

flow("F05", "Pengukuran kinerja dan laporan wajib",
     "Catatan kejadian resolusi tinggi dari controller, edge, atau simulator diolah menjadi ukuran kinerja sinyal, KPI resmi (PKJI, LOS PM 96/2015), dan laporan yang wajib disampaikan ke Forum LLAJ, Dirjen/BPTJ, dan Gubernur.",
     [("a", "L", "Catatan kejadian 0,1 detik dari controller, edge, atau simulator", "T1", "controller/edge/sim"),
      ("b", "K", "Dikirim berkala dalam paket lewat MQTT", "T2", "infra/"),
      ("c", "S", "Ingest dan simpan: rinci 90 hari, ringkasan 15 menit selama 5 tahun", "T1", "services/atspm, TimescaleDB"),
      ("d", "S", "Mesin ATSPM: terminasi fase, split failure, arrivals on green, diagram koordinasi", "T1", "services/atspm"),
      ("e", "S", "KPI PKJI dan LOS PM 96; perbandingan sebelum-sesudah dan hidup-mati", "T1", "services/kpi-pkji"),
      ("f", "S", "Generator laporan: Forum LLAJ, Dirjen/BPTJ, Gubernur triwulanan", "T2", "services/reports"),
      ("g", "U", "Dashboard pimpinan dan engineer; dashboard publik dengan metode terbuka", "T2", "apps/tmc-web"),
      ("h", "P", "Pejabat, DPRD, Forum LLAJ, warga", "T2", "")],
     [("a", "b", ""), ("b", "c", ""), ("a", "c", "T1 langsung"), ("c", "d", ""), ("d", "e", ""), ("e", "f", ""), ("e", "g", ""), ("f", "h", ""), ("g", "h", "")])

flow("F06", "Deteksi berbasis kamera dan detektor virtual",
     "Kamera yang sudah ada diolah di kotak edge AI menjadi angka jumlah kendaraan, okupansi, dan panjang antrian, serta pembacaan pelat untuk bukti dan prioritas. Hanya angka ringkasan yang dikirim ke pusat; data pelat tunduk pada tata kelola perlindungan data pribadi.",
     [("a", "L", "Kamera CCTV (RTSP) atau kamera analitik vendor", "T2", "kamera eksisting"),
      ("b", "L", "Edge AI: hitung kendaraan, okupansi, antrian; baca pelat (disamarkan)", "T3", "edge/ (Jetson, YOLO, OCR)"),
      ("c", "L", "Pemeriksaan kualitas deteksi (malam, hujan); turun otomatis bila buruk", "T3", "edge/ health"),
      ("d", "K", "Kirim angka ringkasan lewat MQTT, tanpa video", "T3", "infra/"),
      ("e", "S", "Detektor virtual menjadi catatan kejadian dan masukan kendali", "T3", "services/cai, services/atspm"),
      ("f", "S", "Tata kelola PDP: dasar hukum, retensi pelat singkat, akses terbatas, DPIA", "T3", "keamanan & kepatuhan"),
      ("g", "U", "Tampilan kamera langsung (WebRTC) dengan lapisan hitungan", "T2", "apps/tmc-web, gerbang video"),
      ("h", "P", "Operator ruang kendali; pejabat perlindungan data", "T3", "")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", "pelat"), ("a", "g", "stream"), ("e", "g", "angka"), ("g", "h", ""), ("f", "h", "")])

flow("F07", "Kendali responsif dan adaptif",
     "Data detektor dipakai untuk memilih program dan menala offset secara otomatis (T3), lalu membagi ulang waktu hijau setiap siklus dan mengendalikan perimeter kawasan jenuh (T4). Mode bayangan dan ukuran kinerja independen memastikan setiap algoritma terbukti sebelum mengendalikan lampu.",
     [("a", "L", "Detektor (virtual, loop, radar) melaporkan okupansi dan antrian", "T3", "edge/, controller"),
      ("b", "S", "Gerbang kesehatan: adaptif hanya bila detektor sehat", "T3", "services/adaptive"),
      ("c", "S", "Pemilihan program otomatis dan penalaan offset koridor (Link Pivot, data GPS)", "T3", "services/adaptive (TRPS), services/atspm"),
      ("d", "S", "Cyclic max-pressure membagi hijau tiap siklus, perubahan maksimal lima detik", "T4", "services/adaptive"),
      ("e", "S", "Pengendalian perimeter kawasan pusat kota saat jenuh", "T4", "services/adaptive"),
      ("f", "S", "Mode bayangan dan ATSPM sebagai pengamat independen", "T3", "shadow harness, services/atspm"),
      ("g", "K", "Perintah split/program lewat antarmuka controller", "T3", "services/cai, MQTT"),
      ("h", "L", "Controller menjalankan; jadwal lokal tetap sebagai cadangan", "T3", "controller"),
      ("i", "U", "Konsol adaptif: parameter, keputusan, dan nilai antara yang bisa dijelaskan", "T4", "apps/tmc-web")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", "T4"), ("d", "e", ""), ("c", "g", ""), ("d", "g", ""), ("e", "g", ""), ("g", "h", ""), ("a", "f", ""), ("f", "i", ""), ("d", "i", "")])

flow("F08", "Prioritas bus dan kendaraan darurat",
     "Permintaan prioritas datang dari sistem pelacakan bus dan pusat komando pemadam atau ambulans. Layanan prioritas menilai kelayakan, menjaga batas keselamatan, lalu memberi hijau tambahan atau preemption melalui controller, dan mencatat dampaknya.",
     [("a", "P", "AVL/APC operator bus; CAD pemadam dan ambulans", "T3", "operator bus, 112/119"),
      ("b", "K", "API mitra sesuai dokumen antarmuka; MoU digital detik prioritas", "T3", "integrasi (ICD)"),
      ("c", "S", "Layanan permintaan prioritas: kelayakan (terlambat, muatan), antrian permintaan", "T3", "services/priority"),
      ("d", "S", "Prioritas bersyarat (OCC/Transit-MP) dan darurat bertingkat dengan penyelesaian konflik", "T4", "services/priority"),
      ("e", "S", "Batas: pejalan kaki tidak dipotong, satu aktivasi per siklus, jeda, pemulihan koordinasi", "T3", "services/priority"),
      ("f", "K", "Perintah tahan, perpanjang, atau preempt ke controller", "T3", "services/cai"),
      ("g", "L", "Controller memberi hijau tambahan atau preempt; check-out geofence mengakhiri", "T3", "controller, edge/"),
      ("h", "U", "Konsol prioritas: permintaan, dilayani/ditolak, dampak jalan samping", "T3", "apps/tmc-web"),
      ("i", "S", "Log dan KPI: waktu tempuh bus, waktu tanggap darurat", "T3", "services/atspm")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", "T4"), ("c", "e", ""), ("d", "e", ""), ("e", "f", ""), ("f", "g", ""), ("g", "i", ""), ("c", "h", ""), ("i", "h", "")])

flow("F09", "Bukti pelanggaran untuk ETLE Polri",
     "Sistem hanya menyediakan bukti. Edge AI mendeteksi pelanggaran seperti menerobos merah, pusat menyusun paket bukti dengan kontrol perlindungan data, lalu mengirimkannya ke Back Office ETLE Polri untuk diverifikasi dan ditindak oleh petugas.",
     [("a", "L", "Edge AI mendeteksi terobos merah (aktuasi saat kuning/merah) dan pelat", "T3", "edge/, services/atspm (YRA)"),
      ("b", "S", "Paket bukti: foto/klip 30 detik, pelat terenkripsi, waktu, lokasi", "T3", "services/evidence, object store"),
      ("c", "S", "Kontrol PDP dan DPIA; retensi bukti sesuai alur Perpol 2/2025", "T3", "keamanan & kepatuhan"),
      ("d", "K", "API ke Back Office ETLE Polda sesuai Perpol 8/2023", "T4", "integrasi (ICD Polri)"),
      ("e", "P", "Petugas Polri memverifikasi dan menindak; aplikasi tidak menerbitkan tilang", "T4", "Polri"),
      ("f", "S", "Status tindak lanjut hanya-baca; laporan integrasi tahunan", "T4", "services/evidence"),
      ("g", "U", "Dashboard keselamatan: pelanggaran per simpang, tren", "T3", "apps/tmc-web")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", "status"), ("b", "g", ""), ("f", "g", "")])

flow("F10", "Keluhan publik dan jaminan layanan",
     "Laporan warga masuk lewat aplikasi kota atau CRM, menjadi tiket dengan target waktu penyelesaian, dan didiagnosis dengan data kinerja sinyal termasuk pemutaran ulang kejadian. Jawaban dan status dikembalikan ke pelapor.",
     [("a", "P", "Warga melapor lewat aplikasi kota, CRM, atau telepon", "T2", "CRM kota"),
      ("b", "K", "API CRM dua arah", "T2", "integrasi CRM"),
      ("c", "S", "Tiket tujuh langkah, klasifikasi, target penyelesaian tiga jam", "T2", "services/ticket"),
      ("d", "S", "Matriks diagnosis: jenis keluhan dipetakan ke data ATSPM terkait", "T2", "services/atspm"),
      ("e", "S", "Pemutaran ulang kejadian historis (status lampu dan detektor saat keluhan)", "T3", "services/atspm, TimescaleDB"),
      ("f", "U", "Operator menindaklanjuti; tiket kerja ke teknisi bila perlu", "T2", "apps/tmc-web"),
      ("g", "P", "Jawaban ke pelapor; status dapat dilihat publik", "T2", "CRM kota, dashboard publik")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("d", "f", ""), ("e", "f", ""), ("f", "g", "")])

flow("F11", "Digital twin, mode bayangan, dan marketplace algoritma",
     "Setiap jadwal atau algoritma baru diuji dulu di simulator yang dikalibrasi dengan data kota, lalu dijalankan dalam mode bayangan dengan data hidup tanpa mengendalikan lampu, dan baru dipromosikan bertahap ke jam sepi dan jam sibuk. Pada T5 pihak ketiga dapat mengajukan algoritma lewat jalur yang sama.",
     [("a", "S", "Generator jaringan simulasi dari registri simpang dan peta OSM", "T1", "sim/"),
      ("b", "S", "Kalibrasi twin per koridor dengan data hitungan dan GPS", "T3", "sim/, services/twin"),
      ("c", "S", "Skenario: jadwal baru, insiden, acara; kebijakan TDM skala kota (T5)", "T3", "services/twin"),
      ("d", "S", "Pekerja simulasi menjalankan; hasil MoE dan catatan kejadian", "T3", "sim/ worker"),
      ("e", "S", "Mode bayangan: algoritma menerima data hidup, keputusan dicatat, tidak dikirim", "T3", "shadow harness"),
      ("f", "S", "Veto statistik dan uji konflik prioritas", "T4", "services/adaptive"),
      ("g", "P", "Universitas atau vendor mengajukan algoritma (marketplace)", "T5", "portal mitra"),
      ("h", "S", "Promosi bertahap: jam sepi, jam sibuk, perbandingan hidup-mati", "T3", "services/adaptive"),
      ("i", "U", "Laporan divergensi dan keputusan lanjut atau berhenti", "T3", "apps/tmc-web")],
     [("a", "b", ""), ("b", "c", ""), ("c", "d", ""), ("d", "e", ""), ("e", "f", ""), ("f", "h", ""), ("g", "d", "T5"), ("e", "i", ""), ("h", "i", "")])

flow("F12", "Platform banyak kota, data terbuka, dan pengelolaan permintaan perjalanan",
     "Satu platform melayani banyak kota dengan data terpisah per yurisdiksi, membandingkan kinerja antar kota, menghitung ambang legal kebijakan pembatasan kendaraan, dan membuka data lewat API publik untuk aplikasi navigasi, peneliti, dan warga.",
     [("a", "P", "Kota A, Kota B, dan seterusnya sebagai tenant; Kemenhub/BPTJ; provinsi", "T5", "tenant"),
      ("b", "S", "Isolasi data per tenant dan yurisdiksi; peran akses", "T4", "apps/api (multi-tenant)"),
      ("c", "S", "Benchmark antar kota: arrivals on green, LOS, ketersediaan perangkat", "T5", "services/kpi-pkji"),
      ("d", "S", "Kalkulator ambang kebijakan pembatasan (V/C dan kecepatan) dan evaluasi tahunan", "T5", "services/tdm"),
      ("e", "S", "Penasihat pembelajaran mesin yang hanya mengusulkan parameter", "T5", "services/advisor"),
      ("f", "K", "API publik dan data terbuka; integrasi ERP dan ganjil-genap pemprov", "T5", "API gateway"),
      ("g", "U", "Portal data terbuka; dashboard benchmark", "T5", "apps/tmc-web"),
      ("h", "P", "Aplikasi navigasi (GLOSA/SPaT), peneliti, warga", "T5", "")],
     [("a", "b", ""), ("b", "c", ""), ("b", "d", ""), ("b", "e", ""), ("c", "f", ""), ("d", "f", ""), ("c", "g", ""), ("f", "h", ""), ("g", "h", "")])

# Gambaran keseluruhan (komponen per lapisan, tanpa panah)
OVERVIEW = dict(id="F00", judul="Gambaran keseluruhan komponen IRAMA per lapisan dan tahap",
    lanes={
        "P": [("Operator ruang kendali", "T2"), ("Teknisi lapangan", "T2"), ("Pimpinan & publik", "T2"), ("Operator bus, 112/119", "T3"), ("Polri & Back Office ETLE", "T4"), ("Bapenda, DLH, tol, cuaca", "T4"), ("Kota lain, BPTJ, navigasi", "T5")],
        "U": [("Web perencana", "T1"), ("Konsol operator", "T2"), ("Aplikasi teknisi", "T2"), ("Dashboard publik", "T2"), ("Konsol prioritas & koridor", "T3"), ("Video wall TMC kota", "T4"), ("Portal data & benchmark", "T5")],
        "S": [("Registri simpang & aset", "T1"), ("Kalkulator PKJI & editor jadwal", "T1"), ("Antarmuka controller (CAI)", "T1"), ("ATSPM & KPI", "T1"), ("Kesehatan, alarm, tiket", "T2"), ("Laporan wajib", "T2"), ("Responsif: program & offset", "T3"), ("Prioritas bus & darurat", "T3"), ("Twin & mode bayangan", "T3"), ("Bukti ETLE", "T3"), ("Adaptif MP & perimeter", "T4"), ("Multi-tenant, TDM, penasihat", "T5")],
        "K": [("MQTT + VPN", "T2"), ("Alarm email/WA, CRM", "T2"), ("NATS antar layanan", "T3"), ("API mitra (ICD)", "T3"), ("mTLS & segmentasi", "T4"), ("API publik", "T5")],
        "L": [("Simulator SUMO", "T1"), ("Controller & jadwal lokal", "T2"), ("Edge ringan di kabinet", "T2"), ("Kamera CCTV", "T2"), ("Edge AI & detektor virtual", "T3"), ("Fusi radar & GLOSA", "T5")],
    })

# ------------------------------------------------------------------ render
def wrap(t, w=22):
    return "\n".join(textwrap.wrap(t, w))

def draw_flow(f, out_png):
    steps = f["steps"]; edges = f["edges"]
    n = len(steps)
    col = {s[0]: i for i, s in enumerate(steps)}
    fig_w = 2.25 + 1.68 * n; fig_h = 6.8
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=200)
    ax.set_xlim(0, fig_w); ax.set_ylim(0, fig_h); ax.axis("off")
    lane_h = (fig_h - 0.9) / len(LANES); top = fig_h - 0.75
    # lanes
    for i, (k, name) in enumerate(LANES):
        y0 = top - (i + 1) * lane_h
        ax.add_patch(Rectangle((0, y0), fig_w, lane_h, facecolor=LANE_FILL[i], edgecolor="#BDBDBD", lw=0.6))
        ax.text(0.12, y0 + lane_h / 2, name, va="center", ha="left", fontsize=7.2, color="#37474F", fontweight="bold")
    # judul & legenda
    ax.text(0.12, fig_h - 0.28, "%s  %s" % (f["id"], f["judul"]), fontsize=9.5, fontweight="bold", va="center")
    lx = fig_w - 0.15
    for st in reversed(list(STAGE_COLOR)):
        ax.text(lx, fig_h - 0.62, STAGE_NAME[st], fontsize=5.8, ha="right", va="center",
                bbox=dict(boxstyle="round,pad=0.25", fc=STAGE_COLOR[st], ec="none"), color="white")
        lx -= 1.25
    # boxes
    bw, bh = 1.46, 0.92
    pos = {}
    for sid, lane, text, st, comp in steps:
        cx = 2.15 + col[sid] * 1.68 + bw / 2
        li = LANE_IDX[lane]
        cy = top - li * lane_h - lane_h / 2
        pos[sid] = (cx, cy)
        ax.add_patch(FancyBboxPatch((cx - bw / 2, cy - bh / 2), bw, bh, boxstyle="round,pad=0.02,rounding_size=0.06",
                                    fc="white", ec=STAGE_COLOR[st], lw=1.2))
        ax.text(cx - bw / 2 + 0.06, cy - 0.04, wrap(text, 24), fontsize=5.3, va="center", ha="left", color="#212121", linespacing=1.15)
        ax.text(cx + bw / 2 - 0.02, cy + bh / 2 - 0.02, st, fontsize=5.6, ha="right", va="top", color="white", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.15", fc=STAGE_COLOR[st], ec="none"))
        ax.text(cx - bw / 2 + 0.03, cy + bh / 2 - 0.03, sid, fontsize=5.2, ha="left", va="top", color="#616161")
    # arrows
    for a, b, lab in edges:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        dx = x2 - x1; dy = y2 - y1
        if abs(dx) < 0.01:
            s_pt = (x1, y1 - bh / 2 if dy < 0 else y1 + bh / 2); e_pt = (x2, y2 + bh / 2 if dy < 0 else y2 - bh / 2); cs = "arc3,rad=0"
        elif dx > 0:
            s_pt = (x1 + bw / 2, y1); e_pt = (x2 - bw / 2, y2)
            cs = "arc3,rad=%.2f" % (0.0 if abs(dy) < 0.01 and col[b] - col[a] == 1 else (-0.25 if col[b] - col[a] > 1 and abs(dy) < 0.01 else 0.15))
        else:
            s_pt = (x1 - bw / 2, y1); e_pt = (x2 + bw / 2, y2); cs = "arc3,rad=0.35"
        arr = FancyArrowPatch(s_pt, e_pt, connectionstyle=cs, arrowstyle="-|>", mutation_scale=8, lw=0.9, color="#455A64", shrinkA=1, shrinkB=1)
        ax.add_patch(arr)
        if lab:
            mx, my = (s_pt[0] + e_pt[0]) / 2, (s_pt[1] + e_pt[1]) / 2 + (bh / 2 + 0.07 if abs(dy) < 0.01 else 0.12)
            ax.text(mx, my, lab, fontsize=5.2, ha="center", va="center", color="#455A64",
                    bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.85))
    fig.savefig(out_png, bbox_inches="tight", pad_inches=0.05); plt.close(fig)

def draw_overview(o, out_png):
    ncol = max(len(v) for v in o["lanes"].values())
    fig_w = 2.25 + 1.5 * ncol; fig_h = 6.2
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=200)
    ax.set_xlim(0, fig_w); ax.set_ylim(0, fig_h); ax.axis("off")
    lane_h = (fig_h - 0.9) / len(LANES); top = fig_h - 0.75
    for i, (k, name) in enumerate(LANES):
        y0 = top - (i + 1) * lane_h
        ax.add_patch(Rectangle((0, y0), fig_w, lane_h, facecolor=LANE_FILL[i], edgecolor="#BDBDBD", lw=0.6))
        ax.text(0.12, y0 + lane_h / 2, name, va="center", ha="left", fontsize=7.2, color="#37474F", fontweight="bold")
        items = o["lanes"][k]
        bw, bh = 1.36, 0.66
        for j, (text, st) in enumerate(items):
            cx = 2.15 + j * 1.5 + bw / 2; cy = y0 + lane_h / 2
            ax.add_patch(FancyBboxPatch((cx - bw / 2, cy - bh / 2), bw, bh, boxstyle="round,pad=0.02,rounding_size=0.06", fc="white", ec=STAGE_COLOR[st], lw=1.2))
            ax.text(cx - bw / 2 + 0.06, cy - 0.05, wrap(text, 23), fontsize=5.5, va="center", ha="left", color="#212121")
            ax.text(cx + bw / 2 - 0.02, cy + bh / 2 - 0.02, st, fontsize=5.6, ha="right", va="top", color="white", fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.15", fc=STAGE_COLOR[st], ec="none"))
    ax.text(0.12, fig_h - 0.28, "%s  %s" % (o["id"], o["judul"]), fontsize=9.5, fontweight="bold", va="center")
    lx = fig_w - 0.15
    for st in reversed(list(STAGE_COLOR)):
        ax.text(lx, fig_h - 0.62, STAGE_NAME[st], fontsize=5.8, ha="right", va="center", bbox=dict(boxstyle="round,pad=0.25", fc=STAGE_COLOR[st], ec="none"), color="white")
        lx -= 1.25
    fig.savefig(out_png, bbox_inches="tight", pad_inches=0.05); plt.close(fig)

# ------------------------------------------------------------------ mermaid & markdown
def mermaid(f):
    lines = ["flowchart LR"]
    lane_names = dict(LANES)
    for k, name in LANES:
        ss = [s for s in f["steps"] if s[1] == k]
        if not ss: continue
        lines.append('  subgraph %s["%s"]' % (k, name.replace("\n", " ")))
        for sid, lane, text, st, comp in ss:
            lines.append('    %s%s["%s. %s (%s)"]' % (f["id"], sid, sid, text.replace('"', "'"), st))
        lines.append("  end")
    for a, b, lab in f["edges"]:
        lines.append("  %s%s -->%s %s%s" % (f["id"], a, ("|%s|" % lab) if lab else "", f["id"], b))
    for st, c in STAGE_COLOR.items():
        ids = ",".join("%s%s" % (f["id"], s[0]) for s in f["steps"] if s[3] == st)
        if ids: lines.append("  style %s stroke:%s,stroke-width:2px" % (ids.split(",")[0], c))
    return "\n".join(lines)

def md_section(sederhana):
    out = []
    out.append("## %s Diagram alur fitur utama dan pemetaannya ke arsitektur dan tahap\n" % ("" if sederhana else "8."))
    out.append("Diagram berikut menggambarkan cara IRAMA bekerja pada kondisi end-state, satu diagram per fitur utama. Cara membacanya sama untuk semua diagram.\n")
    out.append("- Baris (lajur mendatar) adalah lapisan arsitektur: pengguna dan mitra eksternal, penyajian, pusat, komunikasi dan integrasi, lapangan. Posisi kotak menunjukkan komponen mana yang menjalankan langkah itu.")
    out.append("- Kotak adalah langkah, diberi huruf urut dan warna bingkai. Label kecil di pojok kanan atas (T1 sampai T5) menandai tahap saat langkah itu pertama tersedia. Warna: T1 hijau, T2 biru, T3 jingga, T4 ungu, T5 merah.")
    out.append("- Panah adalah aliran data atau perintah. Label pada panah menjelaskan kondisi, misalnya \"bila putus\".")
    out.append("- Untuk membaca diagram pada tahap tertentu, abaikan kotak yang labelnya lebih tinggi dari tahap itu. Contoh: pada T2, kotak berlabel T3 sampai T5 belum ada, dan alur berhenti pada kotak terakhir yang tersedia.\n")
    out.append("Tabel di bawah tiap diagram memetakan langkah ke komponen dalam struktur repositori (apps, services, edge, sim, infra) dan tahapnya.\n")
    # overview
    out.append("### F00 Gambaran keseluruhan komponen per lapisan dan tahap\n")
    out.append("![F00](%s)\n" % rel_png("F00"))
    out.append("Diagram ini memperlihatkan semua komponen yang ada pada end-state, dikelompokkan per lapisan, dengan label tahap pemunculannya. Diagram F01 sampai F12 memperlihatkan bagaimana komponen tersebut bekerja sama untuk tiap fitur.\n")
    for f in FLOWS:
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

def rel_png(fid):
    name = [x for x in os.listdir(HERE) if x.startswith(fid) and x.endswith(".png")]
    return "diagram/" + (name[0] if name else fid + ".png")

def main():
    draw_overview(OVERVIEW, os.path.join(HERE, "F00_Gambaran_Keseluruhan.png"))
    for f in FLOWS:
        slug = f["judul"].split(",")[0].replace(" ", "_")[:40]
        png = os.path.join(HERE, "%s_%s.png" % (f["id"], slug))
        draw_flow(f, png)
        io.open(os.path.join(HERE, "%s.mmd" % f["id"]), "w", encoding="utf-8").write(mermaid(f))
        print("ok", os.path.basename(png))
    io.open(os.path.join(HERE, "_bagian_diagram.md"), "w", encoding="utf-8", newline="\n").write(md_section(False))
    io.open(os.path.join(HERE, "_bagian_diagram_sederhana.md"), "w", encoding="utf-8", newline="\n").write(md_section(True))
    print("markdown ok")

if __name__ == "__main__":
    main()
