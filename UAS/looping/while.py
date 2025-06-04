cuaca = ['cerah', 'berawan', 'hujan', 'angin kencang', 'kabut', 'salju', 'petir']

while True:
    print("\nPilih cuaca berikut ini:")
    for i in range(len(cuaca)):
        print(f"{i+1}. {cuaca[i]}")
    
    pilihan = input("\nMasukkan nomor cuaca atau ketik 'stop' untuk berhenti: ").lower()
    
    if pilihan == 'stop':
        print("Program dihentikan.")
        break
    
    pilih = int(pilihan) - 1  # Mengurangi 1 agar sesuai dengan indeks list
    if 0 <= pilih < len(cuaca):
        print(f"Cuaca yang Anda pilih: {cuaca[pilih]}")
    else:
        print("Pilihan tidak valid. Coba lagi.")








cuaca = "cerah"
while cuaca != "hujan":
    print("Cuaca saat ini adalah", cuaca)
    cuaca = input("Masukkan cuaca baru (cerah/awan/hujan): ")

print("Cuaca sekarang hujan, bawalah payung!")


# ulang = int(input("Masukkan jumlah baris bintang yang ingin ditampilkan: "))
# print("Menampilkan bintang:")
# count = 1
# while count <= ulang:
#     print('*' * count)
#     count += 1