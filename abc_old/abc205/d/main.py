from bisect import bisect_left
import sys
input = sys.stdin.readline

N, Q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A_modified = [A[i] - i - 1 for i in range(N)]
"""「何番目までの整数がこの区間に入るか」"""

ans = []

for _ in range(Q):
    k = int(input())
    available = bisect_left(A_modified, k)
    if available < N:
        # 区間の右端から必要な分だけずらす
        ans.append(A[available] - (A_modified[available] - k) - 1)
    else:
        # AがすべてKより左側にいるのでその分を増やせばOK
        ans.append(k + N)

print(*ans, sep="\n")
