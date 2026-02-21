M, A, B = [int(x) for x in input().split()]

seq = [(1, 0), (0, 1)]

for _ in range(M**2 + 5):
    b1 = seq[-1]
    b2 = seq[-2]
    seq.append(((b1[0] * A + b2[0] * B) % M, (b1[1] * A + b2[1] * B) % M))

seq = set(seq)

ng = set()
for p, q in seq:
    # px + qy = M となるx, yの組をansに
    if p == 0 or q == 0:
        if p == 0 and q == 0:
            continue
        if p == 0:
            # y = 0, x任意
            for x in range(M):
                ng.add((x, 0))

        else:
            for y in range(M):
                ng.add((0, y))

    else:
        for y in range(M):
            xp = M - q * y
            if 0 <= xp // p < M and xp % p == 0:
                ng.add((xp // p, y))

print(M**2 - len(ng))
