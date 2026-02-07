N, MOD = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = 0
for i in range(N):
    for j in range(N):
        if int(str(A[i]) + str(A[j])) % MOD == 0:
            ans += 1
            print(A[i], A[j])

print(ans)
