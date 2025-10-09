from bisect import bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]

B = []
counts = []

for x in A:
    count = 1
    while x % 2 == 0:
        count *= 2
        x //= 2

    B.append(x)
    counts.append(count)

counts_sum = [0]
for x in counts:
    counts_sum.append(counts_sum[-1] + x)

Q = int(input())
for _ in range(Q):
    target = int(input())
    print(B[bisect_left(counts_sum, target) - 1])
