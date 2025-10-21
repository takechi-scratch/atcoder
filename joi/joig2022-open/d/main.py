def solve(H, W, N, stbs):
    dxs = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    dys = [1, 0, -1, 1, 0, -1, 1, 0, -1]

    def count_stbs(x: int, y: int) -> int:
        ans = 0
        for dx, dy in zip(dxs, dys):
            if (x + dx, y + dy) in stbs:
                ans += stbs[(x + dx, y + dy)]

        return ans

    ans = 0
    for x, y in stbs.keys():
        for dx, dy in zip(dxs, dys):
            now_ans = count_stbs(x + dx, y + dy)
            if now_ans > ans:
                ans = now_ans

    print(int(ans))


def solve2(H, W, N, stbs):
    dxs = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    dys = [1, 0, -1, 1, 0, -1, 1, 0, -1]

    def count_stbs(x: int, y: int) -> int:
        ans = 0
        for dx, dy in zip(dxs, dys):
            if (x + dx) * 10000 + y + dy in stbs:
                ans += stbs[(x + dx) * 10000 + y + dy]

        return ans

    ans = 0
    for raw in stbs.keys():
        x, y = raw // 10000, raw % 10000
        for dx, dy in zip(dxs, dys):
            now_ans = count_stbs(x + dx, y + dy)
            if now_ans > ans:
                ans = now_ans

    print(int(ans))


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    H, W = [int(x) for x in input().split()]
    N = int(input())
    stbs = defaultdict(int)

    if H <= 1000 and W <= 1000:
        for _ in range(N):
            stb = tuple(int(x) for x in input().split())
            stbs[stb[0] * 10000 + stb[1]] += 1
        solve2(H, W, N, stbs)
    else:
        for _ in range(N):
            stb = tuple(int(x) for x in input().split())
            stbs[stb] += 1
        solve(H, W, N, stbs)


main()
