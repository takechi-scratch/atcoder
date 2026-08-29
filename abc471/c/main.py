from sortedcontainers import SortedSet

N = int(input())
A = [int(x) for x in input().split()]
SA = SortedSet(A + [10**18, -(10**18)])
ans = 0
now = 0

while len(SA) > 2:
    next_pos = SA.bisect_right(now)

    if abs(now - SA[next_pos - 1]) <= abs(now - SA[next_pos]):
        ans += abs(now - SA[next_pos - 1])
        now = SA[next_pos - 1]
    else:
        ans += abs(now - SA[next_pos])
        now = SA[next_pos]

    SA.discard(now)

print(ans)
