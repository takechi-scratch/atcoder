from itertools import permutations

N = int(input())
A = [int(x) for x in input().split()]

for P in permutations(range(1, N + 1), N):
    for i in range(N):
        if A[i] != -1 and P[i] != A[i]:
            break

    else:
        print("Yes")
        print(*P)
        exit()

print("No")
