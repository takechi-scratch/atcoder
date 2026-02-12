grid = []
for _ in range(8):
    grid.append(list(input()))

ans = 0
for i in range(8):
    for j in range(8):
        if grid[i][j] == "#":
            continue

        available = True
        for ti in range(8):
            if i != ti and grid[ti][j] == "#":
                available = False

        for tj in range(8):
            if j != tj and grid[i][tj] == "#":
                available = False

        ans += available

print(ans)
