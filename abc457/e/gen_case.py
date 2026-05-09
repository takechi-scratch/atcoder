import random

N = random.randint(1, 500)
M = random.randint(1, 500)
print(N, M)
for _ in range(M):
    l = random.randint(1, N)
    print(l, random.randint(l, N))

print((N + 1) * N // 2)
for i in range(N):
    for j in range(i, N):
        print(i + 1, j + 1)
