import random
N = 10
K = 5
P = 5

print(N, K, P)
for _ in range(N):
    print(random.randint(1, 100), *[random.randint(1, P) for _ in range(K)])
