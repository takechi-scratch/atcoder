# 各列ごとにブロックをsortして、何秒後に下に来れるかをチェック
# ブロックを消しながらいつ消えるかを記録していく

from sortedcontainers import SortedList

N, W = [int(x) for x in input().split()]
grid = [SortedList() for _ in range(W)]
ans = [10 ** 9 + 1 for _ in range(N)]

for i in range(N):
    x, y = [int(x) - 1 for x in input().split()]
    grid[x].add((y, i))

# WAポイント！初期条件もちゃんと確認する。
if min([len(x) for x in grid]) >= 1:
    before_ans = -1
    for _ in range(N):  # ほぼ無限
        next_delete = before_ans + 1

        for x in grid:
            next_delete = max(next_delete, x[0][0] + 1)

        # 消せるブロックが0の列ができたら終わり
        end = False
        for x in grid:
            ans[x[0][1]] = next_delete
            x.pop(0)

            if len(x) == 0:
                end = True

        if end:
            break

        before_ans = next_delete

# ここからクエリ

Q = int(input())
for _ in range(Q):
    t, a = [int(x) for x in input().split()]
    print("Yes" if ans[a - 1] > t else "No")
