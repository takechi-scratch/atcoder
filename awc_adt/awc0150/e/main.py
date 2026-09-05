N, Q, T = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A_sum = [0]
for x in A:
    A_sum.append(A_sum[-1] + x)

for _ in range(Q):
    l, r = [int(x) for x in input().split()]
    print("Yes" if A_sum[r] - A_sum[l - 1] > T else "No")
