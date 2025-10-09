import sys

input = sys.stdin.readline

N, Q = [int(x) for x in input().split()]
S = list(input())


def get_dist(x, y):
    m1, m2 = max(x, y), min(x, y)
    return min(m1 - m2, m2 + N - m1)


prints = []
for _ in range(Q):
    x, y = [int(x) - 1 for x in input().split()]
    if S[x] == S[y]:
        ans = 1
    elif S[(x - 1) % N] != S[x] or S[(x + 1) % N] != S[x] or S[(y - 1) % N] != S[y] or S[(y + 1) % N] != S[y]:
        ans = 2
    else:
        ans = 3

    prints.append(min(ans, get_dist(x, y)))

print(*prints, sep="\n")
