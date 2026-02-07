P, Q = [int(x) for x in input().split()]
X, Y = [int(x) for x in input().split()]
print("Yes" if 0 <= X - P < 100 and 0 <= Y - Q < 100 else "No")
