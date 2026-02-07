from bisect import bisect_left

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
MOD = 998244353

A.sort()
B.sort()

B_sum = [0]
for x in B:
    B_sum.append((B_sum[-1] + x) % MOD)

ans = 0
for x in A:
    below_count = bisect_left(B, x)
    ans += x * below_count - B_sum[below_count]
    ans %= MOD
    ans += B_sum[-1] - B_sum[below_count] - x * (M - below_count)
    ans %= MOD

print(ans % MOD)
