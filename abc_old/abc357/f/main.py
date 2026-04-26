from atcoder.lazysegtree import LazySegTree

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
MOD = 998244353


class Element:
    def __init__(self, multi_sum: int, a_sum: int, b_sum: int, size: int):
        self.multi_sum = multi_sum % MOD
        self.a_sum = a_sum % MOD
        self.b_sum = b_sum % MOD
        self.size = size


def op(x: Element, y: Element):
    return Element(x.multi_sum + y.multi_sum, x.a_sum + y.a_sum, x.b_sum + y.b_sum, x.size + y.size)


def mapping(f: tuple[int, int], x: Element):
    return Element(
        x.multi_sum + x.a_sum * f[1] + x.b_sum * f[0] + f[0] * f[1] * x.size,
        x.a_sum + f[0] * x.size,
        x.b_sum + f[1] * x.size,
        x.size,
    )


# 積の和, Aの和, Bの和, サイズ
lst = LazySegTree(
    op,
    Element(0, 0, 0, 0),
    mapping,
    lambda f, g: ((f[0] + g[0]) % MOD, (f[1] + g[1]) % MOD),
    (0, 0),
    [Element(a * b, a, b, 1) for a, b in zip(A, B)],
)

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        l, r, x = query[1:]
        lst.apply(l - 1, r, (x, 0))
    elif query[0] == 2:
        l, r, x = query[1:]
        lst.apply(l - 1, r, (0, x))
    else:
        l, r = query[1:]
        print(lst.prod(l - 1, r).multi_sum)
