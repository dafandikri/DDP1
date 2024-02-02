# Input: pesan_zog, angka_1, angka_2
pesan_zog=str(input("Masukkan pesan Kelompok Zog: "))
angka_1=int(input("Masukkan angka 1: "))
angka_2=int(input("Masukkan angka 2: "))
print()

# Konversi pesan ke ASCII
bytes_string = bytes.fromhex(pesan_zog)
ascii_string = bytes_string.decode("ASCII")

# Cetak hasil terjemahan pesan
print(f"Hasil terjemahan pesan: {ascii_string}")

# mendapatkan password dengan mengalikan angka_1, angka_2, dan 13
string_biner = bin(angka_1*angka_2*13) 

# Cetak pesan dan password
print(f"Password: {string_biner}")
print()
print(f"Pesan '{ascii_string}' telah diterima dengan password '{string_biner}'")
