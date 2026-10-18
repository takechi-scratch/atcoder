# 整数範囲で切り上げを行う（標準のmath.ceilでは浮動点小数による誤差が発生する）


def ceil_div(N: int, M: int):
    return (N + M - 1) // M


if __name__ == "__main__":
    import random
    import math

    for _ in range(3):
        N, M = random.randint(1, 200), random.randint(2, 10)
        print(f"{N = }, {M = }")
        print(f"{ceil_div(N, M)   = }")
        print(f"{math.ceil(N / M) = }\n")

    for _ in range(3):
        N, M = random.randint(10**16, 10**18), random.randint(2, 10)
        print(f"{N = }, {M = }")
        print(f"{ceil_div(N, M)   = }")
        print(f"{math.ceil(N / M) = }\n")
