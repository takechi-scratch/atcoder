N, Q = [int(x) for x in input().split()]
L = [10**18] + [int(x) for x in input().split()]
R = [int(x) for x in input().split()] + [10**18]

right_min = 10**18
for i in range(N):
    right_min = min(right_min, R[i])
    if i == 0:
        continue
    R[i] = min(R[i], L[i] + right_min)

left_min = 10**18
for i in range(N - 1, -1, -1):
    left_min = min(left_min, L[i])
    if i == N - 1:
        continue
    L[i] = min(L[i], R[i] + left_min)


for _ in range(Q):
    s, t = [int(x) - 1 for x in input().split()]
    if s < t:
        print(R[s])
    else:
        print(L[s])
