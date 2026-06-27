from collections import defaultdict

N, M = [int(x) for x in input().split()]
birds = [[int(x) for x in input().split()] for _ in range(N)]

decrease_list = [[] for _ in range(M + 1)]
increase_list = [[] for _ in range(M + 1)]

for a, d, b in birds:
    decrease_list[d - 1].append(a)
    increase_list[d - 1].append(b)

birds_count = defaultdict(int)
for x in birds:
    birds_count[x[0]] += 1

ans = len(set(x[0] for x in birds))
for i in range(M):
    for x in decrease_list[i]:
        birds_count[x] -= 1
        if birds_count[x] == 0:
            ans -= 1

    for x in increase_list[i]:
        birds_count[x] += 1
        if birds_count[x] == 1:
            ans += 1

    print(ans)
