#                    __        __                                 
#    ____ ___  ___  / /_____ _/ /__________ _________  _________ _
#   / __ `__ \/ _ \/ __/ __ `/ __/ ___/ __ `/ ___/ _ \/ ___/ __ `/
#  / / / / / /  __/ /_/ /_/ / /_/ /  / /_/ / /__/  __/ /  / /_/ / 
# /_/ /_/ /_/\___/\__/\__,_/\__/_/   \__,_/\___/\___/_/   \__,_/  
#                                                                 
#                              MetaTraceRA                        
# nucleus_ops/x2_docmeta.py

import os
from PyPDF2 import PdfReader
from docx import Document

def run(file_path, output_path=None):
    if not os.path.isfile(file_path):
        msg = f"[!] File tidak ditemukan: {file_path}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
        return

    if file_path.lower().endswith('.pdf'):
        read_pdf_metadata(file_path, output_path)
    elif file_path.lower().endswith('.docx'):
        read_docx_metadata(file_path, output_path)
    else:
        msg = "[!] Format tidak didukung. Gunakan PDF atau DOCX."
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')


def read_pdf_metadata(file_path, output_path=None):
    try:
        reader = PdfReader(file_path)
        meta = reader.metadata

        if not meta:
            msg = "[i] Tidak ada metadata ditemukan dalam PDF."
            print(msg)
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(msg + '\n')
            return

        lines = [f"[+] Metadata PDF: {file_path}\n"]
        for key, value in meta.items():
            lines.append(f"{key[1:]:20}: {value}")

        output = '\n'.join(lines)
        print(output)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(output + '\n')

    except Exception as e:
        msg = f"[!] Gagal membaca metadata PDF: {e}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')


def read_docx_metadata(file_path, output_path=None):
    try:
        doc = Document(file_path)
        core_props = doc.core_properties

        lines = [f"[+] Metadata DOCX: {file_path}\n"]
        for attr in dir(core_props):
            if not attr.startswith('_') and not callable(getattr(core_props, attr)):
                value = getattr(core_props, attr)
                if value:
                    lines.append(f"{attr:20}: {value}")

        output = '\n'.join(lines)
        print(output)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(output + '\n')

    except Exception as e:
        msg = f"[!] Gagal membaca metadata DOCX: {e}"
        print(msg)
        if output_path:
            with open(output_path, 'w') as f:
                f.write(msg + '\n')
