# 解説AC。DPの持つ情報は「最後にどこの飴を食べたか」（N^2）
# ナップサックDPにとらわれて「～番目までに」とすると解けない！！！！

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

dp = [[None for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        # i==jは考慮しなくてよい（バグの原因）
        if i - j <= 0:
            dp[i][j] = -(10**18)
        else:
            dp[i][j] = A[i] + A[j]

max_dp = [[-(10**18) for _ in range(N)] for _ in range(N)]
ans = 0

# 1個前がi番目、2個前がj番目
for i in range(N):
    for j in range(N):
        if dp[i][j] < 0:
            continue

        # max_dp[j][min(j - 1, i - K)]が、1個より前の条件を満たす最大スコア
        dp[i][j] = max(dp[i][j], max_dp[j][min(j - 1, i - K)] + A[i])

        max_dp[i][j] = max(max_dp[i][j], dp[i][j])
        if j - 1 >= 0:
            max_dp[i][j] = max(max_dp[i][j], max_dp[i][j - 1])
        ans = max(ans, dp[i][j])

print(ans)
