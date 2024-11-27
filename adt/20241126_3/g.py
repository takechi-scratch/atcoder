# https://atcoder.jp/contests/abc365/tasks/abc365_d
# やったことあるやつ。DP。

# テンプレコード（じゃんけん）
# 実装で散々手こずったのでこれを使いなさい！！！
def janken(me, you):
    if me == you:
        return 0

    if me == 0:
        return (you == 1) * 2 - 1
    elif me == 1:
        return (you == 2) * 2 - 1
    else:
        return (you == 0) * 2 - 1

assert janken(2, 1) == -1
assert janken(0, 1) == 1

N = int(input())
S = ["RSP".index(x) for x in list(input())]

dp = [[-10 ** 18] * 3 for _ in range(N)]

for i in range(N):
    for now_hand in range(3):
        if janken(now_hand, S[i]) == -1:
            continue

        if i == 0:
            dp[i][now_hand] = janken(now_hand, S[i])
            continue

        temp_ans = -10 ** 18
        for bef_hand in range(3):
            if now_hand == bef_hand:
                continue
            temp_ans = max(temp_ans, dp[i-1][bef_hand] + janken(now_hand, S[i]))

        dp[i][now_hand] = temp_ans

print(max(dp[-1]))
