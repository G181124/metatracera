#                    __        __                                 
#    ____ ___  ___  / /_____ _/ /__________ _________  _________ _
#   / __ `__ \/ _ \/ __/ __ `/ __/ ___/ __ `/ ___/ _ \/ ___/ __ `/
#  / / / / / /  __/ /_/ /_/ / /_/ /  / /_/ / /__/  __/ /  / /_/ / 
# /_/ /_/ /_/\___/\__/\__,_/\__/_/   \__,_/\___/\___/_/   \__,_/  
#                                                                 
#                              MetaTraceRA                        

# nucleus_ops/x4_fileinfo.py

import os
import mimetypes
import time

def run(file_path, output_path=None):
    if not os.path.isfile(file_path):
        msg = f"[!] File tidak ditemukan: {file_path}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
        return

    try:
        size = os.path.getsize(file_path)
        mime_type, _ = mimetypes.guess_type(file_path)
        ctime = time.ctime(os.path.getctime(file_path))
        mtime = time.ctime(os.path.getmtime(file_path))
        atime = time.ctime(os.path.getatime(file_path))
        basename = os.path.basename(file_path)
        abs_path = os.path.abspath(file_path)

        lines = [f"[+] Informasi file: {file_path}\n"]
        lines.append(f"Nama File         : {basename}")
        lines.append(f"Lokasi Absolut    : {abs_path}")
        lines.append(f"Ukuran            : {size:,} bytes")
        lines.append(f"Tipe MIME         : {mime_type or 'Tidak diketahui'}")
        lines.append(f"Waktu Dibuat      : {ctime}")
        lines.append(f"Waktu Dimodifikasi: {mtime}")
        lines.append(f"Waktu Diakses     : {atime}")

        output = '\n'.join(lines)
        print(output)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(output + '\n')

    except Exception as e:
        msg = f"[!] Gagal mengambil informasi file: {e}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
