from itertools import combinations

N = int(input())
N2 = 16
A = [[-1] * N2 for _ in range(N2)]
for i in range(N * 2 - 1):
    for j, x in enumerate((int(x) for x in input().split())):
        A[i][i + j + 1] = x

B = [[[[-1 for _ in range(N2)] for _ in range(N2)] for _ in range(N2)] for _ in range(N2)]
for x1, x2, x3, x4 in combinations(range(N2), 4):
    B[x1][x2][x3][x4] = max(
        A[x1][x2] ^ A[x3][x4],
        A[x1][x3] ^ A[x2][x4],
        A[x1][x4] ^ A[x2][x3],
    )

ans = -1
for x1, x2, x3, x4 in combinations(range(N2), 4):
    a = set(range(N2)) - {x1, x2, x3, x4}
    y1, y2, y3, y4 = sorted(a)
    ans = max(ans, B[x1][x2][x3][x4] ^ B[y1][y2][y3][y4])
