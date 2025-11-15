from atcoder.fenwicktree import FenwickTree
from sortedcontainers.sortedlist import SortedList

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

SA = SortedList(A)
FA = FenwickTree(500005)
for x in A:
    FA.add(x, x)

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        x, y = query[1] - 1, query[2]
        SA.discard(A[x])
        FA.add(A[x], -A[x])
        A[x] = y
        SA.add(A[x])
        FA.add(y, y)

    else:
        l, r = query[1], query[2]
        if l > r:
            print(l * N)
            continue

        # SortedListで二分探索
        li = SA.bisect_left(l)
        ri = SA.bisect_left(r)
        # FenwickTreeで区間和（Aiの方をもつ）
        print(FA.sum(l, r) + l * li + r * (N - ri))
