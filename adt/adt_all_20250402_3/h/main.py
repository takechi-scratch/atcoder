import heapq

N, M = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]

queue = []
heapq.heapify(queue)

for i in range(N):
    heapq.heappush(queue, (P[i], i, 0))


ans = 0
while M > 0:
    price, index, num = heapq.heappop(queue)

    if M < price:
        break

    M -= price
    ans += 1
    num += 1

    heapq.heappush(queue, ((num * 2 + 1) * P[index], index, num))

print(ans)
