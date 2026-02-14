N = int(input())
A = [int(x) - 1 for x in input().split()]
ans = [None] * N

for start in range(N):
    if ans[start] is not None:
        continue

    route = [start]
    route_set = set([start])
    now = start
    while True:
        now = A[now]
        if now in route_set:
            break

        route.append(now)
        route_set.add(now)

    for x in route:
        ans[x] = now

print(*[x + 1 for x in ans])
