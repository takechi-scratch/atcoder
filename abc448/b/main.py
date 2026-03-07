N, M = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

ans = 0
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    a -= 1
    if b >= C[a]:
        ans += C[a]
        C[a] = 0
    else:
        ans += b
        C[a] -= b

print(ans)
