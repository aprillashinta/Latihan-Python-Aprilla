nama_pembeli = input("Masukkan Nama Pembeli: ")
id_barang = input("Masukkan ID Barang: ")
nama_barang = input("Masukkan Nama Barang: ")
harga_satuan = int(input("Masukkan Harga Satuan: Rp "))
jumlah_beli = int(input("Masukkan Jumlah Beli: "))

total_bayar = harga_satuan * jumlah_beli

print("\n========================================")
print("TOKO SPAREPART & AKSESORIS MOTOR")
print("TOKO APRILLA ADDIVI TIAR ALMASHINTA")
print("=" * 40)

print(f"\nNama Pembeli : {nama_pembeli}")
print(f"ID Barang    : {id_barang}")
print(f"Nama Barang  : {nama_barang}")
print(f"Harga Satuan : Rp. {harga_satuan:.2f}")
print(f"Jumlah Beli  : {jumlah_beli}")
print(f"Total Bayar  : Rp. {total_bayar:.2f}")
print("-" * 40)
print(f"Total Pembayaran Rp {total_bayar}")
print("\nKasir,\nDRUPADI CANTIX")
print("=" * 40)
