from sortedcontainers import SortedList

N, D = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

sl = SortedList([-(10**18), 10**18, A[0]])

right = 1
ans = 0
for left in range(N):
    # rightをできるだけ右に
    while right < N:
        next_add = A[right]
        pos = sl.bisect_left(next_add)
        if abs(sl[pos - 1] - next_add) < D or abs(sl[pos] - next_add) < D:
            break

        sl.add(next_add)
        right += 1

    ans += right - left

    # leftを1だけ右に
    sl.remove(A[left])

print(ans)
