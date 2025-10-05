# 解説AC。（まだできていない）
# 困難は分割せよ→同時に2点動いているときと、1点の移動が終わり残りの1点が動いているとき
# 同時に動くのはしんどいので、1点を固定し「点と直線の距離」を用いる

from math import sqrt


def get_dist(x1, y1, x2=0, y2=0):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def nearest_point_line(base_sx: int, base_sy: int, dx: int, dy: int, start: int, goal: int):
    dist = goal - start
    # WAポイント！ゼロ割りに気を付ける。
    # ベクトルの正規化で長さが0の時に注意。
    if dist <= 0 or get_dist(dx, dy) <= 0:
        return get_dist(base_sx, base_sy)

    dx, dy = dx / get_dist(dx, dy), dy / get_dist(dx, dy)

    # 三分探索
    # 極値を1つだけ持つ関数の最小値を求める！！
    while goal - start > 10**-12:
        mid1 = start + (goal - start) / 3

        check_x = base_sx + dx * (mid1 / dist) * dist
        check_y = base_sy + dy * (mid1 / dist) * dist
        dist1 = get_dist(check_x, check_y)

        mid2 = start + (goal - start) / 3 * 2
        check_x = base_sx + dx * (mid2 / dist) * dist
        check_y = base_sy + dy * (mid2 / dist) * dist
        dist2 = get_dist(check_x, check_y)

        if dist1 == dist2:
            break
        if dist1 < dist2:
            goal = mid2
        else:
            start = mid1

    mid = (start + goal) / 2
    check_x = base_sx + dx * (mid / dist) * dist
    check_y = base_sy + dy * (mid / dist) * dist
    return get_dist(check_x, check_y)


def solve(TSx: int, TSy: int, TGx: int, TGy: int, ASx: int, ASy: int, AGx: int, AGy: int):
    T_dist = get_dist(TSx, TSy, TGx, TGy)
    A_dist = get_dist(ASx, ASy, AGx, AGy)
    ans = 10**18

    if T_dist > A_dist:
        TSx, TSy, TGx, TGy, ASx, ASy, AGx, AGy = ASx, ASy, AGx, AGy, TSx, TSy, TGx, TGy
        T_dist, A_dist = A_dist, T_dist

    Tdx, Tdy = TGx - TSx, TGy - TSy
    Adx, Ady = AGx - ASx, AGy - ASy

    # Tの長さ分にAのdxdyを縮小させる！
    Adx, Ady = Adx * (T_dist / A_dist), Ady * (T_dist / A_dist)

    # ベクトルを引き算して、Tを固定する
    move_dx = Adx - Tdx
    move_dy = Ady - Tdy

    # Tをpointとして固定、Aをbaseに
    ans = min(ans, nearest_point_line(ASx - TSx, ASy - TSy, move_dx, move_dy, 0, get_dist(move_dx, move_dy)))
    # Tが終点にいるとき、Aをbaseに
    ans = min(ans, nearest_point_line(ASx - TGx, ASy - TGy, Adx, Ady, T_dist, A_dist))

    return ans


T = int(input())
for _ in range(T):
    TSx, TSy, TGx, TGy = [int(x) for x in input().split()]
    ASx, ASy, AGx, AGy = [int(x) for x in input().split()]

    ans = solve(TSx, TSy, TGx, TGy, ASx, ASy, AGx, AGy)
    print(f"{ans:.12f}")
