from math import log2, ceil


def bisect_devide(N, M):
    if N < M:
        return 0

    base = 1 << ceil(log2(N / M))
    # print(base)

    return max(base - (base * M - N), base // 2)


def solve(N: int, M: int, A: list[int]):
    ok, ng = 1, max(A) + 1
    while ng - ok > 1:
        X = (ok + ng) // 2

        base = len([l for l in A if l >= X])
        add = 0
        for l in A:
            add += max(0, bisect_devide(l, X) - 1)

        add = min(add, M)

        if base + add > (N + M) // 2:
            ok = X
        else:
            ng = X

    return ok


T = int(input())
for _ in range(T):
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    print(solve(N, M, A))
