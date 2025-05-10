N = int(input())
dp = [[0] * 9 for _ in range(N)]
dp[0] = [1] * 9

MOD = 998244353

for i in range(N - 1):
    for j in range(9):
        dp[i][j] %= MOD
        dp[i + 1][j] += dp[i][j] % MOD
        if j + 1 < 9:
            dp[i + 1][j + 1] += dp[i][j] % MOD
        if j - 1 >= 0:
            dp[i + 1][j - 1] += dp[i][j] % MOD

print(sum(dp[-1]) % MOD)
