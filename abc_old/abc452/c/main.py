N = int(input())
pos = [[int(x) for x in input().split()] for _ in range(N)]

M = int(input())
candidates = [input() for _ in range(M)]

available_chars = [set() for _ in range(N)]
for i in range(N):
    for j in range(M):
        if len(candidates[j]) != pos[i][0]:
            continue

        available_chars[i].add(candidates[j][pos[i][1] - 1])

for x in candidates:
    if len(x) != N:
        print("No")
        continue

    for i, ok in enumerate(available_chars):
        if x[i] not in ok:
            print("No")
            break
    else:
        print("Yes")
