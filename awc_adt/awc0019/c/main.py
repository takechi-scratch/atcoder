N = int(input())
A = [int(x) for x in input().split()]

A.sort()
print(len([x for x in range(N - 1) if A[x + 1] - A[x] != 1]) + 1)
