N = 5

for i in range(1, N + 1):
    for j in range (i):
        print(chr(ord('A') + j), end="")
    print()