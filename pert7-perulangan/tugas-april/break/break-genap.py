n = int(input("Masukkan jumlah bilangan genap yang ingin ditampilkan: "))
count = 0

for num in range(2, 100, 2):
    print(num)
    count += 1
    if count == n:
        break
