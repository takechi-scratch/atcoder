# ただ遅延セグ木を貼るだけじゃ無理そう？

from atcoder.lazysegtree import LazySegTree

N = int(input())
A = [int(x) for x in input().split()]

seg = LazySegTree(
    lambda x, y: x + y,
    0,
    lambda f, x: max(0, x - f),
    lambda f1, f2: f1 + f2,
    0,
    A,
)

all_things = sum(A)
Q = int(input())
for _ in range(Q):
    l, r, k = [int(x) for x in input().split()]
    seg.apply(l - 1, r, k)
    now = seg.all_prod()
    print(all_things - now)
    all_things = now
