import time

start = time.time()

import random
import math

N = int(input())
pos = [[int(x) for x in input().split()] for _ in range(N)]


route = list(range(N))
random.shuffle(route)


def dist(i, j):
    x1, y1 = pos[route[i]]
    x2, y2 = pos[route[j]]
    return abs(x1 - x2) + abs(y1 - y2)


t = 100000000.0
now_ans = 0
for i in range(N - 1):
    now_ans += dist(i, i + 1)

while time.time() - start < 1.8:
    i = random.randrange(1, N - 1)
    j = random.randrange(2, N)
    if j + 1 < N - 1:
        score = (dist(i - 1, j) + dist(test, test + 2)) - (dist(test - 1, test) + dist(test + 1, test + 2))
    else:
        score = dist(test - 1, test + 1) - dist(test - 1, test)

    if score <= 0 or random.random() <= math.e ** (-score / t):
        route[test], route[test + 1] = route[test + 1], route[test]
        now_ans += score

    if now_ans < 10**10:
        break

    t *= 0.9999932

else:
    pass
    # print(now_ans)
    # raise RuntimeError()


print(" ".join([str(x + 1) for x in route]))
print(now_ans)
