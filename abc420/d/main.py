from collections import deque

H, W = [int(x) for x in input().split()]
A = [list(input()) for _ in range(H)]
sides = [[] for _ in range(H * W * 2)]

for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            start = i * W + j
            A[i][j] = "."
        elif A[i][j] == "G":
            goal = i * W + j
            A[i][j] = "."


for i in range(H):
    for j in range(W):
        now_node = i * W + j
        if A[i][j] == "#":
            continue

        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            next_node = ni * W + nj
            if not (0 <= ni < H and 0 <= nj < W) or A[ni][nj] == "#":
                continue

            # if A[i][j] == "." or A[i][j] == "?": 前の区別はいらなそう
            if A[ni][nj] == ".":
                sides[now_node].append(next_node)
                sides[now_node + H * W].append(next_node + H * W)

            elif A[ni][nj] == "o":
                sides[now_node].append(next_node)

            elif A[ni][nj] == "x":
                sides[now_node + H * W].append(next_node + H * W)

            elif A[ni][nj] == "?":
                sides[now_node].append(next_node + H * W)
                sides[now_node + H * W].append(next_node)

            else:
                raise RuntimeError

bfs = deque([start])
score = [10 ** 18] * H * W * 2
score[start] = 0
ans = 10 ** 18

while len(bfs) > 0:
    now = bfs.popleft()

    for next_node in sides[now]:
        if score[now] + 1 >= score[next_node]:
            continue

        score[next_node] = score[now] + 1
        bfs.append(next_node)

ans = min(score[goal], score[goal + H * W])

if ans == 10 ** 18:
    print(-1)
else:
    print(ans)
