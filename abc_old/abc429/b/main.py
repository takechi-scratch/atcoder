N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print("Yes" if sum(A) - M in A else "No")
