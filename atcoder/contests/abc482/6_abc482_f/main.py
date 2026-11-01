from math import isqrt

N, M = [int(x) for x in input().split()]

divisors = [x for x in range(1, isqrt(N) + 10) if N % x == 0]
divisors = set(divisors + [N // x for x in divisors if N % x == 0])

ans = [10**18] * M
for x in divisors:
    x %= M
    for t in range(1, M + 2):
        ans[x] = min(ans[x], t)

        x *= x
        x %= M

print(*[x if x < 10**18 else -1 for x in ans], sep="\n")
