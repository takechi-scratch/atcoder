N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
sides_id = [[] for _ in range(N)]
for i in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides_id[u].append(i)
    sides[v].append(u)
    sides_id[v].append(i)

ans = M
for stop_id in range(M):
    visited = [False] * N
    visited[0] = True

    dfs = [0]
    while len(dfs) > 0:
        now = dfs.pop()
        for i, next_node in enumerate(sides[now]):
            if visited[next_node]:
                continue

            if sides_id[now][i] == stop_id:
                continue

            visited[next_node] = True
            dfs.append(next_node)

    if all(visited):
        ans -= 1

print(ans)
