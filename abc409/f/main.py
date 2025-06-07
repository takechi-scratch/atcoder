# WA解法。どこかがおかしい

from atcoder.dsu import DSU
import heapq

def manhattan(i: int, j: int):
    return abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])

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

dists = []
dists_set = set()
for i in range(N):
    for j in range(i + 1, N):
        dists_set.add((i, j))
        dists.append((manhattan(i, j), i, j))

heapq.heapify(dists)

for query in queries:
    if query[0] == 1:
        a, b = query[1] - 1, query[2] - 1
        nodes.append((a, b))
        leader_nearest = []
        for i in range(len(nodes) - 1):
            leader = uf.leader(i)
            distance = manhattan(len(nodes) - 1, i)
            leader_nearest.append((distance, i, len(nodes) - 1))

        for distance, i, j in leader_nearest:
            heapq.heappush(dists, (distance, i, j))
            dists_set.add((i, j))

    elif query[0] == 2:
        if len(dists) == 0:
            print(-1)
            break

        nearest_distance, i, j = heapq.heappop(dists)
        dists_set.discard((i, j))
        merges = []
        merges.append((i, j))
        while len(dists) > 0:
            distance, i, j = heapq.heappop(dists)
            if distance > nearest_distance:
                heapq.heappush(dists, (distance, i, j))
                break

            dists_set.discard((i, j))
            if not uf.same(i, j):
                merges.append((i, j))

        print(nearest_distance)

        for i, j in merges:
            uf.merge(i, j)

    else:
        u, v = query[1] - 1, query[2] - 1
        print("Yes" if uf.same(u, v) else "No")
