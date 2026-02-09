from sortedcontainers import SortedList

N, K = [int(x) for x in input().split()]
H = [int(x) for x in input().split()]

sl = SortedList(H[:K])
ans = sl[-1] - sl[0]
for i in range(N - K):
    sl.add(H[i + K])
    sl.discard(H[i])
    ans = max(ans, sl[-1] - sl[0])

print(ans)
