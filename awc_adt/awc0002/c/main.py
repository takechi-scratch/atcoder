from math import ceil

n, k = [int(x) for x in input().split()]
ans = 0
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    ans = max(ans, ceil((k - a) / b))
print(ans)
