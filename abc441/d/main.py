import sys

sys.setrecursionlimit(10**7)

N, M, L, S, T = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
costs = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = [int(x) for x in input().split()]
    sides[u - 1].append(v - 1)
    costs[u - 1].append(c)

ok = set()

def dfs(now: int, now_cost: int, count: int):
    if count == L:
        if S <= now_cost <= T:
            ok.add(now)
        return

    for next_node, next_cost in zip(sides[now], costs[now]):
        if now_cost + next_cost > T:
            continue

        dfs(next_node, now_cost + next_cost, count + 1)

dfs(0, 0, 0)

print(" ".join([str(x + 1) for x in sorted(ok)]))
