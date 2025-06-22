N, Q = [int(x) for x in input().split()]
A = [int(x) - 1 + 1 for x in input().split()]

is_black = [0] * (N + 2)
ans = 0

for i, x in enumerate(A):
    is_black[x] = 1 - is_black[x]

    if is_black[x]:
        if is_black[x - 1] == is_black[x + 1] == 0:
            ans += 1
        elif is_black[x - 1] == is_black[x + 1] == 1:
            ans -= 1

    else:
        if is_black[x - 1] == is_black[x + 1] == 0:
            ans -= 1
        elif is_black[x - 1] == is_black[x + 1] == 1:
            # なぜか+2にしていた…
            ans += 1

    print(ans)
