N, K, T = [int(x) for x in input().split()]
ans = 0
for _ in range(N):
    d, r = [int(x) for x in input().split()]
    if r >= K * d:
        ans += r

print("Yes" if ans >= T else "No")
