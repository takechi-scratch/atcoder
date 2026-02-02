from math import log2, floor
from itertools import product
from sys import exit

N = int(input())
A = [23 - int(x) for x in input().split()]
A.reverse()

if any(x < 0 for x in A):
    print("No")
    exit()

print("Yes")
LAST_ANS = [1] * 100

def div(now: int, last_max: int = None) -> list[list[int]]:
    if last_max is None:
        last_max = now
    if now < 0:
        return []
    if now == 0:
        return [[]]
    res = []
    for pick in range(1, last_max + 1):
        for next_res in div(now - pick, min(last_max, pick)):
            res.append([pick] + next_res)
    return res

def include(parent: list, children: list) -> bool:
    for c in children:
        if parent.count(c) < children.count(c):
            return False

    return True

if N <= 2:
    LAST_ANS = A

elif N == 3:
    if A[2] - A[1] == A[0]:
        LAST_ANS = [A[0], A[1]]
    else:
        LAST_ANS = A

elif all(A[i] + 1 == A[i + 1] for i in range(N - 1)) and A[0] == 0:
    ans_len = floor(log2(A[-1])) + 1
    LAST_ANS = [2 ** i for i in range(ans_len)]


elif A[-1] <= 11:
    comb_sets = [div(x) for x in A]
    for sets in product(*comb_sets):
        for i in range(len(sets) - 1):
            if not include(sets[i + 1], sets[i]):
                break
        else:
            if len(LAST_ANS) > len(sets[-1]):
                LAST_ANS = list(sets[-1])


if LAST_ANS[0] == 0:
    LAST_ANS.pop(0)

if len(LAST_ANS) <= 81:
    print(len(LAST_ANS))
    print(*LAST_ANS)
else:
    raise RuntimeError
