N, S, T = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print("Yes" if (T - S) * 60 >= sum(A) else "No")
