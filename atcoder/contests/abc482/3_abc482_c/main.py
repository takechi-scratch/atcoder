from bisect import bisect_left

H, W, N, Q = [int(x) for x in input().split()]

R = []
C = []
for _ in range(N):
    r, c = [int(x) for x in input().split()]
    R.append(r)
    C.append(c)

R.sort()
C.sort()

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        print(bisect_left(R, query[2] + 1) - bisect_left(R, query[1]))
    else:
        print(bisect_left(C, query[2] + 1) - bisect_left(C, query[1]))
