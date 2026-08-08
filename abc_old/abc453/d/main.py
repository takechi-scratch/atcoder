from collections import deque
from sys import exit

H, W = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]

DIRECTION = ["D", "U", "L", "R"]

start, goal = (-1, -1), (-1, -1)
for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            start = (i, j)
        elif S[i][j] == "G":
            goal = (i, j)

best_score = [[[10**18] * 4 for _ in range(W)] for _ in range(H)]
bfs = deque()
for dir in range(4):
    bfs.append((start, dir, 0))
    best_score[start[0]][start[1]][dir] = 0

while len(bfs) > 0:
    now, now_dir, now_score = bfs.popleft()
    i, j = now
    if now_score > best_score[i][j][now_dir]:
        continue

    ok_dir = list(range(4))

    if S[i][j] == "o":
        ok_dir = [ok_dir[now_dir]]
    elif S[i][j] == "x":
        ok_dir.pop(now_dir)

    for next_dir in ok_dir:
        di, dj = [(1, 0), (-1, 0), (0, -1), (0, 1)][next_dir]

        if not (0 <= i + di < H and 0 <= j + dj < W):
            continue

        ni, nj = i + di, j + dj

        if S[ni][nj] == "#":
            continue

        if best_score[ni][nj][next_dir] <= now_score + 1:
            continue

        best_score[ni][nj][next_dir] = now_score + 1
        bfs.append(((ni, nj), next_dir, now_score + 1))

before_dir = 0
for before_dir in range(4):
    if best_score[goal[0]][goal[1]][before_dir] < 10**18:
        route = []
        i, j = goal
        ok = True
        while (i, j) != start:
            for dir in range(4):
                di, dj = [(-1, 0), (1, 0), (0, 1), (0, -1)][before_dir]

                if not (0 <= i + di < H and 0 <= j + dj < W):
                    continue

                ni, nj = i + di, j + dj

                if S[ni][nj] == "o" and before_dir != dir:
                    continue
                elif S[ni][nj] == "x" and before_dir == dir:
                    continue

                if best_score[ni][nj][dir] < 10**18 and best_score[i][j][before_dir] - best_score[ni][nj][dir] == 1:
                    route.append(DIRECTION[before_dir])
                    i, j = ni, nj
                    before_dir = dir
                    break
            else:
                ok = False

        if ok:
            print("Yes")
            print("".join(reversed(route)))
            break


else:
    print("No")
    exit()
