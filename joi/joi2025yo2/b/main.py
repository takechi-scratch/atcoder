import heapq
from collections import defaultdict
from atcoder.dsu import DSU

N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
P = [int(x) - 1 for x in input().split()]

uf = DSU(N)
for i, x in enumerate(P):
    if x != -2:
        uf.merge(i, x)

side_groups = []
start_groups = []

for nodes in uf.groups():
    visited = set()
    starts = []
    sides = defaultdict(list)

    for now in nodes:
        before_node = P[now]
        if before_node == -2:
            starts.append(now)
        else:
            sides[before_node].append(now)

    start_groups.append(starts)
    side_groups.append(sides)

ans = -2
for i, x in enumerate(P):
    if x == -2 and A[i] <= X:
        ans = max(ans, i)

for sides, starts in zip(side_groups, start_groups):
    if starts is None:
        continue

    scores = {}
    djk = []
    for start in starts:
        if A[start] <= X:
            scores[start] = A[start]
            djk.append((A[start], start))

    heapq.heapify(djk)

    while len(djk) > 0:
        now_score, now = heapq.heappop(djk)

        if now_score < scores[now]:
            continue

        for next_node in sides[now]:
            next_score = now_score + A[next_node]
            if next_score > X:
                continue

            if next_node not in scores or scores[next_node] > next_score:
                heapq.heappush(djk, (next_score, next_node))
                scores[next_node] = next_score

    for key, value in scores.items():
        if value > X:
            continue

        ans = max(ans, key)

print(ans + 1)
