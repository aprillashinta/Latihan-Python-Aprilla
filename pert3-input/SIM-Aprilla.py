def tampilkan_sim():
    golongan_sim = input("Masukkan Golongan SIM (A/B/C): ")
    no_sim = input("Masukkan No SIM: ")
    nama = input("Masukkan Nama Lengkap: ")
    tempat_lahir = input("Masukkan Tempat lahir: ")
    tanggal_lahir = input("Masukkan Tanggal Lahir (dd-mm-yyyy): ")
    jenis_kelamin = input("Masukkan Jenis Kelamin (PRIA/WANITA): ")
    tempat_tinggal = input("Masukkan Tempat Tinggal: ")
    pekerjaan = input("Masukkan Pekerjaan: ")
    domisili = input("Masukkan Domisili: ")
    tanggal_berlaku = input("Masukkan Tanggal Berlaku SIM (dd-mm-yyyy): ")

    print ("\nTAMPIL HASIL INPUT DATA SIM:")
    print ("------------------------------------------------------------")
    print ("            KEPOLISIAN NEGARA REPUBLIK INDONESIA")
    print ("                    SURAT IZIN MENGEMUDI")
    print ("============================================================")
    print (f"Jenis SIM         : {golongan_sim}")
    print (f"Nomor SIM         : {no_sim}")
    print (f"Nama Lengkap      : {nama}")
    print (f"Tempat/Tgl Lahir  : {tempat_lahir}, {tanggal_lahir}")
    print (f"Jenis Kelamin     : -- {jenis_kelamin}")
    print (f"Alamat            : {tempat_tinggal}")
    print (f"Pekerjaan         : {pekerjaan}")
    print (f"Domisili          : POLDA {domisili}")
    print (f"Tanggal Berlaku   : {tanggal_berlaku}")
    print ("------------------------------------------------------------")

tampilkan_sim()