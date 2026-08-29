import random

N = random.randint(1, 7)
K = random.randint(1, N)

print(N, K)
print(*["".join([str(random.randint(0, 10)) for _ in range(random.randint(1, 10))]) for _ in range(N)], sep="\n")
