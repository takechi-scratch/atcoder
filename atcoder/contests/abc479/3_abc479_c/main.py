from itertools import product

N, W = [int(x) for x in input().split()]
dishes = [[int(x) for x in input().split()] for _ in range(N)]

ans = 0
for comb in product(range(2), repeat=N):
    now_w = 0
    now_ans = 0
    for i in range(N):
        if comb[i] == 0:
            continue

        now_ans += dishes[i][0]
        now_w += dishes[i][1]

    if now_w <= W:
        ans = max(now_ans, ans)

print(ans)
