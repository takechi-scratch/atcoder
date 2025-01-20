# 初の優先度付きキュー！！やったーーー

import heapq

H, W, X = [int(x) for x in input().split()]
P, Q = [int(x) for x in input().split()]
# WAポイント！入力の座標はだいたい1大きい！！！！
P -= 1
Q -= 1
score = []
for _ in range(H):
    score.append([int(x) for x in input().split()])

visited = [[False] * W for _ in range(H)]

# 優先度付きキューを使って大きさ順に並べておくことで、まだ吸収できるか&どこを吸収したらいいかすぐわかる
# テンプレコード: 優先度付きキュー/heapqの使い方
pri_que = [(score[P][Q], (P, Q))]
heapq.heapify(pri_que)
visited[P][Q] = True
now_score = 0

# DFSってことになるのかな？
while len(pri_que) > 0:
    teki_score, root_pos = heapq.heappop(pri_que)

    # 最小でも吸収できないなら終了
    if teki_score >= now_score / X and now_score != 0:  # 右はスタート時の例外
        break

    # print(teki_score)

    root_i, root_j = root_pos
    now_score += teki_score

    # あるあるの、移動方向列挙
    for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        # あるあるの、範囲外防止
        if not(-1 < root_i + di < H and -1 < root_j + dj < W):
            continue

        if visited[root_i + di][root_j + dj] is True:
            continue

        heapq.heappush(pri_que, (score[root_i + di][root_j + dj], (root_i + di, root_j + dj)))
        # WAポイント！ここでvisitedを設定しておかないと、2重で追加されてしまうことがある
        visited[root_i + di][root_j + dj] = True

print(now_score)
