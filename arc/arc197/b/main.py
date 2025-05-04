# WA解答（ロジックミス）

def solve(N: int, A: list[int]):
    A.sort()
    min_ans, max_ans = 1, N

    A_sum = [A[0]]
    for x in A[1:]:
        A_sum.append(A_sum[-1] + x)

    while max_ans - min_ans > 1:
        mid = (min_ans + max_ans) // 2
        reachable = False

        right_sum = A_sum[-1] - A_sum[N - mid - 1]
        for left_gets in range(N - reachable):
            average = (A_sum[left_gets] + right_sum) / (left_gets + 1 + mid)
            if average < A[N - mid - 1]:
                reachable = True

        if reachable:
            min_ans = mid
        else:
            max_ans = mid

    return min_ans


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    print(solve(N, A))
