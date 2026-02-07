N, K, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()
sake = A[:K]

now = 0
for i, x in enumerate(reversed(A[:K])):
    now += x
    if now >= X:
        print((N - K) + i + 1)
        break

else:
    print(-1)
