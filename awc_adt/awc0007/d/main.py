N, A, B = [int(x) for x in input().split()]
ads_T = [[int(x) - 1 for x in input().split()] for _ in range(A)]
ads_A = [[int(x) - 1 for x in input().split()] for _ in range(B)]

pos_T = [[0] * (N + 1) for _ in range(N + 1)]
for r1, c1, r2, c2 in ads_T:
    pos_T[r1][c1] += 1
    pos_T[r1][c2 + 1] -= 1
    pos_T[r2 + 1][c1] -= 1
    pos_T[r2 + 1][c2 + 1] += 1

for i in range(1, N + 1):
    for j in range(N + 1):
        pos_T[i][j] += pos_T[i - 1][j]

for j in range(1, N + 1):
    for i in range(N + 1):
        pos_T[i][j] += pos_T[i][j - 1]

pos_A = [[0] * (N + 1) for _ in range(N + 1)]
for r1, c1, r2, c2 in ads_A:
    pos_A[r1][c1] += 1
    pos_A[r1][c2 + 1] -= 1
    pos_A[r2 + 1][c1] -= 1
    pos_A[r2 + 1][c2 + 1] += 1

for i in range(1, N + 1):
    for j in range(N + 1):
        pos_A[i][j] += pos_A[i - 1][j]

for j in range(1, N + 1):
    for i in range(N + 1):
        pos_A[i][j] += pos_A[i][j - 1]


ans = 0
for i in range(N):
    for j in range(N):
        if pos_A[i][j] >= 1 and pos_T[i][j] >= 1:
            ans += 1

print(ans)
