X, Y, L, R, A, B = [int(x) for x in input().split()]

ans = 0
for i in range(A, B):
    if L <= i < R:
        ans += X
    else:
        ans += Y

print(ans)
