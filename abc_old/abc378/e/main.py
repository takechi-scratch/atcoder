# WA解答。modを出してから足し合わせないといけないのでこれではだめ。
# modを利用した累積和でやるといいらしい。

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = 0

for i in range(N):
    ans += (i + 1) * (N - i) * (A[i] % M)

# print(sum(A))
print(ans)
