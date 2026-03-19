N, Q = [int(x) for x in input().split()]
V = [int(x) for x in input().split()]

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        x, y = query[1] - 1, query[2] - 1
        V[y] += V[x]
        V[x] = 0
    else:
        print(V[query[1] - 1])
