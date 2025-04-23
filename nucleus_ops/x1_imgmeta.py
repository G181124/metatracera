#                    __        __                                 
#    ____ ___  ___  / /_____ _/ /__________ _________  _________ _
#   / __ `__ \/ _ \/ __/ __ `/ __/ ___/ __ `/ ___/ _ \/ ___/ __ `/
#  / / / / / /  __/ /_/ /_/ / /_/ /  / /_/ / /__/  __/ /  / /_/ / 
# /_/ /_/ /_/\___/\__/\__,_/\__/_/   \__,_/\___/\___/_/   \__,_/  
#                                                                 
#                              MetaTraceRA                        

# nucleus_ops/x1_imgmeta.py

from PIL import Image
from PIL.ExifTags import TAGS
import os

def run(file_path, output_path=None):
    if not os.path.isfile(file_path):
        msg = f"[!] File tidak ditemukan: {file_path}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
        return

    try:
        image = Image.open(file_path)
        exif_data = image._getexif()

        if not exif_data:
            msg = "[i] Tidak ada metadata EXIF ditemukan."
            print(msg)
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(msg + '\n')
            return

        lines = [f"[+] Metadata untuk: {file_path}\n"]
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            lines.append(f"{tag:25}: {value}")

        output = '\n'.join(lines)
        print(output)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(output + '\n')

    except Exception as e:
        msg = f"[!] Gagal membaca metadata: {e}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
