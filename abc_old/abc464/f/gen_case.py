import random

N = random.randint(1, 10)
A = [random.randint(1, 20) for _ in range(N)]
X = random.randint(1, sum(A))

print(N, X)
print(*A)
