N = int(input())
A = [int(x) for x in input().split()]
A.sort(reverse=True)

print(sum(A[i] for i in range(N) if i % 2 == 0) - sum(A[i] for i in range(N) if i % 2 == 1))
