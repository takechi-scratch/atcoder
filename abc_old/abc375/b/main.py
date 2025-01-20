N = int(input())

route = []

for _ in range(N):
    route.append([int(x) for x in input().split()])
# 最後に戻ってくるので0,0を足す
route.append([0, 0])

kyori = 0
# WAポイント！初期値に注意。問題文を見落とさない。
x, y = 0, 0

for i in range(N + 1):
    # 距離の計算はスラスラ書けるようにしておきたい
    kyori += ((route[i][0] - x) ** 2 + (route[i][1] - y) ** 2) ** 0.5
    x, y = route[i][0], route[i][1]

print(kyori)
