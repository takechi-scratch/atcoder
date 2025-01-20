from collections import defaultdict

N, C = [int(x) for x in input().split()]
start = defaultdict(list)
end = defaultdict(list)
happen_dates = set()

for _ in range(N):
    a, b, c = [int(x) for x in input().split()]
    start[a - 1].append(c)
    end[b].append(c)
    happen_dates.add(a - 1)
    happen_dates.add(b)

happen_dates = list(sorted(happen_dates))
ans = 0
now_price = 0

for i in range(len(happen_dates)):
    if i > 0:
        ans += min(C, now_price) * (happen_dates[i] - happen_dates[i - 1])

    date = happen_dates[i]
    for s in start[date]:
        now_price += s

    for e in end[date]:
        now_price -= e

print(ans)
