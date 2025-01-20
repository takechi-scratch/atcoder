import bisect

N = int(input())
X = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
Q = int(input())

# クエリは先に読み込んでおくのがベスト！！
query = []
for _ in range(Q):
    query.append([int(x) for x in input().split()])

# 累積和の計算。
now_sum = 0
P_sum = []
for i in range(N):
    now_sum += P[i]
    P_sum.append(now_sum)
    now_sum

for i in range(Q):
    left, right = query[i]

    # リストの二分探索はbisectを使うのが便利
    hiku_index = bisect.bisect_left(X, left)
    hikareru_index = bisect.bisect_right(X, right)

    # リストの-1番目を参照しないように、0にする
    if hiku_index == 0:
        hiku = 0
    else:
        hiku = P_sum[hiku_index - 1]

    # WAポイント！コーナーケースに注意。
    # この問題ではマイナスの番地もあるため、hikareru_indexが0になる可能性もある。
    # 片方にしていない実装などは要注意、WAが出たら見直し必須！！
    if hikareru_index == 0:
        hikareru = 0
    else:
        hikareru = P_sum[hikareru_index - 1]

    print(hikareru - hiku)
