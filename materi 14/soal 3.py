# soal 3 dari materi 14


kalimat = input("Masukkan sebuah kalimat: ")
kata_kata = kalimat.split()
jumlah_kata = len(kata_kata)
print("Jumlah kata dalam kalimat:", jumlah_kata)
kata_kata.sort()
print("Kata-kata terurut:", kata_kata)
