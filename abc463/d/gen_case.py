import random

N = random.randint(2, 12)
K = random.randint(2, N)
clothes = []
for _ in range(N):
    l = random.randint(0, 29)
    r = random.randint(l + 1, 30)
    clothes.append((l, r))

print(N, K)
print(*[f"{x[0]} {x[1]}" for x in clothes], sep="\n")
