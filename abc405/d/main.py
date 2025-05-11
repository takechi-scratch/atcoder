# 解説通りやるだけ。
# 全ての出口からBFSをすると間に合わない

from collections import deque

H, W = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]

min_score = [[10 ** 12] * W for _ in range(H)]
bfs = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            bfs.append((i, j))
            min_score[i][j] = 0

directions = ((1, 0, "^"), (-1, 0, "v"), (0, 1, "<"), (0, -1, ">"))

while len(bfs) > 0:
    now = bfs.popleft()
    now_score = min_score[now[0]][now[1]]

    for di, dj, mark in directions:
        ni, nj = now[0] + di, now[1] + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue

        if S[ni][nj] in ("E", "#"):
            continue

        if min_score[ni][nj] > now_score + 1:
            S[ni][nj] = mark
            min_score[ni][nj] = now_score + 1
            bfs.append((ni, nj))

print(*["".join(x) for x in S], sep="\n")
