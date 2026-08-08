from atcoder.dsu import DSU

H, W = [int(x) for x in input().split()]
C = [list(input()) for _ in range(H)]
uf = DSU(H * W)


def get_id(i, j):
    return i * W + j


def get_pos(x):
    return x // W, x % W


for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            continue

        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            if not (0 <= i + di < H and 0 <= j + dj < W):
                continue
            if C[i + di][j + dj] == ".":
                uf.merge(get_id(i, j), get_id(i + di, j + dj))


ng_list = (
    list(range(W))
    + [i * W for i in range(H)]
    + [H * W - i for i in range(1, W + 1)]
    + [i * W + W - 1 for i in range(H)]
)

ng_list = set(ng_list)
ans = 0
for group in uf.groups():
    if len(group) == 1:
        i, j = get_pos(group[0])
        if C[i][j] == "#":
            continue

    for x in group:
        if x in ng_list:
            break
    else:
        ans += 1

print(ans)
