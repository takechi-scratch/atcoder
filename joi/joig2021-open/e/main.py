# 解説AC（WA取り）
# 2つの条件があるときは、頂点を増やしてBFSをする！！！！（典型なんだからそろそろ覚えたい）

import heapq

N, M, L = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
costs = [[] for _ in range(N)]
rev_sides = [[] for _ in range(N)]
rev_costs = [[] for _ in range(N)]


for _ in range(M):
    a, b, c = [int(x) for x in input().split()]
    sides[a - 1].append(b - 1)
    costs[a - 1].append(c)
    rev_sides[b - 1].append(a - 1)
    rev_costs[b - 1].append(c)

best_scores = [[10**18] * (M + 1) for _ in range(N)]
# スコアが一番小さいものと、そのターン数（たぶん一番大きいもの）
best_best_scores = [[10**18, -1] for _ in range(N)]
best_best_scores[0] = [0, 0]
queue = [(0, 0, 0)]

while len(queue) > 0:
    now_score, now_turns, now = heapq.heappop(queue)
    if now_score > best_scores[now][now_turns]:
        # WAポイント！
        # breakとcontinueの間違いにはくれぐれも注意！！！！
        continue

    for next_node, score in zip(sides[now], costs[now]):
        if best_scores[next_node][now_turns] <= now_score + score:
            continue

        if best_best_scores[next_node][0] <= now_score + score and best_best_scores[next_node][1] <= now_turns:
            continue

        best_scores[next_node][now_turns] = now_score + score
        if best_best_scores[next_node][0] > now_score + score or (
            best_best_scores[next_node][0] == now_score + score and best_best_scores[next_node][1] > now_turns
        ):
            best_best_scores[next_node][0] = now_score + score
            best_best_scores[next_node][1] = now_turns

        heapq.heappush(queue, (now_score + score, now_turns, next_node))

    for next_node, score in zip(rev_sides[now], rev_costs[now]):
        if best_scores[next_node][now_turns + 1] <= now_score + score:
            continue

        if best_best_scores[next_node][0] <= now_score + score and best_best_scores[next_node][1] <= now_turns + 1:
            continue

        best_scores[next_node][now_turns + 1] = now_score + score
        if best_best_scores[next_node][0] > now_score + score or (
            best_best_scores[next_node][0] == now_score + score and best_best_scores[next_node][1] > now_turns + 1
        ):
            best_best_scores[next_node][0] = now_score + score
            best_best_scores[next_node][1] = now_turns + 1
        heapq.heappush(queue, (now_score + score, now_turns + 1, next_node))

ans = 10**18
for turns, score in enumerate(best_scores[-1]):
    if score <= L:
        ans = min(ans, turns)

if ans == 10**18:
    print(-1)
else:
    print(ans)
