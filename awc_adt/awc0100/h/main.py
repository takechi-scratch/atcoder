import sys

sys.setrecursionlimit(10**7)

N, M = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)

for x in sides:
    x.sort(key=lambda i: -B[i])

ans = [0]
visited = [False] * N
visited[0] = True


def dfs(now):
    for next_node in sides[now]:
        if visited[next_node]:
            continue

        ans.append(next_node)
        visited[next_node] = True
        dfs(next_node)
        break


dfs(0)

for i in sorted(range(N), key=lambda i: -B[i]):
    if not visited[i]:
        ans.append(i)
        visited[i] = True
        dfs(i)

print(" ".join([str(x + 1) for x in ans]))
