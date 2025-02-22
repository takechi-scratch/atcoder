S = list(input())
w_count = 0

for i, x in enumerate(S):
    if x == "W":
        w_count += 1
    elif x == "A" and w_count > 0:
        S[i - w_count] = "A"
        for j in range(i - w_count + 1, i + 1):
            S[j] = "C"
        w_count = 0
    else:
        w_count = 0

print("".join(S))
