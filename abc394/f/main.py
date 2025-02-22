# 途中

N = int(input())
sides = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = [int(x) - 1 for x in input().split()]
    sides[a].append(b)
    sides[b].append(a)

ans = -1
for root in range(N):
    deep_used = False
    now_cut = 0
    for one in sides[root]:
        if len(sides[one]) == 1:
            continue

        deep_used = True

        for two in sides[one]:
            if two == root:
                continue

            if len(sides[two]) == 1:
                now_cut += 1
                continue

            for three in sides[two]:
                if three == one:
                    continue

                if len(sides[three]) == 1:
                    now_cut += 1
                    continue

                for four in sides[three]:
                    if four == two:
                        continue
                    now_cut += len(sides[four]) - 1

    if deep_used:
        if ans == -1:
            ans = N - now_cut
        else:
            ans = min(ans, N - now_cut)

print(ans)
