import itertools
import more_itertools

N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    sides[a].append(b)
    sides[b].append(a)

def divide_group(N: int):
    d = list(range(N))
    l = list(more_itertools.powerset(d))[1:]

    for i in range(1, N + 1):
        for ans in itertools.combinations(l, i):
            check = []
            for x in ans:
                check.extend(x)

            if len(check) == N and sorted(check) == d:
                yield ans

for x in divide_group(N):
    print(x)
