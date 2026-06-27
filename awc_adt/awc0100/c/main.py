N, L, Q = [int(x) for x in input().split()]
A = [input() for _ in range(N)]

for _ in range(Q):
    C = [int(x) - 1 for x in input().split()][1:]
    operations = ["0"] * L
    for x in C:
        for i, y in enumerate(A[x]):
            if operations[i] == "0" and y == "1":
                operations[i] = "1"

    print("".join(operations))
