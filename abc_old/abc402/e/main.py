# 期待値DPとビットDPの組み合わせ
# 期待値をDPで計算する復習が必要

N, X = [int(x) for x in input().split()]
problems = []
for _ in range(N):
    problems.append([int(x) for x in input().split()])

dp = [[-1] * (2 ** N) for _ in range(X + 1)]
dp[0][0] = 0
ans = 0  # 随時更新
for cur_x in range(X + 1):
    for cur_raw_solved in range(2 ** N):
        cur_solved = list(bin(cur_raw_solved)[2:])
        cur_solved = ["0"] * (N - len(cur_solved)) + cur_solved
        # 和ではなく最大をとること
        # nowから遷移を伸ばすのではなく、
        # どこからの遷移でnowに来るかを考えるとわかりやすくなる
        max_ans = 0
        for next_solve in range(N):
            if cur_solved[next_solve] == "0":
                continue

            before_x = cur_x - problems[next_solve][1]

            if before_x < 0 or dp[before_x][cur_raw_solved] < 0:
                continue

            now_ans = 0
            now_ans += dp[before_x][cur_raw_solved] * (100 - problems[next_solve][2]) / 100

            # 解いた場合
            cur_solved[next_solve] = "0"
            if dp[before_x][int("".join(cur_solved), 2)] >= 0:
                now_ans += (dp[before_x][int("".join(cur_solved), 2)] + problems[next_solve][0]) * problems[next_solve][2] / 100

            cur_solved[next_solve] = "1"

            max_ans = max(max_ans, now_ans)

        dp[cur_x][cur_raw_solved] = max_ans
        ans = max(ans, dp[cur_x][cur_raw_solved])

print(ans)
