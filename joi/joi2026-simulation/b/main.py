from bisect import bisect_right

N, K = [int(x) for x in input().split()]
monsters = [[int(x) for x in input().split()] for _ in range(N)]
X = [-10 ** 18] + [int(x) for x in input().split()] + [10 ** 18]

X.sort()
X_active = [False] * (K + 2)
monsters.sort(key=lambda x: x[0])

ans = 0
for a, h in monsters:
    near = bisect_right(X, a)
    move_cost = min(a - X[near - 1], X[near] - a)
    if move_cost < h:
        if a - X[near - 1] < X[near] - a:
            X_active[near - 1] = True
        elif a - X[near - 1] > X[near] - a:
            X_active[near] = True
        else:
            if not X_active[near - 1]:
                X_active[near] = True

        ans += move_cost
    else:
        ans += h

ans += X_active.count(True)
print(ans)
