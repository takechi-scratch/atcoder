from collections import deque

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)
S = list(input())

scores = [[] for _ in range(N)]
starts = [set() for _ in range(N)]
bfs = deque([])
for i, x in enumerate(S):
    if x == "S":
        scores[i].append((0, i))
        bfs.append((i, 0, i))

while len(bfs) > 0:
    now, now_score, start = bfs.popleft()
    for next_node in sides[now]:
        if len(scores[next_node]) >= 2 and now_score + 1 > scores[next_node][1][0]:
            continue

        if start not in starts[next_node]:
            scores[next_node].append((now_score + 1, start))
            starts[next_node].add(start)
            bfs.append((next_node, now_score + 1, start))

ans = []
for i, x in enumerate(S):
    if x == "D":
        ans.append(scores[i][0][0] + scores[i][1][0])
print(*ans, sep="\n")
