from atcoder.dsu import DSU

N, Q = [int(x) for x in input().split()]
uf = DSU(N)

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        uf.merge(query[1] - 1, query[2] - 1)
    else:
        print(uf.size(query[1] - 1))
