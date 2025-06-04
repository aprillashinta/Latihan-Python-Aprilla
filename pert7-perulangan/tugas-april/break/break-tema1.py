# Program untuk mencari angka dalam daftar
angka_dicari = int(input("Masukkan angka yang ingin dicari: "))
daftar_angka = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for angka in daftar_angka:
    if angka == angka_dicari:
        print("Angka", angka_dicari, "ditemukan!")
        break
else:
    print("Angka", angka_dicari, "tidak ditemukan dalam daftar.")
