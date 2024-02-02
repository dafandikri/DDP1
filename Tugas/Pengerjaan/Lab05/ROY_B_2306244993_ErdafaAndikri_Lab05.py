""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY
    Tanggal: 13 Oktober 2023

    Program ini dibuat untuk memenuhi tugas Lab 5.

    Program ini akan membuat sebuah database nilai lab untuk user.
    User dapat menambahkan data, melihat data, mengupdate data, dan menghapus data menggunakan nama sebagai ID.
    Program akan menampilkan menu dan user dapat memilih kegiatan yang ingin dilakukan.
    Program akan menampilkan pesan kesalahan jika user memasukkan input yang salah.
"""

# Menampilkan menu kegiatan
def printMenu():
    print("Selamat datang di Database Nilai Dek Depe")
    print("1. Tambah data ke database")
    print("2. Baca data dari database")
    print("3. Update data di database")
    print("4. Hapus data dari database")
    print("5. Keluar")

# Mengecek apakah nama sudah ada di database
def cekNama(nama, database):
    for i in range(len(database)):
        if nama.lower() == database[i][0]:
            return (True, i)
    return (False, -1)

# Kegiatan 1: Menambahkan data ke database
def kegiatan1(person, nama, database):
    counter = 1
    nilai = ""
    while nilai != "stop":
        nilai = str(input(f"Masukkan nilai Lab {counter} (ketik STOP untuk selesai): "))
        if nilai.lower() == "stop":
            counter -= 1
            break
        try:
            nilai = int(nilai)
            if nilai < 0 or nilai > 100:
                raise ValueError
        except:
            print("Masukkan sebuah angka bulat 0 sampai 100!")
            print()
            continue
        else:
            person.append(float(nilai))
            counter += 1
    database.append(person)
    print(f"Berhasil menambahkan {counter} nilai untuk {nama} ke database")

# Kegiatan 2, 3, dan 4: Melihat, mengupdate, dan menghapus data dari database
def kegiatan234(nama, database, kegiatan):
    # Menentukan kegiatan yang ingin dilakukan
    if kegiatan == 2:
        action = "lihat"
    elif kegiatan == 3:
        action = "update"
    else:
        action = "hapus"
    
    # Mengecek apakah nama ada di database
    nama_sama, i = cekNama(nama, database)

    # Jika nama ada di database
    if nama_sama == True:
        try:
            urutan_lab = int(input("Masukkan nilai Lab ke berapa yang ingin di" + action + ": "))
            # Mengecek apakah urutan lab ada di database dan tidak negatif
            if urutan_lab < 0 or urutan_lab > len(database[i]):
                raise IndexError
            if kegiatan == 2:
                if database[i][urutan_lab] == None:
                    raise IndexError
                else:
                    print(f"Nilai Lab {urutan_lab} {nama} adalah {database[i][urutan_lab]}")
            elif kegiatan == 3:
                nilai_baru = float(input(f"Masukkan nilai baru untuk Lab {urutan_lab}: "))
                nilai_lama = database[i][urutan_lab]
                database[i][urutan_lab] = nilai_baru
                print(f"Berhasil mengupdate nilai Lab {urutan_lab} {nama} dari {nilai_lama} ke {nilai_baru}")
            else:
                database[i][urutan_lab] = None
                print(f"Berhasil menghapus nilai Lab {urutan_lab} {nama} dari database")
        
    # Error handling
        # Apabila urutan lab tidak ada di database
        except IndexError:
            if urutan_lab < 0:
                print("Masukkan sebuah angka bulat positif!")
            else:
                print(f"Tidak terdapat nilai untuk Lab {urutan_lab}")
        # Apabila input bukan angka
        except TypeError:
            print("Input harus berupa angka!")
    # Apabila nama tidak ada di database
    else:
        print("Nama tidak ada dalam database")
        
# Main program
def main():
    database = []
    kegiatan = 0
    while kegiatan != 5:
        printMenu()
        try:
            kegiatan = int(input("Masukkan kegiatan yang ingin dilakukan: "))
            if kegiatan not in range(1, 6):
                raise TypeError
            if kegiatan == 5:
                break
        except:
            print("Masukkan sebuah angka bulat 1 sampai 5!")
            print()
            continue
        nama = str(input("Masukkan nama: "))
        person = []
        if kegiatan == 1:
            # Mengecek apakah nama ada di database
            nama_sama, i = cekNama(nama, database)
            if not nama_sama:
                person.append(nama.lower())
                kegiatan1(person, nama, database)
            else:
                print("Nama sudah ada di database")
                print()
                continue
        elif kegiatan == 2:
            kegiatan234(nama, database, kegiatan)
        elif kegiatan == 3:
            kegiatan234(nama, database, kegiatan)
        elif kegiatan == 4:
            kegiatan234(nama, database, kegiatan)
        elif kegiatan == 5:
            break
        print()
    print("Terimakasih telah menggunakan Database Nilai Dek Depe")

# Menjalankan main program
if __name__ == "__main__":
    main()