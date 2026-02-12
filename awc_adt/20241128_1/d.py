# https://atcoder.jp/contests/abc224/tasks/abc224_b

from itertools import combinations

H, W = [int(x) for x in input().split()]
A = []
for _ in range(H):
    A.append([int(x) for x in input().split()])

def solve():
    for i1, i2 in combinations(range(H), 2):
        i1, i2 = min(i1, i2), max(i2, i1)
        for j1, j2 in combinations(range(W), 2):
            j1, j2 = min(j1, j2), max(j1, j2)
            if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                print("No")
                return

    print("Yes")

solve()
