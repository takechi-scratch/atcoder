N, M = [int(x) for x in input().split()]
W = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

dp = [False] * (2**N)
dp[0] = True
for capacity in C:  # M回
    next_dp = dp
    now_capacity = [0] * (2**N)
    for i in range(2**N):  # 2^N回
        if dp[i] is True:
            continue

        now_ans = 10**18
        for reduce in range(N):  # N回
            if (1 << reduce) & i == 0:
                continue

            now_ans = min(now_ans, now_capacity[i - (1 << reduce)] + W[reduce])

        now_capacity[i] = now_ans
        if now_ans <= capacity:
            next_dp[i] = True

    dp = next_dp

print("Yes" if dp[-1] else "No")
