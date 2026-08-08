import random

N = random.randint(1, 8)
Q = random.randint(1, 20)

print(N, Q)
for _ in range(Q):
    l = random.randrange(1, N + 1)
    r = random.randrange(l, N + 1)
    print(l, r, random.randint(1, 50))
