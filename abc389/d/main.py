# （半）解説AC的な。確認してから実装を始めました。

R = int(input())

# 先に円の中にあるかの関数を定義
def in_circle(x, y):
    return x ** 2 + y ** 2 <= R ** 2

max_x = R + 1

# 円の4分の1だけをシミュレート
quarter_ans = 0
for now_y in range(2, R + 1):
    # yを1上げて、円に入るxの最大を狭めていく
    # 「しゃくとり法」といって、実際には全体でyを1回上げてxを1回下げているだけなのでO(R)で嬉しい
    while not in_circle(now_y - 0.5, max_x - 0.5) and max_x > 0:
        max_x -= 1

    if max_x > 0:
        quarter_ans += max_x - 1

ans = quarter_ans * 4
# 中心でまたがっているものは一応別でカウント
ans += R * 4 - 3

print(ans)
