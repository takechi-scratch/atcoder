N, W = [int(x) for x in input().split()]
things = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[-10 ** 18] * (W + 1) for _ in range(N + 1)]
dp[0] = [0] * (W + 1)

for i in range(1, N + 1):
    for j in range(W + 1):
        max_value = dp[i-1][j]
        if j - things[i - 1][0] >= 0 and dp[i-1][j-things[i - 1][0]] + things[i - 1][1] > max_value:
            max_value = dp[i-1][j-things[i - 1][0]] + things[i - 1][1]
        dp[i][j] = max_value

print(dp[-1][-1])
