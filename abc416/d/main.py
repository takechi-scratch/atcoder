from sortedcontainers import SortedList

def solve(N: int, M: int, A: list[int], B: list[int]):
    ans = sum(A) + sum(B)
    A.sort()
    B = SortedList(B)
    for x in reversed(A):
        b_index = B.bisect_left(M - x)
        if b_index >= len(B):
            continue
        ans -= M
        del B[b_index]

    return ans


T = int(input())
for _ in range(T):
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    ans = solve(N, M, A, B)
    print(ans)
