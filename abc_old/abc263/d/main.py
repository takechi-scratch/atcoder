N, L, R = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


L_best = [0] * N

toku_sum = 0
for i in range(N):
    toku_sum += L - A[i]
    if toku_sum <= L_best[i - 1]:
        L_best[i] = toku_sum
    else:
        L_best[i] = L_best[i - 1]


R_best = [0] * N

toku_sum = 0
for i in range(N):
    toku_sum += R - A[N - i - 1]
    if toku_sum <= R_best[i - 1]:
        R_best[i] = toku_sum
    else:
        R_best[i] = R_best[i - 1]

L_best.insert(0, 0)
R_best.insert(0, 0)
sum_A = sum(A)
ans = sum_A
for i in range(N + 1):
    ans = min(ans, sum_A + L_best[i] + R_best[N - i])

print(ans)
