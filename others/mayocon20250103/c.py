H, W, K = [int(x) for x in input().split()]
grid = []
save_nokori = 0
for _ in range(H):
    grid.append(list(input()))
    save_nokori += grid[-1].count("#")

ans = 0
for raw_x in range(2 ** H):
    x_choices = list(bin(raw_x)[2:])
    x_choices = ["0"] * (H - len(x_choices)) + x_choices
    save_x_nokori = save_nokori
    for x in range(H):
        if x_choices[x] == "0":
            continue
        save_x_nokori -= grid[x].count("#")


    for raw_y in range(2 ** W):
        nokori = save_x_nokori
        y_choices = list(bin(raw_y)[2:])
        y_choices = ["0"] * (W - len(y_choices)) + y_choices
        for y in range(W):
            if y_choices[y] == "0":
                continue

            for temp_x in range(H):
                if grid[temp_x][y] == "#" and x_choices[temp_x] != "1":
                    nokori -= 1

        if nokori == K:
            ans += 1

print(ans)

