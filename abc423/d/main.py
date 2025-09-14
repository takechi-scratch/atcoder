from collections import deque
import heapq

N, K = [int(x) for x in input().split()]
kyaku = [tuple(int(x) for x in input().split()) for _ in range(N)]

lines = deque()
events = []

for i, x in enumerate(kyaku):
    heapq.heappush(events, (x[0], 1, i))

count_in = 0
while len(events) > 0:
    time, event_type, i = heapq.heappop(events)
    if event_type == 1:
        lines.append(i)
    else:
        count_in -= kyaku[i][2]

    while len(lines) > 0:
        if count_in + kyaku[lines[0]][2] <= K:
            in_i = lines.popleft()
            count_in += kyaku[in_i][2]
            print(time)

            heapq.heappush(events, (time + kyaku[in_i][1], 0, in_i))

        else:
            break
