def get_xy(num: int):
    return num // N, num % N


def get_dist(n1, n2):
    x1, y1 = get_xy(n1)
    x2, y2 = get_xy(n2)
    return abs(x1 - x2) + abs(y1 - y2)


N, M = [int(x) for x in input().split()]
S, T = [int(x) - 1 for x in input().split()]

P = [S]
if M > 0:
    P += [int(x) - 1 for x in input().split()]

M += 1
dp = [[10**18] * M for _ in range(1 << M)]
dp[0][0] = 0

for states in range(1, 1 << M):
    for now_n in range(M):
        now_ans = 10**18
        for reduce in range(M):
            if states & (1 << reduce) == 0:
                continue
            now_ans = min(now_ans, dp[states - (1 << reduce)][reduce] + get_dist(P[reduce], P[now_n]))

        dp[states][now_n] = now_ans

print(min(x + get_dist(P[i], T) for i, x in enumerate(dp[-1])))
