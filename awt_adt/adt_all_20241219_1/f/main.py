# https://atcoder.jp/contests/abc370/tasks/abc370_c
# 前やったことあるやつ

S = list(input())
T = list(input())
X = []

for i in range(len(S)):
    if S[i] > T[i]:
        S[i] = T[i]
        X.append("".join(S))

for i in range(len(S) - 1, -1, -1):
    if S[i] < T[i]:
        S[i] = T[i]
        X.append("".join(S))

print(len(X))
if len(X) > 0:
    print("\n".join(X))
