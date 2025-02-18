# 今入っている値の最大値・最小値を求めるためにSortedSetを使えば早い
# C++のstd::setと同じ

from collections import defaultdict
from sortedcontainers import SortedSet

Q = int(input())
S = defaultdict(int)
S_set = SortedSet()

for _ in range(Q):
    query = [int(x) for x in input().split()]

    if query[0] == 1:
        x = query[1]
        S_set.add(x)

        S[x] += 1

    elif query[0] == 2:
        x, c = query[1:]
        if S[x] > c:
            S[x] -= c

        else:
            S[x] = 0
            S_set.discard(x)

    elif query[0] == 3:
        print(S_set[-1] - S_set[0])

    else:
        raise RuntimeError
