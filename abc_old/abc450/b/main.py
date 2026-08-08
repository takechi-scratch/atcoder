N = int(input())
C = [[int(x) for x in input().split()] for _ in range(N - 1)]

ok = False
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if C[i][k - i - 1] > C[i][j - i - 1] + C[j][k - j - 1]:
                ok = True
                break

print("Yes" if ok else "No")
