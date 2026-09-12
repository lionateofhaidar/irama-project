# 03 — Peta Regulasi & Kepatuhan (untuk desain ITCS)

**Cara pakai file ini**
- Bagian A: tabel per regulasi (pasal → isi → implikasi aplikasi → tahap T1–T5). Tahap: T1 MVP (monitoring, inventaris, manajemen plan/TOD), T2 siap jual (koordinasi, KPI PKJI/PM 96, pelaporan), T3 transisi adaptif (detektor, actuated/cyclic MP, TSP dasar), T4 setara ITCS (AI/ANPR, ETLE-integration, EVP, digital twin), T5 end-state (ERP/KRE, C2C multi-agensi, CV).
- Bagian B: matriks kepatuhan ringkas (kebutuhan C-01…C-43; C-01…C-35 identik dengan R05 §G.1 = penomoran kanonis). Bagian C: siapa berwenang untuk apa.
- Nomor pasal PM 49/2014 adalah rekonstruksi (label pasal hilang saat ekstraksi) [R05 A.4]. Verifikasi ke `docs/sources/_teks_ekstraksi/`.
- Sumber utama: R05 (regulasi), R00 B–H (bacaan langsung PM 49, PM 76, PM 96, Pergub 68, Dirjen 273, SK 7234), teks UU PDP & Pergub ganjil-genap.

## A. Tabel per regulasi

### A.1 UU 22/2009 tentang LLAJ
| Pasal | Isi ringkas | Implikasi untuk aplikasi | Tahap |
|---|---|---|---|
| 1 angka 19, 29, 34 | Definisi APILL, MRLL, SIK LLAJ | Terminologi resmi di UI/dokumen [R05 A.1] | T1 |
| 7(2), 9, 12 | Kemenhub: sarana-prasarana & MRLL; **Polri: registrasi, penegakan hukum, operasional MRLL, pusat kendali SIK LLAJ, pengumpulan/penyajian data** | ITCS = subsistem Dishub; wajib jalur data & kendali ke Polri; tidak boleh mengklaim fungsi operasional/penegakan Polri | T1 (desain) |
| 13, 321 | Forum LLAJ koordinasi antarinstansi | Laporan MRLL ke Forum; entitas stakeholder | T2 |
| 25–28, 275 | Jalan wajib berperlengkapan (APILL, alat pengawasan); dilarang mengganggu fungsi; sanksi | Inventaris aset; log gangguan/vandalisme | T1 |
| 93–94 | MRLL: 8 cara (termasuk pengendalian simpang & ruas); 5 kegiatan; perencanaan memuat identifikasi masalah, arus, daya tampung, pelanggaran & kecelakaan, LOS | Modul perencanaan & data survei; penetapan LOS | T1–T2 |
| 95, 102 | Kebijakan lalu lintas via Permen/Perda dan dinyatakan dengan APILL/rambu/marka; pemasangan ≤60 hari; **berlaku mengikat 30 hari setelah pemasangan** | Atribut tanggal pasang & tanggal berlaku hukum per aset | T1 |
| 96(3)–(4), 97 | Gubernur bertanggung jawab MRLL jalan provinsi setelah rekomendasi instansi; Kapolri bertanggung jawab optimalisasi operasional & pengawasan; Polri boleh MRLL sementara saat situasional | Workflow rekomendasi; mode "operasional Polri" tercatat | T2 |
| 98 | Penanggung jawab MRLL wajib analisis, evaluasi, laporan berbasis data & kinerja ke Forum LLAJ | Modul laporan kinerja periodik | T2 |
| 103 | APILL perintah/larangan diutamakan atas rambu/marka; saat gridlock **kotak kuning diutamakan** atas APILL | Logika gridlock / kotak kuning | T3 |
| 104, 282 | Perintah petugas Polri diutamakan atas APILL | **Mode manual/override petugas** dengan log | T1 |
| 106(4)c, 287(2) | Pengemudi wajib patuh APILL; sanksi kurungan ≤2 bulan/denda ≤Rp500 rb | Bukti pelanggaran → Polri | T4 |
| 133 | MKLL: kriteria V/C, angkutan umum, lingkungan; retribusi pengendalian (ERP); evaluasi berkala | Data pendukung TDM/ERP | T5 |
| 134–135(3) | Kendaraan hak utama; APILL tidak berlaku bagi mereka | Preemption/priority darurat | T3–T4 |
| 245–247 | SIK LLAJ terpadu oleh Pemerintah/provinsi; **pusat kendali mengintegrasikan subsistem, dikelola Polri**; data dapat diakses setiap pembina | Arsitektur: ITCS = subsistem pemprov terintegrasi ke pusat kendali Polri (C2C) | T4 |
| 248–249 | Pengembangan SIK: pemantauan, deteksi arus, **pengenalan TNKB**, identifikasi kendaraan; pusat kendali: rekam jejak elektronis, dukungan penegakan hukum, info kualitas udara | Fungsi ANPR & data udara berdasar UU | T4 |
| 250, 251 | Data pusat kendali **harus dapat diakses masyarakat**; SIK untuk penegakan hukum oleh Polri | Portal/API publik (dengan pengecualian data pribadi) | T2 |
| 260, 262(3) | Penyidik Polri; PPNS terbatas & wajib didampingi Polri di jalan | Aplikasi bukan penindak | T4 |
| 272 | Peralatan elektronik untuk penindakan; hasilnya alat bukti | Dasar ETLE; format bukti terverifikasi | T4 |

### A.2 PP 32/2011 (MRLL, Andalalin, MKLL)
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| 2, 5 | Tanggung jawab per status jalan; gubernur setelah rekomendasi Kemenhub/PU/Polri; koordinasi provinsi berbatasan | Atribut status jalan; workflow rekomendasi; multi-yurisdiksi Bodetabek | T1 |
| 7, 9 | Identifikasi masalah & inventarisasi (volume, komposisi, variasi, arah, pengaturan, kecepatan & tundaan, kinerja perlengkapan, prakiraan) | Skema data survei & perlengkapan | T1 |
| 16 | Polri memegang pangkalan data pelanggaran & kecelakaan | Data kecelakaan via API Polri, bukan dikumpulkan sendiri | T4 |
| 19, 21 | LOS ditetapkan gubernur; 9 indikator; kebijakan per ruas/simpang | Modul penetapan LOS target | T2 |
| 24, 27 | Perintah/larangan per ruas provinsi = keputusan gubernur; wajib diinformasikan | Arsip SK & sosialisasi | T2 |
| 31 | Pemeliharaan: **memantau keberadaan & kinerja perlengkapan jalan** | Modul kesehatan aset | T1 |
| 34–35 | Optimalisasi operasional saat situasional/**APILL tidak berfungsi**/prioritas/pekerjaan jalan/kecelakaan → dilaksanakan Polri dengan APILL sementara | Notifikasi kegagalan ke Polri; event khusus | T2 |
| 44, 46 | Pengawasan gubernur (efektivitas kebijakan); penegakan Polri langsung/elektronik | Laporan efektivitas; ETLE ranah Polri | T2/T4 |
| 60–63 | MKLL: kriteria, strategi, wajib rambu, evaluasi tiap tahun | Dashboard evaluasi MKLL tahunan | T5 |
| 64–66, 70–71 | Pembatasan perseorangan (V/C ≥0,7 & <30 km/jam; jumlah penumpang/TNKB); motor (V/C ≥0,5) | Kalkulator kelayakan pembatasan; dasar ganjil-genap | T5 |
| 79–83 | ERP: V/C ≥0,9, ≤10 km/jam, 2×2 lajur, **bukan jalan nasional**; dana untuk kinerja lalu lintas & teknologi; diatur Perda | Integrasi ERP; pembiayaan | T5 |

### A.3 PP 79/2013 (Jaringan LLAJ) & PP 37/2011 (Forum LLAJ)
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| PP 79 Ps.42–43 | Jenis APILL 3/2/1 warna; susunan; makna warna termasuk merah+kuning | Sama dengan PM 49 (turunannya) | T1 |
| PP 79 Ps.26 huruf c, f | Perlengkapan jalan: APILL; alat pengawasan & pengamanan (timbangan) | Alat pengawasan ≠ CCTV lalu lintas | — |
| PP 37/2011 | Forum LLAJ: tugas koordinasi, keanggotaan | Stakeholder & pelaporan | T2 |

### A.4 Permenhub PM 96/2015 (Pedoman MRLL)
| Bagian | Isi | Implikasi | Tahap |
|---|---|---|---|
| Ps.1(4) | MRLL oleh pejabat/petugas berkompetensi | Manajemen pengguna & kualifikasi | T1 |
| **Ps.5(2)–(3)** | MRLL di jalan nasional DKI oleh gubernur setelah **persetujuan Dirjen Hubdat** (perencanaan & perekayasaan) | Flag simpang jalan nasional; workflow persetujuan | T1 |
| Lamp.I Bab II | 8 kegiatan perencanaan (5 wajib); kamera boleh untuk pengamatan; LHRT ≥4×/tahun; VJP 9% | Sumber data | T1–T2 |
| Lamp.I Bab II.D | **LOS simpang A–F (tundaan <5…>60 s)**; LOS ruas kecepatan; target LOS minimal per fungsi jalan | Skema LOS dashboard | T1 |
| Lamp.I Bab II.E | Alternatif penanganan **wajib disimulasikan sebelum ditetapkan** | Simulasi (SUMO) sebelum deploy plan | T3 |
| Lamp.I Bab III–IV | Penetapan lokasi/jenis APILL via Keputusan Gubernur; wajib sosialisasi; **uji coba pengoperasian APILL** saat pemasangan | Arsip SK; checklist commissioning | T1 |
| Lamp.I Bab VI | Monev = LOS sebelum vs sesudah; tindakan korektif | Modul before–after | T2 |
| Lamp.II.A, D | Prioritas angkutan massal: **bus priority di simpang ber-APILL**; hijau khusus angkutan umum & pejalan kaki | Fitur TSP | T3 |
| Lamp.II.F.b | Warrant APILL (750/8 jam; >30 s; 175 ped; 5 laka) | Modul kelayakan | T2 |
| Lamp.II.F.d | APILL otonom adaptif wajib detektor | Health check sebelum mode adaptif | T3 |
| Lamp.II.F.e | ATCS ≥3 simpang, ≤1 km, detektor, komunikasi, Control Centre Room; opsional kamera, DIS, VMS, detektor bus, fase bus priority, pemantau kecepatan/volume | Corridor grouping & inventaris | T2 |
| Lamp.II.F.g | ITS di simpang ber-ATCS: pemantau kecepatan/volume + media informasi | Modul ATIS | T2 |
| Lamp.II.F.h | Kotak kuning hanya pada adaptif/ATCS & LOS ≥C | Validasi | T3 |
| Lamp.II.G–H | ITS ruas (detektor, kamera, VMS); pembatasan berdasar emisi; APILL tenaga surya | — | T4–T5 |
| Lamp.III | Kajian ke Dirjen minimal kecepatan rata-rata & V/C; laporan ≥1×/tahun; evaluasi Dirjen | Template kajian & laporan tahunan | T2 |

### A.5 Permenhub PM 49/2014 (APILL) — pasal rekonstruksi
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| 3–10 | Jenis, fungsi, makna warna (merah+kuning), susunan | State machine head | T1 |
| 4, 11–12 | Otonom vs terkoordinasi; siklus terkoordinasi = skema antar-APILL oleh **sistem terpusat** | Dasar ATCS/ITCS terpusat | T2 |
| 13–16 | Siklus tetap **≥8 rencana**; semi-adaptif; adaptif | Mode kendali & fallback TOD | T1 |
| 17–18 | 12 aspek makro/mikro penentuan siklus; tata cara oleh Dirjen | Dokumentasi algoritma; rujuk PKJI/Dirjen 273 | T2 |
| 19–24 | Komponen; controller 5–70 °C, RH ≤95% | Atribut aset | T1 |
| 25 | Boleh dipasangi detektor, kamera, DIS, perangkat TI **bersertifikat** | Atribut sertifikasi per perangkat | T1 |
| 27–28 | Penyelenggaraan oleh Dirjen (nasional/perpotongan)/gubernur (provinsi)/tol (BUJT) | Peta kewenangan per simpang | T1 |
| 29–39 | Penempatan & tinggi (≥300/175–265/≥500 cm), ≤3 armatur/tiang | Checklist inspeksi | T1 |
| 41 | Pemeliharaan berkala **≥6 bulan**; insidentil termasuk **penyesuaian siklus dengan arus aktual** | Jadwal PM; log re-timing | T1 |
| 42 | Umur teknis ≤5 tahun; penghapusan berdasarkan penilaian kinerja | Asset life cycle | T1 |
| 43–45 | Pembuat terdaftar Ditjen; peralihan 2 tahun; pembinaan Dirjen | Atribut pabrikan | T1 |
| (tidak ada) | Durasi min hijau/kuning/all-red/pejalan kaki; protokol; log; police panel | Ambil dari PKJI & SK 7234 [R05 B] | — |

### A.6 Permenhub PM 76/2021 (SMTC/ITS) — dari bacaan penuh [R00 C]
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| 1(1), 2–3 | Definisi SMTC; maksud; ruang lingkup | Positioning produk = SMTC | T1 |
| 4(2)–(4) | **Sistem terbuka, berkesinambungan, berstandar**; 8 jenis data (kecepatan, pola aliran, kepadatan, waktu perjalanan, cuaca, kondisi jalan, identitas kendaraan, sarana-prasarana) | Standar terbuka (NTCIP/API); skema data wajib | T1–T2 |
| 4(5)–(6), 5 | Data → dasar MRLL/MKLL & informasi masyarakat; tujuan real time | ATIS publik | T2 |
| 6 | 12 jenis SMTC | Roadmap modul | — |
| **7** | ATMS: subsistem ATCS, pemantauan real time, VMS, kecelakaan, jalan penghubung, ETLE, waktu tempuh, prioritas bus; **prinsip: semua perangkat terhubung ke ruang kendali & dapat disetel dari ruang kendali**; layanan prioritas kendaraan khusus, pemantauan visual, informasi, penindakan, **deteksi kerusakan dari ruang kendali, rekaman operasional & historis**, deteksi kecepatan | Daftar modul minimal & requirement arsitektur terpusat | T2–T4 |
| 8 | ATIS: kepadatan, jalur alternatif, parkir, cuaca; daring/ponsel/rambu | Portal publik | T2 |
| 11 | APTS: **sinyal prioritas bus untuk perubahan fase**; kurangi tundaan angkutan umum | TSP | T3 |
| 13 | Manajemen darurat: info ambulans, pemadam, RS, derek | Integrasi CAD | T4 |
| 15 | TDM: identifikasi kendaraan, ERP, ANPR | T5 | T5 |
| 18 | Standar teknis oleh Dirjen | Pantau pedoman turunan | — |
| 19 | Penyelenggara: gubernur (provinsi); **BPTJ jalan nasional Jabodetabek**; boleh kerja sama badan usaha (rencana–bangun–operasi–pelihara) | Model bisnis KPBU/kerja sama | T1 |
| 20–21 | Integrasi dengan sistem K/L & pemda; wajib **unit kerja pengelola & SDM kompeten** | Persyaratan organisasi pembeli | T2 |
| 22–24 | Pembinaan & pengawasan (penilaian efektivitas, koreksi) | Laporan efektivitas | T2 |

### A.7 Perda DKI 5/2014 (Transportasi)
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| 8–10 | Target **60% KBU & 35 km/jam**; Renstra 5 tahun; RIT evaluasi 5 tahun | KPI strategis | T2 |
| 67–71, 73 | MRLL; **prioritas di persimpangan untuk KBU**; informasi masyarakat; pengawasan & penegakan | TSP; portal | T3 |
| 74 | Dilarang memasang/memindahkan APILL tanpa **izin Kepala Dinas** | Referensi izin per aset | T1 |
| 78–86 | 14 cara pembatasan; ERP: 9 ruas, 07.00–20.00 hari kerja, kriteria V/C ≥0,9/≤10 km/jam; efektivitas = kenaikan kecepatan; dana untuk teknologi & SDM; Dewan Pengawas | Integrasi ERP; KPI kecepatan | T5 |
| 95 | PPNS Dishub hanya pelanggaran tertentu (busway, kawasan pengendalian, dll.) | Batas modul penindakan Dishub | T4 |
| 232–235 | Sistem informasi transportasi Pemda; **dapat diakses masyarakat**; untuk penegakan hukum oleh Polri | Portal & API | T2 |
| 237, 239 | Penilaian kinerja tahunan; kerja sama via perjanjian | Laporan tahunan; MoU | T2 |

### A.8 Pergub DKI 68/2021 (Jak Lingko)
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| 1 angka 4–5 | Interoperabilitas & interkoneksi | Kriteria desain | T1 |
| 10(6)–(7) | 18 jenis data operasional (AVL, waktu tempuh, headway, kecelakaan & pelanggaran, aduan); **wajib kerahasiaan & keamanan** | Sumber AVL untuk TSP; keamanan | T3 |
| 11 | Integrasi ke sistem Pemprov; **data milik Pemprov**; akses pihak lain dengan persetujuan Gubernur | Klausul kepemilikan data; RBAC | T2 |
| 13 | Pembatasan: ERP, ganjil-genap, dll.; data terintegrasi ke sistem Pemprov | Integrasi TDM | T5 |
| 15 | Monev; laporan ke Gubernur tiap 3 bulan | Laporan triwulan | T2 |

### A.9 Pergub DKI 155/2018 jo. 88/2019 jo. 76/2020 (ganjil-genap)
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| 88/2019 Ps.1 | 26 ruas ganjil-genap (Pintu Besar Selatan, Gajah Mada, Hayam Wuruk, Majapahit, Medan Merdeka Barat, Thamrin, Sudirman, Sisingamangaraja, Panglima Polim, Fatmawati (Ketimun 1–TB Simatupang), Suryopranoto, Balikpapan, Kyai Caringin, Tomang Raya, S. Parman (Tomang Raya–Gatot Subroto), Gatot Subroto, MT Haryono, Rasuna Said, DI Panjaitan, A. Yani (Bekasi Timur Raya–Perintis Kemerdekaan), Pramuka, Salemba Raya Barat, Salemba Raya Timur (Paseban–Diponegoro), Kramat Raya, St. Senen, Gunung Sahari) | Geofence ruas & jadwal; konteks ANPR | T4–T5 |
| 88/2019 Ps.3 | Senin–Jumat **06.00–10.00 & 16.00–21.00**; tidak Sabtu/Minggu/libur nasional; berlaku 9 Sep 2019 | Jadwal kebijakan | T5 |
| 88/2019 Ps.4 | Pengecualian: disabilitas bertanda khusus, ambulans, pemadam, angkutan umum plat kuning, listrik, sepeda motor, pengangkut BBM/BBG, pimpinan lembaga tinggi negara, dinas plat merah/TNI/Polri, tamu negara, pertolongan kecelakaan, pengangkut uang berkawalan Polri, diskresi Polri; tanda khusus via Kepala Dishub | Whitelist kelas kendaraan | T5 |
| 76/2020 Ps.4A | Pengecualian tenaga kesehatan COVID-19 (bertanda khusus) | Whitelist dinamis | — |

### A.10 Perpres 55/2018 (RIT Jabodetabek 2018–2029)
| Bagian | Isi | Implikasi | Tahap |
|---|---|---|---|
| Ps.3–4, 13 | Pedoman pusat & pemda; rencana aksi berkoordinasi BPTJ; evaluasi 5 tahun | Selaraskan roadmap dengan RITJ | T1 |
| Lamp. target 2029 | 60% angkutan umum; ≤90 menit; **≥30 km/jam**; cakupan 80%; ≤3 pindah moda | KPI | T2 |
| Lamp. Kebijakan 6 | ELE; **ERP & pengaturan motor**; **prioritas bus di persimpangan**; sistem informasi lalu lintas real time di arteri (Thamrin–Sudirman–Rasuna Said dll.); **pembangunan/pengembangan ATCS** DKI + 8 kota/kab (Kemenhub/pemda); CCTV arteri | Justifikasi program di Bodetabek | T2–T4 |

### A.11 UU 27/2022 Pelindungan Data Pribadi (relevansi ANPR/CCTV)
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| 1 angka 1 | Data pribadi = data orang perseorangan yang teridentifikasi/dapat diidentifikasi, langsung/tidak langsung | Pelat nomor + waktu + lokasi = data pribadi (dapat diidentifikasi via regident) | T4 |
| 4(2) | Data spesifik: kesehatan, **biometrik**, genetika, **catatan kejahatan**, anak, keuangan | Face recognition = biometrik; data pelanggaran = catatan kejahatan → risiko tinggi | T4 |
| 16 | Pemrosesan (perolehan…penghapusan) wajib terbatas, spesifik, sah, transparan, sesuai tujuan | Retensi & minimisasi data ANPR | T4 |
| 20(2) | Dasar pemrosesan: persetujuan; perjanjian; **kewajiban hukum**; kepentingan vital; **tugas kepentingan umum/pelayanan publik/kewenangan berdasarkan peraturan**; kepentingan sah | Dasar hukum ITCS = pelayanan publik/kewenangan (UU 22/2009, PM 76) — dokumentasikan | T4 |
| 21 | Informasi legalitas, tujuan, jenis, retensi kepada subjek | Kebijakan privasi publik | T4 |
| 34 | **DPIA wajib** untuk: keputusan otomatis berdampak hukum, data spesifik, skala besar, pemantauan sistematis | ANPR/ETLE = pemantauan sistematis skala besar → DPIA | T4 |
| 35, 39 | Wajib keamanan; cegah akses tidak sah; sistem elektronik andal | Enkripsi, RBAC, audit | T2 |
| 46 | Kegagalan pelindungan → pemberitahuan tertulis ≤3×24 jam ke subjek & lembaga | Prosedur insiden | T2 |
| 53 | Wajib **pejabat/petugas PDP** bila pemrosesan untuk pelayanan publik / pemantauan teratur skala besar | Peran DPO di organisasi pengguna | T4 |
| 57 | Sanksi administratif (teguran, penghentian, penghapusan, denda) | Risiko kepatuhan | — |
| 65, 67 | Pidana memperoleh/mengungkap data pribadi secara melawan hukum (≤5 tahun/Rp5 M) | Kontrol akses ketat, larangan berbagi tanpa dasar | — |
| 74 | Penyesuaian ≤2 tahun sejak 17 Okt 2022 | Sudah berlaku penuh | — |

### A.11b Perpol 8/2023 (Penyelenggaraan Lalu Lintas Berbasis Sistem Elektronik) & Perpol 2/2025 (Penindakan Berbasis Bukti Rekaman Elektronik)
| Pasal | Isi | Implikasi | Tahap |
|---|---|---|---|
| Perpol 8/2023 Ps.13–16 | Tahapan penyelenggaraan sistem elektronik lalu lintas Polri: pengumpulan, klasifikasi, analisis data, integrasi sistem, evaluasi | Data ITCS masuk sebagai sumber yang dikumpulkan/diklasifikasikan Polri | T4 |
| Perpol 8/2023 Ps.17 | Integrasi sistem data & informasi dengan **kementerian/lembaga/pemda/badan hukum** melalui: analisis kebutuhan, penilaian sistem, **standar & protokol keamanan, penggunaan API**, migrasi data, uji coba, validasi, pengawasan, pemeliharaan | ITCS wajib menyediakan API terdokumentasi (format data, metode pertukaran) dan ikut uji coba/validasi Polri | T4 |
| Perpol 8/2023 Ps.18 | Rincian: kebutuhan data/tujuan/manfaat; identifikasi arsitektur, basis data, protokol komunikasi, fitur; standar format & metode pertukaran; API sesuai peraturan | Dokumen Interface Control Document (ICD) ke Polri | T4 |
| Perpol 8/2023 Ps.19 | Evaluasi oleh Kapolri via fungsi lalu lintas, dapat melibatkan gubernur/bupati/walikota, **minimal 1×/tahun**, laporan ke Kapolri/menteri/gubernur | Laporan integrasi tahunan; audit trail | T4 |
| Perpol 8/2023 Ps.20–24 | Kantor pengolah & operasional; operator | Titik kontak operasional (Back Office ETLE Polda) | T4 |
| Perpol 2/2025 Ps.3 | Alat bukti rekaman elektronik dari ETLE statis/portabel/mobile (terintegrasi **Back Office ETLE Polri**) dan/atau **"perangkat elektronik lainnya" yang wajib diverifikasi petugas Polri** | Kamera ITCS = "perangkat elektronik lainnya": bukti dikirim ke Back Office ETLE via API, diverifikasi Polri; aplikasi **tidak menerbitkan tilang** | T4 |
| Perpol 2/2025 Ps.4 | Jenis pelanggaran: kecepatan, sabuk, rambu/marka, **APILL**, penumpang motor, helm, aktivitas mengganggu, lajur, parkir, muatan/dimensi, lainnya | Klasifikasi event pelanggaran yang boleh dikirim | T4 |
| Perpol 2/2025 Ps.8–14 | Alur: identifikasi → verifikasi ERI (regident) → surat konfirmasi (3 hari) → konfirmasi pemilik (5 hari) → tilang → pembayaran (7 hari) → blokir STNK bila tidak bayar | Status tindak lanjut hanya dibaca dari Polri (read-only); retensi bukti mengikuti alur | T4 |

### A.12 Kep. Dirjen 273/1996, SK Dirjen 7234/2013, KepKa LAN 1/2023
| Sumber | Isi | Implikasi | Tahap |
|---|---|---|---|
| Dirjen 273/1996 | Metode perhitungan fixed-time (lihat rumus A); **evaluasi waktu APILL ≥1×/3 bulan**; kriteria pemasangan; tata letak | Kalkulator; jadwal retiming | T1–T2 |
| SK 7234/2013 Bab II | Spesifikasi controller (≥8+8 SG, ≥4–16 program, 10 plan/hari, conflict monitor, manual panel, start-up), detektor (≥4 zona, gap & occupancy), DIS (RS-485, countdown), power, penandaan; perkiraan kebutuhan 5 tahun | Model data controller & spesifikasi pengadaan | T1–T3 |
| KepKa LAN 1/2023 & Modul PKN II | Struktur RPP 11 komponen; milestone jangka pendek/menengah/panjang; stakeholder; marketing | Format dokumen untuk pembeli pemda (pejabat PKN) | — |

## B. Matriks kepatuhan ringkas (C-01…C-43)
Penomoran C-01…C-35 **identik dengan R05 §G.1** (kanonis; dipakai juga oleh `04_Katalog_Kebutuhan.md`, `docs/planning/04` dan `05`). C-36…C-43 adalah tambahan dari bacaan penuh PM 76, UU PDP, SK 7234, dan Perpol ETLE.

| ID | Kebutuhan | Dasar | Tahap |
|---|---|---|---|
| C-01 | Atribut status jalan per simpang; flag jalan nasional; workflow persetujuan Dirjen/BPTJ | PM 49 Ps.28; PM 96 Ps.5; PM 76 Ps.19 | T1 |
| C-02 | Referensi Keputusan Gubernur (lokasi & jenis APILL) per aset | PM 96 Lamp.I III; PP 32 Ps.24 | T1 |
| C-03 | Tanggal pasang → berlaku hukum +30 hari; tenggat pemasangan 60 hari | UU Ps.102 | T1 |
| C-04 | Izin Kepala Dinas sebelum aset APILL aktif/dipindah | Perda Ps.74 | T1 |
| C-05 | Sertifikasi & logo perhubungan per perangkat TI/APILL | PM 49 Ps.21, 25 | T1 |
| C-06 | Pemeliharaan berkala ≤6 bulan + insidentil (re-timing) dengan alarm jatuh tempo | PM 49 Ps.41 | T1 |
| C-07 | Umur teknis ≤5 tahun; penilaian kinerja untuk penghapusan | PM 49 Ps.42 | T1 |
| C-08 | Pemantauan keberadaan/lokasi/kondisi/fungsi perlengkapan jalan | PP 32 Ps.31; PM 96 | T1 |
| C-09 | ≥8 rencana siklus (TOD) sebagai fallback; mode tetap/semi-adaptif/adaptif/terkoordinasi | PM 49 Ps.11–16 | T1 |
| C-10 | Algoritma siklus mempertimbangkan 12 aspek makro/mikro; terdokumentasi | PM 49 Ps.17 | T2 |
| C-11 | Corridor grouping ATCS ≥3 simpang, ≤1 km; kelengkapan minimal | PM 96 Lamp.II.F.e | T2 |
| C-12 | Mode adaptif hanya bila detektor sehat | PM 96 Lamp.II.F.d | T3 |
| C-13 | Pemantau kecepatan/volume + media informasi (ITS) | PM 96 Lamp.II.F.g | T2 |
| C-14 | Bus priority & hijau khusus angkutan umum/pejalan kaki | Perda Ps.70; PM 96 Lamp.II.A; PM 76 Ps.11 | T3 |
| C-15 | Override manual petugas Polri/TMC dengan audit log | UU Ps.104; PP 32 Ps.34–35 | T1 |
| C-16 | Preemption kendaraan hak utama | UU Ps.134–135 | T3 |
| C-17 | Logika kotak kuning saat gridlock; syarat LOS ≥C | UU Ps.103; PM 96 Lamp.II.F.h | T3 |
| C-18 | Notifikasi kegagalan APILL ke Polri/TMC; insiden tercatat | PP 32 Ps.34–35; PM 76 Ps.7(4)e | T1 |
| C-19 | Simulasi & sosialisasi sebelum kebijakan ditetapkan | PM 96 Lamp.I II.E, III.C | T3 |
| C-20 | Monev LOS sebelum/sesudah; laporan ke Forum LLAJ, Dirjen (tahunan), Gubernur (triwulan) | PM 96 Bab VI; UU Ps.98; Pergub 68 Ps.15 | T2 |
| C-21 | Template kajian ke Dirjen (kecepatan rata-rata & V/C) | PM 96 Lamp.III | T2 |
| C-22 | Integrasi ke pusat kendali SIK LLAJ Polri; data dapat diakses pembina | UU Ps.246–247 | T4 |
| C-23 | Portal/API publik (kecuali data pribadi) | UU Ps.250; Perda Ps.233 | T2 |
| C-24 | ETLE: hanya bukti elektronik → Polri; tidak ada denda otomatis oleh Dishub | UU Ps.272, 260, 262; Perda Ps.95 | T4 |
| C-25 | Integrasi pajak/uji emisi/TNKB via perjanjian & dasar hukum | PP 32 Ps.16; UU Ps.248; Pergub 68 Ps.13; Perda Ps.239 | T4 |
| C-26 | Kerahasiaan & keamanan data; data milik Pemprov; akses pihak ketiga dengan persetujuan | Pergub 68 Ps.10(7), 11 | T2 |
| C-27 | Interoperabilitas/interkoneksi; integrasi Jakarta Smart City/JAKI | Pergub 68 Ps.1, 10–11 | T2 |
| C-28 | ERP hanya ruas memenuhi kriteria, bukan jalan nasional; jam & ruas Perda | PP 32 Ps.79–83; Perda Ps.78–85 | T5 |
| C-29 | Ganjil-genap/pembatasan perseorangan: ruas, jam, whitelist pengecualian; evaluasi tahunan | Pergub 155/88/76; PP 32 Ps.62–66 | T5 |
| C-30 | LOS A–F PM 96 & KPI 35/30 km/jam | PM 96; Perda Ps.8; Perpres 55 | T1 |
| C-31 | Info kualitas udara; pembatasan berdasar emisi; APILL tenaga surya dipertimbangkan | UU Ps.249; PM 96 Lamp.II.H | T4 |
| C-32 | Aksesibilitas: tombol pejalan kaki, isyarat suara | PM 49 Ps.33; PM 96 Lamp.II.C | T2 |
| C-33 | Kompetensi operator; unit kerja pengelola | PM 96 Ps.1(4); PM 76 Ps.21 | T2 |
| C-34 | Rencana aksi RITJ & koordinasi BPTJ (Bodetabek) | Perpres 55 Ps.4 | T2 |
| C-35 | Laporan monev triwulan (Jak Lingko) & penilaian kinerja transportasi tahunan | Pergub 68 Ps.15; Perda Ps.237 | T2 |
| C-36 | Sistem terbuka & berstandar (NTCIP/API terdokumentasi); semua perangkat online & dapat disetel dari ruang kendali; rekaman operasional & historis | PM 76 Ps.4(2), 7(3)–(4) | T1–T2 |
| C-37 | Dasar pemrosesan data pribadi terdokumentasi (pelayanan publik/kewenangan); kebijakan privasi | UU PDP Ps.20–21 | T4 |
| C-38 | DPIA sebelum ANPR/ETLE/face recognition; minimisasi & retensi | UU PDP Ps.16, 34 | T4 |
| C-39 | Pejabat PDP di organisasi pengguna; prosedur insiden ≤3×24 jam | UU PDP Ps.46, 53 | T4 |
| C-40 | Keamanan siber: RBAC, audit, enkripsi, kabinet terkunci/alarm (NEMA TS 8 sebagai referensi) | UU PDP Ps.35, 39; TSPH | T2 |
| C-41 | Spesifikasi controller/detektor/DIS sesuai SK 7234 untuk pengadaan | SK 7234 Bab II | T3 |
| C-42 | Bukti pelanggaran dari kamera ITCS diperlakukan sebagai "perangkat elektronik lainnya": dikirim ke Back Office ETLE Polri via API, diverifikasi petugas Polri; aplikasi tidak menerbitkan/menghitung tilang; status tindak lanjut read-only | Perpol 2/2025 Ps.3–4, 8–14 | T4 |
| C-43 | ICD integrasi dengan Polri: format data, metode pertukaran, protokol keamanan, API, uji coba & validasi, pengawasan, pemeliharaan; laporan evaluasi integrasi tahunan | Perpol 8/2023 Ps.17–19 | T4 |

## C. Kewenangan siapa untuk apa
| Fungsi | Dishub/Gubernur (jalan provinsi/kota) | Polri | Dirjen Hubdat / BPTJ | Catatan |
|---|---|---|---|---|
| Perencanaan & perekayasaan MRLL, pengadaan/pemasangan/pemeliharaan APILL | ✔ (setelah rekomendasi) | rekomendasi operasional | ✔ jalan nasional & perpotongan; persetujuan untuk DKI di jalan nasional | UU Ps.96; PM 49 Ps.28; PM 96 Ps.5 |
| Operasional MRLL, pengaturan situasional, APILL sementara | — | ✔ | — | UU Ps.7, 97; PP 32 Ps.34–35 |
| Penegakan hukum, ETLE, penyidikan | PPNS terbatas (Perda Ps.95), didampingi Polri; ITCS hanya mengirim bukti ke Back Office ETLE | ✔ (verifikasi bukti, konfirmasi, tilang, blokir STNK) | — | UU Ps.260–272; Perpol 2/2025 Ps.3, 8–14; Perpol 8/2023 Ps.17 |
| Pusat kendali SIK LLAJ | subsistem pemprov | ✔ pengelola pusat kendali | — | UU Ps.247 |
| Penyelenggaraan SMTC/ITS | ✔ jalan provinsi (boleh kerja sama badan usaha) | — | Dirjen (nasional non-Jabodetabek); **BPTJ (nasional Jabodetabek)** | PM 76 Ps.19 |
| Penetapan LOS, kebijakan per ruas, ERP, ganjil-genap | ✔ (Keputusan/Perda/Pergub) | — | — | PP 32 Ps.19, 24, 63; Perda |
| Data pangkalan pelanggaran & kecelakaan | pengguna via perjanjian | ✔ pemilik | — | PP 32 Ps.16 |
| Data operasional transportasi terintegrasi | ✔ pemilik (Pemprov) | akses dengan persetujuan | — | Pergub 68 Ps.11 |
| Pembinaan & pengawasan SMTC | Gubernur untuk provinsi | — | Menteri/Dirjen/BPTJ | PM 76 Ps.22–24 |

**Pointer ke detail**
- Pasal lengkap & kutipan verbatim: R05 A–H; PM 76 penuh: R00 C; PM 49 & SK 7234: R00 B, H; Pergub 68: R00 D.
- Teks asli: `docs/sources/_teks_ekstraksi/` (UU_22_2009, PP_32_2011, PP_79_2013, Permenhub_PM_*, Perda_DKI_5_2014, Pergub_DKI_*, Perpres_55_2018, UU_27_2022_*).
- Perpol ETLE: `docs/sources/_teks_ekstraksi/Perpol_8_2023_*.txt`, `Perpol_2_2025_*.txt` (bagian A.11b).
- Tindak lanjut sumber belum ada: Pergub turunan MRLL/ERP, PM 67/2021, Perdirjen tata cara siklus [R05 daftar tindak lanjut].
