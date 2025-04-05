from bisect import bisect_left
from collections import defaultdict

H, W, now_r, now_c = [int(x) for x in input().split()]
now_r, now_c = now_r - 1, now_c - 1
row_walls = defaultdict(list)
col_walls = defaultdict(list)

N = int(input())
for _ in range(N):
    r, c = [int(x) - 1 for x in input().split()]
    row_walls[r].append(c)
    col_walls[c].append(r)

for r in row_walls.values():
    r.sort()

for c in col_walls.values():
    c.sort()

Q = int(input())
for _ in range(Q):
    d, l = input().split()
    l = int(l)

    match d:
        case "L":
            next_wall_index = bisect_left(row_walls[now_r], now_c) - 1
            next_wall = row_walls[now_r][next_wall_index] if next_wall_index >= 0 else -1

            now_c = max(now_c - l, next_wall + 1)

        case "R":
            next_wall_index = bisect_left(row_walls[now_r], now_c)
            next_wall = row_walls[now_r][next_wall_index] if next_wall_index < len(row_walls[now_r]) else W

            now_c = min(now_c + l, next_wall - 1)

        case "U":
            next_wall_index = bisect_left(col_walls[now_c], now_r) - 1
            next_wall = col_walls[now_c][next_wall_index] if next_wall_index >= 0 else -1

            now_r = max(now_r - l, next_wall + 1)

        case "D":
            next_wall_index = bisect_left(col_walls[now_c], now_r)
            next_wall = col_walls[now_c][next_wall_index] if next_wall_index < len(col_walls[now_c]) else H

            now_r = min(now_r + l, next_wall - 1)

    print(now_r + 1, now_c + 1)
