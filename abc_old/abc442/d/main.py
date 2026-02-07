from atcoder.fenwicktree import FenwickTree
N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
ft = FenwickTree(N)
for i, x in enumerate(A):
    ft.add(i, x)

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        x = query[1] - 1
        left = ft.sum(x, x + 1)
        right = ft.sum(x + 1, x + 2)
        ft.add(x, right - left)
        ft.add(x + 1, left - right)

    else:
        l, r = query[1:]
        print(ft.sum(l - 1, r))
