import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

H, W = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
Q = int(input())

is_monotone = all(X[i] < X[i + 1] for i in range(W - 1))
X_set = set(X)

for _ in range(Q):
    a, b = [int(x) for x in input().split()]
    if a + 1 == b:
        if a in X_set or b in X_set:
            print(1)
        else:
            print(2)
    elif is_monotone:
        print(b - a + 1 - (bisect_right(X, b) - bisect_left(X, a)))
    else:
        break
