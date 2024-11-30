# https://atcoder.jp/contests/abc342/tasks/abc342_a

S = list(input())

for i in range(len(S)):
    if S.count(S[i]) == 1:
        print(i + 1)
        break
