# 16 — Panduan Data Latih Vision Tracker

Disusun 14 September 2026 untuk pekerjaan T1 dan T2. Dokumen ini menjelaskan langkah menyiapkan data latih, melatih, dan menguji model deteksi kendaraan untuk Vision Tracker IRAMA dengan cara pra-label otomatis yang kemudian dikoreksi manusia. Semua alat yang dipakai gratis atau open-source, sesuai keputusan tanpa pengadaan sampai T3 selesai. Angka waktu, kecepatan, dan kuota layanan cloud adalah perkiraan per 2025-2026 dan dapat berubah, sehingga perlu dicek ulang di halaman resmi masing-masing alat.

## Ringkasan

Hasil yang dituju adalah model deteksi enam kelas yang, bersama tracker dan garis hitung, menghasilkan hitungan kendaraan per kelas per 15 menit. Target akurasi hitungan untuk T1 dan T2 sekitar 90% pada siang hari dan sekitar 85% pada malam atau hujan. Target ini sengaja diturunkan sekitar 5 poin dari target akhir (95% siang dan 90% malam atau hujan) agar pekerjaan data selesai cepat; penalaan bertahap dimulai di T3.

Keluaran akhir T2 berupa dataset berlabel versi v0.2 berisi sekitar 2.000 sampai 3.000 gambar, bobot model dalam format ONNX yang berjalan di laptop tim, dan tabel akurasi hitungan per kondisi (pagi atau siang, malam, hujan; puncak dan non-puncak).

Perkiraan total kerja sekitar 55 sampai 76 jam orang, sesuai anggaran jam kerja di bagian jadwal. Bila dua orang bekerja paruh waktu, kalendernya sekitar tiga minggu.

Cloud gratis bisa dipakai untuk pelatihan. Rekomendasinya adalah Kaggle Notebooks sebagai tempat utama untuk pra-label dan pelatihan, karena menyediakan GPU gratis dengan kuota mingguan, dan Google Colab versi gratis sebagai cadangan. Rekaman Dishub yang nanti diperoleh lewat MoU tetap diproses dan dilatih di laptop agar data tidak keluar dari lingkungan yang disepakati.

Hal yang sengaja dikorbankan demi kecepatan adalah pemisahan angkot dan pikap dari kelas mobil, kondisi malam tanpa penerangan dan hujan sangat lebat, sudut kamera yang tidak lazim, serta penyamaran wajah dan pelat pada frame data latih yang berasal dari video publik. Semuanya dijadwalkan kembali di T3. Penyamaran pada cuplikan yang disimpan produk tetap berlaku mulai T2 (F-T2-151).

### Kelas yang dilabel dan padanannya

| Kelas | Contoh yang termasuk | Padanan PKJI 2023 | Kegunaan |
|---|---|---|---|
| motor | sepeda motor, termasuk berboncengan, ojek, motor bermuatan | SM | arus lalu lintas |
| mobil | sedan, MPV, SUV, taksi, angkot, mikrobus seperti Elf, pikap | MP | arus lalu lintas (angkot dan pikap dipisah di T3) |
| bus | bus kecil, sedang, besar, bus kota dan bus antarkota | KS | arus lalu lintas |
| truk | truk enam roda ke atas, truk boks sedang dan besar, truk gandeng | KS | arus lalu lintas |
| kendaraan tak bermotor | sepeda, becak, gerobak, delman | KTB | rasio KTB dan hambatan samping (bobot 0,4) |
| pejalan kaki | orang berjalan di badan jalan atau menyeberang | tidak dikonversi | hambatan samping (bobot 0,5) |

Dua jenis hambatan samping lain, yaitu kendaraan berhenti atau parkir (bobot 1,0) dan kendaraan keluar-masuk sisi jalan (bobot 0,7), tidak dilabel sebagai kelas. Keduanya dihitung dari perilaku lintasan kendaraan hasil tracker (kendaraan diam di zona tertentu, atau lintasan yang memotong batas sisi jalan).

## Gambaran alur kerja

| Tahap | Alat | Keluaran | Perkiraan waktu |
|---|---|---|---|
| A. Mencatat sumber video | spreadsheet atau CSV | register sumber | 2-3 jam |
| B. Mengambil frame | ffmpeg, Python, ImageHash | folder frame per kondisi | 3-4 jam |
| C. Pra-label otomatis | Kaggle (GPU gratis), RF-DETR, detektor open-vocabulary | berkas prediksi untuk Label Studio | 2-3 jam |
| D. Koreksi manusia | Label Studio | label COCO v0.1 | 8-12 jam (dua orang) |
| E. Putaran belajar aktif | Kaggle, Label Studio | label COCO v0.2 | 10-16 jam |
| F. Pelatihan | Kaggle (RF-DETR kecil atau YOLOX-tiny) | bobot model dan berkas ONNX | 3-6 jam pengawasan |
| G. Uji kecepatan | laptop, ONNX Runtime | ms per frame per model | 2 jam |
| H. Uji akurasi hitungan | Vision Tracker, lembar hitung manual | tabel akurasi per kondisi | 10-16 jam |
| I. Penyimpanan dan versi | folder terstruktur, Kaggle dataset privat, git | dataset v0.1 dan v0.2 | 1-2 jam |

## Persiapan alat

| Alat | Fungsi | Lisensi | Catatan |
|---|---|---|---|
| Python 3.11 atau 3.12 | menjalankan skrip bantu | PSF | pakai virtual environment terpisah per proyek |
| ffmpeg | memotong video dan mengambil frame | LGPL/GPL (tergantung build) | alat bantu kerja, tidak dibundel ke produk |
| ImageHash dan Pillow | membuang frame yang hampir sama | BSD dan HPND | pasang dengan pip |
| Label Studio Community | koreksi label | Apache-2.0 | pasang dengan pip, berjalan lokal di laptop |
| CVAT | alternatif alat anotasi | MIT | Docker lokal, atau versi cloud gratis yang berbatas |
| RF-DETR (paket rfdetr) | pra-label dan model utama | Apache-2.0 | dari Roboflow; periksa berkas lisensi untuk tiap varian |
| YOLOX | model ringan alternatif untuk CPU | Apache-2.0 | dari Megvii |
| Grounding DINO atau OWLv2 | pra-label kelas yang tidak ada di dataset COCO | Apache-2.0 | tersedia lewat pustaka Hugging Face transformers |
| supervision (termasuk ByteTrack) | tracker dan garis hitung | MIT | dari Roboflow |
| ONNX Runtime | menjalankan model di laptop | MIT | paket onnxruntime (CPU) atau onnxruntime-directml (iGPU Radeon) |
| deface (opsional) | menyamarkan wajah | MIT | dipakai bila data akan diunggah ke cloud |
| Akun Kaggle | GPU gratis untuk pra-label dan pelatihan | layanan gratis | GPU dan akses internet di notebook memerlukan verifikasi nomor telepon |
| Akun Google (Colab) | GPU cadangan | layanan gratis | ketersediaan GPU tidak dijamin |
| git | versi label, register, dan hasil uji | GPL-2.0 | video dan frame tidak dimasukkan ke git |

Catatan kuota (per 2025-2026, dapat berubah, cek halaman resmi):

- Kaggle memberi kuota GPU gratis mingguan sekitar 30 jam, dengan batas durasi per sesi (sekitar 9 sampai 12 jam) dan penyimpanan keluaran notebook yang terbatas. Kuota ini cukup untuk beberapa putaran pelatihan model kecil setiap minggu.
- Google Colab versi gratis biasanya memberi GPU T4 bila tersedia, dengan batas durasi sesi dan pemutusan otomatis saat tidak aktif. Karena tidak ada jaminan, Colab diposisikan sebagai cadangan.

Catatan lisensi pustaka tambahan. Beberapa pustaka populer berpindah ke lisensi AGPL pada 2025, termasuk turunan pustaka augmentasi gambar tertentu. Sebelum menambah pustaka apa pun, periksa berkas lisensinya. Keluarga Ultralytics YOLO (AGPL) tidak dipakai sesuai keputusan proyek.

## Langkah kerja

### Langkah A. Mengumpulkan dan mencatat sumber video

**Tujuan.** Setiap video yang dipakai tercatat asal, kondisi, dan kegunaannya, sehingga data latih dan data uji tidak tercampur dan asal data bisa dipertanggungjawabkan saat produk dijual.

**Cara.**
1. Kumpulkan klip dari rekaman sendiri, rekaman yang dibagikan pihak lain, atau YouTube. Untuk YouTube, unduh memakai alat pengunduh open-source (misalnya yt-dlp) dan simpan tautan aslinya di register.
2. Isi satu baris register untuk setiap klip. Kolom yang diisi adalah nama file, sumber atau tautan, nama simpang, pendekat (utara, selatan, timur, barat), kondisi (pagi, siang, sore, malam, hujan), periode (puncak atau non-puncak), resolusi, frame rate, durasi, lisensi atau izin, tanggal rekam, tanggal dicatat, dan kegunaan (latih, uji, atau demo).
3. Pilih satu klip untuk setiap kondisi utama sebagai klip uji. Klip uji dipakai untuk menghitung akurasi dan tidak boleh ada satu frame pun darinya yang masuk data latih. Bila memungkinkan, klip uji diambil dari simpang yang berbeda dengan klip latih.
4. Simpan video mentah di folder khusus di laptop. Bila tim sudah memiliki disk eksternal, cadangkan ke sana; bila belum, jangan membeli (nol pengadaan sampai T3), cukup simpan register sumber dan tautannya sehingga video publik dapat diunduh ulang, lalu hapus video yang sudah selesai diolah.

```
file,sumber_url,simpang,pendekat,kondisi,periode,resolusi,fps,durasi_menit,lisensi_izin,tanggal_rekam,tanggal_catat,kegunaan
```

**Kriteria selesai.** Register terisi untuk semua klip. Untuk data latih tersedia minimal dua klip pagi atau siang puncak, satu klip non-puncak, satu klip malam, dan satu klip hujan. Untuk data uji tersedia satu klip per kondisi yang ditandai "uji".

**Perkiraan waktu.** 2 sampai 3 jam.

### Langkah B. Mengambil frame secara efisien

**Tujuan.** Mendapatkan gambar yang beragam dengan jumlah secukupnya. Frame yang berdekatan dalam video hampir identik, sehingga melabel semuanya membuang waktu.

**Cara.**
1. Ambil satu frame setiap 2 detik untuk klip ramai dan malam atau hujan, serta satu frame setiap 3 detik untuk klip sepi. Perkecil lebar gambar ke 1280 piksel agar ringan diunggah.
2. Beri nama file yang menjelaskan asalnya, misalnya `S01_U_pagi_puncak_000123.jpg` (kode simpang, pendekat, kondisi, periode, nomor frame).
3. Buang frame yang hampir sama dengan membandingkan hash perseptual. Selisih hash 6 atau kurang dianggap mirip.
4. Kelompokkan frame per kondisi dan per sudut kamera, lalu ambil sesuai target tabel di bawah. Klip yang ditandai "uji" tidak ikut diproses di langkah ini.

```
ffmpeg -i klip.mp4 -vf "fps=1/2,scale=1280:-2" -q:v 2 frames/S01_U_pagi_puncak_%06d.jpg
```

```python
from PIL import Image
import imagehash, pathlib
riwayat = []
for p in sorted(pathlib.Path("frames").glob("*.jpg")):
    h = imagehash.phash(Image.open(p))
    if any(h - lama <= 6 for lama in riwayat[-50:]):
        p.unlink()          # hapus frame yang hampir sama dengan 50 frame terakhir
    else:
        riwayat.append(h)
```

| Kondisi | Putaran awal (v0.1) | Total akhir T2 (v0.2) | Catatan |
|---|---|---|---|
| Pagi atau siang, puncak | 300 | 900 | motor padat, prioritas utama |
| Pagi atau siang, non-puncak | 150 | 400 | objek lebih jarang, cepat dikoreksi |
| Malam | 200 | 500 | silau lampu kendaraan |
| Hujan | 150 | 400 | pantulan dan buram |
| Sudut atau simpang lain | 50 | 300 | menambah keragaman |
| Jumlah | 850 | 2.500 | |

**Kriteria selesai.** Jumlah frame per kondisi mendekati target putaran awal, tidak ada frame dari klip uji, dan nama file konsisten.

**Perkiraan waktu.** 3 sampai 4 jam.

### Langkah C. Pra-label otomatis di Kaggle

**Tujuan.** Mesin menggambar kotak dan menebak kelas lebih dulu, sehingga manusia cukup memperbaiki. Menghapus kotak yang salah jauh lebih cepat daripada menggambar kotak baru, karena itu ambang keyakinan pra-label dibuat agak rendah.

**Cara.**
1. Kompres frame satu batch menjadi berkas zip, lalu unggah ke Kaggle sebagai dataset privat (menu Datasets, New Dataset, atur visibilitas Private).
2. Buat notebook baru, tambahkan dataset tadi, lalu di pengaturan notebook pilih akselerator GPU dan nyalakan akses internet (butuh verifikasi nomor telepon akun).
3. Pasang paket rfdetr dan supervision sesuai petunjuk repositori resminya. Pustaka transformers umumnya sudah tersedia di Kaggle.
4. Jalankan model RF-DETR ukuran besar (misalnya varian Base atau Large) yang sudah dilatih pada dataset COCO dengan ambang keyakinan 0,30 sampai 0,35. Kelas COCO dipetakan ke kelas IRAMA: motorcycle menjadi motor, car menjadi mobil, bus menjadi bus, truck menjadi truk, bicycle menjadi kendaraan tak bermotor, dan person menjadi pejalan kaki.
5. Terapkan dua aturan otomatis. Kotak orang yang titik tengahnya berada di dalam kotak motor atau sepeda dianggap pengendara dan dibuang. Kotak "truk" yang kecil (pikap sering tertebak sebagai truck di COCO) diberi tanda untuk diperiksa manusia.
6. Untuk becak dan gerobak yang tidak ada di COCO, jalankan detektor open-vocabulary (OWLv2 atau Grounding DINO) dengan kata kunci seperti "rickshaw", "pedicab", "cart", dan "pushcart". Kotak yang lolos ambang 0,30 dan tidak bertumpuk dengan kotak lain diberi kelas kendaraan tak bermotor. Detektor ini lambat, jadi cukup dijalankan pada frame dari lokasi yang memang memiliki becak atau gerobak.
7. Simpan hasilnya sebagai berkas tugas Label Studio yang berisi "predictions". Koordinat kotak di Label Studio ditulis dalam persen terhadap lebar dan tinggi gambar.
8. Unduh berkas hasil dari tab Output notebook (folder `/kaggle/working`).

Konfigurasi label proyek Label Studio yang dipakai di langkah D:

```xml
<View>
  <Image name="image" value="$image"/>
  <RectangleLabels name="label" toName="image">
    <Label value="motor"/><Label value="mobil"/><Label value="bus"/>
    <Label value="truk"/><Label value="kendaraan tak bermotor"/><Label value="pejalan kaki"/>
  </RectangleLabels>
</View>
```

Contoh satu kotak prediksi di dalam berkas tugas:

```json
{"data": {"image": "/data/local-files/?d=frames/S01_U_pagi_puncak_000123.jpg"},
 "predictions": [{"model_version": "rfdetr-coco-v0", "result": [
   {"from_name": "label", "to_name": "image", "type": "rectanglelabels",
    "original_width": 1280, "original_height": 720, "score": 0.62,
    "value": {"x": 41.2, "y": 55.0, "width": 3.1, "height": 6.4, "rotation": 0,
              "rectanglelabels": ["motor"]}}]}]}
```

**Kriteria selesai.** Setiap frame punya entri prediksi, dan pemeriksaan acak 20 gambar menunjukkan kotak berada di posisi yang benar.

**Perkiraan waktu.** 2 sampai 3 jam, sebagian besar untuk persiapan. Pemakaian GPU diperkirakan kurang dari 30 menit untuk sekitar 1.000 gambar.

### Langkah D. Koreksi manusia di Label Studio

**Tujuan.** Menghasilkan label yang benar dan konsisten dengan kecepatan tinggi.

**Cara memasang dan membuka proyek (PowerShell di laptop).**

```
pip install label-studio
$env:LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED="true"
$env:LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="C:\irama-data"
label-studio start
```

1. Buka alamat lokal yang ditampilkan (biasanya `http://localhost:8080`), buat akun lokal, lalu buat proyek baru dan tempel konfigurasi label dari langkah C.
2. Di pengaturan proyek, tambahkan Local Storage yang menunjuk ke folder frame di bawah `C:\irama-data`, lalu impor berkas tugas berisi prediksi.
3. Aktifkan opsi untuk menampilkan prediksi sebagai pra-anotasi, sehingga setiap gambar terbuka dengan kotak tebakan mesin.
4. Pakai tombol angka 1 sampai 6 untuk memilih kelas dan tombol pintas kirim yang ditampilkan Label Studio agar tangan tidak perlu berpindah ke tetikus.

**Aturan anotasi singkat.**
- Kotak dibuat rapat mengelilingi objek.
- Objek yang terpotong tepi gambar atau tertutup objek lain tetap dilabel bila lebih dari separuhnya terlihat.
- Motor berboncengan atau bermuatan cukup satu kotak yang mencakup motor dan penumpangnya.
- Pengendara motor, sepeda, dan becak tidak dilabel sebagai pejalan kaki.
- Orang yang menuntun sepeda cukup dilabel sepedanya sebagai kendaraan tak bermotor.
- Kendaraan yang parkir atau berhenti tetap dilabel, karena diperlukan untuk hambatan samping.
- Angkot dan pikap dilabel sebagai mobil pada T1 dan T2.
- Pantulan di kaca, gambar di baliho, dan kendaraan di layar tidak dilabel.
- Bila ragu antara bus dan truk, pilih yang paling mirip lalu tambahkan komentar pada gambar tersebut.

**Pembagian kerja dua orang.** Setiap orang menjalankan Label Studio di laptopnya sendiri dengan konfigurasi label yang sama persis, lalu mengerjakan kelompok frame yang berbeda (misalnya dibagi per simpang atau per kondisi). Hasilnya diekspor dalam format COCO dan digabung memakai skrip penggabung sederhana yang disiapkan di repositori saat sprint pertama. Setiap orang memeriksa 5% gambar milik rekannya. Bila lebih dari 10% gambar yang diperiksa perlu diperbaiki, aturan anotasi diperjelas sebelum melanjutkan.

**Kecepatan yang dituju.** Sekitar 15 sampai 25 detik per gambar untuk kondisi normal, dan 40 sampai 60 detik untuk jam puncak yang sangat padat motor.

**Kriteria selesai.** Semua gambar batch v0.1 terkirim, pemeriksaan silang selesai, dan berkas COCO v0.1 tersimpan.

**Perkiraan waktu.** 8 sampai 12 jam untuk sekitar 850 gambar, dibagi dua orang.

### Langkah E. Putaran belajar aktif

**Tujuan.** Menambah data dengan usaha koreksi sekecil mungkin, dengan cara hanya mengoreksi gambar yang paling membingungkan model.

**Cara.**
1. Latih model kecil versi v0.1 dari label hasil langkah D memakai pengaturan cepat di langkah F (jumlah epoch dikurangi).
2. Jalankan model v0.1 pada batch frame baru (sekitar 1.000 gambar dari kondisi yang masih kurang, terutama malam dan hujan).
3. Hitung skor keraguan setiap gambar, misalnya jumlah kotak dengan keyakinan antara 0,30 dan 0,60. Urutkan dari yang paling ragu.
4. Koreksi penuh sekitar separuh gambar yang paling ragu. Separuh sisanya cukup dilihat sekilas (sekitar 10 detik) dan diterima bila tidak ada kesalahan mencolok. Jalan pintas ini disengaja dan menjadi sumber turunnya sekitar 5 poin akurasi yang sudah disetujui.
5. Ulangi sekali lagi untuk putaran kedua. Putaran ketiga hanya dijalankan bila hasil langkah H masih jauh dari target.

**Kriteria selesai.** Dataset v0.2 berisi sekitar 2.500 gambar dengan sebaran kondisi sesuai tabel di langkah B.

**Perkiraan waktu.** 10 sampai 16 jam koreksi untuk dua putaran, ditambah dua kali pelatihan.

### Langkah F. Pelatihan di Kaggle

**Tujuan.** Menghasilkan model yang cukup akurat dan cukup cepat untuk laptop tim.

**Cara.**
1. Bagi data menjadi latih, validasi, dan uji dengan perbandingan sekitar 80:10:10 berdasarkan klip atau potongan waktu. Pembagian acak per frame membuat frame hampir kembar muncul di data latih dan validasi sehingga nilai validasi terlihat bagus padahal model belum tentu andal.
2. Untuk RF-DETR, susun folder `train`, `valid`, dan `test` yang masing-masing berisi gambar dan berkas `_annotations.coco.json`, sesuai format yang diminta repositori resminya. Unggah sebagai dataset privat Kaggle.
3. Latih varian kecil RF-DETR (misalnya Nano atau Small) untuk dipakai di laptop. Pengaturan awal yang wajar adalah 30 sampai 50 epoch, batch 4 dengan akumulasi gradien 4, dan resolusi bawaan varian tersebut. Nama kelas varian dan argumen dapat berbeda antar versi paket, jadi ikuti README repositori.
4. Sebagai pembanding yang lebih ringan untuk CPU, latih YOLOX-tiny dari bobot pra-latih resminya selama 100 sampai 150 epoch pada resolusi 416 sampai 640, dengan berkas konfigurasi (exp) yang menunjuk ke dataset dan jumlah kelas enam.
5. Tambahkan variasi gelap, buram, dan kontras rendah bila paket pelatihan menyediakannya, agar model lebih tahan kondisi malam dan hujan.
6. Ekspor model terbaik ke ONNX memakai fungsi atau skrip ekspor yang disediakan masing-masing repositori, lalu unduh berkas ONNX, berkas konfigurasi, dan log pelatihan.

```python
from rfdetr import RFDETRSmall      # varian kecil; nama kelas mengikuti versi paket
model = RFDETRSmall()
model.train(dataset_dir="/kaggle/input/irama-v02", epochs=40,
            batch_size=4, grad_accum_steps=4, output_dir="/kaggle/working/rfdetr_v02")
```

```
python tools/train.py -f exps/example/custom/yolox_tiny_irama.py -d 1 -b 16 --fp16 -o -c yolox_tiny.pth
python tools/export_onnx.py -f exps/example/custom/yolox_tiny_irama.py -c best_ckpt.pth --output-name yolox_tiny_irama.onnx
```

**Cara menjaga kuota Kaggle.**
- Jalankan pelatihan dengan menyimpan versi notebook dan menjalankan semua sel di latar belakang, sehingga peramban tidak perlu tetap terbuka.
- Matikan GPU saat hanya menyunting kode atau memeriksa hasil.
- Simpan checkpoint ke `/kaggle/working` agar bisa dilanjutkan bila sesi terputus.
- Mulai dengan epoch sedikit untuk memastikan alur berjalan, baru jalankan pelatihan penuh.
- Bila kuota habis, pindahkan notebook ke Colab. Pilihan terakhir adalah melatih YOLOX-tiny semalaman di laptop.

**Kriteria selesai.** Berkas ONNX dan log pelatihan tersimpan, dan nilai mAP validasi tercatat sebagai indikator awal.

**Perkiraan waktu.** Pelatihan sekitar 1 sampai 3 jam per putaran di GPU Kaggle. Waktu pengawasan orang sekitar 3 sampai 6 jam untuk seluruh putaran.

### Langkah G. Uji kecepatan di laptop

**Tujuan.** Memastikan model yang dipilih cukup cepat untuk laptop tim (AMD Ryzen 7 7730U, RAM 32 GB, GPU terintegrasi Radeon).

**Cara.**
1. Pasang ONNX Runtime versi CPU, dan bila ingin mencoba iGPU pasang versi DirectML.
2. Jalankan setiap model ONNX pada 200 frame, catat rata-rata milidetik per frame, lalu ulangi dengan penyedia CPU dan DirectML.
3. Tambahkan waktu tracker dan garis hitung (biasanya kecil dibanding waktu deteksi).
4. Terapkan aturan pemilihan. Vision Tracker mengolah sekitar 10 frame per detik video. Untuk rekaman, pemrosesan minimal dua kali waktu nyata berarti total paling lama sekitar 50 milidetik per frame. Untuk stream, minimal 10 frame per detik berarti paling lama sekitar 100 milidetik per frame per stream.
5. Bila varian RF-DETR terlalu lambat di CPU, pakai YOLOX-tiny untuk operasi T1 dan T2, dan simpan RF-DETR untuk pra-label serta untuk perangkat ber-GPU di tahap berikutnya.

```
pip install onnxruntime
pip install onnxruntime-directml
```

Perkiraan kasar yang perlu dibuktikan lewat pengukuran adalah YOLOX-tiny sekitar 15 sampai 35 milidetik per frame dan varian kecil RF-DETR sekitar 50 sampai 150 milidetik per frame di CPU laptop ini.

**Kriteria selesai.** Tabel milidetik per frame dan frame per detik untuk setiap model dan penyedia, beserta keputusan model yang dipakai.

**Perkiraan waktu.** 2 jam.

### Langkah H. Uji akurasi hitungan

**Tujuan.** Mengukur akurasi dengan ukuran yang dipakai untuk kelulusan, yaitu hitungan per kelas per 15 menit. Nilai mAP dari langkah F hanya indikator tambahan, karena yang dipakai modul optimasi adalah hitungan kendaraan yang melintas.

**Cara membuat hitungan referensi manual.**
1. Untuk setiap klip uji, tentukan garis hitung pada layar yang sama persis dengan garis hitung yang dipakai sistem.
2. Putar klip dan hitung kendaraan yang melintasi garis selama 15 menit. Lakukan dalam dua putaran: putaran pertama khusus motor pada kecepatan normal, putaran kedua untuk kelas lain pada kecepatan 1,5 sampai 2 kali.
3. Catat dengan lembar hitung per kelas atau skrip penghitung tombol keyboard sederhana yang merekam setiap tekanan tombol beserta waktunya.
4. Untuk pejalan kaki dan kendaraan tak bermotor, hitung kejadian di zona pengamatan hambatan samping sesuai definisi PKJI.

**Cara menghitung dengan sistem.** Jalankan Vision Tracker (detektor, ByteTrack, dan garis hitung dari pustaka supervision) pada klip yang sama. Hitungan per kelas diperoleh dengan menyaring deteksi per kelas sebelum garis hitung, atau memakai fitur hitung per kelas bila tersedia pada versi supervision yang dipakai.

**Rumus akurasi.** Untuk kelas k pada satu klip, akurasi = 1 − |S − M| / M, dengan S hitungan sistem dan M hitungan manual. Bila ada beberapa potongan 15 menit, pakai 1 − Σ|S − M| / ΣM agar kesalahan lebih dan kurang tidak saling menghapus. Untuk kelas yang jumlahnya kecil (M kurang dari 20 per 15 menit), persentase menjadi tidak stabil, sehingga kriteria diganti menjadi selisih absolut paling banyak 2 kendaraan.

| Kondisi | Kelas | Hitung manual | Hitung sistem | Akurasi |
|---|---|---|---|---|
| Siang puncak | motor | | | |
| Siang puncak | mobil | | | |
| Malam | motor | | | |
| Hujan | mobil | | | |

**Kriteria lulus T1 dan T2.** Setiap kelas mencapai akurasi sekitar 90% pada klip siang dan sekitar 85% pada klip malam atau hujan, atau memenuhi aturan selisih absolut untuk kelas yang jumlahnya kecil.

**Analisis kesalahan.** Catat pola kesalahan yang paling sering, misalnya satu kendaraan terhitung dua kali karena identitas tracker berganti, motor yang berhimpitan terlewat, atau truk tertebak sebagai bus. Pola ini menentukan frame apa yang ditambahkan pada putaran berikutnya dan parameter tracker apa yang disetel.

**Perkiraan waktu.** 10 sampai 16 jam, sebagian besar untuk hitungan manual.

### Langkah I. Penyimpanan dan versi dataset

**Tujuan.** Dataset dan model bisa dilacak, dipakai ulang, dan dipulihkan bila laptop bermasalah.

**Struktur folder yang disarankan di laptop.**

```
C:\irama-data\
  video_mentah\          tidak masuk git; cadangan ke disk eksternal bila sudah dimiliki
  frames\v0.1\  frames\v0.2\
  label\v0.1\coco.json  label\v0.2\coco.json
  split\v0.2\train\  valid\  test\
  uji_hitungan\referensi_manual.csv  hasil_sistem.csv
  model\v0.2\*.onnx
  register_sumber.csv  CHANGELOG.md
```

**Aturan versi.** v0.1 adalah hasil koreksi putaran awal, v0.2 adalah hasil dua putaran belajar aktif untuk kelulusan T2, dan v0.3 dijadwalkan di T3 saat angkot dan pikap dipisahkan. Setiap versi dicatat di CHANGELOG (jumlah gambar per kondisi, perubahan aturan anotasi, model yang dilatih).

**Tempat penyimpanan.**
- Berkas label, register sumber, dan hasil uji disimpan di repositori git karena ukurannya kecil.
- Frame dan video tidak disimpan di Git LFS. Kuota LFS gratis GitHub sekitar 1 GB dan sudah terpakai sekitar 420 MB oleh bahan acuan, sedangkan frame v0.2 diperkirakan sekitar 500 MB.
- Frame disimpan sebagai dataset privat Kaggle, dengan cadangan di disk eksternal bila sudah dimiliki.
- Berkas model ONNX disimpan di laptop dan di dataset atau model privat Kaggle.
- Rekaman Dishub yang diperoleh lewat MoU tidak diunggah ke layanan cloud mana pun dan dilatih di laptop.

**Perkiraan waktu.** 1 sampai 2 jam.

## Jadwal kerja dua orang

| Minggu | Orang A | Orang B | Keluaran |
|---|---|---|---|
| Minggu pertama | register sumber, ambil frame, pra-label di Kaggle | pasang Label Studio, susun aturan anotasi, mulai koreksi | label v0.1 (sekitar 850 gambar) |
| Minggu kedua | latih model v0.1, prediksi batch baru, uji kecepatan | hitungan referensi manual pada klip uji | batch putaran pertama siap dikoreksi |
| Minggu ketiga | latih model v0.2, jalankan Vision Tracker pada klip uji, isi tabel akurasi | koreksi putaran kedua, analisis kesalahan | label v0.2, model ONNX terpilih, laporan akurasi |

Anggaran jam kerja yang disarankan:
- Koreksi label sekitar 25 sampai 35 jam untuk dua orang.
- Hitungan referensi manual sekitar 10 sampai 16 jam.
- Persiapan, pra-label, pelatihan, uji kecepatan, dan penyimpanan sekitar 20 sampai 25 jam.

Hal yang sengaja ditunda ke T3 untuk menghemat waktu:
- Pemisahan angkot dan pikap dari kelas mobil.
- Malam tanpa penerangan jalan dan hujan sangat lebat.
- Sudut kamera yang tidak lazim (sangat tinggi, sangat rendah, atau lensa mata ikan).
- Objek yang sangat kecil di kejauhan.
- Penyamaran wajah dan pelat pada frame data latih dari video publik (cuplikan yang disimpan produk sudah disamarkan sejak T2).
- Kelas kendaraan prioritas (ambulans, damkar, mobil polisi) untuk deteksi anomali.
- Label tambahan untuk antrian dan okupansi per lajur.

## Risiko dan mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Kuota GPU gratis habis atau GPU tidak tersedia | pelatihan tertunda | pindah ke Colab, kurangi epoch, latih model kecil, laptop semalaman sebagai cadangan terakhir |
| Motor berhimpitan pada jam puncak | motor terlewat atau terhitung ganda | garis hitung di area yang tidak terlalu padat, olah 10 frame per detik, setel parameter ByteTrack, tambah frame puncak pada putaran belajar aktif |
| Kondisi malam dan hujan | akurasi turun | tambah frame malam dan hujan, variasi gelap dan buram saat pelatihan, laporkan akurasi per kondisi secara terpisah |
| Data terlalu banyak dari satu simpang | model gagal di simpang lain | ambil data dari beberapa simpang, bagi data per klip, uji pada klip dari simpang berbeda |
| Hak cipta video YouTube | penggunaan dipersoalkan saat produk dijual | user memutuskan video YouTube boleh dipakai untuk uji dan latih; semua sumber dicatat di register; sebelum penjualan skala besar model dilatih ulang dengan data berizin (rekaman Dishub, rekaman sendiri, video berlisensi Creative Commons); video dan frame tidak disebarkan |
| Lisensi varian model atau pustaka berubah | kewajiban membuka kode | periksa berkas lisensi per varian, hindari pustaka berlisensi AGPL |
| Label hilang karena laptop bermasalah | pekerjaan anotasi terulang | ekspor COCO setiap akhir sesi, simpan ke git (berkas label berukuran kecil) dan ke disk eksternal bila ada |
| Anotasi tidak konsisten antar orang | model bingung pada kelas tertentu | aturan anotasi tertulis, pemeriksaan silang 5%, diskusi singkat tiap akhir minggu |

## Daftar periksa

- Register sumber video terisi dan klip uji per kondisi sudah ditandai.
- Frame putaran awal sesuai target dan tidak ada frame dari klip uji.
- Akun Kaggle terverifikasi, dataset privat terunggah, dan pra-label selesai.
- Label Studio berjalan di kedua laptop dengan konfigurasi label yang sama.
- Label v0.1 selesai dikoreksi dan diperiksa silang 5%.
- Dua putaran belajar aktif selesai dan label v0.2 tersimpan.
- Model kecil terlatih, diekspor ke ONNX, dan kecepatannya diukur di laptop.
- Hitungan referensi manual tersedia untuk setiap klip uji.
- Tabel akurasi per kelas dan per kondisi terisi dan dibandingkan dengan kriteria lulus T1 dan T2.
- Dataset, model, register, dan CHANGELOG tersimpan sesuai aturan versi, dan data Dishub tidak berada di cloud.
