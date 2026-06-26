from bisect import bisect_left

N, K = [int(x) for x in input().split()]
clothes = [[int(x) for x in input().split()] for _ in range(N)]
clothes.sort()
clothes_lefts = [x[0] for x in clothes]
clothes_min_rights = [x[1] for x in clothes]
for i in range(N - 1, 0, -1):
    clothes_min_rights[i - 1] = min(clothes_min_rights[i - 1], clothes_min_rights[i])


ok, ng = 0, 10**10
while ng - ok > 1:
    dist = (ok + ng) // 2
    picked = 0
    now_r = -(10**18)
    while True:
        next_i = bisect_left(clothes_lefts, now_r + dist)
        if next_i >= N:
            break

        picked += 1
        now_r = clothes_min_rights[next_i]

    if picked >= K:
        ok = dist
    else:
        ng = dist

if ok <= 0:
    print(-1)
else:
    print(ok)
