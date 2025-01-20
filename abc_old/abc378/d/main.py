# DFSの使い方は要復習。
# 書きなれておければ時間短縮に。

from collections import deque

H, W, K = [int(x) for x in input().split()]
grid = []
# WAポイント！二次元リスト（三次元リスト？）の際は生成時に注意。うまくやらないと連動してしまう。
# テンプレコード、二次元リストの生成をリスト内包表記で
ok_to = [[[] for _ in range(W)] for _ in range(H)]

for _ in range(H):
    grid.append(list(input()))

start = []

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            continue
        start.append((i, j))

        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            # テンプレコード、移動がマス外に行くときの処理。
            if not(-1 < i + x < H and -1 < j + y < W):
                continue

            # そのマスから行けるところの一覧をあらかじめ作っておく。
            if grid[i + x][j + y] == ".":
                ok_to[i][j].append([i + x, j + y])



dfs = deque(start)
dfs_route = deque([{x} for x in start])
dfs_score = deque([0] * len(start))
ans = 0

while len(dfs) > 0:
    x, y = dfs.pop()
    route = dfs_route.pop()
    score = dfs_score.pop() + 1

    if score > K:
        ans += 1
        continue

    for i, j in ok_to[x][y]:
        # ルートの中に含まれていた場合。折り返しとかを柔軟に検知できるとよりよいかも。
        if (i, j) in route:
            continue

        dfs.append((i, j))
        # WAポイント！routeに要素を足すとfor文の中でどんどん足されて行ってしまう。
        # setの結合（和集合）のやり方も要復習。
        dfs_route.append(route | {(i, j)})
        dfs_score.append(score)

# 向きが決まっているので2で割る必要はない。
print(ans)
