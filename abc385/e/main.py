# 本番WA→解説AC
# 木の問題。やったことがなかったので要復習。
# 実際はグラフの特徴をつかめばOKかな？

N = int(input())
sides = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(x) - 1 for x in input().split()]
    sides[u].append(v)
    sides[v].append(u)

# 初期値の設定は丁寧に。
max_yuki = 3
for root in range(N):
    full_x = len(sides[root])
    # xのそれぞれについて、何本yを伸ばせるかリスト化
    ys = [len(sides[i]) - 1 for i in sides[root]]
    ys.sort(reverse=True)

    # xが増える→yは減る（そこまでのysの最小値）、その中での最大をとる
    for x in range(1, full_x + 1):
        max_yuki = max(max_yuki, 1 + x * (1 + ys[x - 1]))

print(N - max_yuki)
