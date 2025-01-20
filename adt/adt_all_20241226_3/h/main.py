from collections import deque

N, M = [int(x) for x in input().split()]
trains = [[] for _ in range(N)]
sides = [[] for _ in range(N)]
ans = [10 * 18] * N

for i in range(M):
    l, d, k, c, A, B = [int(x) for x in input().split()]
    trains[B].append((l, d, k, c))
    sides[B].append(A)
    # lスタート, d間隔, k本数, c所要時間, Aから B

bfs = deque()

for i in range(len(trains[N])):
    l, d, k, c = trains[N][i]
    A = sides[N][i]

    l + d
    bfs.append((trains[i]))

while len(bfs) > 0:
    last_time = 0
