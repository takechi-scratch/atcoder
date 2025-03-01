from math import sqrt, ceil
from collections import deque

N, M = [int(x) for x in input().split()]
ans = [[-1] * N for _ in range(N)]
# visited = [[False] * N for _ in range(N)]

twice = {x ** 2 for x in range(ceil(sqrt(M)) + 1)}
available_dxdy = []
for dx in range(ceil(sqrt(M)), -1, -1):
    if M - dx ** 2 in twice:
        available_dxdy.append((dx, int(sqrt(M - dx ** 2))))

bfs = deque([((0, 0), 0)])
# visited[0][0] = True
ans[0][0] = 0

while len(bfs) > 0:
    now, score = bfs.popleft()
    x, y = now

    for abs_dx, abs_dy in available_dxdy:
        for ox, oy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            dx, dy = abs_dx * ox, abs_dy * oy

            if not (0 <= x + dx < N and 0 <= y + dy < N):
                continue
            if ans[x + dx][y + dy] != -1:
                continue

            ans[x + dx][y + dy] = score + 1
            bfs.append(((x + dx, y + dy), score + 1))

print("\n".join([" ".join([str(i) for i in x]) for x in ans]))
