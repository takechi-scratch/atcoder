# 結局は「後ろから見る」のが強い（BFSにもちこむ）

from collections import deque

N = int(input())
teleporters = []
for _ in range(N - 1):
    a = int(input())
    teleporters.append([[int(x) - 1 for x in input().split()] for _ in range(a)])
teleporters.append([])

sides = [[] for _ in range(N)]
for i, x in enumerate(teleporters):
    for j, y in enumerate(x):
        p, q = y
        sides[p].append((i, j, 0))
        sides[q].append((i, j, 1))

score = [10**18] * N
score[-1] = 0

bfs = deque([(N - 1, 0)])
while len(bfs) > 0:
    now, now_score = bfs.popleft()
    if now_score > score[now]:
        continue

    for next_i, next_j, next_k in sides[now]:
        next_other_score = score[teleporters[next_i][next_j][1 - next_k]]

        if next_other_score == 10**18:
            continue

        next_score = max(next_other_score, now_score) + 1

        if next_score >= score[next_i]:
            continue

        score[next_i] = next_score
        bfs.append((next_i, next_score))

if score[0] == 10**18:
    print(-1)
else:
    print(score[0])
