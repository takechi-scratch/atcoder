X, Y = [int(x) for x in input().split()]

ok = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= X or abs(i - j) >= Y:
            ok += 1

print(ok / 36)
