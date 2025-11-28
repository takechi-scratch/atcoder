import heapq

N, M, K = [int(x) for x in input().split()]
assert K == 0
sides = [[] for _ in range(N)]
times = [[] for _ in range(N)]
costs = [[] for _ in range(N)]
for _ in range(M):
    a, b, l, c = [int(x) for x in input().split()]
    sides[a - 1].append(b - 1)
    times[a - 1].append(l)
    costs[a - 1].append(c)

dks = [(0, 0)]
need_costs = [10**18] * N
need_costs[0] = 0
while len(dks) > 0:
    now_cost, now = heapq.heappop(dks)
    for next_node, cost in zip(sides[now], costs[now]):
        if now_cost + cost < need_costs[next_node]:
            need_costs[next_node] = now_cost + cost
            heapq.heappush(dks, (now_cost + cost, next_node))

if need_costs[N - 1] == 10**18:
    print(-1)
else:
    print(need_costs[N - 1])
