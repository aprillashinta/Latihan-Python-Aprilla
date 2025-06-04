# ganjil
# for b in range(3, 25, 1):
#     if b % 2 == 0:
#         continue
#     print(b)

# genap
# for b in range(1, 11, 1):
#     if b % 2 != 0:
#         continue
#     print(b)


# Tema 1: Menampilkan Angka yang Tidak Mengandung Digit 5
# start = int(input("Masukkan angka mulai: "))
# end = int(input("Masukkan angka akhir: "))

# for num in range(start, end + 1):
#     if '5' in str(num):
#         continue
#     print(num)

# Tema 2: Menampilkan Bilangan Genap yang Tidak Terbagi 4
start = int(input("Masukkan angka mulai: "))
end = int(input("Masukkan angka akhir: "))

for num in range(start, end + 1):
    if num % 2 != 0:
        continue
    if num % 4 == 0:
        continue
    print(num)


