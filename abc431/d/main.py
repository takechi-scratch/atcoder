N = int(input())
parts = [[int(x) for x in input().split()] for _ in range(N)]
W_sum = sum(x[0] for x in parts)

dp = [0 for _ in range(W_sum + 1)]

# jは頭の重さ
for i in range(N):
    next_dp = [0 for _ in range(W_sum + 1)]
    for j in range(W_sum + 1):
        now_ans = dp[j] + parts[i][2]
        if j >= parts[i][0]:
            now_ans = max(now_ans, dp[j - parts[i][0]] + parts[i][1])

        next_dp[j] = now_ans

    dp = next_dp

ans = 0
for head in range(W_sum):
    if head <= W_sum - head and dp[head] > ans:
        ans = dp[head]

print(ans)
