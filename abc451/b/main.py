N, M = [int(x) for x in input().split()]
ans = [0] * M
for _ in range(N):
    a, b = [int(x) - 1 for x in input().split()]
    ans[a] -= 1
    ans[b] += 1

print(*ans, sep="\n")
