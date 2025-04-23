# MetaTraceRA

MetaTraceRA adalah alat forensik metadata berbasis CLI yang cepat, ringan, dan dirancang khusus untuk sistem seperti Kali Linux. Tools ini bekerja **real-time** tanpa database lokal dan mendukung berbagai tipe file seperti gambar, dokumen, serta memiliki fitur penghapusan metadata.

---

## 🔧 Fitur Utama

- Analisis metadata gambar (EXIF)
- Metadata dokumen PDF dan DOCX
- Hashing file (MD5, SHA1, SHA256)
- Informasi teknis file (ukuran, tipe MIME, timestamp)
- Deteksi lokasi dari metadata GPS (EXIF)
- Pembersihan metadata gambar
- Dukungan ekspor hasil
- Mode analisis gabungan `--analyze`

---

## ⚙️ Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/G181124/metatracera.git
cd metatracera
```

### 2. Buat Virtual Environment (Direkomendasikan)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Cara Penggunaan

### 📸 Analisis metadata gambar (EXIF)
Mendukung: `.jpg`, `.jpeg`
```bash
python metatracera.py --file foto.jpg
```

### 📝 Metadata dokumen PDF atau DOCX
Mendukung: `.pdf`, `.docx`
```bash
python metatracera.py --doc file.pdf
python metatracera.py --doc file.docx
```

### 🔐 Hashing file
Mendukung: semua tipe file
```bash
python metatracera.py --hash file.zip
```

### 📂 Informasi dasar file
Mendukung: semua tipe file
```bash
python metatracera.py --fileinfo file.png
```

### 🌍 Lokasi dari metadata GPS (jika ada)
Mendukung: `.jpg`, `.jpeg` dengan EXIF GPS
```bash
python metatracera.py --geolocate gambar.jpg
```

### ✂️ Hapus metadata dari gambar
Mendukung: `.jpg`, `.jpeg`
```bash
python metatracera.py --clean gambar.jpg
```

### 🧠 Analisis metadata + lokasi sekaligus
Mendukung: `.jpg`, `.jpeg`
```bash
python metatracera.py --analyze gambar.jpg
```

### 📤 Ekspor hasil ke folder `output/`
Tambahkan `--export` ke perintah apa pun:
```bash
python metatracera.py --file gambar.jpg --export
```

---

## 📁 Output
Semua hasil ekspor akan disimpan otomatis ke folder `output/` dengan nama unik berdasarkan timestamp dan nama file.

---

## 🧪 Catatan
- `--geolocate` hanya bekerja jika metadata GPS tersedia
- `--clean` hanya untuk file gambar (format JPEG)

---

Gunakan MetaTraceRA dengan bijak.
