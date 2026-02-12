from bisect import bisect_left

N = int(input())
A = [int(x) for x in input().split()]

A.sort()

ans = 0
for i in range(N):
    ans += N - bisect_left(A, A[i] * 2)

print(ans)
