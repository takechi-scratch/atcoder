from atcoder.fenwicktree import FenwickTree

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A_sum = [A[0]]
for x in A[1:]:
    A_sum.append((A_sum[-1] + x) % M)

A_sum_sum = [A_sum[0]]
for x in A_sum[1:]:
    A_sum_sum.append(A_sum_sum[-1] + x)

pair = [(x, i) for i, x in enumerate(A_sum)]
bit = FenwickTree(N)

over_count = 0
for i in range(N):
    bit.add(pair[i][1], 1)
    over_count += i - bit.sum(0, pair[i][1])

ans = 0
for i in range(N):
    ans += A_sum_sum[-1] - A_sum_sum[i]

ans -= over_count * M
print(ans)
