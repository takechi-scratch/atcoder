N, K = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]

# ヒント、こういうコーナーケースを書くとバグを見落としがち
# if len(X) <= 1:
#     print(abs(X[0]))
#     exit()

ans = 10 ** 18
# WAポイント！範囲指定時の添え字に注意。
# +1をつけるようにすること。
for left in range(N - K + 1):
    right = left + K - 1
    max_dis = X[right] - X[left]
    ans = min(ans, max_dis + min(abs(X[right]), abs(X[left])))

print(ans)
