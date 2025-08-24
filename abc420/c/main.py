N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ans = sum(min(A[i], B[i]) for i in range(N))

for _ in range(Q):
    c, x, v = input().split()
    x = int(x) - 1
    v = int(v)

    if c == "A":
        ans -= min(A[x], B[x])
        ans += min(v, B[x])
    elif c == "B":
        ans -= min(A[x], B[x])
        ans += min(A[x], v)

    if c == "A":
        A[x] = v
    else:
        B[x] = v

    print(ans)
