from collections import defaultdict
from math import comb, gcd

N = int(input())
points = [tuple(int(x) for x in input().split()) for _ in range(N)]

# dictの入れ子ではなく、キーをtupleにするとMLE・TLEのリスクが減る！
# 具体的には、line_lengthsはkeyをtuple(辺の向き, 辺の長さ)にしている
lines = {}
line_lengths = defaultdict(int)

for i in range(N):
    for j in range(N):
        if i >= j:
            continue

        if points[i][0] - points[j][0] == 0:
            katamuki = "infinity"
        else:
            dy, dx = points[i][1] - points[j][1], points[i][0] - points[j][0]
            if dx < 0:
                dx *= -1
                dy *= -1
            div = gcd(dx, dy)
            dx /= div
            dy /= div
            katamuki = (dx, dy)

        dist = (points[i][1] - points[j][1]) ** 2 + (points[i][0] - points[j][0]) ** 2

        if katamuki not in lines:
            lines[katamuki] = 0

        lines[katamuki] += 1
        line_lengths[(katamuki, dist)] += 1

ans = 0
for key, value in lines.items():
    ans += comb(value, 2)

no = 0
for value in line_lengths.values():
    no += comb(value, 2)

print(ans - no // 2)
