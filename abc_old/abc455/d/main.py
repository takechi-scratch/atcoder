N, Q = [int(x) for x in input().split()]
below_card_nums = list(range(N))
connect_above = [-1] * N
connect_below = [-i - 1 for i in range(N)]

for _ in range(Q):
    c, p = [int(x) - 1 for x in input().split()]
    c_below = connect_below[c]
    if c_below < 0:
        below_card_nums[-c_below - 1] = -1
    else:
        connect_above[c_below] = -1
    connect_below[c] = p
    assert connect_above[p] == -1
    connect_above[p] = c

ans = []
for i in range(N):
    if below_card_nums[i] == -1:
        ans.append(0)
        continue

    count = 0
    now = below_card_nums[i]
    while True:
        count += 1
        if connect_above[now] == -1:
            break
        now = connect_above[now]

    ans.append(count)

print(*ans)
