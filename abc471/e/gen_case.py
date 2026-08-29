import random

N = random.randint(1, 10)
K = random.randint(1, N)

print(N, K)
print(*[random.randint(1, 100) for _ in range(N)])
