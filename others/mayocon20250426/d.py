H, N = [int(x) for x in input().split()]
magic = []
for _ in range(N):
    magic.append(tuple(int(x) for x in input().split()))

dp = [None] * H

for i in range(H):
    now_ans = 10 ** 18
    for a, b in magic:
        before = 0
        if i - a >= 0:
            before += dp[i - a]

        now_ans = min(now_ans, before + b)

    dp[i] = now_ans

print(dp[-1])
