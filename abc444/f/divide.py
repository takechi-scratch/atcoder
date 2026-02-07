from math import log2, ceil, floor

N = 63
M = 31

A = [N]

while True:
    print(A)
    B = []
    for x in A:
        if x <= 1:
            continue

        B.append(x // 2)
        B.append((x + 1) // 2)

    if len(A) == len(B):
        break

    A = B

base = 1 << ceil(log2(N / M))
print(base)

print(max(base - (base * M - N), base // 2))
