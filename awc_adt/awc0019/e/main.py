# 解説AC。キーをとってソートする&「箱を好感しても同じだから～」の議論は、
# 見たことはあったけど思いつくのは難しそうだなぁ…。

import heapq

N = int(input())
luggages = [[int(x) for x in input().split()] for _ in range(N)]

luggages.sort(key=sum)
ok_l = []
now_W = 0
for x in luggages:
    heapq.heappush(ok_l, -x[0])
    now_limit = sum(x)
    now_W += x[0]
    while now_limit < now_W and len(ok_l) > 0:
        now_W += heapq.heappop(ok_l)

print(len(ok_l))
