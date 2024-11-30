import sys
sys.setrecursionlimit(10**7)

N, M = [int(x) for x in input().split()]

base = []
for i in range(N):
    base.append(1 + 10 * i)

plus_max = M - base[-1]
ans = []

def generate(base, free):
    if free == 0:
        ans.append([str(x) for x in base])
        return

    free_to = M - 10 * (free - 1)
    if free == N:
        start = base[-1 * free]
    else:
        start = base[-1 * free - 1] + 10
    for i in range(start, free_to + 1):
        if free == 1:
            generate(base[:-1 * free] + [i], free - 1)
        else:
            generate(base[:-1 * free] + [i] + base[-1 * free + 1:], free - 1)

generate(base, N)
print(len(ans))
print("\n".join([" ".join(x) for x in ans]))
