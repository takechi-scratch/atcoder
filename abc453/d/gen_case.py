import random

H = random.randint(2, 5)
W = random.randint(2, 5)

grid = [["."] * W for _ in range(H)]

si, sj = random.randrange(H), random.randrange(W)
grid[si][sj] = "S"
gi, gj = random.randrange(H), random.randrange(W)
while (si, sj) == (gi, gj):
    gi, gj = random.randrange(H), random.randrange(W)
grid[gi][gj] = "G"

for _ in range(H * W - 2):
    k = random.choice(["o", "x"])
    gi, gj = random.randrange(H), random.randrange(W)
    while grid[gi][gj] == "S" or grid[gi][gj] == "G":
        gi, gj = random.randrange(H), random.randrange(W)

    grid[gi][gj] = k

print(H, W)
for l in grid:
    print(*l, sep="")
