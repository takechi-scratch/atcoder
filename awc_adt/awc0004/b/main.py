N, T = [int(x) for x in input().split()]
ans = 0
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    ans += max(0, a - b * T)

print(ans)
