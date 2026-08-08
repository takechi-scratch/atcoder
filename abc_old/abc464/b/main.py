H, W = [int(x) for x in input().split()]
pictures = [input() for _ in range(H)]
min_x, min_y, max_x, max_y = 10**18, 10**18, -(10**18), -(10**18)
for i in range(H):
    for j in range(W):
        if pictures[i][j] != "#":
            continue

        min_x = min(min_x, i)
        max_x = max(max_x, i)
        min_y = min(min_y, j)
        max_y = max(max_y, j)

for i in range(min_x, max_x + 1):
    print(pictures[i][min_y : max_y + 1])
