# Analisis keputusan investasi dari jumlah tabungan yang Anda miliki dan jenis investasi yang sesuai
risiko = int(input("Seberapa besar toleransi risikomu? (1-10): "))
tabungan = float(input("Berapa jumlah tabungan yang kamu miliki? (dalam rupiah): "))

if tabungan <= 1000000:
    pilihan = "Sebaiknya mulai dengan membeli Minigold/Antam/deposito."
elif tabungan <= 5000000:
    if risiko >= 8: 
        pilihan = "Investasi saham kecil atau emas Minigold/Antam."
    elif risiko >= 5:
        pilihan = "Reksa dana dan obligasi atau pertimbangkan membeli emas."
    elif risiko >= 3:
        pilihan = "Reksa dana pasar uang atau Minigold/Antam."
    else:
        pilihan = "Investasi aman seperti deposito."
elif tabungan < 20000000:
    if risiko >= 8:
        pilihan = "Saham atau cryptocurrency!"
    elif risiko >= 5:
        pilihan = "Saham dan obligasi."
    elif risiko >= 3:
        pilihan = "Pertimbangkan reksa dana campuran."
    else:
        pilihan = "Reksa dana konservatif lebih cocok."
else:
    if risiko >= 8:
        pilihan = "Investasi saham atau cryptocurrency lebih banyak!"
    elif risiko >= 5:
        pilihan = "Saham, obligasi, dan properti."
    elif risiko >= 3:
        pilihan = "Reksa dana campuran dan real estate."
    else:
        pilihan = "Investasi aman seperti obligasi dan reksa dana konservatif."

print("\nRekomendasi: ", pilihan)
