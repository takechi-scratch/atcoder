N, L = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]

if L % 3 != 0:
    print(0)
    exit()

point_counts = [0] * L
cur = 0
for d in D:
    point_counts[cur] += 1
    cur += d
    cur %= L
point_counts[cur] += 1

ans = 0
for start in range(L // 3):
    ans += point_counts[start] * point_counts[start + L // 3] * point_counts[start + L // 3 * 2]

print(ans)
