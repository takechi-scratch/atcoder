T, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

now = -(10**18)
for t in range(T + 1):
    if abs(now - A[t]) >= X:
        now = A[t]
        print(t, now)
