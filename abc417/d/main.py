# DP + 累積和 + 二分探索
# 後ろからDPを柔軟にできるようにする。
# メモ化再帰だと遅い（1TLE）

from bisect import bisect_right


N = int(input())
gifts = [tuple(int(x) for x in input().split()) for _ in range(N)]

dp = [[None] * 1001 for _ in range(N + 1)]
dp[-1] = list(range(1001))

for i in range(N - 1, -1, -1):
    for j in range(1001):
        # 「1コ次」を見てから、前を更新するのを繰り返せば
        # 後ろからのDPでもできる。
        if j <= gifts[i][0]:
            if j + gifts[i][1] < 1001:
                dp[i][j] = dp[i + 1][j + gifts[i][1]]
        else:
            dp[i][j] = dp[i + 1][max(j - gifts[i][2], 0)]

down_points_sum = [0]
for x in gifts:
    down_points_sum.append(down_points_sum[-1] + x[2])

Q = int(input())
for _ in range(Q):
    X = int(input())
    if X <= 1000:
        print(dp[0][X])
        continue

    downs = bisect_right(down_points_sum, X - 1000)
    if downs >= len(down_points_sum):
        print(X - down_points_sum[-1])
        continue

    now_point = X - down_points_sum[downs]
    print(dp[downs][now_point])
