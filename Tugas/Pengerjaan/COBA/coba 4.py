file_read = open("file1.txt", "rt")
for line in file_read.readlines():
    print(line.strip())