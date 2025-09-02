# Dictionary dengan tuple sebagai key
lokasi_item = {} # angka 10 itu adalah sumbu x dan 20 adalah sumbu y
lokasi_item[(10, 20)] = "Peti Harta Karun"
lokasi_item[(5, 8)] = "Pohon Ajaib"
lokasi_item[(3, 15)] = "Sumber Air"

# Input dari pengguna
x = int(input("Masukkan koordinat X: "))
y = int(input("Masukkan koordinat Y: "))

koordinat = (x, y)

# Cek apakah ada item di koordinat tersebut
if koordinat in lokasi_item:
    print(f"Ada {lokasi_item[koordinat]} di sini!")
else:
    print("Tidak ada apa-apa di sini.")
