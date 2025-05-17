from sortedcontainers import SortedSet
from collections import defaultdict

H, W, N = [int(x) for x in input().split()]

grid_row_j = defaultdict(SortedSet)
grid_col_i = defaultdict(SortedSet)

for _ in range(N):
    x, y = [int(x) - 1 for x in input().split()]
    grid_row_j[x].add(y)
    grid_col_i[y].add(x)

Q = int(input())

for _ in range(Q):
    query = [int(x) - 1 for x in input().split()]

    if query[0] == 0:
        x = query[1]
        picked = grid_row_j[x]
        print(len(picked))

        grid_row_j[x] = SortedSet()
        for pick_y in picked:
            grid_col_i[pick_y].discard(x)

    elif query[0] == 1:
        y = query[1]
        picked = grid_col_i[y]
        print(len(picked))

        grid_col_i[y] = SortedSet()
        for pick_x in picked:
            grid_row_j[pick_x].discard(y)

    else:
        raise RuntimeError
