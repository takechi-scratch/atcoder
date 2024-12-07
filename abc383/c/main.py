H, W, D = [int(x) for x in input().split()]
floor = []

for _ in range(H):
    floor.append(list(input()))

dfs = []
ans = 0

for i in range(H):
    for j in range(W):
        if floor[i][j] == "H":
            dfs.append((i, j, 0))
            ans += 1
            floor[i][j] = "O"

while len(dfs) > 0:
    i, j, n = dfs.pop()

    if n >= D:
        continue

    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if not (0 <= i + di < H and 0 <= j + dj < W):
            continue

        if floor[i + di][j + dj] == ".":
            if n + 1 < D:
                dfs.append((i + di, j + dj, n + 1))
            ans += 1
            floor[i + di][j + dj] = "O"

print(ans)
