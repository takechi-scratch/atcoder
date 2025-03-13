N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

dp = [[(0, 0)] * 2 for _ in range(N + 1)]

for stones in range(1, N + 1):
    for turn in range(2):
        for choose in range(K):
            if stones - A[choose] < 0:
                continue

            next_stones = stones - A[choose]
            if turn == 0:
                dp[stones][turn] = max(dp[stones][turn], (dp[next_stones][1][0] + A[choose], dp[next_stones][1][1]), key=lambda x: x[0])
            else:
                dp[stones][turn] = max(dp[stones][turn], (dp[next_stones][0][0], dp[next_stones][0][1] + A[choose]), key=lambda x: x[1])

ans = -1
for i in range(K):
    ans = max(ans, dp[-1][0][0])

print(ans)
