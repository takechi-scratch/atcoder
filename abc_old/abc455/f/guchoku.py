from atcoder.lazysegtree import LazySegTree
from itertools import permutations

N, Q = [int(x) for x in input().split()]
MOD = 998244353

seg = LazySegTree(
    lambda x, y: (x[0] + y[0], x[1] + y[1]),
    (0, 0),
    lambda f, x: (x[0] + f * x[1], x[1]),
    lambda f1, f2: f1 + f2,
    0,
    [(0, 1)] * N,
)

for _ in range(Q):
    l, r, a = [int(x) for x in input().split()]
    seg.apply(l - 1, r, a)

    B = [seg.get(i)[0] for i in range(l - 1, r)]
    M = r - l + 1
    ans = 10**18
    for steps in permutations(range(M)):
        now = B[steps[0]]
        now_score = 0
        for x in steps[1:]:
            now_score += now * B[x]
            now_score %= MOD
            now += B[x]

        assert ans == 10**18 or ans == now_score
        ans = min(ans, now_score)

    print(list(sorted(B)))
    print(ans)
