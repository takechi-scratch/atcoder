H, W = [int(x) for x in input().split()]
board = [["#"] + ["."] * (W - 2) + ["#"] for _ in range(H)]
board[0] = ["#"] * W
board[-1] = ["#"] * W
for x in board:
    print(*x, sep="")
