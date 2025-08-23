def format_rupiah(angka):
    return f"Rp {angka:,.2f}".replace(",", ".").replace(",", ".", 1)


def get_numeric_input(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < 0:
                print("Nilai tidak boleh negatif")
                continue
            return nilai
        except ValueError:
            print("Masukkan angka yang valid!")

# fungsi utama
            
def tampilkan_header():
    print("="*44)
    print("       SELAMAT DATANG DI SERBAMAHAL")
    print("="*44)
    print("--- Masukkan Detail Barang ---")
    print("(Ketik 'selesai' di nama barang untuk selesai)")

def hitung_subtotal(daftar_harga, daftar_jumlah):
    total = 0
    for i in range(len(daftar_harga)):
        total += daftar_harga[i] * daftar_jumlah[i]
    return total

def hitung_diskon(subtotal):
    if subtotal >= 500000:
        persen = 10
    elif subtotal >= 30000:
         persen = 5
    jumlah_diskon = subtotal * persen /100
    return jumlah_diskon, persen

def tampilkan_struk(semua_nama, semua_harga, semua_jumlah, subtotal, total_diskon, persen_dsikon):
    print("="*44)
    print("         STRUK PEMBELIAN ANDA")
    print("="*44)
    print("Detail Belanja:")  
    for i in range(len(semua_nama)):
        total_item = semua_harga[i] * semua_jumlah[i]
        print(f"{i+1}. {semua_nama[i]:15} ({semua_jumlah[i]} x {format_rupiah(semua_harga[i])}) = {format_rupiah(total_item)}")
    print("-"*44)
    print(f"Subtotal            : {format_rupiah(subtotal)}")
    print(f"Diskon ({persen_diskon}%)       : - {format_rupiah(total_diskon)}")
    print("-"*44)
    print(f"Total yang harus dibayar: {format_rupiah(subtotal - total_diskon)}")
    print("="*44)
    print("     TERIMA KASIH TELAH BERBELANJA!")
    print("="*44)


daftar_nama_barang = []
daftar_harga_barang = []
daftar_jumlah_barang = []

tampilkan_header()

while True:
    nama_barang = input("Nama Barang: ")
    if nama_barang.lower() == "selesai":
        break

    harga = get_numeric_input("Harga Satuan: Rp ")
    jumlah = get_numeric_input("Jumlah: ")

    daftar_nama_barang.append(nama_barang)
    daftar_harga_barang.append(harga)
    daftar_jumlah_barang.append(jumlah)

    print("--- Barang berhasil ditambahkan! ---")

print("Menghitung total belanja Anda...")

# Hitung total & diskon
subtotal = hitung_subtotal(daftar_harga_barang, daftar_jumlah_barang)
total_diskon, persen_diskon = hitung_diskon(subtotal)

# Tampilkan struk
tampilkan_struk(
    daftar_nama_barang,
    daftar_harga_barang,
    daftar_jumlah_barang,
    subtotal,
    total_diskon,
    persen_diskon
)    
    
        
