# 2個ずつ取っておく
# 間がすべて偶数になるようにする

from sortedcontainers import SortedList

N = int(input())
A = [int(x) for x in input().split()]

A1 = [A[i] for i in range(2 * N + 2) if i % 2 == 0]
A2 = [A[i] for i in range(2 * N + 2) if i % 2 == 1]

A2_SL = SortedList(A2)

ans = -10 ** 18
for i, x in enumerate(A1):
    ans = max(ans, x + A2_SL[-1])
    A2_SL.discard(A2[i])

print(ans)
