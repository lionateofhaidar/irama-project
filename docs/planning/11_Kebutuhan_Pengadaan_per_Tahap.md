# 11 — Kebutuhan Pengadaan Proyek Mandiri per Tahap (versi non-teknis)

Status: 2026-09-13, menjawab permintaan user (Q-03). Konteks: tim 2 orang sampai T2, dana sangat terbatas, "develop dulu baru jual", pilot Bandung, edge-light di T2, open-core on-prem. Semua harga adalah **perkiraan 2026 [perkiraan]** untuk gambaran urutan besaran, bukan penawaran; verifikasi sebelum membeli.

**Cara membaca.** Tiap baris = satu hal yang harus "diadakan" (dibeli, disewa, dipinjam, diurus). Kolom **Tahap** = kapan paling tepat diadakan. Kolom **Bila tidak/terlambat** = apa yang terjadi kalau tidak diadakan atau diadakan setelah tahapnya. Kolom **Bila terlalu awal** = kerugian bila dibeli sebelum waktunya. Prinsip umum: **jangan membeli sebelum ada pertanyaan yang hanya bisa dijawab dengan barang itu.**

Ringkasan biaya kas minimum: **T1 ≈ Rp 0–2 juta** (semua bisa gratis/laptop sendiri); **T2 ≈ Rp 8–25 juta** (mini-PC, kamera uji, VM demo, merek, badan usaha) + controller bench Rp 0–60 juta tergantung bisa pinjam atau tidak; **T3 ≈ Rp 15–40 juta** (edge AI, server); T4–T5 tergantung kontrak pembeli (server/cluster & integrasi dibiayai proyek).

## A. Dokumen, standar, dan pedoman

| # | Item | Untuk apa | Tahap | Harga [perkiraan] | Bila tidak/terlambat | Bila terlalu awal |
|---|---|---|---|---|---|---|
| A1 | PKJI 2023, MKJI 1997, Kep. Dirjen 273/1996, SK Dirjen 7234/2013, PM 49/96/76, UU 22/2009, UU PDP | rumus kalkulator, validator, kepatuhan | **T1 (sudah ada)** | gratis | — | — |
| A2 | NTCIP 1202 v02 (sudah ada) | model data & adaptor baca status | T1 (sudah ada) | gratis (ntcip.org) | — | — |
| A3 | **NTCIP 1202 v03** dan **NTCIP 1211** (prioritas bus/darurat) | skema data mengikuti versi terbaru; objek prioritas untuk controller standar | **awal T2** (sebelum skema data dibekukan) | biasanya **gratis** setelah registrasi di ntcip.org (v02 kita dapat dari sana); bila dijual, ±USD 100–300/dokumen | skema data harus diubah belakangan (migrasi data & ulang uji adaptor, ±2–4 minggu kerja); prioritas bus di T3/T4 tidak kompatibel dengan controller NTCIP baru | tidak ada kerugian selain waktu baca; boleh diambil sekarang bila gratis |
| A4 | NEMA TS 2 (kabinet/controller) & NEMA TS 8 (keamanan siber kabinet) | spesifikasi pengadaan controller baru & checklist keamanan T2 | T2 (TS 8), T4 (TS 2) | USD 300–600/dokumen; ringkasan publik sering cukup | checklist keamanan dibuat dari sumber sekunder (cukup untuk T2); risiko kecil | dana terbuang bila akhirnya controller lokal non-NEMA |
| A5 | HCM (Highway Capacity Manual, ed. 7) | benchmark internasional LOS | opsional T3+ | USD 400–600 | tidak ada; LOS memakai PM 96 & PKJI | tidak perlu sama sekali sampai ada pembeli yang meminta HCM |
| A6 | Paper/laporan Purdue (Link Pivot, ATSPM) & kode ATSPM UDOT | metrik koridor T2–T3 | T2 | gratis (open access, GitHub) | metrik AoG/Link Pivot dibuat "versi sendiri", sulit dibandingkan dengan praktik internasional | — |
| A7 | Regulasi Jabar/Kota Bandung (Perda perhubungan, Perwal ATCS) | kepatuhan & argumen ke Dishub Bandung | **T1 (sedang diunduh)** | gratis (JDIH/BPK) | proposal ke Dishub tidak mengutip aturan lokal → kurang meyakinkan | — |

## B. Perangkat keras

| # | Item | Untuk apa | Tahap | Harga [perkiraan] | Bila tidak/terlambat | Bila terlalu awal |
|---|---|---|---|---|---|---|
| B1 | Laptop pengembang (16 GB RAM, cukup untuk SUMO + Docker) ×2 | seluruh T1 | T1 | sudah dimiliki | tidak bisa mulai | — |
| B2 | **Mini-PC/Raspberry Pi 5 (8 GB) + casing + catu daya** ×1–2 | bukti edge-light: adaptor jalan di alat kecil, buffer offline, heartbeat | **pertengahan T2** (setelah protokol controller diketahui dari kuesioner) | Rp 1,5–3 juta/unit (Pi) atau Rp 5–10 juta (mini-PC industri) | klaim "tetap aman saat jaringan putus" tidak bisa didemokan ke Dishub; edge baru diuji saat pilot → risiko gagal di depan pembeli | membeli sebelum tahu port/protokol controller bisa salah pilih (butuh RS-485, port serial, catu daya kabinet) |
| B3 | **Controller APILL untuk uji meja (bench)** ×1 | menguji adaptor nyata (bukan simulasi) sebelum pilot; HIL | **akhir T2** (sebelum "siap jual" dinyatakan) | pinjam/sewa dari vendor: Rp 0–5 juta; beli baru controller lokal: Rp 30–80 juta; controller NTCIP impor: >Rp 100 juta | adaptor hanya teruji di simulator; pilot pertama menjadi tempat debugging di lapangan (memakan kepercayaan Dishub). **Jalan tengah:** uji langsung di 1 kabinet Dishub (read-only) dengan izin, ini pengganti bench paling murah | uang besar terkunci pada merek yang mungkin bukan merek kota pilot |
| B4 | Kamera IP (RTSP/ONVIF) uji ×1 + tripod | uji pipeline video (live view, hitung kendaraan dasar) dari stream nyata | T2 | Rp 1–3 juta | pipeline hanya diuji dari file rekaman; masalah latensi/putus stream baru muncul di pilot | — |
| B5 | Ponsel dengan GPS logger (gratis) | floating car survei koridor (Q-08) | **T1** | Rp 0 | tidak ada data waktu tempuh koridor untuk before–after | — |
| B6 | **Edge AI box** (Jetson Orin Nano/NX) ×1–2 | detektor virtual dari kamera (count/antrian/pelat) di T3 | **awal T3** | Rp 6–12 juta/unit | fitur virtual detector & pelat (U-08, T3) diuji hanya di laptop; performa nyata di kabinet tidak diketahui | membeli di T1/T2 = dana menganggur ±1 tahun; generasi baru lebih murah |
| B7 | UPS kecil & switch PoE untuk rak uji | replika kabinet | T3 | Rp 2–4 juta | — | — |
| B8 | Server pilot (on-prem di Dishub) 8 vCPU/32 GB/1 TB | T2 "siap jual" di kantor pembeli | **saat pilot berbayar** (dibiayai pembeli/pilot) | Rp 25–50 juta (fisik) atau sewa VM Rp 1,5–3 juta/bulan | demo berjalan di laptop/VM sewaan (cukup untuk presentasi) | jangan beli sendiri; ini biaya proyek pembeli |

## C. Layanan daring & perangkat lunak

| # | Item | Untuk apa | Tahap | Harga [perkiraan] | Bila tidak/terlambat | Bila terlalu awal |
|---|---|---|---|---|---|---|
| C1 | GitHub (repo privat, LFS 1 GB) | kode & dokumen | T1 (sudah) | gratis; GitHub Team USD 4/pengguna/bulan bila butuh branch protection lanjutan | — | — |
| C2 | SUMO, PostgreSQL/PostGIS/TimescaleDB, MQTT, MapLibre, YOLO, Docker | seluruh stack | T1 | gratis (open source) | — | — |
| C3 | **VM demo publik** (4 vCPU/8–16 GB) | demo daring ke Dishub tanpa membawa laptop; uji stabilitas 30 hari | **akhir T1 / awal T2** (saat mulai presentasi) | Rp 300–900 ribu/bulan | demo hanya lewat laptop; tidak ada bukti "berjalan stabil 30 hari" | biaya bulanan berjalan tanpa penonton |
| C4 | Domain (.id/.co.id) + email bisnis | kredibilitas saat menghubungi Dishub/vendor | **awal T2** (sebelum surat/kuesioner dikirim) | Rp 150–400 ribu/tahun (+ email Rp 0–70 ribu/pengguna/bulan) | surat dari email gratisan kurang meyakinkan pejabat | — |
| C5 | Peta dasar (OSM self-host / MapTiler / Mapbox) | peta TMC | T1 (OSM gratis); layanan berbayar bila peta harus mulus di demo | Rp 0–500 ribu/bulan | — | — |
| C6 | Alat kolaborasi (Notion/Google Workspace gratis) | dokumen, jadwal | T1 | Rp 0 | — | — |
| C7 | Sertifikat TLS, VPN untuk edge (WireGuard) | keamanan T2 | T2 | Rp 0 (Let's Encrypt, open source) | — | — |
| C8 | GPU cloud sesekali (pelatihan model deteksi) | melatih ulang model hitung kendaraan pada rekaman Indonesia (motor dominan) | T3 | Rp 20–60 ribu/jam, total Rp 1–3 juta | akurasi malam/hujan rendah; fitur virtual detector kurang dipercaya | — |

## D. Data (rincian di `13_Kebutuhan_Data_per_Tahap.md`)

| # | Item | Tahap | Biaya | Bila tidak/terlambat |
|---|---|---|---|---|
| D1 | Rekaman CCTV 3–5 klip ±30 menit (user menyediakan) | T1 | Rp 0 | pipeline video tidak bisa dibangun/diuji |
| D2 | Survei hitung kendaraan & geometri 3–5 simpang koridor pilot (hitung dari video/kunjungan) | T1 | Rp 0–1 juta (transport) | kalkulator PKJI hanya diuji dengan contoh buku; demo tidak "terasa Bandung" |
| D3 | Floating car ≥6 run/arah pada koridor pilot | T1–T2 | Rp 0–500 ribu (BBM) | tidak ada angka waktu tempuh sebelum/sesudah |
| D4 | Akses log/status controller & RTSP CCTV dari Dishub (izin) | T2 | Rp 0 (surat/MoU) | adaptor nyata & ATSPM dari data nyata tertunda ke pilot |
| D5 | AVL Trans Metro Bandung / operator bus | T3 | Rp 0 (perjanjian) | prioritas bus hanya di simulasi |
| D6 | Data probe komersial (TomTom/HERE) | opsional T3+ | Rp 5–30 juta/tahun | tidak wajib; floating car & AVL cukup |

## E. Legal, badan usaha, merek, sertifikasi

| # | Item | Untuk apa | Tahap | Harga [perkiraan] | Bila tidak/terlambat | Bila terlalu awal |
|---|---|---|---|---|---|---|
| E1 | **Cek merek "IRAMA" di PDKI + domain** | memastikan nama aman | **sekarang (T1)** | Rp 0 (cek daring) | rebranding setelah materi & repo dibuat: rugi waktu & kredibilitas | — |
| E2 | **Pendaftaran merek** (kelas 9 perangkat lunak, kelas 42 jasa) | perlindungan nama saat mulai dipresentasikan | **akhir T1 / awal T2** | Rp 500 ribu (UMK) – 1,8 juta per kelas + jasa konsultan opsional | nama bisa didahului pihak lain setelah demo publik | — |
| E3 | **Badan usaha** (Perseroan Perorangan atau PT) + NPWP + rekening | syarat MoU pilot, kerja sama vendor, e-katalog, hibah | **sebelum MoU pilot (T2)** | PT Perorangan: Rp 50–300 ribu (OSS); PT biasa via notaris: Rp 3–8 juta | tidak bisa tanda tangan MoU/kontrak pilot; hibah/kerja sama kampus terhambat | biaya tahunan (laporan pajak, SPT) sebelum ada pendapatan — kecil untuk PT Perorangan |
| E4 | Perjanjian kerahasiaan (NDA) & perjanjian data (template) | menerima dokumen protokol vendor & data Dishub; kewajiban PDP | T2 | Rp 0–2 juta (template/konsultasi) | vendor enggan berbagi dokumentasi; risiko PDP saat menerima rekaman/pelat | — |
| E5 | Kebijakan privasi + DPIA (penilaian dampak PDP) | wajib sebelum memproses pelat (U-08: pelat mulai T3) | **awal T3** (sebelum ANPR diaktifkan) | Rp 0 (disusun sendiri) – 10 juta (konsultan) | pelanggaran UU PDP (sanksi administratif/pidana), Dishub tidak berani memakai fitur pelat | — |
| E6 | **TKDN perangkat lunak** | syarat e-katalog/tender pemda | lewat mitra vendor (T2); sendiri setelah pembeli pertama (T3) | Rp 0 (Kemenperin gratis untuk software domestik; butuh dokumen & badan usaha) | tidak bisa masuk e-katalog sendiri; bergantung mitra | — |
| E7 | Lisensi open-core (teks Apache-2.0 + lisensi komersial modul) | kejelasan hukum kode | T2 (sebelum kode dibagikan ke pihak luar) | Rp 0–5 juta (review hukum) | ambiguitas hak saat kolaborasi kampus/vendor | — |
| E8 | Sertifikasi perangkat Kemenhub | wajib untuk perangkat TI di APILL (PM 49 Ps.25) — **berlaku untuk perangkat vendor**, bukan software | T4 (bila menjual perangkat sendiri) | ditanggung vendor | edge box buatan sendiri tidak boleh dipasang permanen di APILL tanpa sertifikat → pakai perangkat vendor bersertifikat atau posisikan edge sebagai "komputer ruang kendali mini" di luar jalur sinyal | — |
| E9 | Asuransi tanggung gugat / klausul batas tanggung jawab | bila software mengubah lampu lalu lintas | T2 (dalam MoU pilot: pilot read-only dulu, perubahan hanya oleh petugas) | Rp 0 (klausul) | tuntutan bila terjadi kecelakaan saat pilot | — |

## F. SDM & pengetahuan (bukan pembelian, tetapi harus "diadakan")

| # | Item | Tahap | Bentuk | Bila tidak |
|---|---|---|---|---|
| F1 | Pendamping traffic engineer paruh waktu (dosen/mahasiswa S2 ITB/Unpar/Itenas) | T1–T2 | kolaborasi riset/hibah (Kedaireka) atau honor kecil | kalkulator & plan tidak divalidasi praktisi; kredibilitas di depan Dishub rendah |
| F2 | Teknisi lapangan mitra (teknisi Dishub atau vendor) | T2 pilot | MoU | pemasangan edge & pengujian kabinet tidak bisa dilakukan tim (tidak ada field engineer) |
| F3 | Pelatihan singkat NTCIP/ATSPM (gratis: FHWA/ITE webinar, dokumentasi UDOT) | T2 | mandiri | — |

## G. Urutan pengadaan yang disarankan (garis waktu 2 orang)

1. **Bulan 0 (sekarang):** cek merek & domain (E1); unduh NTCIP v03/1211 bila gratis (A3); regulasi Bandung (A7). Biaya ≈ Rp 0.
2. **Bulan 1–4 (T1):** tidak membeli apa pun; data D1–D3 dikumpulkan sendiri; kolaborasi F1 dijajaki.
3. **Bulan 4–5 (akhir T1):** VM demo (C3), domain & email (C4), daftar merek (E2), PT Perorangan (E3). Biaya ≈ Rp 2–5 juta + Rp 0,5–1 juta/bulan.
4. **Bulan 5–7 (T2 awal):** kuesioner ke Dishub/vendor (`12`) → keputusan adaptor; **baru** beli mini-PC/Pi (B2) dan kamera uji (B4). Biaya ≈ Rp 3–13 juta.
5. **Bulan 8–12 (T2 akhir):** akses bench/kabinet Dishub (B3 jalan tengah), NDA (E4), MoU pilot read-only (E9), TKDN via mitra (E6).
6. **T3:** edge AI (B6), DPIA (E5), GPU cloud (C8), AVL bus (D5).
7. **T4–T5:** server/cluster, integrasi instansi, sertifikasi — dibiayai kontrak.

Rujukan: `docs/planning/04` (tahapan), `06` (arsitektur), `03` (pengadaan pemda & TKDN), `docs/kb/03` (kepatuhan C-xx), `docs/kb/10` (U-/Q-).
