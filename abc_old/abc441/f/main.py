import sys

sys.setrecursionlimit(10**7)

N, M = [int(x) for x in input().split()]
items = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M + 1):
        if j - items[i][0] >= 0:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - items[i][0]] + items[i][1])
        else:
            dp[i + 1][j] = dp[i][j]

must_buy = [False] * N
must_not_buy = [False] * N

memo = [[None] * (M + 1) for _ in range(N + 1)]
for j in range(M + 1):
    memo[0][j] = True

def get_id(i, j):
    return i * (M + 1) + j

def dfs(i: int, j: int):
    if memo[i][j] is not None:
        return memo[i][j]

    ok_buy = False
    ok_not_buy = False
    if j - items[i - 1][0] >= 0:
        if dp[i][j] - dp[i - 1][j - items[i - 1][0]] <= items[i - 1][1]:
            ok_buy = dfs(i - 1, j - items[i - 1][0])

    if dp[i][j] - dp[i - 1][j] == 0:
        ok_not_buy = dfs(i - 1, j)

    if ok_buy:
        must_buy[i - 1] = True
    if ok_not_buy:
        must_not_buy[i - 1] = True

    memo[i][j] = ok_buy or ok_not_buy
    return ok_buy or ok_not_buy

dfs(N, M)

ans = []
for i in range(N):
    if must_buy[i] and not must_not_buy[i]:
        ans.append("A")
    elif must_not_buy[i] and not must_buy[i]:
        ans.append("C")
    else:
        ans.append("B")

print("".join(ans))
