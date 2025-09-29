from bisect import bisect_left, bisect_right

N, M, X, Y = [int(x) for x in input().split()]

house_X = {}
house_Y = {}

for _ in range(N):
    h_x, h_y = [int(x) for x in input().split()]
    if h_x not in house_X:
        house_X[h_x] = []
    house_X[h_x].append(h_y)

    if h_y not in house_Y:
        house_Y[h_y] = []
    house_Y[h_y].append(h_x)

for value in house_X:
    house_X[value].sort()

for value in house_Y:
    house_Y[value].sort()


reached = set()
Cs = "UDLR"

for _ in range(M):
    d, c = input().split()
    c = int(c)
    dx, dy = ((0, c), (0, -1 * c), (-1 * c, 0), (c, 0))[Cs.index(d)]

    if dy == 0:
        if Y not in house_Y:
            X += dx
            Y += dy
            continue

        now_houses = house_Y[Y]
        left = bisect_left(now_houses, min(X, X + dx))
        right = bisect_right(now_houses, max(X, X + dx))
        for i in range(left, right):
            reached.add((now_houses[i], Y))

    else:
        if X not in house_X:
            X += dx
            Y += dy
            continue

        now_houses = house_X[X]
        left = bisect_left(now_houses, min(Y, Y + dy))
        right = bisect_right(now_houses, max(Y, Y + dy))
        for i in range(left, right):
            reached.add((X, now_houses[i]))

    X += dx
    Y += dy

print(X, Y, len(reached))
