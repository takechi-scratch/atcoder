def solve(N: int, K: int, L: int, A: list[int]):
    A.sort()
    dists = [A[i + 1] - A[i] for i in range(N - 1)]
    dists.sort(reverse=True)
    left = A[0]
    right = L - A[-1]

    now_ans = 0
    best_ans = max(left, right) + (left + right) * (K - 1)
    for d in dists:
        now_score = d // 2
        if K <= 0:
            break

        now_ans += now_score
        K -= 1
        left += now_score
        right += now_score
        best_ans = max(best_ans, now_ans + max(left, right) + (left + right) * (K - 1))

    return max(best_ans, now_ans)


T = int(input())
for _ in range(T):
    N, K, L = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    print(solve(N, K, L, A))
