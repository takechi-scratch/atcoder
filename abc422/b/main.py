# 上下左右をそのまま記述（8方向なら、diとdjをforで回すのが速そう）

H, W = [int(x) for x in input().split()]
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue

        blacks = 0
        blacks += (0 <= i + 1 < H and 0 <= j < W) and S[i + 1][j] == "#"
        blacks += (0 <= i - 1 < H and 0 <= j < W) and S[i - 1][j] == "#"
        blacks += (0 <= i < H and 0 <= j + 1 < W) and S[i][j + 1] == "#"
        blacks += (0 <= i < H and 0 <= j - 1 < W) and S[i][j - 1] == "#"

        if not (blacks == 2 or blacks == 4):
            print("No")
            exit()

print("Yes")
