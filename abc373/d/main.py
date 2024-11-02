# 後日解答、解説AC。
from collections import deque

N, M = [int(x) for x in input().split()]
ans = [None] * N
cost = [{} for _ in range(N)]

for _ in range(M):
    u, v, w = [int(x) for x in input().split()]
    cost[u - 1][v - 1] = w

for i in range(N):
    if ans[i] is not None or len(cost[i]) == 0:
        continue

    ans[i] = 0

    bfs = deque([])
    bfs.extend([(i, x) for x in cost[i].keys()])

    while len(bfs) > 0:
        u, v = bfs.popleft()
        w = cost[u][v]

        if ans[v] is None:

            ans[v] = ans[u] + w

            bfs.extend([(u, x) for x in cost[u].keys()])

print(" ".join([str(x) for x in ans]))
