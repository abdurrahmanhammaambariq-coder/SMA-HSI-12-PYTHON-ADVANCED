N = 5

for i in range(N, 0, -1):
    print(" " * ( N - i), end="")

    # huruf naik
    for j in range(i):
       print(chr(ord('A') + j), end="")

    # huruf turun
    for j in range(i-2,-1,-1):
       print(chr(ord('A') + j), end="")
    print()

