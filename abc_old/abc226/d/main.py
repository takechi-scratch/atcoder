# WAポイント！最大公約数、GCDの計算は案外軽い！！
from math import gcd

N = int(input())
towns = []
for _ in range(N):
    towns.append([int(x) for x in input().split()])

magics = set()
# 垂直・水平移動の時だけ特殊なので、処理を変える
used_particular = [False] * 4

for before in range(N):
    x1, y1 = towns[before]
    for after in range(N):
        x2, y2 = towns[after]
        dx, dy = x2 - x1, y2 - y1

        if before == after:
            continue

        if dx == 0:
            used_particular[(dy > 0)] = True
            continue

        if dy == 0:
            used_particular[2 + (dx > 0)] = True
            continue

        # 移動を最大で何回分に分けられるかがわかる
        move_gcd = gcd(dx, dy)
        magics.add((dx // move_gcd, dy // move_gcd))

print(len(magics) + sum(used_particular))
