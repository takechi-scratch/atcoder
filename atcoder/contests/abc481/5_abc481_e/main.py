from fractions import Fraction


def solve(N: int, pos: list[list[int]]):
    katamuki = []
    positives = set()
    # negatives = set()

    zero_y = None
    for x, y in pos:
        if x == 0:
            zero_y = y
        else:
            now = Fraction(y, x)
            if x > 0:
                positives.add(now)
            else:
                pass
                # negatives.add(now)

            katamuki.append(now)

    katamuki.sort()

    now_ans = len(positives) + int(zero_y is not None and zero_y > 0)
    ans = max(now_ans, N - now_ans)

    for x in katamuki:
        if x in positives:
            now_ans -= 1
        else:
            now_ans += 1

        ans = max(ans, now_ans, N - now_ans)

    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    pos = [[int(x) for x in input().split()] for _ in range(N)]
    print(solve(N, pos))
