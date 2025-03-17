# 正確な分数計算をするならDecimalが便利！
# ただし処理は遅めなので、使うなら（だいたい）B問題まで

from decimal import Decimal
N = int(input())
A = [int(x) for x in input().split()]

rate = Decimal(A[1]) / Decimal(A[0])
for i in range(2, N):
    if Decimal(A[i]) / Decimal(A[i - 1]) != rate:
        print("No")
        exit()

print("Yes")
