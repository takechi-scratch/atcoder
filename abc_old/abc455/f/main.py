from atcoder.lazysegtree import LazySegTree

N, Q = [int(x) for x in input().split()]
MOD = 998244353

# ペアの積の和（nC2のやつ）→総和と2乗和を持っておけばいい！！
seg = LazySegTree(
    lambda x, y: ((x[0] + y[0]) % MOD, (x[1] + y[1]) % MOD, x[2] + y[2]),
    (0, 0, 0),
    lambda f, x: ((x[0] + f * x[2]) % MOD, (x[1] + 2 * f * x[0] + f**2 * x[2]) % MOD, x[2]),
    lambda f1, f2: (f1 + f2) % MOD,
    0,
    [(0, 0, 1)] * N,
)

for _ in range(Q):
    l, r, a = [int(x) for x in input().split()]
    seg.apply(l - 1, r, a)

    s_sum, b_sum, size = seg.prod(l - 1, r)

    print((s_sum**2 - b_sum) % MOD * pow(2, -1, MOD) % MOD)
