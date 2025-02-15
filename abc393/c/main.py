N, M = [int(x) for x in input().split()]
ans = set()

for _ in range(M):
    u, v = [int(x) for x in input().split()]
    if u != v:
        ans.add((u, v))
        ans.add((v, u))

print(M - len(ans) // 2)
