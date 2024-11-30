from bisect import bisect_right

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

sushi_lvs = [A[0]]
for i in range(1, N):
    if sushi_lvs[-1] < A[i]:
        sushi_lvs.append(sushi_lvs[-1])
    else:
        sushi_lvs.append(A[i])

sushi_lvs.reverse()

for j in range(M):
    place = bisect_right(sushi_lvs, B[j])
    if place == 0:
        print(-1)
    else:
        print(N - place + 1)
