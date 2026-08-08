S = list(input())
N = len(S)

ans = 0
for start in range(N):
    for end in range(start + 1, N):
        test = S[start : end + 1]
        if all(test[i] != test[i + 1] for i in range(N - 1)):
            pass
