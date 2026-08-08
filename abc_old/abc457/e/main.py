from collections import Counter
from bisect import bisect_left, bisect_right

N, M = [int(x) for x in input().split()]
clothes = [[int(x) - 1 for x in input().split()] for _ in range(M)]
clothes_counter = Counter([(x[0], x[1]) for x in clothes])
clothes = list(set((x[0], x[1]) for x in clothes))
M = len(clothes)

raw_start_clothes = [[] for _ in range(N)]
raw_end_clothes = [[] for _ in range(N)]
for i, x in enumerate(clothes):
    l, r = x
    raw_start_clothes[l].append((r, i))
    raw_end_clothes[r].append((l, i))

start_clothes = []
start_clothes_id = []
end_clothes = []
end_clothes_id = []

for i in range(N):
    raw_start_clothes[i].sort()
    start_clothes.append([x[0] for x in raw_start_clothes[i]])
    start_clothes_id.append([x[1] for x in raw_start_clothes[i]])

    raw_end_clothes[i].sort()
    end_clothes.append([x[0] for x in raw_end_clothes[i]])
    end_clothes_id.append([x[1] for x in raw_end_clothes[i]])

shortest_end = [start_clothes[i][0] if len(start_clothes[i]) > 0 else 10**18 for i in range(N)]
for i in range(N - 2, -1, -1):
    shortest_end[i] = min(shortest_end[i], shortest_end[i + 1])

Q = int(input())
for _ in range(Q):
    s, t = [int(x) - 1 for x in input().split()]

    if len(start_clothes[s]) == 0 or len(end_clothes[t]) == 0:
        print("No")
        continue

    reach_end_i = bisect_right(start_clothes[s], t) - 1
    if reach_end_i == -1:
        print("No")
        continue

    reach_start_i = bisect_left(end_clothes[t], s)
    if reach_start_i == len(end_clothes[t]):
        print("No")
        continue

    if start_clothes[s][reach_end_i] == t:
        now_id = start_clothes_id[s][reach_end_i]
        if clothes_counter[(clothes[now_id][0], clothes[now_id][1])] > 1:
            print("Yes")
            continue

        if shortest_end[s] < t:
            print("Yes")
            continue

    ok = False
    for dl in range(2):
        for dr in range(2):
            if not (0 <= reach_start_i + dl < len(end_clothes[t]) and 0 <= reach_end_i - dr < len(start_clothes[s])):
                continue

            if end_clothes_id[t][reach_start_i + dl] == start_clothes_id[s][reach_end_i - dr]:
                continue

            if end_clothes[t][reach_start_i + dl] <= start_clothes[s][reach_end_i - dr] + 1:
                if not ok:
                    print("Yes")
                ok = True
                break

    if not ok:
        print("No")
