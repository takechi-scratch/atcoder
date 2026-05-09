from math import ceil

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


def ceil(a, b):
    return (a + b - 1) // b


ok, ng = 0, 9 * 10**18
while ng - ok > 1:
    now = (ok + ng) // 2
    now_count = 0
    for i, x in enumerate(A, start=1):
        if x >= now:
            continue

        now_count += ceil(now - x, i)
    if now_count <= K:
        ok = now
    else:
        ng = now

print(ok)
