N, X = [int(x) for x in input().split()]
food = []
for _ in range(N):
    food.append([int(x) for x in input().split()])

dp = [[(0, 0, 0) for _ in range(X + 1)] for _ in range(N)]

for i in range(N):
    v, a, c = food[i]
    v -= 1

    for j in range(X + 1):
        before = dp[i - 1][j]
        if j - c >= 0:
            eat = dp[i - 1][j - c]
            eat[v] += a
        else:
            eat = (0, 0, 0)

        if min(before) < min(eat):
            dp[i][j] = eat
        elif min(before) > min(eat):
            dp[i][j] = before

        elif sum(before) < sum(eat):
            dp[i][j] = eat

        else:
            dp[i][j] = before

print(min(dp[-1][-1]))
