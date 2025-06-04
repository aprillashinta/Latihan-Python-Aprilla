nama_toko = "Goldie Aprilla Shinta"
nama_pemilik = input("Masukkan Nama Pemilik            : ")
tanggal_pembelian = input("Masukkan Tanggal Pembelian       : ")
harga_per_gram = int(input("Masukkan Harga Emas per Gram (Rp): "))
berat_emas = int(input("Masukkan Berat Emas (gram)       : "))

total_harga = harga_per_gram * berat_emas

print("\n" + "=" * 60)
print(f"                   {nama_toko.upper()}")
print("            SURAT PERNYATAAN KEPEMILIKAN EMAS")
print("=" * 60)
print("Nama Pemilik           :", nama_pemilik)
print("Tanggal Pembelian      :", tanggal_pembelian)
print(f"Harga Emas per Gram    : Rp {harga_per_gram:,.2f}")
print(f"Berat Emas             : {berat_emas} gram")
print(f"Total Harga            : Rp {total_harga:,.2f}")
print("=" * 60)
print("Mohon simpan surat ini sebagai bukti kepemilikan.")

print("\nKasir,\nAprilla Shinta")
print("=" * 60)
