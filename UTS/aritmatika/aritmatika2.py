ukuran_file = float(input("Masukkan Ukuran File (dalam MB)           : "))
kecepatan_internet = float(input("Masukkan Kecepatan Internet (dalam Mbps)  : "))

kecepatan_MBps = kecepatan_internet / 8
waktu_unduh = ukuran_file / kecepatan_MBps

print("\n" + "=" * 70)
print("                     PERHITUNGAN WAKTU UNDUH FILE")
print("=" * 70)
print("Ukuran file                  :", ukuran_file, "MB")
print("Kecepatan internet           :", kecepatan_internet, "Mbps")
print("\nHasil Perhitungan Waktu Unduh:")
print("-> Berdasarkan ukuran file dan kecepatan internet, waktu yang")
print("   dibutuhkan untuk mengunduh file tersebut adalah:")
print("      Waktu Unduh            :", waktu_unduh, "detik")
print("=" * 70)
print("Catatan: \nWaktu ini bisa berubah tergantung kestabilan jaringan internet Anda.")