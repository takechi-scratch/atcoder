H, W = [int(x) for x in input().split()]
grid = []
for _ in range(H):
    grid.append(list(input()))

# 黒の左上と右下を調べる
min_x = W
max_x = -1
min_y = H
max_y = -1

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            min_x = min(min_x, j)
            max_x = max(max_x, j)
            min_y = min(min_y, i)
            max_y = max(max_y, i)

# その範囲の中に白が入ってしまっていたらアウト
ok = True
for i in range(min_y, max_y + 1):
    for j in range(min_x, max_x + 1):
        if grid[i][j] == ".":
            ok = False
            break

print("Yes" if ok else "No")
