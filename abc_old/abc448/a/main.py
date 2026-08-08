N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

for x in A:
    if x < X:
        print(1)
        X = x
    else:
        print(0)
