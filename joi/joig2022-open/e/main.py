N = int(input())
M = int(input())
paintings = [[int(x) for x in input().split()] for _ in range(N)]

dp = [-(10**18)] * (M + 1)
dp[-1] = 0

best_i = -1
best_score = 0
second_i = -2
second_score = -(10**18)

for i, painting in enumerate(paintings):
    a, v = painting
    a -= 1
    dp[a] = max((best_score if best_i != a else second_score) + v, dp[a])

    # ベストの記録にイコールは必須！
    # より良い記録を2つ残しておく
    if dp[a] >= best_score:
        if a == best_i:
            best_score = dp[a]
            continue

        second_i = best_i
        second_score = best_score

        best_i = a
        best_score = dp[a]
    elif dp[a] >= second_score:
        second_i = a
        second_score = dp[a]


print(int(max(dp)))
