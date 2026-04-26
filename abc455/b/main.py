H, W = [int(x) for x in input().split()]
grid = [list(input()) for _ in range(H)]

ans = 0
for si in range(H):
    for sj in range(W):
        for ei in range(si, H):
            for ej in range(sj, W):
                i_size = ei - si + 1
                j_size = ej - sj + 1
                ok = True
                for i in range(i_size):
                    for j in range(j_size):
                        if grid[si + i][sj + j] != grid[si + i_size - i - 1][sj + j_size - j - 1]:
                            ok = False

                if ok:
                    ans += 1

print(ans)
