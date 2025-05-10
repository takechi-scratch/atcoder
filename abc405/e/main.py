import sys
sys.setrecursionlimit(10**9)

from functools import lru_cache


MOD = 998244353

A, B, C, D = [int(x) for x in input().split()]
N = A + B + C + D

factor = [1]
for i in range(1, A + B + C + D):
    factor.append(factor[-1] * i % MOD)

def mod_factorical(n: int, MOD: int = 998244353):
    return factor[n]

@lru_cache(maxsize=None)
def mod_comb(n: int, k: int, MOD: int = 998244353):
    ans = mod_factorical(n, MOD) * pow(mod_factorical(k, MOD), -1, MOD) % MOD
    ans = ans * pow(mod_factorical(n - k, MOD), -1, MOD) % MOD
    return ans

ans = 0

for A_end in range(A, A + B + 1):
    first_B = A_end - A
    second_B = B - first_B
    first_area = mod_comb(A_end - 1, first_B)

    second_third = mod_factorical(second_B + C + D)
    second_third *= pow(mod_factorical(second_B) * mod_factorical(C) % MOD * mod_factorical(D) % MOD * mod_comb(second_B + D, D) % MOD, -1, MOD)

    ans += first_area * second_third
    ans %= MOD

ans %= MOD
print(ans)
