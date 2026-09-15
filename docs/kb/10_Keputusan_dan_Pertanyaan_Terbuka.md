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
| D-08 | Koordinasi hanya untuk grup ≥3 simpang berjarak ≤1 km (mulai T4); simpang adaptif otonom wajib detektor sehat | PM 96/2015 Lamp. II.F | [R00 E] |
| D-09 | **Direvisi 2026-09-14:** inti adaptif T4 = actuated, pembagian hijau dengan batas perubahan per siklus, pemilihan program (TRPS), dan offset dasar; cyclic max-pressure (cycle/offset tetap, split adaptif, min green, rate-limit) di simpang kritis + perimeter control pindah ke T5; bukan RL langsung | bukti Tsitsokas; RL belum pernah deployed | [R04 A.5, F] |
| D-10 | **Direvisi 2026-09-14:** prioritas bus berbasis aturan (green extension/early green ≤10 s; 1 aktivasi/siklus; lockout) dan EVP bertingkat di T4; prioritas bersyarat berbasis occupancy/headway (OCC/Transit-MP) di T5 | OCC-MP, Transit-MP, TSP Handbook, Humagain | [R04 C], [R06 F.2] |
| D-11 | RL/AI hanya sebagai advisor via shadow mode dengan veto statistik sampai terbukti; LLM di luar control loop | Chen 2022; Bagabaldo 2025; BCT-APLight; Jan 2026 | [R04 A.2, A.3, A.15, A.17] |
| D-12 | ATSPM (hi-res log 0,1 s) sebagai observer independen untuk semua algoritma, termasuk AI vendor | HOP-20-002 | [R03 C.5] |
| D-13 | Transparansi: sistem melaporkan nilai antara yang dipengaruhi parameter kalibrasi & alasan keputusan | Req 18.0-1/2 | [R02 D.16] |
| D-14 | Evaluasi manfaat: desain on/off + before–after, memisahkan manfaat retiming dari sistem | TSPH; T414; NYSERDA | [R02 E.3, E.5] |
| D-15 | Data ANPR/pelat/CCTV = data pribadi → UU PDP: dasar pemrosesan, minimisasi, retensi, perjanjian antarinstansi; data terintegrasi milik Pemprov | UU 27/2022; Pergub 68/2021 Ps.10–11 | [KB-03], [R00 D] |
| D-16 | **Direvisi 2026-09-14:** deployment bertahap dari satu simpang (T1–T2), beberapa simpang mandiri (T3), koordinasi dasar (T4), koridor dan jaringan (T5), dengan experimental plan; skala 321 simpang jauh melampaui praktik umum | T414 (65% agensi 5–15 sinyal) | [R02 H.3] |
| D-17 | Pemeliharaan & kesehatan perangkat adalah fitur inti (bukan tambahan): jadwal 6 bulan, umur 5 tahun, % detektor berfungsi, watchdog | PM 49 Ps.41–42; decommissioning ASCT karena deteksi/komunikasi/maintenance | [R00 B], [R02 F.5] |
| D-18 | Re-timing review ≤3 bulan (Dirjen 1996) / ≤3 tahun (NTOC) dicatat sebagai KPI program | Kep. Dirjen 273/1996; TSTM | [R00 G], [R01 H.2] |
| D-19 | Nama & branding tidak memakai "LANCAR" (milik Dishub DKI) | majalah h.17 | [analisis majalah] |
| D-20 | **Direvisi 2026-09-14:** hemat sumber daya: T1–T3 di laptop tim tanpa pengadaan; video mentah dihapus setelah diolah; edge dan agregasi di tepi mulai T4; retensi bertingkat (hi-res ≈ 23 MB/simpang/hari [turunan dari 9 GB/hari/387 sinyal]) | HOP-20-002 | [R03 C.1] |

## B. Keputusan user — DIPUTUSKAN 2026-09-13 (log: `docs/LOG_SESI.md` T-20…T-24)
| ID | Keputusan | Hasil | Catatan/konsekuensi |
|---|---|---|---|
| U-01 | Nama produk | **IRAMA** (sementara; final setelah gambaran fitur end-state) | cek merek PDKI + domain wajib sebelum publikasi (lihat `docs/planning/11` B1–B2). **Status 2026-09-15:** penelusuran awal PDKI oleh user tidak menemukan merek IRAMA untuk produk sejenis; banyak merek IRAMA terdaftar di bidang lain. Sisa cek sebelum mendaftar: kelas dan uraian barang/jasa merek IRAMA yang ada (terutama kelas 9 dan 42), permohonan yang masih diproses, variasi ejaan dan gabungan kata, merek terkenal, domain, dan nama PT di AHU |
| U-02 | Kota/koridor pilot | **Bandung** (basis personel) — Surabaya target ke-2 | dokumen pasar & kuesioner netral kota; data pilot Bandung di `docs/sources/08` & `docs/planning/13` |
| U-03 | Controller sendiri vs integrasi | **Integrasi.** ~~Edge-light di T2, edge penuh T3~~ → **direvisi 2026-09-14 (U-22): tanpa edge sampai T3; controller dibaca tanpa diubah di T3; edge dan adaptor kendali mulai T4** | selaras keputusan nol pengadaan sampai T3 |
| U-04 | Lisensi & hosting | **Open-core** (inti Apache-2.0, modul komersial terpisah); **on-prem default**, cloud opsional | ADR-01, ADR-15 |
| U-05 | Stack | **Python/FastAPI + agen edge Go; React + MapLibre + ECharts; PostgreSQL/PostGIS + TimescaleDB; MQTT; SUMO; Compose → k3s**. Dilengkapi 2026-09-14: Vision Tracker (FFmpeg/OpenCV, RF-DETR atau YOLOX lewat ONNX Runtime, ByteTrack/supervision, MediaMTX); TimescaleDB opsional; MQTT dan agen edge mulai T4 | ADR-02…ADR-05, ADR-19…ADR-25; lisensi di `docs/planning/06` §4 |
| U-06 | Tim & pendanaan | **2 orang sampai T2**, +1–2 di T3–T5, tanpa field engineer, dana sangat terbatas ("develop dulu, jual kemudian") → ~~simulation-first~~ **recording-first** (direvisi 2026-09-14: rekaman CCTV dan video publik diolah Vision Tracker di laptop) + mitra lapangan (teknisi Dishub/vendor), design partner sejak akhir T1, lingkup dipangkas ke Must | tanpa tanggal, berbasis capaian (U-29); perkiraan effort di `docs/planning/04`; T2 = Vision Tracker + Optimasi Simpang, dijual awal sebagai jasa kajian |
| U-07 | Cakupan T5 | **Platform Mobilitas Kota multi-tenant** (`docs/planning/04` §6) | — |
| U-08 | Deteksi kamera | ~~Hybrid; pelat di T3~~ → **direvisi 2026-09-14 (U-09, U-21): Vision Tracker sendiri (model berlisensi bebas, format ONNX) dari rekaman di laptop sampai T3 dan di edge mulai T4; keluaran analitik vendor hanya pembanding; T3 bukti pelanggaran tanpa pelat; ANPR dengan kamera khusus di T4** | DPIA sebelum memproses data Dishub (awal T3); DPIA diperbarui sebelum ANPR (T4) |
| REPO | Repositori | repo privat terpisah `lionateofhaidar/irama-project`; monorepo (`docs/kb`, `docs/planning`, `docs/sources`); PDF & gambar via Git LFS | `docs/planning/10` |

## B2. Keputusan user — DIPUTUSKAN 2026-09-14 (log: `docs/LOG_SESI.md` T-34…T-42)
| ID | Keputusan | Hasil | Catatan/konsekuensi |
|---|---|---|---|
| U-09 | Fokus T2 | **Vision Tracker yang berjalan baik + modul Optimasi Adaptif Waktu Simpang**; pengembangan lanjutan bertahap di T3–T5 | spesifikasi `docs/planning/15`; tahapan `docs/planning/04` |
| U-10 | Lingkup T1 | **Purwarupa ujung ke ujung satu simpang** (hitung enam kelas dari rekaman, formulir sederhana, kalkulator PKJI 2023, rekomendasi, dashboard dasar) | kriteria di `04` bagian 2 |
| U-11 | Mode Vision Tracker | **Rekaman dan stream**; rekaman sebagai kanal piloting dan pengujian awal; mode stream diuji dengan rekaman yang diputar ulang lewat MediaMTX | F-T2-147 |
| U-12 | Skala T2 dan koridor | **Satu simpang lengkap di T2**; offset dasar dan green wave sederhana di T4; optimasi koridor dan jaringan penuh di T5 | D-08, D-09, D-16 direvisi |
| U-13 | Akurasi | **95% siang dan 90% malam atau hujan**, dilonggarkan di T1–T2 menjadi sekitar 90% dan 85% (T-39); penalaan ke 95% dan 90% mulai T3 | rumus di `16` langkah H |
| U-14 | Standar dan LOS | **PKJI 2023 utama + mode pembanding MKJI 1997**; LOS resmi dari tundaan PM 96/2015, derajat kejenuhan pendukung (batas desain 0,85) | D-02, D-03 tetap |
| U-15 | Mode optimasi | **Webster/PKJI baku (T1); tundaan terendah dengan batasan, DJ tertinggi minimal, siklus praktis minimum, pertahankan siklus eksisting (T2); multi-kriteria berbobot (T3)** | dua mode tambahan adalah usulan dengan effort setara atau lebih rendah, disetujui user |
| U-16 | Periode | **Profil 15 menit dikelompokkan otomatis menjadi paling banyak delapan jadwal**, dengan periode manual lewat konfigurasi simpang | PM 49/2014 |
| U-17 | Kelas kendaraan | **Enam kelas rinci dipetakan otomatis ke PKJI (dan MKJI)**; angkot dan pikap dipisahkan di T3 | F-T3-156 |
| U-18 | Hambatan samping dan arah | **Empat jenis kejadian berbobot PKJI 2023** per 200 m per jam; volume per arah dari lintasan dengan cadangan proporsi belok manual | F-T2-145, F-T2-146 |
| U-19 | Keluaran T2 | **Manfaat rupiah sederhana, laporan kajian Word/PDF, validasi PKJI + SUMO**; dashboard dipisah menjadi tiga halaman yang rapi | `15` bagian 6 |
| U-20 | Anomali T3 | **Kendaraan prioritas dan pengawalan, kejadian lalu lintas, pelanggaran sebagai bukti, kesehatan kamera dasar** (lanjutan di T4); vision tambahan: nyala lampu (T2), antrian (dasar T2, lengkap T3), penyeberang dan kecepatan antarkamera (T3) | `05` epik E20 |
| U-21 | ANPR dan controller | **ANPR ke T4** dengan kamera khusus; **controller baca-saja dan ekspor jadwal di T3; kendali di T4**; T2 adalah sistem pendukung keputusan | U-08 direvisi |
| U-22 | Pengadaan dan komputasi | **Produk nol biaya sampai T3 selesai**; biaya administrasi bisnis boleh; **laptop tim sampai T3** | `docs/planning/11`; U-03 direvisi |
| U-23 | Sumber video | **Rekaman saja sampai ada MoU**, setidaknya sampai T2 selesai, paling lambat setelah T3 selesai; **video publik (YouTube) bebas untuk uji dan pelatihan**, risikonya dicatat | `08` R-16; `13` bagian 0 |
| U-24 | Data latih dan tempat pelatihan | **Pra-label otomatis + koreksi manusia** dengan panduan langkah demi langkah yang hemat waktu; GPU gratis Kaggle (utama) dan Colab (cadangan); data Dishub tetap di laptop | `docs/planning/16` |
| U-25 | Lisensi model | **Model berlisensi bebas (Apache-2.0/MIT)**; Ultralytics YOLO (AGPL) tidak dipakai | ADR-19, ADR-25 |
| U-26 | Fitur T2 lama dan model T2 | Pemantauan dan laporan pindah ke T3; kendali ke T4; **T2 = perangkat lunak untuk engineer Dishub, awalnya diserahkan sebagai jasa kajian** | `docs/planning/03` bagian 7 |
| U-27 | Naskah tugas akhir di `docs/sources/` | **Tidak ada yang dipush** (PDF, teks, maupun ringkasannya tetap lokal) | `.gitignore`; dokumen planning merujuk secara umum |
| U-28 | Rekaman T2 | **Sampel terbatas satu simpang pada waktu puncak dan non-puncak, dengan kondisi pagi, malam, dan hujan**; kondisi boleh dari simpang berbeda sesuai ketersediaan data | `docs/planning/13` |
| U-29 | Jadwal dan nama tahap | **Tanpa tanggal, berbasis capaian**; nama tahap: T1 Purwarupa Hitung dan Rekomendasi, T2 Vision Tracker dan Optimasi Simpang, T3 Deteksi Kejadian dan Pemantauan Operasional, T4 Kendali Adaptif Terpadu, T5 Platform Mobilitas Kota | `docs/planning/04` |
| DOC | Versi docx/PDF dokumen planning | **Hanya lokal, tidak dipush** (keputusan 2026-09-13); PDF untuk rekan dilindungi kata sandi, bertanda air, dan dibatasi masa berlakunya | `docs/planning/docx/` di `.gitignore` |

## C. Pertanyaan riset/data yang belum terjawab dari bahan
| ID | Pertanyaan | Cara menjawab |
|---|---|---|
| Q-01 | Protokol & spesifikasi controller yang dipakai di kota target (merek, RS-232/NTCIP, hi-res log?) | **DIPUTUSKAN:** survei Dishub + vendor dengan kuesioner `docs/planning/12` (bahasa awam, asumsi umum tidak ditanyakan, netral kota) |
| Q-02 | ~~Kode enumerasi hi-res Indiana (tabel resmi)~~ **SELESAI (T-11)**: `02_Panduan_Praktis_Standar/Purdue_Indiana_HiRes_Data_Logger_Enumerations.pdf`; dipakai di KB-06 §C | — |
| Q-03 | NTCIP 1202 v03 & 1211 (objek priority, hi-res, SPaT) | **DIPUTUSKAN, direvisi 2026-09-14:** unduh sebelum T3 bila gratis di ntcip.org; bila berbayar, pembelian ditunda ke T4 (nol pengadaan sampai T3); daftar di `docs/planning/11` |
| Q-04 | Metode di balik klaim "+20–30%" ITCS DKI; hasil uji coba 2023 | **DIPUTUSKAN: tidak dikejar**; pakai bukti internasional (NCHRP/FHWA) + hasil pilot sendiri (on/off) |
| Q-05 | Angka tundaan per pendekat Makassar & studi ATCS kota lain (tabel tidak terekstraksi) | **DIPUTUSKAN: prioritas rendah**, cukup sebagai konteks |
| Q-06 | Dataset lokasi ATCS Jakarta (data.jakarta.go.id) | **DIPUTUSKAN: diganti data kota pilot Bandung** (`docs/sources/08`, R07); kebutuhan data per tahap di `docs/planning/13` |
| Q-07 | ~~Perpol ETLE (8/2023, 2/2025)~~ **SELESAI (T-11)**; Pergub DKI turunan MRLL/ERP, PM 67/2021, Perdirjen tata cara waktu siklus **+ regulasi Jabar/Kota Bandung** | **DIPUTUSKAN: semua dikerjakan sekarang** → hasil di `docs/sources/_ringkasan/R07` (sesi 2026-09-13) |
| Q-08 | Ketersediaan & lisensi data probe GPS untuk evaluasi koridor | **DIPUTUSKAN: floating car sendiri + AVL bus kota (Trans Metro Bandung)**; ojol/navigasi setelah ada pembeli. Catatan 2026-09-14: baru relevan mulai T3–T4, karena T1–T2 berfokus satu simpang |
| Q-09 | Kebutuhan TKDN untuk perangkat lunak dalam e-katalog & cara sertifikasinya | **DIPUTUSKAN: lewat mitra vendor lokal dulu**; TKDN software sendiri setelah pembeli pertama |
| Q-10 | Rumus eksplisit platoon ratio & Link Pivot | **DIPUTUSKAN: unduh paper Purdue + rujuk kode ATSPM UDOT** (hasil unduhan di R07) |
| Q-11 | PKJI 2023 rumus Nq1 (5-15) tercetak "s" di dalam akar, padahal dimensi & MKJI/Dirjen 273 menunjukkan kapasitas C — keputusan implementasi sementara: pakai **C** (sesuai MKJI NQ1); **DIPUTUSKAN: pakai C**, uji ke contoh Dirjen 273/MKJI; konfirmasi erratum bila sempat | bandingkan `docs/sources/_teks_ekstraksi/PKJI_2023_*.txt` hlm. 5-15 dengan MKJI 1997 Bab 2; uji terhadap contoh Dirjen 273; cocokkan juga dengan nilai Nq1 di Formulir SA-V contoh PKJI 2023 Lampiran 12.5 (dibaca dari PDF), yang memakai EMP dan faktor PKJI sendiri |
| Q-12 | Lisensi bobot tiap varian RF-DETR yang akan dipakai | periksa berkas lisensi repositori dan halaman model sebelum dipakai; putuskan di ADR-19 bersama uji kecepatan |
| Q-13 | Sumber citra satelit tanpa biaya untuk wizard konfigurasi | bandingkan syarat layanan dan atribusi; cadangan berupa unggahan citra yang diskalakan manual (ADR-17) |
| Q-14 | Ketersediaan rekaman satu simpang lengkap semua lengan pada periode yang sama untuk T2 | rekaman sendiri serentak dari beberapa titik, video publik, atau rekaman Dishub setelah MoU (`docs/planning/13` D2.1) |
| Q-15 | Digitalisasi grafik PKJI 2023 (arus jenuh tipe O, faktor kelandaian, NqMAX) | digitalisasi manual dari berkas PDF lalu uji terhadap contoh resmi PKJI 2023 Lampiran 12.5 (contoh 1 dan 2) dan contoh Dirjen 273 Bab X (tipe O); dicatat sebagai risiko T1 di `docs/planning/04` |

Pointer ke detail: `docs/sources/_ringkasan/R00 §K`, `R02 H`, `R04 F`, `R05 G`, `docs/planning/08`.
