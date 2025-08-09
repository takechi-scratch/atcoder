H, W = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(H)]
P = [int(x) for x in input().split()]

dp = [[10 ** 18 for _ in range(W + 1)] for _ in range(H + 1)]
dp[H - 1][W - 1] = max(P[-1] - A[H - 1][W - 1], 0)
for i in reversed(range(H)):
    for j in reversed(range(W)):
        if i == H - 1 and j == W - 1:
            continue

        next_need = min(dp[i + 1][j], dp[i][j + 1])
        dp[i][j] = max(next_need + P[i + j] - A[i][j], 0)

print(dp[0][0])
