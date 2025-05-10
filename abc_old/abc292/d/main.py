# 普通にDFSで。

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

# 連結成分ごとにDFS
for start in range(N):
    if visited[start]:
        continue

    visited[start] = True
    visit_nodes, visit_sides = 0, 0
    dfs = [start]

    while len(dfs) > 0:
        now = dfs.pop()
        visit_nodes += 1

        for next_node in sides[now]:
            visit_sides += 1
            if not visited[next_node]:
                dfs.append(next_node)
                visited[next_node] = True

    # sidesは2方向からカウントしているので2で割る
    if visit_nodes != visit_sides // 2:
        print("No")
        break

else:
    print("Yes")
