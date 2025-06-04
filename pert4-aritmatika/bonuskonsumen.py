# id_pelanggan = input("Masukkan Id Pelanggan     : ")
# nama_pelanggan = input("Masukkan Nama Pelanggan   : ")
# id_barang = input("Masukkan Id Barang        : ")
# barang = input("Masukkan Barang           : ")
# harga_satuan = int(input("Masukkan Harga Satuan     : Rp "))
# jumlah_beli = int(input("Masukkan Jumlah Beli      : "))

# print("         SWALAYAN 'SAMI LARIZO' SOLO")
# print("=" * 40)
# print ("Id Pelanggan      :", id_pelanggan)
# print ("Nama Pelanggan :", nama_pelanggan)
# print ("Id Barang :", id_barang)
# print ("Nama Barang :", barang)
# print ("Harga Satuan :", harga_satuan)
# print ("Jumlah Beli :", jumlah_beli)

# jumlah_belanja = harga_satuan * jumlah_beli

# if jumlah_belanja >= 3000000:
#     bonus = "TAS CANTIK"
# else:
#     bonus = "Voucher Belanja"

# print("\n---------- Total Pembayaran -----------")
# print("Jumlah Belanja   : Rp", jumlah_belanja)
# print("Bonus            :", bonus)

# uang_pelanggan = int(input("Uang Pelanggan   : Rp "))
# kembalian = uang_pelanggan - jumlah_belanja

# print("Kembalian        : Rp", kembalian)
# print("\nKasir, \nDRUPADI CANTIX")

# ==================================================================


id_pelanggan = input("Masukkan Id Pelanggan     : ")
nama_pelanggan = input("Masukkan Nama Pelanggan   : ")
id_barang = input("Masukkan Id Barang        : ")
barang = input("Masukkan Nama Barang      : ")
harga_satuan = int(input("Masukkan Harga Satuan     : Rp "))
jumlah_beli = int(input("Masukkan Jumlah Beli      : "))

print("\n" + "=" * 50)
print("             SWALAYAN 'SAMI LARIZO' SOLO")
print("=" * 50)

print ("Id Pelanggan    :", id_pelanggan)
print ("Nama Pelanggan  :", nama_pelanggan)
print ("Id Barang       :", id_barang)
print ("Nama Barang     :", barang)
print ("Harga Satuan    :", harga_satuan)
print ("Jumlah Beli     :", jumlah_beli)

jumlah_belanja = harga_satuan * jumlah_beli

if jumlah_belanja >= 3000000:
    bonus = "TAS CANTIK"
else:
    bonus = "Voucher Belanja"

print("\n---------- Total Pembayaran -----------")
print("Jumlah Belanja    : Rp", jumlah_belanja)
print("Bonus             :", bonus)

uang_pelanggan = int(input("\nUang Pelanggan    : Rp "))
kembalian = uang_pelanggan - jumlah_belanja

print("Kembalian         : Rp", kembalian)
print("\nKasir,")
print("DRUPADI CANTIX")
print("=" * 50)
