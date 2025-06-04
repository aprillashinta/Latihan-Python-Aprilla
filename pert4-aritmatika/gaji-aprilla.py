id_karyawan = input("Masukkan ID Karyawan: ")
nama_karyawan = input("Masukkan Nama Karyawan: ")
gaji_pokok = int(input("Masukkan Gaji Pokok: Rp. "))
jam_kerja = int(input("Masukkan Jam Kerja: "))

gaji_kotor = gaji_pokok * jam_kerja
pajak = 0.10
potongan = pajak * gaji_kotor
gaji_bersih = gaji_kotor - potongan

print("\n==================================================")
print("PT. TSELALOE OEN TOENK")
print("Jl. Tselalu Bahagia No. 13, Klaten")
print("==================================================")
print(f"ID Karyawan: {id_karyawan}")
print(f"Nama Karyawan: {nama_karyawan}")
print(f"Gaji Pokok: {int(gaji_pokok)}")
print(f"Jam Kerja: {int(jam_kerja)}")
print("--------------------------------------------------")
print(f"Gaji Kotor: Rp. {gaji_kotor:,.2f}")
print(f"Potongan Pajak (10%): Rp. {potongan:,.2f}")
print(f"Gaji Bersih: Rp. {gaji_bersih:,.2f}")
print("==================================================")
print(f"Total Gaji Bersih Karyawan: Rp. {gaji_bersih:,.2f}")