import random

N = random.randint(1, 100)

x = []
while len(x) < N:
    x.append(-1)

random.shuffle(x)

for i, y in enumerate(x):
    if y == -1:
        x[i] = random.randrange(i + 1)

print(N)
for y in x:
    print(y, random.randint(1, 100))
