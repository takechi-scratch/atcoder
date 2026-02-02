N = int(input())
P = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

if all(x == 1 for x in P):
    if N == 2:
        print(min(C[0] * 2, C[1]))
    else:
        C.sort()
        print(C[0] * 2)

elif all(x == i + 1 for i, x in enumerate(P)):
    print(min(x * (N - i) for i, x in enumerate(C)))

else:
    raise RuntimeError
