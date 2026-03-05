N, M, T = [int(x) for x in input().split()]
plants = [[int(x) for x in input().split()] for _ in range(N)]
need_plants = [i for i in range(N) if plants[i][1] < T]
now_ans = sum(x[0] for i, x in enumerate(plants) if i not in need_plants)

dp = [0] * (M + 1)
# dp[0] = 0
for i in need_plants:
    next_dp = dp
    for j in range(M, -1, -1):
        if j + plants[i][2] <= M:
            dp[j + plants[i][2]] = max(dp[j + plants[i][2]], dp[j] + plants[i][0])

    dp = next_dp

print(dp[-1] + now_ans)
