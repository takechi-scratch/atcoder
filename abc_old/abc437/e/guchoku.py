N = int(input())

A = [([], 0)]

for i in range(1, N + 1):
    x, y = [int(x) for x in input().split()]
    A.append((A[x][0].copy() + [y], i))

A.sort()
print(*[x[1] for x in A][1:])
