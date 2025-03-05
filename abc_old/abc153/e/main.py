# 範囲をみてDPっぽい感じ
# DPテーブルは1重、各更新処理にO(N)かかって計算は2重

H, N = [int(x) for x in input().split()]
A, B = [], []
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    A.append(a)
    B.append(b)
INF = 10 ** 18

dp = [INF] * (H + 1)
dp[0] = 0

for i in range(1, H + 1):
    for j in range(N):
        before = max(i - A[j], 0)
        dp[i] = min(dp[before] + B[j], dp[i])

assert dp[H] < INF
print(dp[H])

# 6分で書けて嬉しい
