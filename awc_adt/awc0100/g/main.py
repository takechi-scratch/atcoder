from atcoder.dsu import DSU

N, M = [int(x) for x in input().split()]
uf = DSU(N)
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    uf.merge(u, v)

Q = int(input())
for _ in range(Q):
    print(uf.size(int(input()) - 1))
