N, Q = [int(x) for x in input().split()]
P = [int(x) - 1 for x in input().split()]
P2 = [-1] * N
for i, x in enumerate(P):
    P2[x] = i

for _ in range(Q):
    query = [int(x) - 1 for x in input().split()]
    if query[0] == 0:
        x, y = query[1:]
        P[x], P[y] = P[y], P[x]
        P2[P[x]], P2[P[y]] = P2[P[y]], P2[P[x]]
    else:
        P, P2 = P2, P

print(*[x + 1 for x in P])
