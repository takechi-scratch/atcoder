# DP的な遷移
# 前々日から今日に飛ぶか、前日から今日に飛ぶかのどっちか、コストが低い方を取る
# 区間ごとにそれやってまとめられる？遅延セグ木？
# [前々日までのスコアの和] [前日までのスコアの和]
# 今日 -> 2つのminを取って、すべてに今日のスコアを足す


def solve(N: int, K: int, A: list[int]):
    start = 0
    now_ans = [A[0], A[0]]
    for i in range(1, K):
        now_ans.append(min(now_ans[-1], now_ans[-2]) + A[i])
    ans_1 = now_ans[-1]

    now_ans = [A[1], A[1]]
    for i in range(1, K):
        now_ans.append(min(now_ans[-1], now_ans[-2]) + A[i + 1])
    ans_2 = now_ans[-1]

    best_ans = min(ans_1, ans_2)
    while start + K <= N - 2:
        next_ans_1 = ans_2
        if ans_1 - A[start] == ans_2:
            next_ans_2 = ans_2 - A[start + 1] + A[start + K + 1]
        else:
            next_ans_2 = min(ans_1 - A[start] + A[start + K + 1], ans_2 - A[start + 1] + A[start + K + 1])

        best_ans = min(best_ans, next_ans_2)

        ans_1 = next_ans_1
        ans_2 = next_ans_2
        start += 1

    return best_ans


T = int(input())
for _ in range(T):
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    if N == 1 and K == 1:
        print(sum(A))
        continue

    ans = solve(N, K, A)
    if K + 1 <= N:
        ans = min(ans, solve(N, K + 1, A))
    print(ans)
