from bisect import bisect_left

N, Q = [int(x) for x in input().split()]

border = list(range(1, N + 1))
color = list(range(N))  # カラーはあえて0から
color_counts = [1] * N

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 2:
        print(color_counts[query[1] - 1])
        continue

    # 以下、色を変える場合
    x, c = query[1:]
    c -= 1
    changing_group = bisect_left(border, x)
    color_counts[color[changing_group]] -= border[changing_group] - border[changing_group - 1]
    color[changing_group] = c
    color_counts[c] += border[changing_group] - border[changing_group - 1]

    # 隣が同じ色だったらボーダーを寄せる
    # 右側
    check = changing_group + 1
    while check < N and color[check] == c:
        border[check - 1] = border[check]
        color[check] = c
        check += 1

    # 左側
    check = changing_group - 1
    while -1 < check and color[check] == c:
        border[check] = border[check - 1]
        color[check] = c
        check -= 1


