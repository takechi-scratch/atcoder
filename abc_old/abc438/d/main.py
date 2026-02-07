N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

dp = [A[0], -(10**18), -(10**18)]
for i in range(1, N):
    next_dp = [-(10**18), -(10**18), -(10**18)]
    next_dp[0] = dp[0] + A[i]
    next_dp[1] = max(dp[0], dp[1]) + B[i]
    next_dp[2] = max(dp[1], dp[2]) + C[i]

    dp = next_dp

print(dp[2])
