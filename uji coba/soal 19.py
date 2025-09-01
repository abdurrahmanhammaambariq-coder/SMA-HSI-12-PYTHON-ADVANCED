# #  Latihan 19: Piramida Bintang
# #  Buat program yang mencetak piramida (segitiga sama kaki) setinggi N
# Petunjuk: Ini adalah tantangan pertama yang membutuhkan logika spasi. Di setiap baris, kamu perlu
#  mencetak sejumlah spasi, diikuti oleh sejumlah bintang. Coba temukan rumus untuk jumlah spasi dan
#  jumlah bintang untuk setiap baris 
# i
#  . Jumlah spasi biasanya 
# N - 1 - i
#  dan jumlah bintang 
# 2 * i +
#  1

N = 5

for i in range(N):
    spasi = " " * (N - 1 - i)
    bintang = "*" * (2 * i + 1)
    print(spasi+bintang)
    














 