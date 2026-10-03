from collections import defaultdict

N, Q = [int(x) for x in input().split()]
appends = [[] for _ in range(N)]
deletes = [[] for _ in range(N)]


for _ in range(Q):
    l, r, x = [int(x) for x in input().split()]
    appends[l - 1].append(x)
    deletes[r - 1].append(x)

C = defaultdict(int)
count = 0


def replace(i: int, dist: int):
    global count

    if C[i] != 0:
        count -= 1

    C[i] += dist

    if C[i] != 0:
        count += 1


ans = []
for i in range(N):
    for x in appends[i]:
        replace(x, 1)

    ans.append(count)

    for x in deletes[i]:
        replace(x, -1)

print(*ans)
