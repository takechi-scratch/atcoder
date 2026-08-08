from collections import defaultdict

N = int(input())
A = [int(x) for x in input().split()]

ans = defaultdict(int)
for x in A:
    ans[x] = max(ans[x], ans[x - 1] + 1)

print(max(ans.values()))
