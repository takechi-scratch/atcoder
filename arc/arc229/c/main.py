def solve():
    N = int(input())
    A = [int(x) for x in input().split()]

    A.sort()
    print(sum(x // 2 for x in A[:2]) + sum(x // 2 * 2 for x in A[2:]))


T = int(input())
for _ in range(T):
    solve()
