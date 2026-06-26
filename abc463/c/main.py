from collections import defaultdict
from bisect import bisect_right

N = int(input())
takahashis = [[int(x) for x in input().split()] for _ in range(N)]
takahashi_talls = defaultdict(int)
for h, l in takahashis:
    takahashi_talls[h] = max(takahashi_talls[h], l)

takahashis = [x for x in takahashis if x[1] == takahashi_talls[x[0]]]


times = [0]
tallests = []
for h, l in sorted(takahashis, key=lambda x: x[0], reverse=True):
    if l <= times[-1]:
        continue
    times.append(l)
    tallests.append(h)


Q = int(input())
T = [int(x) for x in input().split()]
for t in T:
    print(tallests[bisect_right(times, t) - 1])
