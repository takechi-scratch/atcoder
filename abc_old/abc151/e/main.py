# 実際に小さい数でシミュレーションしてみると解法が見つかることが多い

from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()

ans = 0
MOD = 10 ** 9 + 7


# テンプレコード、階乗・組み合わせのMOD
# 標準のmath.combだと(10**9)!とかで流石にTLEするので、自作するのがいい感じ？
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
    return mod_factorical(n, MOD) * pow(mod_factorical(k, MOD), -1, MOD) * pow(mod_factorical(n - k, MOD), -1, MOD) % MOD


# N - 1, K - 1, -1
for i in range(N - K + 1):
    n = N - i - 1
    ans -= A[i] * mod_comb(n, K - 1, MOD)
    ans += A[-1 - i] * mod_comb(n, K - 1, MOD)
    ans %= MOD

print(ans)
