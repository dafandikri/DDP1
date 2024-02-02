user_input = input("Masukkan string: ")
karakter = input("Masukkan karakter yang mau dihitung: ")
jumlah = 0

for char in user_input:
    if char == karakter:
        jumlah += 1

print(f"Jumlah karakter {karakter} dalam string {user_input} adalah {jumlah} buah.")