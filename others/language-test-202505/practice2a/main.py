from atcoder.dsu import DSU

N, Q = [int(x) for x in input().split()]

uf = DSU(N)
for _ in range(Q):
    t, u, v = [int(x) for x in input().split()]
    if t == 0:
        uf.merge(u, v)
    else:
        print(int(uf.same(u, v)))
