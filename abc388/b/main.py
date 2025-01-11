N, D = [int(x) for x in input().split()]
T = []
L = []
for _ in range(N):
    t, l = [int(x) for x in input().split()]
    T.append(t)
    L.append(l)

for i in range(1, D + 1):
    ans = -1
    for j in range(N):
        ans = max(ans, T[j] * (L[j] + i))

    print(ans)
