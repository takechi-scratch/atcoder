N = int(input())
P = [float(x) for x in input().split()]

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for now_turn in range(1, N + 1):
    for now_heads in range(now_turn + 1):
        prob = 0
        prob += dp[now_turn - 1][now_heads - 1] * P[now_turn - 1]
        prob += dp[now_turn - 1][now_heads] * (1 - P[now_turn - 1])
        dp[now_turn][now_heads] = prob

print(sum(dp[-1][i] for i in range(N + 1) if i > N // 2))
# print(dp)
