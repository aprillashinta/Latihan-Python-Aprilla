# Program Perulangan Input Angka dengan Batasan Negatif
for i in range(5):
    angka = int(input("Masukkan angka (masukkan angka negatif untuk berhenti): "))
    
    if angka < 0:
        print("Perulangan dihentikan.")
        break
    
    print("Angka yang Anda masukkan:", angka)
