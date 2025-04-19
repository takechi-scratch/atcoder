from itertools import permutations

N, X = [int(x) for x in input().split()]
problems = []
for _ in range(N):
    problems.append([int(x) for x in input().split()])
    problems[-1][2] /= 100

ans = 0
for priority in permutations(range(N), N):
    dp = [[0] * (N + 1) for _ in range(X + 1)]
    dp[0][0] = 1
    for now_x in range(1, X + 1):
        for now_ok in range(N + 1):
            if now_ok < N:
                dp[now_x][now_ok] += dp[now_x - 1][now_ok] * (1 - problems[priority[now_ok]][2])
            if now_ok > 0 and problems[priority[now_ok - 1]][1] <= now_x:
                dp[now_x][now_ok] += dp[now_x - problems[priority[now_ok - 1]][1]][now_ok - 1] * problems[priority[now_ok - 1]][2]

    current_point = 0
    for i in range(N):
        current_point += problems[priority[i]][0]
        ans = max(ans, current_point * dp[-1][i + 1])

print(ans)
