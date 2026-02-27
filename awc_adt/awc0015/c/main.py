from collections import defaultdict

N = int(input())
members = [[int(x) - 1 for x in input().split()] for _ in range(N)]

groups = [defaultdict(int) for _ in range(10**5)]
group_sum = [0] * (10**5)
for i, x in enumerate(members):
    groups[x[0]][x[1]] += 1
    group_sum[x[0]] += 1

ans = 0
for g in range(10**5):
    if group_sum[g] == 0:
        continue

    ans += (group_sum[g] - 1) * group_sum[g] // 2
    for _, value in groups[g].items():
        ans -= value * (value - 1) // 2

print(ans)
