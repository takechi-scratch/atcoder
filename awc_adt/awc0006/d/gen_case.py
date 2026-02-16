import random

N = random.randrange(1, 100)
M = random.randrange(1, 10)

print(N, M)

for _ in range(M):
    l, r = random.randrange(1, N + 1), random.randrange(1, N + 1)
    print(min(l, r), max(l, r))
