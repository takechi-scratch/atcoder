from atcoder.dsu import DSU

N = int(input())
sides = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(x) for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

uf = DSU(N)

side_node_available = [[] for _ in range(N)]
for now in range(N - 1, -1, -1):
    for next_node in sides[now]:
        if next_node < now:
            continue

        side_node_available[now].append(uf.size(next_node))
        uf.merge(now, next_node)

ans = 0
for i in range(N):
    side_node_available[i]

print(0)
