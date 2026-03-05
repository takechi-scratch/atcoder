N, K = [int(x) for x in input().split()]
ans = 0
for _ in range(N):
    ans += input().count("!") >= K

print(ans)
