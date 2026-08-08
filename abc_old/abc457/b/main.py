N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]
X, Y = [int(x) for x in input().split()]
print(A[X - 1][Y])
