def solve():
    N = int(input())
    items = [[int(x) for x in input().split()] for _ in range(N)]

    if N == 1:
        return items[0][0]

    benefits = [x[0] - x[1] for x in items]
    coupon_price = min(x[0] for x in items)
    cp_index = min([i for i in range(N) if items[i][0] == coupon_price], key=lambda i: items[i][0] - items[i][1])
    benefits.sort()
    normal_sum = sum(x[0] for x in items)

    ans = normal_sum - sum(benefits[(N + 1) // 2 :])

    NN = N - 1
    benefits.remove(items[cp_index][0] - items[cp_index][1])
    benefits_sum = [sum(benefits)]
    for x in benefits:
        benefits_sum.append(benefits_sum[-1] - x)

    for init_coupon in range(1, N):
        now_ans = coupon_price * (init_coupon - 1) + normal_sum
        if NN % 2 != 0:
            slides = (init_coupon + 1) // 2
            start = (NN + 1) // 2 - slides
        else:
            slides = init_coupon // 2
            start = NN // 2 - slides

        start = max(0, start)

        now_ans -= benefits_sum[start]
        ans = min(ans, now_ans)

    return ans


T = int(input())
for _ in range(T):
    print(solve())
