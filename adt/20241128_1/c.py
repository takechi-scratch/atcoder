# https://atcoder.jp/contests/abc312/tasks/abc312_b

N, M = [int(x) for x in input().split()]
grid = []
for _ in range(N):
    grid.append(list(input()))

for i in range(N-8):
    for j in range(M-8):
        score = 0
        for i_add in range(4):
            for j_add in range(4):

                if i_add == 3 or j_add == 3:
                    if grid[i + i_add][j + j_add] == ".":
                        score += 1
                else:
                    if grid[i + i_add][j + j_add] == "#":
                        score += 1

        if score < 16:
            continue

        score = 0
        for i_add in range(4):
            for j_add in range(4):

                if i_add == 3 or j_add == 3:
                    if grid[i + 8 - i_add][j + 8 - j_add] == ".":
                        score += 1
                else:
                    if grid[i + 8 - i_add][j + 8 - j_add] == "#":
                        score += 1

        if score < 16:
            continue

        print(i + 1, j + 1)
