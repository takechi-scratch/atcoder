N = int(input())
P = [int(x) for x in input().split()]

yt = [0, 0]

for i in range(1, N - 1):
    if P[i - 1] < P[i] > P[i + 1]:
        yt.append(i)

    elif P[i - 1] > P[i] < P[i + 1]:
        if len(yt) == 2:
            yt.append(-1)

        yt.append(i)

for _ in range(2):
    yt.append(N - 1)

ans = 0

for pos in range(0, len(yt), 2):
    if yt[pos] <= 0 or yt[pos] >= N - 1 or pos >= len(yt) - 1:
        continue

    ans += (yt[pos] - yt[pos - 1]) * (yt[pos + 2] - yt[pos + 1])

print(ans)
