# 実装途中

N, TK, AO = [int(x) for x in input().split()]
TK -= 1
AO -= 1

sides = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

dist = [10**18] * N


def dfs(now, before, d):
    ans = 0
    dist[now] = d

    for next_node in sides[now]:
        if next_node == before:
            break
        if next_node == AO:
            ans = -(10**18)
            break

        ans = max(dfs(next_node, now), ans, d + 1)

    return ans + 1


dfs(TK, -1, 0)
