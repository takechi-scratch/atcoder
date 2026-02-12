from collections import defaultdict

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A_sum = [0]
for x in A:
    A_sum.append(A_sum[-1] + x)

A_count = defaultdict(int)
for x in A_sum:
    A_count[x] += 1

ans = 0
for target in A_sum[:-1]:
    A_count[target] -= 1
    ans += A_count[target + K]

print(ans)
