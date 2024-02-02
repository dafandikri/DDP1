""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY
    Tanggal: 15 September 2023
    
    Program ini dibuat untuk memenuhi tugas Lab 2.
    
    Program dimulai menanyakan pinjam buku atau keluar.
    Jika pinjam buku, maka akan meminta input user berupa nama, saldo, dan member/non-member.
    Jika member, maka akan meminta input ID berupa 5 digit angka yang jumlahnya 23.
    
    Setelah login berhasil, maka akan meminta input user berupa judul komik dan lama peminjaman.
    Jika judul komik tidak ada, maka akan kembali ke input judul komik.
    Jika judul komik ada, maka akan menampilkan hasil peminjaman dan saldo terbaru yang sudah dikurangi harga komik.
    Jika member, maka akan mendapatkan diskon 20%.
    Jika saldo tidak cukup, maka akan kembali ke input judul komik.

    User bisa ketik exit untuk keluar kembali ke menu utama.
    Jika ketik 2, maka akan keluar dari program.
"""

# Define function untuk print menu
def print_menu():
    print("Selamat Datang di Toko Buku Place Anak Chill")
    print("============================================")
    print("1. Pinjam buku")
    print("2. Keluar")
    print("============================================")

def print_garis():
    print("============================================")

def print_daftar_komik():
    print("X-Man (Rp 7.000/hari)")
    print("Doraemoh (Rp 5.500/hari)")
    print("Nartoh (Rp 4.000/hari)")

def print_katalog():
        print_garis()
        print("Katalog Buku Place Anak Chill")
        print_garis()
        print_daftar_komik()
        print_garis()
        print("Exit")
        print_garis()

# Memastikan variable keluar False untuk loop program utama berjalan
keluar = False

# Looping program utama
while keluar == False:

    # Mengdeclare variable dan memastikan variable kosong
    wrong_id = 0
    selesai_katalog = False
    stop_program_katalog = False
    exit_katalog = False
    harga = 0
    id_list = []
    
    # Menjalan program utama dan meminta input user
    print_menu()
    pilihan = int(input("Apa yang ingin anda lakukan: "))
    if pilihan == 1:
        nama = input("Masukkan nama anda: ")
        saldo = int(input("Masukkan saldo anda (Rp): "))
        member = input("Apakah anda member? [Y/N]: ")

        # Memastikan input member menjadi lowercase agar case-insensitive
        member = member.lower()

        # Jika user punya member, maka akan meminta input ID
        if member == "y":

            # Loop sampai 3 kali jika user salah memasukkan ID stop loop
            while wrong_id < 3:
                id = input("Masukkan ID anda: ")

                # ID akan dijadikan list dan diubah menjadi integer
                id_list = list(id)
                id_list = [int(id_list) for id_list in id_list]

                # Jika panjang digit ID adalah 5 dan jumlah ID adalah 23, maka login berhasil
                if len(id_list) == 5 and sum(id_list) == 23:
                    print("Login member berhasil!")
                    print("")
                    break
                else:
                    wrong_id += 1
                    print("ID anda salah!")
        else:
            print("Login non-member berhasil!")
            print("")

        # Saat loop selesai, akan ke conditional ini: Jika wrong_id == 3, maka akan kembali ke menu utama
        if wrong_id == 3:
            print("Program akan kembali ke menu utama")
            print("")
            wrong_id = 0
            continue
        
        # Memastikan wrong_id kembali ke 0
        wrong_id = 0

        # Looping program katalog
        while stop_program_katalog == False:

            # Looping program katalog jika user salah input judul komik
            while selesai_katalog == False:
                print_katalog()
                comic = input("Buku yang dipilih: ")

                # Memastikan input judul komik menjadi lowercase agar case-insensitive
                comic = comic.lower()

                # Jika user memasukkan exit, maka akan break loop selesai_katalog
                if comic == "exit":
                    selesai_katalog = True
                    break

                # Meminta input user untuk lama peminjaman
                waktu_pinjam = int(input("Ingin melakukan peminjaman untuk berapa hari: "))

                # Jika x-man
                if comic == "x-man":
                    harga = float(7000)
                    selesai_katalog = True
                    break
                # Jika doraemoh
                elif comic == "doraemoh":
                    harga = float(5500)
                    selesai_katalog = True
                    break
                # Jika nartoh
                elif comic == "nartoh":
                    harga = float(4000)
                    selesai_katalog = True
                    break
                # Jika user salah memasukkan judul komik, akan kembali ke loop selesai_katalog
                else:
                    print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!")
                    print("")
                    continue

            # Jika user memasukkan exit, maka akan break loop stop_program_katalog
            if comic == "exit":
                selesai_katalog = False
                break

            # Memastikan variable selesai_katalog kembali ke False
            selesai_katalog = False

            # Menampilkan hasil peminjaman
            print(f"Berhasil meminjam buku {comic.capitalize()} selama {waktu_pinjam} hari")

            # Jika saldo tidak cukup, maka akan kembali ke loop stop_program_katalog dan menampilkan katalog
            if saldo < harga*waktu_pinjam:
                print(f"Tidak berhasil meminjam! Saldo anda kurang {harga*waktu_pinjam-saldo}!")
                print("")
                continue

            #jika saldo cukup
            else:
                # Jika member, maka akan mendapatkan diskon 20% atau dikali 0.8
                if member == "y":
                    saldo = float(saldo-harga*waktu_pinjam*0.8)
                    print(f"Saldo anda saat ini {saldo}")
                    print("")
                    continue
                # Jika non-member, maka tidak mendapatkan diskon
                else:
                    saldo = float(saldo-harga*waktu_pinjam)
                    print(f"Saldo anda saat ini {saldo}")
                    print("")
                    continue

        # Jika user memasukkan exit, maka akan break loop dan kembali ke program utama (selesai_katalog -> stop_program_katalog -> looping program utama)
        if comic == "exit":
            stop_program_katalog = True
            continue

    # Jika user memilih keluar, maka akan break loop dan keluar dari program
    elif pilihan == 2:
        print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
        keluar = True
        break

    # Jika user memasukkan input yang tidak diketahui, maka akan kembali ke menu utama
    else:
        print("Perintah tidak diketahui!")
        print("")
        continue