from collections import deque

N, M, S, T = [int(x) for x in input().split()]
S -= 1
T -= 1
sides = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    sides[a].append(b)

for x in sides:
    x.sort()

bfs = deque([(S, 0)])
scores = [10**18] * N
scores[S] = 0

while len(bfs) > 0:
    now, now_score = bfs.popleft()
    if now_score > scores[now]:
        continue

    for i, next_node in enumerate(sides[now]):
        if i == 0:
            if scores[next_node] <= now_score:
                continue

            scores[next_node] = now_score
            bfs.appendleft((next_node, now_score))

        else:
            if scores[next_node] <= now_score + 1:
                continue

            scores[next_node] = now_score + 1
            bfs.append((next_node, now_score + 1))

if scores[T] == 10**18:
    print(-1)
else:
    print(scores[T])
