import sys
input = sys.stdin.readline

N, M = [int(x) for x in input().split()]

if N > 2000:
    print(-1)
    exit()

bunnies = [[int(x) for x in input().split()] for _ in range(N)]
T = [int(x) for x in input().split()]
T_counts = [0] * N
for i in T:
    T_counts[i - 1] += 1

for i, x in enumerate(T_counts):
    if x == 0:
        continue

    root_pos = bunnies[i]
    for j, now_pos in enumerate(bunnies):
        if i == j:
            continue
        dx = now_pos[0] - root_pos[0]
        sdx = dx // abs(dx) if abs(dx) > 0 else 0
        dy = now_pos[1] - root_pos[1]
        sdy = dy // abs(dy) if abs(dy) > 0 else 0
        if abs(dx) == abs(dy):
            bunnies[j][0] += x * sdx
            bunnies[j][1] += x * sdy
        elif abs(dx) > abs(dy):
            bunnies[j][0] += (x * 2) * sdx
        else:
            bunnies[j][1] += (x * 2) * sdy

print("\n".join([f"{x[0]} {x[1]}" for x in bunnies]))
