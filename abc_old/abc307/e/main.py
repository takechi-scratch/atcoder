# 解説AC。DPを使うとは思わなかった…。
# x人まで+x人目が1人目の色と同じかのDP。
# 問題を見てDPと気づく+DPで持つ要素を決める練習が必要。

N, M = [int(x) for x in input().split()]
MOD = 998244353

dp = [[-1] * 2 for _ in range(N)]
dp[0][0] = M
dp[0][1] = 0

for i in range(1, N):
    dp[i][0] = dp[i - 1][1] * 1 % MOD
    dp[i][1] = dp[i - 1][0] * (M - 1) % MOD + dp[i - 1][1] * (M - 2) % MOD

print(dp[-1][1] % MOD)
# 解説を見てから書くのは簡単
