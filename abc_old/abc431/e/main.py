from collections import deque

# 直す

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve(H: int, W: int, grid: list[list[int]]) -> int:
    score = [[[10**2] * 4 for _ in range(W)] for _ in range(H)]
    replaced = [[False] * W for _ in range(H)]
    if grid[-1][-1] == "A":
        score[-1][-1][0] = 0
        score[-1][-1][1] = 1
        score[-1][-1][3] = 1
    elif grid[-1][-1] == "B":
        score[-1][-1][0] = 1
        score[-1][-1][1] = 0
        score[-1][-1][3] = 1
    else:
        score[-1][-1][0] = 1
        score[-1][-1][1] = 1
        score[-1][-1][3] = 0

    bfs = deque([(H - 1, W - 1, 0), (H - 1, W - 1, 1), (H - 1, W - 1, 3)])
    while len(bfs) > 0:
        i, j, now_d = bfs.popleft()
        now_score = score[i][j][now_d]
        light_di, light_dj = DIR[now_d]

        for next_d in range(4):
            light_next_di, light_next_dj = DIR[next_d]
            if light_di == light_next_di and light_dj == light_next_dj:
                continue

            if (light_di == light_next_di and light_dj * -1 == light_next_dj) or (
                light_dj == light_next_dj and light_di * -1 == light_next_di
            ):
                continue

            if score[i][j][next_d] > now_score + 1:
                score[i][j][next_d] = now_score + 1
                bfs.append((i, j, next_d))

        di, dj = -light_di, -light_dj
        if not (0 <= i + di < H and 0 <= j + dj < W):
            continue

        if grid[i + di][j + dj] == "A":
            next_d = now_d
        elif grid[i + di][j + dj] == "B":
            light_next_di, light_next_dj = light_dj, light_di
            next_d = DIR.index((light_next_di, light_next_dj))
        else:
            light_next_di, light_next_dj = -light_dj, -light_di
            next_d = DIR.index((light_next_di, light_next_dj))

        if score[i + di][j + dj][next_d] > now_score:
            score[i + di][j + dj][next_d] = now_score
            bfs.appendleft((i + di, j + dj, next_d))

    return score[0][0][0]


T = int(input())
for _ in range(T):
    H, W = [int(x) for x in input().split()]
    grid = [list(input()) for _ in range(H)]
    print(solve(H, W, grid))
