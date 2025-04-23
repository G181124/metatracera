# MetaTraceRA

MetaTraceRA adalah alat forensik metadata berbasis CLI yang cepat, ringan, dan dirancang khusus untuk sistem seperti Kali Linux. Tools ini bekerja real-time tanpa database lokal dan mendukung berbagai tipe file seperti gambar, dokumen, serta memiliki fitur penghapusan metadata.

## Fitur Utama

- Analisis metadata gambar (EXIF)
- Metadata dokumen PDF dan DOCX
- Hashing file (MD5, SHA1, SHA256)
- Informasi teknis file (ukuran, tipe MIME, timestamp)
- Pembersihan metadata gambar
- Dukungan ekspor hasil
- Mode analisis gabungan `--analyze`

## Instalasi

1. Clone repository

```
git clone https://github.com/G181124/metatracera.git
cd metatracera
```

2. Buat virtual environment (opsional tapi disarankan)

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependensi

```
pip install -r requirements.txt
```

## Cara Penggunaan

### Analisis metadata gambar (EXIF)  
Format yang didukung: `.jpg`, `.jpeg`
```
python metatracera.py --file foto.jpg
```

### Metadata dokumen PDF atau DOCX  
Format yang didukung: `.pdf`, `.docx`
```
python metatracera.py --doc dokumen.pdf
python metatracera.py --doc dokumen.docx
```

### Hashing file  
Format yang didukung: semua tipe file
```
python metatracera.py --hash file.zip
```

### Informasi dasar file  
Format yang didukung: semua tipe file
```
python metatracera.py --fileinfo file.png
```

### Deteksi lokasi dari metadata GPS (BETA)  
Format yang didukung: `.jpg`, `.jpeg` (jika memiliki koordinat GPS)
```
python metatracera.py --geolocate gambar.jpg
```

### Hapus metadata dari gambar  
Format yang didukung: `.jpg`, `.jpeg`
```
python metatracera.py --clean gambar.jpg
```

### Analisis lengkap metadata + lokasi GPS  
Format yang didukung: `.jpg`, `.jpeg`
```
python metatracera.py --analyze gambar.jpg
```

### Ekspor hasil ke folder output  
Tambahkan `--export` ke perintah apa pun
```
python metatracera.py --file gambar.jpg --export
```

## Output

Semua hasil akan disimpan otomatis di folder `output/` dengan nama file unik berdasarkan waktu dan nama file sumber.

## Catatan

- `--geolocate` hanya bekerja jika metadata GPS tersedia
- `--clean` hanya berfungsi untuk file gambar (JPEG)
- - Fitur `--geolocate` masih dalam tahap BETA. Hasil bisa berbeda tergantung perangkat, kamera, dan jenis kompresi file.

Gunakan MetaTraceRA dengan bijak.
