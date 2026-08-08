T = int(input())
for _ in range(T):
    X, Y, K = [int(x) for x in input().split()]
    ans = 0
    while X != Y:
        if X > Y:
            X //= K
        else:
            Y //= K
        ans += 1

    print(ans)
