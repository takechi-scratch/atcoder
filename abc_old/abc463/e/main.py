import heapq

N, M, Y = [int(x) for x in input().split()]
sides = [[] for _ in range(N + 1)]
costs = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, t = [int(x) for x in input().split()]
    sides[u - 1].append(v - 1)
    sides[v - 1].append(u - 1)
    costs[u - 1].append(t)
    costs[v - 1].append(t)
X = [int(x) for x in input().split()]
for i, x in enumerate(X):
    sides[i].append(N)
    sides[N].append(i)
    costs[i].append(X[i] + Y)
    costs[N].append(X[i])

min_costs = [10**18] * (N + 1)
min_costs[0] = 0

queue = [(0, 0)]
while len(queue) > 0:
    now_cost, now = heapq.heappop(queue)
    if now_cost > min_costs[now]:
        continue

    for next_side, next_cost in zip(sides[now], costs[now]):
        if min_costs[next_side] < now_cost + next_cost:
            continue
        min_costs[next_side] = now_cost + next_cost
        heapq.heappush(queue, (now_cost + next_cost, next_side))

print(*min_costs[1:N])
