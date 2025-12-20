from atcoder.segtree import SegTree


def op(x, y):
    return [min(x[0], y[0]), max(x[1], y[1])]


def e():
    return [-(10**18), 10**18]


N, Q = [int(x) for x in input().split()]
x_seg = SegTree(op, [10**18, -(10**18)], N)
y_seg = SegTree(op, [10**18, -(10**18)], N)

for i in range(N):
    x, y = [int(x) for x in input().split()]
    x_seg.set(i, [x + y, x + y])
    y_seg.set(i, [x - y, x - y])


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        x, y = query[2:]
        x_seg.set(query[1] - 1, [x + y, x + y])
        y_seg.set(query[1] - 1, [x - y, x - y])

    else:
        x, y = query[3:]
        x_seg_res = x_seg.prod(query[1] - 1, query[2])
        y_seg_res = y_seg.prod(query[1] - 1, query[2])
        print(
            max(
                abs(x_seg_res[0] - (x + y)),
                abs(x_seg_res[1] - (x + y)),
                abs(y_seg_res[0] - (x - y)),
                abs(y_seg_res[1] - (x - y)),
            )
        )
        # target = [x + y, x - y]
