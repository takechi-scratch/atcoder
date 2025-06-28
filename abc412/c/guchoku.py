# 誤解法

from itertools import permutations

def solve(N: int, S: list[int]):
    start = S[0]
    goal = S[-1]
    S = S[1: N - 1]

    if len(S) == 0:
        if start * 2 >= goal:
            return 2
        else:
            return -1


    ans = 10 ** 18
    for now_S in permutations(S, len(S)):
        now = start
        for i, x in enumerate(now_S):
            if now * 2 < x:
                break

            now = x

            if now * 2 >= goal:
                ans = min(ans, i + 3)
                break

    if ans == 10 ** 18:
        return -1
    else:
        return ans



T = int(input())
for _ in range(T):
    N = int(input())
    S = [int(x) for x in input().split()]
    print(solve(N, S))
