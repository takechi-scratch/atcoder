# Codonでも実行可能な記述

from itertools import permutations
from sys import exit

N = int(input())
A = [int(x) for x in input().split()]

for P in permutations(range(1, N + 1), N):
    for i in range(N):
        if A[i] != -1 and P[i] != A[i]:
            break

    else:
        print("Yes")
        print(" ".join([str(x) for x in P]))
        exit()

print("No")
