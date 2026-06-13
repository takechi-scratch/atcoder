def solve(S: list[str], K: int):
    def count_replace(start: int, X: list[str] = S):
        if not 0 <= start < len(X) - 2:
            return -1
        return int(X[start] != "A") + int(X[start + 1] != "B") + int(X[start + 2] != "C")

    N = len(S)
    if N < K * 3:
        return -1

    S = [x if x in "ABC" else "." for x in S]
    minimum_replace = []
    destruction_count = []
    for i in range(N - 2):
        minimum_replace.append(count_replace(i))
        destruction_count.append(
            (count_replace(i - 2) == 0)
            + (count_replace(i - 1) == 0)
            + (count_replace(i) == 0)
            + (count_replace(i + 1) == 0)
            + (count_replace(i + 2) == 0)
        )

    return "".join(S)


T = int(input())
for _ in range(T):
    S = list(input())
    K = int(input())
    print(solve(S, K))
