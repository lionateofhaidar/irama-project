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
