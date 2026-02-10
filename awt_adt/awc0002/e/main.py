N, S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A1 = A[: N // 2]
A2 = A[N // 2 :]


A1_count = {}
for select in range(1 << len(A1)):
    now_cost = sum(x for i, x in enumerate(A1) if select & 1 << i)
    if now_cost not in A1_count:
        A1_count[now_cost] = 1
    else:
        A1_count[now_cost] += 1


ans = 0
for select in range(1 << len(A2)):
    now_cost = sum(x for i, x in enumerate(A2) if select & 1 << i)
    if S - now_cost in A1_count:
        ans += A1_count[S - now_cost]

print(ans)
