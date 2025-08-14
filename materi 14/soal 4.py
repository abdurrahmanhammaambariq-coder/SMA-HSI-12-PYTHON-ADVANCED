# soal 4 dari materi 14

# a = [1, 20, 3, 4, 5]
# b = [1, 20, 3, 4, 5]
# c = [1, 30, 3, 4, 5]

# Penjelasan:
# a = [1, 2, 3, 4, 5]
# → list a dibuat.
# b = a
# → b bukan salinan baru, tapi referensi ke list a. Jadi a dan b menunjuk ke list yang sama di memori.
# c = a.copy()
# → c adalah salinan baru dari list a pada saat itu. Isinya sama, tapi tersimpan di alamat memori berbeda.
# b[1] = 20
# → Mengubah elemen indeks ke-1 pada b. Karena b dan a adalah list yang sama, maka a juga ikut berubah.
# c[1] = 30
# → Mengubah elemen indeks ke-1 pada c. Perubahan ini tidak memengaruhi a atau b karena c adalah salinan terpisah.
# print
# a berubah menjadi [1, 20, 3, 4, 5] (terpengaruh oleh b).
# b sama dengan a karena referensi sama.
# c hanya berubah di indeks ke-1 menjadi 30.