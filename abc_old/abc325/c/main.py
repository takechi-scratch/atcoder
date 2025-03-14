H, W = [int(x) for x in input().split()]
grid = [list(input()) for _ in range(H)]

ans = 0
for si in range(H):
    for sj in range(W):
        if grid[si][sj] == ".":
            continue

        ans += 1
        dfs = [(si, sj)]
        grid[si][sj] = "."

        while len(dfs) > 0:
            i, j = dfs.pop()

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if not (0 <= i + di < H and 0 <= j + dj < W):
                        continue

                    if grid[i + di][j + dj] == ".":
                        continue

                    grid[i + di][j + dj] = "."
                    dfs.append((i + di, j + dj))

print(ans)
