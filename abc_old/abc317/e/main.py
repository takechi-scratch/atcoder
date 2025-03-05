# 解説AC。見てる方向埋めは3重ループにはならない！
# 二分探索で実装したらTLEしたので、計算量の見積もりを丁寧にするべき

from collections import deque

H, W = [int(x) for x in input().split()]
grid = [[""] * W for _ in range(H)]

ans = [[10 ** 18] * W for _ in range(H)]

for i in range(H):
    for j, x in enumerate(input()):
        if x in [".", "S", "G"]:
            grid[i][j] = "."
            if x == "S":
                start = (i, j)
            elif x == "G":
                goal = (i, j)

        else:
            grid[i][j] = x

Direction = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

for i in range(H):
    for j in range(W):
        if grid[i][j] in (".", "#", "!"):
            continue

        di, dj = Direction[grid[i][j]]
        now_i, now_j = i, j
        while True:
            now_i += di
            now_j += dj
            if not (-1 < now_i < H and -1 < now_j < W and grid[now_i][now_j] in (".", "!")):
                break
            grid[now_i][now_j] = "!"

bfs = deque([(start, 0)])
# ans[start[0]][start[1]] = 0

while len(bfs) > 0:
    pos, score = bfs.popleft()
    now_i, now_j = pos

    if ans[now_i][now_j] <= score:
        continue

    ans[now_i][now_j] = score

    for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        next_i, next_j = now_i + di, now_j + dj
        if not (-1 < next_i < H and -1 < next_j < W and grid[next_i][next_j] == "."):
            continue

        if ans[goal[0]][goal[1]] != 10 ** 18 and not (next_i == goal[0] and next_j == goal[1]):
            continue

        if ans[next_i][next_j] < score + 1:
            continue

        bfs.append(((next_i, next_j), score + 1))

if ans[goal[0]][goal[1]] == 10 ** 18:
    print(-1)
else:
    print(ans[goal[0]][goal[1]])
