# https://atcoder.jp/contests/abc329/tasks/abc329_b
N = int(input())
A = [int(x) for x in input().split()]

# 降順にソートして前から見ていく
A.sort(reverse=True)
A_max = A[0]
for i, x in enumerate(A):
    if x != A_max:
        print(x)
        break
