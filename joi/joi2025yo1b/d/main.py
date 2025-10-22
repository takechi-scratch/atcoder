N = int(input())
A = [int(x) for x in input().split()]

for _ in range(N - 1):
    next_A = [A[i] + A[i + 1] for i in range(len(A) - 1)]
    print(*next_A)
    A = next_A
