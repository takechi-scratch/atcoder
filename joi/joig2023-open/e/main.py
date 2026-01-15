from atcoder.dsu import DSU

H, W = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(H)]


def grid_id(i: int, j: int):
    return i * W + j


left_uf = DSU(H * W)
left_section_counts = []

counts = 0
for j in range(W):
    counts += H

    if j > 0:
        for i in range(H):
            if grid[i][j] == grid[i][j - 1] and not left_uf.same(grid_id(i, j), grid_id(i, j - 1)):
                counts -= 1
                left_uf.merge(grid_id(i, j), grid_id(i, j - 1))

    for i in range(1, H):
        if grid[i][j] == grid[i - 1][j] and not left_uf.same(grid_id(i, j), grid_id(i - 1, j)):
            counts -= 1
            left_uf.merge(grid_id(i, j), grid_id(i - 1, j))

    left_section_counts.append(counts)


right_uf = DSU(H * W)
right_section_counts = []

counts = 0
for j in range(W - 1, -1, -1):
    counts += H

    if j < W - 1:
        for i in range(H):
            if grid[i][j] == grid[i][j + 1] and not right_uf.same(grid_id(i, j), grid_id(i, j + 1)):
                counts -= 1
                right_uf.merge(grid_id(i, j), grid_id(i, j + 1))

    for i in range(1, H):
        if grid[i][j] == grid[i - 1][j] and not right_uf.same(grid_id(i, j), grid_id(i - 1, j)):
            counts -= 1
            right_uf.merge(grid_id(i, j), grid_id(i - 1, j))

    right_section_counts.append(counts)


ans = 10**18
for i in range(W - 1):
    ans = min(ans, left_section_counts[i] + right_section_counts[W - i - 2])

print(ans)
