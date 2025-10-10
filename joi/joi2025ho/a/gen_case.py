import random

N = random.randint(2, 7)
A = [random.randrange(5) + 1 for _ in range(N)]
B = [random.randrange(5) + 1 for _ in range(N)]
B[0] = A[0]

print(N)
print(*A)
print(*B)
