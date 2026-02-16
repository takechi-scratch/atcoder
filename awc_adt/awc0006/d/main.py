from sortedcontainers import SortedList

N, M = [int(x) for x in input().split()]

k = [[int(x) for x in input().split()] for _ in range(M)]
sk = SortedList([[x[0], x[1] + 1] for x in k])

max_r = 0
i = 0
while i < len(sk):
    l, r = sk[i]
    if r <= max_r:
        sk.pop(i)
    elif i + 1 < len(sk) and l == sk[i + 1][0] and r < sk[i + 1][1]:
        sk.pop(i)
    else:
        max_r = max(max_r, r)
        i += 1

max_r = 1
ans = 0
ok = True
for i in range(len(sk)):
    l, r = sk[i]
    if max_r < l:
        ok = False
        break
    if max_r > N:
        break

    if i + 1 < len(sk) and sk[i + 1][0] <= max_r:
        continue
    if r <= max_r:
        continue

    ans += 1
    max_r = r

if ok and max_r > N:
    print(ans)
else:
    print(-1)
