import heapq

N, K, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

A.sort()
start = A[-1] * K

p_queue = [(-start, N - 1, [0] * (N - 1) + [K])]

ans = []
for _ in range(X):
    now, i, counts = heapq.heappop(p_queue)
    now = 0 - now
    ans.append(now)

    for next_i in range(i, 0, -1):
        if counts[next_i] == 0:
            continue

        next_counts: list[int] = counts.copy()
        next_counts[next_i] -= 1
        next_counts[next_i - 1] += 1
        heapq.heappush(p_queue, (-(now - A[next_i] + A[next_i - 1]), next_i, next_counts))

print("\n".join(str(x) for x in ans))
