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
# ここから。 参考: https://www.youtube.com/watch?v=wDmi65vgLIA
# 決め打ち二分探索で、最低ビタミンの値を決めてしまう
# 最低ビタミンに必要なカロリーをbisectで求めて合計して、目標カロリーと比較

from bisect import bisect_left

left, right = 0, 10 ** 60
while right - left > 1:
    mid = (left + right) // 2

    if bisect_left(dp[0], mid) + bisect_left(dp[1], mid) + bisect_left(dp[2], mid) <= X:
        left = mid
    else:
        right = mid

print(left)
