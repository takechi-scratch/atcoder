from sortedcontainers import SortedSet

N, A = [int(x) for x in input().split()]
S = list(input())

reverses = SortedSet(i for i in range(N) if S[i] == "#")
reverses.add(-1)
reverses.add(N)
default = {-1, N}

ans = 0
now = A - 1
while len(reverses) > 2:
    next_i = reverses.bisect_right(now)
    ans += reverses[next_i] - now
    now = reverses[next_i]
    if reverses[next_i] not in default:
        reverses.pop(next_i)

    if len(reverses) <= 2:
        break

    next_i = reverses.bisect_left(now) - 1
    ans += now - reverses[next_i]
    now = reverses[next_i]
    if reverses[next_i] not in default:
        reverses.pop(next_i)

print(ans)
