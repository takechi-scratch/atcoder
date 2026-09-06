def solve(N: int, A: list[int]) -> bool:
    A.sort()
    oshiyose = [0]
    now = 0

    for x in A:
        if x == now:
            oshiyose[-1] += 1
        else:
            oshiyose.append(x - now)
            oshiyose.append(1)
            now = x

    if oshiyose[0] == 0:
        oshiyose.pop(0)

    can_keep = [x > 1 for x in oshiyose]
    ans = False

    for x in reversed(can_keep):
        if x:
            ans = True
        else:
            ans = not ans

    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    print("Alice" if solve(N, A) else "Bob")
