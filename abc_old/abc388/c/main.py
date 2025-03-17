from bisect import bisect_left

N = int(input())
A = [int(x) for x in input().split()]

ans = 0
for i in range(N):
    # 二分探索が便利！各餅ごとにギリギリ土台にできる餅を見つけて、それより大きい餅はぜんぶOK
    position = bisect_left(A, A[i] * 2)
    ans += N - position

print(ans)
