N, M = [int(x) for x in input().split()]
ingredients: list[list] = [[] for _ in range(N)]
left_nigate = []
for i in range(M):
    q = [int(x) for x in input().split()]
    left_nigate.append(q[0])
    for x in q[1:]:
        ingredients[x - 1].append(i)

B = [int(x) - 1 for x in input().split()]
ans = 0
for x in B:
    for food in ingredients[x]:
        left_nigate[food] -= 1
        if left_nigate[food] == 0:
            ans += 1

    print(ans)
