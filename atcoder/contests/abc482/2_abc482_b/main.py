S = [list(input()) for _ in range(5)]

ans = min(x.count(".") for x in S)
for i in range(5):
    ans = min(ans, sum(S[j][i] == "." for j in range(5)))

ans = min(ans, sum(S[j][j] == "." for j in range(5)))
ans = min(ans, sum(S[j][4 - j] == "." for j in range(5)))

print(ans)
