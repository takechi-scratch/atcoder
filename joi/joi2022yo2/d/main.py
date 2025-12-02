# 途中

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

dp = [[[-(10**18)] * 3 for _ in range(K + 1)] for _ in range(N + 1)]
dp[-1] = [[0] * 3 for _ in range(K + 1)]

# i番目までの飴で、直近のj個の中でk個までを食べたときのおいしさの最大値
for i in range(N):
    for j in range(1, K + 1):
        if j == 1:
            dp[i][j][0] = 0
            dp[i][j][1] = A[i]
            continue

        dp[i][j][0] = dp[i - 1][j - 1][0]
        if
            dp[i][j][0] = max(dp[i - 1][j - 1])
        dp[i][j][1] = max(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0] + A[i])
        if j == 2:
            dp[i][j][2] = dp[i - 1][j - 1][1] + A[i]
        else:
            dp[i][j][2] = max(dp[i - 1][j - 1][2], dp[i - 1][j - 1][1] + A[i])

print(max(dp[N - 1][K]))
