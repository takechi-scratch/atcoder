import random
N = random.randint(2, 20)
A = [random.randint(1, 10 ** 9) for _ in range(N)]
A.sort()

print(N)
print(*A)
