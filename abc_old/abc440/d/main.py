from bisect import bisect_left

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()

for _ in range(Q):
    x, y = [int(x) for x in input().split()]
    ok, ng = x + y - 2, 10 ** 18
    while ng - ok > 1:
        t = (ok + ng) // 2

        count = t - x + 1
        count -= bisect_left(A, t) - bisect_left(A, x)

        if count <= y:
            ok = t
        else:
            ng = t

    print(ok)
