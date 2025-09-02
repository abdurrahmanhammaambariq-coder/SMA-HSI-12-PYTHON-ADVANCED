barang_datang = ["apel", "jeruk", "apel", "pisang", "apel", "jeruk"]

inventaris = {}

for barang in barang_datang:
    inventaris[barang] = inventaris.get(barang, 0) + 1

print(inventaris)
