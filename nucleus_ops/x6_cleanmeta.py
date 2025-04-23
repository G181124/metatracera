#                    __        __                                 
#    ____ ___  ___  / /_____ _/ /__________ _________  _________ _
#   / __ `__ \/ _ \/ __/ __ `/ __/ ___/ __ `/ ___/ _ \/ ___/ __ `/
#  / / / / / /  __/ /_/ /_/ / /_/ /  / /_/ / /__/  __/ /  / /_/ / 
# /_/ /_/ /_/\___/\__/\__,_/\__/_/   \__,_/\___/\___/_/   \__,_/  
#                                                                 
#                              MetaTraceRA                        
# nucleus_ops/x6_cleanmeta.py

from PIL import Image
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
        data = list(image.getdata())
        clean_image = Image.new(image.mode, image.size)
        clean_image.putdata(data)

        cleaned_path = f"output/cleaned_{os.path.basename(file_path)}"
        clean_image.save(cleaned_path)

        msg = (
            f"[+] Metadata berhasil dihapus\n"
            f"File asli  : {file_path}\n"
            f"File hasil : {cleaned_path}"
        )
        print(msg)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')

    except Exception as e:
        msg = f"[!] Gagal menghapus metadata: {e}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
