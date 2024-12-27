# https://atcoder.jp/contests/abc255/tasks/abc255_a
R, C = [int(x) - 1 for x in input().split()]

A = [[int(x) for x in input().split()] for _ in range(2)]
print(A[R][C])
