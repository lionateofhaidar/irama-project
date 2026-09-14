# 07 — Persona dan Stakeholder

Status: draf pra-perencanaan (2026-09-12), kolom tahap direvisi 2026-09-14. Bukti dirujuk ke Bahan Acuan (R00–R06) dan majalah RPP DKI. Tahap: T1 Purwarupa Hitung dan Rekomendasi, T2 Vision Tracker dan Optimasi Simpang, T3 Deteksi Kejadian dan Pemantauan Operasional, T4 Kendali Adaptif Terpadu, T5 Platform Mobilitas Kota. Pengguna pertama adalah engineer lalu lintas (P2); operator ruang kendali dilayani mulai T3.

## 1. Persona utama

| # | Persona | Tujuan | Pain point nyata (bukti) | Kebutuhan informasi | Perangkat | Ukuran sukses | Dilayani sejak |
|---|---|---|---|---|---|---|---|
| P1 | **Operator TMC/CC-Room (shift)** — DKI ±25 orang/shift, call center terhubung CRM, SLA keluhan 3 jam [R06 D] | Menjaga semua simpang "hijau" (online, tidak flashing), menangani keluhan & kejadian cepat | Terlalu banyak layar CCTV tanpa prioritas; tidak tahu simpang mana yang bermasalah sampai ada keluhan (TSPH: komplain jadi ukuran kinerja) [R02]; perubahan plan manual & tidak terdokumentasi (NCDOT field diary) [R01]; transisi plan menimbulkan antrean [R01 C.6] | Peta status real-time, alarm perangkat, status koordinasi/plan aktif, tiket keluhan, SOP kejadian | Video wall, 2–3 monitor, radio/telepon, aplikasi CRM | Waktu deteksi gangguan < 5 menit [A]; SLA keluhan terpenuhi; jumlah intervensi manual tercatat | **T3** (pemantauan kejadian, CCTV live view, tiket) → T4 (kendali) |
| P2 | **Engineer lalu lintas Dishub (Kasie/analis)** | Menyusun & memperbarui plan (TOD/koordinasi), evaluasi kinerja, laporan MRLL | Retiming jarang (>3 tahun; NTOC) [R01]; hitung PKJI manual di spreadsheet; tidak ada data before–after; kesulitan menjelaskan ke pimpinan/DPRD [R02 Req 6.0-11] | Volume/antrian per pendekat, DJ/tundaan/LOS, PCD/AoG, split failure, laporan before–after | PC kantor, Excel, Synchro/Vissim (kadang) | Waktu menyusun plan turun; LOS koridor membaik; laporan Forum LLAJ/Dirjen tepat waktu | **T1** (Vision Tracker, kalkulator PKJI, rekomendasi) → T2 (wizard, dashboard tiga halaman, laporan, SUMO) → T3 (ATSPM, uji lapangan) |
| P3 | **Teknisi lapangan APILL** | Perangkat berfungsi; perbaikan cepat | Detektor/kamera rusak tak terdeteksi (penyebab #1 decommissioning ASCT) [R02 F.5; R06 E.4]; tidak ada work order terstruktur; upload timing di luar jam kerja dilarang (NCDOT) [R01] | Alarm per perangkat, riwayat kegagalan, jadwal PM 6 bulan (PM 49 Ps.41), spare part, lokasi kabinet | HP/tablet, laptop servis, kunci kabinet | MTTR; % detektor berfungsi; PM tepat waktu | T3 (kesehatan kamera, tiket kerja, pemeliharaan berkala) → T4 (alarm controller, aplikasi ponsel) |
| P4 | **Kadishub / Kabid Lalin** | Kinerja terlihat (ranking, keluhan turun), realisasi anggaran, inovasi (PKN/proyek perubahan) [majalah] | Klaim manfaat tanpa MOE [R06 D]; anggaran besar disorot DPRD [R06 D]; ketergantungan vendor/black-box [R02] | Dashboard eksekutif: KPI kota (kecepatan rata-rata vs 35 km/jam Perda), LOS, jumlah simpang aktif, tren bulanan, before–after | HP, laporan PDF, rapat | Bukti dampak yang dapat dipublikasikan; audit bersih | T2 (dashboard, laporan kajian, manfaat rupiah) → T3 (laporan wajib, dashboard publik) |
| P5 | **Petugas Polantas / TMC Polda** | Pengaturan situasional, penegakan hukum, pusat kendali SIK LLAJ (UU Ps.247) [R05] | Tidak punya akses ke status APILL Dishub; harus datang ke lapangan untuk override; ETLE butuh bukti valid | Status simpang, tombol override/plan darurat, log kejadian, ekspor bukti | Ruang TMC Polda, HT, aplikasi ETLE | Waktu respons kejadian; koordinasi tercatat | T3 (akses baca, bukti pelanggaran tanpa pelat) → T4 (mode manual dari konsol, integrasi ETLE) |
| P6 | **Planner Bappeda / Smart City / Diskominfo** | Indikator RPJMD, integrasi data, SPBE, hosting | Data transportasi tercerai (kritik MTI "single data") [R06 D]; sistem vendor tidak punya API; hosting & keamanan tidak jelas | API terbuka, dataset agregat, dashboard publik, dokumen keamanan | Portal data, server pemda/cloud | Integrasi ke portal smart city; SPBE terpenuhi | T3 (API dan dashboard publik) → T5 (data terbuka) |
| P7 | **Pengemudi bus/BRT & operator (TransJakarta, Trans Semanggi, Trans Metro Bandung)** | Headway teratur, waktu tempuh stabil | Tundaan di simpang; prioritas "menghilang" seiring waktu tanpa MoU [R06 A.4] | Konfirmasi prioritas diberikan; laporan headway per koridor | AVL/APC bus, aplikasi operator | Travel time −10–25%, variabilitas −19–50% (benchmark handbook) [R06 A.8] | T4 (TSP) |
| P8 | **Petugas Damkar / AGD 119 / dispatcher** | Sampai lokasi cepat & aman | Terjebak antrean di simpang; preemption tidak ada/tidak konsisten | Rute & preempt otomatis via CAD/AVL (system-based EVP) [R06 B] | CAD, GPS unit | Response time −14–23% (benchmark) [R06 B.3] | T3 (deteksi kendaraan prioritas) → T4 (preemption) |
| P9 | **Warga / pengguna jalan** | Perjalanan lancar & dapat diprediksi; tahu kondisi | Berhenti berulang; tidak tahu alasan lampu; keluhan tak berbalas | Info kondisi & rencana (portal, medsos), kanal keluhan dengan tindak lanjut (UU Ps.250 data pusat kendali dapat diakses) [R05] | HP | Stops/mile & keluhan turun; kepuasan | T3 (dashboard publik, aduan) → T5 (data terbuka, GLOSA) |
| P10 | **DPRD / Inspektorat / BPK** | Akuntabilitas & dampak belanja [R06 D] | Realisasi tinggi tanpa bukti dampak | Laporan before–after, biaya per simpang, uptime | Laporan | Temuan nihil; bukti dampak | T2 (laporan kajian dan manfaat rupiah) |
| P11 | **Vendor controller/detektor** | Interoperabilitas tanpa membuka proprietary | Tidak ada spesifikasi antarmuka standar; takut lock-in terbalik | ICD (NTCIP/RS-232), sertifikasi, uji integrasi | Lab/bench | Integrasi lulus uji conformance | T3 (baca-saja) → T4 (adaptor kendali) |
| P12 | **Admin sistem/IT Dishub** | Sistem aman & tersedia | Kabinet IP = pintu ke jaringan (NEMA TS 8) [R02 G.7]; tidak ada RBAC per yurisdiksi | Manajemen pengguna, audit log, backup | Server | Uptime; audit log lengkap | T2 (akun dan peran dasar) → T3 (IdP) → T4 (mTLS, segmentasi) |

## 2. Peta stakeholder (kota target generik)

```
                       KEPENTINGAN RENDAH            KEPENTINGAN TINGGI
PENGARUH TINGGI  | LATENT: Walikota/Bupati,      | PROMOTOR: Kadishub, Kabid Lalin,
                 | Sekda, DPRD Komisi, Bappeda,  | Kepala UP/UPTD Lalin, Kapolres/
                 | Ditjen Hubdat/BPTJ (jalan     | Kasatlantas (mitra wajib),
                 | nasional), Diskominfo         | Kepala Smart City (bila ada)
PENGARUH RENDAH  | APATHETIC: media, akademisi,  | DEFENDER: operator TMC, teknisi,
                 | YLKI/MTI lokal, warga umum    | engineer lalin, operator BRT,
                 |                               | Damkar/AGD, ULP/UKPBJ, Inspektorat
```
Strategi: promotor → co-design & pilot; latent → briefing indikator (kecepatan, LOS, TomTom) dan kepatuhan anggaran; defender → pelatihan bertingkat (matriks Mampu/Mau: mampu&mau = delegasi; tidak mampu&mau = bimtek; mampu&tidak mau = coaching; tidak mampu&tidak mau = sosialisasi) [majalah h.19–20]; apathetic → publikasi hasil.

**Catatan khusus DKI (dari majalah RPP h.13):** Promotors = Gubernur & Wagub; Latent = Dirjen Hubdat, Dirlantas PMJ, DTKJ, Dirut Jasa Marga & Hutama Karya; Defenders = Sekda, Inspektur, Bapenda, DLH, BPSDM, Bina Marga, Biro KSD, Kabid P&O LLAJ, Kabid Lalin Jalan, UP PKB, **UP SPLL**, Pusdatin Hub, Kasudinhub 5 wilayah; Apathetics = MTI, YLKI, ITDP, media, masyarakat. Untuk kota lain, DTKJ tidak ada; peran Bapenda/DLH hanya muncul bila integrasi pajak/emisi dijadwalkan (T4–T5).

## 3. "A day in the life" — Operator & engineer TMC (sintesis NCHRP 812 §8, TSPH, UP SPLL DKI)

| Waktu | Aktivitas | Dukungan aplikasi (tahap) |
|---|---|---|
| 05:30 | Serah terima shift; cek ringkasan malam: alarm perangkat, simpang flashing, komunikasi putus, transisi plan berlebih (Exhibit 8-16) | Ringkasan shift otomatis; watchdog (no data / max-out malam / stuck ped) (T3; watchdog controller T4) |
| 06:00 | Plan puncak pagi aktif lebih awal agar transisi selesai sebelum puncak (STM2 7-33) | Jadwal hasil rekomendasi (T2); log transisi dari controller (T4) |
| 06:30–09:30 | Pantau koridor prioritas; intervensi manual bila antrean meluber (spillback); koordinasi Polantas di simpang kritis | Peta status + antrian/okupansi; tombol plan darurat/flush; catatan siapa-kapan-mengapa (T3 pemantauan dan catatan manual → T4 kendali dengan jejak audit otomatis) |
| 09:30 | Tangani keluhan (CRM; SLA 3 jam): identitas, lokasi, waktu, berulang?, diagnosis lewat data sebelum kirim teknisi (Exhibit 8-17) | Pemutaran ulang kondisi dari data Vision Tracker (T3); formulir diagnosis (T3) |
| 11:00 | Teknisi: work order detektor rusak (max-out terus-menerus); PM 6 bulanan | Work order & riwayat aset (T3) |
| 13:00 | Engineer: tinjau split failure/PCD koridor; usulkan perubahan split/offset; simulasi sebelum diterapkan (PM 96 wajib simulasi) | Kalkulator PKJI dan rekomendasi (T1–T2); validasi SUMO (T2); ATSPM (T3); mode bayangan (T4) |
| 15:30 | Siapkan plan puncak sore; cek event (unjuk rasa, kunjungan VVIP, banjir) | Deteksi kejadian (T3); plan alternatif dan green wave VIP (T4) |
| 17:00–20:00 | Puncak sore; prioritas bus koridor BRT; preempt Damkar bila ada | TSP/EVP (T4) |
| 21:00 | Laporan harian ke Kabid; unggah perubahan timing hanya saat teknisi tersedia (NCDOT) | Laporan otomatis (T2–T3); kunci jadwal upload (T4) |
| Mingguan/bulanan | Laporan kinerja koridor (AoG, LOS, kecepatan), before–after, Forum LLAJ, triwulan ke Gubernur (Pergub 68) | Laporan kajian (T2); laporan wajib (T3) |
