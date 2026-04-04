S = input()
T = input()

N = len(S)
M = len(T)

dp = [0] * (M + 1)
ans = 0

for i in range(N):
    dp[0] += 1
    for j in range(M - 1, -1, -1):
        if S[i] == T[j]:
            dp[j + 1] += dp[j]
            dp[j] = 0

    ans += sum(dp) - dp[-1]

print(ans)
