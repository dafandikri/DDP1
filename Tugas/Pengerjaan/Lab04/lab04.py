""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY
    Tanggal: 6 Oktober 2023
    
    Program ini dibuat untuk memenuhi tugas Lab 4.
    
    User dapat memasukkan 3 argumen, yaitu:
    1. Path file
    2. Keyword untuk pencarian
    3. Nomor kolom untuk deskripsi statistik

    Program akan menampilkan table dari file yang diberikan, lalu mencari keyword yang diberikan
    Program menampilkan deskripsi statistik dari kolom yang diberikan
    Data min, max dan rata-rata akan ditampilkan

    Error jika file tidak ditemukan, kolom tidak valid, atau keyword tidak ditemukan.
"""

import sys

# Helper function: Print table headers
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

# Function untuk print table dari file yang diberikan
def print_table(filename:str):
    try:
        open_file = open(filename, "r")
    except FileNotFoundError:
        print("Maaf, file input tidak ada")
        sys.exit()
    else:
        print_headers()
        read_file = open_file.readlines()
        for i in range(len(read_file)):
            data = read_file[i].replace("\n", "")
            data = data.split("\t")
            print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(i+1, data[0], data[1], data[2], data[3]))
        open_file.close()
    
# Function untuk print table yang sesuai dengan keyword yang diberikan
def search_phone(filename:str, keyword:str):
    open_file = open(filename, "r")
    read_file = open_file.readlines()
    open_file.seek(0)
    read_file_string = open_file.read()
    if keyword.lower() not in read_file_string.lower():
        print("Tidak ada smartphone dengan keyword '{}'".format(keyword))
        sys.exit()
    print_headers()
    counter = 0
    for i in range(len(read_file)):
        data = read_file[i].replace("\n", "")
        data = data.split("\t")
        if keyword.lower() in data[0].lower():
            counter += 1
            print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(counter, data[0], data[1], data[2], data[3]))
    print(f"Ukuran data dari hasil pencarian: {counter} x 4")
    open_file.close()

# Function untuk print deskripsi statistik dari kolom yang diberikan
def desc_stat(filename:str, column:int):
    open_file = open(filename, "r")
    read_file = open_file.readlines()
    if column == 0 or column > 3 or column < -3:
        print("Kolom tidak valid")
        sys.exit()
    max_val = 0
    min_val = 999999
    sum_val = 0
    for i in range(len(read_file)):
        data = read_file[i].replace("\n", "")
        data = data.split("\t")
        data = data[column]
        if max_val < float(data):
            max_val = float(data)
        if min_val > float(data):
            min_val = float(data)
        sum_val += float(data)
    print(f"Min data:  {min_val:.2f}")
    print(f"Max data:  {max_val:.2f}")
    print(f"Rata-rata: {sum_val/len(read_file):.2f}")
    open_file.close()


# MAIN PROGRAM
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)
    
    file_path = str(sys.argv[1])
    key = str(sys.argv[2])
    column_num = int(sys.argv[3])

    print_table(file_path)
    print()
    search_phone(file_path, key)
    desc_stat(file_path, column_num)
