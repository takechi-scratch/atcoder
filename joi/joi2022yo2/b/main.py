from collections import deque

H, W = [int(x) for x in input().split()]
grid = [list(input()) for _ in range(H)]

score = [[10**18] * W for _ in range(H)]
score[0][0] = 0

bfs = deque([(0, 0)])
while len(bfs) > 0:
    i, j = bfs.popleft()
    for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        if not (0 <= i + di < H and 0 <= j + dj < W):
            continue
        if grid[i][j] == grid[i + di][j + dj]:
            continue

        if score[i + di][j + dj] > score[i][j] + 1:
            score[i + di][j + dj] = score[i][j] + 1
            bfs.append((i + di, j + dj))

if score[-1][-1] == 10**18:
    print(-1)
else:
    print(int(score[-1][-1]))
