# WAポイント！！平方根の計算は誤差あり！！
# 10**15程度以上になる場合は注意
# https://qiita.com/atti/items/bd71a87e998f84c987dc

# 整数でいい場合は、必ずisqrtを使うこと。

from math import log2, isqrt

N = int(input())

def solve(N):
    # aがそれほど大きくならないので全部チェック
    ans = 0
    for a in range(1, int(log2(N)) + 1):
        b_2_max = int(isqrt(N // (2 ** a)))
        # bが奇数の場合のみ数える
        # 偶数のときは2^aに全て預けても同じ表現ができる→重複
        ans += (b_2_max + 1) // 2

    return int(ans)

print(solve(N))
