import random
Q = random.randint(1, 20)
print(Q)

for _ in range(Q):
    T = random.randint(1, 2)
    S = "".join([chr(random.randint(97, 122)) for _ in range(random.randint(1, 10))])
    print(T, S)
