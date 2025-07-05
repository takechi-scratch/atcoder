N, M = [int(x) for x in input().split()]
events = []
for _ in range(M):
  L, R = [int(x) for x in input().split()]
  events.append((L - 1, 1))
  events.append((R, -1))

events.append((N, 0))
events.sort()
ans = 10 ** 18
now = 0
before = 0
for x, diff in events:
  if before != x:
    ans = min(ans, now)

  now += diff
  before = x

print(ans)
