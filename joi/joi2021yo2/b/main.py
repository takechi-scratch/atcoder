# なぜかTLE解法。O(N^2*3^N)なんだけどなぁ...。

from itertools import product
from collections import deque

N, Q = [int(x) for x in input().split()]

assert N <= 5

ABC = ["A", "B", "C"]
ABC_index = {"A": 0, "B": 1, "C": 2}


def str_to_id(s: str | list[str]) -> int:
    ans = 0
    for i, x in enumerate(reversed(s)):
        if x in ABC_index:
            ans += (ABC_index[x]) * (3**i)

    return ans


sides = [[] for _ in range(3**N)]
costs = [[] for _ in range(3**N)]
best_score = [10**18] * (3**N)

for s in product(ABC, repeat=N):
    s_id = str_to_id(s)

    for i in range(1, len(s)):
        next_s_id = str_to_id(s[i::-1] + s[i + 1 :])
        sides[next_s_id].append(s_id)
        costs[next_s_id].append(1)

bfs = deque([])
for s in product(ABC, repeat=N):
    i = str_to_id(list(sorted(s)))
    best_score[i] = 0
    bfs.append((i, 0))

while len(bfs) > 0:
    now, now_score = bfs.popleft()
    if now_score > best_score[now]:
        continue

    for next_node, c in zip(sides[now], costs[now]):
        if now_score + c < best_score[next_node]:
            best_score[next_node] = now_score + c
            bfs.append((next_node, now_score + c))


for _ in range(Q):
    s = list(input())
    print(best_score[str_to_id(s)])
