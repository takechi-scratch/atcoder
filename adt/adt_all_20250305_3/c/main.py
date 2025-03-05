# https://atcoder.jp/contests/abc323/tasks/abc323_b

N = int(input())
A = [input() for _ in range(N)]

max_ans = -1
ans_i = -1
for i, x in enumerate(A):
    A[i] = (x.count("o") * -1, i + 1)

A.sort()
for i in range(N):
    print(A[i][1])
