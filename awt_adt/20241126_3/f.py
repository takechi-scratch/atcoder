# https://atcoder.jp/contests/abc284/tasks/abc284_c
# BFSやれ！！って感じ

from collections import deque

N, M = [int(x) for x in input().split()]
side = [list() for _ in range(N)]
checked = [False] * N

for _ in range(M):
    u, v = [int(x) for x in input().split()]
    side[u-1].append(v-1)
    side[v-1].append(u-1)

ans = 0
for start in range(N):
    if checked[start] is True:
        continue

    bfs = deque([start])
    ans += 1
    while len(bfs) > 0:
        n = bfs.popleft()
        checked[n] = True

        for to in side[n]:
            # WAポイント！bfsの中の項目が重複していないか要チェック。
            # （実際にはTLEが起こる）
            if checked[to] is False and to not in bfs:
                bfs.append(to)

print(ans)
