N, K = [int(x) for x in input().split()]
H = [int(x) for x in input().split()]

dp = [-1] * N
dp[0] = 0

for i in range(1, N):
    before = i - 1
    min_ans = 10 ** 18
    while before >= 0 and i - before <= K:
        min_ans = min(min_ans, dp[before] + abs(H[before] - H[i]))
        before -= 1

    dp[i] = min_ans

print(dp[-1])
