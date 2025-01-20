# https://atcoder.jp/contests/abc309/tasks/abc309_b
N = int(input())
A = [list(input()) for _ in range(N)]
ans = [[y for y in x] for x in A]

for i in range(1, N - 1):
    ans[0][i] = A[0][i - 1]
    ans[N - 1][i] = A[N - 1][i + 1]
    ans[i][0] = A[i + 1][0]
    ans[i][N - 1] = A[i - 1][N - 1]

ans[0][0] = A[1][0]
ans[0][N - 1] = A[0][N - 2]
ans[N - 1][0] = A[N - 1][1]
ans[N - 1][N - 1] = A[N - 2][N - 1]

for x in ans:
    print(*x, sep="")
