# 後日解答、解説AC。
from collections import deque

N, M = [int(x) for x in input().split()]
ans = [None] * N
visited = [False] * N
cost = [{} for _ in range(N)]

for _ in range(M):
    u, v, w = [int(x) for x in input().split()]
    # 逆のコストも付けておく
    cost[u - 1][v - 1] = w
    cost[v - 1][u - 1] = -1 * w

# 各辺からBFSでゴー
for i in range(N):
    if ans[i] is not None:
        continue

    ans[i] = 0
    # キューの中で無限ループにならないように、visitedのフラグを用意しておくこと
    visited[i] = True

    if len(cost[i]) == 0:
        continue

    bfs = deque([])
    bfs.extend([(i, x) for x in cost[i].keys()])
    for j in cost[i].keys():
        visited[j] = True

    while len(bfs) > 0:
        u, v = bfs.popleft()
        w = cost[u][v]

        ans[v] = ans[u] + w

        for j in cost[v].keys():
            # WAポイント！添え字に注意。uなのかvなのかjなのかはっきりして！
            # nextとかの分かりやすい名前の方がいいのかも
            if not visited[j]:
                bfs.append((v, j))
                visited[j] = True

print(" ".join([str(x) for x in ans]))
