from sortedcontainers import SortedList

N, Q = [int(x) for x in input().split()]
horses = [[int(x) for x in input().split()] for _ in range(N)]
horse_scores = SortedList([x[0] for x in horses])
tidy_horses = sum([x for x in horses if x[1] == 2])

for _ in range(Q):
    w, x, y = [int(x) for x in input().split()]
    horses[w - 1] = [x, y]
