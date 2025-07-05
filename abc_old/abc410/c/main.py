N, Q = [int(x) for x in input().split()]
A = [i + 1 for i in range(N)]
rotate_count = 0

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        A[(query[1] - 1 + rotate_count) % N] = query[2]

    elif query[0] == 2:
        print(A[(query[1] - 1 + rotate_count) % N])

    else:
        rotate_count += query[1]
