N, M = [int(x) for x in input().split()]

k = [[int(x) for x in input().split()] for _ in range(M)]
k = [[x[0], x[1] + 1] for x in k]
k.sort()
use = [True] * M

max_r = 0
i = 0
for i in range(M):
    l, r = k[i]
    if r <= max_r:
        use[i] = False
    elif i + 1 < len(k) and l == k[i + 1][0] and r < k[i + 1][1]:
        use[i] = False
    else:
        max_r = max(max_r, r)

    i += 1

k = [x for i, x in enumerate(k) if use[i]]

max_r = 1
ans = 0
ok = True
for i in range(len(k)):
    l, r = k[i]
    if max_r < l:
        ok = False
        break
    if max_r > N:
        break

    if i + 1 < len(k) and k[i + 1][0] <= max_r:
        continue
    if r <= max_r:
        continue

    ans += 1
    max_r = r

if ok and max_r > N:
    print(ans)
else:
    print(-1)
