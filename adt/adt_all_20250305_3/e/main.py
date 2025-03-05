# https://atcoder.jp/contests/abc275/tasks/abc275_c

from itertools import permutations

pones_x = []
pones_y = []
for i in range(9):
    for j, x in enumerate(input()):
        if x == "#":
            pones_x.append(i)
            pones_y.append(j)

ans = 0
for comb in permutations(range(len(pones_x)), 4):
    x1, y1 = pones_x[comb[0]], pones_y[comb[0]]
    x2, y2 = pones_x[comb[1]], pones_y[comb[1]]
    x3, y3 = pones_x[comb[2]], pones_y[comb[2]]
    x4, y4 = pones_x[comb[3]], pones_y[comb[3]]
    if (x1 - x2) * (x2 - x3) != (y1 - y2) * (y2 - y3) * -1:
        continue

    dist_2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if (x3 - x2) ** 2 + (y3 - y2) ** 2 != dist_2:
        continue

    if (x3 - x4) ** 2 + (y3 - y4) ** 2 != dist_2:
        continue

    if (x4 - x1) ** 2 + (y4 - y1) ** 2 != dist_2:
        continue

    ans += 1
    # print((x1, y1), (x2, y2), (x3, y3), (x4, y4))

print(ans // (4 * 2))
