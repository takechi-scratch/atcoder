# 最短経路のbfsでつまずくのが嫌だったのでダイクストラ風に
# 実行時間はかなり厳しい（1500msくらい）

import heapq

H, W = [int(x) for x in input().split()]
grid = []
for _ in range(H):
    grid.append(list(input()))
A, B, C, D = [int(x) - 1 for x in input().split()]

min_costs = [[10 ** 18] * W for _ in range(H)]

bfs = [(0, (A, B))]
min_costs[A][B] = 0
heapq.heapify(bfs)

while len(bfs) > 0:
    now_cost, now = heapq.heappop(bfs)
    if min_costs[now[0]][now[1]] < now_cost:
        continue

    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = now[0] + di, now[1] + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue

        # if min_costs[ni][nj] != 10 ** 18:
        #     continue

        if grid[ni][nj] == ".":
            if min_costs[ni][nj] > now_cost:
                min_costs[ni][nj] = min(min_costs[ni][nj], now_cost)
                heapq.heappush(bfs, (now_cost, (ni, nj)))

        else:
            # 実際に壁を壊すことはせずに、壊せるところの「最小コスト」を1増やして更新
            if min_costs[ni][nj] > now_cost + 1:
                min_costs[ni][nj] = now_cost + 1
                heapq.heappush(bfs, (now_cost + 1, (ni, nj)))

            ni2, nj2 = ni + di, nj + dj
            if not (0 <= ni2 < H and 0 <= nj2 < W):
                continue

            if min_costs[ni2][nj2] > now_cost + 1:
                min_costs[ni2][nj2] = now_cost + 1
                heapq.heappush(bfs, (now_cost + 1, (ni2, nj2)))

print(min_costs[C][D])
