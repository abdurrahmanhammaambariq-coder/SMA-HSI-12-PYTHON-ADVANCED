tugas = []

while True:
    aksi = input("Apa yang ingin Anda lakukan? (tambah, hapus, lihat, keluar): ")

    if aksi == "tambah":
        item = input("Masukkan tugas baru: ")
        tugas.append(item)
        print(f'"{item}" telah ditambahkan ke daftar tugas.')

    elif aksi == "lihat":
        if tugas:
            print("Daftar tugas:")
            for i, t in enumerate(tugas, start=1):
                print(f"{i}. {t}")
        else:
            print("Daftar tugas kosong.")

    elif aksi == "hapus":
        if tugas:
            for i, t in enumerate(tugas, start=1):
                print(f"{i}. {t}")
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor <= len(tugas):
                item = tugas.pop(nomor - 1)
                print(f'"{item}" telah dihapus dari daftar tugas.')
            else:
                print("Nomor tidak valid.")
        else:
            print("Daftar tugas kosong.")

    elif aksi == "keluar":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

'''1 Buat list kosong
tugas = []

List tugas ini akan menyimpan semua item yang ditambahkan pengguna.

Contoh: jika pengguna menambahkan "Belajar Python", maka list akan menjadi ["Belajar Python"].

2 Gunakan loop utama (while True)
while True:
    ...

Loop ini akan menjalankan menu terus-menerus sampai pengguna memilih keluar.

while True → artinya loop tak terbatas sampai ada break.

3 Minta input dari pengguna

aksi = input("Apa yang ingin Anda lakukan? (tambah, hapus, lihat, keluar): ")

aksi menyimpan pilihan pengguna.

Nilai bisa "tambah", "hapus", "lihat", atau "keluar".

4 Gunakan percabangan (if-elif-else) untuk menentukan aksi
a. Tambah
if aksi == "tambah":
    item = input("Masukkan tugas baru: ")
    tugas.append(item)
    print(f'"{item}" telah ditambahkan ke daftar tugas.')

Meminta input tugas baru → simpan di variabel item. .append() menambahkan item ke list tugas.

b. Lihat
elif aksi == "lihat":
    if tugas:  # cek list tidak kosong
        print("Daftar tugas:")
        for i, t in enumerate(tugas, start=1):
            print(f"{i}. {t}")
    else:
        print("Daftar tugas kosong.")

Gunakan enumerate supaya bisa menampilkan nomor urut. Cek dulu apakah list kosong, supaya tidak mencetak kosong saja.

c. Hapus
elif aksi == "hapus":
    if tugas:  # cek list tidak kosong
        for i, t in enumerate(tugas, start=1):
            print(f"{i}. {t}")
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(tugas):
            item = tugas.pop(nomor - 1)
            print(f'"{item}" telah dihapus dari daftar tugas.')
        else:
            print("Nomor tidak valid.")
    else:
        print("Daftar tugas kosong.")

Tampilkan dulu semua tugas → pengguna pilih nomor. .pop(index) menghapus item berdasarkan indeks.

Ingat: indeks list mulai dari 0, tapi nomor yang kita tampilkan mulai dari 1, jadi kita kurangi 1 saat memanggil .pop().

d. Keluar
elif aksi == "keluar":
    print("Terima kasih! Program selesai.")
    break

break menghentikan loop, sehingga program selesai.

e. Input salah
else:
    print("Pilihan tidak valid. Silakan coba lagi.")

Memberi feedback jika pengguna mengetik sesuatu selain 4 opsi di atas.'''
























