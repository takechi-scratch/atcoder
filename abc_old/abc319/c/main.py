from math import factorial
from itertools import permutations

C = [[int(x) for x in input().split()] for _ in range(3)]
ans = 0

def zannen(C1, C2, appears, i):
    return appears[C1] < i and appears[C2] < i and C[C1[0]][C1[1]] == C[C2[0]][C2[1]]

for perm in permutations(((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)), 9):
    appears = {}
    for i, x in enumerate(perm):
        appears[x] = i

    ok = True
    for i in range(9):
        match perm[i]:
            case (0, 0):
                if zannen((0, 1), (0, 2), appears, i) or zannen((1, 0), (2, 0), appears, i) or zannen((1, 1), (2, 2), appears, i):
                    ok = False
                    break

            case (0, 1):
                if zannen((0, 0), (0, 2), appears, i) or zannen((1, 1), (2, 1), appears, i):
                    ok = False
                    break

            case (0, 2):
                if zannen((0, 1), (0, 0), appears, i) or zannen((1, 2), (2, 2), appears, i) or zannen((1, 1), (2, 0), appears, i):
                    ok = False
                    break

            case (1, 0):
                if zannen((0, 0), (2, 0), appears, i) or zannen((1, 1), (1, 2), appears, i):
                    ok = False
                    break

            case (1, 1):
                if zannen((1, 0), (1, 2), appears, i) or zannen((0, 1), (2, 1), appears, i) or zannen((0, 0), (2, 2), appears, i) or zannen((2, 0), (0, 2), appears, i):
                    ok = False
                    break

            case (1, 2):
                if zannen((0, 2), (2, 2), appears, i) or zannen((1, 1), (1, 0), appears, i):
                    ok = False
                    break

            case (2, 0):
                if zannen((1, 0), (0, 0), appears, i) or zannen((2, 1), (2, 2), appears, i) or zannen((1, 1), (0, 2), appears, i):
                    ok = False
                    break

            case (2, 1):
                if zannen((0, 1), (1, 1), appears, i) or zannen((2, 0), (2, 2), appears, i):
                    ok = False
                    break

            case (2, 2):
                if zannen((1, 2), (0, 2), appears, i) or zannen((2, 1), (2, 0), appears, i) or zannen((1, 1), (0, 0), appears, i):
                    ok = False
                    break

    if ok:
        ans += 1

print(ans / factorial(9))
