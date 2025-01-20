from collections import deque

H, W, D = [int(x) for x in input().split()]
floor = []

for _ in range(H):
    floor.append(list(input()))

# WAポイント！！BFSとDFSの使い分けに注意。
# 最短距離が大切な問題はDFSだと機能しない。
# 基本的にはBFSだと思ってdequeを使うべき！
bfs = deque()
ans = 0

for i in range(H):
    for j in range(W):
        # 多頂点でもBFSはできる。
        if floor[i][j] == "H":
            bfs.append((i, j, 0))
            ans += 1
            floor[i][j] = "O"

while len(bfs) > 0:
    i, j, n = bfs.popleft()

    if n >= D:
        continue

    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if not (0 <= i + di < H and 0 <= j + dj < W):
            continue

        if floor[i + di][j + dj] == ".":
            if n + 1 < D:
                bfs.append((i + di, j + dj, n + 1))
            ans += 1
            # 一応ここで完了マークをつけておく（無限ループ対策）
            floor[i + di][j + dj] = "O"

print(ans)
