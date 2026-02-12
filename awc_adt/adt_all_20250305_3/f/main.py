# https://atcoder.jp/contests/abc390/tasks/abc390_c

H, W = [int(x) for x in input().split()]
grid = [[""] * W for _ in range(H)]

min_x, min_y = H - 1, W - 1
max_x, max_y = 0, 0

for i in range(H):
    for j, x in enumerate(input()):
        grid[i][j] = x

        if x != "#":
            continue

        min_x = min(min_x, i)
        min_y = min(min_y, j)
        max_x = max(max_x, i)
        max_y = max(max_y, j)

for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        if grid[i][j] == ".":
            print("No")
            exit()

print("Yes")
