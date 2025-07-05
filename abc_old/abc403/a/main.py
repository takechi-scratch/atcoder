N = int(input())
A = [int(x) for x in input().split()]

print(sum([A[i] for i in range(N) if i % 2 == 0]))
