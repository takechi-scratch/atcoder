# 後日(ほぼ)自力AC。

N = int(input())
A = [int(x) for x in input().split()]

ans = 0
MOD = 998244353

for i in range(N):
    ans += A[i] * i
    ans %= MOD

multiple = 0

for i in range(N-1, -1, -1):
    ans += A[i] * multiple
    ans %= MOD
    multiple += 10 ** len(str(A[i]))
    multiple %= MOD

print(ans)
