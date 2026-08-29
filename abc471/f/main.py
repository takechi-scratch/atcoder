N, K = [int(x) for x in input().split()]
S = [input() for _ in range(N)]


def remove_lezero(s: str):
    ss = list(reversed(s))
    while len(ss) > 0 and ss[-1] == "0":
        ss.pop()
    if len(ss) == 0:
        return "0"
    else:
        return "".join(reversed(ss))


def solve1(S: list[str]):
    S.sort(key=lambda x: (len(x), tuple(x)))
    use = S[-K + 1 :]
    use.sort(key=tuple, reverse=True)
    S = S[: N - K + 1]

    S.sort(key=lambda x: (len(remove_lezero(x)), tuple(remove_lezero(x))))
    first = S.pop()

    return first + "".join(use)


def solve2(S: list[str]):
    S.sort(key=lambda x: (len(x), tuple(x)))
    use = S[-K:]
    use.sort(key=lambda x: (len(remove_lezero(x)), tuple(remove_lezero(x))))
    first = use.pop()

    use.sort(key=tuple, reverse=True)

    return first + "".join(use)


def solve3(S: list[str]):
    S.sort(key=lambda x: (len(x), tuple(x)))
    use = S[-K:]
    use.sort(key=lambda x: tuple(remove_lezero(x)))
    first = use.pop()

    use.sort(key=tuple, reverse=True)

    return first + "".join(use)


if N == 1:
    print(remove_lezero(max(S, key=lambda x: (len(x), tuple(x)))))
else:
    ans1 = remove_lezero(solve1(S[:]))
    ans2 = remove_lezero(solve2(S[:]))
    ans3 = remove_lezero(solve3(S[:]))
    print(remove_lezero(max(ans1, ans2, ans3, key=lambda x: (len(x), tuple(x)))))
