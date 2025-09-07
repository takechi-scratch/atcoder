def solve(A: int, B: int, C: int) -> int:
    # 決め打ちにぶたん。AとCを確保し、かつ合計の文字数が足りていればOK
    ok, ng = 0, 10 ** 18
    while ng - ok > 1:
        test = (ok + ng) // 2
        if A >= test and C >= test and A + B + C >= test * 3:
            ok = test
        else:
            ng = test

    return ok


T = int(input())
for _ in range(T):
    A, B, C = [int(x) for x in input().split()]
    print(solve(A, B, C))
