# WA解法。cubesが巨大になる場合がある。

from math import ceil
N = int(input())

cubes = []

for i in range(1, ceil(N ** (1 / 3))):
    cubes.append(i ** 3)

C = len(cubes)
left, right = 0, 0
for right in range(1, C):
    if cubes[right] - cubes[left] == N:
        print(cubes[right], cubes[left])
        exit()

    while left == right and cubes[right] - cubes[left] > N:
        left += 1

print(-1)
