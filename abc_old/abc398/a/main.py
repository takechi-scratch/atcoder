N = int(input())
ans = ["-"] * N
if N % 2 == 0:
    ans[N // 2 - 1] = "="
    ans[N // 2] = "="
else:
    ans[N // 2] = "="

print(*ans, sep="")
