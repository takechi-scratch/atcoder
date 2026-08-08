from collections import Counter

N = int(input())
S = list(input())


def pair_equal_count(a: str, b: str):
    scores = [0]
    for x in S:
        now_score = scores[-1]
        if x == a:
            now_score += 1
        elif x == b:
            now_score -= 1

        scores.append(now_score)

    ans = 0
    sc = Counter(scores)
    for _, value in sc.items():
        ans += value * (value - 1) // 2

    return ans


def triple_equal_count():
    scores = [(0, 0)]
    for x in S:
        nb, nc = scores[-1]
        if x == "A":
            nb -= 1
            nc -= 1
        elif x == "B":
            nb += 1
        else:
            nc += 1

        scores.append((nb, nc))

    ans = 0
    sc = Counter(scores)
    for _, value in sc.items():
        ans += value * (value - 1) // 2

    return ans


ans = (
    N * (N + 1) // 2
    - pair_equal_count("A", "B")
    - pair_equal_count("B", "C")
    - pair_equal_count("C", "A")
    + 2 * triple_equal_count()
)

print(ans)
