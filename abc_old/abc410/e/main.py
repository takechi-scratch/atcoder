N, H, M = [int(x) for x in input().split()]
monsters = []
for _ in range(N):
    monsters.append(tuple(int(x) for x in input().split()))

ans = 0
dp = [(0, 0) for _ in range(H + 1)]
for i in range(N):
    for j, x in enumerate(dp):
        if x[1] > M:
            ans = max(ans, x[0] - 1)
            dp[j] = (-1, -1)

    next_dp = [(x[0], x[1] + monsters[i][1]) for x in dp]
    for j in range(H + 1):
        now = dp[j]

        if now[0] == -1 or j + monsters[i][0] > H:
            continue

        hp = monsters[i][0]

        if now[0] + 1 > next_dp[j + hp][0]:
            next_dp[j + hp] = (now[0] + 1, now[1])
        elif now[0] + 1 == next_dp[j + hp][0] and now[1] + monsters[i][1] < next_dp[j][1]:
            next_dp[j + hp] = (now[0] + 1, now[1])

    dp = next_dp

for score, mp in dp:
    if mp <= M:
        ans = max(ans, score)

print(ans)
