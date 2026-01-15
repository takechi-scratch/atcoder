from collections import deque

N, M = [int(x) for x in input().split()]

sides = [[] for _ in range(N * 2)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    sides[a].append(b + N)
    sides[b + N].append(a)


visited = [False] * (N * 2)
ans = [None] * N
for start in range(N):
    if visited[start]:
        continue

    bfs = deque([start])
    visited[start] = True
    visited_real = []
    visited_all = set()

    while len(bfs) > 0:
        now = bfs.popleft()
        visited_real.append(now)
        visited_all.add(now % N)

        for next_node in sides[now]:
            if not visited[next_node]:
                visited[next_node] = True
                bfs.append(next_node)

    for x in visited_real:
        if x >= N:
            continue

        ans[x] = N - len(visited_all)

print("\n".join(str(x) for x in ans))
