def solve(N: int, S: list[int]):
    # 0をすべて1にすることだけ考える

    if all(x == 0 for x in S):
        return N
    elif all(x == 1 for x in S):
        return 0

    now = 0
    count = 0
    katamari = [[], []]
    for x in S:
        if x == now:
            count += 1
        else:
            katamari[now].append(count)
            now = 1 - now
            count = 1
    katamari[now].append(count)

    return sum(katamari[0]) + (sum(katamari[1]) - max(katamari[1])) * 2


T = int(input())
for _ in range(T):
    N = int(input())
    S = [int(x) for x in list(input())]

    ans = solve(N, S)
    ans2 = solve(N, [1 - x for x in S])
    print(min(ans, ans2))
