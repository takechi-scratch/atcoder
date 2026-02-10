N, M = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
R = [int(x) for x in input().split()]

C.sort()
R.sort(reverse=True)
ans = 0
for tg in C:
    while len(R) > 0:
        if R[-1] < tg:
            R.pop()
        else:
            break

    if len(R) == 0:
        break

    ans += 1
    R.pop()

print(ans)
