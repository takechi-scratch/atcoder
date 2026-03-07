from collections import defaultdict

import sys

sys.setrecursionlimit(10**7)

N = int(input())
A = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

num_count = defaultdict(int)
path_count = 1
num_set = {A[0]}
num_count[A[0]] += 1
ans = [None] * N


def dfs(now: int):
    global path_count
    if path_count == len(num_set):
        ans[now] = False
    else:
        ans[now] = True

    for next_node in sides[now]:
        if ans[next_node] is not None:
            continue

        if num_count[A[next_node]] == 0:
            num_set.add(A[next_node])
        num_count[A[next_node]] += 1
        path_count += 1
        dfs(next_node)
        path_count -= 1
        num_count[A[next_node]] -= 1
        if num_count[A[next_node]] == 0:
            num_set.remove(A[next_node])


dfs(0)
print(*["Yes" if x else "No" for x in ans], sep="\n")
