from random import randint

N, K = randint(1, 4), randint(1, 4)
NK = N * K

sides = set()
while len(sides) < NK - 1:
    u, v = randint(1, NK), randint(1, NK)
    if u != v and (u, v) not in sides and (v, u) not in sides:
        sides.add((u, v))

print(N, K)
print("\n".join([f"{x[0]} {x[1]}" for x in sides]))
