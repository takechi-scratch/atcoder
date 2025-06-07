# Ai, Bi が100以下であるのがポイント
# SiがBi個分と、TiがAi個分の処理能力はどちらもAi*Biで同じ
# Aiの個数、Biの個数でそれぞれ決め打って探索できる

N, X = [int(x) for x in input().split()]
machines = []
for _ in range(N):
    machines.append(tuple(int(x) for x in input().split()))

ok, ng = 0, 10 ** 18
while ng - ok > 1:
    test_ans = (ok + ng) // 2
    price = 0

    for i, machine in enumerate(machines):
        # A, P, B, Q
        min_price = 10 ** 18
        for a in range(machine[2] + 1):
            # WAポイント！マイナスになるとおかしな動作を起こす
            b = (test_ans - a * machine[0] - 1) // machine[2] + 1
            min_price = min(min_price, a * machine[1] + max(0, b * machine[3]))

        for b in range(machine[0] + 1):
            a = (test_ans - b * machine[2] - 1) // machine[0] + 1
            min_price = min(min_price, max(0, a * machine[1]) + b * machine[3])

        price += min_price

    if price > X:
        ng = test_ans
    else:
        ok = test_ans

print(ok)
