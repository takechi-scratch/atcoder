X, Y, Z = [int(x) for x in input().split()]

if abs(X) < abs(Y) or X * Y < 0:
    print(abs(X))
elif abs(Y) < abs(Z) and Y * Z > 0:
    print(-1)
elif Y * Z > 0:
    print(abs(X))
else:
    print(2 * abs(Z) + abs(X))
