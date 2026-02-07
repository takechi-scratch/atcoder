N, Q = [int(x) for x in input().split()]
A = [int(x) - 1 for x in input().split()]

dp = [[(i + 1, A[i]) for i in range(N)]]
for _ in range(35):
    next_dp = []
    for i in range(N):
        move_1 = dp[-1][i]
        move_2 = dp[-1][move_1[1]]
        next_dp.append((move_1[0] + move_2[0], move_2[1]))

    dp.append(next_dp)

for _ in range(Q):
    t, b = [int(x) for x in input().split()]
    b -= 1
    move_bin = bin(t)[2:]
    ans = 0
    for i, x in enumerate(reversed(move_bin)):
        if x == "0":
            continue
        move = dp[i][b]
        ans += move[0]
        b = move[1]

    print(ans)
