import random

N = random.randint(1, 9)
M = min(random.randint(1, 9), N)

print(N, M)
print(*[random.randint(1, N) for _ in range(N)])
print(*[random.randint(1, 1000) for _ in range(N)])
print(*[random.randint(1, N) for _ in range(M)])
print(*[random.randint(1, 1000) for _ in range(M)])
