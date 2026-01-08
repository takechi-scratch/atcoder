from collections import deque

N, K = [int(x) for x in input().split()]
S = list(input())
COLOR = "RGB"

dp = [[10**18 for _ in range(3)] for _ in range(N + 1)]
dp[-1][2] = 0

pass_records = [deque() for _ in range(3)]
pass_records[2].append((-1, 0))

# 色を変えることはできない！
for i in range(N):
    # 前を消さずに、そのままつなげられる
    # WAポイント！つなげるのは直前の実際の色じゃなくてもいい。
    now_color_num = COLOR.index(S[i])
    dp[i][now_color_num] = dp[i - 1][(now_color_num - 1) % 3]

    for j in range(3):
        # 前を消して、過去のより良い記録で置き換える（つなげない）

        # 「スライド最小値」問題と呼ばれる。dequeを使ってO(1)で解答可能
        # 「いつ削除するか」と「暫定の最小値」を持っておいて、追加するときは余計なものをpopしてから右から挿入
        # 削除されるときになったら、左から削除

        # SortedListやセグ木でもO(logN)でできる。
        if len(pass_records[j]) > 0:
            dp[i][j] = min(dp[i][j], pass_records[j][0][1] + 1)

        now = dp[i][j]
        while len(pass_records[j]) > 0 and pass_records[j][-1][1] > now:
            pass_records[j].pop()

        pass_records[j].append((i, now))
        while pass_records[j][0][0] <= i - K:
            pass_records[j].popleft()

if dp[N - 1][2] == 10**18:
    raise RuntimeError

print(dp[N - 1][2])
