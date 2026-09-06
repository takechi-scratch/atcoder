import math

X = int(input())
if X == 0:
    print("T")

init_ans = [[0, 0], [1, 1]]

for i in range(2, 601):
    now_ans = None
    now_score = 10**18

    for d1 in range(1, math.isqrt(i) + 1):
        if i % d1 != 0:
            continue

        d2 = i // d1

        if d1 + d2 <= now_score:
            now_ans = [d1, d2]
            now_score = d1 + d2

    init_ans.append(now_ans)

ans = ["", "ARC"]
for i in range(2, 601):
    now_ans = "AR" * init_ans[i][0] + "CR" * (init_ans[i][1] - 1) + "C"
    now_score = len(now_ans)

    for a1 in range(1, i // 2 + 1):
        x1 = init_ans[a1][:]
        x2 = init_ans[i - a1][:]

        if min(x1[0], x2[0]) < min(x1[1], x2[1]):
            x1[0], x1[1] = x1[1], x1[0]
            x2[0], x2[1] = x2[1], x2[0]

        if x1[0] > x2[0]:
            x1, x2 = x2, x1

        ans_candidate = (x1[0], x1[1], x2[0] - x1[0], x2[1])

        if sum(ans_candidate) * 2 - 1 <= now_score:
            now_ans = (
                "AR" * ans_candidate[0]
                + "CR" * ans_candidate[1]
                + "AR" * ans_candidate[2]
                + "CR" * (ans_candidate[3] - 1)
                + "C"
            )
            now_score = len(now_ans)

    # for a1 in range(1, i // 2 + 1):
    #     for a2 in range(a1, i - a1):
    #         a3 = i - a1 - a2
    #         if not (a1 <= a2 <= a3):
    #             continue

    #         x = [init_ans[a1][:], init_ans[a2][:], init_ans[a3][:]]

    #         if min(x[j][0] for j in range(3)) < min(x[j][1] for j in range(3)):
    #             for j in range(3):
    #                 x[j].reverse()

    #         x.sort(key=lambda y: y[0])

    #         ans_candidate = (x[0][0], x[0][1], x[1][0] - x[0][0], x[1][1], x[2][0] - x[1][0] - x[0][0], x[2][1])

    #         if sum(ans_candidate) * 2 - 1 <= now_score:
    #             now_ans = (
    #                 "AR" * ans_candidate[0]
    #                 + "CR" * ans_candidate[1]
    #                 + "AR" * ans_candidate[2]
    #                 + "CR" * ans_candidate[3]
    #                 + "AR" * ans_candidate[4]
    #                 + "CR" * (ans_candidate[5] - 1)
    #                 + "C"
    #             )
    #             now_score = len(now_ans)

    ans.append(now_ans)


for i in range(2, 601):
    now_ans = ans[i]
    now_score = len(now_ans)

    for a1 in range(1, i):
        if len(ans[a1]) + len(ans[i - a1]) <= now_score:
            now_ans = ans[a1] + ans[i - a1]
            now_score = len(now_ans)

    ans[i] = now_ans

assert all(len(x) <= 100 for x in ans)


print(ans[X])

for x in range(1, 600):
    if len(ans[x]) > 100:
        print(x)
        print(len(x), "len")
        continue

    now = ans[x]
    for _ in range(x):
        after = now.replace("ARC", "CRA", 1)
        if now == after:
            break
        now = after

    else:
        if now == now.replace("ARC", "CRA", 1):
            continue

    print(x)
    print(ans[x])
