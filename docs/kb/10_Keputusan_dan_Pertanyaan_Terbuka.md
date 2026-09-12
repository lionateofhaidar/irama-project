# 10 — Log Keputusan (yang tersirat dari bahan) & Pertanyaan Terbuka
Cara pakai: bagian A = keputusan desain yang sudah "dipaksa" oleh regulasi/bukti — jangan dibuka ulang tanpa alasan baru; bagian B = keputusan yang masih milik user; bagian C = pertanyaan riset yang belum terjawab dari bahan. Setiap baris punya sumber. Perbarui saat planning.

## A. Keputusan yang tersirat dari bahan (status: DIADOPSI)
| ID | Keputusan | Alasan/bukti | Sumber |
|---|---|---|---|
| D-01 | Fallback wajib: setiap controller menyimpan ≥8 rencana siklus TOD lokal; sistem pusat gagal → controller jalan sendiri | PM 49/2014 Ps.14; NTCIP backup timer; HOP-11-027 Need 4.14 | [R00 B], [R03 A.6], [R02 D.14] |
| D-02 | LOS simpang memakai ambang PM 96/2015 (A<5 … F>60 s/kend); HCM hanya untuk benchmark | kepatuhan & komparabilitas studi lokal | [R00 E], [R06 C.3] |
| D-03 | Rumus kinerja = PKJI 2023 (notasi terbaru), kompatibel MKJI 1997 & Kep. Dirjen 273/1996 | pedoman resmi; PM 49 Ps.18 | [R05 D], [R00 G] |
| D-04 | Antarmuka controller: NTCIP 1202 (dan 1211 untuk priority) wajib untuk pengadaan baru; controller lama via adaptor RS-232 vendor di balik satu abstraksi | anti lock-in; TSPH; R03 D.2 | [R02 G.7], [R03 D] |
| D-05 | Kendali real-time hanya lewat objek kontrol (hold/force-off/omit/call/pattern) + heartbeat < backup timer; perubahan plan lewat transaksi tervalidasi (Annex B) | fail-safe bawaan standar | [R03 A.6, A.14] |
| D-06 | ITCS/produk = subsistem SIK LLAJ yang terintegrasi ke pusat kendali Polri; menyediakan override petugas & preemption hak utama; ETLE hanya penyedia bukti | UU 22/2009 Ps.104, 135, 246–247, 272 | [R05 A.1, G.1 C-15/16/22/24] |
| D-07 | Simpang yang melibatkan jalan nasional di Jakarta/Jabodetabek: workflow persetujuan Dirjen/BPTJ | PM 96/2015 Ps.5; PM 76/2021 Ps.19 | [R05 A.3], [R00 C] |
| D-08 | Koordinasi hanya untuk grup ≥3 simpang berjarak ≤1 km; simpang adaptif otonom wajib detektor sehat | PM 96/2015 Lamp. II.F | [R00 E] |
| D-09 | Inti adaptif T4 = cyclic max-pressure (cycle/offset tetap, split adaptif, min green, rate-limit) di simpang kritis + perimeter control; bukan RL langsung | bukti Tsitsokas; RL belum pernah deployed | [R04 A.5, F] |
| D-10 | Prioritas bus kondisional berbasis occupancy/headway (OCC/Transit-MP; green extension/early green ≤10 s; 1 aktivasi/siklus; lockout); EVP bertingkat | OCC-MP, Transit-MP, TSP Handbook, Humagain | [R04 C], [R06 F.2] |
| D-11 | RL/AI hanya sebagai advisor via shadow mode dengan veto statistik sampai terbukti; LLM di luar control loop | Chen 2022; Bagabaldo 2025; BCT-APLight; Jan 2026 | [R04 A.2, A.3, A.15, A.17] |
| D-12 | ATSPM (hi-res log 0,1 s) sebagai observer independen untuk semua algoritma, termasuk AI vendor | HOP-20-002 | [R03 C.5] |
| D-13 | Transparansi: sistem melaporkan nilai antara yang dipengaruhi parameter kalibrasi & alasan keputusan | Req 18.0-1/2 | [R02 D.16] |
| D-14 | Evaluasi manfaat: desain on/off + before–after, memisahkan manfaat retiming dari sistem | TSPH; T414; NYSERDA | [R02 E.3, E.5] |
| D-15 | Data ANPR/pelat/CCTV = data pribadi → UU PDP: dasar pemrosesan, minimisasi, retensi, perjanjian antarinstansi; data terintegrasi milik Pemprov | UU 27/2022; Pergub 68/2021 Ps.10–11 | [KB-03], [R00 D] |
| D-16 | Deployment bertahap per koridor (pilot 3–5 simpang) dengan experimental plan; skala 321 simpang jauh melampaui praktik umum | T414 (65% agensi 5–15 sinyal) | [R02 H.3] |
| D-17 | Pemeliharaan & kesehatan perangkat adalah fitur inti (bukan tambahan): jadwal 6 bulan, umur 5 tahun, % detektor berfungsi, watchdog | PM 49 Ps.41–42; decommissioning ASCT karena deteksi/komunikasi/maintenance | [R00 B], [R02 F.5] |
| D-18 | Re-timing review ≤3 bulan (Dirjen 1996) / ≤3 tahun (NTOC) dicatat sebagai KPI program | Kep. Dirjen 273/1996; TSTM | [R00 G], [R01 H.2] |
| D-19 | Nama & branding tidak memakai "LANCAR" (milik Dishub DKI) | majalah h.17 | [analisis majalah] |
| D-20 | Server hemat: edge-first, agregasi di tepi, retensi bertingkat (hi-res ≈ 23 MB/simpang/hari [turunan dari 9 GB/hari/387 sinyal]) | HOP-20-002 | [R03 C.1] |

## B. Keputusan user — DIPUTUSKAN 2026-09-13 (log: `docs/LOG_SESI.md` T-20…T-24)
| ID | Keputusan | Hasil | Catatan/konsekuensi |
|---|---|---|---|
| U-01 | Nama produk | **IRAMA** (sementara; final setelah gambaran fitur end-state) | cek merek PDKI + domain wajib sebelum publikasi (lihat `docs/planning/11` E1–E2) |
| U-02 | Kota/koridor pilot | **Bandung** (basis personel) — Surabaya target ke-2 | dokumen pasar & kuesioner netral kota; data pilot Bandung di `docs/sources/08` & `docs/planning/13` |
| U-03 | Controller sendiri vs integrasi | **Integrasi; edge-light di T2** (agen minimal di mini-PC/Pi hanya untuk controller serial-only; edge penuh T3) | selisih effort edge ≈15–25% T2 [asumsi]; T1 tanpa edge |
| U-04 | Lisensi & hosting | **Open-core** (inti Apache-2.0, modul komersial terpisah); **on-prem default**, cloud opsional | ADR-01, ADR-15 |
| U-05 | Stack | **Python/FastAPI + agen edge Go; React + MapLibre + ECharts; PostgreSQL/PostGIS + TimescaleDB; MQTT; SUMO; Compose → k3s** | ADR-02…ADR-05 |
| U-06 | Tim & pendanaan | **2 orang sampai T2**, +1–2 di T3–T5, tanpa field engineer, dana sangat terbatas ("develop dulu, jual kemudian") → **simulation-first + mitra lapangan** (teknisi Dishub/vendor), design partner sejak akhir T1, lingkup dipangkas ke Must | jadwal 2 orang: T1 3–4 bulan, T2 6–9 bulan [asumsi]; T2 = demo + paket kesiapan pilot |
| U-07 | Cakupan T5 | **Platform Mobilitas Kota multi-tenant** (`docs/planning/04` §6) | — |
| U-08 | Deteksi kamera | **Hybrid** (konsumsi output vendor + hitung dasar sendiri di edge); **pemrosesan pelat menjadi output T3** | DPIA & tata kelola PDP (C-37…C-39) maju ke awal T3 |
| REPO | Repositori | repo privat terpisah `lionateofhaidar/irama-project`; monorepo (`docs/kb`, `docs/planning`, `docs/sources`); PDF & gambar via Git LFS | `docs/planning/10` |

## C. Pertanyaan riset/data yang belum terjawab dari bahan
| ID | Pertanyaan | Cara menjawab |
|---|---|---|
| Q-01 | Protokol & spesifikasi controller yang dipakai di kota target (merek, RS-232/NTCIP, hi-res log?) | **DIPUTUSKAN:** survei Dishub + vendor dengan kuesioner `docs/planning/12` (bahasa awam, asumsi umum tidak ditanyakan, netral kota) |
| Q-02 | ~~Kode enumerasi hi-res Indiana (tabel resmi)~~ **SELESAI (T-11)**: `02_Panduan_Praktis_Standar/Purdue_Indiana_HiRes_Data_Logger_Enumerations.pdf`; dipakai di KB-06 §C | — |
| Q-03 | NTCIP 1202 v03 & 1211 (objek priority, hi-res, SPaT) | **DIPUTUSKAN:** unduh/beli saat T2 dimulai (gratis di ntcip.org bila tersedia); daftar pengadaan lengkap di `docs/planning/11` |
| Q-04 | Metode di balik klaim "+20–30%" ITCS DKI; hasil uji coba 2023 | **DIPUTUSKAN: tidak dikejar**; pakai bukti internasional (NCHRP/FHWA) + hasil pilot sendiri (on/off) |
| Q-05 | Angka tundaan per pendekat Makassar & studi ATCS kota lain (tabel tidak terekstraksi) | **DIPUTUSKAN: prioritas rendah**, cukup sebagai konteks |
| Q-06 | Dataset lokasi ATCS Jakarta (data.jakarta.go.id) | **DIPUTUSKAN: diganti data kota pilot Bandung** (`docs/sources/08`, R07); kebutuhan data per tahap di `docs/planning/13` |
| Q-07 | ~~Perpol ETLE (8/2023, 2/2025)~~ **SELESAI (T-11)**; Pergub DKI turunan MRLL/ERP, PM 67/2021, Perdirjen tata cara waktu siklus **+ regulasi Jabar/Kota Bandung** | **DIPUTUSKAN: semua dikerjakan sekarang** → hasil di `docs/sources/_ringkasan/R07` (sesi 2026-09-13) |
| Q-08 | Ketersediaan & lisensi data probe GPS untuk evaluasi koridor | **DIPUTUSKAN: floating car sendiri + AVL bus kota (Trans Metro Bandung)**; ojol/navigasi setelah ada pembeli |
| Q-09 | Kebutuhan TKDN untuk perangkat lunak dalam e-katalog & cara sertifikasinya | **DIPUTUSKAN: lewat mitra vendor lokal dulu**; TKDN software sendiri setelah pembeli pertama |
| Q-10 | Rumus eksplisit platoon ratio & Link Pivot | **DIPUTUSKAN: unduh paper Purdue + rujuk kode ATSPM UDOT** (hasil unduhan di R07) |
| Q-11 | PKJI 2023 rumus Nq1 (5-15) tercetak "s" di dalam akar, padahal dimensi & MKJI/Dirjen 273 menunjukkan kapasitas C — keputusan implementasi sementara: pakai **C** (sesuai MKJI NQ1); **DIPUTUSKAN: pakai C**, uji ke contoh Dirjen 273/MKJI; konfirmasi erratum bila sempat | bandingkan `docs/sources/_teks_ekstraksi/PKJI_2023_*.txt` hlm. 5-15 dengan MKJI 1997 Bab 2; uji terhadap contoh Dirjen 273 |

Pointer ke detail: `docs/sources/_ringkasan/R00 §K`, `R02 H`, `R04 F`, `R05 G`, `docs/planning/08`.
