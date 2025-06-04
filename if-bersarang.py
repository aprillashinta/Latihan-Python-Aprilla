print("Selamat datang di Aplikasi Perkiraan Cuaca!\n")

suhu = float(input("Masukkan suhu udara (dalam Celsius)  : "))
kelembapan = float(input("Masukkan kelembapan udara (%)        : "))

if suhu > 30:
    cuaca = "Panas"
    rekomendasi = ["Minumlah banyak air dan mengenakan pakaian tipis."]
elif suhu >= 20 and suhu <= 30:
    cuaca = "Cerah"
    rekomendasi = ["Cuaca cukup baik, gunakan pakaian ringan."]
elif suhu >= 10 and suhu < 20:
    cuaca = "Dingin"
    rekomendasi = ["Mungkin perlu jaket atau sweater."]
else:
    cuaca = "Sangat dingin"
    rekomendasi = ["Pastikan Anda memakai pakaian hangat."]

if kelembapan > 80:
    cuaca += " dan Lembap"
    rekomendasi.append("Cuaca lembap, hati-hati dengan kemungkinan hujan.")
elif kelembapan < 40:
    cuaca += " dan Kering"
    rekomendasi.append("Hati-hati dengan udara yang sangat kering.")

print("\n" + "=" * 50)
print(f"{'Perkiraan Cuaca':^50}")
print("=" * 50)
print("Cuaca: ", cuaca)
print("\nRekomendasi: ")
for poin in rekomendasi:
    print("- ", poin)
print("=" * 50)




# cuaca = input("Masukkan cuaca saat ini (cerah/awan/hujan): ")

# if cuaca == "hujan":
#     print("Cuaca sekarang hujan, waktu untuk membawa payung!")
# else:
#     if cuaca == "cerah":
#         print("Cuaca cerah, waktunya menikmati hari!")
#     elif cuaca == "awan":
#         print("Cuaca mendung, mungkin hujan sebentar lagi.")
#     else:
#         print("Cuaca tidak diketahui, cek lagi!")


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