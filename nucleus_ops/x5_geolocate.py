#                    __        __                                 
#    ____ ___  ___  / /_____ _/ /__________ _________  _________ _
#   / __ `__ \/ _ \/ __/ __ `/ __/ ___/ __ `/ ___/ _ \/ ___/ __ `/
#  / / / / / /  __/ /_/ /_/ / /_/ /  / /_/ / /__/  __/ /  / /_/ / 
# /_/ /_/ /_/\___/\__/\__,_/\__/_/   \__,_/\___/\___/_/   \__,_/  
#                                                                 
#                              MetaTraceRA                        
# nucleus_ops/x5_geolocate.py

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os

def get_decimal_from_dms(dms, ref):
    try:
        def to_float(x):
            return x[0] / x[1] if isinstance(x, tuple) else float(x)
        degrees = to_float(dms[0])
        minutes = to_float(dms[1])
        seconds = to_float(dms[2])
        decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
        if ref in ['S', 'W']:
            decimal = -decimal
        return decimal
    except Exception as e:
        return None


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

        gps_info = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == 'GPSInfo':
                for key in value:
                    sub_tag = GPSTAGS.get(key, key)
                    gps_info[sub_tag] = value[key]

        if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
            lat = get_decimal_from_dms(gps_info['GPSLatitude'], gps_info['GPSLatitudeRef'])
            lon = get_decimal_from_dms(gps_info['GPSLongitude'], gps_info['GPSLongitudeRef'])
            lines = [
                f"[+] Koordinat ditemukan:",
                f"Latitude : {lat}",
                f"Longitude: {lon}",
                f"[+] Google Maps: https://www.google.com/maps/search/?api=1&query={lat},{lon}"
            ]
            output = '\n'.join(lines)
            print(output)
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(output + '\n')
        else:
            msg = "[i] Metadata GPS tidak ditemukan."
            print(msg)
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(msg + '\n')

    except Exception as e:
        msg = f"[!] Gagal membaca lokasi dari metadata: {e}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
