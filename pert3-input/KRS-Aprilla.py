# print ("FAKULTAS ILMU KOMPUTER - UNIVERSITAS DUTA BANGSA SURAKARTA")
# print ("              Jl. Bhayangkara 55, Surakarta")
# print ("==============================================================")
# print ("                    KARTU RENCANA STUDI")
# print ("NIM             : 240101065")
# print ("Nama            : Aprilla Addivi Tiar Almashinta")
# print ("Program Studi   : Sistem Informasi")
# print ("Kelas           : 24-SI-A3")
# print ("--------------------------------------------------------------")
# print ("MATA KULIAH YANG DIAMBIL :")
# print ("")
# print ("Matakuliah 1    : Algoritma dan Struktur Data")
# print ("SKS             : 3")
# print ("Matakuliah 2    : Pengantar Teknologi Informasi")
# print ("SKS             : 2")
# print ("Matakuliah 3    : Matematika Dasar")
# print ("SKS             : 3")
# print ("Matakuliah 4    : Arsitektur dan Organisasi Komputer")
# print ("SKS             : 3")
# print ("Matakuliah 5    : Konsep Sistem Informasi")
# print ("SKS             : 2")
# print ("Matakuliah 6    : Bisnis dan Manajemen")
# print ("SKS             : 2")
# print ("Matakuliah 7    : Bahasa Inggris 1")
# print ("SKS             : 2")
# print ("Matakuliah 8    : Dasar Pemrograman")
# print ("SKS             : 3")
# print ("==============================================================")


nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")
program_studi = input("Masukkan Program Studi: ")
kelas = input("Masukkan Kelas: ")

mata_kuliah = []
jumlah_sks = []

for i in range(8):
    mk = input(f"Masukkan Mata Kuliah {i+1}: ")
    sks = input(f"Masukkan SKS untuk {mk}: ")
    mata_kuliah.append(mk)
    jumlah_sks.append(sks)

print("\nFAKULTAS ILMU KOMPUTER - UNIVERSITAS DUTA BANGSA SURAKARTA")
print("              Jl. Bhayangkara 55, Surakarta")
print("==============================================================")
print("                    KARTU RENCANA STUDI")
print(f"NIM             : {nim}")
print(f"Nama            : {nama}")
print(f"Program Studi   : {program_studi}")
print(f"Kelas           : {kelas}")
print("--------------------------------------------------------------")
print("\nMATA KULIAH YANG DIAMBIL :")

for i in range(8):
    print(f"Matakuliah {i+1}    : {mata_kuliah[i]}")
    print(f"SKS             : {jumlah_sks[i]}")

print("==============================================================")