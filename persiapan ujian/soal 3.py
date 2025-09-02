jarak = float(input("jarak perjalanan dalam jangka jauh: "))
pengeluaran = float(input(" Konsumsi bahan bakar: "))
harga = float(input(" Harga bensin per liter: "))

liter_bensin = jarak/pengeluaran

hasil = jarak*pengeluaran
print(f"Untuk perjalanan {jarak} km, Anda membutuhkan {liter_bensin:.2f} liter bensin dengan total biaya Rp {hasil:.2f}")









