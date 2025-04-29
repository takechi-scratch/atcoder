N, M, Q = [int(x) for x in input().split()]
visibles = [set() for _ in range(N)]
all_visible = [False] * N

for _ in range(Q):
    query = [int(x) - 1 for x in input().split()]
    if query[0] == 0:
        visibles[query[1]].add(query[2])


    elif query[0] == 1:
        all_visible[query[1]] = True

    else:
        print("Yes" if query[2] in visibles[query[1]] or all_visible[query[1]] else "No")
