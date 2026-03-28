N = int(input())
P = [int(x) for x in input().split()]
W = [int(x) for x in input().split()]

dp = [[-(10**18)] * (2**N) for _ in range(N)]
for i in range(N):
    dp[0][2**i] = 0

for i in range(1, N):
    for status in range(2**N):
        now_score = -(10**18)

        for next_picture in range(N):
            if status & (1 << next_picture) != 0:
                continue
            now_score = dp[status]
