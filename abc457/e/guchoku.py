N, M = [int(x) for x in input().split()]
clothes = [[int(x) - 1 for x in input().split()] for _ in range(M)]

ok_comb = set()
for i in range(M):
    for j in range(i + 1, M):
        l1, r1 = clothes[i]
        l2, r2 = clothes[j]
        if min(r1, r2) < max(l1, l2):
            continue
        ok_comb.add((min(l1, l2), max(r1, r2)))

Q = int(input())
for _ in range(Q):
    s, t = [int(x) - 1 for x in input().split()]
    if (s, t) in ok_comb:
        print("Yes")
    else:
        print("No")
