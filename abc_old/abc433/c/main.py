S = [int(x) for x in list(input())]
N = len(S)

target = [-1]
for i in range(N - 1):
    if S[i + 1] - S[i] == 1:
        target.append(i)

target.append(N - 1)

ans = 0
for i, start in enumerate(target):
    if start == -1 or start == N - 1:
        continue

    width = 0
    start_num = S[start]
    while True:
        if start - width <= target[i - 1]:
            break

        if start + width + 1 >= target[i + 1] + 1:
            break

        if S[start - width] != start_num:
            break

        if S[start + width + 1] - S[start - width] == 1:
            ans += 1
        else:
            break

        width += 1

print(ans)
