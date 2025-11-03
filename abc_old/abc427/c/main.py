import itertools

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

ans = 10**18
for colors in itertools.product(range(2), repeat=N):
    # print(colors)
    now_ans = 0
    for node in range(N):
        for pair_node in sides[node]:
            if colors[node] == colors[pair_node]:
                now_ans += 1

    ans = min(ans, now_ans // 2)

print(ans)
