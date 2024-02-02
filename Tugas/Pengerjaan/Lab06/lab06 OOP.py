""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY
    Tanggal: 3 November 2023

    Program ini dibuat untuk memenuhi tugas Lab 6.

    Program ini adalah sebuah plagiarism checker berdasarkan data dari lab6.txt
    Program ini menerima nama mata kuliah, nama/NPM mahasiswa pertama, dan nama/NPM mahasiswa kedua.
    Program akan menampilkan tingkat kemiripan tugas kedua mahasiswa.
    Program akan menampilkan pesan kesalahan jika input yang dimasukkan tidak sesuai dengan data lab6.txt.
    Program akan berhenti jika user memasukkan "EXIT" sebagai nama mata kuliah.
"""

# Open file Lab6.txt dan baca isi file
f = open("Lab6.txt", "r", encoding="utf-8-sig")
text_list = f.readlines()

# Buat dictionary dari data di Lab6.txt
key = [text_list[i].strip() for i in range(0, len(text_list), 4)]
values = [text_list[i].strip() for i in range(2, len(text_list), 4)]
keyword_dict = {key[i]: values[i] for i in range(0, len(key))}

# Buat list nama, npm, dan matkul dari data di Lab6.txt
key_list = [key[i].split(";") for i in range(len(key))]
nama_list = [key_list[i][0] for i in range(0, len(key_list), 3)]
npm_list = [key_list[i][1] for i in range(0, len(key_list), 3)]
matkul_list = [key_list[i][2] for i in range(0, len(key_list))]

# Print welcome message
print("Selamat datang di program Plagiarism Checker!")

# Loop program
run = True
while run == True:
    print("=====================================================================")
    matkul = input("Masukkan nama mata kuliah yang ingin diperiksa: ")
    
    # Cek apakah user ingin keluar dari program
    if matkul == "EXIT":
        run = False
        continue

    # Cek apakah nama mata kuliah ada di database
    elif matkul not in matkul_list:
        print(f"{matkul} tidak ditemukan.")
        print()
        continue

    # Cek apakah nama/NPM mahasiswa pertama dan kedua ada di database
    identitas1 = input("Masukkan nama/NPM mahasiswa pertama: ")
    if identitas1 not in nama_list and identitas1 not in npm_list:
        print("Informasi mahasiswa tidak ditemukan.")
        print()
        continue
    identitas2 = input("Masukkan nama/NPM mahasiswa kedua: ")
    if identitas2 not in nama_list and identitas2 not in npm_list:
        print("Informasi mahasiswa tidak ditemukan.")
        print()
        continue

    # Cek apakah mahasiswa pertama dan kedua sama
    if identitas1 == identitas2:
        print("Mahasiswa pertama dan kedua tidak boleh sama.")
        print()
        continue
    
    print("============================= Hasil =================================")

    # Mencari tugas mahasiswa pertama dan di konversikan ke set
    if identitas1 in nama_list:
        npm1 = npm_list[nama_list.index(identitas1)]
        tugas1 = keyword_dict.get(f"{identitas1};{npm1};{matkul}")
    else:
        nama1 = nama_list[npm_list.index(identitas1)]
        tugas1 = keyword_dict.get(f"{nama1};{identitas1};{matkul}")
        identitas1 = nama1
    tugas1 = tugas1.split()
    tugas1 = set(tugas1)

    # Mencari tugas mahasiswa kedua dan di konversikan ke set
    if identitas2 in nama_list:
        npm2 = npm_list[nama_list.index(identitas2)]
        tugas2 = keyword_dict.get(f"{identitas2};{npm2};{matkul}")
    else:
        nama2 = nama_list[npm_list.index(identitas2)]
        tugas2 = keyword_dict.get(f"{nama2};{identitas2};{matkul}")
        identitas2 = nama2
    tugas2 = tugas2.split()
    tugas2 = set(tugas2)

    # Mencari keyword yang sama dan menghitung persentase kemiripan
    same_keyword = tugas1.intersection(tugas2)
    plagiarism_percent = len(same_keyword) / len(tugas1) * 100

    # Print hasil kesimpulan plagiarism checker
    print(f"Tingkat kemiripan tugas {matkul} {identitas1} dan {identitas2} adalah {plagiarism_percent:.2f}%.")
    if plagiarism_percent < 31:
        print(f"{identitas1} dan {identitas2} tidak terindikasi plagiarisme.")
    elif plagiarism_percent < 71:
        print(f"{identitas1} dan {identitas2} terindikasi plagiarisme ringan.")
    elif plagiarism_percent <= 100:
        print(f"{identitas1} dan {identitas2}  terindikasi plagiarisme.")
    print()
print("Terima kasih telah menggunakan program Plagiarism Checker!")