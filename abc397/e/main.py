import sys
sys.setrecursionlimit(10 ** 7)
# 忘れずに！！！
import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")


N, K = [int(x) for x in input().split()]
NK = N * K

sides = [[] for _ in range(NK)]
visited = [False] * NK

for _ in range(NK - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

def dfs(now: int, before: int):
    after_pcs = []

    if len(sides[now]) == 1 and sides[now][0] == before:
        return 1

    for next_node in sides[now]:
        if visited[next_node]:
            continue

        visited[next_node] = True
        after_pc = dfs(next_node, now)
        if after_pc % K == 0:
            continue

        after_pcs.append(after_pc)

    if len(after_pcs) >= 3:
        print("No")
        exit()

    if len(after_pcs) == 0:
        return 1

    if len(after_pcs) == 1:
        return (after_pcs[0] + 1) % K

    if (after_pcs[0] + after_pcs[1] + 1) % K != 0:
        print("No")
        exit()

    return 0

visited[0] = True
dfs(0, -1)
assert all(visited)

print("Yes")

# 提出前につけるの忘れず
