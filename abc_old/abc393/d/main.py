N = int(input())
S = list(input())

# sum_1を1多くする
pos_1, pos_1_sum = [], []
for i in range(N):
    if S[i] == "1":
        pos_1.append(i)
        if len(pos_1_sum) == 0:
            pos_1_sum.append(i)
        else:
            pos_1_sum.append(pos_1_sum[-1] + i)

def right(i):
    center = pos_1[i]
    right_ans = pos_1_sum[-1] - pos_1_sum[i]

    rights = len(pos_1) - i - 1
    right_ans -= rights * center
    right_ans -= rights * (rights + 1) // 2

    return right_ans, rights

def left(i):
    center = pos_1[i]
    lefts = i
    left_ans = center * lefts
    if left_ans > 0:
        left_ans -= pos_1_sum[i - 1]
        left_ans -= lefts * (lefts + 1) // 2

    return left_ans, lefts

# WAポイント！！！初期値は解法を見直したら必ず確認すること！！
# pythonの場合は常に10**60でも問題ないはず。
ans = 10 ** 60  # ←これ（N * 2にしてたらバグった）
left_i, right_i = 0, 0
for i in range(pos_1[0], min(N, pos_1[-1] + 1)):
    if left_i + 1 < len(pos_1) and pos_1[left_i + 1] <= i:
        left_i += 1
    if pos_1[right_i] < i:
        right_i += 1

    if left_i == right_i:
        ans = min(ans, left(left_i)[0] + right(right_i)[0])
        continue

    now_ans = 0

    left_ans, lefts = left(left_i)
    now_ans += left_ans + (lefts + 1) * (i - pos_1[left_i] - 1)

    right_ans, rights = right(right_i)
    now_ans += right_ans + (rights + 1) * (pos_1[right_i] - i)

    ans = min(ans, now_ans)

print(ans)
