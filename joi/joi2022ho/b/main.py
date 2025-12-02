N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


# オーバーフロー（64bitで扱える最大値を超えないよう）注意
# Pythonなら動かせはするが、実行時間が遅くなる（たしか）
def judge(test: int):
    def ceil(x: int, y: int) -> int:
        return -(-x // y)

    can_self_study = 0
    need_self_study = 0

    for x, y in zip(A, B):
        if x > y:
            if test > x * M:
                need_self_study += ceil((test - x * M), y)
            else:
                can_self_study += M - ceil(test, x)
        else:
            need_self_study += ceil(test, y) - M

        # なくてもいい
        if need_self_study > N * M:
            return False

    return can_self_study >= need_self_study


ok, ng = 0, 2 * 10**18
while ng - ok > 1:
    test = (ng - ok) // 2 + ok
    if judge(test):
        ok = test
    else:
        ng = test

print(ok)
