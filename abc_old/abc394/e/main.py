# WA解法（途中）

from collections import deque, defaultdict

N = int(input())
sides = [[] for _ in range(N)]
label = [[] for _ in range(N)]

for i in range(N):
    s = input()
    for j, x in enumerate(s):
        if x != "-":
            sides[i].append(j)
            label[i].append(x)

ans = [[-1] * N for _ in range(N)]
for i in range(N):
    ans[i][i] = 0

bfs = deque([("", i, i) for i in range(N)])
while len(bfs) > 0:
    now_str, now_place, start = bfs.popleft()
    for i, next_place in enumerate(sides[now_place]):
        next_str = now_str + label[now_place][i]
