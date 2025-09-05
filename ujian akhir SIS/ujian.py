# --- Fungsi Load Data dari File ---
def load_data(filename):
    data = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                nis = parts[0]
                nama = parts[1]
                nilai = [int(n) for n in parts[2].split(";")] if len(parts) > 2 and parts[2] else []
                data[nis] = {"nama": nama, "nilai": nilai}
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan, buat baru...")
    return data


# --- Fungsi Simpan Data ke File ---
def simpan_data(data, filename):
    with open(filename, "w") as f:
        for nis, info in data.items():
            nilai_str = ";".join(str(n) for n in info["nilai"])
            f.write(f"{nis},{info['nama']},{nilai_str}\n")


# --- Fungsi 1: Lihat Daftar Siswa ---
def lihat_daftar_siswa(filename):
    data = load_data(filename)
    print("\n--- Daftar Siswa ---")
    if not data:
        print("Sorry belum ada data.")
    else:
        for nis, info in data.items():
            print(f"{nis} - {info['nama']}")
    print("--------------------\n")


# --- Fungsi 2: Lihat Detail Siswa ---
def lihat_detail_siswa(filename):
    data = load_data(filename)
    nis = input("Nomer induk kau: ").strip()
    if nis in data:
        info = data[nis]
        nilai = info['nilai']

        print("\n--- Detail Siswa ---")
        print(f"NIS   : {nis}")
        print(f"Nama  : {info['nama']}")
        print(f"Nilai : {nilai if nilai else 'Nilai belum masuk'}")

        if nilai:
            rata2 = sum(nilai) / len(nilai)
            maks = max(nilai)
            min_ = min(nilai)

            if rata2 >= 85:
                grade = "A"
            elif rata2 >= 70:
                grade = "B"
            elif rata2 >= 55:
                grade = "C"
            else:
                grade = "D"

            print(f"Rata-rata : {rata2:.2f}")
            print(f"Tertinggi : {maks}")
            print(f"Terendah  : {min_}")
            print(f"Grade     : {grade}")
        print("--------------------\n")
    else:
        print("Siswa tidak ditemukan.\n")


# --- Fungsi 3: Tambah Siswa Baru ---
def tambah_siswa_baru(filename):
    data = load_data(filename)
    nis = input("Nomer induk baru saje: ").strip()
    if nis in data:
        print("NIS sudah ada!\n")
        return
    nama = input("Masukkan nama lengkap: ").strip()
    data[nis] = {"nama": nama, "nilai": []}
    simpan_data(data, filename)
    print(f"Siswa {nama} berhasil ditambahkan!\n")


# --- Fungsi 4: Tambah Nilai Siswa ---
def tambah_nilai_siswa(filename):
    data = load_data(filename)
    nis = input("Masukkan NIS siswa: ").strip()
    if nis not in data:
        print("Siswa tidak ditemukan!\n")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru: "))
        if 0 <= nilai_baru <= 100:
            data[nis]["nilai"].append(nilai_baru)
            simpan_data(data, filename)
            print("Nilai berhasil ditambahkan!\n")
        else:
            print("Nilai harus 0-100\n")
    except ValueError:
        print("Input nilai harus berupa angka!\n")


# --- Fungsi 5: Simpan & Keluar ---
def simpan_dan_keluar():
    print("Keluar program...\n")
    exit()


# ========== PROGRAM UTAMA ==========
filename = "database_siswa.txt"

while True:
    print("----- Sistem Informasi Siswa -----")
    print("1. Lihat Daftar Siswa")
    print("2. Lihat Detail Siswa")
    print("3. Tambah Siswa Baru")
    print("4. Tambah Nilai Siswa")
    print("5. Simpan & Keluar")
    print("----------------------------------")

    pilihan = input("Pilih menu (1-5): ").strip()

    if pilihan == "1":
        lihat_daftar_siswa(filename)
    elif pilihan == "2":
        lihat_detail_siswa(filename)
    elif pilihan == "3":
        tambah_siswa_baru(filename)
    elif pilihan == "4":
        tambah_nilai_siswa(filename)
    elif pilihan == "5":
        simpan_dan_keluar()
    else:
        print("Pilihan tidak valid!\n")











































