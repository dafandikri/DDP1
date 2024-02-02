n = int(input("Masukkan angka: "))
# for i in range(n, 0, -1):
#     median = i // 2
#     if i % 2 == 0:
#         for j in range(i, median, -1):
#             print(j, end=" ")
#         for k in range(median+1, i+1):
#             print(k, end=" ")
#     elif i % 2 == 1:
#         for l in range(i, median+1, -1):
#             print(l, end=" ")
#         for m in range(median+1, i+1):
#             print(m, end=" ")
#     print()

for i in range(n,0,-1) :
    median = i/2
    for j in range(1,i+1):
        if j <=  median :
            print(i,end="")
            i -= 1
        else :
            print(j, end="")
    print()
