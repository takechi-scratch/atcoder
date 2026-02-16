from math import ceil

N, M, D = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

print(sum([max(0, ceil((x - M) / D)) for x in T]))
