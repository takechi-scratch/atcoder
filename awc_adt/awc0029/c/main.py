N = int(input())
A = [int(x) for x in input().split()]
A.sort()
print(A[-1] + A[-2])
