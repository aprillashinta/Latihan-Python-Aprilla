n = int(input("Masukkan jumlah bilangan ganjil yang ingin ditampilkan: "))
count = 0

for num in range(5, 50, 2):
    print(num)
    count += 1
    if count == n:
        break

# count = 0 
# for num in range(1, 100, 2):
#     print(num)
#     count += 1
#     if count == 5:
#         break