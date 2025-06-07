N = int(input())
A = [int(x) for x in input().split()]
A = list(sorted(set(A)))
print(len(A))
print(*A)
