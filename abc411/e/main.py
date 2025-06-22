# 全てのサイコロがx(able_max)以下となる出目の場合の数は？
# これを累積和的に計算していき、差をとることで「最大値がx」の場合の数が分かる

from collections import defaultdict

MOD = 998244353

N = int(input())
DICE = [[int(x) for x in input().split()] for _ in range(N)]

all_min = 0
able_max = set()

# 高速化のポイント
# heapqやSortedListを使っている場合、dictやlistに置き換えられないかをチェック
# 「大きい方or小さい方から順に取り出す」で、その値があらかじめわかっている場合は置き換え可能
queue = defaultdict(list)
for i, x in enumerate(DICE):
    for y in x:
        able_max.add(y)

    for y in set(x):
        queue[y].append((y, i, x.count(y)))

    all_min = max(all_min, min(x))

# WAポイント！CPythonとPyPyの違い（滅多にないが）
# PyPyだとsetはsortされていない！
able_max = list(sorted(able_max))

# よく使う逆元はあらかじめとる
bunbo_INV = pow(pow(6, N, MOD), -1, MOD)
now_ok = [0] * N

for x in able_max:
    if x > all_min:
        break

    for count in queue[x]:
        now_ok[count[1]] += count[2]

bunsi = 1
for x in now_ok:
    bunsi *= x
    bunsi %= MOD

ans = bunsi * all_min * bunbo_INV % MOD
# beforeでひとつ前を記録
before_bunsi = bunsi

for now_max in able_max:
    if now_max <= all_min:
        continue

    for count in queue[now_max]:
        before_ok = now_ok[count[1]]
        # WAポイント！MODでの計算時には割り算をしない！！！！！！！
        # また、ゼロ割りにも注意
        bunsi = bunsi * pow(before_ok, -1, MOD) * (before_ok + count[2]) % MOD
        now_ok[count[1]] += count[2]

    ans += (bunsi - before_bunsi) * now_max * bunbo_INV % MOD
    before_bunsi = bunsi

assert pow(bunsi * bunbo_INV, -1, MOD) == 1
print(int(ans % MOD))
