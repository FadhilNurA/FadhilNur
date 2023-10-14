#Muhammad Fadhil Nur Aziz
#2306275531
#Kelas G SAN
#https://github.com/ir-nlp-csui/indo-law/tree/main -> untuk mencari file xmlnya silahkan download ini

import os
import sys
import time

# Mulai penghitung waktu
start = time.time()

# Pengecekan jumlah argumen
argc = len(sys.argv)

# Validasi jumlah argumen yang diberikan. Jika kurang dari 3, berikan pesan seperti dibawah
if argc < 3:
    print()
    print("Usage: python search.py [section] [kata kunci 1] [AND/OR/ANDNOT] [kata kunci 2]")
    sys.exit()

# Menyimpan argumen ke dalam variabel yang sesuai
section = sys.argv[1].lower()
keyword1 = sys.argv[2].lower()

# Jika ada lebih dari 4 argumen, simpan operator dan kata kunci kedua
if argc > 4:
    operator = sys.argv[3].upper()
    if operator not in ["AND", "OR", "ANDNOT"]:  # Cek validitas operator
        print('Mode harus berupa AND, OR atau ANDNOT.')
        sys.exit()
    keyword2 = sys.argv[4].lower()

# Pindah ke direktori dataset
path = "C:\dataset"
if not os.path.exists(path):  # Validasi keberadaan direktori
    print(f"Error: Directory {path} does not exist!")
    sys.exit()

os.chdir(path)

documents_found = 0  # untuk menghitung jumlah dokumen yang ditemukan

# Loop melalui setiap file di direktori
for filename in os.listdir():
    if filename.endswith(".xml"):  # Cek apakah file adalah file XML
        with open(os.path.join("C:\dataset", filename), 'r') as file: # Buka file lalu baca
            content = file.read().replace('\n', ' ')

            # Ekstrak data yang dibaca
            start_idx = content.find("<putusan") #mencari indeks awal dari string "<putusan" di dalam 
            end_idx = content.find(">", start_idx) #mengetahui di mana tag ini berakhir. Dalam format XML, sebuah tag akan berakhir dengan karakter ">"
            metadata_part = content[start_idx:end_idx] #mengambil substring dari konten yang dimulai dari start_idx dan berakhir sebelum end_idx.

            # Inisialisasi variabel metadata
            klasifikasi = ""
            lembaga_peradilan = ""
            provinsi = ""
            sub_klasifikasi = ""

            # Ekstrak nilai metadata dari konten
            for attr in ["klasifikasi", "lembaga_peradilan", "provinsi", "sub_klasifikasi"]: #Ini adalah loop yang akan berjalan sebanyak 4 kali, 
                start_attr = metadata_part.find(f'{attr}="') #setiap kali untuk salah satu dari atribut metadata yang disebutkan.
                #Kode di atas mencari indeks awal dari atribut yang saat ini sedang diproses dalam metadata_part.
                if start_attr != -1:
                    start_attr += len(attr) + 2
#Jika atribut ditemukan (indeks awal bukan -1), kita pindahkan indeks ke awal dari nilai atribut itu sendiri. 
#Kita menambahkan panjang attr dan 2 (untuk karakter =").
                    end_attr = metadata_part.find('"', start_attr) #berakhir pada karakter tanda kutip pertama yang ditemukan setelah awal nilai
                    value = metadata_part[start_attr:end_attr] #Mengekstrak Nilai
                    if attr == "klasifikasi": #Menyimpan Nilai ke Variabel yang Sesuai
                        klasifikasi = value
                    elif attr == "lembaga_peradilan":
                        lembaga_peradilan = value
                    elif attr == "provinsi":
                        provinsi = value
                    elif attr == "sub_klasifikasi":
                        sub_klasifikasi = value
            
            # Cari konten bagian yang relevan
            content = content.lower()
            if section != "all":
                start_idx = content.find(f"<{section}>")
                end_idx = content.find(f"</{section}>")
                #kode ini mencari di mana bagian tersebut dimulai dan diakhiri
                
                if start_idx == -1 or end_idx == -1:  # Jika bagian tidak ditemukan, lanjutkan ke file berikutnya
                    continue

                content_section = content[start_idx+len(section)+2:end_idx]
                #Jika bagian ditemukan, kode ini akan mengekstrak konten spesifik tersebut.
            else:
                content_section = content
            
            # Cari kata kunci dalam konten
            if argc == 3:
                if keyword1 in content_section:
                    documents_found += 1
                    print(f"{filename}\t{provinsi}\t{klasifikasi}\t{sub_klasifikasi}\t{lembaga_peradilan}")
            else:
                if operator == "AND":
                    if keyword1 in content_section and keyword2 in content_section:
                        documents_found += 1
                        print(f"{filename}\t{provinsi}\t{klasifikasi}\t{sub_klasifikasi}\t{lembaga_peradilan}")

                elif operator == "OR":
                    if keyword1 in content_section or keyword2 in content_section:
                        documents_found += 1
                        print(f"{filename}\t{provinsi}\t{klasifikasi}\t{sub_klasifikasi}\t{lembaga_peradilan}")

                elif operator == "ANDNOT":
                    if keyword1 in content_section and keyword2 not in content_section:
                        documents_found += 1
                        print(f"{filename}\t{provinsi}\t{klasifikasi}\t{sub_klasifikasi}\t{lembaga_peradilan}")

# Akhiri penghitung waktu dan tampilkan hasil pencarian
end = time.time()

print(f"Banyaknya dokumen yang ditemukan = {documents_found}")
print(f"Total waktu pencarian = {end-start:.3f} detik.")
