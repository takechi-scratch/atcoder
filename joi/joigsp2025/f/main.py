# つながるイベントを記録して、UnionFindで良い感じにまとめる

from atcoder.dsu import DSU
from bisect import bisect_left
import sys

input = sys.stdin.readline

H, W, N = [int(x) for x in input().split()]
islands = [[int(x) - 1 for x in input().split()] for _ in range(N)]

W_islands = [[] for _ in range(W)]
for i, x in enumerate(islands):
    W_islands[x[1]].append((x[0], i))

for i in range(W):
    W_islands[i].sort()

W_islands_heights = [[y[0] for y in x] for x in W_islands]

events = []
for i in range(W):
    for j, x in enumerate(W_islands[i]):
        if i > 0:
            touch_idx = bisect_left(W_islands_heights[i - 1], x[0])
            if touch_idx < len(W_islands[i - 1]):
                target_x = W_islands[i - 1][touch_idx]
                events.append((target_x[0] - x[0], x[1], target_x[1]))

        if i < W - 1:
            touch_idx = bisect_left(W_islands_heights[i + 1], x[0])
            if touch_idx < len(W_islands[i + 1]):
                target_x = W_islands[i + 1][touch_idx]
                events.append((target_x[0] - x[0], x[1], target_x[1]))

        if len(W_islands[i]) > j + 1:
            target_x = W_islands[i][j + 1]
            events.append((target_x[0] - x[0] - 1, x[1], target_x[1]))

events.sort()

unionfind = DSU(N)
for event in events:
    unionfind.merge(event[1], event[2])
    if unionfind.size(event[1]) == N:
        print(event[0])
        break

else:
    print(-1)
