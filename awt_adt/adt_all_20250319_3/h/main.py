# https://atcoder.jp/contests/abc334/tasks/abc334_e

H, W = [int(x) for x in input().split()]
grid = []
for _ in range(H):
    grid.append(list(input()))

renketsu_id = 0
for si in range(H):
    for sj in range(W):
        if grid[si][sj] != "#":
            continue

        grid[si][sj] = renketsu_id
        dfs = [(si, sj)]
        while len(dfs) > 0:
            i, j = dfs.pop()

            for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < H and 0 <= nj < W):
                    continue

                if grid[ni][nj] != "#":
                    continue

                grid[ni][nj] = renketsu_id
                dfs.append((ni, nj))

        renketsu_id += 1

ans = 0
MOD = 998244353

bunbo = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] != ".":
            continue

        bunbo += 1
        neighbor = set()
        if 1 <= i:
            neighbor.add(grid[i - 1][j])

        if i < H - 1:
            neighbor.add(grid[i + 1][j])

        if j < W - 1:
            neighbor.add(grid[i][j + 1])

        if 1 <= j:
            neighbor.add(grid[i][j - 1])

        neighbor.discard(".")

        ans += (renketsu_id - len(neighbor) + 1) % MOD


print(ans * pow(bunbo, -1, MOD) % MOD)
