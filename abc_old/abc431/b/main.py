X = int(input())
N = int(input())
W = [int(x) for x in input().split()]

wear = set()
Q = int(input())
for _ in range(Q):
    p = int(input()) - 1
    if p in wear:
        wear.discard(p)
        X -= W[p]
    else:
        wear.add(p)
        X += W[p]

    print(X)
