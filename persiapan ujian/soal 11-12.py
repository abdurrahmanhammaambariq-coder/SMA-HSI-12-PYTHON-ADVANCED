# Buka file log.txt untuk dibaca
with open("log.txt", "r") as file_log:
    baris_log = file_log.readlines()  # baca semua baris

# Buat file baru untuk menyimpan error
with open("error_log.txt", "w") as file_error:
    for baris in baris_log:
        if "ERROR" in baris:       # cek apakah ada kata ERROR
            file_error.write(baris)  # tulis ke error_log.txt

print("Log error telah disaring ke error_log.txt")


with open("log.txt", "r") as f:
    isi = f.read()
print(isi)




























