import random

N = random.randint(1, 100)
print(N)
print(*[random.randint(0, 1000) for _ in range(N)])
