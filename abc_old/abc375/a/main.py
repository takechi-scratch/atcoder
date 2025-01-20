N = int(input())
S = input()

ans = 0
for i in range(1, N - 1):
    if S[i] == "." and S[i-1] == "#" and S[i+1] == "#":
        ans += 1

print(ans)
