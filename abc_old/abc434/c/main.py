def solve(N: int, H: int, targets: list[list[int]]):
    T = 0
    high_h = H
    low_h = H
    for next_t, l, r in targets:
        high_h += next_t - T
        high_h = min(high_h, r)

        low_h -= next_t - T
        low_h = max(low_h, l)

        if high_h < l or low_h > r:
            return False

        T = next_t

    return True


T = int(input())
for _ in range(T):
    N, H = [int(x) for x in input().split()]
    targets = [[int(x) for x in input().split()] for _ in range(N)]
    print("Yes" if solve(N, H, targets) else "No")
