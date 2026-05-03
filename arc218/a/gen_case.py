import random

N, M = random.randint(5, 7), random.randint(5, 7)
A = [[random.randint(1, N * M) for _ in range(M)] for _ in range(N)]

print(N, M)
for x in A:
    print(*x)
