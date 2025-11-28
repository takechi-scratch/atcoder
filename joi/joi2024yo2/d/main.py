N = int(input())
assert N <= 50

A = [list(input()) for _ in range(N)]


def check(r, si, sj):
    for d in range(r + 1):
        target = A[si - d][sj]
        for x in range(d):
            if A[si - x][sj - d + x] != target:
                return False
            if A[si + d - x][sj - x] != target:
                return False
            if A[si + x][sj + d - x] != target:
                return False
            if A[si - d + x][sj + x] != target:
                return False

    return True


ans = 0
for r in range((N - 1) // 2 + 1):
    for si in range(r, N - r):
        for sj in range(r, N - r):
            if check(r, si, sj):
                ans = 2 * r * (r + 1) + 1

print(ans)
