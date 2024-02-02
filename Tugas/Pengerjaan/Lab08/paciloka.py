""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY
    Tanggal: 17 November 2023

    Program ini dibuat untuk memenuhi tugas Lab 8.

    User diminta untuk input banyak hotel dan user.
    Setelah itu, user diminta input nama hotel, banyak kamar, dan harga kamar.
    Setelah itu, user diminta untuk input nama user dan saldo user.

    User diminta untuk memasukkan perintah angka 1 sampai 8:
        1. Print daftar hotel dan user
        2. Print profit hotel
        3. Print saldo user
        4. Topup saldo user
        5. Booking kamar hotel
        6. Print daftar tamu hotel
        7. Print daftar hotel yang pernah dipesan user
        8. Exit program

    Jika user memasukkan perintah bukan angka 1 sampai 8, maka program akan mengeluarkan pesan error.
    Jika user memasukkan nama hotel atau user yang tidak ada di sistem, maka program akan mengeluarkan pesan error.

    DEV NOTES:
    Cara program ini mengakses data hotel dan user adalah dengan menggunakan list. List ini berisi objek dari class Hotel dan User. 
    Saya menggunakan list comprehension seperti: [hotel.name for hotel in hotels] untuk mengakses nama hotel dari list hotel, ini akan menghasilkan list berisi nama hotel.
    menggunakan list comprehension ini memudahkan saya untuk mengakses data dari list hotel dan user. function next() dan any() juga digunakan untuk mengakses data dari list hotel dan user.
    
"""

class Hotel :
    # Inisialisasi class Hotel
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guest_list = []
    
    def booking(self, other, jumlah_kamar):
        # Fungsi booking kamar hotel jika kamar tersedia dan saldo user cukup
        if self.available_room >= jumlah_kamar and other.money >= self.room_price * jumlah_kamar:
            self.available_room -= jumlah_kamar
            self.profit += self.room_price * jumlah_kamar
            other.money -= self.room_price * jumlah_kamar
            if other.name not in self.guest_list and self.name not in other.hotel_list:
                self.guest_list.append(other.name)
                other.hotel_list.append(self.name)
            print(f"User dengan nama {other.name} berhasil melakukan booking di hotel {self.name} dengan jumlah {input_kamar} kamar!")
        else:
            print(f"Booking tidak berhasil!")

    def __str__(self):
        self.name

class User:
    # Inisialisasi class User
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hotel_list = [] 
    
    # Fungsi topup saldo user
    def topup(self, jumlah_topup):
        self.money += jumlah_topup
        print(f"Berhasil menambahkan {jumlah_topup} ke user {self.name}. Saldo user menjadi {self.money}")
        
    def __str__(self):
        self.name
    
# Main program
if __name__ == '__main__':
    try:
        # Input banyak hotel dan user
        banyak_hotel = int(input("Masukan banyak hotel : "))
        if banyak_hotel < 1:
            raise ValueError
        banyak_user = int(input("Masukan banyak user : "))
        if banyak_user < 1:
            raise ValueError
        print()

        # Input nama hotel, banyak kamar, dan harga kamar
        hotels = []
        for i in range (1, banyak_hotel+1):
            nama_hotel_input = str(input(f"Masukan nama hotel ke-{i} : "))
            if nama_hotel_input.strip() == "" or any(hotel.name == nama_hotel_input for hotel in hotels):
                raise ValueError
            banyak_kamar = int(input(f"Masukan banyak kamar hotel ke-{i} : "))
            if banyak_kamar < 1:
                raise ValueError
            harga_kamar = int(input(f"Masukan harga satu kamar hotel ke-{i} : "))
            if harga_kamar < 1:
                raise ValueError
            hotels.append(Hotel(nama_hotel_input, banyak_kamar, harga_kamar))
        print()

        # Input nama user dan saldo user
        users = []
        for i in range (1, banyak_user+1):
            nama_user_input = str(input(f"Masukan nama user ke-{i} : "))
            if nama_user_input.strip() == "" or any(user.name == nama_user_input for user in users):
                raise ValueError
            saldo_user = int(input(f"Masukan saldo user ke-{i} : "))
            if saldo_user < 1:
                raise ValueError
            users.append(User(nama_user_input, saldo_user))

    # Exception handling jika input tidak valid
    except ValueError:
        print("Input tidak valid atau input sudah ada sebelumnya")
        exit()
    print()

    # Menu utama
    run = True
    while run == True:
        print("=============Welcome to Paciloka!=============")
        print()

        # User memasukkan perintah
        perintah = input("Masukan perintah : ")

        # 1 Print daftar hotel dan user
        if perintah == "1":
            print("Daftar Hotel")
            for i in range (0, banyak_hotel):
                print(f"{i+1}. {hotels[i].name}")
            print()
            print("Daftar User")
            for i in range (0, banyak_user):
                print(f"{i+1}. {users[i].name}")

        # 2 Print profit hotel
        elif perintah == "2":
            input_hotel = str(input("Masukan nama hotel : "))
            if input_hotel.strip() != "" and any(hotel.name == input_hotel for hotel in hotels):
                print(f"Hotel dengan nama {input_hotel} mempunyai profit sebesar {next(hotel for hotel in hotels if hotel.name==input_hotel).profit}")
            else:
                print("Nama hotel tidak ditemukan di sistem!")
                continue

        # 3 Print saldo user
        elif perintah == "3":
            input_user = str(input("Masukan nama user : "))
            if input_user.strip() != "" and any(user.name == input_user for user in users):
                print(f"User dengan nama {input_user} mempunyai saldo sebesar {next(user for user in users if user.name == input_user).money}")
            else:
                print("Nama user tidak ditemukan di sistem!")
                continue
        
        # 4 Topup saldo user
        elif perintah == "4":
            try:
                input_user = str(input("Masukan nama user : "))
                user_topup = next(user for user in users if user.name == input_user)
            except StopIteration:
                print("Nama user tidak ditemukan di sistem!")
                continue

            try:
                input_topup = int(input("Masukkan jumlah uang yang akan ditambahkan ke user : "))
                if input_topup <= 0:
                    raise ValueError
                user_topup.topup(input_topup)
            except ValueError:
                print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
                continue

        # 5 Booking kamar hotel
        elif perintah == "5":
            try:
                input_user = str(input("Masukan nama user : "))
                user_book = next(user for user in users if user.name == input_user)
            except StopIteration:
                print("Nama user tidak ditemukan di sistem!")
                continue

            try:
                input_hotel = str(input("Masukan nama hotel : "))
                hotel_book = next(hotel for hotel in hotels if hotel.name == input_hotel)
            except StopIteration:
                print("Nama hotel tidak ditemukan di sistem!")
                continue

            try:
                input_kamar = int(input("Masukkan jumlah kamar yang akan dibooking : "))
                if input_kamar < 1:
                    raise ValueError
                hotel_book.booking(user_book, input_kamar)
            except ValueError:
                print("Jumlah kamar yang akan dipesan harus lebih dari 0!")
                continue

        # 6 Print daftar tamu hotel
        elif perintah == "6":
            input_hotel = str(input("Masukan nama hotel : "))
            if input_hotel.strip() != "" and any(hotel.name == input_hotel for hotel in hotels):
                hotel_guest = next(hotel for hotel in hotels if hotel.name == input_hotel)
                if hotel_guest.guest_list != []:
                    print(f"{input_hotel} | {', '.join(hotel_guest.guest_list)}")
                else:
                    print(f"Hotel {input_hotel} tidak memiliki pelanggan!")
                    continue
            else:
                print("Nama hotel tidak ditemukan di sistem!")
                continue

        # 7 Print daftar hotel yang pernah dipesan user
        elif perintah == "7":
            input_user = str(input("Masukan nama user : "))
            if input_user.strip() != "" and any(user.name == input_user for user in users):
                user_hotel = next(user for user in users if user.name == input_user)
                if user_hotel.hotel_list != []:
                    print(f"{input_user} | {', '.join(user_hotel.hotel_list)}")
                else:
                    print(f"User {input_user} tidak pernah melakukan booking!")
                    continue
            else:
                print("Nama user tidak ditemukan di sistem!")
                continue

        # 8 Exit program
        elif perintah == "8":
            print("Terima kasih sudah mengunjungi Paciloka!")
            run = False
            continue

        # Exception handling jika perintah tidak valid
        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")
            continue
        print()