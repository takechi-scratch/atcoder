from collections import deque

H, W = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]

bfs = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if not (0 <= i + di < H and 0 <= j + dj < W):
                    continue
                bfs.append((i + di, j + dj, 1))
            S[i][j] = 0
        else:
            S[i][j] = None

while len(bfs) > 0:
    i, j, turn = bfs.popleft()
    if S[i][j] is not None:
        continue

    near_painted = 0
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if not (0 <= i + di < H and 0 <= j + dj < W):
            continue
        if S[i + di][j + dj] is not None and S[i + di][j + dj] < turn:
            near_painted += 1

    if near_painted == 1:
        S[i][j] = turn
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if not (0 <= i + di < H and 0 <= j + dj < W) or S[i + di][j + dj] is not None:
                continue

            bfs.append((i + di, j + dj, turn + 1))


ans = 0
for i in range(H):
    for j in range(W):
        ans += S[i][j] is not None

print(ans)
