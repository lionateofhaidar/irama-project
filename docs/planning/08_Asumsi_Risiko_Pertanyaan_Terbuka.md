# 08 — Asumsi, Risiko Pra-Proyek, dan Pertanyaan Terbuka

Status: draf pra-perencanaan (2026-09-12). Setiap asumsi punya cara validasi; setiap pertanyaan punya rekomendasi default agar planning rinci bisa berjalan tanpa menunggu.

## 1. Asumsi (A-xx)

### Teknis
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-01 | Controller APILL di kota target (mayoritas produk lokal) dapat diakses lewat protokol vendor RS-232/TCP atau NTCIP; sebagian hanya "pilih plan" | SK.7234/2013 mewajibkan interface komunikasi ATCS pada controller [R00 H]; NTCIP hanya pada controller modern | Survei 3 kota: inventaris merek controller, protokol, dokumentasi; uji bench 2 merek |
| A-02 | Kamera CCTV eksisting cukup untuk hitung antrian/okupansi kasar via analitik edge (bukan ANPR) | Praktik DKI (kamera Viero + edge AI) [majalah]; degradasi malam/hujan [R04 A.2] | PoC analitik pada rekaman 3 simpang; ukur akurasi vs manual count |
| A-03 | Data probe (GPS bus, Google/TomTom, ojol) dapat diperoleh untuk evaluasi koridor dengan penetrasi ≥3% | Mahmud & Day 2023 [R04 A.19] | Uji dengan GPS bus BRT kota pilot; cek lisensi data komersial |
| A-04 | Kebutuhan server T2: satu VM 8 vCPU/32 GB untuk ≤50 simpang tanpa video di server [A] | ATSPM ~9 GB/hari untuk 387 sinyal [R03 C.1] → ~25 MB/simpang/hari | Prototipe beban di T1 |
| A-05 | Cyclic max-pressure + TOD fallback dapat berjalan dengan data antrian 10 s dan latensi komunikasi ≤2 s | Tsitsokas 2022 [R04 A.5] | SUMO NEMA twin (SIL) lalu shadow mode |
| A-06 | Jaringan komunikasi simpang–pusat tersedia (fiber/seluler 4G) dan diizinkan Diskominfo | Tipikal ATCS Indonesia memakai fiber/wireless [R02 F.4] | Cek per simpang saat survei |
| A-07 | Log hi-res 0,1 s tidak tersedia dari controller lama; perlu logger eksternal atau derivasi dari status poll 1 s | NCDOT: logger eksternal tak merekam termination type [R03 C.1] | Uji pada controller pilot |

### Pasar & bisnis
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-08 | Dishub kota target punya pos anggaran "pengembangan/pemeliharaan ATCS" tahunan yang bisa dipakai e-purchasing | Yogya, Kudus, Bekasi, Depok belanja ATCS 2023–2025 [Pra-Perencanaan 03] | Wawancara Kabid Lalin 3 kota; cek DPA/LPSE |
| A-09 | Harga software Rp25–60 jt/simpang diterima bila di bawah 20% biaya paket turnkey | Paket Rp350 jt–1,8 M/simpang [03] | Uji harga di 2 kota; bandingkan e-katalog |
| A-10 | Pilot 3–5 simpang berbiaya rendah dapat dilegalkan lewat PKS/swakelola tanpa tender | Perda 5/2014 Ps.239; Pergub 68 Ps.7 [R05] | Konsultasi bagian hukum pemda pilot |
| A-11 | Vendor controller lokal bersedia bermitra (bukan menghalangi) karena membuka pasar software | Javis sudah menjual ATMS sendiri → bisa bersaing [03] | Pendekatan 2 vendor |
| A-12 | Sertifikat TKDN untuk software dapat diperoleh <6 bulan | Perpres 46/2025 preferensi PDN [03] | Konsultasi Kemenperin/LKPP |

### Hukum & tata kelola
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-13 | Aplikasi cukup sebagai "penyedia bukti/data" untuk ETLE; penindakan tetap Polri | UU Ps.272, 260; PP 32 Ps.46 [R05] | Konfirmasi Ditlantas; jangan bangun fitur denda |
| A-14 | Pemda adalah pengendali data (UU PDP); vendor = prosesor; ANPR/plat = data pribadi | UU 27/2022 [Bahan Acuan] | Kajian PDP + PKS pengolahan data sebelum T3 |
| A-15 | Simpang jalan nasional di kota target bisa dioperasikan Dishub kota setelah persetujuan/koordinasi Dirjen/BPTJ | PM 96 Ps.5; PM 49 Ps.28 [R05] | Inventaris status jalan per simpang pilot |
| A-16 | Kewajiban ≥8 rencana siklus, LOS PM 96, pemeliharaan 6 bulan, umur teknis 5 tahun berlaku sebagai syarat produk | PM 49, PM 96 [R00] | Cek dengan konsultan/BPTJ |

### Sumber daya
| ID | Asumsi | Dasar | Validasi |
|---|---|---|---|
| A-17 | Tim inti T1: 1 PM/traffic engineer, 2 backend, 1 frontend, 1 edge/IoT, 1 data/ML paruh waktu [A] | Skala MVP 5 simpang | Diputuskan user (Q-02) |
| A-18 | Akses ke data uji nyata (log APILL, rekaman CCTV, count) dari satu Dishub dalam 2 bulan | Perlu PKS | Q-05 |
| A-19 | Dishub pilot menyediakan minimal 1 operator + 1 teknisi sebagai counterpart | Kebutuhan pelatihan & kalibrasi [R02] | Dalam PKS |

## 2. Register risiko pra-proyek (keputusan produk, pasar, tim, dana, mitra, hukum)

| ID | Risiko | Kemungkinan | Dampak | Mitigasi | Pemilik |
|---|---|---|---|---|---|
| R-01 | Salah asumsi "controller bisa dikendalikan": banyak APILL lama hanya bisa ganti plan lokal → adaptif detik-ke-detik mustahil | Tinggi | Tinggi | T1 desain "plan-level control" (pilih/ubah TOD & split via download) sebagai jalur utama; second-by-second hanya bila NTCIP/ vendor mendukung | Produk |
| R-02 | Vendor petahana memblokir akses protokol/menuntut lisensi | Sedang | Tinggi | Kemitraan B2B2G; adaptor via logger/relay; targetkan kota tanpa vendor dominan dulu | Bisnis |
| R-03 | Membangun terlalu banyak fitur ITCS (ANPR, ETLE, digital twin) sebelum ada pembeli | Tinggi | Tinggi | Disiplin tahap T1–T2 (lihat 04/05); tiap fitur harus punya persona & pembeli | Produk |
| R-04 | Klaim manfaat tidak bisa dibuktikan → kredibilitas hilang | Sedang | Tinggi | Modul before–after on/off sejak T1; MOE PM 96/PKJI; publikasi metode | Produk |
| R-05 | Siklus anggaran APBD melewatkan tahun → 12–18 bulan tanpa pendapatan | Tinggi | Sedang | Pilot swakelola; e-katalog; APBD-P; bidik 3 kota paralel | Bisnis |
| R-06 | Ketergantungan data mitra (AVL bus, Polri, probe komersial) tidak terwujud | Sedang | Sedang | Fitur inti tidak bergantung data mitra; TSP/EVP di T3 dengan MoU tertulis (detik prioritas) [R06] | Bisnis |
| R-07 | UU PDP: ANPR/plat tanpa dasar → sanksi/penolakan Diskominfo | Sedang | Tinggi | T1–T2 tanpa data pribadi; T3+ kajian PDP, minimisasi, hashing plat, retensi | Hukum |
| R-08 | Tim kecil tanpa traffic engineer bersertifikat → salah hitung PKJI/keselamatan (yellow/all-red) | Sedang | Tinggi | Rekrut/konsultan MRLL; validator rumus di aplikasi; uji SUMO | Tim |
| R-09 | Pemda menganggap "adaptif = set and forget" lalu sistem dikembalikan ke fixed-time (umur ASCT 6–7 tahun) | Tinggi | Tinggi | Paket wajib: pelatihan, AMS, KPI kesehatan, retiming ≤3 tahun [R02] | Bisnis/Produk |
| R-10 | Keamanan: kabinet/jaringan pemda lemah; insiden siber merusak reputasi | Sedang | Tinggi | NEMA TS 8, RBAC, audit log, heartbeat/backup timer NTCIP (controller kembali ke TOD) [R03] | Teknis |
| R-11 | Kompetisi harga dari paket turnkey vendor (software "gratis" ikut hardware) | Tinggi | Sedang | Diferensiasi: KPI resmi, transparansi, multi-vendor, analitik; jual ke kota yang sudah punya hardware | Bisnis |
| R-12 | Ketidakjelasan kewenangan (Dishub vs Polri vs BPTJ) menghambat go-live | Sedang | Sedang | Peta yurisdiksi per simpang; workflow persetujuan; libatkan Polantas sejak pilot | Produk/Bisnis |
| R-13 | Nama/merek bentrok dengan produk existing (mis. "SITS", "ATCS Kota X", "Lancar") | Sedang | Rendah | Cek merek DJKI & domain sebelum branding (lihat 02) | Bisnis |
| R-14 | Pendanaan pengembangan T1–T2 tidak cukup hingga pendapatan pertama (12–18 bulan) | Sedang | Tinggi | Q-01; cari pilot berbayar sebagian; hibah riset (Kedaireka/LPDP) [A] | Pemilik |

## 3. Pertanyaan terbuka untuk user (Q-xx) + rekomendasi default

| ID | Pertanyaan | Mengapa penting | Default bila tidak dijawab |
|---|---|---|---|
| Q-01 | Entitas & pendanaan: dikembangkan oleh perusahaan (Hydem Custodia & Co?) dengan modal sendiri, mitra, atau hibah? Berapa runway? | Menentukan skala T1 dan model bisnis | Bootstrapped 12 bulan; T1 dalam 3–4 bulan; T2 dalam 9 bulan |
| Q-02 | Tim: siapa yang tersedia (jumlah, keahlian backend/edge/ML/traffic engineering)? Ada traffic engineer/konsultan MRLL? | Kelayakan T1 & keselamatan | Tim 3–5 orang + 1 konsultan MRLL paruh waktu |
| Q-03 | Bangun/pasarkan hardware (controller/detektor) sendiri atau **software-only** di atas controller vendor? | Menentukan produk, TKDN, modal | **Software-only** + adaptor; hardware via mitra |
| Q-04 | Kota pilot pertama? Ada relasi di Dishub tertentu? | Menentukan survei, protokol controller, bahasa daerah data | 1 kota Bodetabek (akses & jarak) + 1 dari Bandung/Medan |
| Q-05 | Akses data uji: bisakah memperoleh log APILL/CCTV/count dari satu Dishub? Jika tidak, mulai dengan SUMO sintetis? | Kualitas MVP | Mulai SUMO (NEMA, koridor sintetis mirip kota pilot) + data publik CCTV |
| Q-06 | Preferensi stack (bahasa, DB, cloud/on-prem) & lisensi kode (open-source inti + modul komersial, atau proprietary)? | Arsitektur & GTM (SPBE/Diskominfo suka on-prem) | Python (algoritma/edge) + TypeScript (web) + PostgreSQL/TimescaleDB + MQTT; on-prem-first, container; inti proprietary dengan SDK/ICD terbuka [A] |
| Q-07 | Hosting: server pemda (Diskominfo), cloud lokal (mis. BSSN-compliant), atau hybrid? | Keamanan & biaya | On-prem pemda/hybrid; cloud hanya untuk analitik agregat |
| Q-08 | Apakah ETLE/pajak/uji emisi masuk roadmap, atau hanya "penyedia bukti"? | PDP & kewenangan | Hanya penyedia bukti/agregat (T4), tidak ada modul penindakan |
| Q-09 | Bahasa produk: Indonesia saja atau dwibahasa (untuk vendor/standar)? | UI & dokumentasi | UI Indonesia, istilah teknis EN, dokumen API EN |
| Q-10 | Nama & merek: apakah ada preferensi/konotasi yang dihindari; perlu cek DJKI? | Branding | Lihat 02 Kandidat Nama; cek DJKI & domain sebelum T2 |
| Q-11 | Batas keterlibatan Polri: cukup akses baca + log, atau override langsung dari TMC Polda? | Desain RBAC & yurisdiksi | Akses baca + tombol plan darurat dengan approval Dishub (T2); override langsung T3 dengan PKS |
| Q-12 | Apakah ingin menerbitkan bagian inti sebagai open source untuk kepercayaan pemda/akademisi? | Adopsi & TKDN | Buka SDK/adaptor & ICD; inti tetap tertutup sampai T3 |
| Q-13 | Target waktu tayang e-katalog & sertifikasi TKDN? | GTM | Mulai proses saat T1 selesai |

## 4. Keputusan yang sudah tersirat dari bahan acuan (dianggap tetap kecuali user membatalkan)

| ID | Keputusan | Sumber |
|---|---|---|
| D-01 | Standar antarmuka controller: NTCIP 1202 (+1211 untuk prioritas) sebagai bahasa internal; adaptor untuk vendor lama | R02 G.7, R03 |
| D-02 | LOS simpang memakai ambang PM 96/2015; kinerja dihitung PKJI 2023 (MKJI sebagai pembanding) | R00 E, R05 D |
| D-03 | Fallback wajib: ≥8 rencana TOD; degradasi adaptif → actuated → TOD lokal → flash; heartbeat < backup timer | PM 49 Ps.14; HOP-11-027; NTCIP `unitBackupTime` |
| D-04 | Inti adaptif realistis: cyclic max-pressure terkoordinasi (cycle/offset tetap, split adaptif, min green, rate-limit) di simpang kritis; RL hanya advisor via shadow mode | R04 F |
| D-05 | Prioritas bus kondisional berbasis occupancy/headway (green extension/early green ≤10 s, 1 aktivasi/siklus, lockout); EVP bertingkat | R04, R06 |
| D-06 | ATSPM sebagai observer independen; log hi-res 0,1 s sebagai sumber kebenaran KPI; pipeline sama untuk lapangan & SUMO | R03 D |
| D-07 | Evaluasi manfaat wajib desain on/off + before–after, terpisah dari manfaat retiming | R02 E |
| D-08 | Aplikasi = penyedia bukti/data untuk ETLE; bukan penindak; data pribadi diminimalkan (UU PDP) | R05 G |
| D-09 | Keamanan: NEMA TS 8, RBAC per yurisdiksi, audit log semua perintah, LLM di luar control loop | R02 G.7, R04 A.17 |
| D-10 | Deployment bertahap per koridor (≥3 simpang ≤1 km) dengan pilot & experimental plan | PM 96; R02 H.3 |
| D-11 | Transparansi algoritma: nilai perhitungan antara & alasan keputusan tersimpan dan dapat dilaporkan ke publik/pejabat | HOP-11-027 Req 18.0-1/2, 6.0-11 |
| D-12 | Dukung stage-based (Indonesia) dan ring-barrier (NTCIP) dalam model data | R00 I |
