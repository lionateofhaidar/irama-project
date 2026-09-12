# 13 — Kebutuhan Data yang Harus Disediakan per Tahap

Status: 2026-09-13, menjawab permintaan user (Q-06). T1 dirinci **presisi** (apa, format, cara mendapatkan, berapa banyak, untuk fitur apa); T2–T5 berupa **estimasi** yang akan dipertajam saat planning tiap tahap. Koridor pilot: Bandung (3–5 simpang berjarak ≤1 km, syarat ATCS PM 96/2015). Semua data lapangan dikumpulkan dengan izin; rekaman CCTV/pelat tunduk UU PDP (simpan di media terenkripsi, jangan dibagikan ke luar tim).

## T1 — MVP "Lihat & Kelola" (data presisi; semua bisa disediakan tanpa akses sistem Dishub)

| # | Data | Isi & format | Cara mendapatkan | Jumlah | Dipakai untuk (fitur) |
|---|---|---|---|---|---|
| D1.1 | **Daftar simpang koridor pilot** | CSV `simpang.csv`: id, nama simpang, lat, lon, nama jalan tiap kaki (U/T/S/B), status jalan (nasional/provinsi/kota — cek peta jalan nasional), jumlah kaki, ada APILL (ya/tidak), terhubung ATCS (ya/tidak/tidak tahu), catatan | pilih 1 koridor 3–5 simpang (kandidat dari `R07`/`docs/sources/08`); koordinat dari Google Maps/OSM; status jalan dari SK jalan nasional/provinsi | 3–5 simpang | registri simpang F-T1-01, peta F-T1-09, generator SUMO F-T1-106 |
| D1.2 | **Geometri tiap pendekat** | CSV `pendekat.csv`: id simpang, kaki, lebar pendekat L (m), lebar masuk LM (m), lebar keluar LK (m), lebar lajur belok kiri jalan terus LBKiJT (m), jumlah lajur, ada median (ya/tidak), kelandaian (%), tipe lingkungan (komersial/permukiman/akses terbatas), hambatan samping (tinggi/sedang/rendah), jarak parkir terdekat dari garis henti (m) | ukur dari citra satelit (skala Google Earth ±0,5 m) + verifikasi 1 kunjungan dengan meteran roda/aplikasi ukur; foto tiap kaki | 12–20 pendekat | kalkulator PKJI F-T1-16 (lebar efektif A4), validator |
| D1.3 | **Fase & waktu sinyal eksisting** | CSV `plan_eksisting.csv`: id simpang, periode (pagi/siang/sore/malam), nomor fase, gerakan yang dilayani, hijau (s), kuning (s), merah semua (s), urutan; siklus total | cara termudah: rekam video display/lampu 3 siklus per periode dan hitung dengan stopwatch, atau tanya petugas ATCS (bila sudah ada kontak) | 3–5 simpang × 3–4 periode | editor plan F-T1-18, validator F-T1-19/20, jadwal F-T1-21, baseline simulasi |
| D1.4 | **Arus lalu lintas per gerakan** | CSV `arus.csv`: id simpang, kaki, gerakan (lurus/belok kanan/belok kiri/kiri jalan terus), interval 15 menit (waktu mulai), jumlah mobil penumpang (MP), kendaraan sedang/berat (KS), sepeda motor (SM), kendaraan tak bermotor (KTB) | hitung manual dari rekaman video (D1.5) atau dari lapangan; minimal jam puncak pagi (06.30–08.30) & sore (16.00–18.00) + 1 jam sepi; hari kerja Selasa–Kamis | 3–5 simpang × 3 periode × semua gerakan | kalkulator PKJI (q, DJ, tundaan, LOS F-T1-63), demand SUMO, before–after F-T1-64 |
| D1.5 | **Rekaman CCTV/video simpang** (sudah disepakati) | 3–5 klip ±30 menit, MP4/MKV resolusi asli, sudut tetap; sertakan `video_meta.csv`: file, simpang, kaki yang terlihat, tanggal, jam mulai, cuaca, siang/malam, sumber (CCTV Dishub/rekaman sendiri dari tripod/jembatan penyeberangan) | dari Dishub (izin) atau rekam sendiri dari titik tinggi yang aman; variasi: sibuk/sepi, siang/malam, hujan bila ada | 3–5 klip (idealnya 2 simpang × sibuk/sepi + 1 malam + 1 hujan) | hitung kendaraan dasar (uji awal F-T3-123 di laptop), validasi D1.4, demo live view |
| D1.6 | **Floating car (waktu tempuh koridor)** | CSV/GPX dari aplikasi GPS logger (interval 1 s): waktu, lat, lon, kecepatan; `run_meta.csv`: run id, arah, tanggal, jam, periode, cuaca | menyusuri koridor dengan mobil/motor mengikuti arus (bukan mendahului), ≥6 run per arah per periode, hindari Senin/Jumat/hujan | ≥6 run/arah × 2 periode (pagi, sore) = ≥24 run | waktu tempuh & kecepatan koridor (KPI), cyclic TSD (F-T3-76 nanti), bukti before–after |
| D1.7 | **Peta jaringan jalan** | OSM extract area koridor (`.osm`), dikonversi netconvert | saya unduh dari OSM (gratis) | 1 area | generator SUMO F-T1-106 |
| D1.8 | **Foto & sketsa simpang** | foto tiap kaki (arah pandang ke simpang), foto kabinet/tiang (label perangkat bila terlihat), sketsa tata letak lampu & detektor | kunjungan 1 hari | 3–5 simpang | master graphics F-T2-07, inventaris aset F-T1-02 |
| D1.9 | **Contoh perhitungan resmi** (uji regresi) | contoh Yogyakarta Kep. Dirjen 273/1996 Bab X, contoh MKJI 1997 Bab 2 | sudah ada di `docs/sources/_teks_ekstraksi/` | 2 contoh | uji kalkulator (K-01: c=70 s, g=28/30 s, C=824, DS=0,44) |
| D1.10 | (opsional) **Inventaris aset awal** | CSV: id simpang, jenis perangkat (controller/lampu/tiang/kamera/DIS), merek, tahun (bila tahu), kondisi | dari foto D1.8 & tanya petugas | seadanya | F-T1-02/03 (jadwal pemeliharaan ≤6 bulan, umur ≤5 tahun) |

**Format umum:** CSV UTF-8, pemisah koma, titik desimal; satuan meter/detik/kendaraan; satu file per jenis data; nama file huruf kecil tanpa spasi. Template kolom persis seperti di atas akan saya buat di `packages/schemas/` saat sprint 1.

**Prioritas bila waktu terbatas:** D1.1 → D1.3 → D1.4 (satu simpang dulu) → D1.5 → D1.6. Dengan D1.1–D1.4 untuk 1 simpang saja, kalkulator dan editor plan sudah bisa didemokan; sisanya menyusul.

## T2 — Siap jual "Kendali Terkoordinasi" (estimasi; sebagian butuh izin Dishub)

| # | Data | Perkiraan isi | Sumber | Dipakai untuk |
|---|---|---|---|---|
| D2.1 | Hasil kuesioner `12` (merek/protokol controller, jaringan, kamera, ruang kendali) | jawaban 27 + 7 pertanyaan, foto label perangkat | Dishub Bandung + 1–2 vendor | keputusan adaptor (NTCIP/serial), kebutuhan edge |
| D2.2 | Dokumentasi protokol controller (manual/ICD vendor) | PDF/manual, contoh pesan | vendor (NDA) | adaptor RS-232 F-T2-30 |
| D2.3 | Akses baca status 1–3 controller nyata (read-only) atau log yang diekspor | status fase/detektor tiap 1 s; atau ekspor riwayat dari server vendor | Dishub (izin) | adaptor NTCIP/serial F-T1-28/F-T2-29, ATSPM dari data nyata F-T2-56 |
| D2.4 | Akses RTSP 3–10 kamera koridor | URL stream + kredensial (VPN) | Dishub | live view F-T2-95, uji stabilitas |
| D2.5 | Riwayat gangguan & keluhan (1 tahun) | tiket/aduan, waktu respons, jenis kerusakan | Dishub/CRM kota | health & alarm F-T2-44/45, SLA tiket F-T2-50, matriks diagnosis |
| D2.6 | Inventaris aset lengkap & jadwal pemeliharaan | daftar perangkat, tahun, kontrak | Dishub | F-T1-02/03, laporan aset |
| D2.7 | Data survei lalu lintas Dishub (LHR, kecepatan) 1–2 tahun terakhir | laporan/Excel | Dishub | kalibrasi, laporan V/C & kecepatan F-T2-66 |
| D2.8 | Jadwal/plan TOD resmi semua simpang koridor + SK penetapan (bila ada) | dokumen | Dishub | versi plan F-T2-23, referensi SK F-T1-05 |
| D2.9 | Daftar simpang seluruh kota (untuk demo skala 40 simpang) | CSV lokasi & status | open data/Dishub (`docs/sources/08`) | peta kota, uji beban 1 VM |

## T3 — Transisi "Responsif" (estimasi)

| # | Data | Perkiraan isi | Sumber |
|---|---|---|---|
| D3.1 | Stream kamera per pendekat di 3–5 simpang (untuk detektor virtual) + rekaman 24 jam × 7 hari untuk kalibrasi | RTSP + arsip | Dishub |
| D3.2 | Data pelat (ANPR) — hanya setelah DPIA & perjanjian; hash/enkripsi | event pelat, waktu, lokasi | kamera Dishub/vendor |
| D3.3 | AVL Trans Metro Bandung/BRT (posisi 5–10 s, rute, jadwal, headway) | API/CSV | operator bus (perjanjian) |
| D3.4 | Floating car multi-hari (≥4 minggu) atau probe mitra untuk penalaan offset | GPS | tim + mitra |
| D3.5 | Hi-res log controller (0,1 s) bila tersedia, atau data edge logger | event | controller/edge |
| D3.6 | Data cuaca & event kota (kalender acara, banjir) | API BMKG/Pemkot | publik |
| D3.7 | Data kecelakaan/pelanggaran agregat (untuk warrant & keselamatan) | tabel per simpang/tahun | Polres (perjanjian) |

## T4 — Setara ITCS "Adaptif Terpadu" (estimasi)

| # | Data | Sumber |
|---|---|---|
| D4.1 | Antrian/okupansi per link real-time semua simpang kritis (kamera AI/loop/radar) | perangkat lapangan |
| D4.2 | CAD/AVL pemadam & ambulans (unit ditugaskan, rute, posisi) | Damkar/119/112 (perjanjian) |
| D4.3 | Feed ETLE/Back Office Polri (status bukti, read-only), ICD Polri | Polda/Polres (Perpol 8/2023) |
| D4.4 | Bapenda (status pajak per pelat, query), DLH (uji emisi) — via perjanjian & PDP | instansi |
| D4.5 | Data tol/gerbang, cuaca, AQI | pengelola tol, BMKG, DLH |
| D4.6 | Riwayat volume ≥1 tahun untuk model prediksi 15–60 menit | sistem sendiri |
| D4.7 | Akumulasi kendaraan kawasan (MFD) untuk perimeter control | kamera/probe |

## T5 — Platform Mobilitas Kota (estimasi)

| # | Data | Sumber |
|---|---|---|
| D5.1 | Data multi-kota (tenant) dengan skema yang sama | kota-kota pembeli |
| D5.2 | OD/demand kota untuk twin mesoscopic (survei OD, probe, telco) | pemda/mitra data |
| D5.3 | Data kebijakan TDM (ruas & jam ganjil-genap/ERP, pengecualian) | Pergub/Perwal |
| D5.4 | Data terbuka publik yang diterbitkan balik (LOS, waktu tempuh, log prioritas anonim) | sistem sendiri |
| D5.5 | Algoritma pihak ketiga & data uji (marketplace shadow mode) | universitas/vendor |

## Lampiran — daftar cek pengumpulan T1 (bisa dicetak)

- [ ] Pilih koridor (3–5 simpang, ≤1 km antar simpang), catat id & koordinat (D1.1)
- [ ] Ukur geometri tiap pendekat dari citra satelit, verifikasi lapangan (D1.2)
- [ ] Rekam 3 siklus lampu per periode per simpang; isi `plan_eksisting.csv` (D1.3)
- [ ] Rekam/kumpulkan 3–5 klip video 30 menit + isi `video_meta.csv` (D1.5)
- [ ] Hitung arus 15-menit per gerakan dari video untuk jam puncak pagi/sore + 1 jam sepi (D1.4)
- [ ] Floating car ≥6 run/arah pagi & sore dengan GPS logger (D1.6)
- [ ] Foto tiap kaki simpang & kabinet (D1.8)
- [ ] Serahkan semua file dalam satu folder `data/pilot-bandung/T1/` (akan saya masukkan ke repo dengan LFS untuk video)
