# https://atcoder.jp/contests/abc225/tasks/abc225_d

from collections import deque

N, Q = [int(x) for x in input().split()]
front_trains = [-1] * N
after_trains = [-1] * N

for _ in range(Q):
    query = [int(x) - 1 for x in input().split()]
    if query[0] == 0:
        x, y = query[1], query[2]

        front_trains[y] = x
        after_trains[x] = y

    if query[0] == 1:
        x, y = query[1], query[2]

        front_trains[y] = -1
        after_trains[x] = -1

    if query[0] == 2:
        x = query[1]

        ans = deque([x + 1])

        now = x
        while True:
            now = after_trains[now]
            if now == -1:
                break
            ans.append(now + 1)

        now = x
        while True:
            now = front_trains[now]
            if now == -1:
                break
            ans.appendleft(now + 1)

        print(len(ans), *ans)
