S = input()
ans = 0
for start in range(len(S)):
    if S[start] != "t":
        continue

    now_t = 1
    i = start + 1
    while i < len(S):
        if S[i] == "t":
            now_t += 1

        if i - start == 1:
            i += 1
            continue

        if S[i] == "t":
            ans = max(ans, (now_t - 2) / (i - start - 1))

        i += 1

print(ans)
