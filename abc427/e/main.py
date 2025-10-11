# WA解法。原因不明の4WA。なぜ？？？？

from collections import deque

N, M = [int(x) for x in input().split()]
raw_grid = [list(input()) for _ in range(N)]

grid = [["."] * (3 * M) for _ in range(3 * N)]
for i in range(N):
    for j in range(M):
        grid[N + i][M + j] = raw_grid[i][j]

for i in range(N):
    for j in range(M):
        if raw_grid[i][j] == "T":
            tdi, tdj = i, j

for ti in range(3 * N):
    for tj in range(3 * M):
        if grid[ti][tj] == "#":
            continue

        ok = True
        for i in range(ti - tdi, ti - tdi + N):
            for j in range(tj - tdj, tj - tdj + M):
                if not (0 <= i < 3 * N and 0 <= j < 3 * M):
                    continue
                if grid[i][j] == "#":
                    ok = False
                    break

            if not ok:
                break

        if ok:
            if grid[ti][tj] == "T":
                print(0)
                exit()

            grid[ti][tj] = "G"

dists = [[10**18] * (3 * M) for _ in range(3 * N)]
dists[tdi + N][tdj + M] = 0
bfs = deque([(tdi + N, tdj + M)])
ans = 10**18

while len(bfs) > 0:
    i, j = bfs.popleft()
    now_dist = dists[i][j]

    if grid[i][j] == "G":
        ans = min(ans, dists[i][j])

    for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if not (0 <= ni < 3 * N and 0 <= nj < 3 * M) or grid[ni][nj] == "#":
            continue

        if dists[ni][nj] > now_dist + 1:
            dists[ni][nj] = now_dist + 1
            bfs.append((ni, nj))

if ans == 10**18:
    print(-1)
else:
    print(ans)
