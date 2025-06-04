# Daftar menu makanan dan minuman di cafe Eating
menu_makanan = ["Brownies", "Strawberry Waffle", "Cheesecake"]
menu_minuman = ["Hot Chocolate", "Green Tea Latte", "Caffe Latte"]
keranjang = []  # Menyimpan daftar pesanan
harga = []  # Menyimpan harga pesanan

# Fungsi untuk menampilkan menu awal
def menu_awal():
    print("-------------------- DAFTAR MENU --------------------")
    print("=" * 50)
    print("1. Makanan")
    print("2. Minuman")
    print("=" * 50)
    for ver in keranjang:  # Menampilkan isi keranjang
        print(f"Pemesanan Anda : {ver}")
    pilih1 = int(input("Pilih nomor jenis pesanan Anda : "))
    if pilih1 == 1:
        daftar_makanan()
    elif pilih1 == 2:
        daftar_minuman()
    else:
        print("Menu belum terdaftar!")
        menu_awal()

# Fungsi untuk menampilkan daftar makanan
def daftar_makanan():
    print("------------------- DAFTAR MAKANAN -------------------")
    print("1. Brownies          = Rp. 15.000")
    print("2. Strawberry Waffle = Rp. 20.000")
    print("3. Cheesecake        = Rp. 25.000")
    print("=" * 50)
    pilihan_makanan = int(input("Pilih nomor pesanan Anda : "))
    if pilihan_makanan == 1:
        keranjang.append(menu_makanan[0])
        jumlah = int(input("Jumlah Pesanan : "))
        if jumlah > 0:
            harga.append(15000 * jumlah)
        else:
            print("Jumlah tidak valid!")
    elif pilihan_makanan == 2:
        keranjang.append(menu_makanan[1])
        jumlah = int(input("Jumlah Pesanan : "))
        if jumlah > 0:
            harga.append(20000 * jumlah)
        else:
            print("Jumlah tidak valid!")
    elif pilihan_makanan == 3:
        keranjang.append(menu_makanan[2])
        jumlah = int(input("Jumlah Pesanan : "))
        if jumlah > 0:
            harga.append(25000 * jumlah)
        else:
            print("Jumlah tidak valid!")
    else:
        print("Pilihan Tidak Valid!")
    tanya()

# Fungsi untuk menampilkan daftar minuman
def daftar_minuman():
    print("------------------- DAFTAR MINUMAN -------------------")
    print("1. Hot Chocolate     = Rp. 18.000")
    print("2. Green Tea Latte   = Rp. 20.000")
    print("3. Caffe Latte       = Rp. 25.000")
    print("=" * 50)
    pilihan_minuman = int(input("Pilih nomor pesanan Anda : "))
    if pilihan_minuman == 1:
        keranjang.append(menu_minuman[0])
        jumlah = int(input("Jumlah Pesanan : "))
        if jumlah > 0:
            harga.append(18000 * jumlah)
        else:
            print("Jumlah tidak valid!")
    elif pilihan_minuman == 2:
        keranjang.append(menu_minuman[1])
        jumlah = int(input("Jumlah Pesanan : "))
        if jumlah > 0:
            harga.append(20000 * jumlah)
        else:
            print("Jumlah tidak valid!")
    elif pilihan_minuman == 3:
        keranjang.append(menu_minuman[2])
        jumlah = int(input("Jumlah Pesanan : "))
        if jumlah > 0:
            harga.append(25000 * jumlah)
        else:
            print("Jumlah tidak valid!")
    else:
        print("Pilihan Tidak Valid!")
    tanya()

# Fungsi untuk menanyakan tambahan pesanan
def tanya():
    pilihan = input("Apa ada tambahan menu (y/t) : ").lower()
    if pilihan == "y":
        menu_awal()
    elif pilihan == "t":
        hasil()
    else:
        print("Pilihan [y] untuk ya dan [t] untuk tidak")
        tanya()

# Fungsi untuk menghitung hasil pesanan
def hasil():
    print("-------------------- EATING CAFE --------------------")
    print(f"Anda memesan : {', '.join(keranjang)}")
    jumlah = sum(harga)  # Menghitung total harga
    total_item = len(keranjang)  # Menghitung total item dalam keranjang
    
    diskon = 0  # Variabel diskon untuk mencatat diskon yang diterima
    if total_item > 4:  # Jika lebih dari 4 item, memberikan diskon
        print("Selamat! Anda mendapatkan diskon 10%.")
        diskon = 0.1 * jumlah
        jumlah *= 0.9  # Mengurangi total harga sebesar 10%

    print("=" * 50)
    print("STRUK PEMBAYARAN")
    print("=" * 50)
    print(f"Total Pesanan: {total_item} item")
    print(f"Total Harga Sebelum Diskon: Rp {int(sum(harga))}")
    if diskon > 0:  # Menampilkan keterangan diskon jika ada
        print(f"Diskon (10%): -Rp {int(diskon)}")
    print(f"Total Pembayaran Setelah Diskon: Rp {int(jumlah)}")
    print("=" * 50)
    
    bayar = float(input("Bayar       : "))
    if bayar >= jumlah:
        kembalian = bayar - jumlah
        print("=" * 50)
        print("Jumlah Uang Kebalian Anda : Rp ", int(kembalian))
    else:
        print("Uang Anda tidak cukup!")
        hasil()

# Memulai program
menu_awal()