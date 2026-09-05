# N = int(input())
N, K, Q = [int(x) for x in input().split()]
images = [list(input()) for _ in range(N)]

for _ in range(Q):
    r, c = [int(x) - 1 for x in input().split()]
    after = [[None] * K for _ in range(K)]

    for i in range(K):
        for j in range(K):
            after[j][K - i - 1] = images[r + i][c + j]

    for i in range(K):
        for j in range(K):
            images[r + i][c + j] = after[i][j]

for x in images:
    print(*x, sep="")
