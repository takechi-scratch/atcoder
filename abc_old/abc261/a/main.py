L1, R1, L2, R2 = [int(x) for x in input().split()]
ans = 0
for i in range(100):
    ans += L1 <= i + 0.5 <= R1 and L2 <= i + 0.5 <= R2

print(ans)
