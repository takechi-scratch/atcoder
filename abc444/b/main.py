N, K = [int(x) for x in input().split()]
ans = 0
for x in range(1, N + 1):
    if sum(int(y) for y in str(x)) == K:
        ans += 1

print(ans)
