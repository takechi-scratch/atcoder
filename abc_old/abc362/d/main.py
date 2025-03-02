# ダイクストラ法の練習
# ABC395Eを簡単めにした感じ（そっちにも応用できる）

import heapq

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
costs = [[] for _ in range(N)]
for _ in range(M):
    u, v, b = [int(x) for x in input().split()]
    sides[u - 1].append(v - 1)
    costs[u - 1].append(b)

    sides[v - 1].append(u - 1)
    costs[v - 1].append(b)

min_cost = [10 ** 18] * N
# min_cost[0] = A[0]  # こういう先初期化はWAのもとかも
queue = [(A[0], 0)]
heapq.heapify(queue)

while len(queue) > 0:
    now_cost, now = heapq.heappop(queue)
    # 継続をはじくコードを置いておかないと、TLE（無限ループ？）になった

    if min_cost[now] <= now_cost:
        continue

    min_cost[now] = min(min_cost[now], now_cost)

    for next_node, next_side_cost in zip(sides[now], costs[now]):
        next_cost = now_cost + next_side_cost + A[next_node]

        # 上に書いたので、ここには書かなくてOK
        heapq.heappush(queue, (next_cost, next_node))

print(*min_cost[1:])
