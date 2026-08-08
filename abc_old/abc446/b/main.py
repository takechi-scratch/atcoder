N, M = [int(x) for x in input().split()]
orders = []
for _ in range(N):
    input()
    orders.append([int(x) for x in input().split()])

left = set(range(1, M + 1))
ans = []
for i, order in enumerate(orders):
    for x in order:
        if x in left:
            ans.append(x)
            left.remove(x)
            break
    else:
        ans.append(0)

print(*ans, sep="\n")
