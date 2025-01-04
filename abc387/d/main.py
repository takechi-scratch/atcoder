# BFSで実装。
# 状態ごとに、「次に動けるのは上下か？左右か？」を見るのがポイント

from collections import deque

H, W = [int(x) for x in input().split()]
grid = []
for i in range(H):
    l = list(input())
    grid.append(l)

    if "S" in l:
        start = (i, l.index("S"))

# 今回のvisitedはgridを2個持っておく感じ
# 次に動くのが「上下」「左右」でチェック
visited = [[[False] * W for _ in range(H)] for _ in range(2)]

bfs = deque([])
# スタートは上下も左右も
for i in range(2):
    bfs.append((start, 0, i))


while len(bfs) > 0:
    now, score, next_move = bfs.popleft()
    x, y = now

    if grid[x][y] == "G":
        print(score)
        break

        # next_moveの値によって、次の移動を列挙
    if next_move == 1:
        next_dxdy = ((1, 0), (-1, 0))
    else:
        next_dxdy = ((0, 1), (0, -1))

    for dx, dy in next_dxdy:
        # 範囲外に出るならアウト
        if not (0 <= x + dx < H and 0 <= y + dy < W):
            continue

        # 1. gridが#とSではない（普通のBFSと一緒）
        # 2. すでに同じ位置で、次の移動タイプも同じものを数えているならもう追加しない
        #    BFSなので、最短距離のものが一番最初に到達する→次に到達するときにはもう余計になってる
        if grid[x + dx][y + dy] != "#" and grid[x + dx][y + dy] != "S" and visited[next_move][x + dx][y + dy] is False:
            visited[next_move][x + dx][y + dy] = True
            bfs.append(((x + dx, y + dy), score + 1, 1 - next_move))


# 最後までbreakしなかった場合（小技）
else:
    print(-1)

# 端処理
