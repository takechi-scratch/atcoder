from atcoder.fenwicktree import FenwickTree

N, Q = [int(x) for x in input().split()]
S = [int(x) for x in input().split()]
sf = FenwickTree(N)

for i, x in enumerate(S):
    sf.add(i, x)

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        l, r = query[1:]
        print(sf.sum(l - 1, r))
    else:
        x, v = query[1] - 1, query[2]
        sf.add(x, v - S[x])
        S[x] = v
