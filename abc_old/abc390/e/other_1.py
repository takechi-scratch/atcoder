# 途中まで同じ
N, X = [int(x) for x in input().split()]
food = []
for _ in range(N):
    food.append([int(x) for x in input().split()])

dp = [[0] * (X + 1) for _ in range(3)]

for i in range(N):
    v, a, c = food[i]
    v -= 1
    next_dp = [0] * (X + 1)
    for j in range(X + 1):
        next_dp[j] = dp[v][j]
        if j - c >= 0:
            next_dp[j] = max(next_dp[j], dp[v][j - c] + a)

        if j >= 1:
            next_dp[j] = max(next_dp[j], next_dp[j - 1])

    dp[v] = next_dp

# -----------------------------------------------------
# ここから。
# X <= 5000 なので、ビタミン1とビタミン2に割くカロリーを決めても間に合う
# 自宅PCの環境で約6秒、PyPyなら間に合うっぽい？

ans = 0
for v1 in range(X):
    for v2 in range(X - v1):
        ans = max(ans, min(dp[0][v1], dp[1][v2], dp[2][X - v1 - v2]))

print(ans)
