S = [int(x) for x in list(input())]
N = len(S)
MOD = 998244353

positions = [[i for i in range(N) if S[i] == x] for x in range(10)]


factor = [1]
for i in range(1, 10**6):
    factor.append(factor[-1] * i % MOD)

# Codonは-1乗で逆元を計算できない
# MOD - 2乗と同値。MODを指定すれば同じ計算量でやってくれる（はず）
inv_factor = [pow(x, MOD - 2, MOD) for x in factor]


def mod_comb(n: int, k: int, MOD: int = 998244353):
    ans = factor[n] * inv_factor[k] % MOD
    ans = ans * inv_factor[n - k] % MOD
    return ans


def comb_cross_sum(a: int, b: int):
    return mod_comb(a + b - 1, b - 1)


ans = 0
for num in range(9):
    search_pos = positions[num] + positions[num + 1]
    search_pos.sort()
    sum_1 = len(positions[num])
    sum_2 = len(positions[num + 1])
    now_1 = 0
    now_2 = sum_2

    for i in search_pos:
        if S[i] == num:
            now_1 += 1
            if now_1 >= 1 and now_2 >= 1:
                ans += comb_cross_sum(now_1, now_2)
                ans %= MOD
        else:
            now_2 -= 1


print(ans)
