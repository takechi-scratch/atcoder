# 解法を思いつくのに15分くらいかかった...

N, M = [int(x) for x in input().split()]
# 食材ごとに出てくる料理をリストで記録
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
    # 克服した食材が出てくる料理でループ
    for food in ingredients[x]:
        left_nigate[food] -= 1
        if left_nigate[food] == 0:
            ans += 1

    print(ans)
