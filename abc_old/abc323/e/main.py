# DP。それぞれの時間ごとに「その時間からある曲が始まる確率」を出していく

N, X = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]
MOD = 998244353

# テンプレコード「分数のMOD」
def mod_fraction(numerator: int, denominator: int, MOD = 998244353):
    return numerator * pow(denominator, -1, MOD) % MOD

assert mod_fraction(0, 10) == 0

dp = [0 for _ in range(X + 1)]
dp[0] = mod_fraction(1, N)  # 0.5sのときは1/N

for i in range(1, X + 1):
    for j in range(N):
        # 今流れている曲が終わったら、シャッフルを行うのでdpに足す
        # 曲が終わるとするとき「いつから再生が始まっていたか」を求める
        if i - T[j] < 0:
            continue

        dp[i] += mod_fraction(dp[i - T[j]], N)

ans = 0
# 再生中のそれぞれの確率をすべて足す（iがマイナスにならないように気を付ける）
for i in range(X, max(-1, X - T[0]), -1):
    ans += dp[i]
    ans %= MOD

print(ans)

# 22:54 実装開始
# 29:10 つまづく（3重ループ）
# 33分ごろ 実装再開
# 37:35 提出・AC（1発でサンプル通って嬉しい）
