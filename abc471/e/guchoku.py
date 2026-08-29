from itertools import combinations

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
MOD = 998244353

ans = 0
for x in combinations(range(N), K):
    ans += sum(A[i] for i in x) ** 2
    ans %= MOD

print(ans)
