from sortedcontainers import SortedList

N, L, R = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A_sum = [0]
for x in A:
    A_sum.append(A_sum[-1] + x)

ans = 0
SA = SortedList([0])
for x in A_sum[1:]:
    ans += SA.bisect_left(x - L + 1) - SA.bisect_left(x - R)
    SA.add(x)

print(ans)
