def solve(N: int, sides: list[list[int]]):
    cache: list[list[int]] = [[-1] * len(x) for x in sides]

    def dfs(now: int, before: int):
        if len(sides[now]) <= 2:
            if before == -1:
                return 1
            else:
                return 0

        max_ans = 0
        can_use_nodes = 0
        for i, next_node in enumerate(sides[now]):
            if next_node == before:
                continue

            can_use_nodes += 1
            if cache[now][i] >= 0:
                now_ans = cache[now][i]
            else:
                now_ans = dfs(next_node, now)
                cache[now][i] = now_ans

            max_ans = max(now_ans, max_ans)

        if can_use_nodes >= 3:
            return max_ans + 1
        else:
            return 1

    return max(dfs(i, -1) for i in range(N))


Q = int(input())

for _ in range(Q):
    N = int(input())
    sides = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = [int(x) - 1 for x in input().split()]
        sides[u].append(v)
        sides[v].append(u)
    print(solve(N, sides))
