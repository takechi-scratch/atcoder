N = int(input())
H = [int(x) for x in input().split()]

dp = [-1] * N
dp[0] = 0
dp[1] = abs(H[1] - H[0])

for i in range(2, N):
    dp[i] = min(dp[i-2] + abs(H[i-2] - H[i]), dp[i-1] + abs(H[i-1] - H[i]))

print(dp[-1])
# print(*dp)
