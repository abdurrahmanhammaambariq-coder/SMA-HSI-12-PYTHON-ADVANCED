# Definisi class Resep
class Resep:
    def __init__(self, nama_resep):
        self.nama_resep = nama_resep
        self.daftar_bahan = []

    def tambah_bahan(self, bahan):
        self.daftar_bahan.append(bahan)

    def cetak_resep(self):
        print(f"Resep: {self.nama_resep}")
        print("Bahan-bahan:")
        for b in self.daftar_bahan:
            print(f"- {b}")

# Membuat object resep_nasi_goreng
resep_nasi_goreng = Resep("Nasi Goreng")

# Menambahkan bahan-bahan
resep_nasi_goreng.tambah_bahan("Nasi")
resep_nasi_goreng.tambah_bahan("Telur")
resep_nasi_goreng.tambah_bahan("Kecap")
resep_nasi_goreng.tambah_bahan("Bawang Merah")
resep_nasi_goreng.tambah_bahan("Bawang Putih")

# Mencetak resep lengkap
resep_nasi_goreng.cetak_resep()
