import heapq

N, M = [int(x) for x in input().split()]
cars = [[int(x) for x in input().split()] for _ in range(M)]

events = [[] for _ in range(N)]
for i, x in enumerate(cars):
    l, r = x
    events[l - 1].append((0, i))
    events[r - 1].append((1, i))

ok = [False] * M

hq = []
for i in range(N):
    for event_type, event_j in events[i]:
        if event_type == 0:
            heapq.heappush(hq, (cars[event_j][1], event_j))

    if len(hq) > 0:
        _, park_j = heapq.heappop(hq)
        ok[park_j] = True

    co = True
    for event_type, event_j in events[i]:
        if event_type == 1 and not ok[event_j]:
            co = False
            break

    if not co:
        print("No")
        break

else:
    print("Yes")
