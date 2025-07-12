N, L, R = [int(x) for x in input().split()]
ans = 0
for _ in range(N):
    x, y = [int(x) for x in input().split()]
    if x <= L <= R <= y:
        ans += 1

print(ans)
