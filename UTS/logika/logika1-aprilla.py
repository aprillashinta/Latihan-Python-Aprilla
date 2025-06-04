jenis_kulit = input("Jenis kulit (kering, berminyak, kombinasi, sensitif): ")
masalah_kulit = input("Masalah kulit (jerawat, penuaan, dehidrasi): ")

if jenis_kulit == "kering":
    if masalah_kulit == "jerawat":
        rekomendasi = "Pembersih lembut dan pelembap krim."
    elif masalah_kulit == "penuaan":
        rekomendasi = "Serum hyaluronic acid."
    else:
        rekomendasi = "Pelembap intensif."

elif jenis_kulit == "berminyak":
    if masalah_kulit == "jerawat":
        rekomendasi = "Pembersih gel dan eksfoliator."
    elif masalah_kulit == "penuaan":
        rekomendasi = "Serum anti-aging ringan."
    else:
        rekomendasi = "Pelembap oil-free."

elif jenis_kulit == "kombinasi":
    if masalah_kulit == "jerawat":
        rekomendasi = "Pembersih lembut dan toner."
    elif masalah_kulit == "penuaan":
        rekomendasi = "Serum seimbang."
    else:
        rekomendasi = "Pelembap ringan."

else:  # kulit sensitif
    if masalah_kulit == "jerawat":
        rekomendasi = "Pembersih hypoallergenic."
    elif masalah_kulit == "penuaan":
        rekomendasi = "Serum alami."
    else:
        rekomendasi = "Pelembap hypoallergenic."

print("\nRekomendasi: ", rekomendasi)


# volume = int(input("Masukkan volume cintamu padaku (dalam persen): "))

# if volume >= 90:
#     print("Cintamu padaku tak terhingga")
# elif volume >= 70:
#     print("Cintamu padaku begitu dalam")
# elif volume >= 50:
#     print("Cintamu padaku kuat")
# elif volume >= 30:
#     print("Cintamu padaku perlahan tumbuh")
# else:
#     print("Cintamu padaku mungkin kecil")
