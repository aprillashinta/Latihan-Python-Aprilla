while True:
    angka1 = int(input("\nMasukkan Angka-1: "))
    angka2 = int(input("Masukkan Angka-2: "))
    pilih_pengoprasi = input("Pilih Pengoprasi (+, -, *, /): ")

    if pilih_pengoprasi == "+":
        hasil = angka1 + angka2
    elif pilih_pengoprasi == "-":
        hasil = angka1 - angka2
    elif pilih_pengoprasi == "*":
        hasil = angka1 * angka2
    elif pilih_pengoprasi == "/":
        hasil = angka1 / angka2
    else:
        hasil = "Operasi aritmatika yang Anda pilih tidak tersedia."

    print("-" * 40)
    print("Angka-1:", angka1)
    print("Angka-2:", angka2)
    print("Operasi yang dipilih (+, -, *, /):", pilih_pengoprasi)
    print("=" * 40)
    print("Hasil:", hasil)
    print("=" * 40)

    print("Selamat Jawaban Anda Tampil")
    print("-" * 40)

    ulang = input("Tombol ULANG (y/n)? ").lower()
    print("=" * 40)
    if ulang != "y":
        print("Terima kasih telah menggunakan kalkulator!")
        break


# for _ in range(3):
#     angka1 = int(input("Masukkan Angka-1: "))
#     angka2 = int(input("Masukkan Angka-2: "))
#     pilih_pengoprasi = input("Pilih Pengoprasi (+, -, *, /): ")

#     if pilih_pengoprasi == "+":
#         hasil = angka1 + angka2
#     elif pilih_pengoprasi == "-":
#         hasil = angka1 - angka2
#     elif pilih_pengoprasi == "*":
#         hasil = angka1 * angka2
#     elif pilih_pengoprasi == "/" and angka2 != 0:
#         hasil = angka1 / angka2
#     elif pilih_pengoprasi == "/" and angka2 == 0:
#         hasil = "Error: Pembagian dengan nol tidak diizinkan."
#     else:
#         hasil = "Pengoprasi yang Anda pilih tidak tersedia."

#     print("===================================")
#     print("Masukkan Angka-1:", angka1)
#     print("Masukkan Angka-2:", angka2)
#     print("Pilih Pengoprasi (+, -, *, /):", pilih_pengoprasi)
#     print("===================================")
#     print("Hasil:", hasil)
#     print("===================================")

#     print("Selamat Jawaban Anda Tampil")
#     print("===================================")

# print("Terima kasih telah menggunakan kalkulator!")