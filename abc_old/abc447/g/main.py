N = int(input())
problems = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[] for _ in range(7)]
dp[-1] = [(0, [])]
for i in range(N):
    cur_K = problems[i][0]
    cur_A = problems[i][0]
    next_dp = []
    for j in range(6):
        now = dp[j - 1]
        candidates = []
        for now_score, used in now:
            if j <= 3:
                if cur_K in used:
                    continue
            else:
                if cur_K in used[2:]:
                    continue

            candidates.append((now_score + cur_A, used + [cur_K]))

        now = dp[j]

        no_i = 0
        yes_i = 0
        now_ans = []
        for _ in range(10):
            if no_i == len(now):
                while len(now_ans) < 10 and yes_i < len(candidates):
                    now_ans.append(candidates[yes_i])
                    yes_i += 1

            elif yes_i == len(candidates):
                while len(now_ans) < 10 and no_i < len(now):
                    now_ans.append(now[no_i])
                    no_i += 1

            elif now[no_i][0] <= candidates[yes_i][0]:
                now_ans.append(candidates[yes_i])
                yes_i += 1

            else:
                now_ans.append(now[no_i])
                no_i += 1

        next_dp.append(now_ans)

    dp = next_dp


print(max(x[0] for x in dp[5]))
