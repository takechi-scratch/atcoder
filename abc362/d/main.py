# TLE解法。ダイクストラ法を学んでからまた来ます。

from collections import deque

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
sides = {}
costs = {}
for _ in range(M):
    u, v, b = [int(x) for x in input().split()]
    if u - 1 not in sides:
        sides[u - 1] = []
        costs[u - 1] = []
    sides[u - 1].append(v - 1)
    costs[u - 1].append(b)

    if v - 1 not in sides:
        sides[v - 1] = []
        costs[v - 1] = []
    sides[v - 1].append(u - 1)
    costs[v - 1].append(b)

all_ans = []
for goal in range(1, N):
    ans = 10 ** 18
    bfs = deque([(0, {0}, A[0])])
    while len(bfs) > 0:
        now, been, cost = bfs.popleft()
        for i in range(len(sides[now])):
            to = sides[now][i]
            if to in been:
                continue

            if to == goal:
                ans = min(ans, cost + costs[now][i] + A[to])
                continue

            bfs.append((to, been | {to}, cost + costs[now][i] + A[to]))

    all_ans.append(ans)

print(*all_ans)
