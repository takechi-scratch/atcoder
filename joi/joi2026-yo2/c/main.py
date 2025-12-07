N = int(input())
S = list(input())

ans = []
j_count = 0
i = 0
while i < N:
    x = S[i]

    if x == "J":
        j_count += 1
        i += 1

    elif i + 1 < N and S[i] == "O" and S[i + 1] == "I":
        ans.extend(["O", "I"])
        i += 2

    else:
        ans.extend(["J"] * j_count + [x])
        j_count = 0
        i += 1

print("".join(ans + ["J"] * j_count))
