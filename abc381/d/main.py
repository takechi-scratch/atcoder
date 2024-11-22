# WA解答。尺取り法を勉強せよ！！！

from bisect import bisect_left

N = int(input())
A = [int(x) for x in input().split()]

ans = 0
pair_lists = []
pair = []
skip = False

# 2文字ずつ連続でできるものの個数を数える
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

pair_lists.append(pair)

for pair in pair_lists:
    temp_ans = 0

    now_list = []
    now_set = set(now_list)
    for i, x in enumerate(pair):
        if x in now_set:
            # WAポイント！2重ループを取り払うときに独自のやり方は間違える
            # より長くなる解答を見落としがちなので注意
            # 以下は誤答（と思っていたがいい線行ってるのか？）
            pos = bisect_left(now_list, x)
            temp_ans = max(temp_ans, i)
            now_list = now_list[pos + 1:]
            now_set = set(now_list)

        now_list.append(x)
        now_set.add(x)

    temp_ans = max(temp_ans, len(now_list))
    ans = max(temp_ans, ans)

print(ans * 2)

# 尺取り法
# 二重ループをなくすとき（O(N^2)からO(N)へ）
# かつ、範囲を考えるとき（部分文字列とか）

# 左端と右端を定め、区間の長さの最大を調べる。
# 左端を1増やしたとき、右は動かす必要がない！（最大値は単調増加だから）
