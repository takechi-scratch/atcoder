from collections import defaultdict

N = int(input())
dice: list[defaultdict] = []
dice_mens = []
for _ in range(N):
    die = defaultdict(int)
    input_die = [int(x) for x in input().split()]
    dice_mens.append(input_die[0])
    for i in range(1, len(input_die)):
        # 各数字が何面あるかを記録
        die[input_die[i]] += 1

    dice.append(die)

ans = 0
for p in range(N):
    for q in range(p):
        d1, d2 = dice[p], dice[q]
        # WAポイント！和集合と共通部分を正しく選ぶ。
        # 和集合にしたらTLEになりました
        search_number = set(d1.keys()) & set(d2.keys())

        next_ans = 0
        for i in search_number:
            # どちらもその数字が出る確率を足していく
            next_ans += d1[i] * d2[i] / dice_mens[q] / dice_mens[p]

        ans = max(ans, next_ans)

print(ans)
