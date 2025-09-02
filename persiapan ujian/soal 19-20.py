import re

logs = [
    "ERROR2025-08-04Gagal koneksi ke database.",
    "INFO2025-08-04User 'budi' berhasil login.",
    "WARNING2025-08-05Disk hampir penuh."
]

pola = r"(ERROR|INFO|WARNING)(\d{4}-\d{2}-\d{2})(.*)"

for log in logs:
    match = re.search(pola, log)
    if match:
        level = match.group(1)
        tanggal = match.group(2)
        pesan = match.group(3)
        print(f"Level  : {level}")
        print(f"Tanggal: {tanggal}")
        print(f"Pesan  : {pesan}")
        print("-" * 40)


