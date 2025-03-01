N = int(input())

ans = [["-"] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if min(i, N - i - 1, j, N - j - 1) % 2 == 0:
            ans[i][j] = "#"
        else:
            ans[i][j] = "."

print("\n".join(["".join(x) for x in ans]))
