from math import comb
from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

MOD = 998244353

@lru_cache(maxsize=None)
def mod_factorical(n: int, MOD: int = 998244353):
    """再帰の上限変更が必要"""
    assert n >= 0

    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * mod_factorical(n - 1, MOD) % MOD


@lru_cache(maxsize=None)
def mod_comb(n: int, k: int, MOD: int = 998244353):
    if n < k:
        return 0

    return mod_factorical(n, MOD) * pow(mod_factorical(k, MOD), -1, MOD) * pow(mod_factorical(n - k, MOD), -1, MOD) % MOD



# 未満
def solve(N: int, K: int):
    if K == 0:
        return 0, 1

    if N <= 0 or K <= 0 or N < 2 ** (K - 1):
        return 0, 0

    if N & (N - 1) == 0:
        highest_position = len(bin(N)) - 2
        each_counts = mod_comb(highest_position - 2, K - 1)

        return (N - 1) * each_counts % MOD, mod_comb(highest_position - 1, K)

    highest_position = len(bin(N)) - 2
    ans, before_count = solve(2 ** (highest_position - 1), K)
    left = N - 2 ** (highest_position - 1)

    now_ans, count = solve(left, K - 1)
    ans += now_ans + count * (2 ** (highest_position - 1) % MOD) % MOD
    ans %= MOD

    return ans, before_count + count



T = int(input())
for _ in range(T):
    N, K = [int(x) for x in input().split()]
    print(solve(N + 1, K)[0])
