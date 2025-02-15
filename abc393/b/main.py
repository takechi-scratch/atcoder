S = input()

ans = 0
for a in range(len(S)):
    if S[a] != "A":
        continue

    for b in range(a + 1, len(S)):
        if S[b] != "B":
            continue

        if b + b - a < len(S) and S[b + b - a] == "C":
            ans += 1

print(ans)
