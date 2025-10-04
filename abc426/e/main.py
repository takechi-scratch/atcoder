from math import gcd, sqrt


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cross_x(line1: "Lines", line2: "Lines"):
    if line1.a * line2.b - line2.a * line1.b == 0:
        return 10**18

    return (line1.b * line2.c - line2.b * line1.c) / (line1.a * line2.b - line2.a * line1.b)


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

    def get_y(self, x: int):
        return (self.c - self.a * x) / self.b

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __repr__(self):
        return f"Lines({self.a}, {self.b}, {self.c})"


def solve(TSx: int, TSy: int, TGx: int, TGy: int, ASx: int, ASy: int, AGx: int, AGy: int):
    Tline = Lines(TGy - TSy, -TGx + TSx, TGx * TSy - TSx * TGy)
    T_dist = dist(TSx, TSy, TGx, TGy)
    Aline = Lines(AGy - ASy, -AGx + ASx, AGx * ASy - ASx * AGy)
    A_dist = dist(ASx, ASy, AGx, AGy)
    ans = 10**18

    # 交点
    cx = cross_x(Tline, Aline)
    if min(TSx, TGx) <= cx <= max(TSx, TGx):
        cy = Tline.get_y(cx)
        cosx = sqrt(1 / (1 + ((AGy - ASy) / (AGx - ASx)) ** 2))
        if ASx > AGx:
            cosx *= -1

        cross_Ax = ASx + min(dist(TSx, TSy, cx, cy), A_dist) * cosx
        ans = min(ans, dist(cx, cy, cross_Ax, Aline.get_y(cross_Ax)))

        cy = Aline.get_y(cx)
        cosx = sqrt(1 / (1 + ((TGy - TSy) / (TGx - TSx)) ** 2))
        if TSx > TGx:
            cosx *= -1

        cross_Ax = TSx + min(dist(ASx, ASy, cx, cy), T_dist) * cosx
        ans = min(ans, dist(cx, cy, cross_Ax, Tline.get_y(cross_Ax)))

    # 始点・終点
    ans = min(ans, dist(TSx, TSy, ASx, ASy))
    # ans = min(ans, diff(TSx, TSy, AGx, AGy))
    # ans = min(ans, diff(TGx, TGy, ASx, ASy))
    ans = min(ans, dist(TGx, TGy, AGx, AGy))

    if T_dist <= A_dist:
        x0, y0 = TGx, TGy
        goal_base_x = ASx + (T_dist / A_dist) * (AGx - ASx)
        base_line = Aline
        base_Sx, base_Gx = ASx, AGx
    else:
        x0, y0 = AGx, AGy
        goal_base_x = TSx + (A_dist / T_dist) * (TGx - TSx)
        base_line = Tline
        base_Sx, base_Gx = TSx, TGx

    vert_line = Lines(base_line.b, -base_line.a, base_line.a * y0 - base_line.b * x0)

    cx = cross_x(base_line, vert_line)
    if min(base_Sx, goal_base_x) <= cx <= max(base_Sx, goal_base_x):
        goal_base_y = base_line.get_y(goal_base_x)
        ans = min(ans, dist(x0, y0, goal_base_x, goal_base_y))
    else:
        # 点と直線の距離
        pl_dist = abs(base_line.a * x0 + base_line.b * y0 + base_line.c) / sqrt(base_line.a**2 + base_line.b**2)
        ans = min(ans, pl_dist)

    return ans


T = int(input())
for _ in range(T):
    TSx, TSy, TGx, TGy = [int(x) for x in input().split()]
    ASx, ASy, AGx, AGy = [int(x) for x in input().split()]

    ans = solve(TSx, TSy, TGx, TGy, ASx, ASy, AGx, AGy)
    print(ans)
