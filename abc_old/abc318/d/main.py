# 直す！！

import sys
from itertools import combinations

sys.setrecursionlimit(10**7)

N = int(input())
cost = [[-1] * N for _ in range(N)]

for i in range(N - 1):
    d = [int(x) for x in input().split()]
    for j, x in enumerate(d):
        cost[i][j + i + 1] = x
        cost[j + i + 1][i] = x

ans = -1

def search(score, left: set):
    global ans

    if len(left) <= 1:
        return

    for u, v in combinations(left, 2):
        # 辞書での管理はダメかも
        now_score = score + cost[u][v]
        ans = max(ans, now_score)

        left.remove(u)
        left.remove(v)

        search(now_score, left)

        left.add(u)
        left.add(v)

    return


search(0, set(range(N)))
print(ans)
