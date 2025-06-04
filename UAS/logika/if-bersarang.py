cuaca = input("Masukkan cuaca saat ini (cerah/awan/hujan): ")

if cuaca == "hujan":
    print("Cuaca sekarang hujan, waktu untuk membawa payung!")
else:
    if cuaca == "cerah":
        print("Cuaca cerah, waktunya menikmati hari!")
    elif cuaca == "awan":
        print("Cuaca mendung, mungkin hujan sebentar lagi.")
    else:
        print("Cuaca tidak diketahui, cek lagi!")


# bintang = int(input("Masukkan jumlah baris bintang yang ingin ditampilkan: "))
# print("Menampilkan bintang:")

# count = 1
# if bintang > 0:
#     if count <= bintang:
#         while count <= bintang:
#             print('*' * count)
#             count += 1
#     else:
#         print("Tidak ada baris yang dapat ditampilkan.")
# else:
#     print("Jumlah baris harus lebih besar dari 0!")