import heapq

N, K = [int(x) for x in input().split()]
phones = [[int(x) for x in input().split()] for _ in range(N)]
left_phone_days = [x[2] for x in phones]

ans = 0
events = []
for i, phone in enumerate(phones):
    heapq.heappush(events, (phone[0] - 1, 1, i))
    heapq.heappush(events, (phone[1], 2, i))
heapq.heappush(events, (K, -1, -1))

usable = []
ans = 0
before = 0
while len(events) > 0:
    day, event_type, event_i = heapq.heappop(events)
    left_days = day - before
    while left_days > 0 and len(usable) > 0:
        limit, i = heapq.heappop(usable)
        if day > limit:
            continue

        if left_days <= left_phone_days[i]:
            left_phone_days[i] -= left_days
            left_days = 0
            if left_phone_days[i] > 0:
                heapq.heappush(usable, (limit, i))
            break
        else:
            left_days -= left_phone_days[i]
            left_phone_days[i] = 0

    ans += (day - before) - left_days
    before = day
    if event_type == 1:
        heapq.heappush(usable, (phones[event_i][1], event_i))
    # else:
    #     usable.discard((phones[event_i][1], event_i))

print(ans)
