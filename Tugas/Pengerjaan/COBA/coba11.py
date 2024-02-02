kata_depan = ["dalam","atas","antara","kepada","akan","terhadap","oleh","dengan","berkat","tentang","sampai","guna","demi","untuk","bagi","menurut"]
open_file = open("puisi.txt")
read_file = open_file.read()
read_file = read_file.lower()
list_read_file = read_file.split()
counter = 0
for word in list_read_file:
    if word in kata_depan:
        counter+=1

print(counter)