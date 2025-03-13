# 決め打ち二分探索、忘れがち

from bisect import bisect_left, bisect_right

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A.sort()

for _ in range(Q):
    b, k = [int(x) for x in input().split()]

    # 長さ以内でk個を制覇できるか
    # ngのほうが小さい（0スタート）に注意
    ng, ok = 0, 10 ** 18
    while ok - ng > 1:
        mid = (ok + ng) // 2

        left = bisect_left(A, b - mid)
        right = bisect_right(A, b + mid)

        if right - left >= k:
            ok = mid
        else:
            ng = mid

    # -1して最終確認（シンプルなやり方が思いつかない...）
    mid = ok - 1

    left = bisect_left(A, b - mid)
    right = bisect_right(A, b + mid)

    if right - left >= k:
        print(mid)
    else:
        print(ok)

    # print(ok)
