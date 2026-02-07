# 小数点誤差の解決方法がわからない…。

from bisect import bisect_left, bisect_right
from dataclasses import dataclass
from functools import cmp_to_key

EPS = 10 ** -8

@dataclass
class Pair:
    x: int
    y: int
    plus: int = 0

def shogen(a: Pair):
    if a.x > 0 and a.y >= 0:
        return 1 + a.plus * 4
    if a.x <= 0 and a.y > 0:
        return 2 + a.plus * 4
    if a.x < 0 and a.y <= 0:
        return 3 + a.plus * 4
    if a.x >= 0 and a.y < 0:
        return 4 + a.plus * 4

def compare(a: Pair, b: Pair):
    a_s = shogen(a)
    b_s = shogen(b)
    if a_s != b_s:
        return -1 if a_s < b_s else 1

    ans_reverse = (a_s % 2) * 2 - 1

    a_cp = abs(a.y) * abs(b.x)
    b_cp = abs(a.x) * abs(b.y)
    if a_cp == b_cp:
        return 0
    else:
        return -1 * ans_reverse if a_cp < b_cp else 1 * ans_reverse


N, Q = [int(x) for x in input().split()]
monsters = [[int(x) for x in input().split()] for _ in range(N)]
monster_args = []
monster_args_bs = []
for i, pos in enumerate(monsters):
    monster_args.append(Pair(pos[0], pos[1]))
    monster_args_bs.append(Pair(pos[0], pos[1]))
    monster_args_bs.append(Pair(pos[0], pos[1], 1))

monster_args_bs.sort(key=cmp_to_key(compare))

for _ in range(Q):
    a, b = [int(x) - 1 for x in input().split()]
    start, end = monster_args[a], monster_args[b]

    if compare(start, end) == -1:
        start = Pair(start.x, start.y, 1)

    right_i = bisect_right(monster_args_bs, cmp_to_key(compare)(start), key=cmp_to_key(compare))
    left_i = bisect_left(monster_args_bs, cmp_to_key(compare)(end), key=cmp_to_key(compare))

    print(right_i - left_i)
