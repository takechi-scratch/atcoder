# upsolve中。解説を読んでも理解と実装が難しい

from atcoder.segtree import SegTree
from bisect import bisect_left

N = int(input())
A = [int(x) for x in input().split()]

if N % 2 == 0:
    print(min(A[i + N // 2] - A[i] for i in range(N // 2)))
    exit()

dist_score: list[SegTree] = []
for dist in range((N - 3) // 2, (N - 3) // 2 + 4):
    st = SegTree(lambda x, y: min(x, y), 10**18, N - dist)
    for i in range(N - dist):
        st.set(i, A[i + dist] - A[i])

    dist_score.append(st)

ans = -1
for i in range(N - 1):
    for j in range(i + 1, N):
        k = bisect_left(A, A[j] + (A[j] - A[i]))
        if k >= N or A[k] - A[j] != A[j] - A[i]:
            continue

        def pair_pos(x):
            return x - (x >= i) - (x >= j) - (x >= k)

        def real_pos(x):
            return x + (x >= i) + (x >= j) + (x >= k)

        def p(x):
            px = pair_pos(x)
            if px >= (N - 3) // 2:
                return real_pos(px - (N - 3) // 2)
            else:
                return real_pos(px + (N - 3) // 2)

        def calc_dist(x):
            return abs(x - p(x))

        border = [0]
        if calc_dist(i) != calc_dist(i + 1):
            border.append(min(i + 1, p(i + 1)))

        if calc_dist(j) != calc_dist(j + 1):
            border.append(min(j + 1, p(j + 1)))

        if calc_dist(k) != calc_dist(k + 1):
            border.append(min(k + 1, p(k + 1)))

        border = list(sorted(set(border)))
        border.append(N)
        now_ans = 10**18
        for bi in range(len(border) - 1):
            now_ans = min(
                now_ans, dist_score[real_pos(calc_dist(border[bi])) - (N - 3) // 2].prod(border[bi], border[bi + 1])
            )

        ans = max(ans, now_ans)

print(ans)
