N = int(input())
S = [input().lower() for _ in range(N)]
ans = 0
for x in S:
    ans = max(ans, S.count(x))

print(ans)
