H, W, Q = [int(x) for x in input().split()]
query = [[[(-1, "A")] for _ in range(W)] for _ in range(H)]
for i in range(Q):
    r, c, x = input().split()
    r = int(r) - 1
    c = int(c) - 1
    query[r][c].append((i, x))

ans = [[""] * W for _ in range(H)]
for ij in range(H + W - 2, -1, -1):
    for i in range(min(ij, H - 1), -1, -1):
        j = ij - i
        if j >= W:
            break

        now_query = max(query[i][j])
        ans[i][j] = now_query[1]
        if i > 0:
            query[i - 1][j].append((now_query[0], now_query[1]))
        if j > 0:
            query[i][j - 1].append((now_query[0], now_query[1]))
        if i > 0 and j > 0:
            query[i - 1][j - 1].append((now_query[0], now_query[1]))

for i in range(H):
    print("".join(ans[i]))
