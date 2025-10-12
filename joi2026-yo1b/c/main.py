N = int(input())
S = input()

if N <= 2:
    print(0)
    exit()

ans = 0
for i in range(N - 2):
    if S[i : i + 3] in {"AOI", "IOI"}:
        ans += 1

print(ans)
