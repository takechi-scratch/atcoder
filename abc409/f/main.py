# 定数倍が厳しく通らない。C++への翻訳必須？

from atcoder.dsu import DSU
from sortedcontainers import SortedList

def manhattan(i: int, j: int):
    return abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])

class Dist:
    def __init__(self, i: int, j: int):
        self.dist = manhattan(i, j)
        self.i = i
        self.j = j

    def __lt__(self, other):
        assert isinstance(other, Dist)
        return self.dist < other.dist

N, Q = [int(x) for x in input().split()]
nodes = []
for _ in range(N):
    nodes.append(tuple(int(x) for x in input().split()))

last_N = N
queries = []
for _ in range(Q):
    query = tuple(int(x) for x in input().split())
    queries.append(query)
    if query[0] == 1:
        last_N += 1

uf = DSU(last_N)

dists = SortedList()
for i in range(N):
    for j in range(i + 1, N):
        dists.add(Dist(i, j))

for query in queries:
    if query[0] == 1:
        a, b = query[1], query[2]
        nodes.append((a, b))
        for i in range(len(nodes) - 1):
            dists.add(Dist(i, len(nodes) - 1))

    elif query[0] == 2:
        nearest_distance = 10 ** 18
        ok = False
        while len(dists) > 0:
            d = dists.pop(0)
            distance, i, j = d.dist, d.i, d.j

            if uf.same(i, j):
                continue

            if distance > nearest_distance:
                dists.add(Dist(i, j))
                break

            if nearest_distance == 10 ** 18:
                nearest_distance = distance

            uf.merge(i, j)
            ok = True

        if not ok:
            print(-1)
            continue

        assert nearest_distance < 10 ** 18
        print(nearest_distance)

    else:
        u, v = query[1] - 1, query[2] - 1
        print("Yes" if uf.same(u, v) else "No")
