N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
rotated = 0

A_sum = [0]
for x in A:
    A_sum.append(A_sum[-1] + x)

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        rotated += query[1]
    else:
        l, r = query[1] + rotated, query[2] + rotated
        sub = (l - 1) // N
        l -= sub * N
        r -= sub * N

        ans = 0
        ans += A_sum[min(N, r)] - A_sum[l - 1]
        ans += A_sum[max(r - N, 0)]
        print(ans)
