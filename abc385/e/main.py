# WA解答。
# 木の問題。やったことがなかったので要復習。

N = int(input())
sides = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

ans = N
for root in range(N):
    x = len(sides[root])
    y = 10 ** 8
    y_yobi = -1
    for i in sides[root]:
        nobaseru = len(sides[i]) - 1
        if nobaseru < y:
            if y_yobi == -1:
                y_yobi = nobaseru
            else:
                y = max(y_yobi, nobaseru)
                y_yobi = min(y_yobi, nobaseru)

    if y_yobi == -1:
        y_yobi = 10 ** 8

    # ユ木でXをそのまま残すものと、1個消すものを挙げている。
    # 実際は全て消すまでやらなければいけない！
    # XごとのYの値を列挙してソートするのがGood。
    ans = min(ans, N - ((min(y, y_yobi) + 1) * x + 1), N - (y + 1) * (x - 1) - 1)

print(ans)
