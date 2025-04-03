K = int(input())

if K % 9 != 0:
    print(0)
    exit()

dp = [-1] * (K + 1)
dp[0] = 1

for i in range(1, K + 1):
    dp[i] = 0
    for j in range(1, min(10, i + 1)):
        dp[i] += dp[i - j]

    dp[i] %= 10 ** 9 + 7

print(dp[-1])
