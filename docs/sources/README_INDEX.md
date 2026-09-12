# Bahan Acuan — Indeks & Katalog Sumber
Proyek: Integrated/Intelligent Traffic Control System (ITCS) — acuan utama Majalah RPP "LANCAR-Jakarta" (Syafrin Liputo, Dishub DKI, PKN II 2025).
Disusun: 2026-09-12. Semua file diunduh langsung dari sumber; teks PDF diekstrak ke `docs/sources/_teks_ekstraksi/`; catatan studi di `docs/sources/_ringkasan/`; basis pengetahuan ringkas untuk resume sesi di `docs/kb/` (mulai dari `00_START_HERE.md`).

## Cara membaca folder ini
| Folder | Isi | Mulai dari |
|---|---|---|
| `05_Website_Acuan_Majalah_RPP/` | 22 halaman majalah (webp asli + png), JSON dekode FlipHTML5, **ANALISIS_MAJALAH_RPP_LANCAR-JAKARTA.md** | Analisis ini = definisi kebutuhan bisnis |
| `docs/sources/_ringkasan/` | **R00** catatan studi utama (dibaca langsung); R01–R06 catatan studi terstruktur per tema (sub-agen, diverifikasi) | R00 → R05 (regulasi) → R01/R02 (manual) → R04 (algoritma) → R03 (tooling) → R06 (TSP/EVP/konteks) |
| `01_Regulasi_Indonesia/` | UU, PP, Permenhub, Perda/Pergub DKI, Perpres RITJ, PKJI 2023, MKJI 1997, pedoman Dirjen, LAN | R05 + R00 bagian B–H |
| `02_Panduan_Praktis_Standar/` | NCHRP/FHWA/NTCIP/ATSPM/TSP/EVP/Detector handbooks | R01, R02, R03, R06 |
| `03_Jurnal_Akademis/` | arXiv & jurnal (RL, max-pressure, digital twin, green wave, ATCS Indonesia) | R04 |
| `04_Konteks_Jakarta_ITCS/` | arsip berita & halaman web (teks .md) | R06 bagian D |
| `06_Simulasi_Tools_OpenSource/` | dokumentasi SUMO (traffic lights, NEMA, TraCI), paper RL-SUMO | R03 bagian B |
| `docs/sources/_teks_ekstraksi/` | hasil `pdftotext -layout` seluruh PDF | untuk grep/verifikasi |
| `07_Konteks_Kota_Target/` | 38 arsip teks berita/halaman web kota target (Bandung, Medan, Palembang, Surabaya, Bodetabek, dll.) + 1 jurnal UNESA + `_urls.tsv` | `docs/kb/09` |
| `docs/kb/00–11` | **basis pengetahuan ringkas untuk resume sesi**: START_HERE, glosarium, lembar rumus, peta regulasi (C-01…C-43), katalog kebutuhan (KB-REQ), kartu algoritma (K-01…K-14), model data & antarmuka, KPI & monev, pelajaran & risiko, konteks kota, keputusan & pertanyaan terbuka, kartu sumber | `00_START_HERE.md` |

## 01 — Regulasi Indonesia
| File | Sumber | Status/keterangan |
|---|---|---|
| UU_22_2009_Lalu_Lintas_Angkutan_Jalan.pdf (203 hal) | pelayanan.jakarta.go.id | OK |
| PP_32_2011_Manajemen_Rekayasa_Andalalin_MKLL.pdf (58) | peraturan.bpk.go.id/Download/35525 | OK (bphn.go.id 403 → BPK) |
| PP_37_2011_Forum_LLAJ.pdf | luk.staff.ugm.ac.id | OK |
| PP_79_2013_Jaringan_LLAJ.pdf | peraturan.bpk.go.id/Download/33768 | OK (dasar PM 49/2014) |
| Permenhub_PM_49_2014_Alat_Pemberi_Isyarat_Lalu_Lintas.pdf (27) | peraturan.bpk.go.id/Download/94452 | OK — dibaca penuh (R00 B) |
| Permenhub_PM_96_2015_Manajemen_Rekayasa_Lalu_Lintas.pdf (45) | peraturan.bpk.go.id/Download/270482 | OK — bagian kunci dibaca (R00 E) |
| Permenhub_PM_76_2021_Sistem_Manajemen_Transportasi_Cerdas_LLAJ.pdf (17) | peraturan.bpk.go.id/Download/343822 | OK — dibaca penuh (R00 C). Link Dishub Sumut 404; JDIH Kemenhub hanya abstrak |
| Perda_DKI_5_2014_Transportasi.pdf (102) | peraturan.bpk.go.id/Download/62815 | OK |
| Pergub_DKI_68_2021_Sistem_Transportasi_Terpadu_Terintegrasi.pdf (16) | jdih.jakarta.go.id | OK — file pertama rusak, unduh ulang dengan Referer (R00 D) |
| Pergub_DKI_88_2019 & 76_2020 (ganjil-genap) | peraturan.bpk.go.id/Download/233056, /156074 | OK |
| Perpres_55_2018_Rencana_Induk_Transportasi_Jabodetabek.pdf (100) | peraturan.bpk.go.id/Download/79024 | OK (OCR lampiran sebagian buruk) |
| Draf_Raperda_Rencana_Induk_Transportasi_Jakarta.pdf (71) | dprd-dkijakartaprov.go.id | OK tetapi **hasil scan tanpa teks** — hanya bisa dibaca visual |
| PKJI_2023_Pedoman_Kapasitas_Jalan_Indonesia_09-P-BM-2023.pdf (351) | binamarga.pu.go.id | OK — Bab 5 Simpang APILL dirangkum di R05 D |
| MKJI 1997.pdf (564) | disediakan user | OK — pembanding PKJI |
| Pedoman_Teknis_Pengaturan_Lalu_Lintas_Persimpangan_Berdiri_Sendiri_APILL.pdf (Kep. Dirjen 273/1996) | kuliahtransportasi.wordpress.com | OK — dibaca penuh (R00 G) |
| Perdirjen_Hubdat_SK7234_2013_Juknis_Perlengkapan_Jalan.pdf (145) | keselamatanjalan.wordpress.com | OK — Bab II APILL dibaca (R00 H) |
| UU_27_2022_Pelindungan_Data_Pribadi.pdf | peraturan.bpk.go.id / hukumonline | OK (file jdih.semarang ternyata artikel, diganti) |
| Perpol_8_2023_Penyelenggaraan_Lalu_Lintas_Berbasis_Sistem_Elektronik.pdf | peraturan.bpk.go.id (Download) | OK — Ps.13–24 dibaca (integrasi sistem Polri–pemda via API, evaluasi tahunan); KB-03 §A.11b |
| Perpol_2_2025_Penindakan_Pelanggaran_Berbasis_Bukti_Rekaman_Elektronik.pdf | peraturan.bpk.go.id (Download) | OK — dibaca; kamera non-ETLE = "perangkat elektronik lainnya" wajib verifikasi Polri; alur tilang Ps.8–14; KB-03 §A.11b, C-42 |
| KepKa_LAN_1_2023_Pedoman_Pelatihan_Struktural_Kepemimpinan.pdf (130) | pusdikmin.com | OK |
| raw_*.html | halaman detail BPK/JDIH | bukti sumber |

## 02 — Panduan Praktis & Standar
| File | Sumber | Catatan |
|---|---|---|
| NCHRP_812_Signal_Timing_Manual_2nd_Ed_2015.pdf (317) | transops.s3.amazonaws.com (onlinepubs.trb.org redirect HTML) | R01 |
| FHWA_HOP-08-024_Traffic_Signal_Timing_Manual_2008.pdf (274) | ops.fhwa.dot.gov | R01 (rumus eksplisit) |
| Purdue_Indiana_HiRes_Data_Logger_Enumerations.pdf (+ salinan CFL) | docs.lib.purdue.edu (jtrpdata/3) | OK — tabel resmi kode event hi-res ATSPM; memverifikasi R03 §C.2; dirangkum di `docs/kb/06` §C |
| NCDOT_Signal_System_Timing_Philosophy_Manual.pdf (61) | connect.ncdot.gov | R01 |
| FHWA_HOP-11-027_Model_Systems_Engineering_Documents_ASCT.pdf (276) | ops.fhwa.dot.gov | R02 (ConOps/requirements template) |
| NCHRP_20-07_Task414_Benefits_of_Adaptive_Traffic_Control.pdf (165) | onlinepubs.trb.org | R02 |
| NYSERDA_2016_Decision_Tool_Adaptive_Traffic_Control_Systems.pdf (76) | nyserda.ny.gov | R02 |
| FHWA_EDC1_Adaptive_Signal_Control_Technology_Brochure.pdf | fhwa.dot.gov | R02 |
| FHWA_HOP-23-041_Traffic_Signal_Program_Handbook_2023.pdf (276) | ops.fhwa.dot.gov | R02 |
| FHWA_HOP-06-006_Traffic_Control_Systems_Handbook_2005.pdf (369) | ops.fhwa.dot.gov | referensi arsitektur sistem (belum dirangkum) |
| FHWA_HRT-06-108 / 06-139 Traffic Detector Handbook Vol I–II | fhwa.dot.gov | referensi deteksi (belum dirangkum) |
| NTCIP_1202_v02.19_Actuated_Signal_Controller_Objects.pdf (188) | ntcip.org (curl 403 → **Playwright**) | R03 |
| ARC-IT_NTCIP_1202_Standard_Page.html/.md | arc-it.net | R03 |
| FHWA_HOP-20-002_Automated_Traffic_Signal_Performance_Measures_2020.pdf (64) | ops.fhwa.dot.gov | R03 |
| NCDOT_Guide_on_ATSPM.pdf (54) | connect.ncdot.gov | R03 |
| FHWA_EDC4_ATSPM_Factsheet.pdf | ops.fhwa.dot.gov | R03 |
| USDOT_Transit_Signal_Priority_Planning_Implementation_Handbook_2005.pdf (212) | nacto.org | R06 |
| FHWA_HOP-24-019_Emergency_Vehicle_Preemption.pdf | ops.fhwa.dot.gov | R06 |
| CED_HCM_6th_Edition_Overview.pdf (43) | cedengineering.com | R06 (rumus control delay tidak ada di overview) |
| LAN_Modul_Proyek_Perubahan_PKN_II.pdf (62) | pusdikmin.com | R05 F |

## 03 — Jurnal & paper akademis (semua dirangkum di R04 kecuali dicatat)
arXiv: 2211.14426 (critical review RL/MPC), 2206.11996 (RL to reality), 2510.05374 (digital twin intersections), 2202.03290 (D-MP), 2210.10453 (cyclic MP + perimeter control), 2406.19269 (OCC-MP), 2511.00309 (Transit-MP), 2507.22511 (green wave survey), 2411.19359 (TSP-MARL), 1901.00960, 2302.03669, 2007.03433, 2406.02126 (CityLight), 2409.13388, 2412.16225, 2603.15283, 2604.27753, 2109.03210 (EVP mixed-criticality), 2212.02315 (CV arterial), 1909.00395 (sumolights — R03), 2308.14295 (RL-SUMO — R03), 2308.01952 (taxonomy ATSC — R00 I), 1904.08117 (Wei survey — belum dirangkum), Qadri 2020 ETRR (belum dirangkum).
Indonesia: UMSIDA evaluasi ATCS Makassar (ID/EN), Papatung 2019, Pubmedia 2025, Unhas skripsi ATCS, JMIA 2024 (abstrak), ITG Konstruksi Garut (abstrak) — R06 E. PMC11435829 digital twin O&M review — R04 A.20.

## 04 — Konteks Jakarta (arsip teks berita)
BeritaJakarta 145625 & 145079; ANTARA 5050989, 5051249, 5051493, 5014217, 3635259; CNN Indonesia; MetroTV; Kompas.id; TransportasiMedia; Jakarta Globe; Expat Indonesia; Medcom; Tempo (TKDN Solo); TKDN ×2 (konten tidak terambil); TomTom (teks umum); Dishub Semarang ATCS "Tentang". Kronologi & sintesis: R06 D.

## 06 — Simulasi & tools
SUMO docs: Traffic Lights, NEMA Phases, TraCI4Traffic Lights (html + md); arXiv 2308.14295. Rangkuman & rancangan digital twin: R03 B, D.

## 07 — Konteks kota target (arsip teks, riset pra-perencanaan)
38 arsip teks (`Teks_*.md`) + 1 jurnal UNESA + `_urls.tsv` (URL, tanggal, status unduhan) tentang urgensi kemacetan, status ATCS, anggaran, vendor & pengadaan di Bandung, Bandung Barat, Medan, Palembang, Surabaya, Bekasi, Tangerang, Depok, Bogor, Badung, Batam, Bukittinggi, dll. Gagal: data.bandung.go.id/atcs (500), jdih.lkpp Perpres 46/2025 (timeout), pasjabar (404). Rangkuman: `docs/kb/09_Konteks_Jakarta_dan_Kota_Target.md`, `08_Pelajaran_Lapangan_dan_Risiko.md`; pasar & pengadaan: `docs/planning/03`.

## Sumber yang TIDAK bisa diunduh dan workaround
| Sumber | Masalah | Workaround/substitusi |
|---|---|---|
| FlipHTML5 PDF asli majalah | download dimatikan penerbit | Playwright dekode config → 22 gambar halaman + analisis teks |
| FHWA-SA-13-027 Signalized Intersections Guide | 403 Akamai (curl & Playwright) | NCHRP 812 + FHWA STM 2008 mencakup materi |
| ROSAP (FHWA RT Eval ASC; FHWA-NJ TSP) | 403 | NCHRP T414; USDOT TSP Handbook |
| NCHRP Synthesis 403 (Stevanovic 2010) | hanya via NAP (login) | T414 (penulis sama, 2019) + NYSERDA |
| Hindawi/Wiley Wang 2018; UMJ Konstruksia; Academia (Papageorgiou 2003); ResearchGate (Varaiya 2013; ATCS Jakarta IEEE 2022) | 403/paywall | arXiv 2211.14426, 2308.01952, 1904.08117, Qadri 2020; varian MP yang merangkum Varaiya |
| media.neliti.com; unesp HCM2000 ch.16 | HTML/DNS | PKJI/MKJI; CED HCM overview |
| makassar.lan.go.id PerLAN 2/2019 | DNS | KepKa LAN 1/2023 + Modul PKN II |
| data.jakarta.go.id / katalog.data.go.id (dataset lokasi ATCS) | koneksi timeout | dicoba ulang; sementara peta simpang dari majalah hal. 16 |
| tile.loc.gov "Tinjauan ATCS" | PDF rusak | JMIA/Unhas |
| cvmatrik Perdirjen Juknis APILL | 404 | SK.7234/2013 memuat spesifikasi yang sama |
