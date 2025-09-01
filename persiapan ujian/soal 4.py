hari_kunjungan = input('masukan hari: ')
usia = int(input("Umur lu berapa sekarang: "))
harga = 75000

if usia < 5 or usia > 60:
    harga *= 0.5
elif hari_kunjungan in ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu']:
    harga *= 0.8
else:
    harga = harga

print(f"Harga tiket yang harus dibayar: Rp {harga:.0f}")


















