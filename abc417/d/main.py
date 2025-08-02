# 謎の1TLE

from bisect import bisect_right
from functools import lru_cache
import sys
sys.setrecursionlimit(10**7)


N = int(input())
gifts = [tuple(int(x) for x in input().split()) for _ in range(N)]

@lru_cache(maxsize=None)
def solve(finished: int, now_point: int):
    if finished >= N:
        return now_point

    if now_point <= gifts[finished][0]:
        now_point += gifts[finished][1]
    else:
        now_point -= gifts[finished][2]
        now_point = max(now_point, 0)

    return solve(finished + 1, now_point)

down_points_sum = [0]
for x in gifts:
    down_points_sum.append(down_points_sum[-1] + x[2])

Q = int(input())
for _ in range(Q):
    X = int(input())
    if X <= 1000:
        print(solve(0, X))
        continue

    downs = bisect_right(down_points_sum, X - 1000)
    if downs >= len(down_points_sum):
        print(X - down_points_sum[-1])
        continue

    now_point = X - down_points_sum[downs]
    print(solve(downs, now_point))
