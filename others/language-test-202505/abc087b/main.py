A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for a in range(A + 1):
    for b in range(B + 1):
        if 0 <= (X - (a * 500 + b * 100)) // 50 <= C:
            ans += 1

print(ans)
