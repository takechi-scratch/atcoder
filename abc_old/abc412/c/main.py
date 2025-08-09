def solve(N: int, S: list[int]):
    start = S[0]
    goal = S[-1]
    S = S[1: N - 1]
    S.sort()

    if start * 2 >= goal:
        return 2

    ans = [start]
    for i, x in enumerate(S):
        if x >= goal:
            break

        if i < len(S) - 1 and S[i + 1] <= ans[-1] * 2:
            continue

        if x > ans[-1] * 2:
            return -1

        ans.append(x)

    if goal <= ans[-1] * 2:
        if ans[-2] * 2 >= goal:
            return len(ans)
        else:
            return len(ans) + 1
    else:
        return -1



T = int(input())
for _ in range(T):
    N = int(input())
    S = [int(x) for x in input().split()]
    print(solve(N, S))
