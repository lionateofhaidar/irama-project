# 13 — Kebutuhan Data yang Harus Disediakan per Tahap

Status: revisi 2026-09-14, menggantikan versi 2026-09-13. Dasar revisi adalah keputusan user T-34, T-39, T-41, dan T-42 di `docs/LOG_SESI.md`. T1 dan T2 dirinci secara presisi, sedangkan T3 sampai T5 berupa perkiraan yang dipertajam saat planning tiap tahap. Spesifikasi pemakaian data ada di `15`, dan cara menyiapkan data latih ada di `16`.

## 0. Aturan pengumpulan

- **Rekaman saja sampai ada MoU.** Sampai T2 selesai, atau paling lambat sampai T3 dimulai, data video berasal dari rekaman: rekaman sendiri, rekaman yang diserahkan pihak lain, atau video publik. Stream dan portal CCTV Dishub tidak diakses sebelum MoU.
- **Video publik boleh untuk uji dan pelatihan.** Setiap klip dicatat di register sumber (D1.1) beserta tautannya. Sebelum penjualan komersial skala besar, model dilatih ulang dengan data berizin (`08`).
- **Mulai dari sampel terbatas.** Simulasi awal memakai satu simpang pada waktu puncak dan non-puncak, dengan kondisi pagi, malam, dan hujan. Kondisi yang berbeda boleh diambil dari simpang berbeda bila rekaman satu simpang tidak tersedia.
- **Uji akurasi dan optimasi punya syarat berbeda.** Uji akurasi boleh memakai klip dari simpang mana pun. Optimasi satu simpang memerlukan hitungan semua lengan pada periode yang sama.
- **Privasi.** Rekaman disimpan di laptop tim, tidak dibagikan ke luar tim, dan dihapus setelah diolah kecuali sampel validasi yang disamarkan. Rekaman dari Dishub tidak diunggah ke layanan GPU gratis.
- **Hemat ruang.** Rekaman 1080p berukuran sekitar 1,5 sampai 2 GB per jam per kamera. Bila ruang terbatas, rekam atau unduh dalam 720p dan olah per batch.

## T1 — Purwarupa Hitung dan Rekomendasi (presisi)

| # | Data | Isi dan format | Cara mendapatkan | Jumlah minimum | Dipakai untuk |
|---|---|---|---|---|---|
| D1.1 | **Register sumber rekaman** | CSV `register_sumber.csv`: id klip, nama file, sumber (Dishub, rekaman sendiri, video publik), tautan asli, pemilik atau kanal, izin atau lisensi, tanggal rekam atau unggah, simpang, pendekat (U/T/S/B), kondisi (pagi, siang, sore, malam, hujan), periode (puncak atau non-puncak), durasi, resolusi, kegunaan (latih, uji, operasi) | diisi setiap kali klip ditambahkan | semua klip | bukti asal-usul data dan kebijakan data (ADR-22); di T1 berupa berkas CSV, fitur register di aplikasi menyusul di T2 (F-T2-152) |
| D1.2 | **Rekaman simpang target** | MP4 atau MKV, resolusi asli minimal 720p, sudut tetap, garis henti dan kendaraan yang masuk terlihat jelas, satu berkas per pendekat | rekaman sendiri dari titik tinggi yang aman, rekaman yang diserahkan pihak lain, atau video publik | semua pendekat satu simpang; minimal 1 jam puncak dan 1 jam non-puncak pada siang hari | tabel hitungan 15 menit (F-T1-144), rekomendasi T1 |
| D1.3 | **Klip data latih** | klip 5 sampai 15 menit dari berbagai simpang, sudut, dan cahaya | rekaman sendiri dan video publik, dicatat di D1.1 | minimal dua klip puncak pagi atau siang, satu klip non-puncak, satu klip malam, satu klip hujan | dataset berlabel sekitar 2.000 sampai 3.000 gambar (versi v0.2) sesuai `16` |
| D1.4 | **Klip uji akurasi** | klip 15 menit yang tidak dipakai melatih, diutamakan dari simpang berbeda | dipilih dari D1.2 atau sumber lain, ditandai "uji" di register | satu klip per kondisi: siang puncak, siang non-puncak, malam, hujan | uji akurasi sekitar 90% siang dan 85% malam atau hujan |
| D1.5 | **Hitungan manual referensi** | CSV `hitung_manual.csv`: id klip, pendekat, interval 15 menit, jumlah per kelas (motor, mobil, bus, truk, kendaraan tak bermotor, pejalan kaki); garis hitung sama dengan garis di sistem | dihitung tim dari klip uji: putaran pertama khusus motor, putaran kedua kelas lain dengan kecepatan putar 1,5 sampai 2 kali (`16`) | setiap klip uji D1.4 | akurasi = 1 − (jumlah selisih mutlak hitungan sistem dan manual) / (jumlah hitungan manual), rumus lengkap di `16` |
| D1.6 | **Data simpang dasar** | CSV `simpang.csv`: id, nama simpang, koordinat, nama jalan tiap lengan, status jalan (nasional, provinsi, kota), jumlah lengan, jumlah penduduk kota (untuk faktor ukuran kota PKJI), tipe lingkungan (komersial, permukiman, akses terbatas) | peta daring dan dokumen status jalan | satu simpang target | konfigurasi (F-T1-170), kalkulator PKJI |
| D1.7 | **Geometri tiap pendekat** | CSV `pendekat.csv`, satu baris per pendekat dengan kode arah mata angin (U, S, T, B; U1 dan U2 bila satu lengan dibagi pulau jalan menjadi dua pendekat dengan fase berbeda): lebar pendekat di hulu, lebar masuk di garis henti, lebar keluar di titik tersempit setelah area konflik, lebar lajur belok kiri langsung bila ada beserta izin belok kiri langsung, jumlah dan lebar lajur di garis henti, panjang lajur khusus belok yang terbatas, median (ada atau tidak, lebar, ditinggikan atau direndahkan), kelandaian (%) bertanda plus bila menanjak ke arah simpang dan minus bila menurun, jarak kendaraan parkir pertama dari garis henti, gerakan yang diizinkan, jarak garis henti ke titik konflik untuk kendaraan berangkat, kendaraan datang, dan pejalan kaki (untuk merah semua, PKJI 5-9), tipe lingkungan pendekat bila berbeda dari D1.6, kelas hambatan samping hasil pengamatan (rendah, sedang, tinggi; dipakai T1 sebelum hambatan samping otomatis di T2), foto tiap lengan; ditambah satu sketsa simpang berisi pulau jalan, garis henti, marka lajur, zebra cross, halte, akses di sepanjang pendekat, dan arah utara (mengikuti Formulir SA-I PKJI 2023) | ukur lebar dan jarak dari citra satelit, lalu verifikasi dengan satu kunjungan singkat memakai meteran atau aplikasi ukur; lebar masuk diprioritaskan karena selisih 0,5 m pada lebar efektif mengubah arus jenuh dasar pendekat terlindung sebesar 300 SMP/jam (J0 = 600 × LE); kelandaian, parkir, tipe lingkungan, dan hambatan samping dicatat saat kunjungan | semua pendekat simpang target | kalkulator PKJI (lebar efektif, arus jenuh, merah semua) |
| D1.8 | **Fase dan waktu lampu eksisting** | CSV `waktu_eksisting.csv`: periode, nomor fase, gerakan yang dilayani, hijau, kuning, merah semua, urutan fase, waktu siklus | dihitung dari rekaman (tiga siklus per periode dengan stopwatch) atau ditanyakan ke petugas | setiap periode yang direkam | kinerja eksisting, perbandingan dengan rekomendasi |
| D1.9 | **Contoh perhitungan resmi** | contoh Kep. Dirjen 273/1996 dan contoh MKJI 1997 | sudah ada di `docs/sources/` | dua contoh | uji regresi kalkulator (c = 70 s, g = 28/30 s, C = 824, DS = 0,44) |

**Prioritas bila waktu terbatas:** D1.1, lalu D1.2 untuk satu pendekat, lalu D1.5 untuk satu klip siang, lalu D1.6 sampai D1.8. Dengan data itu alur ujung ke ujung sudah bisa didemokan untuk satu pendekat, dan pendekat lain menyusul.

## T2 — Vision Tracker dan Optimasi Simpang (presisi)

| # | Data | Isi dan format | Cara mendapatkan | Jumlah minimum | Dipakai untuk |
|---|---|---|---|---|---|
| D2.1 | **Rekaman satu simpang lengkap** | semua lengan pada periode yang sama; format sama dengan D1.2 | rekaman sendiri serentak dari beberapa titik, rekaman yang diserahkan pihak lain, atau rekaman Dishub setelah MoU | puncak pagi, siang, dan puncak sore pada satu hari kerja; idealnya satu hari penuh 06.00 sampai 20.00, ditambah satu hari akhir pekan bila ada | optimasi per periode, dashboard, laporan kajian |
| D2.2 | **Klip kondisi tambahan** | klip malam dan hujan dari simpang target atau simpang lain | seperti D1.3 | dua klip per kondisi | kelulusan akurasi malam dan hujan |
| D2.3 | **Hitungan manual per kondisi** | seperti D1.5, ditambah arah gerakan (lurus, belok kiri, belok kanan) | dihitung tim dengan alat hitung cepat di aplikasi (F-T2-150) | minimal empat potongan 15 menit per kondisi | laporan akurasi per kelas, arah, dan kondisi |
| D2.4 | **Zona hambatan samping** | panjang segmen jalan yang terlihat kamera (m), sisi jalan, lokasi akses keluar-masuk | diukur dari citra satelit dan ditandai di wizard | setiap pendekat | frekuensi hambatan samping per 200 m per jam dan kelasnya |
| D2.5 | **Area kepala lampu** | kepala lampu terlihat di salah satu kamera; bila tidak ada, klip tambahan yang mengarah ke lampu | ditandai di wizard; cadangan berupa stopwatch seperti D1.8 | satu kepala lampu per fase | waktu eksisting otomatis (F-T2-148) |
| D2.6 | **Jaringan simulasi** | potongan OpenStreetMap di sekitar simpang, dilengkapi konfigurasi simpang | diunduh dan dibangun otomatis | satu area | validasi SUMO |
| D2.7 | **Parameter ekonomi** | UMK kota, harga BBM (bensin dan solar), okupansi rata-rata per kelas, konsumsi BBM saat diam, faktor emisi | sumber resmi terbuka (SK Gubernur UMK, harga BBM resmi, pedoman emisi) | nilai tahun berjalan | manfaat rupiah (F-T2-164) |
| D2.8 | **Parameter kebijakan** | hijau minimum, siklus maksimum, DJ target (bawaan 0,85), waktu penyeberangan | ditanyakan ke Dishub atau memakai nilai bawaan PKJI | satu set per simpang | batas keselamatan mode optimasi |
| D2.9 | **Studi lama untuk uji regresi MKJI** (opsional) | perhitungan kinerja simpang dengan MKJI 1997 beserta hasilnya | naskah tugas akhir di `docs/sources/` (lokal, tidak dipush) atau laporan kajian Dishub | satu studi | uji regresi mode MKJI (F-T2-162) |
| D2.10 | **Jawaban kuesioner `12`** | merek dan protokol controller, jaringan, kamera, kemampuan ekspor NVR | Dishub dan satu sampai dua vendor | satu set | persiapan MoU dan T3 |

## T3 — Deteksi Kejadian dan Pemantauan Operasional (perkiraan; memerlukan MoU)

| # | Data | Perkiraan isi | Sumber | Dipakai untuk |
|---|---|---|---|---|
| D3.1 | Stream kamera Dishub yang ditunjuk | RTSP atau HLS lewat VPN; pilot terbatas, tidak 24 jam | Dishub (MoU) | pilot live, kesehatan kamera |
| D3.2 | Rekaman berlabel kejadian | ambulans, damkar, pengawalan, kendaraan mogok, dugaan kecelakaan, lawan arah, terobos merah, parkir di zona larangan | rekaman Dishub dan video publik (dicatat di D1.1) | data latih dan uji deteksi kejadian |
| D3.3 | Rekaman angkot dan pikap | klip dengan jumlah angkot dan pikap memadai | rekaman sendiri dan video publik | kelas baru dan penalaan akurasi 95% dan 90% |
| D3.4 | Rekaman sebelum dan sesudah penerapan jadwal | periode dan hari yang setara, ditambah hitungan manual pembanding | Dishub dan tim | uji lapangan sebelum-sesudah (F-T3-168) |
| D3.5 | Akses baca status controller dan dokumentasi protokol | status fase dan detektor, manual atau ICD vendor | Dishub dan vendor (NDA) | controller baca-saja, validasi nyala lampu |
| D3.6 | Riwayat gangguan dan keluhan satu tahun | tiket, waktu respons, jenis kerusakan | Dishub dan CRM kota | tiket dan matriks diagnosis |
| D3.7 | Jadwal resmi dan SK penetapan | dokumen jadwal tiap simpang | Dishub | pembanding rekomendasi, ekspor lembar jadwal |
| D3.8 | Inventaris aset dan jadwal pemeliharaan | perangkat, tahun pasang, kondisi, kontrak | Dishub | jadwal pemeliharaan berkala |
| D3.9 | Survei lalu lintas Dishub (LHR, kecepatan) | laporan satu sampai dua tahun terakhir | Dishub | laporan V/C dan kecepatan |
| D3.10 | Data kecelakaan dan pelanggaran agregat | tabel per simpang per tahun | Polres (perjanjian) | dashboard keselamatan |

## T4 — Kendali Adaptif Terpadu (perkiraan)

| # | Data | Sumber |
|---|---|---|
| D4.1 | Hitungan dan antrian waktu nyata dari edge di semua simpang kritis | perangkat lapangan sendiri |
| D4.2 | Log kejadian resolusi tinggi controller | controller dan edge |
| D4.3 | AVL operator bus (posisi, rute, jadwal, headway) | operator bus (perjanjian) |
| D4.4 | CAD pemadam dan ambulans (unit, rute, posisi) | Damkar, 112, 119 (perjanjian) |
| D4.5 | Status tindak lanjut ETLE (hanya baca) dan dokumen antarmuka Polri | Polda atau Polres (Perpol 8/2023) |
| D4.6 | Data pelat dari kamera ANPR, hanya setelah DPIA diperbarui | kamera ANPR sendiri |
| D4.7 | Bapenda dan DLH (kueri status pajak dan uji emisi) | instansi terkait (perjanjian) |
| D4.8 | Data tol, cuaca, dan kualitas udara | pengelola tol, BMKG, DLH |
| D4.9 | Riwayat volume minimal satu tahun | sistem sendiri, untuk prediksi 15 sampai 60 menit |
| D4.10 | Data kedatangan dan waktu tempuh antarsimpang | sistem sendiri dan GPS logger, untuk offset dasar |

## T5 — Platform Mobilitas Kota (perkiraan)

| # | Data | Sumber |
|---|---|---|
| D5.1 | Data banyak kota dengan skema yang sama | kota-kota pembeli |
| D5.2 | Data probe atau GPS dan OD untuk optimasi koridor, jaringan, dan twin kota | pemda atau mitra data |
| D5.3 | Akumulasi kendaraan kawasan untuk pengendalian perimeter | kamera dan probe |
| D5.4 | Data kebijakan TDM (ruas dan jam ganjil-genap atau ERP, pengecualian) | Pergub dan Perwal |
| D5.5 | Data terbuka yang diterbitkan kembali (LOS, waktu tempuh, log prioritas yang dianonimkan) | sistem sendiri |
| D5.6 | Algoritma pihak ketiga dan data ujinya | universitas dan vendor |

## Format umum

CSV UTF-8 dengan pemisah koma dan titik desimal. Satuan meter, detik, dan kendaraan. Satu berkas per jenis data, dengan nama berhuruf kecil tanpa spasi. Nama berkas video mengikuti pola `S01_U_pagi_puncak_20260915.mp4` (simpang, pendekat, kondisi, periode, tanggal). Templat kolom dibuat di `packages/schemas/` pada sprint pertama.

## Lampiran — daftar cek pengumpulan T1 dan T2

T1
- [ ] Pilih satu simpang target dan isi `simpang.csv` (D1.6).
- [ ] Kumpulkan rekaman semua pendekat, minimal 1 jam puncak dan 1 jam non-puncak siang (D1.2), lalu catat di register (D1.1).
- [ ] Kumpulkan klip data latih: dua puncak, satu non-puncak, satu malam, satu hujan (D1.3).
- [ ] Tandai satu klip uji per kondisi dan hitung manual per kelas per 15 menit (D1.4, D1.5).
- [ ] Ukur geometri tiap pendekat dari citra satelit dan verifikasi di lapangan (D1.7).
- [ ] Catat fase dan waktu lampu eksisting dari rekaman (D1.8).
- [ ] Simpan semua berkas di `data/pilot/T1/` di laptop; video tidak masuk repositori.

T2
- [ ] Rekaman semua lengan pada periode yang sama: puncak pagi, siang, puncak sore (D2.1).
- [ ] Klip malam dan hujan tambahan (D2.2) dan hitungan manual per kondisi dengan arah gerakan (D2.3).
- [ ] Panjang zona hambatan samping dan area kepala lampu ditandai di wizard (D2.4, D2.5).
- [ ] Parameter ekonomi dan kebijakan terbaru (D2.7, D2.8).
- [ ] Kuesioner `12` dikirim ke Dishub dan vendor (D2.10).
