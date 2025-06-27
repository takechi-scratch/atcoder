# 「頂点を増やす」方法
# どんな頂点を増やしたら嬉しいかを考えてみよう！！

from collections import deque

N, M = [int(x) for x in input().split()]
sets = []
for i in range(N):
    input()
    s = set(int(x) - 1 for x in input().split())

    if 0 in s and M - 1 in s:
        print(0)
        exit()

    sets.append(s)

sides = [[] for _ in range(M + N)]
for i, now_set in enumerate(sets):
    for x in now_set:
        sides[x].append(M + i)
        sides[M + i].append(x)

score = [-1] * (M + N)
bfs = deque([0])
score[0] = 0
while len(bfs) > 0:
    now = bfs.popleft()
    for next_node in sides[now]:
        if score[next_node] >= 0 and score[next_node] <= score[now] + 1:
            continue

        score[next_node] = score[now] + 1
        bfs.append(next_node)

if score[M - 1] == -1:
    print(-1)
else:
    print(score[M - 1] // 2 - 1)
