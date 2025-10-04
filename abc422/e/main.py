# 解説ACの乱択解法。
# 乱択するときは、少なめの計算量で繰り返せるようにするべき

from time import time

start = time()

from math import gcd
import random


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

tests = 0
while time() - start < 1.8:
    # ランダムに直線を1つ決めて、「それが答えである」かどうか検証
    i, j = random.randrange(N), random.randrange(N)
    if i == j:
        continue
    if i > j:
        i, j = j, i

    a1, b1 = points[i]
    a2, b2 = points[j]

    line = Lines(b2 - b1, -a2 + a1, a2 * b1 - a1 * b2)

    point_count = 0
    for x, y in points:
        if line.through_point(x, y):
            point_count += 1

    if point_count > N // 2:
        print("Yes")
        print(line.a, line.b, line.c)
        break

    tests += 1

else:
    # print(tests)
    print("No")
