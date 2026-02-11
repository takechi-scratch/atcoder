N, K = [int(x) for x in input().split()]
ans = 0
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    if a * b >= K:
        ans += 1

print(ans)
