from sortedcontainers import SortedList

N = int(input())
A = [int(x) for x in input().split()]
last_cangive = SortedList([])
ans = []

for i in range(N):
    get_stones = len(last_cangive) - last_cangive.bisect_left(i + 1)
    last_cangive.add(i + 1 + A[i] + get_stones)
    ans.append(max(0, A[i] + get_stones - (N - i - 1)))

print(*ans)
