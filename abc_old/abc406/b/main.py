N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = 1
for i in range(N):
    ans *= A[i]

    if ans >= 10 ** K:
        ans = 1

print(ans)
