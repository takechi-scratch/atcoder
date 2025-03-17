# WA解答
# 嘘解法をずっと試していたっぽい。

from sortedcontainers import SortedList

N = int(input())
now_mochis = SortedList([int(x) for x in input().split()])

# now_mochis = SortedList([int(x) for x in input().split()])
# N = len(now_mochis)
# print("テスト用です")

ans = 0
for i in range(N - 1, -1, -1):
    pair_mochi = now_mochis.bisect_left(now_mochis[i] * 2)
    if pair_mochi <= i or len(now_mochis) <= pair_mochi:
        continue

    now_mochis.pop(pair_mochi)
    now_mochis.pop(i)

    ans += 1

print(ans)
