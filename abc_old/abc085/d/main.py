import heapq
from math import ceil

N, H = [int(x) for x in input().split()]
katanas = [tuple(int(x) for x in input().split()) for _ in range(N)]

queue = []
for x in katanas:
    queue.append((-x[0], True))
    queue.append((-x[1], False))

heapq.heapify(queue)
ans = 0
while True:
    if H <= 0:
        break

    damage, reuseable = heapq.heappop(queue)
    damage = 0 - damage
    if not reuseable:
        H -= damage
        ans += 1

    else:
        ans += ceil(H / damage)
        break

print(ans)
