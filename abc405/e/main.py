import sys
sys.setrecursionlimit(10**9)

from functools import lru_cache


MOD = 998244353

A, B, C, D = [int(x) for x in input().split()]

factor = [1]
for i in range(1, A + B + C + D):
    factor.append(factor[-1] * i % MOD)
    inv_factor.append(pow(factor[-1], -1, MOD))
inv_factor = [None] * len(factor)

def mod_factorical(n: int):
    return factor[n]

@lru_cache(maxsize=None)
def mod_comb(n: int, k: int, MOD: int = 998244353):
    ans = mod_factorical(n) * inv_factor[k] % MOD
    ans = ans * inv_factor[n - k] % MOD
    return ans

ans = 0

for A_end in range(A, A + B + 1):
    first_B = A_end - A
    second_B = B - first_B
    first_area = mod_comb(A_end - 1, first_B)

    second_third = mod_factorical(second_B + C + D)
    second_third = second_third * inv_factor[second_B] % MOD
    second_third = second_third * inv_factor[C] % MOD
    second_third = second_third * inv_factor[D] % MOD

    second_third *= pow(mod_comb(second_B + D, D), -1, MOD)

    ans += first_area * second_third
    ans %= MOD

ans %= MOD
print(ans)
