N, Q = [int(x) for x in input().split()]
A = [int(x) - 1 for x in input().split()]

is_black = [0] * N
for x in A:
    is_black[x] = 1 - is_black[x]

    ans = 0
    before = False
    for i, x in enumerate(is_black):
        if not before and x == 1:
            ans += 1
            before = True

        if x == 0:
            before = False

    print(ans)
