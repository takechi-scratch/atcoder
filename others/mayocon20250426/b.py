from collections import defaultdict

N, Q = [int(x) for x in input().split()]
follows = defaultdict(set)

for _ in range(Q):
    t, a, b = [int(x) - 1 for x in input().split()]
    if t == 0:
        follows[a].add(b)

    elif t == 1:
        follows[a].discard(b)

    elif t == 2:
        print("Yes" if b in follows[a] and a in follows[b] else "No")
