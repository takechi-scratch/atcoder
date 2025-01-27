# 解説AC。カウンターを持つ2次元DPと考える！
# 日付の1次元だけでは解けない。

N, M = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
bonus = {}
for _ in range(M):
    c, y = [int(x) for x in input().split()]
    if c not in bonus:
        bonus[c] = 0
    bonus[c] += y

dp = [[-1] * (N + 1) for _ in range(N)]
dp[0][0] = 0
dp[0][1] = X[0]
if 1 in bonus:
    dp[0][1] += bonus[1]

for i in range(1, N):
    # 0のときはこれまでのmax、1以上の時は必ず表
    dp[i][0] = max(dp[i - 1])
    for j in range(1, N + 1):
        # WAポイント！到達不可能な場所は迷わずcontinue
        # デバッガでおかしい位置が変わっていないか確認したほうがいいかも
        if dp[i - 1][j - 1] < 0:
            continue

        dp[i][j] = dp[i - 1][j - 1] + X[i]
        if j in bonus:
            dp[i][j] += bonus[j]

print(max(dp[-1]))
