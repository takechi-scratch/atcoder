N = int(input())
S = [list(input()) for _ in range(N)]

def changes(i: int):
    x = S[i]
    now = x.count(".")
    now_changes = []
    for i in range(N + 1):
        now_changes.append(now)
        if i == N:
            break
        if x[i] == "#":
            now += 1
        else:
            now -= 1

    return now_changes

dp = changes(N - 1)
for i in range(N - 2, -1, -1):
    next_dp = []
    before_min = 10 ** 18
    need_changes = changes(i)
    for j in range(N + 1):
        before_min = min(before_min, dp[j])
        next_dp.append(before_min + need_changes[j])

    dp = next_dp

print(min(dp))
