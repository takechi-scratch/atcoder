H, W = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(H)]

row_sum = [sum(x) for x in grid]
col_sum = [sum([grid[i][j] for i in range(H)]) for j in range(W)]

ans = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans[i][j] = row_sum[i] + col_sum[j] - grid[i][j]

print(*[" ".join([str(y) for y in x]) for x in ans], sep="\n")
