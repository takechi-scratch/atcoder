N, M = [int(x) for x in input().split()]
sides = [[] for _ in range(N)]
for num in range(M):
    i, j = [int(x) - 1 for x in input().split()]
    sides[i].append(j)
    sides[j].append(i)
    if num == 0:
        s1, s2 = i, j

candidates = set()


def solve(parent: int):
    for i in range(N):
        if i == parent:
            continue

        if len(sides[parent]) + len(sides[i]) - sides[i].count(parent) == M:
            candidates.add((min(i, parent), max(i, parent)))


solve(s1)
solve(s2)
print(len(candidates))
