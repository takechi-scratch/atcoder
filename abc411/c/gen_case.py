import random

N = random.randint(1, 10)
Q = random.randint(1, 10)
A = [random.randint(1, N) for _ in range(Q)]

print(N, Q)
print(*A)
