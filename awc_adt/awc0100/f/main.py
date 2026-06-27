from bisect import bisect_left

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A_sum = [0]
for x in A:
    A_sum.append(A_sum[-1] + x)

ans = 0
for start in range(N):
    ans += N - bisect_left(A_sum, A_sum[start] + K) + 1

print(ans)
