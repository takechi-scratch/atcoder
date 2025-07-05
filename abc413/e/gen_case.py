import random
print(5)
for _ in range(5):
    N = 3
    P = list(range(1, 2 ** N + 1))
    random.shuffle(P)
    print(N)
    print(*P)
