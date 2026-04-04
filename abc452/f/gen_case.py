import random

N = random.randrange(1, 20)
K = random.randrange(N * (N - 1) // 2 + 1)
P = list(range(N))
random.shuffle(P)

print(N, K)
print(*P)
