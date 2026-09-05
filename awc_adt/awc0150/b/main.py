N = int(input())
A = [int(input()) for _ in range(N)]
ans = 1
for x in A:
    ans *= x

print(ans)
