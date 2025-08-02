# とちゅう

from sortedcontainers import SortedList

def solve(N: int, M: int, A: list[int], B: list[int]):
    A.sort()
    B = SortedList(B)
    for x in reversed(A):
        b_index = B.bisect_right(x)
        if
    return True




T = int(input())
for _ in range(T):
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    ans = solve(N, A)
    if ans in {True, False}:
        print("Yes" if ans else "No")
    else:
        print(ans)
