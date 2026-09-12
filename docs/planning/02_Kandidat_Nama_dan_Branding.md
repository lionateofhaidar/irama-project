# 02 — Kandidat Nama & Branding
Status: draf untuk diputuskan user. Pemeriksaan ketersediaan yang saya lakukan hanya pencarian web sepintas; **pemeriksaan merek di PDKI-DJKI, domain, dan akun media sosial wajib dilakukan sebelum dipakai** (masuk checklist pra-GitHub).

## 1. Kriteria nama
1. Bahasa Indonesia atau terasa Indonesia, mudah diucapkan pejabat & wartawan, 2–3 suku kata.
2. Tidak mengunci ke Jakarta (LANCAR-Jakarta adalah brand Dishub DKI — jangan dipakai).
3. Menggambarkan hasil (arus lancar, irama, denyut kota), bukan teknologi (hindari "AI", "Smart" yang generik dan sudah dipakai banyak vendor).
4. Bisa menjadi akronim yang masuk akal untuk dokumen resmi pemda.
5. Bisa dipasangkan dengan nama kota ("… Bandung", "… Medan") untuk program lokal.
6. Aman dari merek yang sudah dikenal di transportasi (contoh yang harus dihindari: *Serasi* — Serasi Autoraya/Astra; *Travoy* — Jasa Marga; *Tol Kita* — BPJT).

## 2. Kandidat (urut rekomendasi)
| # | Nama | Makna | Akronim resmi (usulan) | Tagline | Catatan risiko |
|---|---|---|---|---|---|
| 1 | **IRAMA** | Irama = ritme; sinyal lalu lintas adalah irama kota; green wave = irama yang serasi | *Integrasi Rekayasa Adaptif & Manajemen APILL* | "Irama kota yang lancar" / "Mengatur irama, melancarkan kota" | Kata umum (musik); pencarian awal tidak menemukan produk lalu lintas bernama IRAMA; cek DJKI kelas 9 & 42 |
| 2 | **NADI** | Nadi = denyut/pembuluh utama; arteri kota; TMC sebagai "pemantau nadi" | *Navigasi Adaptif Dinamis Infrastruktur* atau *Nadi Lalu Lintas Kota* | "Denyut kota di ujung jari" | Ada pemakaian "NADI" di bidang lain (kesehatan/data); cek kelas merek |
| 3 | **ARUS** | Arus = aliran lalu lintas; langsung dimengerti | *Adaptive Road & Urban Signalling* | "Biar arus mengalir" | Sangat generik; banyak konten "arus mudik"; sulit dibedakan di pencarian |
| 4 | **LAJU** | Laju = kecepatan/pace; positif, pendek | *Lalu Lintas Adaptif Jaringan Urban* | "Laju kota, laju warga" | Perlu cek merek; ada kemiripan dengan nama fintech/startup [belum diverifikasi] |
| 5 | **GELOMBANG HIJAU / GEHIJAU** | Terjemahan green wave; teknis & visual | — | "Hijau terus, lancar terus" | Terlalu spesifik ke koordinasi; kurang cocok untuk modul inventaris/KPI |
| 6 | **PANDU LINTAS** | Pandu = memandu; ramah untuk publik | — | "Memandu lalu lintas kota" | Dua kata; "Pandu" dipakai banyak produk |
| 7 | **SIMPANG** (mis. "Simpang Cerdas") | Literal objek yang dikelola | — | — | Terlalu literal & mudah ditiru; cadangan untuk nama modul |

**Rekomendasi:** pilih **IRAMA** sebagai nama platform (dengan sub-merek modul: *IRAMA Pantau* = monitoring/TMC, *IRAMA Atur* = plan & kendali, *IRAMA Ukur* = KPI/ATSPM, *IRAMA Prioritas* = TSP/EVP, *IRAMA Twin* = simulasi), dan **NADI** sebagai cadangan. Alasan: IRAMA menyatu dengan konsep inti signal timing (cycle/offset/green wave = ritme), netral secara geografis, mudah dipasang nama kota ("IRAMA Bandung"), dan akronimnya menyebut APILL (istilah resmi regulasi) sehingga terdengar "resmi" di dokumen pemda.

## 3. Elemen branding awal (untuk dikembangkan di planning)
- **Positioning line:** "Sistem manajemen & kendali lalu lintas kota berbasis standar terbuka — terukur, bertahap, patuh aturan."
- **Bukti yang selalu ditampilkan:** LOS PM 96/2015, tundaan PKJI, arrival-on-green, uptime perangkat — bukan "AI".
- **Warna/visual:** hindari meniru kuning-biru LANCAR-Jakarta; pertimbangkan hijau (green wave) + abu gelap (TMC) [keputusan desain, belum dibuat].
- **Nama program per kota:** "IRAMA Kota Bandung" dst.; tagline lokal boleh diubah pemda (mirip branding Jak Lingko yang diatur pergub).
- **Nama teknis internal/repo:** `irama-platform` (monorepo) atau `irama-core`, `irama-edge`, `irama-twin` [usulan].

## 4. Tindakan sebelum nama dipakai (masuk checklist)
1. Cek merek di PDKI (pdki-indonesia.dgip.go.id) kelas 9 (perangkat lunak), 42 (jasa TI), 37/39 bila relevan.
2. Cek domain (.id, .co.id, .com) dan handle media sosial.
3. Cek nama badan usaha/produk vendor ATCS eksisting (Javis, Qumicon, TKDN, Intracs, dsb.) agar tidak mirip.
4. Uji sebut ke 3–5 orang Dishub/pemda: apakah mudah diingat & tidak berkonotasi negatif di daerah tertentu.
