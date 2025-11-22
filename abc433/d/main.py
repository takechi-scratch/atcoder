from collections import defaultdict

N, MOD = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

factor_mods = [defaultdict(int) for _ in range(15)]
for x in A:
    for factor in range(15):
        x %= MOD
        factor_mods[factor][x] += 1
        x *= 10

ans = 0
for x in A:
    factor = len(str(x))
    x %= MOD
    if x == 0:
        target = 0
    else:
        target = MOD - x

    ans += factor_mods[factor][target]

print(ans)
