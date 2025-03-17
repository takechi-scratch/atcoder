# 全てのパターンを試すだけ。

A, B, C = [int(x) for x in input().split()]
if A * B == C or B * C == A or C * A == B:
    print("Yes")
else:
    print("No")
