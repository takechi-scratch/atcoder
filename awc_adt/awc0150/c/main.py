N, M = [int(x) for x in input().split()]
P = [int(x) - 1 for x in input().split()]

parkings = [False] * M
ans = 0
for x in P:
    now = x
    while now < M:
        if not parkings[now]:
            parkings[now] = True
            ans += 1
            break
        now += 1

print(ans)
