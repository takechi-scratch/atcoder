S = input()
ans = 1

for i, now in enumerate(S):
    if i >= len(S) - 1:
        continue

    now = int(now)
    next_num = int(S[i + 1])

    ans += (now - next_num) % 10

    ans += 1

ans += int(S[-1])
print(ans)
