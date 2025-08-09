from collections import defaultdict
from fractions import Fraction
from math import comb

N = int(input())
points = [tuple(int(x) for x in input().split()) for _ in range(N)]

lines = {}

for i in range(N):
    for j in range(N):
        if i >= j:
            continue

        if points[i][0] - points[j][0] == 0:
            katamuki = "infinity"
        else:
            frac = Fraction(points[i][1] - points[j][1], points[i][0] - points[j][0])
            katamuki = (frac.numerator, frac.denominator)

        dist = (points[i][1] - points[j][1]) ** 2 + (points[i][0] - points[j][0]) ** 2

        if katamuki is not lines.keys():
            lines[katamuki] = [0, defaultdict(int)]

        lines[katamuki][0] += 1
        lines[katamuki][1][dist] += 1

ans = 0
for key, value in lines.items():
    ans += comb(value[0], 2)

no = 0
for value in lines.values():
    for sames in value[1].values():
        no += comb(sames, 2)

print(ans - no // 2)
