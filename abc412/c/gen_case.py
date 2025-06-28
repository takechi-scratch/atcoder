import random

print(5)
for _ in range(5):
    N = random.randint(2, 10)
    print(N)
    print(*[random.randint(1, 10 ** 5) for _ in range(N)])
