# definikan fungsi 
def tampilkan_ktp(): 
    # Mengambil input NIK dari pengguna
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan Nama: ")
    tempat_lahir = input("Masukkan Tempat Lahir: ")
    tanggal_lahir = input("Masukkan Tanggal Lahir (dd-mm-yyyy): ")
    jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ")
    golongan_darah = input("Masukkan Golongan Darah: ")
    alamat = input("Masukkan Alamat: ")
    rt_rw = input("Masukkan RT/RW: ")
    kel_desa = input("Masukkan Kel/Desa: ")
    kecamatan = input("Masukkan Kecamatan: ")
    agama = input("Masukkan Agama: ")
    status_perkawinan = input("Masukkan Status Perkawinan: ")
    pekerjaan = input("Masukkan Pekerjaan: ")
    kewarganegaraan = input("Masukkan Kewarganegaraan: ")

    print("\nTAMPIL HASIL INPUT DATA KTP:")
    
    print ("            PROVINSI JAWA TENGAH")    
    print ("            KABUPATEN SUKOHARJO")

    print(f"NIK              : {nik}")
    print(f"Nama             : {nama}")
    print(f"Tempat/Tgl Lahir : {tempat_lahir}, {tanggal_lahir}")
    print(f"Jenis Kelamin    : {jenis_kelamin}        Gol. Darah : {golongan_darah}")
    print(f"Alamat           : {alamat}")
    print(f"    RT/RW        : {rt_rw}")
    print(f"    Kel/Desa     : {kel_desa}")
    print(f"    Kecamatan    : {kecamatan}")
    print(f"Agama            : {agama}")
    print(f"Status Kawin     : {status_perkawinan}")
    print(f"Pekerjaan        : {pekerjaan}")
    print(f"Kewarganegaraan  : {kewarganegaraan}")

tampilkan_ktp()
