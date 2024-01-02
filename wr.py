# Saya akan membuat sebuah aplikasi kalkulator yang dapat memprediksi atau menghitung
# Winrate dari sebuah hero Dari game Mobile Legends Bang Bang tanpa dataset

# Input
# - nama hero
# - total match
# - total winrate saat ini
# - total winrate yang ingin dicapai

# Proses
# - hitung total match yang harus dimenangkan tanpa kekalahan untuk mencapai winrate yang diinginkan

# Output
# - total match yang harus dimenangkan tanpa kekalahan

# Input
total_match = int(input("Masukkan total match: "))
winrate_saat_ini = float(input("Masukkan winrate saat ini: "))
winrate_yang_diinginkan = float(input("Masukkan winrate yang diinginkan: "))
# Proses
result = (winrate_yang_diinginkan * total_match - winrate_saat_ini *
          total_match) / (100 - winrate_yang_diinginkan)
result = round(result)


# Output
print(
    f"Total match yang harus dimenangkan untuk mencapai winrate yang diinginkan adalah {result} match")
