# WAの乱択解法。
# 乱択するときは、少なめの計算量で繰り返せるようにするべき

from time import time
start = time()

from math import gcd
import random
from collections import defaultdict

class Lines:
    def __init__(self, a: int, b: int, c: int):
        abc_gcd = gcd(abs(a), abs(b), abs(c))
        if a < 0:
            a = -a
            b = -b
            c = -c

        if a == 0 and b < 0:
            b = -b
            c = -c

        self.a = a // abc_gcd
        self.b = b // abc_gcd
        self.c = c // abc_gcd

    def through_point(self, x: int, y: int):
        return self.a * x + self.b * y + self.c == 0

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __repr__(self):
        return f"Lines({self.a}, {self.b}, {self.c})"

N = int(input())
points = [tuple(int(x) for x in input().split()) for _ in range(N)]
checked = set()
lines = defaultdict(int)

while time() - start < 1.8:
    i, j = random.randrange(N), random.randrange(N)
    if i == j:
        continue
    if i > j:
        i, j = j, i

    if (i, j) in checked:
        continue

    checked.add((i, j))

    a1, b1 = points[i]
    a2, b2 = points[j]

    line = Lines(b2 - b1, -a2+a1, a2*b1-a1*b2)

    lines[(line.a, line.b, line.c)] += 1

best_line: Lines = None
best_score = -1
for line, score in lines.items():
    if score > best_score:
        best_line = line
        best_score = score

point_count = 0
best_line = Lines(*best_line)
for x, y in points:
    if best_line.through_point(x, y):
        point_count += 1

if point_count > N // 2:
    print("Yes")
    print(best_line.a, best_line.b, best_line.c)
else:
    print("No")
