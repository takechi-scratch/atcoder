import random

print(10)
for _ in range(10):
    N = random.randint(2, 10)
    A = [random.choice([random.randint(1, 100), random.randint(-100, -1)]) for _ in range(N)]
    print(N)
    print(*A)
