file_found = False
while file_found == False:
    try:
        print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")
        name_input_file = input("Masukkan nama file input daftar makanan: ")
        name_output_file = input("Masukkan nama file output: ")
        input_file = open(name_input_file, "rt")
    except FileNotFoundError:
        print()
        print("Maaf, file input tidak ada")
        print()
    if input_file != None:
        file_found = True
output_file = open(name_output_file, "wt")
print()

if "Daftar Makanan 1: " in input_file.readline():
    makanan1_format_valid = True
    print("yes1")

if "Daftar Makanan 2: " in input_file.readline():
    makanan2_format_valid = True
    print("yes2")

if makanan1_format_valid == True:
    input_file.seek(0)
    unique_list_makanan1 = ""
    list_makanan1 = input_file.readline()
    list_makanan1 = list_makanan1.replace("Daftar Makanan 1: ", "")
    list_makanan1 = list_makanan1.replace("\n", "")
    index_coma = list_makanan1.find(",")
    while index_coma != -1:
        makanan1 = list_makanan1[:index_coma].lower()
        if makanan1 not in unique_list_makanan1:
            unique_list_makanan1 += makanan1 + ","
        list_makanan1 = list_makanan1[index_coma+1:].lower()
        index_coma = list_makanan1.find(",")
    if "," not in list_makanan1:
        if list_makanan1 not in unique_list_makanan1:
            unique_list_makanan1 += list_makanan1
        else:
            unique_list_makanan1 = unique_list_makanan1[:-1]


if makanan1_format_valid == True:
    input_file.seek(1)
    unique_list_makanan2 = ""
    list_makanan2 = input_file.readline()
    list_makanan2 = list_makanan2.replace("Daftar Makanan 1: ", "")
    list_makanan2 = list_makanan2.replace("\n", "")
    index_coma = list_makanan2.find(",")
    while index_coma != -1:
        makanan2 = list_makanan2[:index_coma].lower()
        if makanan2 not in unique_list_makanan2:
            unique_list_makanan2 += makanan2 + ","
        list_makanan2 = list_makanan2[index_coma+1:].lower()
        index_coma = list_makanan2.find(",")
    if "," not in list_makanan2:
        if list_makanan2 not in unique_list_makanan2:
            unique_list_makanan2 += list_makanan2
        else:
            unique_list_makanan2 = unique_list_makanan2[:-1]

action = ""
while action != "5":
    print("Apa yang ingin kamu lakukan?")
    print("================================================")
    print("1. Tampilkan daftar makanan pertama")
    print("2. Tampilkan daftar makanan kedua")
    print('3. Tampilkan gabungan makanan dari dua daftar')
    print("4. Tampilkan makanan yang sama dari dua daftar")
    print("5. Keluar")
    print("================================================")
    action = input("Masukkan aksi yang ingin dilakukan: ")
    print()
    if action == "1":
        if makanan1_format_valid == True:
            print("Daftar makanan pertama:")
            print(unique_list_makanan1)
            output_file.write("Daftar makanan pertama:\n")
            output_file.write(unique_list_makanan1 + "\n")
        else:
            print("Maaf, file input tidak sesuai format")
            output_file.write("Maaf, file input tidak sesuai format\n")
        print()
        output_file.write("\n")
    elif action == "2":
        if makanan2_format_valid == True:
            print("Daftar makanan pertama:")
            print(unique_list_makanan2)
            output_file.write("Daftar makanan pertama:\n")
            output_file.write(unique_list_makanan2 + "\n")
        else:
            print("Maaf, file input tidak sesuai format")
            output_file.write("Maaf, file input tidak sesuai format\n")
        print()
        output_file.write("\n")
    elif action == "3":
        unique_list_makanan2_dupe = unique_list_makanan2
        unique_list_makanan1_dupe = unique_list_makanan1
        if makanan1_format_valid == True and makanan2_format_valid == True:
            print("Gabungan makanan favorit dari kedua daftar:")
            index_coma = unique_list_makanan1_dupe.find(",")
            while index_coma != -1:
                makanan3 = unique_list_makanan1_dupe[:index_coma].lower()
                if makanan3 not in unique_list_makanan2_dupe:
                    unique_list_makanan2_dupe += makanan3 + ","
                unique_list_makanan1 = list_makanan2[index_coma+1:].lower()
                index_coma = list_makanan2.find(",")
            if "," not in list_makanan2:
                if list_makanan2 not in unique_list_makanan2:
                    unique_list_makanan2 += list_makanan2
                else:
                    unique_list_makanan2 = unique_list_makanan2[:-1]        
        else:
            print("Maaf, file input tidak sesuai format")
        print()
    elif action == "4":
        print("Makanan yang sama dari dua daftar:")
        print()
    else:
        print("Maaf, aksi tidak dikenali")
        print()
        continue
print("Terima kasih telah menggunakan program ini!")
print(f"Semua keluaran telah disimpan pada file {name_output_file}")

