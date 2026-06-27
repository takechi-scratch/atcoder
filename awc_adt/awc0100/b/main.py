N = int(input())
A = [sum([int(x) for x in input().split()]) for _ in range(N)]
print(A.index(max(A)) + 1)
