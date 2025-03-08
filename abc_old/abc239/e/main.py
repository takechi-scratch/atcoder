# 制約をよく確認すること！K<=20なので、全ての頂点に対して持っておいてOK
# DFSしつつ、SortedListで子のリストを合わせていく（20個より多い部分は捨てる）

from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10**7)

N, Q = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
bests = [SortedList() for _ in range(N)]

for _ in range(N - 1):
    a, b = [int(x) - 1 for x in input().split()]
    sides[a].append(b)
    sides[b].append(a)

visited = [False] * N
def dfs(now):
    visited[now] = True
    best = SortedList()
    for next_node in sides[now]:
        if visited[next_node]:
            continue

        for x in dfs(next_node):
            best.add(x)

    best.add(X[now])
    while len(best) > 20:
        best.pop(0)

    bests[now] = best
    return best

# 忘れずに
dfs(0)

for _ in range(Q):
    V, K = [int(x) for x in input().split()]
    V -= 1
    print(bests[V][0 - K])
