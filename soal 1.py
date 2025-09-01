N = 5

for i in range (N):
    print(" " * ( N- 1 - i), end="")

    # huruf naik
    for j in range(i+1):
       print(chr(ord('A') + j), end="")

    # huruf turun
    for j in range(i-1,-1,-1):
       print(chr(ord('A') + j), end="")
    print()

