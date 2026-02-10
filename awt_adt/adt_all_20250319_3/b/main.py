# https://atcoder.jp/contests/abc300/tasks/abc300_a

N, A, B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
print(C.index(A + B) + 1)
