import hashlib
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
        with open(file_path, 'rb') as f:
            data = f.read()

        lines = [f"[+] Hash untuk: {file_path}\n"]
        lines.append(f"MD5     : {hashlib.md5(data).hexdigest()}")
        lines.append(f"SHA1    : {hashlib.sha1(data).hexdigest()}")
        lines.append(f"SHA256  : {hashlib.sha256(data).hexdigest()}")

        output = '\n'.join(lines)
        print(output)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(output + '\n')

    except Exception as e:
        msg = f"[!] Gagal menghitung hash: {e}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
