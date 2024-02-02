""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY

    Program ini dibuat untuk memenuhi tugas TP 2.

    User memasukkan 3 argumen, yaitu:
    1. Path file (search.py)
    2. Section untuk pencarian
    3. Keyword untuk pencarian
    4. Operator untuk pencarian (jika ada) (AND, OR, ANDNOT)
    5. Keyword untuk pencarian (jika ada)

    Program akan mencari keyword pada section yang diberikan dari dataset yang diberikan
    Program akan menampilkan nama file, provinsi, klasifikasi, sub klasifikasi, dan lembaga peradilan dari file yang diberikan
    Program akan menampilkan banyaknya dokumen yang ditemukan dan total waktu pencarian

    (BONUS) Program akan menampilkan progress bar saat pencarian berlangsung
"""

import os
import sys
from time import perf_counter

# Membuat list nama-nama file yang ada di folder dataset 
try: 
    path = "indo-law-main/dataset"
    dir_list = os.listdir(path)

# Error handling jika file tidak ditemukan
except FileNotFoundError:
    print("File not found")
    sys.exit()

# List section yang ada di dataset
sections = ["kepala_putusan","identitas","riwayat_penahanan","riwayat_perkara","riwayat_tuntutan","riwayat_dakwaan","fakta","fakta_umum","pertimbangan_hukum","amar_putusan","penutup"]

# Mengdeclare variable di sys.argv
try:
    if sys.argv[1] not in sections and sys.argv[1] != "all":
        raise Exception
    section = f"<{sys.argv[1]}>" 
    section_end = f"</{sys.argv[1]}>" 
    keyword1 = sys.argv[2]

    # Error handling jika operator tidak sesuai
    if len(sys.argv) > 3:
        keyword2 = sys.argv[4]
        operator = sys.argv[3]
        if operator not in ["AND", "OR", "ANDNOT"]:
            raise TypeError

# Error handling jika argumen program tidak sesuai
except TypeError:
    print("Operator harus berupa AND, OR atau ANDNOT.")
    sys.exit()
except:
    print("Argumen program tidak benar.")
    sys.exit()

# Membuat list untuk menyimpan output
searched = []
provinsi = []
klasifikasi = []
sub_klasifikasi = []
lembaga_peradilan = []

# Function untuk mengextract text di file yang akan di output
def extractOutput():
    provinsi_index_start = read_file.find("provinsi=\"")
    provinsi_index_end = read_file.find("\" status=", provinsi_index_start)
    provinsi = read_file[provinsi_index_start + 10:provinsi_index_end]
    if len(provinsi) > 14:
        provinsi = provinsi[:14]

    klasifikasi_index_start = read_file.find("klasifikasi=\"")
    klasifikasi_index_end = read_file.find("\" lama_hukuman=", klasifikasi_index_start)
    klasifikasi = read_file[klasifikasi_index_start + 13:klasifikasi_index_end]
    if len(klasifikasi) > 14:
        klasifikasi = klasifikasi[:14]

    sub_klasifikasi_index_start = read_file.find("sub_klasifikasi=\"")
    sub_klasifikasi_index_end = read_file.find("\" url=", sub_klasifikasi_index_start)
    sub_klasifikasi = read_file[sub_klasifikasi_index_start + 17:sub_klasifikasi_index_end]
    if len(sub_klasifikasi) > 29:
        sub_klasifikasi = sub_klasifikasi[:29]

    lembaga_peradilan_index_start = read_file.find("lembaga_peradilan=\"")
    lembaga_peradilan_index_end = read_file.find("\" provinsi=", lembaga_peradilan_index_start)
    lembaga_peradilan = read_file[lembaga_peradilan_index_start + 19:lembaga_peradilan_index_end]
    if len(lembaga_peradilan) > 19:
        lembaga_peradilan = lembaga_peradilan[:19]

    return provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan

# Function untuk menambahkan output ke list
def appendOutput():
    searched.append(file)
    provinsi_val, klasifikasi_val, sub_klasifikasi_val, lembaga_peradilan_val = extractOutput()
    provinsi.append(provinsi_val)
    klasifikasi.append(klasifikasi_val)
    sub_klasifikasi.append(sub_klasifikasi_val)
    lembaga_peradilan.append(lembaga_peradilan_val)

# Function untuk mengecek keyword di file
def keywordChecker(text):
    if len(sys.argv) == 3:
        if keyword1 in text:
            appendOutput()
    elif len(sys.argv) == 5:
        if operator == "AND":
            if keyword1 in text and keyword2 in text:
                appendOutput()
        elif operator == "OR":
            if keyword1 in text or keyword2 in text:
                appendOutput()
        elif operator == "ANDNOT":
            if keyword1 in text and keyword2 not in text:
                appendOutput()

# (BONUS) Function untuk membuat progress bar
def progressBar(count_value, total, suffix=''):
    columns = os.get_terminal_size().columns
    bar_length = int(columns/2)
    filled_up_Length = int(round(bar_length * count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '#' * filled_up_Length + '_' * (bar_length - filled_up_Length)
    sys.stdout.write("[{}] {}% {}\r" .format(bar, percentage, suffix))
    sys.stdout.flush()

# MAIN PROGRAM
counter_progress = 0
t1_start = perf_counter()
for file in dir_list:
    open_file = open(path + "/" + file, "r")
    read_file = open_file.read()
    read_file = read_file.replace("\n", " ")

    # Jika bukan all, maka akan mencari keyword di section yang diberikan
    if section != "<all>":
        section_index_start = read_file.find(section)
        section_index_end = read_file.find(section_end)
        section_content = read_file[section_index_start + len(section):section_index_end]
        if section_index_start != -1 and section_index_end != -1:
            keywordChecker(section_content)
        counter_progress+=1
        progressBar(counter_progress, len(dir_list), suffix = "Complete")

    # Jika all, maka akan mencari keyword di semua section
    elif section == "<all>":
        keywordChecker(read_file)
        counter_progress+=1
        progressBar(counter_progress, len(dir_list), suffix = "Complete")
    open_file.close()
t1_stop = perf_counter()
timer = t1_stop - t1_start

# Print output
counter = 0

# Print header
print("{:>36}{:>15}{:>15}{:>30}{:>20}".format("Nama File", "Provinsi", "Klasifikasi", "Sub Klasifikasi", "Lembaga Peradilan"))
for i in range(116):
    print("=", end="")
print()

# Print isi tabel
for i in range(0, len(searched)):
    print(f"{searched[i]}{provinsi[i]:>15}{klasifikasi[i]:>15}{sub_klasifikasi[i]:>30}{lembaga_peradilan[i]:>20}")
    counter += 1
print()

# Print statistik
print(f"Banyaknya dokumen yang ditemukan = {counter}\nTotal waktu pencarian            = {timer} detik")




