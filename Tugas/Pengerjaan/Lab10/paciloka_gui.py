""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY
    Tanggal: 1 Desember 2023

    Program ini dibuat untuk memenuhi tugas Lab 10.

    Program ini adalah GUI untuk aplikasi Paciloka.
    User dapat melihat daftar hotel dalam bentuk tabel, memesan kamar, dan keluar dari aplikasi.
    User diminta untuk mengisi nama pengguna, nama hotel, dan jumlah kamar yang ingin dipesan.
    Setelah memesan, user akan mendapatkan informasi pesanan terakhirnya dan pendapatan Paciloka.
"""

import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    # Inisialisasi class PacilokaApp
    def __init__(self, master=None):
        self.master = master
        # Inisialisasi dictionary hotel
        self.dict_hotel = {'hotel1': [10, 250000, 'kode_hotel_1'],
                            'hotel2': [12, 500000, 'kode_hotel_2'], 
                            'hotel3': [10, 7500000, 'kode_hotel_3'], 
                            'hotel4': [1, 1000000, 'kode_hotel_4'], 
                            'hotel5': [10, 900000, 'kode_hotel_5'], 
                            'hotel6': [10, 6000000, 'kode_hotel_6']}
        
        # Inisialisasi posisi dan size window
        master.title("Paciloka App")
        window_width = 800
        window_height = 600
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.master.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.pendapatan = 0
        self.homepage()
    
    # Method untuk membuat homepage
    def homepage(self):
        # Membuat header
        header_labels = ['NAMA HOTEL', 'JUMLAH KAMAR', 'HARGA PER KAMAR', 'KODE']
        for i in range(len(header_labels)):
            tk.Label(self.master, text='|').grid(row=0, column=2*i)
            tk.Label(self.master, text=header_labels[i]).grid(row=0, column=2*i+1)
        tk.Label(self.master, text='|').grid(row=0, column=len(header_labels)*2)
        tk.Label(self.master, text='-' * 100).grid(row=1, column=0, columnspan=len(header_labels)*2+1)

        # Membuat isi tabel
        hotel_items = list(self.dict_hotel.items())
        for i in range(len(hotel_items)):
            hotel, info = hotel_items[i]
            tk.Label(self.master, text='|').grid(row=i+2, column=0)
            tk.Label(self.master, text=hotel).grid(row=i+2, column=1)
            for j in range(len(info)):
                tk.Label(self.master, text='|').grid(row=i+2, column=2*j+2)
                tk.Label(self.master, text="Rp {:,}".format(info[1]) if j == 1 else info[j]).grid(row=i+2, column=2*j+3)
            tk.Label(self.master, text='|').grid(row=i+2, column=8)
        tk.Label(self.master, text='-' * 100).grid(row=len(self.dict_hotel)+2, column=0, columnspan=len(header_labels)*2+1)


        # Membuat input entry dan button
        tk.Label(self.master, text='INPUT').grid(row=len(self.dict_hotel)+3, column=1, sticky='w')
        tk.Label(self.master, text='Nama Pengguna').grid(row=len(self.dict_hotel)+4, column=1, sticky='w')
        tk.Label(self.master, text='Nama Hotel').grid(row=len(self.dict_hotel)+5, column=1, sticky='w')
        tk.Label(self.master, text='Jumlah Kamar').grid(row=len(self.dict_hotel)+6, column=1, sticky='w')

        for i in range(3):
            tk.Label(self.master, text=':').grid(row=len(self.dict_hotel)+4+i, column=2)
        
        # Membuat entry
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=len(self.dict_hotel)+4, column=3)
        self.hotel_entry = tk.Entry(self.master)
        self.hotel_entry.grid(row=len(self.dict_hotel)+5, column=3)
        self.room_entry = tk.Entry(self.master)
        self.room_entry.grid(row=len(self.dict_hotel)+6, column=3)
        
        # Membuat button keluar dan pesan kamar
        tk.Button(self.master, text='Pesan Kamar', fg='green', command=self.booking).grid(row=len(self.dict_hotel)+7, column=3, sticky='w')
        self.master.bind('<Return>', self.booking)
        tk.Button(self.master, text='Keluar', fg='red', command=self.master.destroy).grid(row=len(self.dict_hotel)+7, column=3, sticky='e')

    # Method untuk membuat last sale
    def last_sale(self, username, hotel, room, total):
        # Pendapatan ditambahkan
        self.pendapatan += total

        # Membuat header
        tk.Label(self.master, text='LAST SALE').grid(row=len(self.dict_hotel)+8, column=1, sticky='w')
        tk.Label(self.master, text='Nama Pengguna').grid(row=len(self.dict_hotel)+9, column=1, sticky='w')
        tk.Label(self.master, text='Nama Hotel').grid(row=len(self.dict_hotel)+10, column=1, sticky='w')
        tk.Label(self.master, text='Jumlah Kamar').grid(row=len(self.dict_hotel)+11, column=1, sticky='w')
        tk.Label(self.master, text='Total').grid(row=len(self.dict_hotel)+12, column=1, sticky='w')
        tk.Label(self.master, text='Pendapatan').grid(row=len(self.dict_hotel)+13, column=1, sticky='e')

        for i in range(5):
            tk.Label(self.master, text=':').grid(row=len(self.dict_hotel)+9+i, column=2)

        # Membuat isi tabel
        tk.Label(self.master, text=username).grid(row=len(self.dict_hotel)+9, column=3 , sticky='w')
        tk.Label(self.master, text=hotel).grid(row=len(self.dict_hotel)+10, column=3, sticky='w')
        tk.Label(self.master, text=room).grid(row=len(self.dict_hotel)+11, column=3, sticky='w')
        tk.Label(self.master, text=f'Rp {total:,}').grid(row=len(self.dict_hotel)+12, column=3, sticky='w')
        tk.Label(self.master, text=f'Rp {self.pendapatan:,}').grid(row=len(self.dict_hotel)+13, column=3, sticky='w')

    # Method untuk booking
    def booking(self , event=None):
        # Mengambil input user
        username = self.username_entry.get()
        hotel = self.hotel_entry.get()
        room = self.room_entry.get()

        # Validasi input user
        if not username or not hotel or not room:
            messagebox.showerror("Error", "Tolong isi semua input.")
            return
        if hotel not in self.dict_hotel:
            messagebox.showerror("Error", f"Hotel {hotel} tidak ditemukan.")
            return
        if not room.isdigit():
            messagebox.showerror("Error", "Jumlah kamar harus berupa bilangan bulat.")
            return
        if  int(room) <= 0:
            messagebox.showerror("Error", "Jumlah kamar harus lebih dari 0.")
            return
        if int(room) > self.dict_hotel[hotel][0]:
            messagebox.showerror("Error", f"Tidak bisa memesan sebanyak {room} kamar di hotel {hotel}.")
            return

        # Mengurangi jumlah kamar di hotel
        self.dict_hotel[hotel][0] -= int(room)

        # Menghitung total biaya
        total = int(room) * self.dict_hotel[hotel][1]

        # Menampilkan pesan berhasil
        messagebox.showinfo("Success", f"Booking Berhasil! \nPesanan untuk {username} di hotel \n{hotel} sebanyak {room} kamar! \nTotal Biaya:  Rp {total:,} \nNomer Tiket: {self.dict_hotel[hotel][2]}/{self.dict_hotel[hotel][0]}/{username[:3]}")

        # Menghapus semua widget dan membuat homepage lagi dengan last sale
        for widget in self.master.winfo_children():
            widget.destroy()
        self.homepage()
        self.last_sale(username, hotel, room, total)

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
