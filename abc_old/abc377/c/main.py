N, M = [int(x) for x in input().split()]

board = set()

ans = N ** 2

# 置けないマスをsetで管理する。
# 置けるマスは多すぎて無理なので、少ない方を心掛ける！
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    for x, y in ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (0, 0)):
        if 0 <= a + x < N and 0 <= b + y < N and (a + x, b + y) not in board:
            board.add((a + x, b + y))
            ans -= 1

print(ans)
