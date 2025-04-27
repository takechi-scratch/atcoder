from atcoder.fenwicktree import FenwickTree

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

# 累積和であらかじめMODをとっておけば、引く分は1回か0回かで済む！

A_sum = [0]
for x in A:
    A_sum.append((A_sum[-1] + x) % M)

A_sum_sum = [A_sum[0]]
for x in A_sum[1:]:
    A_sum_sum.append(A_sum_sum[-1] + x)

pair = list(sorted((x, i) for i, x in enumerate(A_sum)))
bit = FenwickTree(N + 1)

over_count = 0
for i in range(N + 1):
    bit.add(pair[i][1], 1)
    over_count += i - bit.sum(0, pair[i][1])

ans = 0
for i in range(N):
    ans += A_sum_sum[-1] - A_sum_sum[i] - A_sum[i] * (N - i)

ans += over_count * M
print(ans)
