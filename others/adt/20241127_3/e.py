# https://atcoder.jp/contests/abc317/tasks/abc317_c
# DFSで実装。時間はギリギリセーフ。BitDPでやった人を見つけたけど、オーバーキルかな

from collections import deque

N, M = [int(i) for i in input().split()]
sides = [[] for _ in range(N)]
points = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = [int(i) for i in input().split()]
    a -= 1
    b -= 1
    sides[a].append(b)
    sides[b].append(a)
    points[a].append(c)
    points[b].append(c)

ans = 0

for start in range(N):
    max_length = 0
    dfs = deque()
    dfs.append((start, set([start]), 0))

    while len(dfs) > 0:
        now, visited_towns, score = dfs.pop()
        max_length = max(score, max_length)

        for i, to in enumerate(sides[now]):
            if to not in visited_towns:
                dfs.append((to, visited_towns | {to}, score + points[now][i]))

    ans = max(ans, max_length)

print(ans)
