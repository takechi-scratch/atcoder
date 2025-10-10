N, D = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A.sort()
print("Yes" if all(A[2 * i + 1] - A[2 * i] <= D for i in range(N)) else "No")
