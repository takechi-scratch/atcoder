N = int(input())
happies = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[-10 ** 18] * 3 for _ in range(N + 1)]
dp[0] = [0, 0, 0]

for i in range(1, N + 1):
    for today_do in range(3):
        max_pts = -10 ** 18
        for yesterday_do in range(3):
            if yesterday_do == today_do:
                continue
            max_pts = max(max_pts, dp[i-1][yesterday_do] + happies[i - 1][today_do])
        dp[i][today_do] = max_pts

print(max(dp[-1]))
