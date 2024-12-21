# N = int(input())
H, W, X, Y = [int(x) for x in input().split()]
X -= 1
Y -= 1
# テンプレコード、グリッドgridの二次元入力。
grid = []
for _ in range(H):
    grid.append(list(input()))
T = list(input())
sizis = "UDLR"

for sizi in T:
    # 適当に"OK"とかいう文字に変えちゃう
    if grid[X][Y] == "@":
        grid[X][Y] = "OK"

    # テンプレコード、移動が文字指示になるときの書き方。リストの順序には注意。
    di, dj = ((-1, 0), (1, 0), (0, -1), (0, 1))[sizis.index(sizi)]
    if not(-1 < di + X < H and -1 < dj + Y < W):
        continue

    if grid[di + X][dj + Y] == "#":
        continue

    X += di
    Y += dj

# いつも通り、ループの後を忘れない！
if grid[X][Y] == "@":
    grid[X][Y] = "OK"

# 後で数える
ans = 0
for i in grid:
    ans += i.count("OK")

print(X + 1, Y + 1, ans)
