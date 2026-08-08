N = int(input())
S = "x" + input() + "x"

ans = 0
for i in range(1, N + 1):
    if S[i] == "x" and S[i - 1] == "x" and S[i + 1] == "x":
        ans += 1

print(ans)
