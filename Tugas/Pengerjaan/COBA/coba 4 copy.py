try:
    my_file = open("myfile.txt", "r")
    print(my_file.readlines())
    my_file.close()
except FileNotFoundError:
    print("File not found")