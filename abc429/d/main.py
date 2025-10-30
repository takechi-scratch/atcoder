from collections import Counter

N, M, C = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A_count = Counter(A)
positions = list(sorted(A_count.keys()))
peoples = [A_count[x] for x in positions]

ans = 0
goal = 0
now_x = 0
for i, start in enumerate(positions):
    if len(positions) == 1:
        times = M
    else:
        times = (start - positions[i - 1]) % M
    while now_x < C:
        now_x += peoples[goal % len(positions)]
        goal += 1
    ans += now_x * times
    now_x -= peoples[i]

print(ans)
