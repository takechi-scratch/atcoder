# そのままやるだけ。はじめにtimeを小さくしておく。
N, C = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

ans = 0
time = -10 ** 18
for i in range(N):
    if T[i] - time >= C:
        ans += 1

        time = T[i]

print(ans)
