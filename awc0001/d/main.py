N, M, K = [int(x) for x in input().split()]
towns = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[0] * (M + 1) for _ in range(N + 1)]
ans = 0

for now in range(N):
    for j in range(1, M + 1):
        a, b = towns[now]
        for before in range(now - 1, max(-1, now - K) - 1, -1):
            # dp[now][j] = max(dp[now][j], dp[before][j])

            if j >= b:
                dp[now][j] = max(dp[now][j], dp[before][j - b] + a)

print(max(max(a) for a in dp))
