# 初ダイクストラ？
# 辺のモードを保持して、各頂点ごとの最小コストを記録していく

import heapq

N, M, X = [int(x) for x in input().split()]
sides = [[[] for _ in range(N)] for _ in range(2)]
min_cost = [[10 ** 20 for _ in range(N)] for _ in range(2)]  # 各モード・辺ごとの最小コストを記録

for _ in range(M):
    u, v = [int(x) - 1 for x in input().split()]
    sides[0][u].append(v)  # モード0のときは、入力通り
    sides[1][v].append(u)  # モード1のときは、ひっくり返して追加

bfs = [(0, 0, 0)]
heapq.heapify(bfs)

ans = 10 ** 20
while len(bfs) > 0:
    # BFSに似てるけど、現時点でのコストが最も小さいものから取り出していくのがポイント
    cost, now, mode = heapq.heappop(bfs)

    min_cost[mode][now] = cost

    if cost + X < min_cost[1 - mode][now]:
        heapq.heappush(bfs, (cost + X, now, 1 - mode))
        min_cost[1 - mode][now] = cost + X
    if now == N - 1:
        ans = min(ans, cost + X)

    for next_node in sides[mode][now]:
        if next_node == N - 1:
            ans = min(ans, cost + 1)

        # WAポイント！！！costの追加判断は、pushする前に。minの更新は、pushした後に。
        # TLEとかWAとかで悩まされてきたやつ…。

        # visitedの場合はここで更新してもいいけど、最大・最小が絡むとおかしなことになる
        if cost + 1 < min_cost[mode][next_node]:
            heapq.heappush(bfs, (cost + 1, next_node, mode))
            min_cost[mode][next_node] = cost + 1

# 一応解が存在することを確認
assert ans != 10 ** 20
print(ans)
