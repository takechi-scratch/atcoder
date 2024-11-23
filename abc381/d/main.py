# WA解答。尺取り法を勉強せよ！！！

from bisect import bisect_left

N = int(input())
A = [int(x) for x in input().split()]

ans = 0
pair_lists = []
pair = []
skip = False

# 2文字ずつ連続でできるものをリストに出す
# WAポイントかも？2
for i in range(1, N):
    if skip:
        skip = False
        continue

    if A[i] == A[i-1]:
        pair.append(A[i])
        skip = True
    else:
        if len(pair) > 0:
            pair_lists.append(pair)
        pair = []

        # 本番、これ忘れた
        if i >= 2 and A[i-1] == A[i-2]:
            pair.append(A[i-1])

if len(pair) > 0:
    pair_lists.append(pair)


for pair in pair_lists:
    now_list = []
    now_set = set(now_list)

    # WAポイントかも？1 しゃくとり法に近いことをしてるけど、何かがおかしいか
    for i, x in enumerate(pair):
        # 重複しない最大の長さを更新
        ans = max(ans, len(now_list))
        if x in now_set:
            # 既存の位置を調べて、そこより前は切り落とす
            pos = bisect_left(now_list, x)
            now_list = now_list[pos + 1:]
            now_set = set(now_list)

        now_list.append(x)
        now_set.add(x)

    ans = max(ans, len(now_list))

print(ans * 2)

# 尺取り法
# 二重ループをなくすとき（O(N^2)からO(N)へ）
# かつ、範囲を考えるとき（部分文字列とか）

# 左端と右端を定め、区間の長さの最大を調べる。
# 左端を1増やしたとき、右は動かす必要がない！（最大値は単調増加だから）
