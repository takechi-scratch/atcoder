# まだできてない

N, M = [int(x) for x in input().split()]
chocolates = [[int(x) for x in input().split()] for _ in range(N)]

chocolates.sort(key=lambda x: (x[0] - x[1], x[0]))

choco_res = []
for start in range(M):
    now = start
    tickets = start
    for a, b in chocolates:
        if tickets < a:
            continue

        exchange_count = (tickets - a) // (a - b) + 1
        now += b * exchange_count
        tickets += (b - a) * exchange_count

    choco_res.append(now)
