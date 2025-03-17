N, D = [int(x) for x in input().split()]
T = []
L = []
for _ in range(N):
    t, l = [int(x) for x in input().split()]
    T.append(t)
    L.append(l)

# iを長さの増加分として、それぞれシミュレート
for i in range(1, D + 1):
    ans = -1
    for j in range(N):
        # max関数で、これまでの値と今見ている重さでベストを記録し直す
        ans = max(ans, T[j] * (L[j] + i))

    print(ans)
