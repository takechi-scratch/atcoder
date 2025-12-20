def solve(N: int, tonakais: list[list[int]]):
    now = sum(x[1] for x in tonakais)
    decrease = [sum(x) for x in tonakais]
    decrease.sort()

    for i, x in enumerate(decrease):
        now -= x
        if now < 0:
            return i

    return N


T = int(input())
for _ in range(T):
    N = int(input())
    tonakais = [[int(x) for x in input().split()] for _ in range(N)]
    print(solve(N, tonakais))
