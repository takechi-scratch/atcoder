# 累積和をとる→leftを後ろから見て、OKなrightを足していく

from collections import defaultdict

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A_sum = [0]
for x in A:
    A_sum.append(A_sum[-1] + x)

ans = 0
appears = defaultdict(int)

# K=0の場合がある！
# 累積和が0の場合、自分自身を含めるとおかしなことになる
for i in range(N + 1):
    ans += appears[A_sum[N - i] + K]
    appears[A_sum[N - i]] += 1

print(ans)

# WAポイント！値が0になりうるときは注意！コーナーケースの1つ。
