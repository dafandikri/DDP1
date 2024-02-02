""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY
    Tanggal: 10 November 2023

    Program ini dibuat untuk memenuhi tugas Lab 7.

    Program ini adalah sebuah Relation finder
    Program ini menerima nama parent dan nama child.
    Setelah itu, program akan menampilkan menu pilihan yang berisi:
        1. CEK_KETURUNAN
            Menampilkan pesan apakah child merupakan keturunan dari parent.
        2. CETAK_KETURUNAN
            Menampilkan semua keturunan dari parent.
        3. JARAK_GENERASI
            Menampilkan jarak generasi antara parent dan child.
        4. EXIT
            Keluar dari program.
"""

# Print menu pilihan
def print_menu():
    print()
    print("=====================================================================")
    print("Selamat Datang di Relation Finder! Pilihan yang tersedia:")
    print("1. CEK_KETURUNAN")
    print("2. CETAK_KETURUNAN")
    print("3. JARAK_GENERASI")
    print("4. EXIT")

# Buat tree dari data relasi parent dan child
def create_tree(relations):
    tree = {}
    for relation in relations:
        parent = relation[0]
        child = relation[1]
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    return tree

# Cek apakah child merupakan keturunan dari parent
def cek_keturunan(nama_parent, nama_child, tree):
    if nama_parent == nama_child:
        return True
    elif nama_parent in tree:
        for child in tree[nama_parent]:
            if cek_keturunan(child, nama_child, tree):
                return True
    return False

# Cetak semua keturunan dari parent
def cetak_keturunan(nama_parent, tree):
    if nama_parent in tree:
        print("-", end=" ")
        for child in tree[nama_parent]:
            print(child, end=" ")
        print()
        for child in tree[nama_parent]:
            cetak_keturunan(child, tree)

# Cek jarak generasi antara parent dan child
def jarak_generasi(nama_parent, nama_child, tree, depth=0):
    if nama_parent == nama_child:
        return depth
    elif nama_parent in tree:
        for child in tree[nama_parent]:
            distance = jarak_generasi(child, nama_child, tree, depth + 1)
            if distance is not None:
                return distance
    return None

# Main program
if __name__ == "__main__":
    # Input data relasi parent dan child
    print("Masukkan data relasi:")
    run = True
    relations = []
    while run == True:
        input_string = input("")
        if input_string == "SELESAI":
            run = False
            continue
        else:
            input_list = input_string.split(" ")
            relations.append(tuple(input_list))
    tree = create_tree(relations)

    # Loop program
    run = True
    while run == True:
        print_menu()
        pilihan_menu = input("Masukkan pilihan: ")

        # Cek apakah child merupakan keturunan dari parent
        if pilihan_menu == "1":
            nama_parent = input("Masukkan nama parent: ")
            nama_child = input("Masukkan nama child: ")
            if nama_parent == nama_child:
                print(f"{nama_child} bukan merupakan keturunan dari {nama_parent}")
                continue
            valid = cek_keturunan(nama_parent, nama_child, tree)
            if valid == True:
                print(f"{nama_child} benar merupakan keturunan dari {nama_parent}")
                continue
            else:
                print(f"{nama_child} bukan merupakan keturunan dari {nama_parent}")
                continue

        # Menampilkan semua keturunan dari parent
        elif pilihan_menu == "2":
            nama_parent = input("Masukkan nama parent: ")
            cetak_keturunan(nama_parent, tree)
            continue

        # Cek jarak generasi antara parent dan child
        elif pilihan_menu == "3":
            nama_parent = input("Masukkan nama parent: ")
            nama_child = input("Masukkan nama child: ")
            if nama_parent == nama_child:
                print(f"{nama_parent} memiliki hubungan dengan {nama_child} sejauh 0")
                continue
            distance = jarak_generasi(nama_parent, nama_child, tree)
            if distance is not None:
                print(f"{nama_parent} memiliki hubungan dengan {nama_child} sejauh {distance}")
                continue
            else:
                print(f"Tidak ada hubungan antara {nama_parent} dengan {nama_child}")
                continue

        # Keluar dari program
        elif pilihan_menu == "4":
            print("=====================================================================")
            print("Terima kasih telah menggunakan Relation Finder!")
            run = False
            continue

        # Jika Pilihan tidak valid
        else:
            print("Pilihan tidak valid!")
            continue