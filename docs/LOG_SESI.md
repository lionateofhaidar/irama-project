# LOG SESI — Integrated Traffic Control System (ITCS)

> File ini adalah log tunggal sesi kerja. Diperbarui setiap kali ada task yang dijalankan.
> Format waktu: WIB (Asia/Jakarta). Tanggal sesi: 2026-09-12.
> Lokasi proyek: `Hydem Custodia & Co/Integrated Traffic Control System/`

---

## 0. Tujuan Sesi (mandat dari user)

1. Mempelajari secara rinci, teliti, dan mendalam website acuan:
   `https://fliphtml5.com/vuikw/bavj/Majalah_RPP-Syafrin_Liputo/`
2. Mengumpulkan bahan bacaan relevan (akademis + praktis) yang direkomendasikan ke folder `docs/sources/`.
   Jika ada yang tidak bisa diunduh → cari workaround.
3. Membaca dan mempelajari semua materi tersebut secara teliti dan mendalam.
4. Selalu membuat dan memperbarui log sesi ini (satu file yang sama, format .md) selengkap dan serinci mungkin.
5. Setelah itu (tahap berikutnya): perencanaan dan pembuatan aplikasi seperti yang digambarkan di website acuan.

---

## 1. Kronologi Task

### [T-01] Inisialisasi dan pemuatan tool — 17:25 WIB
- Memuat tool `WebFetch` dan `WebSearch`.
- Memeriksa direktori kerja: folder `docs/sources/` sudah ada dan berisi satu file dari user: `MKJI 1997.pdf` (Manual Kapasitas Jalan Indonesia 1997, 564 halaman). Repo git ada di level induk (`Hydem Custodia & Co`), folder ITCS masih untracked.
- Tool lokal yang terverifikasi tersedia: `curl`, `python 3.12` (pypdf, pdfplumber, bs4, Pillow, **playwright**), `node 24`, `pdftotext` (poppler).

### [T-02] Studi website acuan (FlipHTML5) — 17:30–18:05 WIB
**Metode dan workaround (berurutan):**
1. `WebFetch` langsung ke URL → **HTTP 403** (diblokir Cloudflare untuk fetcher otomatis).
2. **Workaround 1:** `curl` dengan User-Agent browser → berhasil mengambil HTML landing page (176 KB) dan `javascript/config.js` (50,9 KB). Namun konfigurasi buku **terenkripsi** (prefix `v010001...`), termasuk indeks teks halaman (`fliphtml5_pages`) sehingga nama file gambar halaman tidak terbaca.
3. Mengambil `files/shot.jpg` (sampul 339×480 px) → berhasil, dibaca visual.
4. Mencoba pola lama `files/large/N.jpg` / `files/mobile/N.jpg` → mengembalikan HTML "FlipHtml5 Online Service Error" (redirect `/check/`). Nama file halaman ternyata **ter-hash** (mis. `files/large/afc10927….webp`).
5. **Workaround 2 (berhasil):** menjalankan **Playwright (Chromium headless)** ke `online.fliphtml5.com/vuikw/bavj/`, membiarkan JavaScript FlipHTML5 mendekripsi konfigurasi, lalu membaca `window.bookConfig` dan `window.fliphtml5_pages` → diperoleh daftar 22 URL webp ter-hash. Skrip: `scratchpad/flip_decode.py`.
6. Mengunduh 22 halaman (`.webp` 1980×2800 px) dengan `curl` + cookie jar + Referer, lalu konversi ke PNG 1400×1980 (Pillow) untuk dibaca. Diagram arsitektur di hal. 9 di-crop dan diperbesar 2× agar label terbaca.
7. Fitur "Download PDF" dinonaktifkan penerbit (`basic-btn-disable`), sehingga tidak ada PDF asli; arsip halaman gambar adalah pengganti terbaik.

**Hasil tersimpan di** `docs/sources/05_Website_Acuan_Majalah_RPP/`:
- `halaman_webp/hal_01..22.webp` (asli), `halaman_png/hal_01..22.png` (+2 crop diagram), `sampul_shot.jpg`
- `fliphtml5_bookConfig_decoded.json`, `fliphtml5_pages_decoded.json` (bukti dekode)
- `ANALISIS_MAJALAH_RPP_LANCAR-JAKARTA.md` — analisis mendalam 22 halaman (identitas, struktur, isi per bab, arsitektur, milestone, stakeholder, konteks berita, implikasi desain aplikasi).

**Temuan metadata:**
| Atribut | Nilai |
|---|---|
| Judul buku | Majalah RPP-Syafrin Liputo |
| Book ID / akun | 99018545 / `syafrin.liputo` (`vuikw/bavj`) |
| Tanggal publikasi | 2025-07-02 |
| Jumlah halaman | 22 (A4 portrait, 595×841 pt) |
| Download PDF | dinonaktifkan penerbit |

**Ringkasan isi (detail di file analisis):**
- Dokumen = **Rancangan Proyek Perubahan PKN Tk. II Angk. VII 2025** Kadishub DKI **Syafrin Liputo**: *Strategi Mengatasi Kemacetan Lalu Lintas Melalui Pengembangan **Intelligent Traffic Control System (ITCS)** di Provinsi DKI Jakarta*, branding **#LANCAR-Jakarta**.
- Masalah inti: pengaturan simpang statis/belum adaptif; 321 simpang prioritas, baru 65 ber-ITCS.
- Solusi: ITCS berbasis AI (recognition dan predictive modelling; actuated, self-adaptive, green wave, bus/emergency priority) + **integrasi data** (Polda/ETLE, Bapenda/pajak, DLH/uji emisi, pengelola tol) → KRE dan PL2SE/ERP.
- Milestone: 2 bulan (MoU, kontrak 25 simpang, operasi 5) → 6–12 bulan (20 simpang, kontrak 40, ETLE mulai) → 12–24 bulan (191 simpang, integrasi KRE dan PL2SE). Anggaran Rp 120 M APBD 2025.
- Arsitektur eksisting per simpang: 4 kamera Viero + 1 fisheye + 4 ANPR → junction controller box (PoE/industrial switch, Viero AI processor, RS232 ke APILL controller) → Metro-E/fiber → TMC (server traffic, analytic, VMS, storage; video wall).
- Bab manajerial: visi-misi, peta stakeholder (4 kuadran), sumber daya (mentor Wagub, coach, tim efektif), marketing 4P+1C, kompetensi matriks mampu/mau.

### [T-03] Pembuatan log sesi — 17:53 WIB
- File `LOG_SESI.md` dibuat di root folder proyek; diperbarui setiap task.

### [T-04] Riset dan pengumpulan bahan bacaan — 17:55–18:20 WIB
**Metode:** 12+ `WebSearch` bertema (regulasi Indonesia, manual FHWA/NCHRP, standar NTCIP/ARC-IT, jurnal ATCS Indonesia, survei RL/max-pressure/digital twin, TSP/EVP/ATSPM, konteks berita Jakarta ITCS, LAN/PKN II). Unduhan paralel dengan `curl` (UA browser, referer) dari daftar URL; verifikasi tipe file dengan `file`; file gagal (HTML/0 byte) dihapus.

**Struktur folder `docs/sources/`:**
```
01_Regulasi_Indonesia/           UU, PP, Permenhub, Perda/Pergub DKI, Perpres RITJ, PKJI 2023, LAN
02_Panduan_Praktis_Standar/      NCHRP 812, FHWA STM 2008, ASCT SE docs, NTCIP 1202, ATSPM, TSP, EVP, dll.
03_Jurnal_Akademis/              arXiv (RL, max-pressure, digital twin, green wave, TSP), jurnal Indonesia
04_Konteks_Jakarta_ITCS/         arsip teks berita (BeritaJakarta, ANTARA, CNN, Kompas, dll.), TomTom
05_Website_Acuan_Majalah_RPP/    22 halaman majalah + JSON dekode + analisis
06_Simulasi_Tools_OpenSource/    SUMO docs (traffic lights, NEMA, TraCI), paper RL-SUMO
_teks_ekstraksi/                 hasil pdftotext semua PDF (untuk dipelajari/grep)
MKJI 1997.pdf                    (dari user)
```

**Berhasil diunduh (PDF valid):**
- Regulasi: UU 22/2009 LLAJ (203 hal); PP 32/2011 MRLL-Andalalin-MKLL (58); Permenhub PM 49/2014 APILL (27); Permenhub PM 96/2015 Pedoman MRLL (45); Perda DKI 5/2014 Transportasi (102); Perpres 55/2018 RITJ Jabodetabek (100); Draf Raperda Rencana Induk Transportasi Jakarta (71, **hasil scan tanpa teks**); PKJI 2023 (09/P/BM/2023, 351 hal); KepKa LAN 1/2023 Pedoman Pelatihan Struktural Kepemimpinan (130); Modul Proyek Perubahan PKN II (62).
- Panduan praktis: NCHRP Report 812 Signal Timing Manual 2nd ed. (317); FHWA HOP-08-024 Traffic Signal Timing Manual 2008 (274); FHWA HOP-11-027 Model SE Documents for ASCT (276); NCHRP 20-07 Task 414 Benefits of Adaptive Traffic Control (165); NYSERDA 2016 Decision Tool ATCS (76); FHWA EDC-1 ASCT brochure; FHWA HOP-23-041 Traffic Signal Program Handbook 2023 (276); FHWA HOP-20-002 ATSPM (64); NCDOT ATSPM Guide (54); NCDOT Signal System Timing Philosophy Manual (61); FHWA EDC-4 ATSPM factsheet; FHWA HOP-24-019 EVP; USDOT Transit Signal Priority Handbook 2005 (212); NTCIP 1202 v02.19 (188, via Playwright); HCM 6th Ed. overview (CED, 43); ARC-IT NTCIP 1202 page.
- Jurnal/akademis: 19 paper arXiv (kritik RL/MPC 2211.14426; RL-to-reality 2206.11996; digital twin intersections 2510.05374; max-pressure 2202.03290, 2210.10453, 2406.19269, 2511.00309; green wave survey 2507.22511; TSP-MARL 2411.19359; DRL TSC 1901.00960, 2302.03669, 2007.03433, 2406.02126 CityLight, 2409.13388, 2412.16225, 2603.15283; agentic digital twin 2604.27753; EV routing 2109.03210; CV arterial 2212.02315; sumolights 1909.00395; RL-SUMO 2308.14295); jurnal Indonesia (UMSIDA evaluasi ATCS Makassar ID/EN; Papatung 2019 kebijakan transportasi Jakarta; Pubmedia smart city Jakarta); PMC digital twin O&M review (HTML→md); halaman abstrak JMIA dan ITG Konstruksi.
- Konteks Jakarta: 11 artikel (BeritaJakarta ×2, ANTARA ×4, CNN, MetroTV, Kompas.id, TransportasiMedia, Katadata) + 8 halaman tambahan (TomTom, Jakarta Globe, Expat Indonesia, Medcom, Tempo, TKDN ×2, ANTARA 2023) diarsipkan sebagai `.md`.
- Simulasi: SUMO docs (Traffic Lights, NEMA phases, TraCI tutorial).

**Tidak bisa diunduh dan workaround-nya:**
| Sumber | Masalah | Workaround / status |
|---|---|---|
| `highways.dot.gov` FHWA-SA-13-027 Signalized Intersections Guide | 403 (Akamai) bahkan via Playwright | Dicari mirror lain; jika gagal, substitusi dengan NCHRP 812 dan FHWA STM 2008 yang mencakup materi sama |
| `rosap.ntl.bts.gov` (FHWA RT Eval ASC; FHWA-NJ TSP) | 403 | Substitusi: NCHRP 20-07 T414 (benefit ASCT) dan USDOT TSP Handbook |
| `bphn.go.id` PP 32/2011 | 403 | Berhasil dari `peraturan.bpk.go.id/Download/35525` |
| Hindawi/Wiley Wang 2018 review | 403 Cloudflare | Substitusi: arXiv 2211.14426 (review komprehensif TSC) |
| `jurnal.umj.ac.id` ITS Konstruksia | 403 | Substitusi: UMSIDA dan JMIA abstrak |
| `media.neliti.com` | mengembalikan HTML | Substitusi: UMSIDA dan PKJI 2023 |
| `pessoas.feb.unesp.br` HCM2000 ch.16 | DNS gagal | Substitusi: CED HCM 6th overview + PKJI/MKJI |
| `makassar.lan.go.id` PerLAN 2/2019 | DNS gagal | Substitusi: KepKa LAN 1/2023 (pedoman terbaru) + Modul Proyek Perubahan |
| ResearchGate/Academia (Papageorgiou 2003; Varaiya 2013 max-pressure; ATCS Jakarta IEEE 2022) | perlu login/paywall | Substitusi: paper max-pressure turunan (arXiv) yang merangkum Varaiya; arsitektur ATCS Jakarta diambil dari diagram majalah + berita |
| `dishub.sumutprov.go.id` PM 76/2021 ITS | 404 | Sedang dicari sumber lain (JDIH Kemenhub / BPK) — **penting** karena disebut sebagai dasar hukum ITCS |
| Pergub DKI 68/2021 | file rusak (xref) | Diunduh ulang / dicek |
| arXiv 2503.09252 | 404 (ID keliru) | Dilewati |
| FlipHTML5 PDF asli | download dimatikan penerbit | Arsip 22 gambar halaman + analisis teks manual |

### [T-05] Ekstraksi teks dan persiapan studi — 18:20 WIB
- Semua PDF diekstrak ke `docs/sources/_teks_ekstraksi/*.txt` dengan `pdftotext -layout` (total ±12 MB teks; MKJI 1997 = 1,17 MB). Draf Raperda RIT Jakarta ternyata hasil scan (71 byte teks) → hanya bisa dibaca visual.
- Halaman HTML mentah dikonversi ke `Teks_*.md` (bs4).
- Duplikat Perda 5/2014 (jdih) dihapus.

### [T-06] Studi mendalam bahan bacaan — mulai 18:25 WIB
- Strategi: (1) saya membaca langsung dokumen inti (majalah 22 hal — selesai; regulasi APILL/MRLL/ITS; ringkasan tiap paper); (2) untuk manual tebal (>250 hal) dipakai sub-agen pembaca paralel yang menulis catatan studi terstruktur ke `docs/sources/_ringkasan/`, lalu saya baca dan verifikasi silang dengan teks asli.
- Status: berjalan (lihat pembaruan di bawah).

#### [T-06a] Pembaruan 18:40 WIB — regulasi tambahan dan studi mandiri
- **Permenhub PM 76/2021** (Sistem Manajemen Transportasi Cerdas di bidang LLAJ) — link Dishub Sumut 404; JDIH Kemenhub hanya memberi abstrak 1 halaman; **berhasil** dari `peraturan.bpk.go.id/Download/343822` (17 hal). Teks diekstrak (32 KB) dan **dibaca penuh**.
- **Pergub DKI 68/2021** file pertama rusak (xref) → diunduh ulang dari JDIH Jakarta dengan Referer → valid (10 hal + lampiran), dibaca penuh.
- **Permenhub PM 49/2014** (APILL) dibaca penuh.
- Enam sub-agen pembaca diluncurkan paralel (R01 manual signal timing; R02 ASCT systems engineering & benefit; R03 NTCIP/SUMO/ATSPM; R04 paper akademis; R05 regulasi Indonesia & PKJI; R06 TSP/EVP/HCM/konteks Jakarta) → output ke `docs/sources/_ringkasan/R0x_*.md`.
- Catatan studi mandiri saya ditulis di `docs/sources/_ringkasan/R00_Catatan_Studi_Utama.md` (bertambah seiring bacaan).

#### [T-04b] Pembaruan 19:05 WIB — batch unduhan ke-4 (bahan tambahan hasil riset lanjutan)
- Berhasil: FHWA HOP-06-006 *Traffic Control Systems Handbook* 2005 (261 hal); FHWA HRT-06-108/139 *Traffic Detector Handbook* Vol I & II; Perdirjen Hubdat SK.7234/AJ.401/DRJD/2013 *Petunjuk Teknis Perlengkapan Jalan* (memuat spesifikasi teknis APILL, perangkat kendali, detektor); Kep. Dirjen Hubdat 273/HK.105/DRJD/96 *Pedoman Teknis Pengaturan Lalu Lintas di Persimpangan Berdiri Sendiri dengan APILL* (metode perhitungan waktu siklus, kapasitas, unjuk kerja); arXiv 2308.01952 *A Taxonomy of Adaptive Traffic Signal Control*; skripsi Unhas implementasi ATCS (Bab 1–2); halaman "Tentang ATCS" Dishub Semarang.
- Gagal + workaround: `cvmatrik.com` Perdirjen Juknis APILL → 404 (materi yang sama ada di SK.7234/2013 yang berhasil diunduh); `data.jakarta.go.id` & `katalog.data.go.id` (dataset lokasi ATCS Jakarta) → koneksi timeout dari jaringan ini (akan dicoba ulang nanti / via Playwright; alternatif: peta simpang dari foto hal. 16 majalah); `tile.loc.gov` PDF rusak → dihapus; `portaldata.kemenhub.go.id` & TUMI datahub → timeout.
- Semua PDF baru diekstrak ke `docs/sources/_teks_ekstraksi/`.
- Studi mandiri: Pedoman Teknis 273/1996 (kriteria pemasangan APILL, definisi tahap/fase/siklus, nilai skr, waktu pengosongan/hilang, prosedur A–E) dan PM 96/2015 bagian LOS & pengendalian simpang — catatan di `docs/sources/_ringkasan/R00_Catatan_Studi_Utama.md`.

#### [T-06b] Pembaruan 19:30 WIB — studi mandiri lanjutan
- Dibaca penuh/mendalam oleh saya (bukan sub-agen): Kep. Dirjen Hubdat 273/1996 (seluruh metode: skr, waktu pengosongan, arus jenuh S0=600·We, faktor koreksi, c=(1,5·LT+5)/(1−IFR), g_i, C=S·g/c, DS, NQ, QL, p_SV, tundaan A_j/B_j, LOS); Perdirjen SK.7234/2013 Bab II APILL (spesifikasi controller ≥8+8 signal group, ≥4–16 program, 10 plan/hari, conflict monitor → flashing, manual override, detektor ≥4 zona gap/occupancy, DIS RS-485, interface ATCS); arXiv 2308.01952 Taxonomy of ATSC (generasi UTCS 0–3, COS, reactive/proactive, cyclic/acyclic; 88 metode).
- Catatan tertulis di `docs/sources/_ringkasan/R00_Catatan_Studi_Utama.md` bagian G–I.
- Bahan tambahan dari sitasi paper taksonomi: NCHRP Synthesis 403 *Adaptive Traffic Control Systems: Domestic and Foreign State of Practice* (Stevanovic 2010); Wei et al. 2019 *A Survey on Traffic Signal Control Methods* (arXiv 1904.08117); Qadri et al. 2020 ETRR review — diunduh (lihat hasil di bawah).

#### [T-06c] 19:45 WIB — Sub-agen R04 (paper akademis) selesai; dibaca & diverifikasi
- Output: `docs/sources/_ringkasan/R04_Paper_Akademis_TSC.md` (±8.600 kata; 20 sumber; per-paper: sitasi, masalah, formulasi, data, hasil kuantitatif, keterbatasan, skor relevansi; sintesis taksonomi; TSP/EVP; green wave & data probe; digital twin; rekomendasi bertingkat + 10 guard-rail; 22 kutipan).
- Saya membaca seluruh R04 dan melakukan verifikasi acak angka-angka kunci terhadap teks sumber (min green 7 s & rate-limit 5 s/cycle Tsitsokas; VHT −14,5%/−10,6%/−15,6%; OCC-MP +0,36–2,64% vs RB-MP 3,50–25,75%; "never been deployed" Chen et al.; EVP 96%/−36% Humagain) — hasil verifikasi dicatat di R00 bagian J.
- Temuan yang paling menentukan desain: (1) belum ada RL-TSC yang deployed → RL hanya advisor/shadow mode; (2) **cyclic Max-Pressure** (cycle/offset tetap, MP mengatur split, min green, rate-limit) + perimeter control adalah inti adaptif yang realistis; (3) MP parsial di 20–25% simpang kritis ≥ MP di semua simpang; (4) prioritas bus kondisional berbasis occupancy (OCC/Transit-MP) + EVP bertingkat; (5) data probe GPS cukup untuk evaluasi/penalaan green wave; (6) validasi SIL→HIL→shadow→phased live.

#### [T-06d] 20:05 WIB — Sub-agen R02 (ASCT systems engineering, manfaat, program sinyal) selesai; dibaca & diverifikasi
- Output: `docs/sources/_ringkasan/R02_ASCT_Systems_Engineering_Benefits.md` (±10.900 kata): peta isi 5 dokumen; proses SE (V-model, 10 langkah, checklist ConOps/Requirements/V&V); 18 kategori operational needs ConOps; kutipan requirement App. D per kategori (fallback, logging, priority/preemption, security, interface); desain evaluasi before-after vs on-off; MOE; angka manfaat & biaya T414/NYSERDA; faktor kegagalan; manajemen program TSPH (GcOST, CMF, staffing, maintenance KPI, procurement, NTCIP, NEMA TS 8); 34 requirement kandidat ITCS; arsitektur referensi; tabel risiko-mitigasi; 25 kutipan.
- Verifikasi acak terhadap teks sumber: biaya $55.534/$10.252/$3.814 (T414), alasan decommissioning, kutipan "vendor should never be tasked", Req 18.0-2, kutipan TSPH tentang komplain — semua ditemukan di sumber.
- Temuan yang menentukan desain: traceability need→requirement→verification; fallback TOD/free berbasis ambang detektor/komunikasi/processor adalah requirement inti; transparansi nilai perhitungan antara (anti black-box AI); manfaat lebih besar pada AADT moderat & side-street delay bisa naik; umur ASCT rata-rata 6–7 tahun karena isu institusional → SDM/maintenance/TSMP; skala 321 simpang harus bertahap per grup; procurement best-value, NTCIP wajib, NEMA TS 8.

#### [T-06e] 20:25 WIB — Sub-agen R01 (manual signal timing) selesai; dibaca & diverifikasi
- Output: `docs/sources/_ringkasan/R01_Signal_Timing_Manuals.md` (±11.100 kata, 128 rujukan halaman): peta isi NCHRP 812 / FHWA 2008 / NCDOT; terminologi NEMA ring-barrier, mode kendali, deteksi & decision zone, parameter fase dengan rumus (ITE yellow, red clearance, Gq, PCT, passage time, gap reduction), kapasitas/critical movement/Webster/HCM QEM, koordinasi (pattern, force-off, permissive, yield point, offset reference, transisi), TRPS (V+K·O), arsitektur ASCT & algoritma (SCOOT/SCATS/RHODES/OPAC/ACS-Lite), preemption/priority NTCIP 1211 (strategi, recovery, rail, TSP kondisional), cuaca/insiden/event, oversaturation toolkit, performance measures & high-resolution data/PCD, equipment monitoring (Exhibit 8-16), staffing; implikasi: 16 entitas data, parameter default, 14 algoritma/aturan, KPI, antarmuka TMC; 22 kutipan.
- Verifikasi acak kutipan (gap-out 3 syarat; "not set-and-forget"; ≥30 menit per pattern; SCOOT hold/force-off; Webster; B/C 40:1) terhadap teks sumber — cocok.
- Catatan kejujuran dari sub-agen: badan persamaan NCHRP 812 tidak terekstraksi pdftotext → dilengkapi dari FHWA 2008 dan ditandai [rekonstruksi]; istilah ATSPM/InSync tidak ada di ketiga dokumen.

#### [T-06f] 20:45 WIB — Sub-agen R06 (TSP, EVP, HCM, konteks Jakarta, ATCS Indonesia) selesai; dibaca & diverifikasi
- Output: `docs/sources/_ringkasan/R06_TSP_EVP_HCM_Konteks_Jakarta.md` (±8.900 kata): TSP Handbook (definisi priority vs preemption NTCIP 1211/1202, 4 komponen, tabel strategi & parameter, deteksi, arsitektur PRG/PRS, conditional priority TransLink/LADOT, dampak terukur, SE & evaluasi, checklist 14 poin); EVP (vehicle-based vs system-based/geofence, urutan preempt NTCIP, dampak); HCM 6th overview (travel speed LOS; rumus control delay TIDAK ada di overview — dinyatakan jujur) vs MKJI/PKJI/PM 96; kronologi Jakarta 2004–2025 dengan sumber; fitur ITCS Dishub; TMC; integrasi; vendor; kritik; regulasi; pengalaman ATCS Makassar/Garut/multi-kota; 18 fitur wajib, parameter default TSP/EVP, KPI publik/internal, matriks API, risiko; 22 kutipan; lampiran celah data.
- Verifikasi acak: kutipan "mysteriously diminish", TransLink "two or more minutes late"/4 level, EVP 25 s & −71%, HCM "average travel speed" — ditemukan di sumber.
- Catatan: Dataset lokasi ATCS Jakarta (data.jakarta.go.id) belum bisa diakses (timeout jaringan); NCHRP Synthesis 403 hanya tersedia via NAP (perlu login) → dilewati, materi setara ada di T414/NYSERDA.
- Status: menunggu R03 (NTCIP/SUMO/ATSPM) dan R05 (regulasi & PKJI).

#### [T-06g] 21:05 WIB — Sub-agen R05 (regulasi Indonesia, PKJI 2023, LAN) selesai; dibaca & diverifikasi
- Output: `docs/sources/_ringkasan/R05_Regulasi_Indonesia_PKJI.md` (±11.700 kata): kajian per regulasi dengan nomor pasal (UU 22/2009, PP 32/2011, PM 96/2015, PM 49/2014, Perda 5/2014, Pergub 68/2021, Perpres 55/2018); spesifikasi APILL; rumus PKJI 2023 Bab 5 lengkap (C, J, FUK Jakarta 1,05, wMS, wHH, Webster, wH, DJ, Nq, PA, RKH, TLL/TG/TI) + perbandingan MKJI 1997; indikator & target; struktur RPP PKN II (11 komponen, 5+6 aspek penilaian); 35 kebutuhan kepatuhan (C-01…C-35); 12 formula KPI; daftar larangan/risiko hukum; 37 kutipan; daftar tindak lanjut sumber.
- **Catatan penting:** sub-agen membaca PM 76/2021 saat file masih berupa abstrak 1 halaman (sebelum saya mengganti dengan teks lengkap dari BPK), sehingga R05 Bagian C menyatakan "tidak dapat dikaji". Celah ini **sudah tertutup** oleh catatan saya sendiri di `R00_Catatan_Studi_Utama.md` Bagian C (PM 76/2021 dibaca penuh, 25 pasal).
- Verifikasi acak terhadap teks sumber: UU Ps.247(3) "dikelola oleh Kepolisian", PP 32 Ps.79(3) "tidak dapat dilakukan pada jalan nasional", Perda Ps.8 (60% & 35 km/jam), PKJI "melebihi 130 detik", EMP SM 0,15, Webster (1,5·wHH+5) — cocok.
- Temuan yang menentukan desain: kewenangan terbelah Dishub (MRLL/perlengkapan) vs Polri (operasional MRLL, penegakan hukum, pusat kendali SIK LLAJ Ps.247) → ITCS = subsistem yang wajib terintegrasi ke pusat kendali Polri & menyediakan override petugas; ETLE: aplikasi hanya penyedia bukti, bukan penindak; simpang jalan nasional Jakarta perlu persetujuan Dirjen/BPTJ; LOS PM 96 wajib; ERP/ganjil-genap punya ambang legal V/C & kecepatan; data milik Pemprov, akses pihak ketiga perlu persetujuan Gubernur.
- Tindak lanjut sumber (dari R05): PP 79/2013, PP 37/2011, UU 27/2022 PDP, Pergub turunan (MRLL, ERP, ganjil-genap), Perpol ETLE, Perdirjen tata cara waktu siklus → dicari.

#### [T-06h] 21:20 WIB — Sub-agen R03 (NTCIP 1202, SUMO, ATSPM) selesai; dibaca & diverifikasi
- Output: `docs/sources/_ringkasan/R03_NTCIP_SUMO_ATSPM_Tooling.md` (±11.400 kata): peta MIB NTCIP 1202 v02 (phase/detector/unit/coord/timebase/preempt/ring/channel/overlap/block), objek kontrol C vs parameter P/P2 + transaksi & consistency check, pemetaan perintah TMC→objek, conformance groups; SUMO (tlLogic static/actuated/delay_based/NEMA, custom conditions, TraCI, WAUT, detektor E1/E2/E3, netconvert), sumolights (max-pressure terbaik) & Pan 2023; ATSPM (5 komponen, hi-res log 0,1 s, 14 metrik & cara hitung, kebutuhan detektor, watchdog, praktik agensi); rancangan referensi ITCS (skema data 20 entitas, Controller Abstraction Interface dengan adaptor NTCIP/RS-232/TraCI, pipeline ATSPM, daftar API internal, tabel keputusan desain); 30 kutipan; keterbatasan.
- Verifikasi acak: `unitBackupTime` "revert to Backup Mode"; tabel sumolights (59,21,54)/(158,169,85); split failure ≥80%; "1/10-second resolution" — cocok.
- Semua 6 sub-agen selesai; total catatan studi ±62.000 kata + R00 (catatan mandiri) — seluruhnya telah saya baca penuh dan diverifikasi acak terhadap teks sumber.

### [T-07] 21:30 WIB — Konsolidasi
- `docs/sources/README_INDEX.md` dibuat: katalog seluruh file per folder dengan sumber URL, status, keterangan, urutan baca, serta tabel sumber gagal + workaround/substitusi.
- `R00_Catatan_Studi_Utama.md` ditulis ulang lengkap: bagian A–I (bacaan mandiri), **J** (tabel verifikasi R01–R06), **K** (sintesis lintas-sumber 7 pilar: kepatuhan hukum, model data & antarmuka controller, mesin kendali bertingkat, guard-rail, KPI/monev, tata kelola/SDM, konteks-risiko Jakarta) — ini bahan masuk untuk tahap perencanaan aplikasi.
- Regulasi tambahan (tindak lanjut R05) diunduh & diekstrak: PP 79/2013 Jaringan LLAJ (BPK; Ps.42–43 APILL sejalan PM 49), PP 37/2011 Forum LLAJ (UGM), UU 27/2022 PDP (BPK Download/224884 — file pertama dari jdih.semarang ternyata artikel penjelasan, diganti), Pergub DKI 88/2019 & 76/2020 ganjil-genap (BPK) — ruas & jam ganjil-genap (Senin–Jumat 06.00–10.00 & 16.00–21.00; pengecualian ambulans, pemadam, angkutan umum plat kuning, kendaraan listrik, sepeda motor, dsb.).
- Belum diperoleh (dicatat sebagai tindak lanjut): Perpol ETLE (Perpol 8/2023 & 2/2025 disebut di pencarian, belum diunduh), Pergub DKI turunan MRLL/ERP, PM 67/2021 (organisasi Kemenhub), Perdirjen tata cara waktu siklus (PM 49 Ps.18), dataset lokasi ATCS Jakarta (portal timeout), NCHRP Synthesis 403 (NAP login).

## 2. Status Akhir Sesi (21:35 WIB) & Langkah Berikutnya
**Selesai:**
1. Website acuan dipelajari tuntas (22 halaman diunduh via workaround Playwright; analisis 14 KB).
2. Bahan bacaan terkumpul di `docs/sources/` (±300 MB; 20 regulasi/pedoman Indonesia, 21 manual/standar praktis, 30+ paper/jurnal, 19 arsip konteks Jakarta, dokumentasi SUMO), semua terindeks di `README_INDEX.md`; setiap sumber gagal punya workaround/substitusi tercatat.
3. Semua materi dipelajari: bacaan mandiri (R00 A–I) + 6 catatan studi terstruktur (R01–R06, ±62.000 kata) yang saya baca penuh dan verifikasi acak; sintesis 7 pilar di R00 K.
4. Log sesi ini diperbarui pada setiap task.

**Langkah berikutnya (tahap perencanaan aplikasi):**
- Susun ConOps ITCS (mengikuti template FHWA HOP-11-027 + struktur RPP LAN) berbasis R00 K.
- Turunkan System Requirements (gabungan kandidat R02 H.1 ITCS-*, R05 G.1 C-*, R06 F.1 F-*, R01 I).
- Tetapkan arsitektur (lapisan lapangan/komunikasi/pusat/integrasi/monev) & model data (R03 D.1 + R01 I.1), pilih stack teknologi, dan rencana digital twin SUMO NEMA + pipeline ATSPM.
- Rencana implementasi bertahap 5 → 25 → 65 → 321 simpang dengan verifikasi & validasi (on/off, before–after).

---

## 3. Mandat Lanjutan (21:40 WIB) — Pra-Perencanaan sampai titik "buat GitHub & planning rinci"
Instruksi user (ringkas): (a) dokumentasikan seluruh knowledge/insight dari materi dalam format yang murah dipelajari ulang di sesi lain; (b) jalankan semua task pra-perencanaan sampai user harus membuat GitHub dan planning rinci end-to-end; (c) aplikasi TIDAK harus sama persis dengan end-state ITCS DKI; pengembangan dibagi 4–5 tahap: T1 MVP, T2 siap jual (fitur realistis, server terbatas), T3 transisi, T4 setara/mendekati ITCS, T5 end-state rekomendasi; (d) kreativitas dihargai selama berbasis kebutuhan nyata lapangan; (e) perlu nama aplikasi yang engaging & compelling untuk dijual ke pemda selain DKI (Bandung, Medan, Palembang, Surabaya, kota-kota Bodetabek); (f) log sesi tetap diperbarui setiap task.

### [T-08] Rencana kerja pra-perencanaan
1. Riset konteks kota target (urgensi kemacetan, status ATCS, anggaran) & lanskap vendor/pengadaan ATCS Indonesia → arsip ke `docs/sources/04_Konteks_Jakarta_ITCS/` dan `07_Konteks_Kota_Target/`.
2. Basis pengetahuan ringkas `docs/kb/` (START_HERE, glosarium, lembar rumus, peta regulasi, katalog kebutuhan, kartu algoritma, model data, KPI, pelajaran & risiko, konteks kota, kartu sumber, keputusan & pertanyaan terbuka).
3. Dokumen pra-perencanaan `docs/planning/` (visi & positioning, kandidat nama, pasar & kota target, konsep 5 tahap, inventaris fitur per tahap, arsitektur konseptual & opsi teknologi, persona & stakeholder, asumsi-risiko-pertanyaan, brief planning rinci, checklist pra-GitHub).
4. Log diperbarui per task.

### [T-09] 21:50 WIB — Riset kota target & peluncuran pekerja paralel
- Riset awal (WebSearch): TomTom Traffic Index 2024 — Bandung #12 dunia (10 km = 32 mnt 37 dtk), Medan #15, urutan Indonesia: Bandung > Medan > Surabaya > Palembang > Jakarta (#90). Status ATCS: Bandung (ruang kendali Balai Kota, CCTV publik), Medan (ATCS Dishub, ITS), Palembang (15 simpang terkoneksi), Surabaya (SITS, >90 CCTV), Bekasi (ruang ATCS 2023, 120 CCTV), rapat sinkronisasi ATCS Jabodetabek (2022); hibah Kemenhub ATCS (contoh Bukittinggi Rp9,3 M). Vendor lokal: PT Javis Teknologi Albarokah (ATMS, VID AI, APILL otonom, bus priority; TKDN/SNI), PT Qumicon (ATCS), PT TKDN (Jakarta); produk controller ATCS ada di e-katalog LKPP.
- Lima fork paralel diluncurkan: KB-A (glosarium, lembar rumus, peta regulasi), KB-B (katalog kebutuhan KB-REQ, kartu algoritma, model data & antarmuka, KPI & monev), KB-C (riset kota target → `07_Konteks_Kota_Target/`, pelajaran & risiko, konteks kota, kartu sumber), PP-A (pasar & pengadaan, persona, asumsi-risiko-pertanyaan), PP-B (konsep 5 tahap, inventaris fitur per tahap, arsitektur & opsi teknologi).
- Saya mengerjakan sendiri: visi & positioning, kandidat nama, START_HERE (panduan resume sesi), log keputusan & pertanyaan terbuka, brief planning rinci, checklist pra-GitHub.

### [T-10] 22:05 WIB — Dokumen yang saya tulis sendiri (sambil menunggu fork)
- `docs/planning/01_Visi_Produk_dan_Positioning.md` — masalah nyata lapangan (8, dengan bukti), visi, 7 nilai inti, positioning statement, tabel "berbeda dari ITCS DKI", ringkasan T1–T5, prinsip kreatif-berpijak (3 uji), ukuran sukses program.
- `docs/planning/02_Kandidat_Nama_dan_Branding.md` — 6 kriteria; 7 kandidat (IRAMA, NADI, ARUS, LAJU, GEHIJAU, PANDU LINTAS, SIMPANG) dengan makna/akronim/tagline/risiko; rekomendasi **IRAMA** (sub-merek Pantau/Atur/Ukur/Prioritas/Twin), cadangan NADI; elemen branding awal; tindakan cek merek PDKI/domain. Pencarian web awal tidak menemukan produk lalu lintas bernama IRAMA/NADI (pemeriksaan resmi tetap wajib); "Serasi" dihindari (Serasi Autoraya).
- `docs/planning/09_Brief_Planning_Rinci.md` — masukan tersedia & lokasinya, 7 keputusan awal user, 9 keluaran planning, urutan kerja sesi planning, batas lingkup.
- `docs/planning/10_Checklist_Pra-GitHub.md` — keputusan final, struktur monorepo usulan, fondasi rekayasa hari pertama (ADR, CI sim-smoke, templates, security), data/aset pra-sprint, kesepakatan mitra pilot.
- `docs/kb/10_Keputusan_dan_Pertanyaan_Terbuka.md` — 20 keputusan tersirat dari bahan (D-01…D-20), 8 keputusan milik user dengan default (U-01…U-08), 10 pertanyaan riset (Q-01…Q-10).

### [T-11] 22:20 WIB — Sumber tambahan & fork PP-A selesai
- Diunduh & diekstrak: **Purdue "Indiana Traffic Signal Hi Resolution Data Logger Enumerations" (2012)** + salinan CFL (kode event ATSPM resmi; kode yang dipakai di R03 §C.2 terverifikasi cocok: 0/1/4/5/6/8/10/21/22/45/81/82/105/131) → `02_Panduan_Praktis_Standar/`; **Perpol 8/2023** (Penyelenggaraan Lalu Lintas Berbasis Sistem Elektronik) & **Perpol 2/2025** (Penindakan Pelanggaran LLAJ Berdasarkan Alat Bukti Rekaman Elektronik) dari BPK → `01_Regulasi_Indonesia/`. Menutup pertanyaan Q-02 dan sebagian Q-07.
- Dibaca (saya): Perpol 8/2023 Ps.13–24 — tahapan data & **integrasi sistem Polri–pemda via API** (analisis kebutuhan, penilaian arsitektur, standar & protokol keamanan, uji coba, validasi, audit tahunan, pemeliharaan), kantor pengolah & operasional (pusat komunikasi/koordinasi/kendali/informasi), operator. Perpol 2/2025 — bukti dari ETLE statis/portabel/mobile terintegrasi **Back Office ETLE Polri**; bukti dari "perangkat elektronik lainnya" (mis. kamera ITCS) **wajib diverifikasi petugas Polri**; pelanggaran APILL termasuk objek ETLE; alur identifikasi → verifikasi ERI → surat konfirmasi (≤3 hari) → konfirmasi pemilik (≤5 hari) → tilang → bayar (≤7 hari) → blokir STNK. Implikasi desain: modul ETLE aplikasi = pengiriman bukti (foto/pelat/waktu/lokasi) via API ke Back Office ETLE, bukan penerbitan tilang. Dikirim ke fork KB-A & KB-B untuk dimasukkan ke peta regulasi & model data.
- Fork **PP-A selesai**: `docs/planning/03_Pasar_Kota_Target_dan_Pengadaan.md` (segmentasi, 12 profil kota, buying center, 6 jalur pengadaan, TKDN/Perpres 46/2025, siklus APBD, pesaing Javis/Qumicon/TKDN/Marktel/Yunex-SWARCO, harga pasar ATCS Rp350 jt–4,8 M/simpang [sumber web], model bisnis, GTM), `07_Persona_dan_Stakeholder.md` (12 persona, peta stakeholder, a-day-in-the-life TMC), `08_Asumsi_Risiko_Pertanyaan_Terbuka.md` (19 asumsi, 14 risiko, 13 pertanyaan + default, 12 keputusan tersirat). Insight: urgensi politik kota non-DKI lebih tinggi (TomTom); e-purchasing e-katalog = jalur utama; pendekatan APBD Okt–Feb; T1 harus plan-level control (bukan detik-ke-detik) untuk controller lama; sejarah SCATS Bandung/Jakarta memperkuat argumen standar terbuka.

### [T-12] 22:35 WIB — Verifikasi PP-A & panduan resume
- Dibaca & diperiksa: `docs/planning/03`, `07`, `08` (kualitas baik; sumber web dicantumkan; asumsi bertag [A]). Catatan konsistensi: penomoran D-/Q- di `08` berbeda dari `docs/kb/10` → `10` ditetapkan kanonis (dicatat di START_HERE).
- `docs/kb/00_START_HERE.md` ditulis: ringkasan proyek 5 menit, urutan baca murah→mahal, peta folder, konvensi (tag sumber, ID, nama tahap), cheat-sheet fakta kunci, workaround teknis, tindak lanjut.
- Menunggu fork: KB-A (01–03), KB-B (04–07), KB-C (08, 09, 11 + folder 07_Konteks_Kota_Target), PP-B (04–06).

### [T-13] 22:50 WIB — Fork KB-C selesai (riset kota target, pelajaran & risiko, kartu sumber)
- `docs/sources/07_Konteks_Kota_Target/`: 38 arsip teks + 1 jurnal (UNESA) + `_urls.tsv`; 13 pencarian, 39 unduhan; gagal: data.bandung.go.id/atcs (500), jdih.lkpp Perpres 46/2025 (timeout), pasjabar (404).
- `docs/kb/08_Pelajaran_Lapangan_dan_Risiko.md` (27 pelajaran berbukti + 18 risiko), `09_Konteks_Jakarta_dan_Kota_Target.md` (profil Jakarta + 11 kota/kab target, pola lintas kota, vendor & pengadaan), `11_Kartu_Sumber.md` (kartu semua sumber folder 01–07 & R00–R06; item belum dirangkum ditandai).
- Insight utama: Surabaya = peluang paling konkret (136 simpang/580 kamera SITS, hanya 8 sensor adaptif; Wali Kota menagih 2025); semua kota sudah punya CCTV+ruang kendali tetapi fungsinya pemantauan, bukan kendali → MVP menyerap alur kerja itu; Bandung kehilangan ±20 kamera karena satu node dirusak, Cianjur/Badung server down → resiliensi & health monitoring bisa dijual sekarang; anggaran nyata Rp1–4 M/simpang, pola bertahap 3→23→33; e-katalog + TKDN (Perpres 46/2025 Ps.66) → posisi realistis = lapisan software/ATMS di atas perangkat vendor lokal.

### [T-14] 23:05 WIB — Fork PP-B selesai & diverifikasi (konsep tahapan, inventaris fitur, arsitektur)
- `docs/planning/04_Konsep_Tahapan_1-5.md` (19 KB): 8 prinsip lintas tahap (edge-first & fail-safe, standar terbuka, anti black-box, hemat server, per koridor, KPI regulasi built-in, human-in-the-loop, kreatif berpijak); tiap tahap punya tujuan, exit criteria terukur, nilai bagi pembeli, lingkup, asumsi infrastruktur, sumber data, integrasi, kepatuhan (C-xx), validasi, durasi/tim [asumsi], risiko, dan "sengaja TIDAK dilakukan"; tabel ITCS DKI vs T4 vs T5; prasyarat sebelum planning rinci. Nama kerja tahap versi PP-B: T1 "Lihat & Kelola", T2 "Kendali Terkoordinasi", T3 "Responsif", T4 "Adaptif Terpadu", T5 "Platform Mobilitas Kota".
- `docs/planning/05_Inventaris_Fitur_per_Tahap.md` (27 KB): 141 fitur `F-T#-##` dalam 19 epik (E01 inventaris/aset … E19 TDM) dengan kolom bukti, tahap, MoSCoW, dependensi, data, kepatuhan, ukuran sukses. Ringkasan: T1 24 (20 Must), T2 44, T3 31, T4 29, T5 13; total 71 Must/48 Should/22 Could.
- `docs/planning/06_Arsitektur_Konseptual_dan_Opsi_Teknologi.md` (12 KB): diagram lapisan (penyajian/pusat/integrasi C2C/komunikasi/edge), matriks komponen per tahap, tabel opsi teknologi + rekomendasi awal (Python/FastAPI + Go edge; React+MapLibre+ECharts; PostgreSQL+PostGIS+TimescaleDB; MQTT→NATS; go2rtc/mediamtx video tanpa rekam; SUMO/TraCI; YOLO/PaddleOCR di edge; Keycloak+step-ca; Compose→k3s), model data & API ringkas, retensi & volume data, estimasi server per tahap [asumsi], daftar 18 ADR (ADR-01…ADR-18).
- Verifikasi saya: ketiga file dibaca penuh; konsisten dengan R00 §K, KB-10 (D-01…D-20) dan mandat user (T2 hemat server: 1 VM 8 vCPU/32 GB untuk ≤40 simpang [asumsi]). Catatan konsistensi yang harus dirapikan: (1) nama kerja tahap di `01` & START_HERE ("Lihat & rapikan" dst.) berbeda dari `04` → `04` ditetapkan kanonis, START_HERE & `01` disesuaikan; (2) penomoran ADR: `06` memakai ADR-01…18, sedangkan `10` & KB-10 U-05 memakai ADR-000/001…005 → `06` ditetapkan kanonis, `10` & KB-10 disesuaikan; (3) di `05` ID F-T3-58 (ingest probe) muncul di E18 tetapi dirujuk sebagai dependensi F-T2-66 (laporan kecepatan/V/C, T2) → catatan: di T2 laporan V/C memakai count/survei, probe menyusul di T3 (diperbaiki di file).

### [T-15] 23:10 WIB — Fork KB-A selesai (glosarium, lembar rumus, peta regulasi)
- `docs/kb/01_Glosarium.md` (31 KB, ±160 istilah, 7 kelompok, tiap baris bertag sumber + catatan implementasi); `02_Lembar_Rumus.md` (20 KB; PKJI 2023 A1–A34 dengan padanan MKJI/Dirjen 273, FHWA/NCHRP B1–B18, TRPS, max-pressure/cyclic MP/PC/OCC-MP/Transit-MP/EVP bersyarat, ATSPM E1–E14, LOS & ambang kebijakan; grafik yang perlu didigitalisasi ditandai ⚠); `03_Peta_Regulasi_Kepatuhan.md` (27 KB; tabel per regulasi termasuk PM 76 penuh, Pergub ganjil-genap 155/2018 jo. 88/2019 & 76/2020, UU PDP, **Perpol 8/2023 & 2/2025** dari pesan koordinator; matriks kepatuhan diperluas menjadi C-01…C-42 (C-36–C-38 PDP, C-41–C-42 ETLE); tabel kewenangan Dishub/Polri/Dirjen-BPTJ/Gubernur).
- Catatan KB-A untuk R0x (ditindaklanjuti sebagai catatan erratum, bukan menulis ulang R0x): R05 §C "PM 76 tidak dapat dikaji" sudah usang → rujuk R00 §C; R05 belum memuat Pergub ganjil-genap, UU PDP, Perpol ETLE → kini ada di KB-03; notasi Dirjen 273 vs PKJI berbeda → tabel padanan di KB-02; PKJI Nq1 tercetak "s" di dalam akar padahal dimensinya kapasitas C → keputusan implementasi: pakai C (sesuai MKJI/Dirjen 273), catat sebagai Q-11; kode enumerasi Indiana R03 §C.2 kini terverifikasi (T-11) — label "verifikasi" di glosarium bisa dihapus; angka SCOOT/SCATS R01 D.5 tetap "rekonstruksi" sampai NCHRP Synthesis 403 didapat.
- Menunggu: fork KB-B (04–07) — file sudah ada di disk, fork sedang memverifikasi jumlah.

### [T-16] 23:20 WIB — Fork KB-B selesai (katalog kebutuhan, kartu algoritma, model data, KPI)
- `docs/kb/04_Katalog_Kebutuhan.md` (37 KB): 121 kebutuhan `KB-REQ-###` unik dalam 11 kategori (hukum 22, kendali 24, prioritas 10, deteksi 7, komunikasi 9, fallback/O&M 9, data 9, integrasi 4, TMC-UI 7, KPI 7, pelatihan 3) + 10 non-fungsional (160–169) + 10 constraint `KB-CON-##`; tiap baris: pernyataan verifiable, sumber (ID R0x + pasal), prioritas, tahap, metode verifikasi D/T/A/I.
- `05_Kartu_Algoritma_Kendali.md` (23 KB): 14 kartu K-01 (TOD/Webster/PKJI) … K-14 (green wave/Link Pivot/probe) dengan tujuan, input, parameter default, pseudocode, guard-rail, bukti berangka, kesiapan, tahap, cara uji; pohon keputusan mode per simpang; hierarki fallback wajib.
- `06_Model_Data_dan_Antarmuka.md` (20 KB): 16 entitas konfigurasi + 14 runtime/time-series dengan padanan NTCIP/SUMO/PKJI; 15 enumerasi (kode hi-res dari tabel resmi Purdue termasuk 150/151); tabel CAI × 3 adaptor; matriks 12 integrasi eksternal; API internal per tahap.
- `07_KPI_dan_Monev.md` (14 KB): KPI 6 domain dengan rumus/data/agregasi/ambang/audiens/tahap; desain evaluasi 7 butir; 9 laporan wajib berdasar hukum.
- Inkonsistensi antar-R0x yang dilaporkan KB-B (semuanya sudah diputuskan di KB): PM 76 (R05 usang → R00 C); LOS HCM vs PM 96 (PM 96 resmi, HCM benchmark); min green MP 7 s vs PKJI ≥10 s (K-06 "≥7–10 s, sesuaikan ped/PKJI"); SLA keluhan 3 jam (DKI) vs ≤1 minggu (STM2) → 3 jam target lokal; kode hi-res R03 §C.2 → tabel Purdue resmi.

### [T-17] 23:35 WIB — Verifikasi seluruh basis pengetahuan & perbaikan konsistensi lintas file
- Dibaca penuh oleh saya: KB-02, KB-03, KB-04 (bagian A1–A9), KB-05, KB-06, KB-07; KB-01 dibaca bagian A–B penuh + daftar bagian (188 baris tabel, 7 kelompok). Kualitas: konsisten dengan R00 §K, angka cocok dengan sumber yang saya baca langsung (PM 49/96/76, Dirjen 273, SK 7234, Perpol).
- **Temuan & perbaikan** (skrip `fix_consistency.py`, semua idempoten):
  1. KB-03 §B memakai penomoran C-xx yang bergeser satu (menggabungkan C-02/C-04 R05) sehingga bertentangan dengan R05 §G.1, KB-04, docs/planning/04 & /05 → §B ditulis ulang: **C-01…C-35 identik dengan R05 §G.1 (kanonis)**, tambahan C-36 (PM 76 sistem terbuka & perangkat online), C-37…C-39 (UU PDP), C-40 (keamanan siber), C-41 (SK 7234), C-42 (Perpol 2/2025 bukti kamera non-ETLE), C-43 (Perpol 8/2023 ICD Polri).
  2. Nama kerja tahap: `docs/planning/04` ditetapkan kanonis (T1 "Lihat & Kelola", T2 "Kendali Terkoordinasi", T3 "Responsif", T4 "Adaptif Terpadu", T5 "Platform Mobilitas Kota"); `01` dan START_HERE disesuaikan.
  3. Penomoran ADR: `06` §7 (ADR-01…ADR-18) kanonis; `10_Checklist_Pra-GitHub` dan KB-10 U-05 disesuaikan.
  4. `05` F-T2-66 (kajian V/C, T2) bergantung pada fitur T3 (probe) → diperbaiki: T2 memakai count/survei (F-T2-59), probe menyusul T3.
  5. KB-10: Q-02 ditandai selesai (Purdue), Q-07 sebagian selesai (Perpol), **Q-11 baru** (notasi Nq1 PKJI "s" vs C — implementasi sementara pakai C).
  6. Erratum ditambahkan di kepala R05 §C (PM 76 kini dibaca penuh, rujuk R00 §C; Perpol/PDP/ganjil-genap ada di KB-03) dan R03 §C.2 (kode hi-res terverifikasi Purdue; kode 150/151 di KB-06).
  7. START_HERE §4 konvensi ID dilengkapi (C-##, KB-CON, K-##, E##, ADR) dan §7 tindak lanjut + daftar erratum.
- `README_INDEX.md` diperbarui: baris Perpol 8/2023 & 2/2025 (folder 01), Purdue enumerations (folder 02), bagian baru "07 — Konteks kota target", peta folder ditambah `07_Konteks_Kota_Target/` dan `docs/kb/`, catatan header.

### [T-18] 23:45 WIB — Penutupan fase pra-perencanaan
- Memori sesi (`itcs-project-context.md`) diperbarui: status, titik masuk resume, konvensi kanonis, pelajaran tentang verifikasi keluaran fork.
- Semua fork selesai (KB-A, KB-B, KB-C, PP-A, PP-B); tidak ada task tertunda dari sisi asisten.

---

## 4. Status Akhir Pra-Perencanaan & Langkah Berikutnya (23:50 WIB)

### 4.1 Yang sudah selesai (deliverable)
| Area | File | Keterangan |
|---|---|---|
| Studi acuan | `docs/sources/05_Website_Acuan_Majalah_RPP/ANALISIS_MAJALAH_RPP_LANCAR-JAKARTA.md` | 22 halaman majalah dianalisis |
| Bahan bacaan | `docs/sources/01–07` + `README_INDEX.md` | ±110 sumber (regulasi, manual FHWA/NCHRP/NTCIP/ATSPM, jurnal, konteks Jakarta & kota target, SUMO); workaround unduhan terdokumentasi |
| Catatan studi | `docs/sources/_ringkasan/R00–R06` | R00 = bacaan langsung + verifikasi + sintesis 7 pilar; R01–R06 ±62.000 kata (dengan 2 erratum tercatat) |
| Basis pengetahuan (murah dipelajari ulang) | `docs/kb/00–11` | START_HERE, glosarium (±160 istilah), lembar rumus (PKJI/FHWA/MP/ATSPM), peta regulasi (C-01…C-43), katalog kebutuhan (121 KB-REQ + 10 NFR + 10 constraint), 14 kartu algoritma, model data & antarmuka, KPI & monev, 27 pelajaran + 18 risiko, konteks 12 kota, 20 keputusan/8 keputusan user/11 pertanyaan, kartu sumber |
| Pra-perencanaan | `docs/planning/01–10` | visi & positioning, 7 kandidat nama (rekomendasi IRAMA), pasar & pengadaan 12 kota, konsep T1–T5 dengan exit criteria, 141 fitur per tahap (71 Must), arsitektur & 18 ADR, 12 persona, asumsi-risiko-pertanyaan, brief planning rinci, checklist pra-GitHub |

### 4.2 Keputusan yang menunggu user (KB-10 §B; default disarankan)
1. **U-01 Nama produk**: IRAMA (sub-merek Pantau/Atur/Ukur/Prioritas/Twin); cadangan NADI — wajib cek PDKI, domain, medsos sebelum dipakai.
2. **U-02 Kota/koridor pilot**: Surabaya (peluang paling konkret: 136 simpang SITS, hanya 8 adaptif) atau Bodetabek (dekat, ATCS dasar ada) atau Bandung (urgensi tertinggi, TomTom #12).
3. **U-03 Bangun controller sendiri vs integrasi**: integrasi (pusat + edge) di atas controller vendor lokal ber-TKDN.
4. **U-04 Lisensi & hosting**: open-core (inti Apache-2.0 + modul komersial); on-prem default, cloud opsional.
5. **U-05 Stack**: Python/FastAPI + Go edge; React + MapLibre; PostgreSQL/PostGIS + TimescaleDB; MQTT; SUMO — final lewat ADR-01…ADR-18.
6. **U-06 Tim & pendanaan**: 3–4 orang T1 (8–12 minggu), 5–7 orang T2 (4–6 bulan) [asumsi].
7. **U-07 Cakupan T5**: rekomendasi di `docs/planning/04` §6.
8. **U-08 Deteksi kamera**: hybrid (konsumsi output vendor + hitung dasar sendiri dari RTSP di edge).

### 4.3 Langkah berikutnya (sesi planning rinci)
1. User memutuskan U-01…U-08 (minimal U-01, U-02, U-04, U-05) dan membuat organisasi GitHub sesuai `docs/planning/10` §A–C (monorepo, ADR MADR, CI sim-smoke, project board dari `05`).
2. Sesi planning rinci mengikuti `docs/planning/09`: ConOps → SRS (turunkan dari KB-04 + `05`) → arsitektur & ADR → skema data (KB-06) → rencana sprint T1 → rencana validasi SIL/HIL/shadow/live → rencana pilot & MoU → rencana bisnis/GTM (`03`).
3. Paralel non-teknis: surat minat/MoU Dishub pilot, akses ruang kendali & log controller, izin rekam CCTV (PDP), kontak Ditlantas; bench controller + dokumentasi protokol (Q-01).
4. Riset yang masih terbuka: Q-01, Q-03 (NTCIP 1202 v03 & 1211), Q-04, Q-05, Q-06, Q-07 sebagian (Pergub MRLL/ERP, PM 67/2021, Perdirjen siklus), Q-08, Q-09, Q-10, Q-11.

### 4.4 Cara melanjutkan di sesi lain
Baca `docs/kb/00_START_HERE.md` (5 menit) → §2–§4 log ini → `docs/planning/09` → mulai planning. Setiap task baru wajib dicatat sebagai `[T-19]` dst. di file ini.

---

## 5. Mandat Lanjutan (00:05 WIB, 2026-09-13) — Keputusan user & push ke GitHub
Instruksi user: (a) ajukan setiap hal yang membutuhkan keputusan (U-01…U-08 + Q-01…Q-11) sebagai pertanyaan pilihan ganda semi-terbuka 4 pilihan + jawaban terbuka, disertai rekomendasi; (b) bantu push semua aset lokal ke repositori GitHub yang disiapkan user.

### [T-19] 00:05 WIB — Pemeriksaan lingkungan git & penyusunan pertanyaan keputusan
- Lingkungan: git 2.54 (user `lionateofhaidar`), git-lfs 3.7.1 tersedia, `gh` CLI **tidak terpasang**. Folder proyek berada di dalam repo git induk `Hydem Custodia & Co` (remote `damawebsite-project`) dan masih untracked → perlu keputusan: repo terpisah (nested) atau subfolder repo induk.
- Ukuran aset: total ±314 MB (02 Panduan 92 MB, 03 Jurnal 79 MB, 01 Regulasi 63 MB, 05 Majalah 41 MB, teks ekstraksi 16 MB, MKJI 13 MB); tidak ada file >40 MB (batas GitHub 100 MB/file aman), tetapi PDF/gambar sebaiknya via Git LFS atau dikecualikan. Jenis file: 93 md, 72 txt, 72 pdf, 57 html, 24 png, 22 webp, 2 json, 1 tsv, 1 jpg.
- Pertanyaan keputusan disusun: 8 keputusan user (U) + 11 pertanyaan riset (Q) + 3 keputusan repo (isi, struktur, mekanisme), diajukan bertahap 4 pertanyaan per batch.

### [T-20] 00:20 WIB — Jawaban user batch 1–3 (U-01…U-08, Q-01)
- U-01 Nama: **IRAMA** (sementara; user menilai paling engaging, keputusan final menunggu gambaran fitur end-state).
- U-02 Pilot: awalnya Surabaya, **kemungkinan digeser ke Bandung** karena basis personel di Bandung. CCTV: portal publik Surabaya tidak terjangkau dari lingkungan ini; user akan menyediakan **3–5 klip ±30 menit** variasi kondisi (siang/malam/sibuk/sepi/hujan).
- U-03 Edge: **edge-light di T2** (agen minimal di mini-PC/Pi hanya untuk controller serial-only; edge penuh di T3). Penilaian selisih effort: moderat (±15–25% effort T2) [asumsi].
- U-04 Lisensi: **open-core, on-prem default**.
- U-05 Stack: **Python/FastAPI + Go edge, React+MapLibre, PostgreSQL/PostGIS+TimescaleDB, MQTT, SUMO**.
- U-06 Tim: **berdua sampai T2**, +1–2 orang di T3–T5, tanpa field engineer, dana sangat terbatas (develop dulu, jual kemudian) → pola **simulation-first + mitra lapangan** (teknisi Dishub/vendor), design partner dicari sejak T1 selesai, lingkup dipangkas ke Must, jadwal 2 orang: T1 3–4 bulan, T2 6–9 bulan [asumsi].
- U-07 T5: **Platform Mobilitas Kota multi-tenant**.
- U-08 Kamera: **hybrid** (output vendor + hitung dasar sendiri), **pemrosesan pelat sudah menjadi output T3** (bukan T4) → catatan: DPIA & tata kelola PDP (C-37…C-39) harus maju ke T3.
- Q-01 Kontroler: **survei Dishub + vendor dengan kuesioner** yang saya susun; syarat user: bahasa tidak terlalu teknis, tidak terkesan "AI-generated", protokol/spesifikasi yang umum langsung diasumsikan (tidak ditanyakan), tidak menyebut kota tertentu.

### [T-21] 00:30 WIB — Jawaban user batch 4 (U-02 revisi, Q-03…Q-05)
- U-02 final: **Bandung = kota pilot & design partner; Surabaya = target ke-2**. Dokumen pasar & kuesioner dibuat netral kota.
- Q-03 NTCIP v03/1211: kemungkinan **beli saat T2 dimulai**. Permintaan baru user: **daftar kebutuhan pengadaan proyek mandiri** (standar/dokumen berbayar, perangkat, layanan, data, sertifikasi, legal) per tahap, dengan konsekuensi bila tidak diadakan / diadakan tidak pada tahapnya, dalam bahasa sederhana untuk non-teknis → deliverable baru `docs/planning/11_Kebutuhan_Pengadaan_per_Tahap.md`.
- Q-04 klaim DKI: **tidak dikejar**, pakai bukti internasional + hasil pilot sendiri (on/off).
- Q-05 Makassar: **prioritas rendah**, cukup konteks.
- Deliverable lain yang sudah disepakati: kuesioner survei controller (Q-01) → `docs/planning/12_Kuesioner_Survei_Kontroler.md`.

### [T-22] 00:40 WIB — Jawaban user batch 5 (Q-06…Q-09)
- Q-06: **ganti dengan data kota pilot (Bandung)**. Permintaan baru: **daftar kebutuhan data yang harus disediakan user per tahap** (T1 presisi, T2–T5 estimasi) → deliverable `docs/planning/13_Kebutuhan_Data_per_Tahap.md`.
- Q-07: **semua sekarang** — unduh & rangkum regulasi tersisa (Pergub DKI turunan MRLL/ERP, PM 67/2021 bila ada, Perdirjen tata cara waktu siklus) + regulasi Jabar/Kota Bandung (Perda/Perwal transportasi, ATCS, data) → task riset (fork) di sesi ini.
- Q-08: **floating car sendiri + AVL bus kota**; ojol/navigasi dinegosiasikan setelah ada pembeli.
- Q-09: **TKDN lewat mitra vendor lokal dulu**; TKDN software sendiri setelah pembeli pertama.

### [T-23] 00:50 WIB — Jawaban user batch 6 (Q-10, Q-11, REPO-1, REPO-2)
- Q-10: **unduh paper Purdue (Day et al. 2010 / TPF-5(258)) + rujuk kode open-source ATSPM UDOT** saat T3 → task unduh di sesi ini.
- Q-11: **Nq1 memakai C (kapasitas)**, diuji ke contoh resmi Dirjen 273/MKJI; dicatat sebagai asumsi terdokumentasi.
- REPO-1: **sumber yang sudah terekstraksi lengkap ke teks cukup dipush teksnya; PDF/gambar yang tidak terekstraksi lengkap via Git LFS; repo privat.**
- REPO-2: **struktur monorepo sesuai checklist**, dan **folder lokal ikut dirapikan** agar strukturnya sama dengan repo (docs/kb, docs/planning, docs/sources, docs/LOG_SESI.md, folder kode kosong ber-README).

### [T-24] 01:00 WIB — Jawaban user batch 7 (REPO-3…REPO-5) & mulai restrukturisasi
- REPO-3: **repo terpisah (nested) di folder proyek**; folder ditambahkan ke `.gitignore` repo induk.
- REPO-4: **Git LFS untuk semua PDF & gambar** (±300 MB; dalam kuota gratis GitHub 1 GB).
- REPO-5: repo sudah dibuat di akun `lionateofhaidar`; URL menyusul dari user (belum ditempel) → push dilakukan setelah URL diterima.
- Tindakan: folder lokal dirapikan ke struktur monorepo (`docs/kb`, `docs/planning`, `docs/sources`, `docs/LOG_SESI.md`, `docs/adr` + template MADR, kerangka `apps/ services/ edge/ sim/ packages/ infra/ tests/ .github` ber-README), README.md, LICENSE (Apache-2.0 untuk inti, catatan open-core), `.gitattributes` LFS, `.gitignore`; seluruh rujukan path di dokumen diperbarui otomatis (skrip `restructure.py`).

### [T-25] 01:20 WIB — Restrukturisasi selesai, deliverable baru, keputusan diterapkan, repo lokal dibuat
- Restrukturisasi lokal selesai: `docs/kb` (dulu `Bahan Acuan/_knowledge_base`), `docs/planning` (dulu `Pra-Perencanaan`), `docs/sources` (dulu `Bahan Acuan`), `docs/LOG_SESI.md`; 18 file .md rujukan path diperbarui otomatis; kerangka repo (README, LICENSE, .gitattributes LFS, .gitignore, docs/adr + template MADR, docs/conops, docs/srs, apps/ services/ edge/ sim/ packages/ infra/ tests/ .github ber-README). Folder ditambahkan ke `.gitignore` repo induk.
- Deliverable baru: `docs/planning/11_Kebutuhan_Pengadaan_per_Tahap.md` (dokumen/standar, perangkat, layanan, data, legal/merek/badan usaha/TKDN/PDP, SDM; tahap, harga [perkiraan], konsekuensi bila tidak/terlambat/terlalu awal; urutan pengadaan 2 orang), `12_Kuesioner_Survei_Kontroler.md` (27 pertanyaan Dishub + 7 vendor, bahasa awam, netral kota, tabel asumsi internal yang tidak ditanyakan), `13_Kebutuhan_Data_per_Tahap.md` (T1 presisi D1.1–D1.10 dengan format CSV & cara pengumpulan; T2–T5 estimasi; daftar cek cetak).
- Keputusan user diterapkan ke dokumen: KB-10 §B (U-01…U-08 + REPO) & §C (Q-01…Q-11 berstatus DIPUTUSKAN), `04` §7b revisi (tim 2 orang, edge-light, pelat T3, pilot Bandung), `05` F-T4-125 → T3, `10` checklist dicentang, START_HERE diperbarui.
- Fork riset diluncurkan (Q-07 regulasi Jabar/Bandung + DKI ERP + PM 67/2021 + Perdirjen siklus; Q-10 paper Purdue Link Pivot; Q-06 data simpang/ATCS Bandung) → keluaran `docs/sources/_ringkasan/R07_*`, `docs/sources/08_Data_Kota_Pilot_Bandung/`.
- Git: `git init` (branch main) di folder proyek, LFS diaktifkan, remote `origin` = https://github.com/lionateofhaidar/irama-project.git (repo kosong, dapat diakses). Commit pertama menyusul di entri berikutnya.

### [T-26] 01:30 WIB — Commit pertama & push
- Identitas git repo-lokal diset (`lionateofhaidar`, sama dengan repo induk). Commit pertama `8777d54` "Inisialisasi repo IRAMA": seluruh docs/, kerangka monorepo; 129 file biner (PDF/gambar) sebagai pointer Git LFS; pack teks 4,4 MiB.
- Push `main` ke `origin` (https://github.com/lionateofhaidar/irama-project) dijalankan di latar belakang (unggah LFS ±300 MB). Hasil dicatat di entri berikutnya.
- Catatan: fork riset R07 masih berjalan; hasilnya akan di-commit terpisah setelah diverifikasi.

### [T-27] 01:45 WIB — Push pertama berhasil
- `main` → `origin/main` (commit `8777d54`) berhasil; 129 objek LFS terunggah (414 MB, ±5,9 MB/s). Branch lokal melacak `origin/main`. Repo dapat dibuka di https://github.com/lionateofhaidar/irama-project.
- Catatan kuota: unggahan 414 MB memakai penyimpanan LFS gratis GitHub (batas 1 GB penyimpanan & 1 GB bandwidth/bulan); setiap clone penuh akan memakai ±414 MB bandwidth → clone dengan `GIT_LFS_SKIP_SMUDGE=1` bila hanya perlu teks.

### [T-28] 02:05 WIB — Fork riset R07 selesai & diverifikasi; commit kedua
- Diunduh (folder 01): Perda Kota Bandung 12/2024 Penyelenggaraan Perhubungan (mencabut 16/2012; Bab IX STC Ps.103–106 "sistem terbuka"; Ps.111–114 TIK Dishub+Diskominfo; Ps.122 rekomendasi Polri & Pemprov; Ps.138 optimalisasi oleh Dishub setelah koordinasi Polri), Perda Jabar 5/2024 (Ps.20 persetujuan provinsi untuk MRLL di jalan provinsi; Ps.166 sistem informasi terintegrasi), Perwal Bandung 101/2022 SOTK Dishub (ATCS/CCTV/kinerja berbasis TI di Seksi Lalu Lintas Jalan — eselon IV, tanpa UPT ATCS), Perwal 49/2021 UPTD, Perwal 20/2023 SPBE (scan, hanya abstrak), Pergub DKI 25/2017 ERP (+ pencabutan 20/2022). PM 67/2021 = Ortaker Kemenhub → tidak relevan. Perdirjen "tata cara waktu siklus" tidak ada; yang ada SK.326/2018 (tidak dapat diunduh, dikutip dari tesis PTDI-STTD).
- Diunduh (folder 02): Purdue JTRP 2014 (POG Eq.6.5, platoon ratio Eq.6.6, tabel arrival type hal.71–73), JTRP 2008 (Eq.4.17–4.18), TRB 11-0036 (AOG Eq.6, tundaan Eq.3), poster ATSPM 2016 (algoritma Link Pivot: sapu δ=0…C−1 per link dua arah, akumulasi ke offset hulu, O_new=(O_old+Δ) mod C), pohon repo ATSPM UDOT v4 & v5 (OpenSourceTransportation/Atspm: ConfigApi/DataApi/ReportApi/IdentityApi, WebUI, WatchDog, PostgreSQL provider, Docker). Paper TRR 2259-04 berbayar → direkonstruksi.
- Folder baru `docs/sources/08_Data_Kota_Pilot_Bandung/` (50 file): 24 lokasi/46 kamera ATCS dengan koordinat (endpoint portal), 21 arsip berita, `_urls.tsv`. Temuan: 150 APILL, 66 simpang ber-CCTV terhubung ATCS (Kadishub 23-07-2026), ruang kendali Balai Kota Jl. Wastukencana 2; Wali Kota: ATCS "semi-manual, teknologi usang", uji coba AI di Pasteur; vendor tidak disebut; TMB 5 koridor + AVL BEMO (tanpa GTFS-RT publik). Kandidat koridor pilot: **K-A Pasteur–Cikapayang–Dago (6 simpang, ±1,9 km, semua ≤1 km)**, K-B Soekarno-Hatta Batununggal–Buah Batu–Kircon (kemungkinan jalan nasional), K-C Cibaduyut–M. Toha, K-D PHH Mustofa.
- `R07_Regulasi_Tambahan_Purdue_dan_Data_Bandung.md` (39 KB) dibaca & diverifikasi (rujukan halaman lengkap); README_INDEX diperbarui fork (bagian 01, 02, 08). START_HERE §2 ditambah R07. Q-07 & Q-10 kini SELESAI (kecuali SK.326/2018 resmi & TRR 2259-04 berbayar).
- Commit kedua + push ke `origin/main` (lihat hasil di bawah).
- Hasil: commit `79d34d5` dipush ke `origin/main` (3 objek LFS baru 6,6 MB; PDF Perda Bandung/Jabar & JTRP 2014 sudah masuk di commit pertama karena dibuat sebelum commit). Working tree bersih, `main` sinkron dengan remote.

---

## 6. Status Akhir Sesi 2026-09-13 & Langkah Berikutnya
- **Semua keputusan terjawab** (U-01…U-08, Q-01…Q-11, REPO-1…REPO-5) — tercatat di `docs/kb/10` §B–C dan entri T-20…T-24.
- **Repo GitHub privat** `lionateofhaidar/irama-project`: 2 commit, 132 objek LFS (±421 MB), struktur monorepo; clone ringan: `GIT_LFS_SKIP_SMUDGE=1 git clone …`.
- **Deliverable baru**: `docs/planning/11` (pengadaan per tahap), `12` (kuesioner survei controller), `13` (kebutuhan data per tahap), `docs/sources/_ringkasan/R07`, `docs/sources/08_Data_Kota_Pilot_Bandung/`.
- **Tindakan user berikutnya**: (1) cek merek IRAMA di PDKI & domain; (2) kumpulkan data T1 sesuai daftar cek `docs/planning/13` (koridor kandidat K-A Pasteur–Cikapayang–Dago) + 3–5 klip CCTV; (3) bawa kuesioner `12` ke Dishub Kota Bandung (Seksi Lalu Lintas Jalan, Bidang Lalu Lintas & Perlengkapan Jalan) dan 1–2 vendor; (4) sesi berikutnya: planning rinci end-to-end (ConOps → SRS → ADR-01…ADR-18 → skema data → sprint T1) mengikuti `docs/planning/09`.
- Log berikutnya dimulai dari `[T-29]`.

---

## 7. Mandat Lanjutan (2026-09-13 pagi) — Kepanjangan IRAMA, versi .docx/.pdf dokumen planning, arsitektur per tahap
Instruksi user: (a) tambahkan kepanjangan bahasa Inggris IRAMA yang engaging di dokumen nama; (b) buat versi .docx rapi untuk semua file `docs/planning/` — **tidak dipush ke GitHub**; (c) pendekatan penjelasan .docx disederhanakan untuk pembaca IT Strategy non-teknis; (d) hindari ciri tulisan AI (em-dash, subjudul retoris, titik dua tanpa konteks, clickbait, nada terlalu yakin, pola "bukan X melainkan Y", angka tidak penting, judul "dari X ke Y"); judul teknis & deskriptif; (e) pastikan ada pembahasan arsitektur per tahap T1–T5 yang lengkap & mudah dipahami; (f) versi PDF berpassword yang "kedaluwarsa 3 hari" untuk dibagikan ke rekan (rahasia).

### [T-29] 09:10 WIB — Kepanjangan IRAMA, dokumen arsitektur per tahap, persiapan .docx
- `docs/planning/02` ditambah §2a: makna IRAMA + 4 kepanjangan Inggris (rekomendasi: **Integrated Roadway Adaptive Management Architecture**; alternatif Intelligent Roadway Analytics and Mobility Assurance; Integrated Real-time Arterial Management Assistant; Intelligent Routing, Adaptive signals, and Mobility Analytics), padanan Indonesia, tagline dua bahasa.
- `docs/planning/14_Arsitektur_per_Tahap.md` (baru): lima lapisan (lapangan, komunikasi, pusat, integrasi, penyajian) × T1–T5 dengan gambaran singkat, tabel susunan, alur data/perintah, alasan desain, ukuran; tabel ringkas lapisan×tahap; bagian yang tidak berubah; risiko arsitektur. Ditulis langsung dengan gaya sederhana (aturan gaya user).
- Aturan baru dicatat: `.gitignore` menambah `docs/planning/docx/`, `docs/planning/*.docx`, `docs/planning/*.pdf`; memori `user-writing-and-sharing-preferences` (gaya tulisan, audiens, larangan push docx/pdf).
- Alat tersedia: python-docx 1.2, pypdf 6.16 + cryptography (enkripsi AES-256), reportlab (watermark), Microsoft Word 16 via COM (docx→pdf). LibreOffice/pandoc tidak ada.
- Rencana: tiga fork menulis versi sederhana (markdown subset) untuk dokumen 01–13 ke `docs/planning/docx/src/`; 14 disalin apa adanya; skrip `build_docx.py` membangun .docx (gaya seragam, header "RAHASIA", nomor halaman) → .pdf (Word) → .pdf terenkripsi + watermark + pembatasan cetak/salin.
- Catatan penting untuk user (disampaikan di ringkasan): password PDF **tidak bisa kedaluwarsa dengan sendirinya** di dalam file; PDF standar tidak punya mekanisme waktu. Yang bisa dilakukan: password + larangan cetak/salin + watermark bertanggal + peringatan JavaScript (hanya di Acrobat, mudah dilewati) + membagikan lewat tautan yang kedaluwarsa (OneDrive/Google Drive) dan mengganti password tiap 3 hari.

### [T-30] 18:30 WIB — Versi .docx & PDF terkunci untuk 14 dokumen planning (lokal saja)
- Tiga fork menulis versi sederhana (audiens IT Strategy, aturan gaya user) dokumen 01–13 ke `docs/planning/docx/src/`; 14 disalin dari kanonis. Saya memeriksa: tidak ada em-dash, heading tingkat 4, blok kode, simbol centang; sisa pola "bukan X" (3 kalimat) diperbaiki manual; tiap file punya paragraf Ringkasan.
- `build_docx.py` (python-docx → Word COM → pypdf): 14 .docx (sampul ringkas, header RAHASIA, nomor halaman, tabel berlebar kolom), 14 PDF arsip (`docx/pdf/`), 14 PDF terkunci (`docx/pdf_terkunci/`: AES-256, password buka, larangan cetak/salin/ubah, watermark diagonal "RAHASIA IRAMA | untuk rekan tim | berlaku s.d. 16-09-2026", peringatan JavaScript kedaluwarsa untuk Acrobat). Total 63 halaman. Password di `docx/PASSWORD_LOKAL.txt`.
- Tampilan diperiksa dari render PNG (pymupdf) untuk dokumen 01, 05, 11, 14: rapi.
- Seluruh folder `docs/planning/docx/` terkonfirmasi diabaikan git (`git check-ignore`). Yang dipush hanya: `02` (kepanjangan IRAMA), `14` (arsitektur per tahap, versi kanonis), `.gitignore`, log.
- Keterbatasan yang disampaikan ke user: PDF tidak dapat kedaluwarsa dengan sendirinya; peringatan JavaScript hanya bekerja di Adobe dan mudah dilewati. Rekomendasi: bagikan lewat tautan berkedaluwarsa (OneDrive/Google Drive), kirim password lewat kanal terpisah, jalankan ulang `build_docx.py` untuk password & watermark baru setiap 3 hari, dan pertimbangkan perjanjian kerahasiaan tertulis.

### [T-31] 19:30 WIB — Diagram alur fitur utama end-state dengan pemetaan arsitektur & tahap (dokumen 06)
- `docs/planning/diagram/make_diagrams.py` (matplotlib): 12 diagram alur (F01 pemantauan status; F02 perencanaan & penetapan jadwal; F03 kendali terpusat/manual/cadangan; F04 kesehatan perangkat & tiket; F05 pengukuran kinerja & laporan wajib; F06 deteksi kamera & detektor virtual; F07 kendali responsif & adaptif; F08 prioritas bus & darurat; F09 bukti ETLE; F10 keluhan publik & SLA; F11 twin, mode bayangan, marketplace; F12 multi-kota, data terbuka, TDM) + F00 gambaran komponen per lapisan. Format swimlane: baris = lapisan arsitektur (pengguna/mitra, penyajian, pusat, komunikasi & integrasi, lapangan); kotak = langkah berhuruf; label warna pojok kotak = tahap pertama tersedia (T1 hijau … T5 merah); panah berlabel kondisi. Skrip juga menghasilkan mermaid (`F##.mmd`) dan potongan markdown (versi kanonis dengan mermaid, versi sederhana untuk docx).
- Dokumen 06 kanonis (`docs/planning/06`) ditambah §8 "Diagram alur fitur utama" (cara membaca, F00–F12, tabel langkah → lapisan → komponen repo → tahap, mermaid). Versi docx/PDF 06 ditambah bagian yang sama dalam halaman landscape, satu diagram per halaman (31 halaman).
- Builder docx diperluas: gambar, penanda `<<<LANDSCAPE>>>` dan `<<<PAGEBREAK>>>`, lebar kolom proporsional terhadap lebar halaman aktif; build parsial (`--only`) memakai password yang sudah ada. Semua 14 dokumen dibangun ulang dengan satu password baru (tersimpan di `docx/PASSWORD_LOKAL.txt`).
- Dipush: 06 kanonis + folder `docs/planning/diagram/` (PNG via LFS, mmd, skrip). Tidak dipush: docx/pdf.

---

## 8. Mandat Lanjutan (2026-09-14) — Perubahan kritikal fokus T2: Vision Tracker + Optimasi Adaptif Waktu Simpang
Instruksi user (ringkas, model berganti ke Opus 5):
- (a) Baca ulang konteks sesi (log & dokumen penting) secara teliti.
- (b) **Output T2 = modul Vision Tracker yang berjalan baik + modul Optimasi Adaptif Waktu Simpang.** Pengembangan lanjutan kedua modul dan fitur sampingan lain bertahap di T3–T5.
  - Vision Tracker T2: menghitung arus menurut klasifikasi kendaraan (motor, LV, HV) dan menghitung hambatan samping menurut klasifikasinya. T3: membaca anomali (ambulans, damkar, dan lain-lain yang direkomendasikan).
  - Optimasi Adaptif T2: mengonsumsi tabel terstruktur keluaran Vision Tracker, mengonversi ke volume arus, merekomendasikan waktu siklus & waktu hijau optimal untuk LOS terbaik per periode waktu; fitur konfigurasi data simpang & data statis lewat frontend yang intuitif. Acuan: otomatisasi perhitungan dalam naskah tugas akhir yang diletakkan user di `docs/sources/` (dokumen lokal, tidak dipush), disesuaikan ke standar & best practice terbaru.
  - Dashboard: kapasitas tiap simpang & rincian per arah, volume arus per simpang & per arah, waktu hijau & siklus rekomendasi, LOS optimal keseluruhan & per simpang, dan metrik penting lain.
- (c) **Tidak ada pengadaan sampai T3 selesai**; end-state dengan risiko vendor lock-in minimal.
- (d) Bagian **Definisi Istilah** di akhir `01_Visi_Produk_dan_Positioning` dengan bahasa mudah (contoh: user tidak tahu SUMO).
- (e) Di `14_Arsitektur_per_Tahap`: satu diagram arsitektur high-level alur CCTV → Vision Tracker → … → keputusan/dashboard, lengkap dengan teknologi tiap alur dan penanda tahap T1–T5.
- (f) Ajukan pertanyaan pilihan ganda semi-terbuka (4 pilihan + jawaban terbuka) dengan rekomendasi untuk setiap hal yang ambigu.
- (g) Log sesi tetap diperbarui di file yang sama setiap task.

### [T-32] 09:00 WIB — Mulai mandat baru: baca ulang konteks, ekstraksi naskah tugas akhir
- Status repo saat mulai: `main` sinkron dengan `origin` (commit terakhir `6a8b136`); satu file baru tidak terlacak: naskah tugas akhir user (8,8 MB). Belum di-commit sampai ada keputusan user (akhirnya: tidak dipush, T-40).
- Langkah: ekstraksi teks naskah TA (pdftotext), baca penuh; baca ulang dokumen planning 01, 04, 05, 06, 11, 13, 14 dan KB-10; periksa spesifikasi laptop (CPU/GPU/RAM) untuk menilai kelayakan vision tracker tanpa pengadaan; cek sumber CCTV publik Bandung yang sudah terarsip.

### [T-33] 10:30 WIB — Naskah TA dibaca penuh; pemeriksaan standar PKJI 2023, laptop, dan sumber CCTV
- Naskah tugas akhir yang diletakkan user di `docs/sources/` dibaca penuh (bab metode, analisis kinerja simpang dan ruas, valuasi manfaat, lampiran formulir). **Naskah, teks ekstraksinya, dan ringkasan rinciannya hanya disimpan lokal dan tidak dipush (keputusan user T-40).** Catatan rinci ada di `docs/sources/_ringkasan/R08_Catatan_Lokal_Naskah_TA.md` (lokal, di-.gitignore).
- Garis besar yang relevan untuk produk: rantai perhitungan kinerja simpang bersinyal berbasis MKJI 1997 (hitungan lalu lintas per kelas per 15 menit, geometri & kondisi lingkungan per pendekat, arus jenuh, kapasitas, derajat kejenuhan, antrian, kendaraan terhenti, tundaan, perbandingan kondisi, penentuan waktu siklus Webster) serta valuasi manfaat (nilai waktu, biaya operasional kendaraan, emisi). Modul optimasi IRAMA akan mengotomasi rantai ini dengan standar terbaru.
- **Penyesuaian ke standar terbaru**: PKJI 2023 menggantikan MKJI 1997 (EMP simpang APILL MP 1,00; KS 1,30; SM 0,15 terlindung / 0,40 terlawan; KTB tidak dikonversi, masuk RKTB untuk FHS); LOS simpang resmi berbasis tundaan PM 96/2015 (A <5 … F >60 s/kend), DS tetap ditampilkan (target ≤0,85); hambatan samping dari frekuensi berbobot PKJI 2023 Tabel 4-8 (pejalan kaki 0,5; kendaraan berhenti 1,0; keluar/masuk 0,7; kendaraan lambat/KTB 0,4) per 200 m per jam → KHS SR/R/S/T/ST (Tabel 4-9); tundaan simpang rata-rata tertimbang arus; Nq1 memakai C (Q-11).
- Laptop tim (mesin ini): AMD Ryzen 7 7730U 8 inti/16 thread, RAM 31,4 GB, GPU terintegrasi Radeon (tanpa NVIDIA), disk kosong 249 GB → vision tracker dapat berjalan di CPU/iGPU (ONNX Runtime) untuk pemrosesan batch rekaman dan beberapa stream; cukup untuk T1–T2 tanpa pengadaan.
- Portal ATCS Bandung memutar CCTV publik dalam format HLS lewat endpoint POST `/ajax/cctv-info`; satu percobaan mengembalikan 404 (kemungkinan butuh sesi/header), tidak diteruskan. 46 kamera, sebagian bernama "VID … (Dari Arah …)" = kamera per pendekat. (Keputusan T-39: tidak dipakai sebelum ada MoU.)
- Temuan lisensi penting: Ultralytics YOLO (v8/11) berlisensi AGPL-3.0, bertentangan dengan open-core komersial kecuali membeli lisensi enterprise. Alternatif permisif: RF-DETR, YOLOX, RTMDet (Apache-2.0), ByteTrack/OC-SORT (MIT), supervision (MIT), ONNX Runtime (MIT).

### [T-34] 10:45 WIB — Jawaban user batch A (lingkup T1, mode vision, skala T2, akurasi)
- T1: **purwarupa ujung ke ujung di 1 simpang** (Vision Tracker menghitung MC/LV/HV dari rekaman di semua pendekat, input data simpang manual sederhana, kalkulator PKJI 2023, rekomendasi siklus & hijau, dashboard dasar).
- Mode Vision Tracker T2: **rekaman dan stream langsung**; rekaman menjadi kanal piloting & pengujian di awal, stream langsung untuk operasi.
- Skala T2: **cukup 1 simpang lengkap**; **analisis optimasi tingkat koridor dipindah ke T5** (perlu klarifikasi dampaknya ke koordinasi/green wave T4).
- Akurasi lulus T2: **≥95% siang, ≥90% malam/hujan** per kelas per 15 menit dibanding hitungan manual.

### [T-35] 11:00 WIB — Jawaban user batch B (koridor, standar, LOS, metode optimasi)
- Koridor: **offset dasar/green wave sederhana di T4** (agar tetap setara ITCS); **optimasi koridor & jaringan penuh di T5**. T3–T4 mengoptimasi tiap simpang secara mandiri.
- Standar: **PKJI 2023 utama + mode MKJI 1997** (pembanding studi lama dan uji regresi terhadap angka TA).
- LOS: **tundaan PM 96/2015 sebagai kelas resmi + DS pendukung** (batas desain ≤0,85).
- Metode optimasi: **beberapa mode yang bisa dipilih (toggle)** di T2, minimal: (1) cari tundaan terendah dengan batasan, (2) Webster/PKJI baku, (3) minimalkan DS tertinggi; boleh ditambah pendekatan lain yang effort-nya setara/lebih rendah; (4) **multi-kriteria berbobot dipindah ke T3**. Usulan tambahan saya (effort ≤ opsi 1–3): (5) siklus praktis minimum yang memenuhi DS target; (6) pertahankan siklus eksisting, atur ulang pembagian hijau saja.

### [T-36] 11:15 WIB — Jawaban user batch C (periode, kelas, hambatan samping, per arah)
- Periode: **profil 15 menit dikelompokkan otomatis menjadi maksimal 8 jadwal** (weekday/weekend), dengan **fleksibilitas pengguna menentukan periode lewat konfigurasi simpang**.
- Kelas kendaraan: **simpan kelas rinci, petakan otomatis ke PKJI** (SM/MP/KS/KTB). Catatan implementasi: pemetaan ke MKJI (MC/LV/HV/UM) tetap dibuat untuk mode pembanding MKJI 1997 (keputusan batch B).
- Hambatan samping: **hitung 4 jenis kejadian berbobot PKJI 2023** (pejalan kaki 0,5; kendaraan berhenti/parkir 1,0; keluar-masuk 0,7; kendaraan lambat/KTB 0,4) per 200 m per jam → KHS SR/R/S/T/ST → dipetakan ke tinggi/sedang/rendah untuk FHS simpang; engineer dapat mengoreksi.
- Volume per arah: **dari lintasan masuk-keluar; cadangan proporsi belok manual**, sumber ditandai di dashboard.

### [T-37] 11:30 WIB — Jawaban user batch D (manfaat rupiah, laporan, validasi, dashboard)
- Manfaat ekonomi: **T2 versi sederhana** (nilai waktu pendekatan UMK, BBM/BOK, emisi; parameter terbaru & dapat diubah).
- Laporan kajian otomatis per simpang (Word/PDF, format formulir PKJI SA-I s.d. SA-V + narasi): **T2**.
- Validasi rekomendasi: **hitung PKJI + simulasi SUMO di T2**; uji lapangan sebelum-sesudah di T3.
- Dashboard T2: semua tambahan disetujui (eksisting vs rekomendasi + manfaat; profil volume & komposisi; antrian & detail per pendekat; kualitas data). **Catatan user: jangan dipaksakan dalam satu halaman; rekomendasikan 2–3 halaman dashboard yang terpisah jelas dan rapi.**

### [T-38] 11:45 WIB — Jawaban user batch E (anomali T3, vision tambahan, ANPR, controller)
- Anomali T3: **kendaraan prioritas & pengawalan; kejadian lalu lintas; pelanggaran & hambatan (bukti saja)**; **kesehatan kamera & lingkungan bertahap: yang paling mudah dikenali di T3 (tertutup, gelap, buram, bergeser), lanjutan di T4 (hujan lebat, genangan/banjir, dll.)**.
- Vision tambahan: **semua dipilih** — membaca nyala lampu dari kamera (T2), panjang antrian & okupansi per lajur (dasar T2, lengkap T3), volume & waktu tunggu pejalan kaki (hitungan pejalan kaki sudah ada di T2 sebagai hambatan samping; waktu tunggu T3), kecepatan & waktu tempuh antar kamera tanpa pelat (T3).
- ANPR: **dipindah ke T4** (bersama pengadaan kamera khusus & integrasi ETLE/Bapenda). Keputusan U-08 lama (pelat T3) direvisi.
- Controller: **T3 baca-saja + ekspor lembar jadwal; T4 kendali**. T2 = sistem pendukung keputusan (rekomendasi diterapkan petugas secara manual).

### [T-39] 12:00 WIB — Jawaban user batch F (pengadaan, komputasi, sumber video, data latih)
- Pengadaan: **produk nol biaya sampai T3 selesai** (tanpa perangkat keras, lisensi, data/standar berbayar, sewa server/cloud); **biaya administrasi bisnis boleh** (merek, PT Perorangan, domain/email).
- Komputasi Vision Tracker: **laptop tim sampai T3** (T3 terbatas pada sedikit kamera, tidak 24 jam). Keputusan U-03 edge-light T2 otomatis gugur: edge/mini-PC pindah ke T4.
- Sumber video: **rekaman saja sampai ada MoU**, setidaknya sampai T2 selesai, paling lambat setelah T3 selesai. Implikasi desain: mode stream langsung T2 diuji dengan **rekaman yang diputar ulang sebagai stream** (server RTSP/HLS lokal dari file, mis. MediaMTX), tanpa stream Dishub.
- Data latih: **pra-label otomatis + koreksi manusia**; user meminta **panduan langkah demi langkah yang rinci dan paling hemat waktu**; **boleh mengorbankan ±5% akurasi di T1–T2** (target T1–T2 menjadi ±90% siang / ±85% malam-hujan), penalaan bertahap mulai T3 hingga target 95%/90%. → deliverable baru: panduan data latih Vision Tracker.

### [T-40] 12:15 WIB — Jawaban user batch G (lisensi AI, fitur lama, model T2, naskah TA)
- Lisensi model deteksi: **model berlisensi bebas (Apache-2.0/MIT)**, mis. RF-DETR/YOLOX/RTMDet + ONNX Runtime + ByteTrack; Ultralytics (AGPL) tidak dipakai.
- Fitur T2 lama: **pantauan & laporan ke T3** (CCTV live view, kesehatan kamera, tiket keluhan, laporan wajib berbasis data vision); **kendali ke T4** (kendali terpusat, alarm controller, edge di kabinet).
- Model T2: **perangkat lunak untuk engineer Dishub; awalnya diserahkan sebagai jasa kajian** yang dijalankan tim di laptop (Dishub memberi rekaman, tim menyerahkan dashboard & laporan).
- Naskah TA: **tidak ada yang dipush** (PDF, teks, maupun ringkasannya tetap lokal; dokumen planning merujuk tanpa kutipan rinci). Tindakan: `.gitignore` ditambah, entri log T-33 disunting agar tidak memuat identitas & rincian naskah (rincian dipindah ke catatan lokal R08 yang tidak dipush).

### [T-41] 12:30 WIB — Jawaban user batch H (rekaman T2, jadwal, nama tahap)
- Rekaman: idealnya seharian semua pendekat, tetapi **simulasi awal dimulai dari sampel terbatas satu simpang pada waktu puncak dan non-puncak, dengan kondisi pagi, malam, dan hujan**; data diusahakan lengkap untuk setiap lengan, **namun puncak/non-puncak dan pagi/malam/hujan bisa berasal dari simpang berbeda**, tergantung ketersediaan data di YouTube atau sumber lain yang dapat diakses. Implikasi: dukung "rekaman komposit" (klip per kondisi boleh dari simpang berbeda untuk uji akurasi); optimasi per simpang tetap memerlukan hitungan semua lengan pada periode yang sama; pengelompokan otomatis 8 jadwal baru aktif bila ada rekaman panjang, sebelum itu periode ditetapkan pengguna. Perlu kebijakan sumber YouTube (hak cipta/ToS).
- Jadwal: **tanpa tanggal, berbasis capaian** (kriteria kelulusan tiap tahap).
- Nama tahap disetujui: **T1 Purwarupa Hitung dan Rekomendasi; T2 Vision Tracker dan Optimasi Simpang; T3 Deteksi Kejadian dan Pemantauan Operasional; T4 Kendali Adaptif Terpadu; T5 Platform Mobilitas Kota.**

### [T-42] 12:45 WIB — Jawaban user batch I (YouTube, tempat pelatihan, urutan kelas) & rencana eksekusi revisi
- YouTube: **bebas dipakai untuk uji dan pelatihan** (keputusan user; risiko hak cipta/ToS dicatat di register risiko dengan mitigasi: register sumber dan pelatihan ulang dengan data berizin sebelum penjualan komersial skala besar).
- Tempat pelatihan: user bertanya apakah cloud gratis memungkinkan → **ya**: rekomendasi Kaggle Notebooks (GPU gratis, kuota mingguan) sebagai utama dan Google Colab (gratis) sebagai cadangan; tanpa biaya sehingga tidak termasuk pengadaan; data Dishub (setelah MoU) tetap dilatih di laptop. Rincian di panduan data latih.
- Kelas T1–T2: **6 kelas dulu** (motor, mobil termasuk angkot/pikap, bus, truk, kendaraan tak bermotor, pejalan kaki); **angkot & pikap menyusul di T3** bersama penalaan akurasi.
- Rencana eksekusi revisi (setelah semua keputusan terkumpul):
  1. Dokumen baru: `15_Spesifikasi_Vision_Tracker_dan_Optimasi_Simpang.md` (spesifikasi kedua modul T2, konfigurasi, 3 halaman dashboard, skema tabel, rantai PKJI 2023, mode optimasi, manfaat rupiah, laporan, validasi, peta jalan T1–T5) dan `16_Panduan_Data_Latih_Vision_Tracker.md` (langkah demi langkah hemat waktu, cloud gratis).
  2. Tulis ulang: `04` (tahapan), `14` (arsitektur per tahap + diagram pipeline high-level berpenanda tahap), `11` (pengadaan nol sampai T3), `13` (kebutuhan data).
  3. Revisi besar: `05` (re-tag tahap 141 fitur + epik baru E20–E23), `06` (stack vision, lisensi, strategi anti lock-in, diagram F00–F12 diperbarui), `01` (ringkasan tahap + Definisi Istilah).
  4. Revisi kecil: `03`, `08`, `09`, `10`, `12`, KB-10, START_HERE, README.
  5. Versi docx/PDF semua dokumen yang berubah (lokal), commit & push dokumen kanonis saja (naskah TA & docx tidak dipush).
  6. Paralel: fork menyusun draf Definisi Istilah dan panduan data latih.

> **Koreksi stempel waktu (dicatat 09:58 WIB).** Jam pada judul T-32 sampai T-42 adalah perkiraan dan tidak akurat. Menurut waktu modifikasi berkas di laptop (zona UTC+7), log ini terakhir disimpan pukul 03:15 WIB tanggal 2026-09-14 setelah T-42 ditulis, dan dokumen hasil T-43 sampai T-47 tersimpan antara 03:17 dan 03:30 WIB. Entri mulai T-43 memakai jam dari waktu modifikasi berkas atau jam sistem.

### [T-43] 03:17 WIB: Catatan lokal naskah tugas akhir (R08)
- Dibuat `docs/sources/_ringkasan/R08_Catatan_Lokal_Naskah_TA.md` (LOKAL, masuk .gitignore, tidak dipush sesuai keputusan T-40). Isinya rantai perhitungan simpang bersinyal di naskah (MKJI 1997), angka hasil yang dipakai sebagai uji regresi mode MKJI, dan pemetaan setiap langkah ke PKJI 2023.
- Dokumen planning hanya merujuk naskah secara umum ("naskah tugas akhir di docs/sources") tanpa judul, nama, NIM, atau kutipan angka.

### [T-44] 03:21 WIB: Dokumen baru 15 Spesifikasi Vision Tracker dan Optimasi Simpang
- Berkas: `docs/planning/15_Spesifikasi_Vision_Tracker_dan_Optimasi_Simpang.md`.
- Isi bagian Vision Tracker: posisi kedua modul per tahap; alur kerja pengguna; masukan; enam kelas rinci dan pemetaan otomatis ke PKJI/MKJI; proses; tabel keluaran hitung_15m, hambatan_samping_15m, status_lampu, antrian_1m, peristiwa (T3), mutu_rekaman; rumus hambatan samping berbobot per 200 m per jam; target akurasi T1-T2 sekitar 90% siang dan 85% malam atau hujan, T3 ke atas 95% dan 90%; kinerja di laptop; privasi; peta jalan.
- Isi bagian Optimasi: masukan; periode otomatis maksimal delapan jadwal atau manual; konversi SMP; rantai PKJI 2023 sepuluh langkah; enam mode (Webster/PKJI baku T1; tundaan terendah dengan batasan, minimalkan DJ tertinggi, siklus praktis minimum, pertahankan siklus eksisting T2; multi-kriteria berbobot T3); batas keselamatan; keluaran; validasi SUMO; manfaat rupiah (nilai waktu UMK, BBM saat diam, emisi); laporan otomatis; peta jalan.
- Wizard konfigurasi delapan langkah; dashboard tiga halaman (Ringkasan Simpang dan Rekomendasi; Arus Lalu Lintas dan Kapasitas; Kinerja Pendekat dan Kualitas Data); kriteria kelulusan T1 dan T2.

### [T-45] 03:24 sampai 03:27 WIB: Tulis ulang 04 dan re-tag 05
- `04_Konsep_Tahapan_1-5.md` ditulis ulang (revisi 2026-09-14). Prinsip P1 sampai P8: nol pengadaan sampai T3, lock-in minimal, transparan, standar Indonesia, manusia tetap memutuskan, satu simpang lalu banyak simpang mandiri lalu koridor di T5, minimisasi data, kreatif tetapi berpijak kebutuhan. Setiap tahap memuat tujuan, kriteria kelulusan, nilai, lingkup, infrastruktur, data, integrasi, kepatuhan, validasi, upaya, risiko, dan hal yang tidak dikerjakan. Ditambah tabel ITCS DKI vs T4 vs T5 dan pengadaan/komputasi per tahap.
- `05_Inventaris_Fitur_per_Tahap.md` di-re-tag dengan skrip scratchpad `retag_05.py`. ID fitur lama tetap; kolom Tahap menjadi acuan dan fitur yang pindah ditandai "**T#** (dulu T#)". Epik baru E20 Vision Tracker, E21 Optimasi Waktu Simpang, E22 Konfigurasi Simpang dan Data Statis, E23 Dashboard.

| Tahap | Fitur | Must | Should | Could |
|---|---|---|---|---|
| T1 | 13 | 13 | 0 | 0 |
| T2 | 33 | 26 | 6 | 1 |
| T3 | 42 | 20 | 20 | 2 |
| T4 | 62 | 34 | 20 | 8 |
| T5 | 29 | 7 | 11 | 11 |
| Total | 179 | 100 | 57 | 22 |

### [T-46] 03:20 sampai 03:24 WIB: Hasil dua fork (draf Definisi Istilah dan dokumen 16)
- Draf `docs/planning/_draft_definisi_istilah.md`: 143 istilah dalam tujuh kelompok (lalu lintas dan simpang; kinerja dan perhitungan; regulasi dan kelembagaan; kendali dan prioritas; vision dan AI; perangkat lunak dan infrastruktur; bisnis dan pengadaan). Sudah diperiksa. Istilah yang masih perlu ditambah saat digabung ke 01: GLOSA, SPaT, ICD, CRM, PWA, MapLibre, FastAPI, React, Keycloak, ONVIF, WebRTC, OER. Draf dihapus setelah digabung.
- `docs/planning/16_Panduan_Data_Latih_Vision_Tracker.md` berisi langkah A sampai I:
  - register sumber;
  - pengambilan bingkai tiap 2 sampai 3 detik dengan penyaringan duplikat;
  - pra-label di Kaggle dengan RF-DETR, ditambah OWLv2 untuk becak dan gerobak;
  - koreksi di Label Studio;
  - dua putaran active learning;
  - pelatihan RF-DETR Small atau YOLOX-tiny, lalu ekspor ONNX;
  - uji kecepatan di laptop;
  - rumus akurasi hitungan;
  - versi dataset.
- Dokumen 16 juga memuat jadwal tiga minggu (55 sampai 75 jam-orang), risiko termasuk YouTube, dan daftar periksa. Sudah diperiksa dan sesuai keputusan T-39 dan T-42.

### [T-47] 03:30 WIB: Draf bagian awal dokumen 06 (belum disisipkan)
- Disusun di scratchpad sebagai `06_head.md`. Isinya lapisan arsitektur, komponen per tahap, tabel teknologi beserta lisensinya, model data dan API, dan komputasi per tahap.
- Tabel lisensi dan strategi lock-in minimal:
  - Ultralytics (AGPL) tidak dipakai.
  - Redis versi baru diganti Valkey.
  - EMQX diganti Mosquitto atau NanoMQ.
  - Grafana dan Loki hanya dipakai sebagai alat terpisah tanpa modifikasi.
  - Fitur TimescaleDB berlisensi TSL bersifat opsional.
  - docxtpl diganti python-docx.
- Retensi video: rekaman 1080p sekitar 1,5 sampai 2 GB per jam per kamera. Karena itu rekaman diolah per batch, disimpan di disk eksternal, atau direkam 720p.
- Daftar ADR-01 sampai ADR-25. ADR baru:
  - ADR-19 model deteksi dan ONNX;
  - ADR-20 pipeline vision dan skema;
  - ADR-21 mesin PKJI dan mode;
  - ADR-22 kebijakan data rekaman;
  - ADR-23 tempat pelatihan;
  - ADR-24 pembuatan laporan;
  - ADR-25 pemeriksaan lisensi.

### [T-48] Sebelum jeda: Data diagram alur ditulis ulang untuk tahapan baru
- `docs/planning/diagram/make_diagrams.py` diperbarui:
  - nama tahap baru pada legenda;
  - lajur Pusat menjadi "laptop T1-T3, server T4+";
  - gambaran F00 diperbarui;
  - diagram baru A01 (arsitektur alur data dari CCTV sampai keputusan) untuk dokumen 14.
- Alur F01 sampai F12 disusun ulang:
  - F06 menjadi Vision Tracker dari rekaman sampai tabel hitungan;
  - F03 seluruhnya T4;
  - F08 deteksi di T3, layanan di T4, prioritas bersyarat di T5;
  - F09 bukti tanpa pelat di T3, ANPR dan API di T4;
  - F11 memakai SUMO sejak T2.
- Hasil render pertama diperiksa. Masalah yang ditemukan:
  - label legenda saling menimpa dan terpotong;
  - panah yang melompati kolom menembus kotak;
  - label "konfigurasi" menimpa blok Mode optimasi;
  - garis umpan balik "ukur ulang" melengkung melintasi seluruh A01;
  - label T2, T3, dan T4 di F06 jauh dari panahnya.
- Sesi terjeda dan konteks percakapan diringkas otomatis. Setelah jeda user menulis: "tolong lanjutkan secara hati-hati dan teliti".

### [T-49] 09:40 sampai 09:57 WIB: Mesin gambar diagram ditulis ulang dan semua gambar diperiksa
- **Perutean panah siku.** Garis hanya lewat celah antarkolom dan jalur tipis di tepi lajur. Setiap calon rute diberi skor menurut jumlah belokan, panjang, persilangan, dan garis yang menempel atau menumpuk dengan panah lain. Rute yang menembus kotak ditolak. Panah yang berbagi asal atau tujuan boleh bergabung. Rute juga harus menyediakan ruang label.
- **Tata letak kolom berlapis.** Satu kotak per sel, dan langkah awal ditarik ke dekat penerusnya. Diagram jadi lebih sempit dibanding satu kolom per langkah.
- **Legenda dan teks.** Jarak label legenda dihitung dari lebar teks terukur. Teks kotak dibungkus menurut lebar terukur. Label berkode tahap pada panah diberi warna tahap.
- **Koreksi tahap agar sesuai dokumen 05:**
  - F01: membaca nyala lampu adalah T2.
  - F05: status lampu dan antrian adalah T2.
  - F06: penyamaran video mulai T2. Tampilan dasar ada di T1 dan halaman kualitas data di T2. Panah edge T4 kini menuju tabel hitungan.
  - F08 dan F09: pengenalan kendaraan prioritas dan deteksi pelanggaran dipindah ke lajur Pusat karena dijalankan Vision Tracker.
- **A01 dirancang ulang.**
  - Konfigurasi simpang, dari formulir di T1 dan wizard di T2, masuk kolom Data sehingga panah balik "konfigurasi" hilang.
  - Kolom Data mendapat blok Peristiwa kejadian (T3). Jalur kejadian (T3) berjalan di bawah kolom langsung ke Konsol pemantauan tanpa melalui optimasi.
  - Umpan balik uji sebelum-sesudah (T3, garis putus-putus) keluar dari sisi kanan dan kembali ke Sumber video lewat bawah.
  - Keputusan Kepala Dinas ditetapkan T2. Mode MKJI 1997 ditandai T2.
  - Koordinasi koridor (T5) ada di kolom Tindak lanjut.
- **Markdown hasil skrip.** Bagian diagram di 06 kini berjudul "## 9." karena nomor 8 dipakai daftar ADR. Versi sederhana memakai penanda halaman baru sebelum F01 sampai F12.
- **Verifikasi.** Ke-14 gambar (F00 sampai F12 dan A01) dibuka satu per satu. Tidak ada garis yang menembus kotak, tidak ada label yang menimpa, dan legenda terbaca penuh. Cadangan skrip lama ada di scratchpad sebagai `make_diagrams_backup_preroute.py`.

### [T-50] 10:05 WIB: Dokumen 06 dirakit ulang; satu koreksi di 05
- `06_Arsitektur_Konseptual_dan_Opsi_Teknologi.md` sekarang terdiri dari bagian 1 sampai 8 hasil revisi (draf T-47) dan bagian 9 diagram alur hasil skrip. Cadangan versi lama ada di scratchpad (`06_backup_sebelum_splice.md`). Skrip perakit: `splice_06.py` di scratchpad.
- Koreksi pada draf sebelum dirakit, setelah dicek silang ke `05`:
  - Pemeliharaan berkala adalah T3 (F-T1-03), bukan T4.
  - Aduan kota (CRM) masuk integrasi T3 (F-T2-52).
  - Kalibrasi twin per simpang masuk T3, dan mode bayangan masuk T4.
  - Tabel teknologi diberi catatan bahwa lisensi bobot tiap varian RF-DETR tetap diperiksa lewat ADR-19, sama dengan catatan di `16`.
- Daftar ADR diberi kolom "isi pokok" agar rincian daftar lama tidak hilang. Rincian itu mencakup perintah terbatas dan transaksi, urutan validasi, kontrol keamanan, dan contoh target SLO. Beberapa isi diperbarui:
  - ADR-09 kini berisi actuated, pemilihan program, dan offset dasar di T4, sedangkan max-pressure jaringan pindah ke T5.
  - ADR-10 berlaku sejak T2 karena validasi SUMO dimulai di T2.
  - ADR-13 mencatat bahwa kolom tenant disiapkan sejak skema T1.
- Semua tautan gambar di 06 dan bagian A01 diperiksa dan mengarah ke berkas yang ada.
- `05`: F-T3-107 diubah dari "Kalibrasi twin per koridor" menjadi "Kalibrasi twin per simpang (koridor menyusul)". Ini selaras dengan F11 dan keputusan koridor di T5, dengan offset dasar di T4.

### [T-51] 10:10 WIB: Dokumen 14 ditulis ulang untuk tahapan baru
- `14_Arsitektur_per_Tahap.md` ditulis ulang total, dan cadangan versi lama ada di scratchpad. Bagian 1 adalah diagram A01, arsitektur alur data dari CCTV lewat Vision Tracker, data terstruktur, optimasi, dan penyajian sampai tindak lanjut. Setiap blok mencantumkan teknologinya dan penanda tahap T1 sampai T5. Bagian ini juga menjelaskan cara membaca penanda tahap, jalur kejadian T3, umpan balik uji sebelum-sesudah, tabel komponen dan teknologi, serta versi mermaid. Isinya diambil otomatis dari `diagram/_bagian_pipeline.md`.
- Bagian 2 berisi lima lapisan dan aturan yang berlaku sejak T1: tanpa pengadaan sampai T3, keputusan di tangan manusia, lampu tetap bekerja bila pusat mati mulai T4, angka dapat ditelusuri, data hemat, dan standar terbuka.
- Bagian 3 sampai 7 berisi satu bagian per tahap. Tiap bagian memuat gambaran singkat, susunan lapisan, alur data, alasan susunan, serta ukuran dan komputasi, dengan isi sesuai `04`.
- Bagian 8 berisi tabel ringkasan lapisan, peran sistem, dan pengadaan per tahap. Bagian 9 berisi hal yang tidak berubah sepanjang tahap. Bagian 10 berisi register risiko arsitektur yang diperbarui, termasuk akurasi vision, rekaman terbatas, keterbatasan laptop, ukuran video, hak cipta video publik, lisensi pustaka, dan MoU.
- Isi versi lama yang tidak berlaku lagi dibuang: edge ringan di T2, pelat dan adaptif koridor di T3, serta max-pressure di T4.

### [T-52] 10:20 WIB: Dokumen 11 Kebutuhan Pengadaan ditulis ulang
- `11_Kebutuhan_Pengadaan_per_Tahap.md` ditulis ulang mengikuti keputusan T-39: produk nol biaya sampai T3 selesai, biaya administrasi bisnis boleh. Cadangan versi lama ada di scratchpad (`11_backup.md`).
- Isi:
  1. Ringkasan per tahap.
  2. Barang tanpa biaya sampai T3: laptop, perangkat lunak berlisensi bebas, GPU gratis, GitHub, standar gratis, NTCIP bila gratis, peta dan citra tanpa biaya, ponsel, TLS dan WireGuard, dokumentasi terbuka.
  3. Biaya administrasi yang diperbolehkan: merek, PT Perorangan, domain dan email, templat NDA, DPIA, lisensi open-core, TKDN, klausul tanggung jawab.
  4. Rencana lama yang ditunda ke T4 beserta cara menutup celahnya: edge ringan, controller uji, kamera IP uji, Jetson, UPS, server pilot, VM demo, GPU berbayar, NEMA, HCM, data probe.
  5. Pengadaan mulai T4.
  6. SDM tanpa biaya.
  7. Urutan berbasis capaian.
  8. Risiko keputusan nol pengadaan, termasuk laptop sebagai titik tunggal kegagalan, kuota GPU, kinerja, dan ruang disk.
- Perkiraan kas sampai T3 dihitung ulang dari rincian: merek dua kelas Rp 1 sampai 3,6 juta, domain Rp 0,15 sampai 0,4 juta, email Rp 0 sampai sekitar 1,7 juta per tahun untuk dua pengguna, dan PT Perorangan Rp 0,05 sampai 0,3 juta. Totalnya sekitar Rp 1 sampai 6 juta pada tahun pertama.

### [T-53] 10:23 WIB: Dokumen 13 Kebutuhan Data ditulis ulang
- `13_Kebutuhan_Data_per_Tahap.md` ditulis ulang. Cadangan versi lama ada di scratchpad (`13_backup.md`).
- Aturan pengumpulan:
  - hanya rekaman sampai ada MoU;
  - video publik boleh untuk uji dan pelatihan dengan register sumber;
  - mulai dari sampel terbatas;
  - uji akurasi boleh memakai simpang berbeda, tetapi optimasi memerlukan semua lengan pada periode yang sama;
  - aturan privasi;
  - hemat ruang disk.
- T1 dirinci presisi dalam sembilan butir data:
  - register sumber;
  - rekaman simpang target;
  - klip data latih sesuai `16`;
  - klip uji per kondisi;
  - hitungan manual referensi;
  - data simpang;
  - geometri;
  - waktu lampu eksisting;
  - contoh perhitungan resmi.
- T2 dirinci presisi dalam sepuluh butir data:
  - rekaman satu simpang lengkap pada periode yang sama;
  - klip malam dan hujan;
  - hitungan manual per kondisi dengan arah gerakan;
  - zona hambatan samping;
  - area kepala lampu;
  - jaringan simulasi;
  - parameter ekonomi;
  - parameter kebijakan;
  - studi lama untuk uji regresi MKJI, yaitu naskah lokal yang tidak dipush;
  - jawaban kuesioner.
- T3 sampai T5 berupa perkiraan. AVL bus pindah ke T4 karena prioritas bus ada di T4. MFD dan perimeter pindah ke T5. Floating car dan survei koridor dari versi lama dibuang dari T1.
- Data ini dihapus dari versi lama karena tidak lagi sesuai T1: daftar koridor 3 sampai 5 simpang, floating car, dan inventaris aset (sekarang T3).
- Pemeriksaan otomatis jumlah kolom tabel di semua dokumen planning dan log tidak menemukan masalah. Satu rumus yang memuat karakter pemisah tabel di 13 sudah ditulis ulang dalam kata-kata sebelum pemeriksaan.

### [T-54] 10:36 WIB: Dokumen 01 diperbarui dan bagian 8 Definisi Istilah ditambahkan
- Bagian 1 sampai 7 di `01_Visi_Produk_dan_Positioning.md` diselaraskan dengan tahapan baru. Cadangan versi lama ada di scratchpad (`01_backup.md`), dan skrip perakitnya adalah `build_01.py`.
  - Pernyataan visi kini dimulai dari CCTV yang sudah ada menjadi hitungan dan rekomendasi waktu sinyal PKJI 2023.
  - Nilai inti: controller dibaca mulai T3 dan dikendalikan mulai T4; T1 sampai T3 tanpa pengadaan; T2 dijual sebagai jasa kajian. Ditambah nilai kedelapan, lisensi bebas dan lock-in minimal.
  - Positioning disesuaikan per tahap. Tabel perbedaan dengan ITCS DKI mendapat baris baru tentang perangkat dan lisensi.
  - Tabel ringkasan tahapan memakai nama dan isi baru dari `04`.
  - Ukuran sukses ditambah target akurasi Vision Tracker dan kajian tanpa survei hitung manual penuh. Uji tundaan kini pada simpang pilot di T3, bukan koridor.
- Bagian 8 Definisi Istilah dibuat dari draf fork T-46 dengan 215 istilah dalam tujuh kelompok, diurutkan abjad di setiap kelompok.
- Koreksi pada draf:
  - Entri lisensi diganti karena menyatakan IRAMA hanya memakai Apache atau MIT, padahal ada komponen BSD, EPL, dan MPL. Entri baru menjelaskan lisensi permisif, copyleft lemah, GPL/AGPL, dan SSPL/BSL/RSAL.
  - Akurasi kini memuat target malam dan hujan.
  - BOK di T2 kini dijelaskan sebatas BBM saat diam.
  - Klaim max-pressure dilunakkan.
  - RF-DETR tidak lagi disebut "terbaru", dan pemeriksaan lisensi bobot disebutkan.
  - MVP disesuaikan: T1 purwarupa, T2 versi pertama yang dijual.
- 73 istilah ditambahkan, termasuk 12 yang sebelumnya dicatat kurang (GLOSA, SPaT, ICD, CRM, PWA, MapLibre, FastAPI, React, Keycloak, ONVIF, WebRTC, OER). Sisanya ditemukan lewat pemindaian otomatis singkatan di dokumen 01, 03, 04, 05, 06, 08, 11, 13, 14, 15, dan 16, misalnya UMK, DLH, Bapenda, NDA, detektor virtual, Kaggle, Colab, OWLv2, penyamaran, register sumber, dan jasa kajian.
- Makna singkatan yang jarang dicek pada konteksnya lebih dulu. Contohnya, PDN di `03` berarti produk dalam negeri, dan OER di `05` berarti Octet Encoding Rules pada NTCIP. TDBU tidak dimasukkan karena maknanya tidak dapat dipastikan dari dokumen.
- Draf `_draft_definisi_istilah.md` dipindahkan dari repositori ke scratchpad setelah digabung.

### [T-55] 10:50 WIB: Revisi kecil dokumen 03, 05, 07, 08, 09, 10, 12, KB-10, dan START_HERE
- Cara kerja: kata kunci tahapan lama (misalnya "Lihat & Kelola", edge-light, "siap jual", max-pressure di T4, pelat di T3) dipindai di semua dokumen. Isi yang tertinggal diubah lewat skrip `minor_updates.py` di scratchpad. Setiap penggantian dicek tepat satu kali, dan berkas baru ditulis bila semua cek lolos. Cadangan versi sebelumnya ada di scratchpad (`backup_minor/`).
- `03`:
  - Proposisi nilai disesuaikan: CCTV dan controller eksisting, tanpa pengadaan sampai T3, serta validasi bertahap.
  - Model bisnis baru "jasa kajian waktu sinyal per simpang" (T2, sesuai keputusan T-40). Tahap model lain disesuaikan: paket koridor ke T4 sampai T5, ATSPM ke T3 sampai T4, B2B2G ke T3 sampai T4.
  - Go-to-market kini dimulai dari satu simpang Bandung dan jasa kajian, lalu MoU sebelum T3.
- `05`: F-T3-116 (tata kelola PDP) sebelumnya bergantung pada F-T3-99 yang sudah pindah ke T4. Isinya kini retensi video dan klip untuk data Dishub di T3, dependensinya F-T2-151, dan aturan pelat menyusul di T4.
- `07`: nama tahap baru dipakai. Kolom "Dilayani sejak" untuk dua belas persona dan kolom tahap pada linimasa hari operator diperbarui, misalnya operator mulai T3, teknisi T3, bus T4, dan DPRD T2.
- `08`:
  - Asumsi A-02, A-04, A-05, A-17, dan A-18 direvisi. Asumsi baru A-20 sampai A-23: video publik, GPU gratis, sampel dari simpang berbeda, dan penerimaan engineer.
  - Mitigasi risiko R-01, R-04, R-06, R-07, dan R-14 direvisi. Risiko baru R-15 sampai R-22: akurasi vision, hak cipta video publik, laptop, lisensi, sampel tidak mewakili, kuota GPU, perbedaan PKJI dan SUMO, dan MoU tertunda.
  - Catatan status Q-01 sampai Q-13 ditambahkan.
  - D-04, D-05, dan D-10 direvisi: adaptif per simpang di T4, max-pressure di T5, prioritas bus bersyarat di T5, dan deployment dimulai dari satu simpang.
- `09`: tabel masukan ditambah dokumen 11 sampai 16 dan Definisi Istilah. Status keputusan, keluaran planning 10 dan 11 (spesifikasi T2 serta data dan pelatihan), rencana V&V, dan urutan kerja disesuaikan.
- `10`:
  - Checklist A (sumber data dan stack) diperbarui.
  - Struktur repositori B ditulis ulang: services/vision, optimizer, reports, metrics, cai, priority, adaptive, edge di T4, dan sim satu simpang.
  - C: CI kini mencakup pemeriksaan lisensi, uji regresi PKJI, vision-smoke, dan sim-smoke. Skema data T1 dan T2. Daftar ADR sebelum sprint 1.
  - D (data sebelum sprint 1) dan E (MoU menjelang T3) diperbarui.
- `12`:
  - Tujuan internal diperbarui.
  - Empat pertanyaan rekaman kamera ditambahkan di akhir bagian D (nomor 21 sampai 24): lokasi dan lama simpan rekaman, cara menyalin, kejelasan pandangan tiap pendekat, dan akses dari luar.
  - Bagian E sampai G dinomori ulang menjadi 25 sampai 32. G kini memuat uji di satu atau beberapa simpang dan kesediaan mencoba jadwal hasil kajian.
  - Pertanyaan vendor H8 tentang ekspor MP4 dan RTSP ditambahkan.
  - Tabel asumsi disesuaikan dengan T4 dan U-08 yang direvisi, ditambah asumsi retensi NVR.
- KB-10:
  - D-08, D-09, D-10, D-16, dan D-20 diberi tanda revisi.
  - U-03, U-05, U-06, dan U-08 dicoret atau dilengkapi.
  - Bagian baru B2 berisi keputusan user 2026-09-14 U-09 sampai U-29, ditambah baris DOC tentang versi docx/PDF lokal.
  - Q-03 dan Q-08 diberi catatan. Pertanyaan riset baru Q-12 sampai Q-15: lisensi bobot RF-DETR, citra satelit tanpa biaya, rekaman satu simpang lengkap, dan digitalisasi grafik PKJI.
- START_HERE:
  - Tanggal dan ringkasan proyek diperbarui, begitu pula inti produk T1 dan T2, pola recording-first, urutan baca yang kini mencakup 15, 16, 14, dan istilah, peta folder (planning 01 sampai 16, diagram, docx lokal, R08 lokal), serta konvensi ADR-01 sampai ADR-25 dengan nama tahap baru.
  - Lembar fakta ditambah EMP, hambatan samping, akurasi, laptop, ukuran video, dan lisensi dilarang.
  - Tiga workaround ditambahkan: diagram, docx, dan jam log dari jam sistem. Tindak lanjut terbaru juga dicatat.
- `docs/kb/02_Lembar_Rumus.md`: tiga baris rumus (C2, D2, D9) memuat tanda nilai mutlak "|" yang memecah tabel. Tanda itu di-escape tanpa mengubah isi rumus. Masalah ini sudah ada sejak commit awal dan ditemukan lewat pemeriksaan tabel otomatis.
- Pemeriksaan tabel otomatis di semua dokumen planning dan KB tidak menemukan masalah lagi. Penomoran kuesioner juga dicek: 1 sampai 32 berurutan, dan vendor 1 sampai 8.

### [T-56] 10:54 WIB: Kerangka kode dan README utama diselaraskan
- `git mv services/kpi-pkji services/optimizer` dan `git mv services/atspm services/metrics` dijalankan agar nama folder sama dengan dokumen 06 dan diagram. Folder baru `services/vision` dan `services/reports` dibuat.
- README kerangka diperbarui: .github, apps/api, apps/tmc-web, edge (kini T4 dengan catatan tanpa edge sebelum T4), infra, packages, services/adaptive (tanpa max-pressure), cai (baca-saja T3, kendali T4), metrics, optimizer, priority, reports, vision, sim (satu simpang), dan tests (uji akurasi vision).
- `README.md` utama ditulis ulang. Isinya ringkasan produk, status 2026-09-14, tabel tahapan baru, titik mulai baca (termasuk 15, 14, 13, dan Definisi Istilah), struktur (planning 01 sampai 16, ADR-01 sampai ADR-25), catatan lisensi dengan pemeriksaan lisensi di CI, serta catatan bahwa berkas kerja docx/PDF dan catatan pribadi hanya lokal.

### [T-57] 11:00 WIB: Judul diagram berpola "dari X sampai Y" diganti; putaran rute ulang
- Aturan gaya user melarang judul berpola "dari X ke Y". Dua judul melanggarnya dan kini diganti dengan judul teknis yang deskriptif:
  - F06 menjadi "Pipeline Vision Tracker dan keluaran tabel hitungan".
  - A01 menjadi "Arsitektur alur data IRAMA per komponen, teknologi, dan tahap".
  - Judul bagian 1 dokumen 14 menjadi "Arsitektur alur data, komponen, dan teknologi (A01)".
  - Nama berkas gambar menjadi `A01_Arsitektur_Alur_Data.png` dan `F06_Pipeline_Vision_Tracker_dan_keluaran.png`. Potongan nama berkas kini berhenti di batas kata.
- Pemeriksaan gambar dekat menemukan persimpangan ambigu di A01. Panah "Hambatan samping" ke tabel data dan panah "Kejadian" ke tabel peristiwa bertemu di satu titik belok. Penyebabnya perutean serakah, sehingga ditambahkan putaran rute ulang: setiap panah dilepas lalu dirutekan lagi terhadap panah lain, dan rute baru dipakai hanya bila skornya lebih baik. Hasilnya, ketiga panah Vision Tracker ke Data kini bersarang rapi.
- Ke-14 gambar dibuka ulang satu per satu dan semuanya bersih. Dokumen 06 dan 14 dirakit ulang, dan semua tautan gambar dicek masih mengarah ke berkas yang ada.
- Versi sederhana bagian A01 kini diberi penanda halaman mendatar sebelum gambar dan kembali tegak setelah tabel.

### [T-58] 11:05 WIB: Perbaikan pembuat docx (`build_docx.py`, lokal)
- Substitusi tautan markdown ternyata berisi karakter kontrol 0x01 akibat kesalahan escape di sesi sebelumnya. Akibatnya teks tautan bisa hilang atau XML Word rusak. Substitusi kini memakai `\1`.
- Penanda baru `<<<PORTRAIT>>>` ditambahkan untuk kembali ke halaman tegak setelah `<<<LANDSCAPE>>>`.
- Daftar bernomor kini memakai nomor dari sumber dengan indentasi gantung. Gaya "List Number" bawaan melanjutkan nomor dari daftar sebelumnya.
- Tinggi gambar dibatasi agar muat di halaman, penting untuk diagram di halaman mendatar.
- Lebar kolom tabel kini dihitung dari panjang teks rata-rata tiap kolom, tidak lagi dari preset per jumlah kolom.
- Cadangan versi sebelumnya ada di scratchpad (`build_docx_backup.py`).

### [T-59] 11:20 WIB: Sumber docx sederhana 05, 15, dan 16 lewat fork; perbaikan kanonis dari temuan fork
- Tiga fork menulis sumber docx sederhana untuk 05 (inventaris fitur, hitung ulang cocok: 179 fitur, 100 Must, 57 Should, 22 Could), 15 (spesifikasi T2), dan 16 (panduan data latih, semua langkah dan perintah dipertahankan). Ketiganya dicek otomatis: tanpa em-dash, tanpa en-dash, tanpa pola "bukan", dan tabel konsisten.
- Temuan fork diperbaiki di dokumen kanonis:
  - `15`: FFmpeg diberi label LGPL sebagai program terpisah (sebelumnya tertulis Apache-2.0). Rujukan "Diagram alur dari CCTV sampai dashboard" diganti "Diagram arsitektur alur data (A01)".
  - `16`: penundaan penyamaran ke T3 dijelaskan hanya berlaku untuk frame data latih; cuplikan produk tetap disamarkan sejak T2 (F-T2-151). Disk eksternal hanya dipakai bila sudah dimiliki, dan cadangan tanpa pembelian memakai register sumber serta tautan unduh ulang. Total jam kerja disamakan dengan anggaran rinci, yaitu sekitar 55 sampai 76 jam orang.
  - `05`: dependensi dirapikan.
    - Rujukan ke ID yang tidak ada (F-T2-56, F-T2-25, F-T3-56, F-T3-102) diganti ID yang benar.
    - Fitur yang bergantung pada fitur di tahap lebih lambat kini merujuk sumber data yang tersedia di tahapnya, misalnya nyala lampu kamera F-T2-148, antrian dasar F-T2-149, tabel hitungan F-T1-144, rekomendasi F-T1-160, kesehatan kamera F-T3-154, dan kecepatan antarkamera F-T3-157.
    - Deskripsi F-T1-10, F-T1-64, F-T2-51, F-T2-59, F-T2-62, F-T2-66, F-T3-53, F-T3-60, F-T3-131, dan F-T2-49 disesuaikan. Sel tahap F-T4-125 dirapikan.
- Pemeriksaan dependensi otomatis atas 179 fitur kini tidak menemukan masalah. Pemeriksa ini juga menemukan lima masalah yang tidak dilaporkan fork. Jumlah fitur per tahap dan MoSCoW tidak berubah.
- Sumber sederhana 05 dan 16 diselaraskan dengan perbaikan tersebut.

### [T-60] 11:40 WIB: Sumber docx sederhana untuk semua dokumen yang berubah (lokal, tidak dipush)
- Sumber sederhana di `docs/planning/docx/src/` (untuk pembaca strategi IT, mengikuti aturan gaya user) diperbarui sebagai berikut:
  - **Ditulis ulang:** 01 (bagian naratif, lalu Definisi Istilah 215 istilah diambil dari kanonis dengan rentang angka ditulis "sampai"), 04, 06, 08, 09, 10, 11, dan 13.
  - **Dirakit dari bagian kanonis dan hasil skrip:**
    - 06: bagian awal ditambah diagram versi sederhana di halaman mendatar.
    - 14: bagian A01 versi sederhana ditaruh di halaman mendatar lalu kembali tegak. Bagian 2 sampai 10 diambil dari kanonis dengan nomor bagian dibuang dan label diubah menjadi awalan tebal. "Mengapa disusun begini" menjadi "Alasan susunan", rujukan nomor dokumen diganti nama dokumen, dan tabel ringkasan enam kolom ditaruh di halaman mendatar.
  - **Ditambal:** 03 (proposisi nilai, model bisnis jasa kajian, tahap model lain, urutan masuk pasar, pilot satu simpang), 07 (kolom tahap persona dan linimasa), dan 12 (pertanyaan rekaman 21 sampai 24, penomoran 1 sampai 32, pertanyaan uji jadwal, pertanyaan vendor 8, dugaan awal).
  - **Lewat fork (T-59):** 05, 15, dan 16. Dokumen 02 tidak berubah.
- Temuan saat menulis versi sederhana diperbaiki juga di kanonis:
  - A-10 di `08` dan jalur swakelola di `03` tidak lagi menyebut pilot 3 sampai 5 simpang.
  - Risiko baru R-23 (tim tanpa teknisi lapangan, T4) ditambahkan di `08`, sehingga nomor risiko kanonis dan versi sederhana sama.
  - Entri "Uji di meja" di Definisi Istilah tidak lagi memakai pola "X, bukan Y".
- Pemeriksaan otomatis atas 16 sumber sederhana tidak menemukan em-dash, en-dash, pola "bukan", judul berpola "dari X ke Y", judul berbentuk pertanyaan, maupun tabel rusak.

### [T-61] 11:49 WIB: Pembuat docx diperkuat, lalu docx dan PDF dibangun ulang dan diperiksa
- Perbaikan tambahan di `build_docx.py`:
  - Blok kode dengan baris kosong dan kutipan tidak lagi membuat pembuat berhenti.
  - Lebar kolom tabel kini punya batas bawah dari kata terpanjang dan lebar minimum absolut sekitar 0,18 cm per huruf ditambah bantalan sel, sehingga kata tidak terpotong di tengah.
- Build penuh dijalankan tiga kali; yang terakhir berlaku. Hasilnya 16 docx, 16 PDF arsip, dan 16 PDF terkunci. Sandi baru disimpan di `PASSWORD_LOKAL.txt` (lokal). Sandi tidak ditulis di log karena log dipush.
- Verifikasi tampilan: halaman contoh dari 01, 04, 05, 06, 11, 12, 13, 14, dan 16 dirender ke gambar lalu diperiksa.
  - Di 14, A01 tampil di halaman mendatar 2 sampai 3, lalu kembali tegak, dan tabel ringkasan tampil mendatar di halaman 8.
  - Di 06, diagram F00 sampai F12 tampil mendatar.
  - Daftar bernomor mulai dari 1 di setiap bagian, blok kode rapi, dan tabel tidak lagi memotong kata.
- Verifikasi PDF terkunci: ke-16 berkas terenkripsi AES-256 (V5, R6, AESV3), sandi salah ditolak, sandi baru membuka berkas, dan tanda air "RAHASIA IRAMA | untuk rekan tim | berlaku s.d. 17-09-2026" ada. Izin cetak, ubah, dan salin dimatikan.
- Berkas docx, PDF, dan sumber sederhana tetap lokal, di `.gitignore`, dan tidak dipush.

### [T-62] 11:55 WIB: Commit dan push dokumen kanonis; pembaruan memori
- Sebelum commit dilakukan dua pemeriksaan:
  - Semua berkas yang akan dipush dipindai. Tidak ada nama atau NIM penulis naskah, judul naskah, email user, maupun sandi PDF lama atau baru.
  - Status abaikan dicek. Naskah, teks ekstraksi TA, R08, folder docx, dan berkas sandi semuanya di-.gitignore.
- Commit `90f3e5c` (76 berkas, 4.470 baris ditambah, 1.921 dihapus) dipush ke `origin/main`, termasuk 14 objek LFS. Setelah push, daftar berkas terlacak (407 berkas) diperiksa ulang dan tidak memuat berkas terlarang.
- Memori sesi diperbarui:
  - `itcs-project-context` berisi tahapan baru, keputusan 2026-09-14, dokumen 14 sampai 16, aturan tidak dipush, dan workaround heredoc serta jam log.
  - `user-writing-and-sharing-preferences` berisi cara bertanya keputusan lewat pilihan ganda 4 ditambah jawaban terbuka, larangan judul "dari X ke Y" termasuk diagram, dan larangan push naskah TA.
- START_HERE langkah 1 kini merujuk bagian status terbaru log (bagian 9).

## 9. Status Akhir Sesi 2026-09-14 dan Langkah Berikutnya

**Selesai pada mandat 2026-09-14:**
- Seluruh keputusan batch A sampai I (T-34 sampai T-42) sudah diterapkan ke dokumen.
- Dokumen baru `15` (spesifikasi Vision Tracker dan Optimasi Simpang) dan `16` (panduan data latih).
- Ditulis ulang: `04`, `11`, `13`, dan `14`. Dokumen `14` kini dibuka dengan A01, diagram arsitektur alur data per komponen, teknologi, dan penanda tahap T1 sampai T5.
- `06` dirakit ulang, `05` di-re-tag dengan dependensi yang sudah divalidasi, dan `01` ditambah Definisi Istilah.
- Revisi kecil diterapkan pada `03`, `07`, `08`, `09`, `10`, `12`, KB-00, KB-02, KB-10, README, dan README kerangka.
- Diagram F00 sampai F12 dan A01 digambar ulang dengan perutean siku dan diperiksa satu per satu.
- Versi docx dan PDF terkunci untuk ke-16 dokumen dibangun ulang dan diperiksa. Berkasnya lokal dengan sandi baru di `docs/planning/docx/PASSWORD_LOKAL.txt`, berlaku sesuai kesepakatan sampai 17-09-2026.

**Yang perlu disiapkan user berikutnya (rincian di `13`):**
- Register sumber rekaman.
- Rekaman semua pendekat satu simpang, minimal 1 jam puncak dan 1 jam non-puncak siang.
- Klip data latih: dua puncak, satu non-puncak, satu malam, dan satu hujan.
- Satu klip uji per kondisi beserta hitungan manual per 15 menit.
- Geometri tiap pendekat.
- Fase dan waktu lampu eksisting.
- Cek merek IRAMA di PDKI dan ketersediaan domain (Rp 0).

**Langkah teknis berikutnya:**
- Planning rinci T1: ConOps dan SRS T1 sampai T2, backlog sprint.
- ADR prioritas: ADR-01, 02, 03, 15, 19, 20, 21, 22, dan 25.
- Penyiapan data latih mengikuti `16`.
- Menjawab pertanyaan riset Q-12 sampai Q-15 di KB-10: lisensi bobot RF-DETR, citra satelit tanpa biaya, rekaman satu simpang lengkap, dan digitalisasi grafik PKJI.

**Catatan untuk sesi berikutnya:**
- Jam log diambil dari jam sistem.
- Skrip panjang ditulis lewat Write tool karena heredoc mengubah garis miring terbalik.
- Setelah mengubah data diagram, jalankan `make_diagrams.py`, lalu perbarui 06 dengan mengganti bagian 9 memakai isi `diagram/_bagian_diagram.md`, dan 14 dengan mengganti bagian 1 memakai isi `diagram/_bagian_pipeline.md`. Skrip bantu perakitan sesi ini ada di scratchpad dan tidak tersimpan permanen.
