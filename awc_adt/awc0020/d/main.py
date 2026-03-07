from collections import defaultdict

N, L = [int(x) for x in input().split()]
routers = [[int(x) for x in input().split()] for _ in range(N)]

events = defaultdict(int)
for x, r in routers:
    events[max(0, x - r)] += 1
    events[min(L + 1, x + r + 1)] -= 1

count = 0
before_place = -1
ok = True
for place, diff in sorted(events.items()):
    count += diff
    if place > L:
        break

    if count == 0 and place - before_place > 1:
        ok = False
        break

    before_place = place

print("Yes" if ok else "No")
