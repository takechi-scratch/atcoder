# 未完
# SortedSetとMax更新のセグ木だけでも行ける気がする

from sortedcontainers import SortedSet
from atcoder.segtree import SegTree

import sys
input = sys.stdin.readline

N, Q = [int(x) for x in input().split()]
S = list(input().strip("\n"))

def op(a, b):
    return min(a, b)


starts = SortedSet()
seg = SegTree(max, 0, N)

start = -1
for i in range(N):
    if start == -1:
        start = i
        continue

    if S[start] == S[i]:
        starts.add(start)
        continue
    else:
        seg.set(start, i - start)
        start = i

for _ in range(Q):
    query = input().strip("\n").split()
    if query[0] == "1":
        i, x = int(query[1]) - 1, query[2]
        now_kukan = starts[starts.bisect_left(i)]
        starts.discard(now_kukan)
        starts


    else:
        l, r = int(query[1]) - 1, int(query[2])







# 両端だけ管理する
# SortedSetにスタート位置と、
