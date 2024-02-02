""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY
    Tanggal: 24 November 2023

    Program ini dibuat untuk memenuhi tugas Lab 9.

    User diminta unutk input nama manager, jumlah pembayaran manager, dan stamina manager.

    Program akan menampilkan menu:
        1. Lihat status pegawai
            Menampilkan status manager dan pegawai dalam bentuk tabel (Class, Nama, Total kerja, Stamina, Gaji)

        2. Beri tugas
            User diminta untuk input nama pegawai, bonus pekerjaan, dan beban stamina. 
            Informasi ini akan digunakan untuk memanggil method give_work() dari class Manager.

        3. Cari pegawai baru
            User diminta untuk input nama pegawai baru. 
            Jika nama pegawai sudah ada, maka program akan mengeluarkan pesan error.

        4. Pecat pegawai
            User diminta untuk input nama pegawai yang akan dipecat.
            Jika nama pegawai tidak ada, maka program akan mengeluarkan pesan error.

        5. Keluar
            Program akan print goodbye message dan berhenti.

    Program ini menggunakan konsep inheritance seperti class Worker dan Manager yang merupakan subclass dari class Person.
    Program ini juga menggunakan konsep polymorphism seperti method work() yang berbeda implementasinya di class Worker.
"""

class Person:
    # Inisialisasi class Person
    def __init__(self, name, payment, stamina):
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0


    # Getter dan setter
    @property
    def name(self):
        return self.__name
    
    @property
    def payment(self):
        return self.__payment
    
    @property
    def stamina(self):
        return self.__stamina
    
    @stamina.setter
    def stamina(self, new_stamina):
        self.__stamina = new_stamina

    @property
    def total_work(self):
        return self.__total_work
    
    @total_work.setter
    def total_work(self, new_total_work):
        self.__total_work = new_total_work
        

    # Fungsi untuk mengecek apakah stamina cukup untuk bekerja
    def is_available(self,cost_stamina):
        return self.__stamina >= cost_stamina

    # Fungsi kalkulasi gaji
    def pay_day(self):
        return self.__payment * self.__total_work

    # Fungsi kerja
    def work(self, cost_stamina):
        self.__stamina -= cost_stamina
        self.__total_work += 1
    
    # Fungsi saat diprint
    def __str__(self):
        return f"{self.__class__.__name__:20} | {self.__name:20} | Total kerja: {self.__total_work:20} | Stamina:{self.__stamina:20} | Gaji:{self.pay_day():20}"
    

class Worker(Person):
    # Inisialisasi class Worker
    def __init__(self, name):
        super().__init__(name, payment=5000, stamina=100)
        self.__bonus = 0
    
    
    # Getter dan setter
    @property
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def bonus(self, new_bonus):
        self.__bonus = new_bonus


    # Fungsi kalkulasi gaji + bonus (dikarenakan worker punya bonus)
    def pay_day(self):
        return self.payment * self.total_work + self.__bonus

    # Fungsi kerja + bonus (dikarenakan worker diberikan bonus)
    def work(self, bonus, cost_stamina):
        super().work(cost_stamina)
        self.__bonus += bonus

    # Fungsi get dan set bonus
    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, new_bonus):
        self.__bonus = new_bonus    


class Manager(Person):
    # Inisialisasi class Manager
    def __init__(self, name, payment, stamina):
        super().__init__(name, payment, stamina)
        self.__list_worker = []


    # Getter
    @property
    def list_worker(self):
        return self.__list_worker
        

    # Fungsi get list worker
    def get_list_worker(self):
        return self.__list_worker

    # Fungsi untuk meng-hire karyawan baru dengan nama yang unik
    def hire_worker(self, name):
        for worker in self.__list_worker:
            if worker.name == name:
                self.stamina -= 10
                print("Sudah ada!")
                return
        new_worker = Worker(name)
        self.__list_worker.append(new_worker)
        self.work(10)
        print("Berhasil mendapat pegawai baru")
    
    # Fungsi untuk memecat karyawan dari list nama yang ada
    def fire_worker(self, name):
        for worker in self.__list_worker:
            if worker.name == name:
                self.__list_worker.remove(worker)
                self.work(10)
                print("Berhasil memecat " + name)
                return
        self.stamina -= 10
        print("Nama tidak ditemukan")

    # Fungsi untuk memberi tugas kepada karyawan dari list nama yang ada
    def give_work(self, name, bonus ,cost_stamina):
        for worker in self.__list_worker:
            if worker.name == name:
                if not worker.is_available(cost_stamina):
                    self.stamina -= 10
                    print("Pegawai tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup.")
                    return
                worker.work(bonus, cost_stamina)
                self.work(10)
                print("""Pegawai dapat menerima pekerjaan
========================================
Berhasil memberi pekerjaan kepada """ + name)
                return
        self.stamina -= 10
        print("Nama tidak ditemukan")


# Main program
def main():
    # Input nama manager, jumlah pembayaran, dan stamina
    name = input("Masukkan nama manajer: ").title()
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    # Inisialisasi class Manager
    manager = Manager(name, payment, stamina)

    # Looping menu
    while manager.is_available(1):
        print("""
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """)
        action = int(input("Masukkan pilihan: "))

        if action == 1:
            list_worker = manager.get_list_worker()
            print(manager)
            for worker in list_worker:
                print(worker)

        elif action == 2:
            name = input("Tugas akan diberikan kepada: ").title()
            bonus = int(input("Bonus pekerjaan: "))
            cost_stamina = int(input("Beban stamina: "))
            print("Hasil cek ketersediaan pegawai:")
            manager.give_work(name, bonus, cost_stamina)

        elif action == 3:
            name = input("Masukkan nama pegawai baru: ").title()
            manager.hire_worker(name)

        elif action == 4:
            name = input("Nama pegawai yang akan dipecat: ").title()
            manager.fire_worker(name)

        elif action == 5:
            print("""
----------------------------------------
Berhenti mengawasi hotel, sampai jumpa !
----------------------------------------""")
            return
    print("""
----------------------------------------
Stamina manajer sudah habis, sampai jumpa !
----------------------------------------""")
if __name__ == "__main__":
    main()
