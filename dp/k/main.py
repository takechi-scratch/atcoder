N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

able_to_win = [None] * (K + 1)
able_to_win[0] = False

for i in range(1, K + 1):
    ok = False
    for x in A:
        if x > i:
            continue
        if not able_to_win[i - x]:
            ok = True
            break

    able_to_win[i] = ok

print("First" if able_to_win[K] else "Second")
# print(able_to_win)
