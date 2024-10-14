# DP基礎！次が1倍のモードと次が2倍のモードにわける。
# evimaさんの動画を参考に

N = int(input())
A = [int(x) for x in input().split()]
dp = [[-1, -1] for _ in range(N)]

for i in range(N):
    if i == 0:
        # ここだけコーナーケースとして分けたけど正解？
        dp[i][0] = 0
        dp[i][1] = A[i]
        continue

    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + A[i] * 2)
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] + A[i])
    # print(dp[i])

print(max(dp[-1]))
