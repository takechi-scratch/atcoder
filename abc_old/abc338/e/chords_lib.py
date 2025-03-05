# 弦の長さを求めるテンプレコード（結局使わなかった）

N = int(input())
Nodes = 2 * N

def chord_dist(a, b):
    return min(abs(a - b), Nodes - abs(a - b))


def facing_chord_dist(a, b, is_right: bool):
    if a == b:
        return 0

    if a < b:
        return abs(a - b) if is_right else Nodes - abs(a - b)
    else:
        return Nodes - abs(a - b) if is_right else abs(a - b)
