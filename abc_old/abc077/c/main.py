# Bを決めて、そこからCがいくつ選べるか→二分探索
# それを累積させる
# Aを決めて、Bがどこ以上になるか→Bを二分探索して、上の累積から値をとる

from bisect import bisect_right

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

B.sort()
C.sort()

B_sum = [0]
for x in reversed(B):
    B_sum.append(B_sum[-1] + N - bisect_right(C, x))

B_sum.reverse()

ans = 0
for x in A:
    ans += B_sum[bisect_right(B, x)]

print(ans)
