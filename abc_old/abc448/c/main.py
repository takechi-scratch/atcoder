N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A_sorted = [(x, i) for i, x in enumerate(A)]
A_sorted.sort()

for _ in range(Q):
    K = int(input())
    B = set(int(x) - 1 for x in input().split())
    for i in range(6):
        if A_sorted[i][1] not in B:
            print(A_sorted[i][0])
            break
