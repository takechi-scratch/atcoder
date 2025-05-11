# MODをとる操作・逆元の計算は遅い！！！
# 定数倍が遅いのは、やはりPythonの弱み
# 実行時間 1999ms / 2000ms

import sys
sys.setrecursionlimit(10**9)

from functools import lru_cache


MOD = 998244353

A, B, C, D = [int(x) for x in input().split()]

# lru_cacheを過信しすぎない。
# 手作業で前計算するのもあり
factor = [1]
inv_factor = {}
for i in range(1, max(A + B, B + C + D) + 100):
    factor.append(factor[-1] * i % MOD)

def calc_inv_factor(n: int):
    if n in inv_factor:
        return inv_factor[n]

    res = pow(factor[n], -1, MOD)
    inv_factor[n] = res
    return res

def mod_factorical(n: int):
    return factor[n]

@lru_cache(maxsize=None)
def mod_comb(n: int, k: int, MOD: int = 998244353):
    ans = factor[n] * calc_inv_factor(k) % MOD
    ans = ans * calc_inv_factor(n - k) % MOD
    return ans

ans = 0

# A（リンゴ）の一番右の位置を決める
for A_end in range(A, A + B + 1):
    first_B = A_end - A
    second_B = B - first_B
    # A_endより左に来て良いのはAとBだけ
    first_area = mod_comb(A_end - 1, first_B)

    # A_endより右側で、残りのB・C・Dを並べる場合の数
    second_third = factor[second_B + C + D]
    second_third = second_third * calc_inv_factor(second_B) % MOD
    second_third = second_third * calc_inv_factor(C) % MOD
    second_third = second_third * calc_inv_factor(D) % MOD

    # BはDより右側に来てはいけないので、
    # BとDを並べる場合の数で割る（OKなのはその中の1通りしかないため）
    second_third *= calc_inv_factor(second_B + D) * factor[second_B] * factor[D] % MOD

    ans += first_area * second_third
    ans %= MOD

ans %= MOD
print(ans)
