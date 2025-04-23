# README Internal - MetaTraceRA

## Deskripsi Umum
MetaTraceRA adalah CLI tool forensik metadata yang dirancang untuk digunakan di sistem berbasis Linux (khususnya Kali Linux) untuk melakukan analisis dan penghapusan metadata secara real-time dari file gambar, dokumen, serta pengumpulan informasi dasar file. Tool ini tidak menyimpan data permanen, namun seluruh fitur mendukung ekspor output ke file teks.

---

## Struktur Direktori
```
metatracera/
├── metatracera.py               # Entry-point CLI utama
├── requirements.txt             # Dependensi Python
├── output/                      # Folder output otomatis
├── README.md                    # Dokumentasi publik
├── nucleus_ops/                # Modul internal setiap fitur
│   ├── x1_imgmeta.py           # Analisis metadata gambar (EXIF)
│   ├── x2_docmeta.py           # Metadata PDF & DOCX
│   ├── x3_hashgen.py           # Hashing file (MD5, SHA1, SHA256)
│   ├── x4_fileinfo.py          # Info dasar file (ukuran, MIME, waktu)
│   ├── x5_geolocate.py         # Ambil GPS dari EXIF (koordinat)
│   ├── x6_cleanmeta.py         # Bersihkan metadata gambar (JPEG)
```

---

## Detail CLI Argumen
Setiap argumen di-handle dari `argparse` dalam `metatracera.py`. Hasil dapat diekspor dengan `--export`, hasil disimpan dalam format `.txt` ke folder `output/`.

| Argumen      | Modul            | File yang Didukung      | Output       | Catatan Teknis  |
|--------------|------------------|--------------------------|--------------|------------------|
| `--file`     | `x1_imgmeta.py`  | .jpg, .jpeg              | Metadata EXIF| EXIF standar via `Pillow`
| `--doc`      | `x2_docmeta.py`  | .pdf, .docx              | Metadata     | PDF pakai `PyPDF2`, DOCX pakai `python-docx`
| `--hash`     | `x3_hashgen.py`  | Semua file               | MD5, SHA1, SHA256 | `hashlib`
| `--fileinfo` | `x4_fileinfo.py` | Semua file               | Ukuran, waktu, MIME | `os`, `mimetypes`
| `--geolocate`| `x5_geolocate.py`| .jpg, .jpeg (dengan GPS) | Koordinat & Google Maps | Parsing `GPSInfo`, konversi DMS → decimal
| `--clean`    | `x6_cleanmeta.py`| .jpg, .jpeg              | Gambar tanpa metadata | `Image.putdata()` overwrite tanpa EXIF
| `--analyze`  | Gabungan `--file` dan `--geolocate` | .jpg, .jpeg | Dua output sekaligus | Menyimpan dua file jika `--export`


---

## Penanganan Output
Semua hasil ekspor ditulis sebagai file `.txt` menggunakan pola:
```
output/{modul}_{namafile}_{YYYYMMDD_HHMMSS}.txt
```
Gambar hasil `--clean` disimpan sebagai:
```
output/cleaned_{namafile}.jpg
```

---

## Metadata Test dan Simulasi (Developer Only)
Untuk menguji fitur `--file` dan `--geolocate`, bisa digunakan library `piexif` (opsional untuk publik):
```python
import piexif
from PIL import Image
image = Image.new('RGB', (100, 100), color='red')
image.save('test.jpg')
exif_dict = {
    '0th': {piexif.ImageIFD.Make: b'MetaTraceRA', piexif.ImageIFD.Model: b'TestCam X2000'},
    'Exif': {piexif.ExifIFD.DateTimeOriginal: b'2025:04:08 11:11:11'},
    'GPS': {
        piexif.GPSIFD.GPSLatitudeRef: 'N',
        piexif.GPSIFD.GPSLatitude: [(7,1), (11,1), (11,1)],
        piexif.GPSIFD.GPSLongitudeRef: 'E',
        piexif.GPSIFD.GPSLongitude: [(110,1), (45,1), (0,1)]
    }
}
exif_bytes = piexif.dump(exif_dict)
piexif.insert(exif_bytes, 'test.jpg')
```

---

## Logika `get_export_path()`
Fungsi dalam `metatracera.py` yang membuat path hasil ekspor:
```python
def get_export_path(module_name, original_path):
    basename = os.path.basename(original_path)
    name, _ = os.path.splitext(basename)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"output/{module_name}_{name}_{timestamp}.txt"
```

---

## Error Handling
- Jika file tidak ditemukan → `[!] File tidak ditemukan`
- Jika tidak ada metadata → `[i] Tidak ada metadata EXIF ditemukan.`
- Jika tidak ada GPS → `[i] Metadata GPS tidak ditemukan.`
- Jika proses gagal → `[!] Gagal membaca...` + detail `Exception`

---

## Keamanan dan Etika Penggunaan
Tool ini **tidak menyimpan cache, log, atau metadata permanen**. Pengguna bertanggung jawab penuh atas penggunaan:
- Jangan gunakan untuk menyimpan atau memproses metadata pribadi tanpa izin
- Jangan gunakan untuk aktivitas pemalsuan identitas, penyamaran, atau penyusupan privasi
- Cocok digunakan untuk:
  - Investigasi metadata internal
  - Forensik file publik
  - Pembersihan metadata sebelum publikasi

---

## Rencana Pengembangan (Opsional)
- Ekspor ke JSON atau HTML
- Pendeteksi manipulasi EXIF
- Mode interaktif CLI
- Integrasi dengan sistem report otomatis
