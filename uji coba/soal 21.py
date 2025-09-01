N = 9

for i in range(N//2+1):
                print(i)
                spasi = " " * (N//2 - i)
                bintang = "a" * (2*i + 1)
                print(spasi + bintang)
        

for i in range(N//2-1,-1,-1):# 1 awal batas mulai dan 1 tengah itu stopnya (batas akhir) dan 1 terakhir itu sebegai langkah
                spasi = " " * (N//2 - i)
                bintang = "a" * (2*i + 1)
                print(spasi + bintang)
        
