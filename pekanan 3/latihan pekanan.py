# proyek_pembersih.py

try:
    # Buka file input (transaksi kotor) untuk dibaca
    with open("transaksi_kotor.txt", "r") as file_input:
        
        # Buka file output (laporan bersih) untuk ditulis
        with open("laporan_bersih.txt", "w") as file_output:
            
            # Tulis header laporan
            file_output.write("LAPORAN TRANSAKSI BERSIH\n")
            file_output.write("=========================\n")
            
            # Variabel untuk akumulasi total seluruh transaksi
            grand_total = 0
            
            # Loop baca setiap baris dari file input
            for baris in file_input:
                # Bersihkan baris dari spasi dan newline
                baris = baris.strip()
                
                # Lewati jika baris kosong
                if not baris:
                    continue
                
                # Pecah baris menjadi list dengan delimiter koma
                data_potongan = baris.split(",")
                
                # Bersihkan dan proses setiap bagian data
                id_bersih = data_potongan[0].strip().upper()
                nama_bersih = data_potongan[1].strip().title()
                jumlah_bersih = int(data_potongan[2].strip())
                harga_bersih = float(data_potongan[3].strip())
                
                # Hitung total harga per transaksi
                total_harga = jumlah_bersih * harga_bersih
                
                # Tambahkan ke grand total
                grand_total += total_harga
                
                # Format output untuk ditulis ke file
                string_output = (
                    f"ID: {id_bersih} | Produk: {nama_bersih} | "
                    f"Jumlah: {jumlah_bersih} | Total Harga: Rp {total_harga}"
                )
                
                # Tulis hasil bersih ke file output
                file_output.write(string_output + "\n")
            
            # Footer laporan
            file_output.write(f"\nTotal Keseluruhan: Rp {grand_total}\n")
            file_output.write("--- ANALISIS SELESAI ---\n")

    print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

except FileNotFoundError:
    print("File transaksi_kotor.txt tidak ditemukan. Pastikan file ada di folder yang sama.")
