import sys
sys.setrecursionlimit(10**7)

N = int(input())
X = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
costs = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = [int(x) for x in input().split()]
    u -= 1
    v -= 1

    sides[u].append(v)
    sides[v].append(u)

    costs[u].append(w)
    costs[v].append(w)

# スコアと、現在の電荷
def dfs(now: int, before: int) -> tuple[int, int]:
    if len(sides[now]) == 1 and sides[now][0] == before:
        return costs[now][0] * abs(X[now]), X[now]

    score = 0
    denka = X[now]
    return_cost = -1
    for i, next_node in enumerate(sides[now]):
        if next_node == before:
            return_cost = costs[now][i]
            continue

        below_score, below_denka = dfs(next_node, now)
        score += below_score
        denka += below_denka

    if before == -1:
        return_cost = 0

    assert return_cost >= 0
    return score + return_cost * abs(denka), denka

print(dfs(0, -1)[0])
