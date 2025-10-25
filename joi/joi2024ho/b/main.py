import heapq
from bisect import bisect_right
import sys

input = sys.stdin.readline

N, M = [int(x) for x in input().split()]
S, T, L, K = [int(x) for x in input().split()]
S -= 1
T -= 1
sides = [[] for _ in range(N)]
costs = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    sides[a].append(b)
    sides[b].append(a)
    costs[a].append(c)
    costs[b].append(c)

ans = None

costs_from_start = [10**18] * N
costs_from_start[S] = 0
# WAポイント！ダイクストラのミス。タプルの優先順位に注意。
queue = [(0, S)]
while len(queue) > 0:
    now_score, now = heapq.heappop(queue)
    if now_score != costs_from_start[now]:
        continue

    for i, next_node in enumerate(sides[now]):
        if costs_from_start[now] + costs[now][i] < costs_from_start[next_node]:
            costs_from_start[next_node] = costs_from_start[now] + costs[now][i]
            heapq.heappush(queue, (costs_from_start[next_node], next_node))

costs_to_goal = [10**18] * N
costs_to_goal[T] = 0
queue = [(0, T)]
while len(queue) > 0:
    now_score, now = heapq.heappop(queue)
    if now_score != costs_to_goal[now]:
        continue

    for i, next_node in enumerate(sides[now]):
        if costs_to_goal[now] + costs[now][i] < costs_to_goal[next_node]:
            costs_to_goal[next_node] = costs_to_goal[now] + costs[now][i]
            heapq.heappush(queue, (costs_to_goal[next_node], next_node))


if costs_from_start[T] <= K:
    ans = N * (N - 1) // 2
elif N <= 3000 and M <= 3000:
    ans = 0
    for i in range(N):
        for j in range(i):
            if (
                min(
                    costs_to_goal[S],
                    costs_from_start[i] + L + costs_to_goal[j],
                    costs_from_start[j] + L + costs_to_goal[i],
                )
                <= K
            ):
                ans += 1

else:
    ans = 0
    costs_from_start.sort()
    for goal in range(N):
        if K - costs_to_goal[goal] > 0:
            ans += bisect_right(costs_from_start, K - costs_to_goal[goal] - L)

print(ans)
