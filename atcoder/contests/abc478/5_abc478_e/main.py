N, Q = [int(x) for x in input().split()]
le_sides = [[] for _ in range(N)]
lt_sides = [[] for _ in range(N)]

start_cands = set(range(N))
for _ in range(Q):
    t, u, v = [int(x) for x in input().split()]
    if u == v:
        if t == 1:
            print("No")
            exit()
        continue

    if t == 0:
        le_sides[v - 1].append(u - 1)
    else:
        lt_sides[v - 1].append(u - 1)

    start_cands.discard(u - 1)

if len(start_cands) == 0:
    start_cands = {min(i for i in range(N) if len(le_sides[i]) > 0 or len(lt_sides[i]) > 0)}

existable_max = [10**18] * N
for start in start_cands:
    if existable_max[start] < 10**18:
        continue

    existable_max[start] = N
    dfs = [(start, N)]
    while len(dfs) > 0:
        now, now_max = dfs.pop()
        if now_max > existable_max[now]:
            continue

        for next_node in le_sides[now]:
            if existable_max[next_node] <= existable_max[now]:
                continue
            existable_max[next_node] = existable_max[now]
            if existable_max[next_node] <= 0:
                print("No")
                exit()

            dfs.append((next_node, existable_max[next_node]))

        for next_node in lt_sides[now]:
            if existable_max[next_node] <= existable_max[now] - 1:
                continue
            existable_max[next_node] = existable_max[now] - 1
            if existable_max[next_node] <= 0:
                print("No")
                exit()

            dfs.append((next_node, existable_max[next_node]))

# assert all(1 <= x <= N for x in existable_max)
for i in range(N):
    if existable_max[i] == 10**18:
        existable_max[i] = N
print("Yes")
print(*existable_max)
