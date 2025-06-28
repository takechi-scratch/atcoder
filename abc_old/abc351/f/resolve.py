from atcoder.fenwicktree import FenwickTree

N = int(input())
A = [int(x) for x in input().split()]

sums = FenwickTree(N)
counts = FenwickTree(N)

ans = 0
queue = [(x, i) for i, x in enumerate(A)]
queue.sort()

for x, i in queue:
    ans += x * counts.sum(0, i) - sums.sum(0, i)

    sums.add(i, x)
    counts.add(i, 1)

print(ans)
