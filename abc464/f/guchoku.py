from itertools import permutations

N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
MOD = 998244353

fact = 1
for i in range(2, N + 1):
    fact *= i
    fact %= MOD

ans = 0
for turns in permutations(range(N), N):
    now = 0
    for x in turns:
        now += A[x]
        if now >= X:
            break

    ans += now * pow(fact, -1, MOD)
    ans %= MOD

print(ans)
