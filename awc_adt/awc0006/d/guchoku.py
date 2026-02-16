from itertools import product

N, M = [int(x) for x in input().split()]

k = [[int(x) for x in input().split()] for _ in range(M)]

ans = 10**18
for choice in product(range(2), repeat=M):
    test = set()
    for c, x in zip(choice, k):
        if c == 0:
            continue
        test |= set(range(x[0], x[1] + 1))
    if len(test) == N:
        ans = min(ans, len([x for x in choice if x == 1]))

if ans == 10**18:
    print(-1)
else:
    print(ans)
