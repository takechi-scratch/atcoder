from collections import deque

Q = int(input())
queue = deque()

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        c, x = query[1:]
        queue.append((x, c))

    if query[0] == 2:
        now = query[1]
        ans = 0

        while now > 0:
            x, c = queue.popleft()
            now -= c
            ans += x * c

        if now < 0:
            queue.appendleft((x, -now))
            ans -= x * -now

        print(ans)
