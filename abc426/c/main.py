from atcoder.segtree import SegTree

N, Q = [int(x) for x in input().split()]

seg = SegTree(lambda a, b: a + b, 0, [1] * N)
updated = -1

for _ in range(Q):
    x, y = [int(x) for x in input().split()]
    update_pc = seg.prod(0, x)
    print(update_pc)

    for i in range(updated + 1, x):
        seg.set(i, 0)

    seg.set(y - 1, seg.get(y - 1) + update_pc)
    updated = max(updated, x - 1)
