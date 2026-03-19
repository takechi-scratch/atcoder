N, M = [int(x) for x in input().split()]
nearest_costs = [[10**18] * N for _ in range(N)]
for i in range(N):
    nearest_costs[i][i] = 0

for _ in range(M):
    u, v, w = [int(x) for x in input().split()]
    nearest_costs[u - 1][v - 1] = min(nearest_costs[u - 1][v - 1], w)

for k in range(N):
    for i in range(N):
        for j in range(N):
            nearest_costs[i][j] = min(nearest_costs[i][j], nearest_costs[i][k] + nearest_costs[k][j])


S, K = [int(x) for x in input().split()]
S -= 1
T = [int(x) - 1 for x in input().split()]

dp = [[10**18] * K for _ in range(2**K)]

for start_index in range(K):
    dp[1 << start_index][start_index] = nearest_costs[S][T[start_index]]

for status in range(2**K):
    for now_index in range(K):
        if dp[status][now_index] >= 10**18:
            continue

        for next_index in range(K):
            # if (1 << next_index) & status != 0:
            #     continue

            if nearest_costs[T[now_index]][T[next_index]] >= 10**18:
                continue

            dp[status | (1 << next_index)][next_index] = min(
                dp[status | (1 << next_index)][next_index],
                dp[status][now_index] + nearest_costs[T[now_index]][T[next_index]],
            )


ans = min(now_ans + nearest_costs[T[last_index]][S] for last_index, now_ans in enumerate(dp[-1]))
if ans >= 10**18:
    print(-1)
else:
    print(ans)
