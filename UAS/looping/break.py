cuaca_hari = ['Cerah', 'Hujan', 'Berawan', 'Gerimis', 'Sejuk']
cuaca_input = input("Masukkan cuaca yang ingin dihentikan: ")

for cuaca in cuaca_hari:
    if cuaca == cuaca_input:
        break
    print("Cuaca hari ini: ", cuaca)

    
# ulang = int(input("Masukkan jumlah baris bintang yang ingin ditampilkan: "))
# print("Menampilkan bintang:")

# for count in range(1, ulang + 1):
#     if count > 5:
#         print("Jumlah baris terlalu banyak, menghentikan program.")
#         break
#     print('*' * count)


