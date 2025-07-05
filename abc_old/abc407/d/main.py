import sys
sys.setrecursionlimit(10**7)

H, W = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(H)]

def calc_score(A_put: list[list[bool]]):
    ans = 0

    for i in range(H):
        for j in range(W):
            if not A_put[i][j]:
                ans ^= A[i][j]

    return ans

def solve(A_put: list[list[bool]], ok: int):
    ans = calc_score(A_put)
    if ok >= H * W:
        return ans

    i, j = ok // W, ok % W
    ans = max(ans, solve(A_put, ok + 1))

    if 0 <= i < H - 1 and not A_put[i][j] and not A_put[i + 1][j]:
        A_put[i][j] = True
        A_put[i + 1][j] = True
        ans = max(ans, solve(A_put, ok + 1))
        A_put[i][j] = False
        A_put[i + 1][j] = False

    if 0 <= j < W - 1 and not A_put[i][j] and not A_put[i][j + 1]:
        A_put[i][j] = True
        A_put[i][j + 1] = True
        ans = max(ans, solve(A_put, ok + 1))
        A_put[i][j] = False
        A_put[i][j + 1] = False

    return ans

print(solve([[False] * W for _ in range(H)], 0))
