def solve(N: int, S: list[str], X: list[int], Y: list[int]):
    dp = [[-(10**18)] * 2 for _ in range(N)]
    # 雨0, 晴れ1
    dp[0] = [0, 0]
    if S[0] == "S":
        dp[0][0] = -X[0]
    else:
        dp[0][1] = -X[0]

    for i in range(1, N):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = max(dp[i - 1][0] + Y[i - 1], dp[i - 1][1])

        if S[i] == "S":
            dp[i][0] -= X[i]
        else:
            dp[i][1] -= X[i]

    return max(dp[-1])


T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    X = [int(x) for x in input().split()]
    Y = [int(x) for x in input().split()]
    print(solve(N, S, X, Y))
