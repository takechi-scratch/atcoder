from bisect import bisect_left

N, K, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A_sum = [0]
for x in A:
    A_sum.append(A_sum[-1] + x)

ans = 0
for i in range(N):
    ans += max(0, N - max(bisect_left(A_sum, A_sum[i] + M) - 1, i + K - 1))

print(ans)
