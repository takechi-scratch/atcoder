from collections import deque

N, M = [int(x) for x in input().split()]
keiro = {}
for i in range(N):
    keiro[i] = []
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    keiro[a].append(b)

bfs = deque([0])
bfs_score = deque([0])
ans = -1
visited = set()

while len(bfs) > 0:
    tyousa = bfs.popleft()
    now_score = bfs_score.popleft()

    if tyousa == 0 and now_score > 0:
        ans = now_score
        break


    if tyousa in visited:
        continue

    visited.add(tyousa)


    for x in keiro[tyousa]:
        bfs.append(x)
        bfs_score.append(now_score + 1)

print(ans)
