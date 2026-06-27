N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]
print(sum(x * y for x, y in A))
