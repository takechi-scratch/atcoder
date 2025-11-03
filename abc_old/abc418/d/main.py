N = int(input())
T = [int(x) for x in list(input())]

ans = 0
last_ends = [0, 0]

for x in T:
    next_last_ends = [0, 0]
    if x == 0:
        next_last_ends[0] += last_ends[1] # 10
        next_last_ends[1] += last_ends[0] # 00
    else:
        next_last_ends[0] += last_ends[0] # 01
        next_last_ends[1] += last_ends[1] # 11

    next_last_ends[x] += 1
    ans += next_last_ends[1]
    last_ends = next_last_ends

print(ans)
