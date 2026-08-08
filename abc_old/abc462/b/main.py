N = int(input())
to = [set(int(x) - 1 for x in input().split()[1:]) for _ in range(N)]

for x in range(N):
    count = []
    for fr in range(N):
        if x == fr:
            continue
        if x in to[fr]:
            count.append(fr + 1)

    print(len(count), *count, sep=" ")
