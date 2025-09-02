angka_rahasia = 42
maks_percobaan = 5

for i in range(maks_percobaan):
    angka = int(input("tebak hayo angkanya: "))
    if angka == angka_rahasia:
        print("congrats")
        break
    elif angka > angka_rahasia:
        print("ketinggian")
    else:
        print("kependekan")
else:
    ("kalah lu")