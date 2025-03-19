# https://atcoder.jp/contests/abc330/tasks/abc330_b

N, L, R = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = []
for i in range(N):
    if L <= A[i] <= R:
        ans.append(str(A[i]))

    elif A[i] < L:
        ans.append(str(L))

    else:
        ans.append(str(R))

print(*ans)
