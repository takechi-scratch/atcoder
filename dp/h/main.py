H, W = [int(x) for x in input().split()]
grid = [list(input()) for _ in range(H)]
dp = [[0] * W for _ in range(H)]

MOD = 10**9 + 7

dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        if grid[i][j] == "#":
            continue

        ans = 0
        if i > 0:
            ans += dp[i - 1][j]
        if j > 0:
            ans += dp[i][j - 1]

        dp[i][j] = ans % MOD

print(dp[-1][-1])
