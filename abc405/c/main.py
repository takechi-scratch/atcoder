N = int(input())
A = [int(x) for x in input().split()]

print((sum(A) ** 2 - sum([x ** 2 for x in A])) // 2)
