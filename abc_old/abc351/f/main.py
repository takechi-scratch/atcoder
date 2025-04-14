from atcoder.fenwicktree import FenwickTree

N = int(input())
A = [int(x) for x in input().split()]

ans = 0
pre_index = [-1] * N
for i, x in enumerate(sorted([(x, i) for i, x in enumerate(A)])):
    pre_index[x[1]] = i

now_sum = 0
register_numbers = FenwickTree(N)
count_numbers = FenwickTree(N)

for i in range(N - 1, 0, -1):
    register_numbers.add(pre_index[i], A[i])
    count_numbers.add(pre_index[i], 1)
    now_sum += A[i]

    ans += register_numbers.sum(pre_index[i - 1], N) - A[i - 1] * count_numbers.sum(pre_index[i - 1], N)

print(ans)
