N, X = [int(x) for x in input().split()]
problems = []
for _ in range(N):
    problems.append([int(x) for x in input().split()])

dp = [[-1] * (2 ** N) for _ in range(X + 1)]
dp[0][0] = 0
ans = 0  # 随時更新
for cur_x in range(X + 1):
    for cur_raw_solved in range(2 ** N):
        if dp[cur_x][cur_raw_solved] < 0:
            continue

        ans = max(ans, dp[cur_x][cur_raw_solved])

        cur_solved = list(bin(cur_raw_solved)[2:])
        cur_solved = ["0"] * (N - len(cur_solved)) + cur_solved
        for next_solve in range(N):
            if cur_solved[next_solve] == "1":
                continue

            if cur_x + problems[next_solve][1] > X:
                continue

            if dp[cur_x + problems[next_solve][1]][cur_raw_solved] < 0:
                dp[cur_x + problems[next_solve][1]][cur_raw_solved] = 0
            dp[cur_x + problems[next_solve][1]][cur_raw_solved] += dp[cur_x][cur_raw_solved] * (100 - problems[next_solve][2]) / 100

            # 解いた場合
            cur_solved[next_solve] = "1"

            if dp[cur_x + problems[next_solve][1]][int("".join(cur_solved), 2)] < 0:
                dp[cur_x + problems[next_solve][1]][int("".join(cur_solved), 2)] = 0
            dp[cur_x + problems[next_solve][1]][int("".join(cur_solved), 2)] += (dp[cur_x][cur_raw_solved] + problems[next_solve][0]) * problems[next_solve][2] / 100

            cur_solved[next_solve] = "0"

print(ans)
