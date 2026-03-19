from collections import deque

N, M, K = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
capacities = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = [int(x) for x in input().split()]
    sides[u - 1].append(v - 1)
    sides[v - 1].append(u - 1)
    capacities[u - 1].append(w)
    capacities[v - 1].append(w)


scores = [10**18] * N
scores[0] = 0
bfs = deque([0])
while len(bfs) > 0:
    now = bfs.popleft()
    for next_node, next_w in zip(sides[now], capacities[now]):
        if scores[next_node] < 10**18:
            continue

        if next_w < K:
            continue

        scores[next_node] = scores[now] + 1
        bfs.append(next_node)

if scores[-1] == 10**18:
    print(-1)
else:
    print(scores[-1])
