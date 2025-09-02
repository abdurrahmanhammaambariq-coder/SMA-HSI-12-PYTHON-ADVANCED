 # data = "NAMA:BudiSantoso|UMUR:25|KOTA:Jakarta"
# data.split('|')
# for i in data.split(':'):
#     print(data)

data = "NAMA:BudiSantoso|UMUR:25|KOTA:Jakarta"

# Pecah berdasarkan '|'
bagian = data.split('|')

# Loop tiap bagian
for item in bagian:
    label, nilai = item.split(':')  # pisahkan label dan nilai
    print(f"{label}: {nilai}")










